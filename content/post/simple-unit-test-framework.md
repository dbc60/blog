---
title: "A Simple Unit Test Framework"
date: 2026-03-29T05:26:46-04:00
2026: ["03"]
tags: [c, testing]
# Featured image (optional)
featuredImage: "images/banners/chloe-and-laptop.jpg"
featuredImageDescription: "Chloe comfort test"
featuredCopyright: "copyright © 2026 Douglas Cuthbertson"
---
Over the past few years, I created [Basic Unit Test](https://github.com/dbc60/but) (BUT), the simplest possible unit-test framework for C code that I could think of. I had one important criterion for it, and that was the code for the test driver had to be separate from the code for the test suites. I didn't want to tie each test suite to a specific driver. I wanted the flexibility to write different drivers, possibly with different features, to be able to load and run the test suites.
<!--more-->
{{< table_of_contents >}}
## Overview
Any unit-test framework needs to define its test suites, test cases, and a way to detect, collect, and report errors. Let's start with how test cases are defined and then see how they are collected into a test suite.

## Test Cases
A test case needs a test function and optionally a setup and cleanup function. I found it convenient to define them with a macro and a typedef:

```c
#define BUT_TEST_FN(NAME) void NAME(struct BUTTestCase *btc)
typedef BUT_TEST_FN(but_test_fn);

#define BUT_SETUP_FN(NAME) void NAME(struct BUTTestCase *btc)
typedef BUT_SETUP_FN(but_setup_fn);

#define BUT_CLEANUP_FN(NAME) void NAME(struct BUTTestCase *btc)
typedef BUT_CLEANUP_FN(but_cleanup_fn);
```

On the surface, it looks a bit silly to have three separate macros for these function signatures, because they are all identical. For small test suites, it doesn't matter much, but for a large enough test suite the names signal intent. I never wrote a "large enough" test suite with BUT, so I just used `BUT_TEST_FN`. Here's one that ignores the test case and throws an exception:

```c
BUT_TEST_FN(test_failure) {
    BUT_UNUSED(btc);
    BUT_THROW(but_expected_failure);
}
```

The test case itself has a name and a pointer for each of these functions.

```c
struct BUTTestCase {
    char           *name;
    but_setup_fn   *setup;
    but_test_fn    *test;
    but_cleanup_fn *cleanup;
};
typedef struct BUTTestCase BUTTestCase;
```

The name and test function cannot be NULL, but if the test doesn't need any setup or cleanup, then those fields can be NULL.

I made a few macros to make it easier to define test cases. Here the author of the test case can simply give the test case a name and the three pointers to functions:

```c
#define BUT_CASE(NAME, TEST, SETUP, CLEANUP) \
    static BUTTestCase TEST##_case = {       \
        .name    = NAME,                     \
        .setup   = SETUP,                    \
        .test    = TEST,                     \
        .cleanup = CLEANUP,                  \
    }
```

For example:

```c
BUT_CASE("Expected Test Failure", test_failure, NULL, NULL);
```

defines a test case called "Expected Test Failure" where the test just throws an exception. No setup or cleanup functions are needed. There is a `BUT_CASE_NAME` variant that comes in handy, because it separates the name of the test case from the name of the test function. For example:

```c
BUT_CASE_NAME("Expected Test Setup Failure", setup_failure, NULL, test_failure, NULL);
BUT_CASE_NAME("Expected Test Cleanup Failure", cleanup_failure, NULL, NULL,
              test_failure);
```

I also provide macros that define a test case and allow you to define the test function in place, both with and without setup and cleanup functions.

```c
#define BUT_TEST(NAME, TEST)                              \
    static void TEST(void);                               \
    static void TEST##_wrapper(struct BUTTestCase *btc) { \
        BUT_UNUSED(btc);                                  \
        TEST();                                           \
    }                                                     \
    static BUTTestCase TEST##_case = {                    \
        .name    = NAME,                                  \
        .setup   = NULL,                                  \
        .test    = TEST##_wrapper,                        \
        .cleanup = NULL,                                  \
    };                                                    \
    static void TEST(void)
```

There are several variants that enable users to define their own struct with `BUTTestCase` as its first element and have fields for test-specific data.

## Test Suites
A test suite needs only a name or ID and a set of test cases. Here's its definition:

```c
struct BUTTestSuite {
    char         *name;
    u32           count;
    BUTTestCase **test_cases;
};
typedef struct BUTTestSuite BUTTestSuite;
```

The driver will need to retrieve the test suite from a DLL, so I defined some macros to make it easy to define test suites:

```c
// a macro to define a common field for test-case structs to embed a BUTTestCase.
#define BUT_EMBED_CASE BUTTestCase btc

// Auto-register test cases in a suite
#define BUT_SUITE_BEGIN(NAME)      static BUTTestCase *NAME##_cases[] = {
#define BUT_SUITE_ADD(TC)          &TC##_case,
#define BUT_SUITE_ADD_EMBEDDED(TC) &TC##_case.btc,
#define BUT_SUITE_END              }
```

 and ensure the retrieval function is also defined:
```c
#define BUT_GET_TEST_SUITE(NAME, SUITE)                                  \
    static BUTTestSuite SUITE##_ts                                       \
        = {.name       = NAME,                                           \
           .count      = sizeof SUITE##_cases / sizeof SUITE##_cases[0], \
           .test_cases = SUITE##_cases};                                 \
    DLL_SPEC_EXPORT BUTTestSuite *get_test_suite(void) {                 \
        return &SUITE##_ts;                                              \
    }
```

I also defined a function pointer that the driver uses to cast a void pointer to the right type, `typedef BUTTestSuite *(*but_get_test_suite)();`, though, I wish I had named it `get_test_suite_fn` to convey its type more and look less like the actual function.

The begin, add, and end macros are used in just that order:

```c
BUT_SUITE_BEGIN(ts)
BUT_SUITE_ADD(simple_t1)
BUT_SUITE_ADD(simple_t2)
BUT_SUITE_ADD_EMBEDDED(deep1)
BUT_SUITE_END;
```

Tack on a `BUT_GET_TEST_SUITE` macro and you're done:

```c
BUT_GET_TEST_SUITE("My Tests", ts);
```

## Exceptions and Assertions
Exceptions are key to detecting errors. They enable a quick escape, in an orderly fashion, from deep inside test code out to the driver. If some constraint isn't held, test code throws an exception and the driver catches it, inspects it, and reports from where it was thrown and why it was thrown. The where and why helps in debugging the offending piece of code.

The exception component is inspired by and uses many of the methods from chapter 3 of David Hanson's book, "C Interfaces and Implementations, Techniques for Creating Reusable Software". It is implemented as a set of wrappers around `setjmp`/`longjmp`.

### Reasons
Exceptions themselves are just static strings, so each one is unique, and if the strings are well chosen they describe themselves.

```c
typedef char const *BUTExceptionReason;
```

Here are a few that BUT provides for general use:
```c
BUTExceptionReason but_expected_failure   = "expected failure";
BUTExceptionReason but_unexpected_failure = "unexpected failure";
BUTExceptionReason but_invalid_value      = "invalid value";
```

### State
To provide a well-structured exception handling mechanism, we define an environment that can be in one of three states:

- **Entered**: a try block has been entered and `setjmp` has been called to initialize a jump buffer.
- **Throw**: an exception has been thrown by a call to `longjmp` using the most recently defined jump buffer.
- **Handled**: either a thrown exception has been caught, or a finally block has been entered w/o a thrown exception.

These three states are represented by this enum:

```c
typedef enum BUTExceptionState {
    BUT_ENTERED,
    BUT_THROWN,
    BUT_HANDLED,
} BUTExceptionState;
```

### Environment
Exceptions are managed as a stack of environments that contain a jump buffer, a link to the parent environment, a state field, and context captured from a thrown exception that gets passed into a handler so the issue can be recorded and reported for analysis.

One important detail is that its `state` field is declared `volatile`. This is one of the few times where `volatile` is essential, because compilers are allowed to stash values in registers. In light of `setjmp`/`longjmp`, the state must be restored after calling `longjmp`. However, there is a serious flaw in the implementation. The context information, `reason`, `details`, `file`, and `line`, are not also declared `volatile`. The code works when compiled with Visual Studio 2022, but will fail miserably if compiled with clang.

### Throwing and Catching
Test code can just throw an exception using one of the throw macros. The simplest, `BUT_THROW(reason)` records the file and line number from which it was called. `BUT_THROW_DETAILS` allows for a printf-style format string and a sequence of values to be captured before throwing the exception.

To catch an exception, define a try catch block using `BUT_TRY` to open a new block, `BUT_CATCH(some_exception)` or `BUT_CATCH_ALL` to catch all exceptions, and `BUT_END_TRY` to close it. `BUT_TRY` initializes a new exception environment (`BUTExceptionEnvironment`) which includes calling `setjmp` on the environment's jump buffer. `setjmp` returns zero, which maps to the `BUT_ENTERED` state. It also gets the current stack, and pushes the new environment on to the top of the stack.

Normal execution continues with the code in the try block, and if the catch block finds that the state is `BUT_ENTERED` it pops the stack, changes the state to `BUT_HANDLED`, and lets execution continue. Similarly, when execution gets to `BUT_END_TRY`, it checks the state and if it's `BUT_ENTERED` (maybe there was no catch block), it pops the stack and sets the state to handled.

Calling `BUT_THROW()` throws an exception which pops the top environment off the stack, captures the details of the exception, and calls `longjmp` on the environment's jump buffer to return execution to where `setjmp` was called. Now `setjmp` returns 1, which sets the state to `BUT_THROWN` and the catch block will compare its exception against the incoming one. If the exception is a match, the state is changed to handled, and execution continues normally. If it's not a match, execution continues to the end of the try/catch block where the exception is rethrown so another try/catch block can attempt to handle it.

If no try/catch block can handle the exception, the stack becomes empty and the throw code calls the context's currently defined handler. Usually that's the test driver's handler, which will catch the exception and record/report the error.

### Context
I found it useful to wrap the environment in a context that combines a pointer to an exception handler with a stack of environments.

```c
struct BUTExceptionContext {
    but_handler_fn          *handler; ///< exception handler
    BUTExceptionEnvironment *stack;   ///< top of a stack of exception environments
};
```

I defined a global default context, `g_default_context_` and an active context pointer, `g_context_` in `exception.c` that get built into both the driver code and each test suite. The global context is initialized to the default context the first time `but_get_exception_context()` is called.


### The Exception Context Problem

The DLL model creates a subtle issue. Both the driver and each test DLL statically link the exception library, so they each get their own independent copy of the exception stack. An exception thrown from the DLL without any try/catch blocks wants to pop an environment from the DLL's stack, which is empty. The throw hits the unhandled exception handler.

BUT solves this with context injection. The driver has its own instance of a `BUTExceptionContext` holding a handler function pointer and the exception stack pointer. After loading the DLL, the driver calls `GetProcAddress` to find the test suite's `but_set_exception_context` function and calls it to pass a pointer to the driver's own context. From that point on, exceptions thrown in the DLL find the driver's exception frames.

One small wart in this implementation is that `BUT_CATCH` compares the address of the thrown exception to the one its argument points to. This won't work if the driver ever needs to catch a specific exception thrown from a test suite. However, the BUT driver uses `BUT_CATCH_ALL` so pointer mismatch isn't an issue.

There's a related wrinkle with exception *reasons*. Reasons are constant strings. Matching them by pointer equality would compare a pointer in the DLL to the address of the same string in the driver, which are different objects at different addresses even though they hold the same text. BUT uses `strcmp` for exception matching. When the driver's handler catches an exception it uses `BUT_UNEXPECTED_EXCEPTION` which is just `strcmp(e, but_expected_failure)`. If the exception is not expected (`strcmp` returns a non-zero value), then it has caught something interesting and reports it.

## Summary
At this point BUT was good enough. What I really wanted was a test framework that could inject faults into memory management functions to stress test C code. My intent was to continue using the same pattern of macros and typedefs to develop a fault-injection test framework. It worked for a while, but eventually turned out to be harder than I thought. I had to rework the entire exception-handling implementation into a service provided by the driver to test suites through a shared interface. That's the story for the next post.

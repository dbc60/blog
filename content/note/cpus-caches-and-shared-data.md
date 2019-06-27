---
title: About CPUs, Caches and Shared Data
date: 2016-03-07
draft: true
categories: blog
tags: [multiprocessing, c++, c++11]
---

This post is about when a central processing unit (CPU) can reorder instructions that load and store shared values, that is, values that are visible to more than one processor.
<!--more-->

## Sequential Consistency for Data-Race Free (SC-DRF) Programs
Software memory models have converged on sequential consistency for data-race-free programs (SC-DRF).

- Java: SC-DRF required since 2005.
- C11 and C++11: SC-DRF default and remains true unless you use relaxed atomics (relaxed == transitional tool).

SC-DRF amounts to a contract. The programmer guarantees that a race-condition was not written, and the compiler guarantees to provide the illusion of executing the program you wrote.

## Acquire and Release Orderings
We have a key general concept, called a `Transaction`. A transaction is a logical operation on related data that maintain an invariant. It is:

- Atomic: all or nothing
- Consistent: reads a consistent state, or takes data from one consistent state to another.
- Independent: correct in the presence of other transactions on the same data.

Example:

```cpp
bank_account acct1, acct2;
// begin transaction - ACQUIRE exclusivity
acct1.credit(100);
acct2.debit(100);
// end transaction - RELEASE exclusivity
```

The transaction ensures we don't expose inconsistent state (for example, a credit without also a debit).

The way we do this is by defining a critical region with our common tools.

- Critical region: code that must execute in isolation w.r.t. other program code.
- Locks (`mut_x` is a mutex protecting `x`):

```cpp
{ lock_guard<mutex> hold(mut_x);    // enter critical region (lock "acquire")
  ... read/write x ...
}                                   // exit critical region (lock "release")
```

- Ordered atomics (`whose_turn` is a `std::atomic<>` variable protecting `x`):

```cpp
// spin-lock with an atomic variable.
while(whose_turn != me) {}  // enter critical region (atomic read "acquires" value)
... read/write x ...
whose_turn = someone_else;  // exit critical region (atomic write "release")
```

- Transactional memory (still research right now, but same idea):

```cpp
atomic {                    // enter critical region
    ... read/write x ...
}                           // exit critical region
```

1. Key Rule for a Critical Region: Code Can't Move Out!
2. It's okay to move code into a critical region
3. It's **not** okay to move code after the "release" to before the "acquire".

For example, by rule 2, we can transform the following code:

```cpp
x = "life";
mut.lock();

y = "universe";

mut.unlock();
z = "everything";
```

into this code:

```cpp
mut.lock();
z = "everything";
y = "universe";
x = "life";
mut.unlock();
```

However, even though the assignments of `x` and `z` didn't start in the critical region, it is not okay to take the first code example, and swap the assignments of `x` and `z`:

```cpp
// NOT LEGAL!
z = "everything";   // race bait
mut.lock();

y = "universe";

mut.unlock();
x = "life";         // race bait
```

The reason you can't swap those assignments is that when you release something, what you are conceptually doing is releasing all actions taken by this thread so far. It includes all actions in the critical region, plus any other work the thread did. For example, setting `y` to "universe" might be a flag stating that we are done writing to `x`. If we moved the write to `x` to below the release operation, then we're not releasing the entire state of the thread that's doing the release operation.

Conversely, I can't move the assignment to `z` before the acquire, because I'd be doing things before the acquire, so I wouldn't be seeing state in the critical region I intended to acquire (that is, whatever the value of `z` was before we set the value of `y`).

Key Concepts: "Acquire" and "Release" are one way barriers. We can move memory accesses down through an `acquire`, but not up above an `acquire`. Likewise, we can move memory accesses up through a `release`, but not down past a `release`.

More precisely: *A release store makes its prior accesses visible to a thread performing an acquire load that sees (pairs with) that store*.

Compiler's can see that mutexes and atomics use special instructions to ensure acquire and release semantics hold. They can't see into opaque function calls, so unless the compiler can prove otherwise, it must assume that each opaque function call is a full barrier.

There are two flavors of acquire and release that differ in a subtle way. One is a "Plain" Acquire/Release, and the other is a "Sequentially Consistent (SC)" Acquire/Release. Remember that you can't move any memory operations up across an acquire or down across a release. This means that we can't move an acquire and release past each other. However, there is a hole in the story. A release-acquire pair can move past each other, so the following sequence:

- acquire (critical section 1)
- acquire (critical section 2)
- release (critical section 2)
- release (critcal section 1)
- acquire (critical section 3)

can become:

- acquire (critical section 1)
- acquire (critical section 2)
- release (critcal section 2)
- acquire (critical section 3) - potential deadlock!!!
- release (critcal section 1)

For the SC Acquire/Release, we add an additional rule that says we can't reorder acquire/release operations with each other at all. Ordinary memory operations can still be reordered down across an acquire, or up across a release, but a release cannot move down across an acquire and an acquire cannot move up across a release. This makes acquire/release completely sequentially consistent.

Note that the Itanium processor has separate `load.acquire` and `store.release` instructions. It can move a load-acquire (`ld.acq`) up across a store-release (`st.rel`), so it needs an extra fence on the store-release to ensure loads and store are completely sequentially consistent. I think something similar happens with ARM or PowerPC processors, too. Other processors can implement completely sequentially consistent loads and stores directly (like the Intel x86 and AMD64 processors).

### How Do We Express Acquire and Release in our Code
We use mutexes, atomics and/or fences. Here are some rules:

- We don't want to write fences by hand if we don't have to.
- We do want the compiler to produce barriers for you on your behalf. We use "critical region" abstractions:
    - mutexes (lock = acquire, unlock = release)
    - `std::atomic<>` variables (read = acquire, write = release)

### Sequential Consistency is More Than Just About Acquire-Release Alone
Here is a transivity/causality example. Assume `x` and `y` are atomic variables, and `g` is an ordinary global variable. All variables are initially zero.

| Thread 1 | Thread 2 | Thread 3 |
| :--- | :--- | :--- |
| `g = 1;` <br> `x = 1;` | `if (x == 1)` <br> &nbsp;&nbsp;&nbsp;&nbsp; `y = 1;` | `if (y == 1)` <br> &nbsp;&nbsp;&nbsp;&nbsp;`assert(g == 1);`|

In C++11 `atomic<T>`, and C11 `atomic_*` are by default SC acquire-release (NB: **not** C/C++ `volatile`). If you reach into the `memory_order_*` "bucket" and explicitly take over what the memory orders are, then you had better know what you are doing. That said, there is a performance reason to do this on PowerPC and ARM today.

What you get is that:

- each individual read and write of an atomic variable is guaranteed to be all or nothing.
- Each thread's read/writes are guaranteed to execute in *source code order*.
- Special operations: swap, compare-and-swap are conceptually atomic execution of the following code:

```cpp
    T atomic<T>::exchange(T desired)
    {
        T oldval = this->value;
        this->value = desired;
        return oldval;
    }

    bool atomic<T>::compare_exchange_strong(T& expected, T desired)
    {
        if (this-value == expected)
        {
            this->value = desired;
            return true;
        }

        expected = this->value;
        return false;
    }
```

In C++11, compare-and-swap is written as either `compare_exchange_strong` or `compare_exchange_weak`. The way you use it is, for example, `if (val.compare_exchange_strong(expected, desired))`. It means, "Am I the one who gets to change *val* from *expected* to *desired*?" If yes, atomically set it to the desired value and return true (I changed it), otherwise return false.

It is often written in loops, "CAS loop."

- `_weak` vs. `_strong`: `_weak` allows spurious failures.
    - Prefer `_weak` when you're going to write a CAS loop anyway. The difference is that the loop can fail spuriously. Even if the value was *expected*, `compare_exchange_weak` can still return false on a particular nanosecond. That's okay in a loop, because it will succeed most likely on the next iteration.
    - Almost always want `_strong` when doing a single test.

### Controlling Reordering #3: Write Fences & Ordering APIs
Fences are explicit "sandbars" against reordering.

A Linux memory barrier is `mb()`. It is a full memory barrier:

```cpp
flag1 = 1;
mb();
// Linux full barrier is approximately equivalent to the x86 'mfence' instruction
if (flag2 != 0)) { ... }
```

Similarly, a Win32 memory barrier is `InterlockedExchange(&flag, val)`:

```cpp
InterlockedExchange(&flag1, 1);
// Win32 ordered API is approximately equivalent to the x86 'xchg' instruction
if (flag2 != 0) { ... }
```

These barriers mean that the write of `flag1` and the read of `flag2` cannot be reordered.

Their disadvantages are:

- Non-portable: Different flavors on different processors.
- Tedious: Have to be written (correctly == differently) at *every* point of use.
- Error-prone: Hard to reason about. 'Lock-free' papers avoid mentioning.
- Performance: Usually too heavy. Standalone barriers are especially pessimized - they do not allow any reordering of instructions, whereas acquire and release allow some movement/reordering.
- NB: Avoid "barriers" that purport to apply *only to one kind* of reordering (for example, compiler), as reordering can happen at any level. Example: Win32 *_ReadWriteBarrier* affects only compiler reordering.

Avoid standalone fences! They are heavyweight. They require more synchronization, and prevent more optimizations than acquire-load and release-store atomic operations. **Also, ordering should be associated with a specific load or store, not be a standalone fence because it has to be more heavyweight (a full fence), rather than just an acquire-load or release-store.

### Code Generation
On the x86 architecture, an Ordinary Load is the same instruction as an SC Atomic Load. They are both `mov` instructions. So, we don't get any optimization of Ordinary Loads over the SC Atomic loads. Here's what happens with `mov` (from the Intel 64 and IA-32 Architectures Software Developer's Manual, Volume 3A, section 8.2.2):

- *Reads are not reordered with **any** reads*. This is very strong.
- *Writes are not reordered with **any** writes (some exceptions)*. This is very strong.
- *Writes are not reordered with **older** reads*.
- Reads may be reordered with **older** writes to different memory locations. A store to `y` and a load to `x` may be reordered.
- *Reads & writes not reordered with **locked** instructions (like `xchg`, which has an implicit `lock` preceding it)*. All we need is a SC Release operation to let loads and stores float upward across it. Instead, the x86 memory model forces a full barrier on us. It's not that big a deal, but still it's more than we need.
- Reads cannot pass earlier LFENCE and **MFENCE**. *MFENCE* is a full memory barrier. The C11 and C++11 standards don't care about LFENCE and SFENCE.
- Writes cannot pass earlier LFENCE, SFENCE and *MFENCE*.
- LFENCE cannot pass earlier reads.
- SFENCE cannot pass earlier writes.
- MFENCE cannot pass earlier reads or writes.

The four rules in *italics* are stronger than what we need for Sequential Consistency for Data Race Free (SC-DRF) code.

### C++ Memory Order Tools
The `memory_order_*` values are:

- `memory_order_relaxed`
- `memory_order_acquire`
- `memory_order_release`
- `memory_order_acq_rel`
- `memory_order_seq_cst` (sequentially consistent)

There is also `memory_order_consume`, but it is something odd with `carries_dependency` and `kill_dependency`, but Herb Sutter didn't discuss it in his Atomic Weapons presentation.

The last one, `memory_order_seq_cst`, is the default, so you don't need to specify it. Atomic loads and store will just use it and work in a sequentially consistent manner.

The weakest memory order is `relaxed`. The load/store is still atomic, but there are no ordering guarantees - it can float up or down relative to other loads and stores.

Here's an excerpt from the C++ Standard (&sect;29.3/1):

- `memory_order_relaxed`: no operation orders memory.
- `memory_order_release`, `memory_order_acq_rel`, and `memory_order_seq_cst`: **a store operation performs a release** operation on the affected memory location.
- `memory_order_consume`: a load operation performs a consume operation on the affected memory location.
- `memory_order_acquire`, `memory_order_acq_rel`, and `memory_order_seq_cst`: **a load operation performs an acquire** operation on the affected memory location.

Some combinations are nonsense. Example (&sect;29.6/13):

> Suppose we want to load a value using an atomic load operation: `C A::load(memory_order order = memory_order_seq_cst)`, or some variation on this. In the standard, the requires paragraph (&sect;29.6/13) for loads says **Requires: The order shall not be `memory_order_release` or `memory_order_acq_rel`**. It states this, because only stores release something. Loads don't release anything - they acquire something.

There are a handful of patterns that can benefit from using relaxed atomics *judiciously*:

- Examples: Event counters. Dirty flags. Reference counting.
- Degenerate example: Atomic variable accessed in a race-free manner (that is, in a region where it doesn't need to be atomic because it's not shared or the program is synchronized in some other way).

Wrap relaxed atomic operations. Keep the relaxed operations inside types that implement the patterns:

- Don't let relaxed atomic op calls spread out into the callers.
- Problem: It's very subtle to define the library so that the "relaxed-ness" is not detectable to the client.

#### Example: Simple Event Counting
If you have several worker threads that are incrementing an atomic counter and doing nothing else with that counter, and you have a main thread that reads the count only after all other threads have completed, then the code for the worker threads can replace `++count;` with `count.fetch_add(1, memory_order_relaxed);`, and the main thread can replace `count` with `count.load(memory_order_relaxed)`:

Worker Thread Before:

```cpp
// count is atomic and is initially zero.
while ()
{
    ...
    if (...)
        ++count;
    ...
    ...
}
```

Main Thread Before:

```cpp
int main()
{
    launch_workers();   // starts each worker thread
    ...

    join_workers(); // ostensibly does a .join on each worker thread
    std::cout << count << std::endl;
}
```

Worker Thread After:

```cpp
while ()
{
    ...
    if (...)
        count.fetch_add(1, memory_order_relaxed);
    ...
    ...
}
```

Main Thread After:

```cpp
int main()
{
    launch_workers();   // starts each worker thread
    ...

    join_workers(); // ostensibly does a .join on each worker thread
    std::cout << count.load(memory_order_relaxed) << std::endl;
}
```

#### Example: Simple Event Counting, a Better Solution
Consider count is wrapped in a class, so you have an `event_counter` type, and make `count` an instance of that type. Use a type that encapsulates the desired semantics and hides the relaxed memory ops. Then you can document the class stating it's intended use (only for blinding incrementing and then reading the value once all writing is completed and synchronized).

### C++ Concurrency
A future is an asynchronous value.

- Available in C++11 as `future<T>`/`shared_future<T>`.
- Available in Java as `Future<T>`, .NET as `Task<T>`.

What we already have in C++ is a synchronous call, where the caller waits for the callee to complete:

```cpp
auto result = f(x, y, z);
// ... code here doesn't run until f completes and result is ready ...
go_and_use(result);     // value available
```

We also have an asynchronous function call:

```cpp
auto result = async([=]{return f(x,y,z);}); // asynchronous call
// ... code here runs concurrently with f ...
go_and_use(result.get());                   // use it when ready; n.b.: this may block
```

Use `future.get()` to get the value you need for the next job. Use `future.wait()` when you need the side effects to complete (even if the asynchronous call was to a void function) before moving on to the next job.

*future/shared_future* are:

- Great for usability: easy to talk about async values ==> async function calls.
- Absolutely essential for composability: easy to take multiple libraries that launch async work and combine them consistently.

#### What's Missing
What we want, and what the C++ standards committee is looking at, is a way to not wait for the value of the future. The API they are considering is:

- `future.then()` which allows you to compose the next item of work once the current future is done.
- `when_any()` (like `||`) and `when_all()` (like `&&`), which allow you to compose the next item of work when ??? one or more futures complete?

While we're waiting for `.then`, `when_any` and `when_all` to become part of the standard, we have a couple of options:

1. Use a library, like the Visual Studio Parallel Patterns Library (PPL). Look into this and the WinRT API. Note that it should be really easy to convert code from PPL to what ever the standard comes up with.
2. Turn blocking into non-blocking by occupying a thread:
    - calling `async`: `auto next = async([] {go_and_use(f.get());});`
    - wrap *std::future* by writing a template function with two template parameters and have a trailing return `decltype` in three lines of code:

```cpp
template<typename Fut, typename Work>
auto then( Fut f, Work w) -> future<decltype(w(f.get()))>
{ return async([=]{ w( f.get() );}); }

// now we can write:
auto next = then(f, [](int r){go_and_use(r);});
```

You can always turn non-blocking into blocking by calling `.wait()` with no overhead.

You can always turn blocking into non-blocking via `async()`, or equivalent, at the cost of occupying (borrowing (+wakeup)) a thread.

Go read Herb Sutter's article [Sharing is the Root of all Contention](http://herbsutter.com/2009/02/13/effective-concurrency-sharing-is-the-root-of-all-contention/).

#### C++11 Wrapper Problem
The complete solution is:

```cpp
template<class T>
 class wrap {
 private:
    T t;    // wrapped object
    :::     // wrapper-specific state

public:
    wrap(T t_ = T{}) : t{t_} {}

    template<typename F>
    auto operator()(F f) -> decltype(f(t)) {    // strategy: take any code (!)
        // wrapper work
        auto result = f(t);                     // pass the wrapped object to it
        // more wrapper work
        return result;                          // and return the result
    }
};
```

If you use this pattern, the calling code is something like this:

```cpp
wrap<X> w;
w([](X& x) {
    x.accounts.credit(bob, 100);
    x.accounts.debit(mary, 100);
    cout << x.balance() << endl;
});
```

```cpp
template<class T>
class foo {

};
```

Applying this pattern to the monitor pattern in C++11:

```cpp
template<class T>
class monitor {
private:
    mutable T t;
    mutable std::mutex m;

public:
    monitor(T t_ = T{}) : t{t_} {}

    template<typename F>
    auto operator()(F f) const -> decltype(f(t))
    {
        std::lock_guard<mutex> _{m};
        return f(t);
    }
};
```

#### Using `monitor<T>`

```cpp
monitor<string> s = "start\n";  // conversion ok
vector<future<void>> v;

for (int i = 0; i < 5; ++i)
    v.push_back()(async([&,i] {
        s([=](string& s) {
            s += to_string(i) + " " + to_string(i);
            s += "\n";"
        });

        s([](string& s) {
            std::cout << s;
        });
    }));

for (auto& f:v) f.wait()        // and join
std::cout << "Done\n";
```

If we had polymorphic (generic) lambdas, the code becomes very slick:

```cpp
monitor<string> s = "start\n";  // conversion ok
vector<future<void>> v;

for (int i = 0; i < 5; ++i)
    v.push_back()(async([&,i] {
        s([=](s) {      // <== don't need "string& s", just "s"
            s += to_string(i) + " " + to_string(i);
            s += "\n";"
        });

        s([](s) {       // <== don't need "string& s", just "s"
            std::cout << s;
        });
    }));

for (auto& f:v) f.wait();   // and join
std::cout << "Done\n";
```

This can be written with a C++14 conformant compiler!

#### Getting Back to Concurrency
The `monitor<T>` was interesting, but it is blocking. What we really want is a message queue that asynchronously hands off the work to a worker thread (sounds like the LMAX Disruptor pattern might be useful). The proposed C++ library name is `concurrent_queue`, and it would replace a mutex. Similarly, it would be nice to have `concurrent<T>` to replace the `monitor<T>` wrapper defined above.

How hard could it be? You can turn blocking into non-blocking by replacing a mutex with a message queue. Also remember that our `monitor<T>` implementation is:

```cpp
template<class T>
class monitor {
private:
    mutable T t;
    mutable std::mutex m;

public:
    monitor(T t_ = T{}) : t{t_} {}

    template<typename F>
    auto operator()(F f) const -> decltype(f(t))
    {
        std::lock_guard<mutex> _{m};
        return f(t);
    }
};
```

Now we turn this into non-blocking by adding a message queue (we'll use `concurrent_queue` as a placeholder, since the C++11 standard doesn't define one). NOTE: This implementation is incomplete - there's no return value.

```cpp
template<class T>
class concurrent {
private:
    mutable T t;
    mutable concurrent_queue<Tstd::function<void()>> q;
    bool done = false;
    std::thread thd;

public:
    // The thd object waits until done==false, pops the next item off the queue and
    // executes it.
    concurrent(T t_ = T{}) : t{t_}, thd{[=] {while(!done) q.pop()(); }} {}

    // The desctructor pushes a lambda that sets done to true, and then waits for
    // for the thread to complete. What the worker thread does, is keep popping work
    // items off the queue, until it hits this last lambda. That causes the worker to
    // execute the lambda, and set done to true. When done is true, the worker exits
    // its loop and returns!
    ~concurrent() {q.push([=] {done = true;}); thd.join();}

    // This functor takes any type F that I can pass an object of type T to, and instead
    // of taking a lock (as in the mutable<T>) and then executing f(t) and then unlock, it // says "push a lambda which when executed, will run f(t)." This lamda will run on
    // the worker thread after it pops the lambda off the queue.
    template<typename F>
    void operator()(F f) const {q.push([=] {f(t);});}
};
```

So what we have is an object that upon creation spins up a thread and owns the object of type `T`. It lets me pass any work I want to do to that object, executes that work one after the other asynchronously. Callers never block, waiting for the work to complete. It also gets nice orderly shutdown, because at the end it simply enqueues a message to say it's done. That last method, in the desctructor, is the only method that may block.

This is an idiom similar to the Active Object pattern that comes up in Herb Sutter's concurrency course.

To use this class template, just create an object of `concurrent<T>`, say `obj`, and pass it a lambda or a pointer to a function that defines the work to be done (e.g., `obj([=] {do_work();});`)

```cpp
concurrent<string> s = "start\n";
vector<future<void>> v;

// Push 5 lambdas onto v
for (int i = 0; i < 5; ++i)         // launch some work
{
    v.push_back()(async([&,i] {
        s([=](string& s) {
            s += to_string(i) + " " + to_string(i);
            s += "\n";
        });

        s([](string& s) {
            std::cout << s;
        });
    }));
}

// Enqueue those lambda
for (auto& f:v) f.wait();   // and join
std::cout << "Done\n";
```

This is exactly the same code that was used for the monitor, just with concurrent substituted in the first line. The difference is that this code never blocks the caller, except at `f.wait();` The second `for`-loop merely enqueus a vector full of futures that take a void and return void. It's possible that the main thread prints "Done" to `cout` before the worker thread has a chance to complete so much as the first work item.

Here's another example that creates an asynchronous `ostream`:

```cpp
concurrent<ostream&> async_cout{cout};  // capture cout(!)
vector<future<void>> v;

for (int i = 0; i < 5; ++i)     // launch some work
{
    v.push_back(async([&,i] {
        async_cout([=](ostream& cout) {
            cout << to_string(i) << " " << to_string(i);
            cout << "\n";
        });
        async_cout([=](ostream& cout) {
            cout << "Hi from " << i << endl;
        });
    }));
}

for (auto& f:v) f.wait();       // and join
aync_cout([](ostream& cout){cout << "Done\n";});
```

Here's how to write `operator()` for the concurrent class template so it returns the correct value. In the monitor case, we used `-> decltype(f(t))`. Here we want to return a future:

```cpp
template<typename F>
auto operator()(F f) const -> std::future<decltype(f(t))> {
    // make a promise
    auto p = make_shared<std::promise<decltype(f(t))>>();
    auto ret = p->get_future();

    // capture the promise and push it onto the queue.
    q.push([=] {
        try {p->set_value(f(t));}
        catch(...) {p->set_exception(current_exception());}
    });

    return ret;
}
```

There is a problem with this code: `future::set_value` has two overloads. It has the one used above and it has an empty one that takes no arguments for void. The code above won't compile if `t` is void. To make that work, call a helper which you overload for `promise<Fut>` and `promise<void>`:

```cpp
template<typename F>
auto operator()(F f) const -> std::future<decltype(f(t))> {
    // make a promise
    auto p = make_shared<std::promise<decltype(f(t))>>();
    auto ret = p->get_future();

    // capture the promise and push it onto the queue.
    q.push([=] {
        // If f(t) succeeds, we set the value. If it throws, we correctly store
        // and propagate the exception.
        try {p->set_value(*p, f, t);}
        catch(...) { p->set_exception(current_exception()); }
    });

    return ret;
}

template<typename Fut, typename F, typename T>
void set_value(std::promise<Fut>& p, F& f, T& t) { p.set_value(F(t)); }

template<typename F, typename T>
void set_value(std::promise<void>& p, F& f, T& t) { f(t); p.set_value(); }
```

#### One Note on `std::async`
*future*/*shared_future* destructors do not join (which is good, because blocking is bad), **except** when spawned from `async` (bad!). Here are reasons why this is a bad idea, and it should be fixed in the standard (maybe it was for C++14). Consider these two pieces of code:

```cpp
// (a)
{
    async([]{ f(); });
    async([]{ g(); });
}

// (b)
{
    auto f1 = async([]{ f(); });
    auto f2 = async([]{ g(); });
}
```

These two chunks of code don't do the same thing, because the future destructor joins. This means (a) is *not* asynchronous at all. You have to capture the future to make it live a little longer so these two lines of code can overlap.

Similarly:

```cpp
{
    async(launch::async, []{ f(); });
    async(launch::async, []{ g(); });
}
```

There is no concurrency at all in this code either! Herb considers this behavior a bug. I would, too.

Finally,

```cpp
void func() {
    future<int> f = start_some_work();
    /* ... more code that doesn't f.get() or f.wait() */
}
```

You don't know if this code will block or not. It depends on whether the function chose to launch its work via a `std::thread` or `std::async`. For example, if `start_some_work` returns a future that is a move of a move of a move ... of a move of something that was eventually launched with `std::async`, this function will block before exiting its scope, otherwise it won't!

This is not composable. We must always be able to tell if code might block. It means we can't use futures reliably on a highly responsive thread, like a GUI thread.

Can I use `std::future`, even though I don't need the result, if the caller:

- Could be called under a lock the task may need? (Deadlock).
- Is supposed to be responsive (e.g., a GUI thread)? (Nonresponsive).

#### Tracking Down Whether `std::futures` from `std::async` Still Block in 2016
Per Scott Meyer's March 30, 2013 article (revised) [`std::futures` from `std::async` aren't special!](http://scottmeyers.blogspot.com/2013/03/stdfutures-from-stdasync-arent-special.html), he says "It's comparatively well known that the `std::future` returned from `std::async` will block in its destructor until the asynchronously running thread has completed:"

```cpp
void f()
{
  std::future<void> fut = std::async(std::launch::async,
                                     [] { /* compute, compute, compute */ });

}                                    // block here until thread spawned by
                                     // std::async completes
```

From my reading of the spec, &sect;30.6.8/5, nothing has changed in this area between C++11 and C++14, so the destructor of the `std::future` returned from `std::async` is still required to block until the asynchronously running thread has completed.

Furthermore, the following code from [C++ Quiz] should always emit "z":

```cpp
##include <iostream>
##include <string>
##include <future>

int main() {
    for (;;)
    {
        std::string x = "x";

        std::async(std::launch::async, [&x]() {
            x = "y";
        });
        std::async(std::launch::async, [&x]() {
            x = "z";
        });

        std::cout << x;
    }

    return 0;
}
```

The explanation is:

> The destructor of a future returned from async is required to block until the async task has finished (see elaboration below). Since we don't assign the futures that are returned from async() to anything, they are destroyed at the end of the full expression (at the end of the line in this case). §12.2¶3 in the standard: "Temporary objects are destroyed as the last step in evaluating the full-expression (1.9) that (lexically) contains the point where they were created."
>
> This means that the first async call is guaranteed to finish execution before async() is called the second time, so, while the assignments themselves may happen in different threads, they are synchronized.
>
> Elaboration on synchronization:
> According to § 30.6.8¶5 of the standard:
> Synchronization:
> [...]
> If the implementation chooses the launch::async policy,
> — the associated thread completion synchronizes with (1.10) the return from the first function that successfully detects the ready status of the shared state or with the return from the last function that releases the shared state, whichever happens first.
>
> In this case, the destructor of std::future<> returned by the async() call is "the last function that releases the shared state", therefore it synchronizes with (waits for) the thread completion.

### The `const` and `mutable` Keywords
Two main changes in the language:

1. `const` objects must be thread safe. That is, they must be either bitwise immutable, or internally synchronized so a writer won't interfere with, say, a reader making a copy of that `const` object. This makes it possible for copy constructors to function.
2. `mutable` objects must be thread safe. That is, they must be either bitwise-const or internally synchronized.

```cpp
class widget {
    mutable mutex m;    // protects internal data
    ...                 // more data

public:
    info get_info() const {
        lock_guard<mutex> hold(m);
        return { /* use 'more data' */};
    }

    ...                 more code
};
```

The mutex in the widget class is already synchronized, so it is *thread safe* and thus can be declared mutable. It's necessary to declare it mutable so the `const` function `get_info` will compile (otherwise, the compiler would complain about modifying a member variable in a `const` function).


Here's another example. Say we have an atomic counter in our class, and the value of that counter is **not** externally mutable.

```cpp
class widget {
    atomic<int> counter;    // internal instrumentation only.
    ...                     // other data

public:
    info get_info() const {
        ++counter;          // oops - can't modify members in a const function
        return {/* use 'other data' */};
    }
};
```

We can declare our counter mutable because it is an atomic `int`, so it is already thread safe. Making it mutable means that our `const` function will compile.

```cpp
class widget {
    mutable atomic<int> counter;    // internal instrumentation only.
    ...                             // other data

public:
    info get_info() const {
        ++counter;
        return {/* use 'other data' */};
    }
};
```

The counter in this example, and the mutex in the previous example are thread-safe, therefore they want to be mutable.

C++11:
`const == mutable == thread-safe` (bitwise `const` or internally synchronized).

Look for members that are declared `mutable`, but are **not** already thread-safe (that is, not already atomic, mutex or concurrent queue) and fix them.

### Of Promises and Futures
There's a great discussion of promises, futures, threads and `std::async` on [stackoverflow](http://stackoverflow.com/questions/14283703/when-is-it-a-good-idea-to-use-stdpromise-over-the-other-stdthread-mechanisms). Here are some of the highlights:

ANSWER:
A `std::future` is a strange beast: in general, you cannot modify its value directly. Three producers which can modify its value are:

1. `std::async` through an asynchronous callback, which will return a `std::future` instance.
2. `std::packaged_task`, which, when passed to a thread, will invoke its callback thereby updating the `std::future` instance associated with that `std::packaged_task`. This mechanism allows for early binding of a producer, but a later invocation.
3. `std::promise`, which allows one to modify its associated `std::future` through its `set_value()` call. With this direct control over mutating a `std::future`, we must ensure that the design is thread-safe if there are multiple producers (use `std::mutex` as necessitated) - WHAT? WHY NOT USE `std::shared_future`? Perhaps that only allows for multiple consumers and doesn't take into account multiple producers.

Seth Carnegie says:

> An easy way to think of it is that you can either set a future by returning a value or by using a promise. future has no set method; that functionality is provided by promise.

David Rodrguez says:

> The consumer end of the communication channel would use a `std::future` to consume the datum from the shared state, while the producer thread would use a `std::promise` to write to the shared state.

But as an alternative, why not simply just use a `std::mutex` on a stl container of results, and one thread or a thread-pool of producers to act on the container? What does using `std::promise`, instead, buy me, besides some extra readability vs a stl container of results?

The control appears to be better in the `std::promise` version:

1. `wait()` will block on a given future until the result is produced
2. if there is only one producer thread, a mutex is not necessary

The following google-test passes both helgrind and drd, confirming that with a single producer, and with the use of wait(), a mutex is not needed.

TEST

```cpp
static unsigned MapFunc( std::string const& str )
{
    if ( str=="one" ) return 1u;
    if ( str=="two" ) return 2u;
    return 0u;
}

TEST( Test_future, Try_promise )
{
    typedef std::map<std::string,std::promise<unsigned>>  MAP;
    MAP          my_map;

    std::future<unsigned> f1 = my_map["one"].get_future();
    std::future<unsigned> f2 = my_map["two"].get_future();

    std::thread{
        [ ]( MAP& m )
        {
            m["one"].set_value( MapFunc( "one" ));
            m["two"].set_value( MapFunc( "two" ));
        },
      std::ref( my_map )
    }.detach();

    f1.wait();
    f2.wait();

    EXPECT_EQ( 1u, f1.get() );
    EXPECT_EQ( 2u, f2.get() );
}
```

Furthermore, Seth Carnegie says, "You don't choose to use a `promise` *instead* of the others, you use a `promise` to *fulfill* a `future` in conjunction with the others. The code sample at [cppreference.com](http://en.cppreference.com/w/cpp/thread/future) gives an example of using all four:"

```cpp
##include <iostream>
##include <future>
##include <thread>

int main()
{
    // future from a packaged_task
    std::packaged_task<int()> task([](){ return 7; }); // wrap the function
    std::future<int> f1 = task.get_future();  // get a future
    std::thread(std::move(task)).detach(); // launch on a thread

    // future from an async()
    std::future<int> f2 = std::async(std::launch::async, [](){ return 8; });

    // future from a promise
    std::promise<int> p;
    std::future<int> f3 = p.get_future();
    std::thread( [](std::promise<int>& p){ p.set_value(9); },
                 std::ref(p) ).detach();

    std::cout << "Waiting...";
    f1.wait();
    f2.wait();
    f3.wait();
    std::cout << "Done!\nResults are: "
              << f1.get() << ' ' << f2.get() << ' ' << f3.get() << '\n';
}
```

prints

> Waiting...Done!
> Results are: 7 8 9

Futures are used with all three threads to get their results, and a promise is used with the third one to fulfill a future by means other than a return value. Also, a single thread can fulfill multiple futures with different values via promises, which it can't do otherwise.

An easy way to think of it is that you can either set a future by returning a value or by using a promise. future has no set method; that functionality is provided by promise. You choose what you need based on what the situation allows.

#### What is a Promise?
This question was asked on [stackoverflow](http://stackoverflow.com/questions/11004273/what-is-stdpromise/12335206#12335206) which contains an outstanding summary:

There are two distinct, though related, concepts in C++11:

- Asynchronous completion (a function that is called somewhere else).
- Concurrent execution (a *thread*, something that does work concurrently)
- The two are somewhat orthogonal concepts. Asynchronous computation is just a different kind of function call, while a thread is an execution context.
- Futures should be thought of as the asynchronous drop-in replacement for ordinary return types.
- We have the template `std::future<T>`, which represents a future value of type `T`.

If we consider the function `int foo(double, char, bool);`, then the future for it is `std::future<int>`.

There is a hierarchy of abstraction for asynchronous computation. From highest to lowest, it is:

1. `std::async`: The most convenient and straightforward way to perform an asynchronous computation is via the `async` function template, which returns the matching future immediately:
    - `auto fut = std::async(foo, 1.5, 'x', false);   // is a std::future<int>`
    - We have very little control over the details. We don't know if the function is executed concurrently, serially upon `fut.get()`, or by some other black magic.
    - The results are easy to obtain: `auto res = fut.get();    // is an int`
2. The next lower level of abstraction is `std::packaged_task`. We could use it to *implement* something like `async`, and thus have explicit control over the way the asynchronous function is executed. For example, we could insist it run on a separate thread by means of the `std::thread` class.
    - `std::packaged_task` is a class template
        - It wraps a function and provides a `future` for the function return value
        - The object itself is callable, and callable at the caller's discretion.
    - `std::packaged_task<int(double, char, bool)> tsk(foo);`
    - `auto fut = tsk.get_future();     // is a std::future<int>`
    - The `future` becomes ready once we call the task and the call completes. This is the ideal job for a separate thread. We just have to make sure to *move* the task into the thread:
    - `std::thread thr(std::move(tsk), 1.5, 'x', false);`
    - Be sure to either `detach` or `join` the thread (or use Anthony Williams' `scoped_thread` wrapper).
    - When the function call finishes, our result will be ready: `auto res - fut.get();`
3. The lowest level, `std::promise` allows us to implement the packaged task. The `promise` is the building block for communicating with a future. The principal steps are these:
    - The calling thread makes a promise.
    - The calling thread obtains a future from the promise.
    - The promise, along with function arguments, are moved into a separate thread.
    - The new thread executes the function and populates the future to fulfill the promise.
    - The original thread retrieves the result.

Here's an outline of an example for our own "packaged task":

```cpp
template <typename> class my_task;

template <typename R, typename ...Args>
class my_task<R(Args...)>
{
    std::function<R(Args...)> fn;
    std::promise<R> pr;             // the promise of the result

public:
    template <typename ...Ts>
    explicit my_task(Ts &&... ts) : fn(std::forward<Ts>(ts)...) { }

    template <typename ...Ts>
    void operator()(Ts &&... ts)
    {
        pr.set_value(fn(std::forward<Ts>(ts)...));  // fulfill the promise
    }

    std::future<R> get_future() { return pr.get_future(); }

    // disable copy, default move
};
```

Usage of this template is essentially the same as that of `std::packaged_task`. Note that moving the entire task subsumes moving the promise. In more ad-hoc situations, one could also move a promise object explicitly into the new thread and make it a function argument of the thread function, but a task wrapper like the one above seems like a more flexible and less intrusive solution.

#### Exceptions and Promises
Continuing from [stackoverflow](http://stackoverflow.com/questions/11004273/what-is-stdpromise/12335206#12335206):

Promises are intimately related to exceptions. The interface of a promise alone is not enough to convey its state completely, so exceptions are thrown whenever an operation on a promise does not make sense. All exceptions are of type `std::future_error`, which derives from `std::logic_error`. First off, a description of some constraints:

- A default-constructed promise is inactive. Inactive promises can die without consequences.
- A promise becomes active when a future is obtained via `get_future()`. However, only *one* future may be obtained!
- A promise must either be satisfied via `set_value()` or have an exception set via `set_exception()` before its lifetime ends if its future is to be consumed. A satisfied promise can die without consequence, and `get()` becomes available on the future. A promise with an exception will raise the stored exception upon call of `get()` on the future. If the promise dies with neither value nor exception, calling `get()` on the `future` will raise a "broken promise" exception.

## References
- [Scott Meyers - CPU Caches and Why You Care](https://vimeo.com/97337258) at the Norwegian Developers Conference (NDC), and also on YouTube from the [2014 Code::dive conference](https://www.youtube.com/watch?v=WDIkqP4JbkE).
- [Data-Oriented Design book](http://www.dataorienteddesign.com/dodmain/) in beta.
- [Mike Actor - Data-Oriented Design and C++](https://www.youtube.com/watch?v=rX0ItVEVjHc) on YouTube from CppCon 2014.

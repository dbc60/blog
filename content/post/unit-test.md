---
title: "Unit Test"
date: 2025-01-30T20:40:29-05:00
2025: ["01"]
tags: [blog, draft]
draft: true
---
I am getting back into C programming on a regular basis. One of the problems with writing C code is making sure it does what you intend it to do. I've made lots of mistakes in the past, and I'd like to reduce their likelihood a little. One way to do that is to test the hell out of code, so a unit-test framework would be useful. There are lots of test frameworks out there, like [Check](https://libcheck.github.io/check/), [CUnit](https://cunit.sourceforge.net/), [CuTest](https://cutest.sourceforge.net/), and a great many others. Some of them look great, but I think that the experience of writing my own will be a gentle way to get back into a regular habit of writing C.
<!--more-->
{{< table_of_contents >}}
While writing this note and looking for a few exemplary test frameworks, I found [cmocka](https://cmocka.org/). It has a great looking website making me think it must be very polished. So what am I doing writing my own unit test framework? I'm writing one for the experience, to try my own ideas of what unit tests and the testing experience should look and feel like. It should be fun, too.

## Goals
I'll start simply. In fact, what's the simplest unit test framework that can get the job done? Such a project needs:

- Test Driver: a program to load and run a set of tests.
- Test Suite: something that contains a set of tests, like a shared library.
- Test Case: some standard way to write test cases and collect them into test suites such that a test driver can load, setup, run, and teardown each test.
- Test Result: a way to indicate whether a test passed or failed, and why.
- Reporting: a backend module to report test results in a consistent format.

The bulk of a test driver can be captured in a static library. An actual test driver can be built up from components, so a specific driver can have a particular backend, or several selectable backends for reporting results. The rest of the internals are common to all drivers.

To my mind, a shared library should encapsulate a suite of test cases. The test driver itself can be built as a static library that provides all of the functionality needed to load and run tests, and collect results that can be reported in some manner (e.g., written to a terminal or a file).

## Resources

- [Subunit](https://github.com/testing-cabal/subunit) is a streaming protocol for test results.
- [xUnit.net](https://xunit.net/) is an open-source unit testing tool for the .NET Framework.
- [xUnit](https://www.martinfowler.com/bliki/Xunit.html), by Martin Fowler.
- [Common JUnit XML Format & Examples](https://github.com/testmoapp/junitxml). At least in the world of Java programming, the JUnit XML file format is a standard format to exchange test results between tools. It might be worth considering as a backend to a test driver.

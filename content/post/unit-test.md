---
title: "Writing a Unit Test Framework in C"
date: 2025-01-30T20:40:29-05:00
publishDate: 2026-03-21T00:00:00-04:00
years: ["2025"]
tags: [blog, c, testing]
---
The C programming language was one of the first programming languages I ever learned (after learning Basic, APL, and Fortran). I haven't written much in C lately and I miss it, so I decided I needed a project to write C on a regular basis.

One of the problems with writing C code is making sure it does what you intend it to do. I've made lots of mistakes in the past, and I'd like to reduce their likelihood a little. One way to do that is to test code thoroughly, so a unit-test framework would be useful.
<!--more-->

There are already lots of test frameworks out there, like [Check](https://libcheck.github.io/check/), [CUnit](https://cunit.sourceforge.net/), and [CuTest](https://cutest.sourceforge.net/). Some of them look great, but I think that the experience of writing my own will be a gentle way to get back into a regular habit of writing C.
{{< table_of_contents >}}
I should note that I don't have Linux. I use Windows, and so I need code that compiles and runs there. That said, [Check](https://libcheck.github.io/check/) looks great, but the [tutorial jumps to using Autotools](https://libcheck.github.io/check/doc/check_html/check_3.html#Setting-Up-the-Money-Build-Using-Autotools). I just can't relate to that with my Windows development environment.

[CUnit](https://cunit.sourceforge.net/) organizes tests into test suites and test suites into a registry. It looks like developers have to bring their own test driver and compile/link in their registry to the driver. That doesn't quite fit my mental model for organizing tests. I think there should be a standalone driver that dynamically loads test suites. In other words, the driver is an executable and each test suite is a DLL.

[CuTest](https://cutest.sourceforge.net/)'s documentation is a little sparse, but similar to CUnit, it looks like that each test suite a standalone executable. Again, I want a separate test driver where test suites can be listed on the command line and possibly provide command-line options for running tests and specifying output formats.

While writing this note and looking for a few exemplary test frameworks, I found [cmocka](https://cmocka.org/). It has a great looking website making me think it must be very polished. It also requires writing your own main function for each test suite. I'd rather just write tests and not be concerned about a main function.

I'm writing a unit-test framework for the experience, to try my own ideas of what unit tests and the testing experience should look and feel like. For example, if a test fails it should be able to throw an exception that is caught by the driver. In C exception handling can be supported through setjmp/longjmp. Splitting that between an executable and a DLL is difficult. Perhaps that's why these frameworks are designed so that test suites are standalone executables. I think I've figured out how to get around that obstacle and do it cleanly.

## Goals
I'll start simply. In fact, what's the simplest unit test framework that can get the job done? Such a project needs:

- Test Driver: load and run test suites.
- Test Suite: a set of tests to run.
- Test Case: some standard way to write test cases and collect them into test suites such that a test driver can load, setup, run, and teardown each test.
- Test Result: a way to indicate whether a test passed or failed, and why.
- Reporting: a backend module to report test results in a consistent format.

The bulk of a test driver can be implemented in a static library. An actual test driver can be built up from components, so a specific driver can have a particular backend, or several selectable backends for reporting results. The rest of the internals are common to all drivers.

I believe a shared library should encapsulate a suite of test cases. The test driver itself can be built as a static library that provides all of the functionality needed to load and run tests, and collect results that can be reported in some manner (e.g., written to a terminal or a file).

## Resources

- [Subunit](https://github.com/testing-cabal/subunit) is a streaming protocol for test results.
- [xUnit.net](https://xunit.net/) is an open-source unit testing tool for the .NET Framework.
- [xUnit](https://www.martinfowler.com/bliki/Xunit.html), by Martin Fowler.
- [Common JUnit XML Format & Examples](https://github.com/testmoapp/junitxml). At least in the world of Java programming, the JUnit XML file format is a standard format to exchange test results between tools. It might be worth considering as a backend to a test driver.

## What Came Next

The framework described here was completed and is called [Basic Unit Test](https://github.com/dbc60/but) (BUT). A follow-up post will cover the implementation in detail. After working with BUT, I identified one big design problem and several improvements worth pursuing, so I built a second framework called **Faultline**. I'll push that to GitHub soon and write more on that in a subsequent series. It was quite a journey.

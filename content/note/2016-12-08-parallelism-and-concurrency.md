---
title: Parallelism & Concurrency
date: 2016-12-08
categories: [software]
tags: [concurrency, parallelism]
---

Notes from Martin Thompson's talk "A quest for predictable latency with Java concurrency."
<!--more-->

## Parallelism and Concurrency

> 1. Parallel is the opposite of Serial
> 1. Concurrent is the opposite of Sequential
> 1. Vector is the opposite of Scalar
>
>     -- John Gustafson

> - Concurrency is about *dealing* with lots of things at once.
> - Parallelism is about *doing* lots of things at once.
>
>     -- Rob Pike

- Concurrent Example: One processor that time-slices two threads.
- Parallel Example: Two processors, each with their own region of memory, each
  executing a single thread.
- Parallel & Concurrent Example: Two processors, sharing the same memory
  system, each one executing a single thread.

## References

- [A Quest for Predictable Latency with Java Concurrency](https://vimeo.com/181814264)
- [Aeron IPC on Github](https://github.com/real-logic/Aeron)
- [Aeron - The Next-Generation in High Performance Messaging](https://www.infoq.com/presentations/aeron)
- [Do We Need Another Messaging System](http://highscalability.com/blog/2014/11/17/aeron-do-we-really-need-another-messaging-system.html)
- [Aeron: Open-source high-performance messaging](https://www.youtube.com/watch?v=tM4YskS94b0)
- [Agrona](https://github.com/real-logic/Agrona)
- [Real Logic](http://real-logic.github.io/)
- [Simple Binary Encoding](http://real-logic.github.io/simple-binary-encoding/)

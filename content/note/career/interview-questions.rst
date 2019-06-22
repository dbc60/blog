---
title: Interview Questions
date: 2019-03-07
draft: true
categories: career
tags: [interview, golang, c++]
cssDetail: drop-caps_goudy
---

Here is a small collection of questions to ask engineering candidates.
<!--more-->

.. contents:: Contents
   :class: sidebar


.. _interview questions:

*****************
C/C++ Basic Types
*****************

What are the types of x and y?

.. code-block:: c++

    int x;
    int *x;
    int *x, y;
    int x[42];
    int *x[42];
    int (*x)[42];
    int (*x)(int);
    int (*x[42])(int);

*********
Go Basics
*********

* When would you use an interface vs a struct?

**************
Go Concurrency
**************

* How do you manage concurrent access to a resource in Go?
* When would you prefer a mutex over a channel & goroutine?
* How might you exit a goroutine that is waiting to read from a channel?

    * One way is to close the channel and check the second value from the result of the receive operator ``false``.

* Are there any other mechanisms for exiting such a goroutine?

    * Provide a ``done`` channel, and use a ``select`` statement to choose
      between the data channel and the done channel. Exit when the done channel
      returns a value.

* What is returned by the receive operator from a closed channel?
* How do you tell the difference between a value received from an open channel
  vs a closed channel?

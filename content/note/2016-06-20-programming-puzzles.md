---
layout: post
title: Programming Puzzles
categories: work
tags:
  - c
  - c++
  - puzzles
excerpt: Programming puzzles for interviews.
---

## Contents
{:.no_toc}

- TOC
{:toc}

## The Type of the Variable
1. `int t;`
1. `int *t;`
1. `int t[10];`
1. `int *t[10];`
1. `int *(t[10]);`
1. `int (*t)[10];`
1. `int (*t)();`
1. `int (*t)(int);`
1. `int (*t[10])(int);`

## C++ in C
What structs would you need to create in C to produce a representation of the following class:

```
class C {
    int i;

public:
    C(int x): i(x);
    virtual ~C();
    virtual void set(int x);
    virtual int get();
};
```

## Links & Loops

- Say you have a singly-linked list. How would you determine if there is a loop in the list?
- Given a singly-linked list, reverse the order of its elements.

## Other Questions & Puzzles
- What's the difference between big-endian and little-endian data?

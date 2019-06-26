---
layout: post
title: API Design
date: 2016-03-07
draft: true
categories: blog
tags: [api]
excerpt: Certainly one aspect of API design is to make the API as regular and as easy to use as possible.
---

## Contents
{:.no_toc}

- TOC
{:toc}

## Discontinuities
 I like this quote:

 > The primary goal of component API design is to eliminate API discontinuities.
  -- Casey Muratori

Five characteristics that effect discontinuities:
1. Granularity: Split API A into APIs B and C to gain control.
2. Redundancy: You have to choose whether to use API A or B. There is an API A which does some things. There is also an API B which does the same thing, but maybe takes different parameters or does it in a different way.
3. Coupling: There is a link between API A and API B. If you do one thing in A, you must also do another thing in B.
4. Retention: The API is in two parts - one is on your side and one is on their side. When the API is called, it retains some data, so the next time its called the result depends on the values from a previous call.
5. Flow Control: Who is calling whom? Is the game/application code calling the library? Does the library call into the application? Does the application call the library and the library also callsback the application?

## Granularity
You can have a single API to, say, `UpdateOrientation(Object);`, or you can have something more fine-grained:

Separate get/set functions:

```c
    Orientation = GetOrientation(Object);
    Change = GetOrientationChange(Object);
    SetOrientation(Object, Orientation + Change);
```

By separating `UpdateOrientation` into `GetOrientation`, `GetOrientationChange` and `SetOrientation`, not only can we combine two orientations into a new orientation, but we can add extra processing between get and set:

```c
    Orientation = GetOrientation(Object);
    Change = GetOrientationChange(Object);
    Change += 3.14f;
    SetOrientation(Object, Orientation + Change);

    Orientation = GetOrentation(Object);
    Change = GetOrientationChange(Object);
    RunSomeOtherUnrelatedThing();
    SetOrientation(Object, Orientation + Change);
```

When designing an API or evaluating an API, follow this checklist:

- Write the code that uses the API.
  - Spend a day or two writing to the kind of API you'd like to use.
  - When you evaluate an API, see how closely it matches the one you'd like to use.
- All retained mode constructs have immediate-mode equivalent. This allows you to transition from the retained mode to a more fine-grained immediate mode when you need to.
- For every API that uses callbacks or inheritance, there is an equivalent API that does neither.
- No API requires the use of an API-specific data type for which the average game already has an equivalent.
- Any API function your game may not consider atomic can be re-written using between 2 and 4 more granular APIs (not counting accessors).
- Any data which does not clearly have a reason for being opaque should be transparent in all possible ways (construction, access, I/O, etc.)
- Use of the component's resource management (memory, file, string, etc.) is completely optional.
- Use of the component's file format is completely optional.
- Full run-time source code is available.

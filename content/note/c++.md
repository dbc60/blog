---
title: C++11
date: 2016-03-07
draft: true
categories: notes
tags:
  - c++
  - c++11
---

Everything cool about C++11.
<!--more-->

## Identifier Names
There is a [good answer on stackoverflow](http://stackoverflow.com/questions/228783/what-are-the-rules-about-using-an-underscore-in-a-c-identifier) regarding reserved identifiers in C++. There are patterns of identifiers reserved for the language and compilers.

- Identifiers reserved in any scope, including for use as implementation macros:
    - identifiers beginning with an underscore followed immediately by an uppercase letter
    - identifiers containing adjacent underscores ("double undersores")
- In the global namespace, identifiers beginning with an underscore are also reserved. Specifically, the standard lists the C99 standard as a normative reference (1.2), so the following patterns of identifiers are reserved per paragraph 7.2.3 of the C99 standard:
    - All identifiers that begin with an underscore and either an uppercase letter or another underscore are always reserved for any use.
    - All identifiers that begin with an underscore are always reserved for use as identifiers with file scope in both the ordinary and tag name spaces.
    - Each macro name in any of the following subclauses (including the future library directions) is reserved for use as specified if any of its associated headers is included; unless explicitly stated otherwise (see 7.1.4).
    - All identifiers with external linkage in any of the following subclauses (including the future library directions) are always reserved for use as identifiers with external linkage.154
    - Each identifier with file scope listed in any of the following subclauses (including the future library directions) is reserved for use as a macro name and as an identifier with file scope in the same name space if any of its associated headers is included.
- In the `std` namespace all identifiers are reserved, though you are allowed to make template specializations.

Some rules of thumb are:
- never start a symbol with an underscore.
- never name a symbol with two consecutive underscores inside

For example:
```cpp
##define _WRONG
##define __WRONG_AGAIN
##define RIGHT_
##define WRONG__WRONG
##define RIGHT_RIGHT
##define RIGHT_x_RIGHT
```

Also, [MSDN](https://msdn.microsoft.com/en-us/library/565w213d.aspx) helps clarify patterns of identifiers that may and may not be used in C++. Among other things, it says:

> Use of two sequential underscore characters ( __ ) at the beginning of an identifier, or a single leading underscore followed by a capital letter, is reserved for C++ implementations in all scopes. You should avoid using one leading underscore followed by a lowercase letter for names with file scope because of possible conflicts with current or future reserved identifiers.

## Range-based For Loops

## Compile-time Constant Expression Evaluation

## References
- <a id="range-for"></a>[Range-based for loop](http://en.cppreference.com/w/cpp/language/range-for)
- <a id="constexpr"></a>[constexpr specifier](http://en.cppreference.com/w/cpp/language/constexpr)
- <a id="std::for_each"></a>[`std::for_each` algorithm](http://en.cppreference.com/w/cpp/algorithm/for_each)
- [Advice on naming identifiers](http://stackoverflow.com/questions/228783/what-are-the-rules-about-using-an-underscore-in-a-c-identifier)
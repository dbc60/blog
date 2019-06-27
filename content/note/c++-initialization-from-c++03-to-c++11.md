---
title: C++ Initialization from C++03 to C++11
date: 2016-03-07
draft: true
categories: blog
tags:
    - c++
    - c++11
    - initialization
---

Initialization of Plain Old Data (POD) types has become more consistent, and it is now possible to initialize member arrays, containers and dynamically allocated POD types with a clean uniform syntax.
<!--more-->

## C++ Initialization Syntax
Danny Kalev wrote a very informative article<sup>1</sup> comparing the four ways available in C++03 to initialize variables to the new uniform method available in C++11. The short version is that C++03 doesn't have any way to initialize member arrays, nor dynamically allocated Plain Old Data (POD) types, and it's difficult to initialize Standard Library containers. The initialization syntax available is inconsistent.

- POD types are initialized with the equal sign (`=`), or the equal sign can be replace by the initial value wrapped in parentheses (`int n = 0;`, or `int n(0);`). However, if the POD type is an array, and it is dynamically allocated, there is no way to initialize it:
    - `char *buff = new char[1024];  // no initialization is possible`
- Data members in a class are initialized through the constructor's member initialization list, where the initial value for each member is enclosed in parentheses. However, if the data member is an array, there is no way to initialize it.
- Class objects are initialized by enclosing a comma-separated list of values in parentheses.
- Aggregates can be initialized, but the comma-separated list of values are enclosed in braces.
- Strings are initialized by a string literal which encloses the value in double quotes.

Delightfully, C++11 addresses these issues with a universal initialization notation using braces.

```cpp
// POD initialization
int a{0};

// STL container initialization
std::string s{"hello"};
std::string s2{s}; //copy construction
std::vector<std::string> vs{"alpha", "beta", "gamma"};
std::map<std::string, std::string> stars {
    {"Superman", "+1 (212) 545-7890"},
    {"Batman", "+1 (212) 545-0987"}
};

// Initialization of a dynamically allocated array
double *pd = new double [3] {0.5, 1.2, 12.99};

// Initialization of a data member array
class C
{
    int x[4];
public:
    C(): x{0,1,2,3} {}
};
```

C++11 adds some additional initialization techniques:
- Class member initializer, where each member is initialized where it is defined. This syntax is easier to read and write than a member initialization list.
- Class member initializers also enable member array initialization using equal-sign, parentheses or the new brace initialization syntax.
- Note that both the member initialization list and the class member initializer may be used, but the former takes precedence. Both can be used. If the class has multiple constructors those members with initializers will have those default values, unless the particular constructor overrides those defaults with a member initializer list.

## References
- <a id="ref1"></a>[Get to Know the New C++11 Initialization Forms](http://www.informit.com/articles/article.aspx?p=1852519)
- <a id="ref2"></a>[Is C++11 Uniform Initialization a Replacement for the Old Style Syntax?](http://programmers.stackexchange.com/questions/133688/is-c11-uniform-initialization-a-replacement-for-the-old-style-syntax)
- <a id="ref3"></a>[Initializer Lists and Uniform Initialization](http://www.learncpp.com/cpp-tutorial/b-4-initializer-lists-and-uniform-initialization/)
- <a id="ref4"></a>[C++11: Initializer Lists and Range-for Statements](http://ignoringthevoices.blogspot.com/2011/11/c11-initializer-lists-and-range-for.html)
- <a id="ref5"></a>[List Initialization (since C++11)](http://en.cppreference.com/w/cpp/language/list_initialization)
- <a id="ref6"></a>[std::initializer_list](http://en.cppreference.com/w/cpp/utility/initializer_list)
- <a id="ref7"></a>[Range-based for loop (since C++11)](http://en.cppreference.com/w/cpp/language/range-for)
- <a id="ref8"></a>[Overload Resolution: Implicit Conversion Sequence in List-initialization](http://en.cppreference.com/w/cpp/language/overload_resolution#Implicit_conversion_sequence_in_list-initialization)
- <a id="ref9"></a>[C++ Concepts: PODType](http://en.cppreference.com/w/cpp/concept/PODType)

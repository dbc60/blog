---
title: "Testing With Permutations"
date: 2023-05-02T10:43:42-04:00
2023: ["05"]
tags: [swdev]
draft: true
---
How do I test a library that matches glob patterns to file paths? Glob patterns consist of literal characters, a few wildcards, '`?`', '`[`', and '`*`', the last of which can be doubled to match paths recursively, and each of which can be escaped to match the literal character. So we have eight kinds of patterns to test: literals, four kinds of wildcards, and three escaped wildcards, which means there are $8! = 40,320$ possible permutations. Fortunately, we don't have to test all of those possibilities to ensure reasonable code coverage.
<!--more-->
{{< table_of_contents >}}

## Different Types of Glob Patterns

A glob pattern is a string consisting of Unicode characters and possible wildcard patterns. A wildcard is one of '`?`', '`*`', or '`[`'. Also, the backslash ('`\`') is used to escape each of these characters so they are not interpreted as a wildcard pattern. For example "`\?`" will match a literal question mark instead of "any single character except a path separator."

This leads to these patterns:

1. Literal strings.
2. '`?`' will match any single character except a path separator.
3. '`[`' starts defining a character class.
4. '`*`' will match multiple characters except a path separator.
5. '`**`' will match multiple characters including path separators.
6. Escaped wildcards, "`\?`", "`\[`", and "`\*`", which match the literal wildcard characters in a path.

## The Easy Patterns

Literal strings are the simplest pattern. There are no wildcards at all. They are compared to a path string character-by-character.

The simplest wildcard is the question mark (`?`). As stated above, it matches any single character in the path except a path separator.

## Character Classes

A character class defines a set of characters that can match any single character in a path. The set is delineated by a pair of brackets ('`[`', and '`]`'). If the first character after the leading '`[`' is not '`!`', then it matches all characters enclosed in the brackets. Note that the string enclosed by the brackets is not allowed to be empty, so an unescaped '`]`' can be included if it is the first character in the set. That leads to odd looking patterns like, "`[][!]`" which will match '`[`', '`]`', or '`!`' in a path.

The syntax of character classes extends beyond listing a set of characters between the brackets. Two characters separated by a hyphen (`-`) defines a range of characters, where the range is based on the value of the characters' Unicode code points. For example, "`[A-Za-z0-9]`" defines the set of all ascii alphanumeric characters, and "`[A-Fa-f0-9]`" defines the set of all hexadecimal digits. An explicit hyphen can be included in a character class if it is either the first or last character between the brackets, or if it is escaped (i.e., `\-`).

Finally, a character class can be negated, or complemented, by placing an exclamation point as the first character between the brackets. In this case, it will match any single character NOT in the class.

> A Note on Path Separators
>
> The [glob(7) documentation](https://man7.org/linux/man-pages/man7/glob.7.html) says that a range (like "`[.-0]`") containing the '`/`' character is syntactically incorrect. I suppose the reason for that is it's safer to require an explicit path separator than to allow a hidden one in a range.
>
> I'd like any glob implementation to work on Windows as well. It would be silly to have one syntax for glob patterns on Linux and another on Windows, so '`/`' in patterns will match '`\`' in actual paths on Windows.


### Match a Directory

### Match Directories Recursively

## Permutations

## Choosing Example Patterns

## Generating Expected Answers

## Putting It All Together

## Implementations

- [sryze/glob](https://github.com/sryze/glob) in C++.

---
title: "Glob Patterns"
date: 2023-05-08T17:01:29-04:00
2023: ["05"]
tags: [swdev]
featuredImage: "/images/banners/zebra-rhode-island-zoo-2011.jpg"
featuredDescription: "Rhode Island Zebra"
featuredCopyright: "Rhode Island Zebra, copyright © Douglas Cuthbertson 2011"
---
Some time in 2016 or 2017, I needed a way to match file paths with [glob patterns](https://en.wikipedia.org/wiki/Glob_(programming)). The trick was that it had to work in a filter driver running in the Windows kernel. There weren't a lot of ready-to-use libraries that were kernel-ready. In fact I couldn't find any, so I wrote my own.
<!--more-->

I needed an implementation that would accept the [normal wildcards][glob7] and it would be really helpful if it also accepted the `**` wildcard to match directory paths recursively. My first thought was to look for examples to get an idea of how to structure a solution. I hoped that I could find an open-source library where I could just transliterate the code from whatever language it was written to C (without any calls to the standard library, because that's not a thing within the Windows kernel). All the examples I could find were either limited to the standard wildcards or had exponential behavior, as [Russ Cox so eloquently discussed](https://research.swtch.com/glob).

That got me thinking about the shape of glob patterns. Simple patterns, made up of literal strings, the `?` wildcard and character classes, are matched character-by-character (with a little extra processing for character strings). The `*` pattern matches zero-or-more characters followed by whatever _simple pattern_ follows it. So `abc*xyz` is a simple pattern, `abc`, followed by a zero-or-more pattern `*xyz` that amounts to a loop that consumes a character (except a path separator) every time the simple `xyz` pattern fails to match the path. I'm going to refer to `*` patterns as _directory patterns_, because they are limited to matching file and directory names within a single directory.

Similarly, `**` patterns, _recursive patterns_, can be thought of requiring a loop that consumes any character that isn't matched by whatever pattern follows it. The trick here is to realize that `**` can be followed by a simple pattern and zero-or-more directory patterns. If at any point during the matching process the simple pattern or any of the directory patterns fail, the recursive pattern consumes one character from the path and the process starts over from that point. This is still an $O(n)$ process, because it always makes progress through the path.

This realization, that recursive patterns are made up of simple and directory patterns, led to a relatively simple algorithm. I uploaded [an implementation in Go on GitHub][dbc60/glob]. It's different from what I wrote for that filter driver. That code diverged from the syntactic rules in the [glob(7) man page][glob7] and very Windows-centric. This implementation does its best to hold to those rules and runs in user space on both Windows and Linux.

[glob7]: https://man7.org/linux/man-pages/man7/glob.7.html
[dbc60/glob]: https://github.com/dbc60/glob

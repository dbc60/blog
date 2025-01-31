---
title: "Glob Patterns"
date: 2023-05-08T17:01:29-04:00
2023: ["05"]
tags: [sweng]
math: true
featuredImage: "/images/banners/zebra-rhode-island-zoo-2011.jpg"
featuredImageDescription: "Rhode Island Zebra"
featuredCopyright: "copyright © 2011 Douglas Cuthbertson"
lastmod: 2023-11-12
---
Some time in 2016 or 2017, I needed a way to match file paths with [glob patterns](https://en.wikipedia.org/wiki/Glob_(programming)). The trick was that it had to work in a filter driver running in the Windows kernel. There weren't a lot of ready-to-use libraries that were kernel-ready. In fact I couldn't find any, so I wrote my own.
<!--more-->

Back then, I wrote an implementation in C which was very Windows-centric, and didn't hold to the syntactic rules from the [glob(7) man page][glob7]. It was sufficient for the job, but I wanted to revisit the problem and create something more generally useful. I uploaded [an implementation in Go on GitHub][dbc60/glob] that holds to the [glob(7)][glob7] rules, is very efficient, and runs in user space on both Windows and Linux.

This Go module accepts the `**` wildcard (to match directory paths recursively) as well as [normal wildcards][glob7]. When I originally researched how to go about building a pattern-matching function, I looked for existing code to get an idea of how to structure a solution. I hoped that I could find an open-source library where I could just transliterate the code from whatever language it was written to C (without any calls to the standard library, because that's not a thing within the Windows kernel). All the examples I could find were either limited to the standard wildcards or had exponential behavior, as [Russ Cox so eloquently discussed](https://research.swtch.com/glob).

That got me thinking about the shape of glob patterns. Simple patterns, made up of literal strings, the `?` wildcard, and character classes, are matched character-by-character (with a little extra processing for character classes). The `*` pattern matches zero-or-more characters followed by whatever simple pattern follows it. So `abc*xyz` is a glob composed of a simple pattern, `abc`, followed by a zero-or-more pattern `*xyz`. The latter pattern is called a _directory pattern_, because it's limited to matching file and directory names within a single directory. Directory patterns amount to specifying a loop that consumes a character (except a path separator) every time the simple pattern that follows it fails to match some portion of a path.

Similarly, `**` patterns, _recursive patterns_, can be thought of requiring a loop that consumes any character that isn't matched by whatever pattern follows it. The trick here is to realize that `**` can be followed by a simple pattern and zero-or-more directory patterns. If at any point during the matching process the simple pattern or any of the directory patterns that may follow it fail, then processing continues by allowing `**` to consume one character from the path and then matching the path to the pattern restarts from that point. This is still an $O(n)$ process, because each iteration makes progress through the path until either the whole pattern and path are consumed, or a match cannot be found.

This realization, that recursive patterns are made up of simple and directory patterns, led to a relatively simple algorithm and a fast implementation. See the [repo][dbc60/glob] for the code.

[glob7]: https://man7.org/linux/man-pages/man7/glob.7.html
[dbc60/glob]: https://github.com/dbc60/glob

Updated 2023-11-12: spelling, grammar and to clarify how recursive patterns are processed.
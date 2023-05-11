---
title: "Communicating"
date: 2023-04-25T07:43:42-04:00
2023: ["04"]
tags: ["life"]
draft: true
---
I must not be communicating well with managers. They don't seem to understand the value of what I bring to the company. My coworkers have on occassion complemented me, saying code I've written is easy to read, understand, and once in a while elegantly structured.

Where am I going with this post? What is it I want to communicate? My disappointment with the layoff at F5? Am I wondering why I was selected for the layoff? I should contact Chris Ford and ask for his reasoning. It's okay to ask for insight.
<!--more-->
{{< table-of-contents >}}

I guess I'm sad about the announcement that all of AIP will be disbanded, and worse, everything that Threat Stack built over the past decade or so will be gone. I really enjoyed working on the Windows agent. I thought it had a few clever designs, especially when it came to monitoring activity in the file system. It had a recursive glob pattern matcher, it detected file deletions, it had a memory allocator and used tags so that the lack of memory leaks could be verified just by running `poolmon`, running the agent (to load and exercising the driver) and stopping the agent. When the driver unloads, `poolmon` showed no tagged memory that belonged to the minifilter.

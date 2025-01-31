---
title: Software-Development Workshop
'2023': ['11']
date: '2023-11-18T12:04:32.000Z'
tags: [sweng, draft]
draft: true
---
I have recently started to consider an analogy between the process of software development and a workshop as a place where a craftsperson builds stuff. A workshop for writing software is a place where a programmer can find the various tools and resources needed for creating computer programs. The programmer can select tools from the workshop to build their own development environment, or to continue the analogy, set up their workbench for the tasks at hand.

<!--more-->

My main goal is to organize my tools and be clear about what I need and use to write software, explore the process of software development, and figure out why some tools work well and others don't. I also want to hone my skills in a few programming languages, try out various development techniques and methodologies, and just see what works. If I find a larger project along the way and create something useful, all the better.

When I write code, it's primarily on the Windows operating system. I've dabbled in Linux and FreeBSD, and I even have a MacBook Pro for work. I need to get used to it. It's a very foreign environment. So, I hope to take the time to learn more about them along the way.

The programming languages I have the most experience with are C, C++, and [Go](https://go.dev) (aka, golang). I mostly use Visual Studio Code for editing. For building code written in Go, except for the editor, there's just one set of tools. When it comes to C/C++ programs I use the Community Editions of Visual Studio.

That covers only Windows programs. I want to have more experience with writing code for Linux, MacOS, and the various BSD operating systems. I have been interested in [clang](https://clang.llvm.org/get_started.html) for a while, so I built it from source. The tools needed for that were:

* [CMake](https://cmake.org/download/).
* [Python](https://www.python.org/downloads/).
* [Visual Studio 17 2022 Community Edition](https://visualstudio.microsoft.com/vs/community/).
* [Git for Windows](https://gitforwindows.org/) to checkout the [llvm repository](https://github.com/llvm/llvm-project.git).

Just building clang was quite an experience. Once CMake created the VS solution and project files, it took a little over 20 minutes for Visual Studio 2022 CE to build llvm, clang, clang++, and the rest of the toolset. I'm glad I built a rather beefy home computer last year, because this build took a lot of computing power. I think it's the first time I've seen all 32 threads pegged at 100% and memory usage climb so high (72 GB at one point).

{{< figure src="/images/building-clang.png" link="/images/building-clang.png" title="Building LLVM and Clang on Windows Poof!" alt="Building LLVM and Clang on Windows" >}}

I've had bad experiences with both Python and CMake on Windows, but after building clang my opinion of both of them has improved. I'll be more open to Python programming down the road. On the other hand, while I might explore CMake it's probably more complex than what I need for most of my software projects. Most often, I find that simple build scripts do the job.

Another goal I have for my "workshop" is to hone my skills in C, C++, and Go. I may eventually try some others, like [Rust](https://www.rust-lang.org/) and [OCaml](https://ocaml.org/). Of course, JavaScript is so pervasive that I'll have to see what I can do with it. I used an old version of [Node.js](https://nodejs.org/en/) at work a long time ago. It was used with great success for many years to develop agents for an intrusion-detection system running on Linux. We eventually ported it to Golang where the code was far easier to maintain.

I've written a lot of Windows batch scripts (`bat` or `cmd` files) and some bash scripts (mostly while running git bash). I'd like to be better at writing PowerShell (it's so much more powerful than the Windows command terminal), bash scripts, and to explore the [Tcl/Tk](https://www.tcl.tk/) scripting language.

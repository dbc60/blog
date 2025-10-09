---
title: "A Templating Journey"
date: 2024-05-03T04:53:08-04:00
years: ["2024"]
tags: [blog, draft]
draft: true
---
It started with a desire to make templates of some `cmd` files I wrote to build C software projects. Given the tools I had at hand and the few programming languages I know, Go templates, particularly the [HTML templates](https://pkg.go.dev/html/template) seemed like a flexible and easy to use solution, and then I fell down a rabbit hole.
<!--more-->
{{< table_of_contents >}}

## Background
Several years back, I started following [Handmade Hero](https://handmadehero.org/) by Casey Muratori. Within the first few episodes, Muratori was advocating for keeping software development as simple as possible and knowing your tools. He eschewed build systems and third-party libraries (even the standard library to the greatest degree possible). He built a build system with simple `.cmd` files (or maybe they were `.bat` files, but that doesn't matter much) that ran some version of Microsoft's Visual Studio compiler with just the command-line options needed.

I liked the idea a lot, so I built on his scripts and created a set of my own that gave me build options for debug and release, that cleaned out build artifacts, built unit tests separately, and built separate components so I could refactor large components into smaller ones or add new components and have some confidence they would build and run on their own.

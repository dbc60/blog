---
title: Ray Tracing in One Weekend
date: 2017-02-04
draft: true
categories: programming
tags:
    - graphics
    - ray tracing
---

Peter Shirley has written a little book called "Ray Tracing in One Weekend". It's referenced by some people who are familiar with a program called [smallpaint](https://users.cg.tuwien.ac.at/zsolnai/gfx/smallpaint/), which uses concepts from the book.
<!--more-->

## Ray Tracing in One Weekend
I want to get [this book](https://smile.amazon.com/gp/product/B01B5AODD8/ref=smi_www_rco2_go_smi_2609328962?_encoding=UTF8&*Version*=1&*entries*=0&ie=UTF8). It's only $2.99, but exists only as a Kindle Edition and is only $49 pages long. The blog post [announcing the book](http://in1weekend.blogspot.com/2016/01/ray-tracing-in-one-weekend.html) has the table of contents, and a link to a post about [the tools he used to write the book](http://psgraphics.blogspot.com/2016/01/process-for-speed-writing-book.html).

There's at least one bit of errata. Pete Shirley's blog post, [Bug in my Schlick code](http://psgraphics.blogspot.com/2016/12/bug-in-my-schlick-code.html) covers the problem.

## Review
First I skimmed the book. It seems very straightforward and well organized, so I was looking forward to really diving in. The very first code example posed a problem. The author used images/screenshots to display his code and they are too small to easily read. I use Kindle for PC. According to a post in the Kindle forum, images can be magnified on the Kindle Fire, but not on Kindle for PC. Well, for $2.99 I'll squint or look at his code on [github](https://github.com/petershirley/raytracinginoneweekend).

## References

- [MyScript](http://webdemo.myscript.com/) allows you to draw equations and produces the LaTeX output. It seems to have other features, but I haven't investigated them yet.
- [Ray Tracing in One Weekend Kindle Minibook](https://smile.amazon.com/gp/product/B01B5AODD8/ref=smi_www_rco2_go_smi_2609328962?_encoding=UTF8&*Version*=1&*entries*=0&ie=UTF8)
- [Announcement of Ray Tracing in ONe Weekend](http://in1weekend.blogspot.com/2016/01/ray-tracing-in-one-weekend.html) with the table of contents, and links to graphics books with background material.
- [Smallpaint](https://users.cg.tuwien.ac.at/zsolnai/gfx/smallpaint/), a global illumination renderer in fewer than 250 lines of C++ code.
- [TU Wien Rendering #29 - Path Tracing Implementation & Code Walkthrough](https://www.youtube.com/watch?v=cDi-uti2oLQ) - a YouTube video that is related to smallpaint.
- [Rendering Course from TU Wien University](https://www.cg.tuwien.ac.at/courses/Rendering/VU.SS2016.html). The whole course is now [available in video](https://users.cg.tuwien.ac.at/zsolnai/gfx/rendering-course/)
- [YouTube playlist for TU Wien Ray Tracing Course](https://www.youtube.com/playlist?list=PLujxSBD-JXgnGmsn7gEyN28P1DnRZG7qi).
- [smallpt](http://www.kevinbeason.com/smallpt/): someone who condensed smallpaint down to 99 lines of C++ code. It's silly to try to read i, as it is too condensed and poorly formatted.
- Physically Based Rendering From Theory to Implementation (PBRT). The third edition, published 12/2016 is available on [Amazon](https://smile.amazon.com/gp/product/0128006455/ref=as_li_tl?ie=UTF8&tag=pharr-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=0128006455&linkId=c4c600baa19b9d30346c1af2b5483f18), but it costs nearly $105.
- [Embree](https://embree.github.io/) is a collection of high-performance ray tracing kernels developed at Intel. They are available on GitHub under the Apache 2.0 license.
- [An Even Easier Introduction to CUDA on HN](https://news.ycombinator.com/item?id=13565763)
- [An Even Easier Introduction to CUDA](https://devblogs.nvidia.com/parallelforall/even-easier-introduction-cuda/)
- [Breakdown of a Simple Ray Tracer on HN](https://news.ycombinator.com/item?id=13563577)
- [Breakdown of a Simple Ray Tracer](http://mrl.nyu.edu/~perlin/raytrace1_breakdown/)

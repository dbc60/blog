---
title: "Hugo"
date: 2019-06-12T07:18:40-04:00
draft: true
categories: [web]
tags: [hugo]
---

Some notes on `Hugo`_, a static site generator.
<!--more-->

#############
Hugo Extended
#############

Hugo has an extended version that seems to be for supporting Sass/SCSS. It has
a few other features. If Hugo has a decent plug-in system, it might be nice to
break out some of the features into plug-ins.

The `0.43 release <https://gohugo.io/news/0.43-relnotes/>`- announced you need
the extended version only if you want to edit SCSS.

Here's a list of what some people use the extended version for:

* SASS/SCSS support without any additional tooling or configuration. Beats
  wrangling with Webpack, etc.

These were `listed in the forum <https://discourse.gohugo.io/t/should-i-use-hugo-extended-for-a-new-hugo-project/13954/3>`_, but they can all be done on the basic version:

* Minify - that’s my main use case.
* Resource catenation - my other main use case. Lets you keep code neatly
  arranged in source files but bundled for production efficiency.
* Fingerprinting/Subresource Integrity - useful for security.
* Source maps - useful for debugging.
* Image processing.
* PostCSS - never used it but sounds like it is useful for some people.

You can use themes that use SASS/SCSS with the regular version provided that
they have added the compiled styles to /resources in the theme

Sass was originally written in Ruby. Hugo Extended has a SASS parser included so you do not need to install Ruby.

.. _hugo: https://gohugo.io

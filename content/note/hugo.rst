---
title: "Hugo"
date: 2019-06-12T07:18:40-04:00
draft: true
categories: [web]
tags: [hugo]
cssDetail: "drop-caps-cheshire"
summary: Some notes on `Hugo`_, a static site generator.
---

Hugo has an extended version that seems to be for supporting Sass/SCSS.  It adds ``toCSS`` to the ``resources`` object. Vanilla Hugo doesn't have that method.

The `0.43 release <https://gohugo.io/news/0.43-relnotes/>`- announced you need
the extended version only if you want to edit SCSS.

One person (lost the link) uses hugo-extended for "SASS/SCSS support without any additional tooling or configuration. Beats wrangling with Webpack, etc."

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

Sass was originally written in Ruby. Hugo Extended has a SASS parser included
so you do not need to install Ruby.

##########
Guidelines
##########

* Don't start a note or post with a heading. It prevents the really cool
  drop-caps styling from working.
* If you want your summary to be different from the starting paragraph, put it
  in the YAML frontmatter.
* By default Hugo will use the first 70 words of your post for a
  `content summary <https://gohugo.io/content-management/summaries/>`_. It's
  horrible. It doesn't care about paragraphs, headings, or anything else.
  Use either the summary definition in the YAML frontmatter, or use the
  ``< !--more-->`` separator to control where the summary should end.

.. _hugo: https://gohugo.io

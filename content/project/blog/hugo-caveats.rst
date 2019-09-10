---
title: "Hugo Caveats"
date: 2019-09-09T05:52:07-04:00
draft: true
categories: blog
---

Hugo is a wonderful static site generator. However it has some quirks and limitations. Here are some of its pitfalls and how to avoid them.
<!--more-->

###################
Blocks and Comments
###################

If a partial defines a block, that block may be preceded only by blank lines. Do NOT put HTML comments before any ``{{ define ... }}`` statements.

In templates you can use statements like ``{{ "<!-- layouts/_default/single.html -->" | safeHTML }}`` to generate comments in output files. For production, you can run Hugo with the ``--minify`` options to remove all comments.

My use of blocks isn't entirely correct. Each block can have default content that can be overridden in other templates. My ``layouts/_default/baseof.html`` should fill in the ``main`` block and break it up into smaller parts so the sidebar with ``secondaryNav.html`` is included by default, rather than including it explicitly in each template (like ``_default/section.html``, ``_default/list.html``, etc.).

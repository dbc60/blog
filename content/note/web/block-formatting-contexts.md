---
title: "Block Formatting Contexts"
date: 2019-07-21T08:26:07-04:00
draft: true
---

When it comes to the [visual formatting model](https://developer.mozilla.org/en-US/docs/Web/CSS/Visual_formatting_model), block formatting contexts are big players. So it is crucial for CSS authors to have a solid understanding of their relationship with the flow, floats, clear, and margins.
<!--more-->

A block formatting context is a box that satisfies at least one of the following:

- the value of "float" is not "none",
- the used value of "overflow" is not "visible",
- the value of "display" is "table-cell", "table-caption", or "inline-block",
- the value of "position" is neither "static" nor "relative".

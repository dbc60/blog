---
title: "Basic Html"
date: 2019-04-11T07:34:55-04:00
draft: true
categories: [web]
---

Mozilla has an `Introduction to CSS <mdn intro css_>`_ course as well as an `Introduction to HTML <mdn intro html_>`_ course.

<!--more-->

******************
Dealing with Files
******************

`Dealing with files
<https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/
Dealing_with_files>`_ provides some conventions on file names and directory
structure. I renamed several files, replacing spaces in their names with dashes.

This site is built by `Hugo`_, so folders such as ``images``, ``styles``, and
``scripts`` are under the ``static`` directory. I renamed ``static/js`` to
``static/scripts`` to mirror the MDN convention.

******************
Learn Me Some HTML
******************

My goal is to really understand the structure of my site, so I know where
things are and what needs to be modified as I build it to look the way I want it to. The
`Vanilla theme <https://vanilla-bootstrap-hugo-theme.netlify.com/>`_ is a nice
place to start, but I don't understand the choices made for structure and styling. Additionally, it uses `Bootstrap <https://getbootstrap.com/>`_. Do I
need all of Bootstrap or can I build a good looking website with less CSS?

I've also played with SCSS. I'd like to use that as much asa possible. Thanks to
Hugo-extended for making SASS/SCSS possible.

Terms:

* an opening tag is an element name wrapped in a pair of angle brackets.
* a closing tag is the same as an opening tag, except that it includes a
  forward slash before the element name.
* the content of an element is the text between an opening and closing tag. The
  content may contain other elements.
* the element consists of the opening and closing tags, plus the content
  between them.

.. _mdn intro css: https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS
.. _mdn intro html: https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML
.. _mdn: https://developer.mozilla.org/en-US/
.. _hugo: https://gohugo.io/
.. _bootstrap layout overview: https://getbootstrap.com/docs/4.3/layout/overview/

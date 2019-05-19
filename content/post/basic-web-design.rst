---
title: "Basic Web Design"
date: 2019-04-13T04:45:15-04:00
categories: [software]
tags: [design, web]
---

How much structure is really needed to make a web page. I have a lot to learn.
<!--more-->

###########
Inspiration
###########

*Italics text*

**Bold text**

I read an article on `HN <https://news.ycombinator.com>`_ titled `58 Bytes of
CSS to look great nearly everywhere <58 bytes of css_>`_. The article itself
was inspiring as the author was advocating just these 5 lines of CSS for
styling:

.. code-block:: css

    main {
      max-width: 38rem;
      padding: 1.5rem;
      margin: auto;
    }

I then wondered "How could this be?" I looked at the page source. It used a
little more CSS.

.. code-block:: css

    body {
      font-family: Arial, Helvetica, sans-serif;
      background-color: #fffaf7;
      line-height: 1.3;
    }
    main {
      max-width: 38rem;
      padding: 1.5rem;
      margin: auto;
    }
    header {
      margin-bottom: 1.5rem;
    }
    h1 {
      margin-bottom: .5rem;
    }
    time {
      color: #888;
    }
    hr {
      border: none;
      height: 2px;
      background-color: #ddd;
      margin: 2rem auto;
    }
    footer {
      margin-top: 2rem;
      text-align: center;
    }
    a {
      color: #ff3c3c;
      text-decoration: none;
      outline: 0;
    }
    a:hover {
      text-decoration: underline;
    }
    ::selection {
      background-color: #fff888;
    }

The author's `configs page <jrl ninja config_>`_ page had this concoction.

.. code-block:: css

    body {
      font-family: Arial, Helvetica, sans-serif;
      background-color: #fff9fe;
      line-height: 1.3;
    }
    main {
      max-width: 38rem;
      padding: 1.5rem;
      margin: auto;
    }
    header, section {
      margin-bottom: 3rem;
    }
    section h2 {
      margin-bottom: 0;
      line-height: 0.6rem;
    }
    #stack {
      font-size: 75%;
    }
    section p {
      white-space: pre-wrap;
      color: #6c5f6c;
    }
    img {
      margin: 0.2rem;
      opacity: 0.25;
    }
    img:hover {
      opacity: 1;
      cursor: pointer;
    }
    a {
      text-decoration: none;
      outline: 0;
    }
    a:hover {
      text-decoration: underline;
    }
    ::selection {
      background-color: #d2ffdf;
    }

Clearly ``main`` is still there, but I read the article as stating that's all
that was *really* necessary. Why would someone write something so misleading,
especially to novices? He was just unclear. He really meant 58 bytes for layout,
not layout + styling. Still, his count is wrong. It's 63 bytes as written.

Well, at least it provoked `a conversation <58 bytes of css_>`_. `Web Design in
4 minutes <web design in 4 minutes_>`_ was one site cited as an example of
simple web design. It's CSS is quite a bit longer. Still, it's ``main`` layout consists of just:

.. code-block:: css

    main {
      margin: 0 auto;
      max-width: 50em;
      padding: 4em 1em;
    }

NOTE: The author has recently updated his CSS to replace the ``max-width`` and
``padding`` values with ``70ch`` and ``2ch``, respectively (and some other
minor changes). Apparently, ``ch`` for ``max-width`` is more generic and
portable, which means fewer changes to handle mobile devices.
`Some say <https://www.reddit.com/r/css/comments/bb73cw/58_bytes_of_css_to_look_great_nearly_everywhere/ekj8yhm/>`_ a value in the
range of 50-80 characters is optimal. There's an explanation of the 'ch' unit
`here <https://meyerweb.com/eric/thoughts/2018/06/28/what-is-the-css-ch-unit/>`_.
They are not exactly character width, especially if you're not using a
fixed-width font.
They are `defined as <https://drafts.csswg.org/css-values-3/#ch>`_:

  Equal to the used advance measure of the “0” (ZERO, U+0030) glyph found in
  the font used to render it. (The advance measure of a glyph is its advance
  width or height, whichever is in the inline axis of the element.)

So, fonts with a skinny zero might look compact. Be careful about selecting different fonts, say one for headlines and another for body copy. They will likely fill the space very differently.

.. code-block:: css

    body {
      font-family: Liberation Sans, Arial, sans-serif;
      background-color: #fffaf7;
      line-height: 1.3;
    }
    main {
      max-width: 70ch;
      padding: 2ch;
      margin: auto;
    }
    header {
      margin-bottom: 1.5rem;
    }
    h1 {
      margin-bottom: .5rem;
    }
    time {
      color: #888;
    }
    hr {
      border: 2px solid #ddd;
      margin: 2rem auto;
    }
    #fn {
      font-size: 85%;
    }
    footer {
      margin-top: 2rem;
      text-align: center;
    }
    a {
      color: #ff3c3c;
      text-decoration: none;
      outline: 0;
    }
    a:hover {
      text-decoration: underline;
    }
    ::selection {
      background-color: #fff888;
    }

While `content <wdi4m content_>`_ is the first thing one should work on, it got
me wondering about how to structure the content. How much structure is needed
to make content easy to read?

Now I'm reminded of `CSS Zen Garden`_. It was a beautiful experiment in how CSS
could be applied to the same content to create a wide variety of presentations.
How much structure was used there?

It starts with an HTML5 doctype, ``<!DOCTYPE html>``. The ``html`` tag is simply
``<html lang="en">``. The ``<head>...</head>`` section contains a ``<meta>``
tag to define the charset, a ``<title>`` tag, two ``<link>`` tags, one for a
CSS stylesheet and the other for an RSS link:

.. code-block:: html

    <meta charset="utf-8">
    <title>CSS Zen Garden: The Beauty of CSS Design</title>

    <link rel="stylesheet" media="screen" href="style.css?v=8may2013">
    <link rel="alternate" type="application/rss+xml" title="RSS" href="http://www.csszengarden.com/zengarden.xml">

These are followed by four more ``<meta>`` elements to define the viewport,
author, description, and robots data properties.

The ``<body>`` element has only an ``id`` attribute. It's followed by a
``<div>`` element with a ``class`` attribute. This div wraps all of the content
on the page.

Is a ``<main>`` element a substitute for a full-body ``<div>`` wrapper?
`Mozilla MDN web docs <main html element_>`_ says ``<main>`` represents the
dominant content of the ``<body>`` of a document. The example they give shows
other content can both precede and succeed the ``<main>`` element, so it is not
a substitute for a ``<div>`` element that wraps everything.

Is a full-body ``<div>`` wrapper necessary? It is used in the sample CSS to
provide an opportunity for markup. The original `CSS Zen Garden`_ had CSS
definitions for ``<body>`` and the page-wrapper ``<div>`` as follows:

.. code-block:: css

    body {
        font: 75% georgia, sans-serif;
        line-height: 1.88889;
        color: #555753;
        background: #fff url(http://csszengarden.com/001/blossoms.jpg) no-repeat bottom right;
        margin: 0;
        padding: 0;
    }

    .page-wrapper {
        background: url(http://csszengarden.com/001/zen-bg.jpg) no-repeat top left;
        padding: 0 175px 0 110px;
        margin: 0;
        position: relative;
    }

The current front page of `CSS Zen Garden`_ has a more simple style:

.. code-block:: css

    body {
      color: #325050;
      background: #fff;
      font-family: 'Libre Baskerville', sans-serif;
      font-size: 70%;
    }

    .page-wrapper {
      position: relative;
    }

Another source of inspiration is `Gwern's blog <https://www.gwern.net/index>`_. It is beautifully designed and has a lot of the features I want. Considering the sight is written in markdown, it may even be possible for me to use markdown and still get things like a table of contents for each article, and sidebars. Then again, markdown may require manually adding ``<section>``'s and other HTML.

###########################
Anatomy of an HTML Document
###########################

.. code-block:: html

  <!DOCTYPE html>
  <html>
    <head>
      <meta charset="uktf-8">
      <title>My Test Page</title>
    </head>
    <body>
      <p>This is my page</p>
    </body>
  </html>

.. raw:: html

      <p>This is my page</p>

That's an outline of the most basic elements:

* ``<!DOCTYPE html>``
* ``<html>``
* ``<head>``
* ``<body>``

.. _58 bytes of css: https://news.ycombinator.com/item?id=19607169
.. _jrl ninja config: https://jrl.ninja/configs/
.. _web design in 4 minutes: https://jgthms.com/web-design-in-4-minutes/
.. _wdi4m content: https://jgthms.com/web-design-in-4-minutes/#content
.. _css zen garden: http://www.csszengarden.com/
.. _main html element: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main
.. _css zen codepen: https://codepen.io/stephanie08/pen/RoBYBR/
.. _docutils syntax highlighting: http://docutils.sourceforge.net/sandbox/code-block-directive/docs/syntax-highlight.html
.. _docutils pygments long: http://docutils.sourceforge.net/sandbox/stylesheets/pygments-long.css
.. _docutuls pygments default: http://docutils.sourceforge.net/sandbox/stylesheets/pygments-default.css
.. _ducutils stylesheets: http://docutils.sourceforge.net/sandbox/stylesheets/

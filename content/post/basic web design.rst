---
title: "Basic Web Design"
date: 2019-04-09T04:45:15-04:00
draft: true
categories: [design]
tags: [web]
---

How much structure is really needed to make a web page. I have a lot to learn.
<!--more-->

Inspiration
***********

I read an article on `HN <https://news.ycombinator.com>`_ titled `58 Bytes of CSS to look great nearly everywhere <58 bytes of css_>`_. The article itself was inspiring as the author was advocating just these 5 lines of CSS for styling:

.. code-block:: css

    main {
      max-width: 38rem;
      padding: 1.5rem;
      margin: auto;
    }


I then wondered "How could this be?" I looked at the page source. It used a little more CSS.

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

Clearly ``main`` is still there, but I read the article as stating that's all that was *really* necessary. Why would someone write something so misleading, especially to novices?

Well, at least it provoked `a conversation <58 bytes of css_>`_. `Web Design in 4 minutes <web design in 4 minutes_>`_ was one site cited as an example of simple web design. It's CSS is quite a bit longer.

While `content <wdi4m content_>`_ is the first thing one should work on, it got me wondering about how to structure the content. How much structure is needed to make content easy to read?

Now I'm reminded of `CSS Zen Garden`_. It was a beautiful experiment in how CSS could be applied to the same content to create a wide variety of presentations. How much structure was used there?

It starts with an HTML5 doctype, ``<!DOCTYPE html>``. The ``html`` tag is simply ``<html lang="en">``. The ``<head>...</head>`` section contains a ``<meta>`` tag to define the charset, a ``<title>`` tag, two ``<link>`` tags, one for a CSS stylesheet and the other for an RSS link:

.. code-block:: html

    <meta charset="utf-8">
    <title>CSS Zen Garden: The Beauty of CSS Design</title>

    <link rel="stylesheet" media="screen" href="style.css?v=8may2013">
    <link rel="alternate" type="application/rss+xml" title="RSS" href="http://www.csszengarden.com/zengarden.xml">

These are followed by four more ``<meta>`` elements to define the viewport, author, description, and robots data properties.

The ``<body>`` element has only an ``id`` attribute. It's followed by a ``<div>`` element with a ``class`` attribute. This div wraps all of the content on the page.

Is a ``<main>`` element a substitute for a full-body ``<div>`` wrapper? `Mozilla MDN web docs <main html element_>`_ says ``<main>`` represents the dominant content of the ``<body>`` of a document. The example they give shows other content can both precede and succeed the ``<main>`` element, so it is not a substitute for a ``<div>`` element that wraps everything. 

Is a full-body ``<div>`` wrapper necessary? It is used in the sample CSS to provide an opportunity for markup. The original `CSS Zen Garden`_ had CSS definitions for ``<body>`` and the page-wrapper ``<div>`` as follows:

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

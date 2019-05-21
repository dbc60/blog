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

So, fonts with a skinny zero might look compact. Be careful about selecting
different fonts, say one for headlines and another for body copy. They will
likely fill the space very differently.

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

************
Basic Layout
************

I'm starting my layout with the basics from `Web Design in 4 Minutes`_. The
first step is to center the website on the screen and set a maximum line length:

.. code-block:: css

    body {
        margin: 0 auto;
        max-width: 70ch;
    }

The second step is to style the text with a font to make it more readable. `Web
Design in 4 Minutes`_ suggests

.. code-block:: css

    body {
      font-family: "Helvetica", "Arial", sans-serif;
    }

I have a several locally cached fonts from `gwern.net`_, so I chose

.. code-block:: scss

    $base-font-family: "Source Serif Pro", "Helvetica Neue", Helvetica, Arial,  sans-serif;

    body {
      font-family: $base-font-family;
      font-weight: 400;
      font-style: normal;
    }

The next step is to make the text more readable by adjusting the spacing
between lines and headings, as follows:

.. code-block:: css

    body {
      line-height: 1.5;
      padding: 4em 1em;
    }

    h2 {
      margin-top: 1em;
      padding-top: 1em;
    }

The next step adds color and contrast. The author asserts black text on a white
background is harsh on the eyes, so he uses color ``#555`` for body text, and
``#333`` for a couple of headings and strong text:

.. code-block:: css

    body {
      color: #555;
    }

    h1,
    h2,
    strong {
      color: #333;
    }

I disagree with him. I find the lack of contrast makes text more difficult to
read. For more contrast, I wrote:

.. code-block:: scss

    body {
        color: $secondary;
    }

    h1, h2, strong {
      color: $color-text-strong;
    }

and added these SCSS variable definitions:

.. code-block:: scss

    // Variables
    //
    // Variables should follow the `$component-state-property-size` formula for
    // consistent naming.

    // Color system

    $white:    #fff !default;
    $gray-100: #f8f9fa !default;
    $gray-200: #e9ecef !default;
    $gray-300: #dee2e6 !default;
    $gray-400: #ced4da !default;
    $gray-500: #adb5bd !default;
    $gray-600: #6c757d !default;
    $gray-700: #495057 !default;
    $gray-800: #343a40 !default;
    $gray-900: #212529 !default;
    $black:    #000 !default;

    $grays: () !default;
    // stylelint-disable-next-line scss/dollar-variable-default
    $grays: map-merge(
      (
        "100": $gray-100,
        "200": $gray-200,
        "300": $gray-300,
        "400": $gray-400,
        "500": $gray-500,
        "600": $gray-600,
        "700": $gray-700,
        "800": $gray-800,
        "900": $gray-900
      ),
      $grays
    );

    $blue:    #007bff !default;
    $indigo:  #6610f2 !default;
    $purple:  #6f42c1 !default;
    $pink:    #e83e8c !default;
    $red:     #dc3545 !default;
    $orange:  #fd7e14 !default;
    $yellow:  #ffc107 !default;
    $green:   #28a745 !default;
    $teal:    #20c997 !default;
    $cyan:    #17a2b8 !default;

    $colors: () !default;
    // stylelint-disable-next-line scss/dollar-variable-default
    $colors: map-merge(
      (
        "blue":       $blue,
        "indigo":     $indigo,
        "purple":     $purple,
        "pink":       $pink,
        "red":        $red,
        "orange":     $orange,
        "yellow":     $yellow,
        "green":      $green,
        "teal":       $teal,
        "cyan":       $cyan,
        "white":      $white,
        "gray":       $gray-600,
        "gray-dark":  $gray-800
      ),
      $colors
    );

    $primary:       $blue !default;
    $secondary:     $gray-900 !default;

The next step adds a nice light gray background to code and ``<pre></pre>``
sections:

.. code-block:: css

    code,
    pre {
      background: #eee;
    }

    code {
      padding: 2px 4px;
      vertical-align: text-bottom;
    }

    pre {
      padding: 1em;
    }

Next we use the primary color to add a visual accent to links. The author of
`Web Design in 4 Minutes`_ uses a redish color:

.. code-block:: css

    a {
      color: #e81c4f;
    }

I used my primary color, defined above:

.. code-block:: scss

    a {
      color: $primary;
    }

Next, `Web Design in 4 Minutes`_ says the accent color can be complimented with
more subtle shades to be used on borders, background, and even body text. To do
that, the author presents us with CSS which sets the color of body text, and
creates colored borders on code and monospaced text in ``<pre></pre>`` blocks.
The body text is now a slightly bluish gray. While the normal background is
white, the background for ``pre`` and code sections is a light bluish gray. The
left border is a deep blue, while the bottom border is only one pixel wide, and
a subtley darker bluish gray:

.. code-block:: css

    body {
      color: #566b78;
    }

    code,
    pre {
      background: #f5f7f9;
      border-bottom: 1px solid #d8dee9;
      color: #a7adba;
    }

    pre {
      border-left: 2px solid #69c;
    }

My primary color is a shade of blue (``#007bff``), so I chose different
complimentary colors. By this reasoning, I should update the colors of the text
for ``body``,``code`` and ``pre`` sections, and the background color of ``code``
and ``pre`` sections.

Well, now I'm running into a puzzle. The suggestions have morphed into 7 color
categories.

#. background: defaults to white.
#. accent: #e81c4f, a redish color for links and probably some other little
   things.
#. complimentary: #566b78, a blue-gray color to compliment the accent and be
   used on body text.
#. section-background: #f5f7f9, a light-gray or off-white color used for
   background on code and pre sections.
#. section-text: #a7adba, a medium-gray color for text in code and pre sections.
#. seciont-border-bottom: #d8dee9, a slightly darker grayish color for the
   bottom-border of code and pre sections.
#. section-border-left: a brighter bluish-gray for the left-border of code and
   pre sections.

What I don't understand is why these colors were chosen, what is the intent for
their general usage, and why seven colors? Other sites that talk about `color
palettes <https://www.websitebuilderexpert.com/designing-websites/
how-to-choose-color-for-your-website/>`_ `suggest fewer <https://
www.smashingmagazine.com/2016/04/web-developer-guide-color/>`_ colors, in the
range of four to six. Also, pink (#e83e8c) is an awful accent color.

Following `A Simple Web Developer's Color Guide <https://
www.smashingmagazine.com/2016/04/web-developer-guide-color/>`_, I decided I
like a light-grayish yellow (#f2eee2) as a base color. I'll eventually navigate
over to `Paletton <http://paletton.com/>`_ and choose an accent (complimentary)
color. It came up with #f2eee2, which is a purpley gray.

There are too many variables and considerations to add color quickly. I
simplified by going with a white background and black text. I used blue
(#007bff) for the accent (link coloring) and a bright highlight. The dark
highlight is ``$gray-400`` (``#ced4da``), the background for ``code`` and
``pre`` sections is ``$gray-100`` (``#f8f9fa``).

*********
Reference
*********

* `Why Programmers Suck at Picking Colors`_
* `Using Color in Information Display Graphics`_
  * `Designing a Color Graphics Page`_
  * `Heirarchy of Color Usage Guidelines`_
* `Munsell Color System`_
* `CIELab color space`_
* `CIECAM02`_

.. _gwern.net: https://www.gwern.net/index
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
.. _using color in information display graphics: https://colorusage.arc.nasa.gov/
.. _designing a color graphics page: https://colorusage.arc.nasa.gov/graphics_page_design.php
.. _heirarchy of color usage guidelines: https://colorusage.arc.nasa.gov/GuidelinesHierarchy.php
.. _munsell color system: https://en.wikipedia.org/wiki/Munsell_color_system
.. _cielab color space: https://en.wikipedia.org/wiki/CIELAB_color_space
.. _ciecam02: https://en.wikipedia.org/wiki/CIECAM02
.. _why programmers suck at picking colors: https://web.archive.org/web/20150311143508/http://www.betaversion.org/~stefano/linotype/news/108

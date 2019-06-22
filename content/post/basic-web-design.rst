---
title: "Basic Web Design"
date: 2019-04-13T04:45:15-04:00
categories: [software]
tags: [design, web]
cssDetail: "drop-caps_goudy"
---

How much structure is really needed to make a web page. I have a lot to learn.
<!--more-->

###########
Inspiration
###########

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

It starts with an HTML5 doctype, ``<!DOCTYPE html>``. The ``html`` tag is
simply ``<html lang="en">``. The ``<head>...</head>`` section contains a
``<meta>`` tag to define the charset, a ``<title>`` tag, two ``<link>`` tags,
one for a CSS stylesheet and the other for an RSS link:

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

Another source of inspiration is `Gwern's blog <https://www.gwern.net/index>`_.
It is beautifully designed and has a lot of the features I want. Considering
the sight is written in markdown, it may even be possible for me to use
markdown and still get things like a table of contents for each article, and
sidebars. Then again, markdown may require manually adding ``<section>``'s and
other HTML.

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
first step is to center the website on the screen and set a maximum line
length:

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
#. section-text: #a7adba, a medium-gray color for text in code and pre
   sections.
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

######################
Block Element Modifier
######################

The `Block Element Modifier <bem methodology_>`_ is a way to organize web page design and development. Blocks are the primary unit of organization. As such, each block is stored in a separate folder, and each technology (e.g., HTML or CSS) is represented by a separate file in the folder. Also, each block has documentation contained in a ``.wiki`` file inside the folder.

*******************************
Directory Structure Conventions
*******************************

Block implementations consist of separate files. Each technology (HTML, CSS,
etc.) gets its own file. For example, if the appearance of the ``input`` block
is defined using CSS, the code is stored in the ``input.css`` file.
::

    project
        common.blocks/
            input.css   # CSS implementation of the input block
            input.js    # JavaScript implementation of the input block

The code of modifiers and elements is also stored in separate files of the
block. This approach allows you to include just the modifiers and elements
that are needed for this implementation of the block.
::

    project
        common.blocks/
            input.css            # CSS implementation of the input block
            input.js             # JavaScript implementation of the input block
            input_theme_sun.css  # Implementation of the input_theme_sun modifier
            input__clear.css     # CSS implementation of the input__clear element
            input__clear.js      # JavaScript implementation of the input__clear element

Files are grouped by meaning, not by type. Each block has a directory with the
name of the block that contains the files for implementing the block.

In some approaches to file structure organization, block directories are not
used. In this case, the block files are grouped using a namespace that is set
as the block name.
::

    project
        common.blocks/
            input/            # Directory for the input block
                input.css     # CSS implementation of the input block
                input.js      # JavaScript implementation of the input block
            popup/            # Directory for the popup block
                popup.css     # CSS implementation of the popup block
                popup.js      # JavaScript implementation of the popup block

To improve navigation across the project, block modifiers with multiple values
can also be combined in separate directories.
::

    project
        common.blocks/                     # Redefinition level with blocks
            input/                         # Directory for the input block
                _type/                     # Directory for the input_type modifier
                    input_type_search.css  # CSS implementation of the input_type modifier
                    input_type_pass.css    # CSS implementation of the input_type modifier
                input.css                  # CSS implementation of the input block
                input.js                   # JavaScript implementation of the input block
            popup/                         # Directory for the popup block

Approaches
==========

The approaches to folder structure are:

* Nested
* Flat
* Flex

Nested
------

This is the classic file structure approach for BEM projects:

* Each block corresponds to a single directory.
* The code of modifiers and elements is stored in separate files.
* The files of modifiers and elements are stored in separate directories.
* The block directory is the root directory for the subdirectories of its
  elements and modifiers.
* Names of element directories begin with a double underscore (``__``).
* Names of modifier directories begin with a single underscore (``_``).

::

    project
        common.blocks/                            # Redefinition level with blocks
            input/                                # Directory for the input block
                _type/                            # Directory for the input_type modifier
                    input_type_search.css         # CSS implementation of the input_type modifier
                __clear/                          # Directory for the input__clear element
                    _visible/                     # Directory for the input__clear_visible modifier
                        input__clear_visible.css  # CSS implementation of the input__clear_visible modifier
                    input__clear.css              # CSS implementation of the input__clear element
                    input__clear.js               # JavaScript implementation of the input__clear element
            input.css                             # CSS implementation of the input block
            input.js                              # JavaScript implementation of the input block

The nested approach is used in the file structure of BEM libraries:

* bem-core
* bem-components

Flat
----

Simplified structure for the file structure:

* Directories aren't used for blocks.
* Optional elements and modifiers are implemented in separate files or in the
  main block file.

::

    project
        common.blocks/
            input_type_search.css     # The input_type_search modifier in CSS
            input_type_search.js      # The input_type_search modifier in JavaScript
            input__clear.js           # Optional element of the input block
            input.css
            input.js
            popup.css
            popup.js
            popup.png

Flex
----

The most flexible approach is a combination of flat and nested. Blocks with a
branched file structure used the nested approach. Simple blocks use the flat
approach. How it works:

* Each block corresponds to a separate directory.
* Elements and modifiers can be implemented in block files or in separate
  files.

::

    project
        common.blocks/
            input/                                # Directory for the input block
                _type/                            # Directory for the input_type modifier
                    input_type_search.css         # CSS implementation of the input_type modifier
                __clear/                          # Directory for the input__clear element
                    _visible/                     # Directory for the input__clear_visible modifier
                        input__clear_visible.css  # CSS implementation of the input__clear_visible modifier
                    input__clear.css              # CSS implementation of the input__clear element
                    input__clear.js               # JavaScript implementation of the input__clear element
                input.css                         # CSS implementation of the input block
                input.js                          # JavaScript implementation of the input block
            popup/                                # Directory for the popup block
                popup.css
                popup.js
                popup.png

*****************
Naming Convention
*****************

* Names are written in lowercase Latin letters.
* Words within names are separated by a hyphen (``-``).
* The block name specifies a namespace for its elements and modifiers.
* The element name is separated from the block name by a double underscore
  (``__``).
* The modifier name is separated from the block or element name by a single
  underscore (``_``).
* The modifier value is separated from the modifier name by a single
  underscore (``_``).
* For boolean modifiers, the value is not included in the name.

I wonder if it might be wise to use an explicit, but optional, namespace in
addition to the block name. Wouldn't it be needed to avoid a collision between
libraries and our own custom components?

Block Example
=============

Here is an example of a block in HTML and CSS. The block is a CSS class used
in an HTML element.

.. code-block:: html

    <div class="menu">...</div>

.. code-block:: css

    .menu { color: red; }

Element Example
===============

An element cannot exist outside of a block, and its name is appended to its
parent block with two underscores as a separator. For example ``menu__name``
is a valid name for an ``item`` contained in a ``menu`` block.

.. important::

    Important: Identical elements in the same block have the same name. For
    example, all menu items in the menu block are called ``menu__item``.

Here is an example of an element in HTML and CSS.

.. code-block:: html

    <div class="menu">
        ...
        <span class="menu__item"></span>
    </div>

.. code-block:: css

    .menu__item { color: red; }

Block Modifier Example
======================

Here are two examples of valid block modifier names where the block is menu
and the modifier is separated from the menu by an underscore. The first one is
a boolean, so it has no value. The name of the second one is ``theme`` with a
modifier value of ``islands``::

    menu_hidden

    menu_theme_islands

Here are how the two block modifiers are represented in HTML and CSS.

HTML:

.. code-block:: html

    <div class="menu menu_hidden"> ... </div>
    <div class="menu menu_theme_islands"> ... </div>

CSS:

.. code-block:: css

    .menu_hidden { display: none; }
    .menu_theme_islands { color: green; }

Element Modifier Example
========================

Here a two examples of element modifiers. Note the block and element are both
part of the modifier name. Again, the first one is a boolean, so the modifier
has an intrinsic value of ``true``, and in the second the modifier value
follows its name and is separated by an underscore::

    menu__item_visible

    menu__item_type_radio

Here is how these element modifiers are defined in HTML and CSS.

HTML:

.. code-block:: html

    <div class="menu">
        ...
        <span class="menu__item menu__item_visible menu__item_type_radio"> ... </span>
    </div>

CSS:

.. code-block:: css

    .menu__item_visible {}
    .menu__item_type_radio { color: blue; }

******************************
Alternative Naming Conventions
******************************

There are a few alternative naming conventions used among those who adhere to
the BEM method.

* Two-dash Style
* CamelCase Style
* React Style
* No Namespace Style

Two-dash Style
==============

``block-name__elem-name--mod-name--mod-val``

* Names are written in lowercase Latin letters.
* Words within the names of BEM entities are separated by a hyphen (``-``).
* The element name is separated from the block name by a double underscore
  (``__``).
* Boolean modifiers are separated from the name of the block or element by a
  double hyphen (``--``).
* The value of a modifier is separated from its name by a double hyphen
  (``--``).

CamelCase Style
===============

``blockName-elemName_modName_modVal``

* Names are written in Latin letters.
* Each word inside a name begins with an uppercase letter.
* The separators for names of blocks, elements, and modifiers are the same as
  in the standard scheme.

React Style
===========

``BlockName-ElemName_modName_modVal``

* Names are written in Latin letters.
* Names of blocks and elements begin with an uppercase letter. Names of
  modifiers begin with a lowercase letter.
* Each word inside a name begins with an uppercase letter.
* An element name is separated from the block name by a single hyphen (``-``).
* The separators between names and values of modifiers are the same as in the
  standard scheme.

No Namespace Style
==================

``_available``

* Names are written in Latin letters.
* The name of the block or element is not included before the modifier.

This naming scheme limits the use of mixes, because it makes it impossible to
determine which block or element a modifier belongs to.

*****
Mixes
*****

A mix is an instance of different BEM entities being hosted on a single DOM
node. Mixes allow us to

* Combine the behaviors and styles of several BEM entities while avoiding code
  duplication.
* Create semantically new interface components on the basis of existing BEM
  entities.

Consider the case of a mix comprising a block and an element of another block.
Assume that links in your project are implemented via a ``link`` block. We
need to format menu items as links. There are several ways to do that.

* Create a modifier for a menu item that turns the item into a link.
  Implementing such a modifier would necessarily involve copying the behavior
  and styles of the ``link`` block. That would result in code duplication.
* Have a mix combining a generic ``link`` block and a ``link`` element of a
  ``menu`` block. A mix of the two BEM entities will allow us to use the basic
  link functionality of the ``link`` block and additional CSS rules of the
  ``menu`` block without copying the code.

***********
Definitions
***********

Block Implementation
====================

A set of different technologies that determine the following aspects of a BEM
entity:

* behavior
* appearance
* tests
* templates
* documentation
* description of dependencies
* additional data (e.g., images)

Block Redefinition
==================

Modifying a block implementation by adding new features to the block on a
different level.

Redefinition Level
==================

A set of BEM entities and their partial implementations.

The final implementation of a block can be divided into different redefinition
levels. Each new level extends or overrides the original implementation of the
block. The end result is assembled from individual implementation technologies
of the block from all redefinition levels in a pre-determined consecutive
order.

Any implementation technologies of BEM entities can be redefined.

For example, there is a third-party library linked to a project on a separate
level. The library contains ready-made block implementations. The
project-specific blocks are stored on a different redefinition level.

Let's say we need to modify the appearance of one of the library blocks. That
doesn't require changing the CSS rules of the block in the library source code
or copying the code at the project level. We only need to create additional
CSS rules for that block at the project level. During the build process, the
resulting implementation will incorporate both the original rules from the
library level and the new styles from the project level.

##########
Components
##########

Building a web UI is more than a CSS problem. Beyond building anything trivial,
developers have difficulties trying to do things that are not just related to
building an application or adapting widgets. Developers spend more time
managing assets and their dependencies to avoid making changes in one place
that cause unexpected changes in what appeared to be an unrelated part of the
application.

Components help to define an interface for widgets and isolate their
implementations. Thus it becomes easier to reason about the application.

A component is a module that encapsulates a set of related functions. It
includes behavior, presentation, and the logic that determines when certain
presentations are displayed.

Use a component as a primary unit of scale. A prefabricated component is more
than just CSS. It is everything you need to create that widget. You end up with
HTML, CSS, JavaScript (JS), possibly images, and other assets.

Each component should have a directory with all the assets it needs. One of the
characteristics of components is that they are simpler abstraction than
modules, because modules are not a concept of how you assemble various
technologies into one widget. Also, components are composable through their
interfaces and a compositional model.

Note that simple does not mean easy. It refers to a lack of complexity. There's
a lack of entanglement in the system. It's about component A not knowing how
component B is made, and instead using the interface the component provides.

Think about composabilty of just reusability when designing components. Mere
reusability leads to entanglement. So, be careful when pulling apparently
common items from components into reusable objects. It can lead to complexity
and entanglement when the components diverge, and what was once common needs to
be specialized for each component.

*******************************
Tools supporting Web Components
*******************************

* Define components with `React <https://facebook.github.io/react>`_
* Style components with `SUIT CSS <https://suitcss.github.io>`_. It is a
  modular, simple set of tools which try to make it easier to style components.
  Instead of managing large CSS files, you can think about just the CSS you
  need for a particular component, and then you can compose more complicated
  interfaces from a variety of composable components.
* Manage components with `Component <https://github.com/componnet/component>`_,
  which is a node.js tool. Use it by defining your assets and
  dependent-components for a comonent in a ``component.json`` file. The tool
  will track dependendencies among components, which is particularly useful for
  CSS, because order is important.

#########
Reference
#########

* `Why Programmers Suck at Picking Colors`_
* `Using Color in Information Display Graphics`_
  * `Designing a Color Graphics Page`_
  * `Heirarchy of Color Usage Guidelines`_
* `Munsell Color System`_
* `CIELab color space`_
* `CIECAM02`_
* `Enduring CSS`_ A Guide to Writing Style Sheets for Large Scale, Rapidly
   Changing, Long-ived Web Projects.
* `Enduring CSS blog post`_
* `Nicolas Gallagher - Adaptation and Components <adaptation and components
  video_>`_ video on YouTube.
* `Nicolas Gallagher <http://nicolasgallagher.com/>`_
* `BEM Methodology`_
* `Enduring CSS`_
* `Enduring CSS Blog Post`_
* `Battling BEM CSS`_: 10 Common Problems and How to Avoid Them.
* `Scaling Down the BEM for Small Projects <bem for small projects_>`_.
* `Code Guide for Sustainable HTML and CSS <code guide for html and css_>`_
* `Atomic CSS`_
* * `Block Element Module <bem_>`_

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
.. _enduring css: https://ecss.io/
.. _enduring css blog post: https://benfrain.com/enduring-css-writing-style-sheets-rapidly-changing-long-lived-projects/
.. _adaptation and components video: https://www.youtube.com/watch?v=m0oMHG6ZXvo
.. _bem: https://en.bem.info/
.. _bem methodology: https://en.bem.info/methodology/
.. _pep8 max line length: https://www.python.org/dev/peps/pep-0008/#maximum-line-length
.. _shoot to kill css selector intent: https://csswizardry.com/2012/07/shoot-to-kill-css-selector-intent/
.. _battling bem css: https://www.smashingmagazine.com/2016/06/battling-bem-extended-edition-common-problems-and-how-to-avoid-them/
.. _bem for small projects: https://www.smashingmagazine.com/2014/07/bem-methodology-for-small-projects/
.. _code guide for html and css: https://codeguide.co
.. _atomic css: https://acss.io/

---
title: "Hugo Blog Styling"
date: 2019-06-11T07:29:40-04:00
draft: true
categories: [blog]
tags: [html, css]
cssDetail: "drop-caps_cheshire"
---

I am going to try applying naming convention of the `Block Element Modifier <bem_>`_ methodology and the file/folder organization advice from `Enduring CSS <https://ecss.io/>`_ to organize my Sass, CSS, and HTML templeates.

The first question is, will Hugo and Sass support organizing components by
directory? Suppose I want a navigation menu with navigation items. The
template, ``nav.html`` is stored in the ``layouts/partials/`` folder. I also
have several ``.scss`` files in ``assets/scss/``. On top of that, the
individual items that go in the nav menu are defined in ``config/_default/
config.toml`` as:

.. code-block::

    # See https://feathericons.com/
    # The value of pre is the icon name
    [menu]
      [[menu.nav]]
        name = "Home"
        pre = "home"
        url = "/"
        weight = 1
      [[menu.nav]]
        name = "Notes"
        pre = "edit"
        url = "/note/"
        weight = 2
      [[menu.nav]]
        name = "About"
        pre = "smile"
        url = "/about/"
        weight = 3
      [[menu.nav]]
        name = "Now"
        pre = "coffee"
        url = "/now/"
        weight = 4
      [[menu.nav]]
        name = "Tags"
        pre = "tag"
        url = "/tags/"
        weight = 5
      [[menu.nav]]
        name = "Categories"
        pre = "bookmark"
        url = "/categories"
        weight = 6
      [[menu.nav]]
        name = "RSS"
        pre = "rss"
        url = "/index.xml"
        weight = 7

One person uses ``layouts/TYPE/block.html`` that usually contains one ``<div
class="TYPE">`` element to emulate the concept of a block in the BEM
methodology. He also has a ``static/TYPE.styl`` that gets compiled to
``TYPE.css``. While not quite BEM, it's a start.

Hugo has `a roadmap <hugo 1.0 roadmap_>`_. It's worth consulting before I get too deeply involved in making modifications to Hugo.

*********
Drop Caps
*********

My current drop-cap styles:

* drop-caps_cheshire    => ``drop-caps_cheshire``
* drop-caps_goudy       => ``drop-caps_goudy``
* drop-caps_de-zs       => ``drop-caps_de-zs``
* drop-caps_yinit       => ``drop-caps_yinit``

If I want to make a drop-caps component, I need to create a
``layouts/drop-caps`` folder. Each of my styles would be a modifier (or maybe
an element). Due to constraints of Hugo, they'd be placed in
``static/_<modifier-name>`` or some similar name. They can't be placed in the
``layouts/drop-caps`` folder because the CSS files need to be copied to the
``/public`` folder. Only files in ``static/`` are automatically copied. Should
the modifier carry the block in its name? For example, which of the following
naming conventions should the ``_chesire`` modifier be?

* ``static/_cheshire/_cheshire.css``
* ``static/drop-caps/_chesire.css``
* ``static/drop-caps_cheshire/modifier.css``
* ``static/modifier/_cheshire.css``
* ``static/modifier/drop-caps_cheshire.css``

Reconsidering the block part, the HTML needs to be under the ``layouts/``
folder, but could be organized in one of several ways.

* ``layouts/drop-caps/drop-caps.html``
* ``layouts/block/drop-caps.html``
* ``layouts/drop-caps.html``
* ``layouts/drop-caps/block.html``
* ``layouts/partials/block/drop-caps.html``
* ``layouts/partials/drop-caps/block.html``

With Hugo's constraints, I kind of like:

* ``layouts/partials/drop-caps.html``
* ``static/drop-caps/drop-caps.css``
* ``static/drop-caps/drop-caps_goudy.css``
* ``static/drop-caps/drop-caps_cheshire.css``

Simiilarly colors for the drop-caps block would be modifiers, such as ``static/
modifier/drop-caps_green.css``.

When should layout HTML be placed in a subdirectory of ``layouts`` and when
should it be placed under ``layouts/partials``? I think the answer is to place
HTML under a subdirectory of ``layouts/`` when there is content in a
subdirectory of the ``contents`` folder. Use ``layouts/partials`` when an HTML
template includes the partial using the
``{{ partial "<PATH>/<PARTIAL>.html" . }}`` action.

When Hugo looks for a partial template, it checks just two places:

#. ``layouts/partials/*<PARTIALNAME>.html``
#. ``themes/<THEME>/layouts/partials/*<PARTIALNAME>.html``

The second argument is a dot (``.``). It gives the partial a "context". In Go
Templates, ``{{ . }}`` always refers to the *current context*. In the top
level of your template, this will be the data set made available to it. Inside
of an iteration, however, it will have the value of the current item in the
loop; i.e., ``{{ . }}`` will no longer refer to the data available to the
entire page.

If you need to access page-level data (e.g., page params set in front matter)
from within the loop, you will likely want to do one of the following (See `Introduction to Hugo Templating <https://gohugo.io/templates/introduction/>`_ for details):

#. Define a variable independent of context outside the loop; e.g.,
   ``{{ $title := .Site.Title }}``, and then reference ``$title`` inside the
   loop.
#. Use ``$.`` to access the global context; e.g., ``{{ $.Site.Title }}``
   inside a loop.

.. _bem: https://en.bem.info/
.. _hugo 1.0 roadmap: https://discourse.gohugo.io/t/roadmap-to-hugo-v1-0/2278

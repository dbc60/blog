---
title: "Hugo Blog Styling"
date: 2019-06-11T07:29:40-04:00
draft: true
categories: [blog]
tags: [html, css]
---

I'm going to try applying naming convention of the `Block Element Modifier <bem_>`_ methodology and the file/folder organization advice from `Enduring CSS <https://ecss.io/>`_ to organize my Sass, CSS, and HTML templeates.

<!--more-->

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

.. _bem: https://en.bem.info/

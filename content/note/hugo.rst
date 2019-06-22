---
title: "Hugo"
date: 2019-06-12T07:18:40-04:00
draft: true
categories: [web]
tags: [hugo]
cssDetail: "drop-caps_yinit"
summary: Some notes on Hugo, a static site generator.
---

`Hugo`_ has an extended version that seems to be for supporting Sass/SCSS.  It
adds ``toCSS`` to the ``resources`` object. Vanilla Hugo doesn't have that
method.

The `0.43 release <https://gohugo.io/news/0.43-relnotes/>`- announced you need
the extended version only if you want to edit SCSS. Hugo extended places
generated output files in ``/resources/_gen/``. For example, the `Fresh theme <https://themes.gohugo.io/hugo-fresh/>`_ generates assets like
``/resources/_gen/assets/sass/style.sass_cf66e63debe6917c04534d6c7b66f623.json``.

One person (lost the link) uses hugo-extended for "SASS/SCSS support without
any additional tooling or configuration. Beats wrangling with Webpack, etc."

These were `listed in the forum <https://discourse.gohugo.io/t/should-i-use-hugo-extended-for-a-new-hugo-project/13954/3>`_, but they can all be done on the basic version:

* Minify - that’s my main use case.
* Resource catenation - my other main use case. Lets you keep code neatly
  arranged in source files but bundled for production efficiency.
* Fingerprinting/Subresource Integrity - useful for security.
* Source maps - useful for debugging.
* Image processing.
* PostCSS - never used it but sounds like it is useful for some people.

You can use themes that use SASS/SCSS with the regular version provided that
they have added the compiled styles to ``/resources`` in the theme

Sass was originally written in Ruby. Hugo Extended has a SASS parser included
so you do not need to install Ruby.

####################
Creating New Content
####################

Make an `archetype <https://gohugo.io/content-management/archetypes/>`_ so ``hugo new`` creates files with all the desired frontmatter. The default creates files with ``date``, ``title``, and ``draft = true``.

##########
Hugo Pipes
##########

The ``/assets`` directory is used to store all the files which need to be processed by `Hugo Pipes <https://gohugo.io/hugo-pipes/>`_. It is not created by default, so users will have to manually create it to use pipes. Only the files referenced by ``.Permalink`` or ``.RelPermalink`` in other files will be published to the ``public`` directory.

******************
Hugo Configuration
******************

There seems to be two directories for storing configuration data. The first is the ``/config`` directory. The `documentation for directories <https://gohugo.io/getting-started/directory-structure/>`_ says:

    Hugo ships with a large number of `configuration directives <https://gohugo.io/getting-started/configuration/#all-variables-yaml>`_. The `config directory <https://gohugo.io/getting-started/configuration/#configuration-directory>`_ is where those directives are stored as JSON, YAML, or TOML files. Every root setting object can stand as its own file and structured by environments. Projects with minimal settings and no need for environment awareness can use a single ``config.toml`` file at its root.

    Many sites may need little to no configuration, but Hugo ships with a large number of `configuration directives <https://gohugo.io/getting-started/configuration/#all-variables-yaml>`_ for more granular directions on how you want Hugo to build your website. Note: assets directory is not created by default.

The other directory is the ``/data`` directory. The docs say:

    This directory is used to store configuration files that can be used by Hugo when generating your website. You can write these files in YAML, JSON, or TOML format. In addition to the files you add to this folder, you can also create `data templates <https://gohugo.io/templates/data-templates/>`_ that pull from dynamic content.

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

#############
Building Hugo
#############

Hugo Extended can be built and installed in a single command:

.. code-block:: bat

    go install --tags extended

Remove ``--tags extended`` if you do not want/need Sass/SCSS support.

Alternatively, run ``go build`` or go build --tags extended`` to just build
Hugo without installing it.

When I run ``go build --tags extended``, the output is:

.. code-block:: bat

    # github.com/wellington/go-libsass/libs
    cc1.exe: sorry, unimplemented: 64-bit mode not compiled in

.. _hugo: https://gohugo.io

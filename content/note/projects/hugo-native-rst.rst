---
title: "Hugo Native Rst"
date: 2019-05-24T08:36:34-04:00
draft: true
categories: [projects]
tags: [software, hugo, golang]
---

The goal is to create a better parser for content files marked up with
reStructuredText (reST).
<!--more-->

Currently Hugo launches a Python script, `rst2html5`_ as an external agent to
parse reST files. While a good first step, it has several shortcomings. In
particular, it doesn't process ``.. math::`` blocks in such a way that MathJax
can format them correctly. Also, it would be nice if it had more of Sphinx'
capabilities, such as defining links between content files and defining custom
roles.

*********
Reference
*********

* `Hugo Contribution Workflow`_
* `rst2html5`_
* `go-rst <demizer go-rst_>`_
* `hhatto gorst`_
* `reStructuredText <rst_>`_, the markup syntax and parser component of `DocUtils`_
* `Guidelines for Contributing to Hugo`_
* `Lexical Scanning in Go slides`_
* `Lexical Scanning in Go YouTube video`_

Open Issues Related to reStructuredText
***************************************

* `reST uses Long Token Names for Syntax Highlighting`_
* `Use short token for code highlighting`_
* `Add support for native Go implmentation of reST`_

.. _rst: http://docutils.sourceforge.net/rst.html
.. _docutils: http://docutils.sourceforge.net/index.html
.. _rst2html5: https://pypi.org/project/rst2html5/
.. _demizer go-rst: https://github.com/demizer/go-rst
.. _hhatto gorst: https://github.com/hhatto/gorst
.. _hugo contribution workflow: https://gohugo.io/contribute/development/#the-hugo-git-contribution-workflow
.. _guidelines for contributing to hugo: https://github.com/gohugoio/hugo/blob/master/CONTRIBUTING.md
.. _reST uses long token names for syntax highlighting: https://github.com/gohugoio/hugo/issues/5349
.. _use short token for code highlighting: https://github.com/gohugoio/hugo/pull/5350
.. _add support for native Go implementation of reST: https://github.com/gohugoio/hugo/issues/1436
.. _lexical scanning in go slides: https://talks.golang.org/2011/lex.slide#1
.. _lexical scanning in go youtube video: https://www.youtube.com/watch?v=HxaD_trXwRE

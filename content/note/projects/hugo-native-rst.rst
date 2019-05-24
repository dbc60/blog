---
title: "Hugo Native Rst"
date: 2019-05-24T08:36:34-04:00
draft: true
---

The goal is to create a better parser for content files marked up with
reStructuredText (rST).
<!--more-->

Currently Hugo launches a Python script, `rst2html5`_ as an external agent to
parse rST files. While a good first step, it has several shortcomings. In
particular, it doesn't process ``.. math::`` blocks in such a way that MathJax
can format them correctly. Also, it would be nice if it had more of Sphinx'
capabilities, such as defining links between content files and defining custom
roles.

*********
Reference
*********

* `rst2html5`_
* `go-rst <demizer go-rst_>`_
* `hhatto gorst`_
* `reStructuredText <rst_>`_, the markup syntax and parser component of `DocUtils`_

.. _rst: http://docutils.sourceforge.net/rst.html
.. _docutils: http://docutils.sourceforge.net/index.html
.. _rst2html5: https://pypi.org/project/rst2html5/
.. _demizer go-rst: https://github.com/demizer/go-rst
.. _hhatto gorst: https://github.com/hhatto/gorst

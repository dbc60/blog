---
title: "Hugo Native reStructuredText"
date: 2019-05-24T08:36:34-04:00
draft: true
categories: [project]
tags: [hugo, golang, software]
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

********************
A Note on goroutines
********************

I found `this note <https://groups.google.com/forum/#!msg/golang-nuts/q--5t2cxv78/Vkr9bNuhP5sJ>`_ on the go-nuts Google group:

    When Rob `held that talk <lexical scanning in go youtube video_>`_, there
    was a restriction in Go that meant that a goroutine started during
    initialization might not run to completion. That restriction was lifted, so
    you can omit the presented workaround, if you'd like so. The text/template
    package has a slightly revised version of the lexer presented in the talk.

So, it's no longer necessary to make that odd ``nextItem()`` function that
pulled tokens from the channel or kept the state machine running.

Rob Pike also commented, stating:

    That talk was about a lexer, but the deeper purpose was to demonstrate how
    concurrency can make programs nice even without obvious parallelism in the
    problem. And like many such uses of concurrency, the code is pretty but not
    necessarily fast.

    I think it's a fine approach to a lexer if you don't care about
    performance. It is significantly slower than some other approaches but is
    very easy to adapt. I used it in ivy, for example, but just so you know,
    I'm probably going to replace the one in ivy with a more traditional model
    to avoid some issues with the lexer accessing global state. You don't care
    about that for your application, I'm sure.

    So: It's pretty and nice to work on, but you'd probably not choose that
    approach for a production compiler.

    -rob

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
* `A look at Go lexer/scanner packages <go lexer-scanner packages_>`_
* `Writing a Lexer and Parser in Go - Part 1`_
* `Writing a Lexer and Parser in Go - Part 2`_
* `Writing a Lexer and Parser in Go - Part 3`_
* `Handwritten Parsers and Lexers in Go`_
* `Some Strategies for Fast Lexical Analysis`_
* `Git Searching Issues and PRs`_
* `Hugo Starter Kits`_
* `Fountain Markup`_ is a markup language used for screenwriting. It might be
  interesting to make a Fountain parser plug-in for Hugo. Someone suggested
  assigning `.fou` as a default file extension, much like `.md` and
  `.markdown` are used for markdown files. They're all plain text in the end,
  but it's nice to have a file extension as a hint to the format of a file's
  content.

Open Issues Related to reStructuredText
***************************************

* `reST uses Long Token Names for Syntax Highlighting`_
* `Use short token for code highlighting`_
* `Add support for native Go implementation of reST`_

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
.. _go lexer-scanner packages: https://arslan.io/2015/10/12/a-look-at-go-lexerscanner-packages/
.. _writing a lexer and parser in Go - part 1: https://web.archive.org/web/20160204130813/http://www.adampresley.com/2015/04/12/writing-a-lexer-and-parser-in-go-part-1.html
.. _writing a lexer and parser in go - part 2: https://web.archive.org/web/20160203233801/http://adampresley.com/2015/05/12/writing-a-lexer-and-parser-in-go-part-2.html
.. _writing a lexer and parser in go - part 3: https://web.archive.org/web/20160204184840/http://adampresley.com/2015/06/01/writing-a-lexer-and-parser-in-go-part-3.html
.. _handwritten parsers and lexers in go: https://blog.gopheracademy.com/advent-2014/parsers-lexers/
.. _some strategies for fast lexical analysis: http://nothings.org/computer/lexing.html
.. _git searching issues and prs: https://help.github.com/en/articles/searching-issues-and-pull-requests#search-by-the-title-body-or-comments
.. _hugo starter kits: https://gohugo.io/tools/starter-kits/
.. _fountain markup: https://fountain.io/

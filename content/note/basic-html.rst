---
title: "Basic Html"
date: 2019-04-11T07:34:55-04:00
categories: [web]
---

.. |--| unicode:: U+2013   .. en dash
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Mozilla has an `Introduction to CSS <mdn intro css_>`_ course as well as an `Introduction to HTML <mdn intro html_>`_ course.

<!--more-->

******************
Dealing with Files
******************

`Dealing with files
<https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/
Dealing_with_files>`_ provides some conventions on file names and directory
structure. I renamed several files, replacing spaces in their names with dashes.

This site is built by `Hugo`_, so folders such as ``images``, ``styles``, and
``scripts`` are under the ``static`` directory. I renamed ``static/js`` to
``static/scripts`` to mirror the MDN convention.

******************
Learn Me Some HTML
******************

My goal is to really understand the structure of my site, so I know where
things are and what needs to be modified as I build it to look the way I want it to. The
`Vanilla theme <https://vanilla-bootstrap-hugo-theme.netlify.com/>`_ is a nice
place to start, but I don't understand the choices made for structure and styling. Additionally, it uses `Bootstrap <https://getbootstrap.com/>`_. Do I
need all of Bootstrap or can I build a good looking website with less CSS?

I've also played with SCSS. I'd like to use that as much asa possible. Thanks to
Hugo-extended for making SASS/SCSS possible.

Terms:

* an opening tag is an element name wrapped in a pair of angle brackets.
* a closing tag is the same as an opening tag, except that it includes a
  forward slash before the element name.
* the content of an element is the text between an opening and closing tag. The
  content may contain other elements.
* the element consists of the opening and closing tags, plus the content
  between them.

Nesting Elements
================

Elements can be nested.

.. code-block:: html

    <p>My cat is <strong>very</strong> grumpy.</p>

.. raw:: html

    <p>My cat is <strong>very</strong> grumpy.</p>

Block versus Inline Elements
============================

There are two important categories of elements in HTML. They are bock-level elements and
inline elements.

Block-level elements form a visible clock on a page -- they will appear on a new line
form whatever content went before it, and any content that goes after it will also appear
on a new line. Block-level elements tend to be strucural elements on the page that
represent, for example, paragraphs, lists, navigation menus, footers, etc. A block-level
element wouldn't be nested inside an inline element, but it might be nested inside
another block-level element.

Inline elements are those that are contained within block-level elements and surround
only small parts of the documment's content, not entire paragraphs and groupings of
content. An inline element will not cause a new line to appear in the document, they
would normally appear inside a paragraph of text, for example an ``<a>`` element
(hyperlink) or emphasis elements such as ``<em>`` or ``<strong>``.

.. note::

    HTML5 redefined the element categories. See `Element content categories <https://
    html.spec.whatwg.org/multipage/indices.html#element-content-categories>`_. These
    definitions are more accurate and less ambiguous than the ones that went before, but
    they are a lot more complicated to understand than "block" and "inline".

.. note::

    You can find useful reference pages that include lists of block and inline elements |--| see `Block-level elements <https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements>`_ and `Inline elements <https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements>`_.

Empty Elements
==============

Not all elements follow the above pattern of opening tag, content, closing tag. Some
elements consist only of a single tag, which is usually used to insert/embed something in
the document at the place it is included. For example, the <img> element embeds an image
file onto a page in the position it is included in:

.. code-block:: html

    <img src="https://raw.githubusercontent.com/mdn/beginner-html-site/gh-pages/images/
    firefox-icon.png">

.. raw:: html

    <img src="https://raw.githubusercontent.com/mdn/beginner-html-site/gh-pages/images/
    firefox-icon.png">

Attributes
==========

Elements can have attributes. The paragraph element below has a ``class`` attribute:

.. code-block:: html

    <p class="editor-note">My cat is very grumpy</p>

Attributes contain extra information about the element which you don't want to appear in
the actual content. In this case, the ``class`` attribute allows you to give the element
an identifying name that can be later used to target the element with style information
and other things.

An attribute should have:

#. A space between it and the element name (or the previous attribute, if the element has
   more than one attribute).
#. The attribute name, followed by an equal sign.
#. An attribute value, with opening and closing quote marks wrapped around it.

For example:

.. code-block:: html

    <p>A link to my <a href="http://douglascuthbertson.com" title="Dream, Sketch, Code"
    target="_blank">favorite website</a>.</p>

forms a link:

.. raw:: html

    <p>A link to my <a href="http://douglascuthbertson.com" title="Dream, Sketch, Code"
    target="_blank">favorite website</a>.</p>

List Elements
=============

There are three different kinds of lists. THere are unordered, ordered, and description lists. Here's an unordered list.

.. code-block:: html

    <ul>
      <li>milk</li>
      <li>eggs</li>
      <li>bread</li>
      <li>hummus</li>
    </ul>

.. raw:: html

    <ul>
      <li>milk</li>
      <li>eggs</li>
      <li>bread</li>
      <li>hummus</li>
    </ul>

Here's an ordered list.

.. code-block:: html

    <ol>
      <li>Drive to the end of the road</li>
      <li>Turn right</li>
      <li>Go straight across the first two roundabouts</li>
      <li>Turn left at the third roundabout</li>
      <li>The school is on your right, 300 meters up the road</li>
    </ol>

.. raw:: html

    <ol>
      <li>Drive to the end of the road</li>
      <li>Turn right</li>
      <li>Go straight across the first two roundabouts</li>
      <li>Turn left at the third roundabout</li>
      <li>The school is on your right, 300 meters up the road</li>
    </ol>

Here's a description list.

.. code-block:: html

    <dl>
      <dt>solilquy</dt>
      <dd>
        In drama, where a character speaks to themselves, representing their inner
        thoughts or feelings and in the process relaying them to the audience (but not to
        other characters.)
      </dd>
      <dt>monologue</dt>
      <dd>
        In drama, where a character speaks their thoughts out loud to share them with the
        audience and any other characters present.
      </dd>
      <dt>aside</dt>
      <dd>
        In drama, where a character shares a comment only with the audience for humorous
        or dramatic effect. This is usually a feeling, thought, or piece of additional
        background information.
      </dd>
      <dd>
        In writing, a section of content that is related to the current topic, but
        doesn't fit directly into the main flow of content so is presented nearby (often
        in a box off to the side.)
      </dd>
    </dl>

.. raw:: html

    <dl>
      <dt>solilquy</dt>
      <dd>
        In drama, where a character speaks to themselves, representing their inner
        thoughts or feelings and in the process relaying them to the audience (but not to
        other characters.)
      </dd>
      <dt>monologue</dt>
      <dd>
        In drama, where a character speaks their thoughts out loud to share them with the
        audience and any other characters present.
      </dd>
      <dt>aside</dt>
      <dd>
        In drama, where a character shares a comment only with the audience for humorous
        or dramatic effect. This is usually a feeling, thought, or piece of additional
        background information.
      </dd>
      <dd>
        In writing, a section of content that is related to the current topic, but
        doesn't fit directly into the main flow of content so is presented nearby (often
        in a box off to the side.)
      </dd>
    </dl>

Note that it is permitted to have a single term with multiple descriptions, as in "aside",
above.

Emphasis and Importance
=======================

Use the ``<em>`` element for emphasis. It is recognized by screen readers and spoken in a
different tone. Note that ``<em>`` is often styled in italic, by default.  Don't use this
tag purely for italic styling. Instead use a ``<span>`` element and some CSS.

Use the ``<strong>`` element to indicate importance. To emphasize important words, we
tend to stress them in spoken language and bold them in written language. The
``<strong>`` element is also recognized by screen readers, and spoken in a different
tone. It is often styled in **bold**, but shouldn't be used purely for bold styling.
Instead use a ``<span>`` element and some CSS.

The ``<blockquote>`` Element
============================

If a section of block level content (a paragraph, multiple paragraphs, a list, etc.) is
quoted from somewhere, wrap it inside a ``<blockquote>`` element to signify this, and
include a URL pointing to the source of the quote insdie a ``<cite>`` attribute. For
example, the following markup is taken from the MDN ``<blockquote>`` element page:

.. code-block:: html

  <p>The <strong>HTML <code>&lt;blockquote&gt;</code> Element</strong> (or <em>HTML Block
  Quotation Element</em>) indicates that the enclosed text is an extended quotation.</p>

To turn this into a block quote, do this:

.. code-block:: html

  <blockquote cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote">
    <p>The <strong>HTML <code>&lt;blockquote&gt;</code> Element</strong> (or <em>HTML
    Block Quotation Element</em>) indicates that the enclosed text is an extended
    quotation.</p>
  </blockquote>

Allegedly, browser default styling will render this as an indented paragraph to indicate
it is a quote.

.. raw:: html

  <blockquote cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote">
    <p>The <strong>HTML <code>&lt;blockquote&gt;</code> Element</strong> (or <em>HTML
    Block Quotation Element</em>) indicates that the enclosed text is an extended
    quotation.</p>
  </blockquote>

Inline Quotations
=================

Inline quotations work in the same way, except they use the ``<q>`` element. For example:

.. code-block:: html

  <p>The quote element — <code>&lt;q&gt;</code> — is <q cite="https://
  developer.mozilla.org/en-US/docs/Web/HTML/Element/q">intended
  for short quotations that don't require paragraph breaks.</q></p>

Browser default styling is minimal. The inline quote is, however, rendered in quotes to
indicate a quotation.

.. raw:: html

  <p>The quote element — <code>&lt;q&gt;</code> — is <q cite="https://
  developer.mozilla.org/en-US/docs/Web/HTML/Element/q">intended
  for short quotations that don't require paragraph breaks.</q></p>

Citations
=========

The content of the ``cite`` attribute sounds useful, but unfortunately browsers,
screenreaders, etc. don't really do much with it. There is no way to get the browser to
display the contents of ``cite``, without writing your own solution using JavaScript or
CSS. If you want to make the source of the quotation available on the page you need to
make it available in the text via a link or some other appropriate way.

There is a ``<cite>`` element, but this is meant to contain the title of the resource
being quoted, e.g. the name of the book. There is no reason however why you couldn't link
the text inside <cite> to the quote source in some way:

.. code-block:: html

    <p>
      According to the
      <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote">
        <cite>MDN blockquote page</cite>
      </a>:
    </p>

    <blockquote cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote">
      <p>The <strong>HTML <code>&lt;blockquote&gt;</code> Element</strong> (or <em>HTML
      Block Quotation Element</em>) indicates that the enclosed text is an extended
      quotation.</p>
    </blockquote>

    <p>
      The quote element — <code>&lt;q&gt;</code> — is
      <q cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q">intended for
      short quotations that don't require paragraph breaks.</q> --
      <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q">
        <cite>MDN q page</cite>
      </a>.
    </p>

Citations are styled in italic font by default. Here's what the example above looks like:

.. raw:: html

    <p>
      According to the
      <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote">
        <cite>MDN blockquote page</cite>
      </a>:
    </p>

    <blockquote cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote">
      <p>The <strong>HTML <code>&lt;blockquote&gt;</code> Element</strong> (or <em>HTML
      Block Quotation Element</em>) indicates that the enclosed text is an extended
      quotation.</p>
    </blockquote>

    <p>
      The quote element — <code>&lt;q&gt;</code> — is
      <q cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q">intended for
      short quotations that don't require paragraph breaks.</q> --
      <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q">
        <cite>MDN q page</cite>
      </a>.
    </p>


.. _mdn intro css: https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS
.. _mdn intro html: https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML
.. _mdn: https://developer.mozilla.org/en-US/
.. _hugo: https://gohugo.io/
.. _bootstrap layout overview: https://getbootstrap.com/docs/4.3/layout/overview/

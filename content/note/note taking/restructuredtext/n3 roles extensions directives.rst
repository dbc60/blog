########################################
Sphinx Roles, Extensions, and Directives
########################################

*****
Roles
*****

It seems that formatting, and syntax highlighting can be had inline by defining and using `roles <sphinx roles_>`_. Interpreted text uses backquotes (`````) around the text. An explicit role marker may optionally appear before or after the text, delimited with colons. For example:

    This is `interpreted text` using the default role.

    This is :title:`interpreted text` using an explicit role.

There is a built-in :code:`code` role, so one can format text with it by writing ``:code:`int x = 0;```.

To get `syntax highlighting <pygment lexers_>`_ you can define a custom role. For example::

    .. role:: cpp(code)
        :language: c++

.. NOTE: I've moved the definition of this role to a file read-in by the
.. rst_prolog directive in conf.py

which you can then use like so:

Write "``:cpp:`class Foo {public: Foo();}; Foo::Foo() {}```" to get: :cpp:`class Foo {public: Foo();}; Foo::Foo() {}`. Let's try ``:cpp:`class Bar;```: :cpp:`class Bar;`.

Oh well. It seems that syntax highlighting fails for inline code with Sphinx 1.6.3. Maybe it will work with a later version. Here's how I expected it to be highlighted:

.. code-block:: cpp

    class Bar;

    class Foo
    {
        public: Foo();
    };

    Foo::Foo() {}

* `Define custom roles <defining custom roles in sphinx_>`_

*************
Index Entries
*************

The documentation for `generating index entries`_ recommends placing the directives *before* the thing to which they refer. For example, to index a heading, place the index directive just above the heading.

.. _generating index entries: http://www.sphinx-doc.org/en/stable/markup/misc.html#index-generating-markup

*********
Footnotes
*********

Footnote references, like ``[5]_``, are resolved later with text like::

    .. [5] A numerical footnote. Note
       there's no colon after the ``]``.

`Footnotes`_ can also have automatically assigned numbers, or symbols.

********************
Roles and Directives
********************

Sphinx is built on docutils, a set of tools for parsing and working with reStructuredText markup. The rst parser in docutils is designed to be extended in two main ways:

#. *Directives* let you work with large blocks of text and intercept the parsing steps as well as the formatting steps.
#. *Roles* are intended for inline markup, within a paragraph.

See `Defining Custom Roles in Sphinx`_.

Admonition Directives
=====================

The Following admonition directives have been implemented:

* attention
* caution
* danger
* error
* hint
* important
* note
* tip
* warning

.. attention:: The matter is closed!

.. caution:: There be giants here!

.. DANGER::
    Beware Killer Rabbits!

.. Error:: Your thoughts do not compute.

.. hint:: The inspector is not whom he seems to be.

.. important:: Play nice, or you will be punished.

.. note:: This is a note admonition.
   This is the second line of the first paragraph.

   - The note contains all indented body elements
     following.
   - It includes this bullet list.

.. tip:: Cow tipping can be harmful if you're on the wrong side of the cow.

.. warning:: You may be on the wrong side of the cow!

.. admonition:: And, by the way...

   You can make up your own admonition too.

Other Directives
================

.. versionadded:: 1.0
  this was added.

.. versionchanged:: 1.1
  this was changed.

.. deprecated:: 1.2
  use this other thing instead.

The `seealso directive`_ is typically placed in a section just before any subsections. For the HTML output, it is shown boxed off from the main flow of the text.

The content of the `seealso directive`_ should be a reST definition list.

.. seealso::

   Term X
      Definition of X.

   `Pygment Lexers`_
      Documentation for lexers supported by pygment.

.. topic:: Topic Title

  Indented lines following the
  topic directive form the body
  of the topic, and are interpreted
  as body elements - whatever that means.

.. sidebar:: Sidebar Title

  Indented lines following the
  sidebar directive form the body
  of the sidebar, and are interpreted
  as body elements - whatever that means.

The rubric directive creates a paragraph heading that is not used to create a table of contents node.

.. rubric:: Line Blocks

Line blocks are useful for address blocks, verse (poetry, song lyrics), and unadorned lists, where the structure of lines is significant. Line blocks are groups of lines beginning with vertical bar ("|") prefixes. Each vertical bar prefix indicates a new line, so line breaks are preserved. Initial indents are also significant, resulting in a nested structure. Inline markup is supported. Continuation lines are wrapped portions of long lines; they begin with a space in place of the vertical bar. The left edge of a continuation line must be indented, but need not be aligned with the left edge of the text above it. A line block ends with a blank line.

This example illustrates continuation lines:

  | Lend us a couple of bob till Thursday.
  | I'm absolutely skint.
  | But I'm expecting a postal order and I can pay you back
    as soon as it comes.
  | Love, Ewan.

This example illustrates the nesting of line blocks, indicated by the initial indentation of new lines:

Take it away, Eric the Orchestra Leader!

    | A one, two, a one two three four
    |
    | Half a bee, philosophically,
    |     must, *ipso facto*, half not be.
    | But half the bee has got to be,
    |     *vis a vis* its entity.  D'you see?
    |
    | But can a bee be said to be
    |     or not to be an entire bee,
    |         when half the bee is not a bee,
    |             due to some ancient injury?
    |
    | Singing...

.. centered:: Create a Centered Boldfaced line of text.

Here is a horizontal list in three columns:

.. hlist::
   :columns: 3

   * A list of
   * short items
   * that should be
   * displayed
   * horizontally

A code block:

.. code-block:: c

  #include <stdlib.h>

  int
  main(int argc, char **argv) {
      // This is a single-line comment
      /*
       * Here we have a block comment
       */
      printf("Hello, world!\n");
  }

  enum foo {GARDENS, PICNICS};

Apparently, Sphinx v1.8.0+ will have more options for highlighting and code
blocks. These examples don't work in v1.7.2, but are `documented in master
<http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.
html#showing-code-examples>`_::

  A code block with line numbers:

  .. code-block:: c
     :linenos:

    #include <stdlib.h>

    int
    main(int argc, char **argv) {
        // This is a single-line comment
        /*
         * Here we have a block comment
         */
        printf("Hello, world!\n");
    }

    enum foo {GARDENS, PICNICS};

  A short code block with a line number threshold of 5:

  .. code-block:: c
     :linenosthreshold: 5

    int main(int argc, char **argv) {
        printf("Hello, world!\n");
    }

  A longer code block with a line number threshold of 5:

  .. code-block:: c
     :linenosthreshold: 5

    #include <stdlib.h>

    int
    main(int argc, char **argv) {
        // This is a single-line comment
        /*
         * Here we have a block comment
         */
        printf("Hello, world!\n");
    }

    enum foo {GARDENS, PICNICS};

.. _pygment lexers: http://pygments.org/docs/lexers/
.. _sphinx roles: http://docutils.sourceforge.net/docs/ref/rst/roles.html
.. _defining custom roles in sphinx: https://doughellmann.com/blog/2010/05/09/defining-custom-roles-in-sphinx/
.. _seealso directive: http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-seealso

**************
Sphinx Domains
**************

This is an example of a Python domain for documenting Python code via Sphinx.
In this case, it's an example of how one might document Python's built-in
function :code:`enumerate()`. You would add this to one of your source files::

  .. py:function:: enumerate(sequence[, start=0])

     Return an iterator that yields tuples of an index and an item of the
     *sequence*. (And so on.)

This is what Sphinx will render:

.. py:function:: enumerate(sequence[, start=0])

   Return an iterator that yields tuples of an index and an item of the
   *sequence*. (And so on.)

See `Sphinx Domains <http://www.sphinx-doc.org/en/1.7/domains.html#domains>`_ for all the available domains and their directives and roles.

Some of the available domains are:

* Python ``py``
* C ``c``
* C++ ``cpp``
* The Standard Domain. It collects all markup that doesn't warrant a domain of its own. Its directives and roles are not prefixed with a domain name.
* JavaScript ``js``

The `sphinx-contrib <https://bitbucket.org/birkenfeld/sphinx-contrib/>`_ repository contains more domains available as extensions. As of this writing, the Python Package Index (`PyPI`_) lists 394 projects that match a search for `sphinxcontrib, sphinx, and extension <https://pypi.org/search/?q=sphinxcontrib+sphinx+extension&c=Topic+%3A%3A+Documentation>`_.

.. _pypi: https://pypi.org

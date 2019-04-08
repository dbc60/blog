.. _link_notes:

#####
Links
#####

**************
Indirect Links
**************

Per the `documentation on internal and external links`_, and `indirect hyperlink targets`_ I can define the link elsewhere and reuse it.

- `Corporate Titles`_
- `Corporate titles on Wikipedia <corporate titles_>`_ uses the same indirect link, but displays its own words rather than those of the reference used in the indirect link.
- `Internal and External Links`_
- `Indirect Hyperlink Targets`_

Indirect links work only for hyperlinks, not for links to local files.

.. references are case-insensitive (BTW, this is a comment)

.. _corporate titles: https://en.wikipedia.org/wiki/Corporate_title
.. _Internal and External Links: https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#internal-and-external-links
.. _documentation on internal and external links: `internal and external links`_
.. _indirect hyperlink targets: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#indirect-hyperlink-targets


.. _explicit_links_rst:

**************
Explicit Links
**************

Explicit links can work internally, within the same document, or externally, between separate documents in the same collection. The syntax is a little different for each one.

Internal Links
==============

All titles are considered candidates for linking. A link to a title is just its name within quotes and a final underscore::

  `Explicit Links`_

If the title is a single word, such as "Links", then the backticks aren't
necessary. We can write::

  Links_

So Links_ links to the heading at the beginning of this file.

.. _link_labels:

Besides using titles, one may create an explicit link target by creating a label. A label looks like::

  .. _link_label:

If the label is in the same file, then there are three methods that can be used to link to it. The first works best if the label is placed above a title::

  .. _my_link:

  ********
  My Title
  ********

To create a hyperlink, write some text between a pair of backticks and put the label between angle-brackets (without the leading underscore, but add a trailing underscore) **and** follow the final backtick with an underscore. In other words, if the label is ``.. _link_notes:``, then the linking text could be::

  `My Link Notes <link_notes_>`_

I've created that label at the top of this file. `Here's the link <link_notes_>`_.

The ``:ref:`` role can also be used to create links to labels. If the label is above a title, the more simple form can be used, and the text of the link will be the title. For example, here's how to link to the heading at the top of this file using the ``link_notes`` label::

  :ref:`link_notes`

If the label doesn't have an associated title, then an explicit caption must be added. For example::

  :ref:`A Caption <link_labels>`

will create a link called "A Caption": :ref:`A Caption <link_labels>`.

Note that by using the ``:ref:`` role, trailing underscores are not needed.

External Links
==============

The only options for external links (those outside of the *current* file) are two use one of the two variants of the ``:ref:`` role::

  :ref:`explicit_links_rst`

  :ref:`Docs on Explicit Links <explicit_links_rst>`

Where the label in the first case must be associated with a title. In the second case, the caption, "Docs on Explicit Links", will be used for when the label is *not* associated with a title, or it will replace the title for labels that *are* associated with one.

* :ref:`explicit_links_rst`
* :ref:`Docs on Explicit Links <explicit_links_rst>`

Other Link Notes
================

If the link text is a single word, such as kalamazoo_, it can work without the surrounding back-ticks. For example, ``kalamazoo_`` can be made to link to https://www.python.org::

  If the link text is a single word, such as kalamazoo_

  .. _kalamazoo: https://www.python.org

The ``:ref:`` role requires a label. I put the label ``.. _javascript:`` at the top of the index page for my JavaScript notes. Now I can create a link to it using the ``:ref:`` role::

  :ref:`javascript`

Here is the index to my :ref:`javascript` notes.

.. _kalamazoo: https://www.python.org

###################
Titles and Headings
###################

RestructuredText is more flexible. It allows for a variety of underline and overline characters. The `quicstart guide <http://docutils.sourceforge.net/docs/user/rst/quickstart.html>`_ is a little confusing. The section about sections gives as examples, the following *adornments* for creating title, secion and subsection headings:

#. ``=`` chapter title
#. ``-`` section title
#. ``~`` subsection title

However, the next section about document titles and subtitles gives the following examples:

#. ``=`` with overline for a document title.
#. ``-`` with overline for a document subtitle.
#. ``=`` for a section title.

The subtitle and section title examples here conflict with the section title above. In reality, any of the non-alphanumeric characters ``=`` ``-`` ````` ``:`` ``'`` ``"`` ``~`` ``^`` ``_`` ``*`` ``+`` ``#`` ``<`` ``>`` can be used. An underline-only adornment is distinct from an overline-and-underline adornment using the same character. There are only two rules:

#. The underline/overline must be at least as long as the title text.
#. Be consistent. All sections marked with the same adornment style are deemed to be at the same level.

The Python and Sphinx conventions for representing the six HTML headings are in the `style guide <http://documentation-style-guide-sphinx.readthedocs.io/en/latest/style-guide.html>`_. They are:


#. ``#`` with overline
#. ``*`` with overline
#. ``=``
#. ``-``
#. ``^``
#. ``"``

We can write::

  ##########
  H1 Heading
  ##########

  Some plain filler text.

  **********
  H2 Heading
  **********

  Some plain filler text.

  H3 Heading
  ==========

  Some plain filler text.

  H4 Heading
  ----------

  Some plain filler text.

  H5 Heading
  ^^^^^^^^^^

  Some plain filler text.

  H6 Heading
  """"""""""

  Some plain filler text.

The result will be:

##########
H1 Heading
##########

Some plain filler text.

**********
H2 Heading
**********

Some plain filler text.

H3 Heading
==========

Some plain filler text.

H4 Heading
----------

Some plain filler text.

H5 Heading
^^^^^^^^^^

Some plain filler text.

H6 Heading
""""""""""

Some plain filler text.

.. miscellaneous rst notation:

######################
Miscellaneous Notation
######################

*****
Lists
*****

Bullet Lists
============

Bullet lists start with one of "-", "+", or "*"::

  - this is item one
  - this is item two

  - this is a long item on the list.
    Continuing text must be aligned
    after the bullet and whitespace.

  Note that a blank line is required
  before the first item and after the last,
  but is optional between items.

- this is item one
- this is item two

- this is a long item on the list.
  Continuing text must be aligned
  after the bullet and whitespace.

Note that a blank line is required
before the first item and after the last,
but is optional between items.

Enumerated Lists
================

Enumerated lists::

  3. This is the first item.
  4. This is the second item.
  5. Enumerators are Arabic numbers,
     single letters, or Roman numeral.
  6. List items should be sequentially
     numbered, but need not start at 1
     (although no all formatters will
     honor the first index).
  #. This item is auto-enumerated.

The result is:

3. This is the first item.
4. This is the second item.
5. Enumerators are Arabic numbers,
    single letters, or Roman numeral.
6. List items should be sequentially
    numbered, but need not start at 1
    (although no all formatters will
    honor the first index).
#. This item is auto-enumerated.

Definition Lists
================

Definition Lists::

  what
    Definition lists associate a term with
    a definition.

  how
    The term is a one-line phrase, and the
    definition is one or more paragraphs or
    body elements, indented relative to the
    term. Blank lines are not allowed
    between term and definition.

The result is:

what
  Definition lists associate a term with
  a definition.

how
  The term is a one-line phrase, and the
  definition is one or more paragraphs or
  body elements, indented relative to the
  term. Blank lines are not allowed
  between term and definition.

Field Lists
===========

Field lists are used as part of an extension syntax, such as options for `directives <http://docutils.sourceforge.net/docs/user/rst/quickref.html#directives>`_, or database-like records meant for further processing. Field lists may also be used as generic two-column table constructs in documents. For example::

  :Authors:
    Tony J. (Tibs) Ibbs,
    David Goodger

    (and sundry other good-natured folks)

  :Version: 1.0 of 2001/08/08
  :Dedication: To my father

results in:

:Authors:
  Tony J. (Tibs) Ibbs,
  David Goodger

  (and sundry other good-natured folks)

:Version: 1.0 of 2001/08/08
:Dedication: To my father

Option Lists
============

There must be at least two spaces between the option and the description. For example::

  -a            command-line option "a"
  -b file       options can have arguments
                and long descriptions
  --long        options can be long also
  --input=file  long options can also have
                arguments
  /V            DOS/VMS-style options too

looks like:

-a            command-line option "a"
-b file       options can have arguments
              and long descriptions
--long        options can be long also
--input=file  long options can also have
              arguments
/V            DOS/VMS-style options too

**************
Blocks of Text
**************

Line Blocks
===========

Line blocks are a way of preserving line breaks::

    | These **lines** are
    | broken *exactly* like in
    | the source file, but we
    | get to use *emphasis*, **bold**,
    | and other markup like :math:`\LaTeX`.

The block above produces:

| These **lines** are
| broken *exactly* like in
| the source file, but we
| get to use *emphasis*, **bold**,
| and other markup like :math:`\LaTeX`.

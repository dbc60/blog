######
Tables
######

There are two basic styles of tables: `grid tables`_ and `simple tables`_. Grid tables are cumbersome to create. Simple tables are easy to create but have some limitations.

Sphinx extends table definitions with an explicit markup block: `the table directive`_, which can create a table with a title. This directive supports two more syntaxes: `CSV tables`_ and `List tables`_.

***********
Grid Tables
***********

Grid tables provide a complete table representation via grid-like "ASCII art". Grid tables allow arbitrary cell contents (body elements), and both row and column spans. However, grid tables are cumbersome to produce, especially for simple data sets.

Grid tables are described with a visual grid made up of the characters "-", "=", "|", and "+". The hyphen ("-") is used for horizontal lines (row separators). The equals sign ("=") may be used to separate optional header rows from the table body.

The vertical bar ("|") is used for vertical lines (column separators). The plus sign ("+") is used for intersections of horizontal and vertical lines. Example::

    +------------------------+------------+----------+----------+
    | Header row, column 1   | Header 2   | Header 3 | Header 4 |
    | (header rows optional) |            |          |          |
    +========================+============+==========+==========+
    | body row 1, column 1   | column 2   | column 3 | column 4 |
    +------------------------+------------+----------+----------+
    | body row 2             | Cells may span columns.          |
    +------------------------+------------+---------------------+
    | body row 3             | Cells may  | - Table cells       |
    +------------------------+ span rows. | - contain           |
    | body row 4             |            | - body elements.    |
    +------------------------+------------+---------------------+

The "ascii art" above produces this table:

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span columns.          |
+------------------------+------------+---------------------+
| body row 3             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 4             |            | - body elements.    |
+------------------------+------------+---------------------+

Cells can have body elements, like the line-block syntax used here::

    +----------------+-----------------+
    | Programming    | Math            |
    +================+=================+
    | array          | function        |
    +----------------+-----------------+
    | | index set of | | domain of     |
    | | an array     | | a function    |
    +----------------+-----------------+
    | | f[e] array   | | f(e) function |
    | | application  | | application   |
    +----------------+-----------------+

to produce this table:

+----------------+-----------------+
| Programming    | Math            |
+================+=================+
| array          | function        |
+----------------+-----------------+
| | index set of | | domain of     |
| | an array     | | a function    |
+----------------+-----------------+
| | f[e] array   | | f(e) function |
| | application  | | application   |
+----------------+-----------------+

There are some pitfalls with grid tables. The examples in `the docs <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#tables>`_ show what can happen with a cell that spans several columns and the text has a vertical bar that accidentally aligns with column boundaries.

*************
Simple Tables
*************

Simple tables provide a compact and easy to type but limited row-oriented table representation for simple data sets. Cell contents are typically single paragraphs, although arbitrary body elements may be represented in most cells. Simple tables allow multi-line rows (in all but the first column) and column spans, but not row spans.

Simple tables are described with horizontal borders made up of "=" and "-" characters. The equals sign ("=") is used for top and bottom table borders, and to separate optional header rows from the table body. The hyphen ("-") is used to indicate column spans in a single row by underlining the joined columns, and may optionally be used to explicitly and/or visually separate rows.

A simple table begins with a top border of equals signs with one or more spaces at each column boundary (two or more spaces recommended). Regardless of spans, the top border must fully describe all table columns. There must be at least two columns in the table (to differentiate it from section headers). The top border may be followed by header rows, and the last of the optional header rows is underlined with '=', again with spaces at column boundaries. There may not be a blank line below the header row separator; it would be interpreted as the bottom border of the table. The bottom boundary of the table consists of '=' underlines, also with spaces at column boundaries. For example, here is a truth table, a three-column table with one header row and four body rows::

    =====  =====  =======
      A      B    A and B
    =====  =====  =======
    False  False  False
    True   False  False
    False  True   False
    True   True   True
    =====  =====  =======

The table above looks like this:

=====  =====  =======
  A      B    A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

*******************
The Table Directive
*******************

The "table" directive is used to associate a title with a table or specify options, e.g.::

    .. table:: Truth table for "not"
       :widths: auto

       =====  =====
         A    not A
       =====  =====
       False  True
       True   False
       =====  =====

which produces this:

.. table:: Truth table for "not"
   :widths: auto

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====

The following options are recognized:

align : "left", "center", or "right"
    The horizontal alignment of the table. (New in Docutils 0.13)

widths : "auto", "grid" or a list of integers
    A comma- or space-separated list of column widths. The default is the width of the input columns (in characters).

The special values "auto" or "grid" may be used by writers to decide whether to delegate the determination of column widths to the backend (LaTeX, the HTML browser, ...). See also the `table_style <http://docutils.sourceforge.net/docs/user/config.html#table-style-html4css1-writer>`_ configuration option.

and the common options :code:`:class:` and :code:`:name:`.

**********
CSV Tables
**********

The "csv-table" directive is used to create a table from CSV (comma-separated values) data. CSV is a common data format generated by spreadsheet applications and commercial databases. The data may be internal (an integral part of the document) or external (a separate file).

Example::

    .. csv-table:: Frozen Delights!
       :header: "Treat", "Quantity", "Description"
       :widths: 15, 10, 30

       "Albatross", 2.99, "On a stick!"
       "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
       crunchy, now would it?"
       "Gannet Ripple", 1.99, "On a stick!"

makes this:

.. csv-table:: Frozen Delights!
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"

***********
List Tables
***********

The "list-table" directive is used to create a table from data in a uniform two-level bullet list. "Uniform" means that each sublist (second-level list) must contain the same number of list items.

Example::

    .. list-table:: Frozen Delights!
       :widths: 15 10 30
       :header-rows: 1

       * - Treat
         - Quantity
         - Description
       * - Albatross
         - 2.99
         - On a stick!
       * - Crunchy Frog
         - 1.49
         - If we took the bones out, it wouldn't be
           crunchy, now would it?
       * - Gannet Ripple
         - 1.99
         - On a stick!

makes this:

.. list-table:: Frozen Delights!
   :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!

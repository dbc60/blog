---
title: "Create Table Heading"
date: 2021-09-23T17:59:37-04:00
years: ["2021"]
---
<!--more-->

```go-html-template
{{/*
  shortcodes/create=table.html

  Read a table in YAML, TOML, or JSON format from .Site.Data or a
  subdirectory of that directory and turn it into HTML.

  A table is structured as an array of rows of columns. In other words, the
  table is an array. Each element of the array is a row that will be wrapped in
  <tr></tr> tags. Each row is an array of cells, where each cell will be either
  a header (<th></th>) or data (<td></td>).

  In addition, if there is a simple key/value pair where the key is "caption"
  and the value is a scalar type, then the value of the scalar (a string is
  probably best) will become the content of the table's <caption> element.

  If the table data contains a "colgroup" array, then rows will be interpreted
  as content for <col> tags. In TOML, it might look like:

    [[colgroup]]
    span = 2
    class = "colgroup-1"
    [[colgroup]]
    span = 2
    class = "colgroup-1"

  If the data contains a "head" array, then each row will be placed in a
  <thead></thead> section and the row elements will be <th></th> header
  elements. Similarly, a "body" array will create a <tbody></tbody> section and
  result in element of a row array being wrapped in <td></td> tags. Finally, a
  "foot" array creates a <tfoot></tfoot> section.

  Note that any array that is not named "head", "body", or "foot" will generate
  rows with data cells (<td></td>) and there will be no <tbody></tbody> tags to
  wrap the section.

  Example call:

  {{</* create-table src="table-example" */>}}

  The overall structure of the code is inspirec by Johann Oberdorfer's article
  "Recursive Directory Listing for Hugo": http://www.johann-oberdorfer.eu/blog/2020/07/03/20-07-03_recursive_function_in_hugo/

  The HTML <table></table> element represents tabular data. The following elements are permitted in this order:

  - an optional <caption></caption> element
  - zero or more <colgroup></colgroup> elements
  - an optional <thead></thead> element
  - either one of the following:
    - zero or more <tbody></tbody> elements
    - one or more <tr></tr> element
  - an optional <tfoot></tfoot> element

  The <caption> element should be the first child of its parent <table> element. When the <table> element that contains the <caption> element is the _only descendant of a <figure> element, you should use the <figcaption> element instead of <caption>. Note that CSS like "table {background: red;}" does NOT alter the caption. For that you need "display: block".

  The <colgroup> element defines a group of columns within a table. If the "span" attribute is present, it is an empty element. If the attribute is not present, then it contains zero or more <col> elements.

    - The <colgroup> element must appear after any optional <caption> element, but before any <thead>, <th>, <tbody>, <tfoot>, and <tr> element.
    - The start tag may be omitted if it has a <col> element as its first child and if it is not preceded by a <colgroup> whose end tag has been omitted.
    - The end tag may be omitted if it is not followed by a space or a comment.

    The <col> element defines a column within a table and is used for definint common semantics on all common cells. It is generally found within a <colgroup> element.
      - it must have a start tag, and it must not have an end tag.
      - The "span" attribute contains a positive integer indicating the number of consecutive columns the <col> element spans. If not present, its default value is 1.

  The <thead> element defines a set of rows defining the head of the columns of the table.
    - Permitted content is zero or more <tr> elements.
    - The <thead> element must appear after any <caption> or <colgroup> element, even if implicitly defined, but before and <tbody>, <tfoot>, and <tr> element.

  The <tbody> element encapsulates a set of table rows (<tr> elements), indicating that they comprise the body of the table. The <tbody> element, along with its cousins <head> and <tfoot>, provide useful semantic information that can be used when rendering for either screen or printer as well as for accessibility purposes.
    - Within the required parent <table> element, the <tbody> element can be added after a <caption>, <colgroup>, and a <thead> element.
    - Permitted content is zero or more <tr> elements.
    - It must NOT be present if its parent <table> elementhas a <tr> element as a child.

  The <tr> element defines a row of cells in a table. The row's cells can then be established using a mix of <td> (data cell) and <th> (header cell) elements. To provide additional control ove how cels fit into (or span across) columns, both <th> and <td> support the "colspan" attribute, which lets you specify how many columns wide the cell should be, with the default being 1. Similarly, you can use the "rowspan" attribute on cells to indicate they should span more than one table row. For an in-depth tutorial, see the HTML table series (https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables).

    The <th> element defines a cell as header or a group of table cells. The exact nature of this group is defined by the scope of the "headers" attributes.
      - permitted parents: a <tr> element.
      - the start tag is mandatory
      - the end tag may be omitted if it is immediately followed by a <th> or <td> element, or if there are no more data in its parent element.

    The <td> element defines a cell of a table that contains data.
      - permitted parents: a <tr> element.
      - the start tag is mandatory.
      - the end tag may be omitted if it is immediately followed by a <th> or <td> element, or if there are no more data in its parent element.

  The <tfoot> element defines a set of rows summarizing the columns of the table. It may contain zero or more <tr> elements.
    - it must appear after any <caption>, <colgroup>, <thead>, <tbody>, or <tr> element.
    - the start tag is mandatory.
    - the end tag may be omitted if there is no more content in the parent <table> element.

  I might want to consider reserving keys that begin with "attr-" for defining attributes within any element of a table. That way, I can write:

    [[row]]
      data = ["one", "tow", "three"]
      attr-class = "my-class"

  and have it transcribed to:

    <tr class="my-class">
      <td>one</td>
      <td>two</td>
      <td>three</td>
    </tr>
*/}}
```

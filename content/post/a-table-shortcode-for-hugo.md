---
title: "A Table Shortcode for Hugo"
date: 2021-09-23T10:59:36-04:00
years: ["2021"]
tags: [blog]
featuredImage: "images/banners/chinese-alligator_00001.jpg"
featuredImageDescription: "Chinese Alligator"
featuredCopyright:  "copyright © 2011 Douglas Cuthbertson"
---
I write a lot of notes in Markdown files and use Hugo to display them in a browser. It makes for easy reading and jumping among them. Several months ago, I needed to create some tables where some cells spanned mulitple rows or columns. That's not possible with Markdown tables. Creating tables in HTML with appropriate classes seemed tedious. I thought it might be less so by defining tables in [TOML](https://toml.io/en/) and use a shortcode to translate them into HTML.
<!--more-->
{{< table_of_contents >}}

I might be wrong. It turns out that it's very hard to define a table in TOML. It's even harder to define one where a cell can span two or more rows or columns. Once you have that, you still have to write a lot of CSS to get it to display properly.

What I have is a way to turn a TOML table stored in `/data/complete-example.toml` into this:

{{< create_table src="complete-example" >}}

It's not a complete solution, but it's enough given the effort to get this far.In the future, if I need fancy tables, I think I'll just embed HTML into the markdown.

The contents of `/data/complete-example.toml` is:

```toml
# Table caption
caption = "All the Features in the create_table Shortcode"

[header]
  hd1 = ["Header R1C1", "Header R1C2", "Header R1C3"]
[[head]]
  hd1 = ["Header R2C1", "Header R2C2", "Header R2C3"]
[[head]]
  hd1 = ["Header R3C1", "Header R3C2", "Header R3C3"]
  hd2 = ["Header R4C1", "Header R4C2", "Header R4C3"]
[[body]]
  row = ["a", "b", "c"]
[[body]]
  row = ["d", "e", "f"]


# Don't embed colgroup in another array. It becomes an embedded map.
# [[head.colgroup]]
#   span = 1
# [[head.colgroup]]
#   span = 2

[[foot]]
  row = ["foot1", "foot2", "foot3"]

# This map is at the top-level of the table and can be used to create an HTML
# colgroup for the table. One entry for each <col> element.
[[colgroup]]
  span = 1
[[colgroup]]
  span = 2
  class = "odd"
[[colgroup]]
  span = 1
  class = "even"
```

To use the shortcode on this file, include `{{</* create_table src="complete-example" */>}}` in a markdown file.

## The create_table Shortcode

This shortcode starts with realizing Hugo's built-in `.Site.Data` variable isn't a path to a configured `data` directory. It's a map of all files in the data folder, its subfolders, the files contained in those subfolders, and the contents of all those files. On one hand, that's rather insane. On the other, it gets all that data into memory so Hugo can operate on it more quickly than if files had to be individually loaded and parsed.

Let's capture that in a variable for use later:

{{< evergreen "/evergreen-notes/create-table/store-site-data.md" >}}

Next, get the data that's in the given file. The file is given in the `src` attribute:

{{< evergreen "/evergreen-notes/create-table/src-file-path.md" >}}

Here's the code to pull out the data just for that file:

{{< evergreen "/evergreen-notes/create-table/src-file-data.md" >}}

From here, I'll give a quick top-down view of the shortcode. It defines a table as an HTML `<table>` element with a class of the same name. The contents of the table is generated from a `buildTable` template and our data:

{{< evergreen "/evergreen-notes/create-table/table-top-level-definition.md" >}}

## buildTable Template

The `buildTable` template attempts to determine if the TOML data has a head and body. It also captures the data for a caption, any column groups, the head, body, and foot of the table. It starts with initializing some variables.

{{< evergreen "/evergreen-notes/create-table/build-table-initialization.md" >}}

The next step is to collect all the keys in the map. The keys are expected to be the components of an HTML table.

- body
- caption
- colgroup
- head
- foot

{{< evergreen "/evergreen-notes/create-table/table-collect-keys" >}}

Now we can fill in all those variables.

{{< evergreen "/evergreen-notes/create-table/table-capture-values" >}}

There are several templates used by that chunk of code. They are small, so we can go through them quickly.

## createColGroup Template

`createColGroup` creates column groups with the `<col>` element:

{{< evergreen "/evergreen-notes/create-table/template-create-colgroup" >}}

## createRowsHead and  processMapHead Templates

These two templates are mutually recursive. `createRowsHead` creates rows in the `<head>` section of the table. It processes each element of the row, creating a new `<th>` element as it goes.

{{< evergreen "/evergreen-notes/create-table/template-create-rows-head" >}}

If a new row needs to be generated, `createRowsHead` calls `processMapHead` which generates a new `<tr>` element. Likewise, `processMapHead` will call back to `createRowsHead` in the case that a column has more than one value.

{{< evergreen "/evergreen-notes/create-table/template-process-map-head" >}}

## createRows and processMap Templates

These two templates are mutually recursive. `createRows` creates the column (`<td>`) elements for each row in `<body>` or `<foot>` element. Note that `createRows` is a recursive template, so it can handle some weirdly designed tables.

{{< evergreen "/evergreen-notes/create-table/template-create-rows" >}}

`processMap` either creates columns in a row, or generates a new row and calls itself recursively. If a column has more than one value, it calls back to `createRows` to process them.

{{< evergreen "/evergreen-notes/create-table/template-process-map" >}}

## The Complete create_table Shortcode

Here's the whole thing w/o comments. It's not that useful, but it was a journey and an education to get here.

{{< evergreen "/evergreen-notes/create-table/create-table-shortcode" >}}

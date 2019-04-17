---
title: Excel Spreadsheets
date: 2016-03-26T10:32:30-05:00
draft: true
categories: software
tags: [excel, spreadsheets]
---

Notes on using Excel.
<!--more-->

## Excel Key Bindings

See [Excel Keyboard Shortcuts](http://www.asap-utilities.com/excel-tips-shortcuts.php) online for a long list. Here are some important ones:

- tab: move right one column
- enter: move down one row
- F2: Edit
- F4: while typing a formula, rotate through absolute and relative cell references:
  - row and column relative references
  - absolute reference to a cell
  - relative row, absolute column
  - absolute row, relative column
- Ctrl+A: select the current area surrounded by whitespace.
- Ctrl+D: Fill down
- Ctrl+R: Fill right
- Ctrl+Shift+F3: Create name by using names of row and column labels
- Ctrl+Shift-V: paste without formatting
- Ctrl+Enter: Fill an area with the same value. Select an area, fill in once cell with the value, and hit Ctrl-Enter to fill the rest of the area.

## Style Guidelines

- Centered headings look better
- Always have at least one blank row and column around each table. It makes it possible to select the whole table within the sheet
- Make columns with the same kind of data the same width. Select all of those columns and drag one to the width you want. All of them will be set to the same width.

## Magic

- Name cells, areas and columns as needed. These names can then be used in formulas instead of the row/column index, which makes the formulas easier to read.
- Make a table out of a related set of rows and columns and give the table a name! It will make it easier to add more rows and make it easy to keep references and formatting consistent.

Instead of using the `VLOOKUP` or `HLOOKUP` function to lookup and use a value from a table, use the two functions, `MATCH` and `INDEX`. It will be faster, and you can use the names of cells and columns to make your formulas more readable. For example, the following assumes you have a few rows of a single column labeled 'TaxJurisdiction', and another column labeled 'Location'. This formula :

```text
=match(Location, TaxJurisdiction)
```

will return the row of the `TaxJurisdiction` area that matches the value in the current row of the `Location` column.

Now we can figure out the taxes based on a columns labeled `Salary` and `Location`. We use the `Location` to lookup the index of the matching `TaxJurisdiction`. That index is then used to select the associated tax rate in the `TaxRates` column/table. Finally, the tax rate is multiplied by the salary and rouned to the nearest dollar.

```text
=ROUND(INDEX(TaxRates,MATCH(Location,TaxJurisdiction)) * Salary, 0)
```

---
title: "Tips"
date: 2019-07-21T07:44:49-04:00
draft: true
---

Various tips and tricks found on the web.
<!--more-->

These tips are things I found useful while experimenting with HTML and CSS or surprising while reading about web design.

## Links in Dummy Text

Always include links within your dummy text to spot stacking context issues. For example, the following HTML that includes links will make it easier to spot CSS errors if some elements cover up other elements.

```html
<div id="header">
    <h2><a href="#">Header</a></h2>
    <p>Lorem ipsum...</p>
</div>

<div id="sidebar">
    <h2><a href="#">Sidebar</a></h2>
    <p>Lorem ipsum...</p>
</div>

<div id="main">
    <h2><a href="#">Main</a></h2>
    <p>Lorem ipsum...</p>
</div>

<div id="footer">
    <h2><a href="#">Footer</a></h2>
    <p>Lorem ipsum...</p>
</div>
```

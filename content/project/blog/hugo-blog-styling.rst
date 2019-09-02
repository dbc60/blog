---
title: "Hugo Blog Styling"
date: 2019-06-11T07:29:40-04:00
draft: true
categories: learning
tags: [blog, html, css, web]
---

I am going to try applying the naming convention from the `Block Element Modifier <bem_>`_ methodology and the file/folder organization advice from `Enduring CSS <https://ecss.io/>`_ to organize my Sass, CSS, and HTML templates.
<!--more-->

The first question is, will Hugo and Sass support organizing components by
directory? Suppose I want a navigation menu with navigation items. The
template, ``nav.html`` is stored in the ``layouts/partials/`` folder. I also
have several ``.scss`` files in ``assets/scss/``. On top of that, the
individual items that go in the nav menu are defined in ``config/_default/config.toml`` as:

.. code-block::

    # See https://feathericons.com/
    # The value of pre is the icon name
    [menu]
      [[menu.nav]]
        name = "Home"
        pre = "home"
        url = "/"
        weight = 1
      [[menu.nav]]
        name = "Notes"
        pre = "edit"
        url = "/note/"
        weight = 2
      [[menu.nav]]
        name = "About"
        pre = "smile"
        url = "/about/"
        weight = 3
      [[menu.nav]]
        name = "Now"
        pre = "coffee"
        url = "/now/"
        weight = 4
      [[menu.nav]]
        name = "Tags"
        pre = "tag"
        url = "/tags/"
        weight = 5
      [[menu.nav]]
        name = "Categories"
        pre = "bookmark"
        url = "/categories"
        weight = 6
      [[menu.nav]]
        name = "RSS"
        pre = "rss"
        url = "/index.xml"
        weight = 7

One person uses ``layouts/TYPE/block.html`` that usually contains one ``<div
class="TYPE">`` element to emulate the concept of a block in the BEM
methodology. He also has a ``static/TYPE.styl`` that gets compiled to
``TYPE.css``. While not quite BEM, it's a start.

Hugo has `a roadmap <hugo 1.0 roadmap_>`_. It's worth consulting before I get too deeply involved in making modifications to Hugo.

########
Partials
########

When should layout HTML be placed in a subdirectory of ``layouts`` and when
should it be placed under ``layouts/partials``? I think the answer is to place
HTML under a subdirectory of ``layouts/`` when there is content in a
subdirectory of the ``contents`` folder. Use ``layouts/partials`` when an HTML
template includes the partial using the
``{{ partial "<PATH>/<PARTIAL>.html" . }}`` action.

When Hugo looks for a partial template, it checks just two places:

#. ``layouts/partials/*<PARTIALNAME>.html``
#. ``themes/<THEME>/layouts/partials/*<PARTIALNAME>.html``

The second argument is a dot (``.``). It gives the partial a "context". In Go
Templates, ``{{ . }}`` always refers to the *current context*. In the top
level of your template, this will be the data set made available to it. Inside
of an iteration, however, it will have the value of the current item in the
loop; i.e., ``{{ . }}`` will no longer refer to the data available to the
entire page.

If you need to access page-level data (e.g., page params set in front matter)
from within the loop, you will likely want to do one of the following (See `Introduction to Hugo Templating <https://gohugo.io/templates/introduction/>`_ for details):

#. Define a variable independent of context outside the loop; e.g.,
   ``{{ $title := .Site.Title }}``, and then reference ``$title`` inside the
   loop.
#. Use ``$.`` to access the global context; e.g., ``{{ $.Site.Title }}``
   inside a loop.

#########
Drop Caps
#########

My current drop-cap styles:

* drop-caps_cheshire    => ``drop-caps_cheshire``
* drop-caps_goudy       => ``drop-caps_goudy``
* drop-caps_de-zs       => ``drop-caps_de-zs``
* drop-caps_yinit       => ``drop-caps_yinit``

If I want to make a drop-caps component, I need to create a
``layouts/drop-caps`` folder. Each of my styles would be a modifier (or maybe
an element). Due to constraints of Hugo, they'd be placed in
``static/_<modifier-name>`` or some similar name. They can't be placed in the
``layouts/drop-caps`` folder because the CSS files need to be copied to the
``/public`` folder. Only files in ``static/`` are automatically copied. Should
the modifier carry the block in its name? For example, which of the following
naming conventions should the ``_chesire`` modifier be?

* ``static/_cheshire/_cheshire.css``
* ``static/drop-caps/_chesire.css``
* ``static/drop-caps_cheshire/modifier.css``
* ``static/modifier/_cheshire.css``
* ``static/modifier/drop-caps_cheshire.css``

Reconsidering the block part, the HTML needs to be under the ``layouts/``
folder, but could be organized in one of several ways.

* ``layouts/drop-caps/drop-caps.html``
* ``layouts/block/drop-caps.html``
* ``layouts/drop-caps.html``
* ``layouts/drop-caps/block.html``
* ``layouts/partials/block/drop-caps.html``
* ``layouts/partials/drop-caps/block.html``

With Hugo's constraints, I kind of like:

* ``layouts/partials/drop-caps.html``
* ``static/drop-caps/drop-caps.css``
* ``static/drop-caps/drop-caps_goudy.css``
* ``static/drop-caps/drop-caps_cheshire.css``

Simiilarly colors for the drop-caps block would be modifiers, such as ``static/
modifier/drop-caps_green.css``.

I thought I might have separate files for modifying the drop-cap fonts based
on screen width. I consider files like ``static/drop-caps/
drop-caps_goudy-120.css`` for screens with a max-width of 120ch. After some
experimentation I simplified, and just included a set of ``@media`` sections
in the existing files.

In the end, I defined a `drop-caps` block, putting the HTML in drop-caps.html.
I put the basic CSS in `static/style/drop-caps/drop-caps.css`. I have several
fonts whose only purpose is to style drop-caps letters, so I created a
modifier CSS file for each of them.

* layouts/partials/drop-caps.html
* static/style/drop-caps/

  * drop-caps.css
  * drop-caps_cheshire.css
  * drop-caps_de-za.css
  * drop-caps_goudy.css
  * drop-caps_kanzlei.css
  * drop-caps_yinit.css

The HTML file uses the definition of the variable ``componentDropCaps`` to define a specific drop-caps style, which is really a modifier. If ``componentDropCaps`` is defined in ``config/_default/params.toml``, say as "``"drop-caps_goudy"``", all pages will have drop caps in the Goudy font. A page can override that value by redefining ``componentDropCaps`` in its yaml or toml frontmatter.

I should create a mechanism for a page to opt-out of drop-caps entirely. Maybe set ``componentDropCaps`` to "``drop-caps_none``", or have another template variable, like ``componentDropCapsNone``, that if defined will select ``<section class="c-drop-caps_none">``. The former is simple enough. It puts an undefined CSS class into the ``<section>`` element.

#################
Two Column Layout
#################

***************
Simple Solution
***************

Here's a simple, maybe the simplest, two-column layout. A background color is set in the example below. it's easy to see that the two colomns are not the same height.

Summary: a left column with float:left and a fixed pixel width, and a right column with width:auto and a left margin equal to the left column width.

Additionally, set ``overflow:hidden`` on the container, otherwise the right column can wrap. In order to place child elements with 100% width in the columns, you also have to add the following CSS so their padding and border is included in that 100% to prevent overflow.

.. code-block:: css

  .child-element {
    box-sizing: border-box;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    -ms-box-sizing: border-box;
  }

.. code-block:: html

  <div id="container">
    <div id="left">
      Hello
    </div>
    <div id="right">
      <div style="background-color: red; height: 10px;">Hello</div>
    </div>
    <div class="clear"></div>
  </div>

The styling is:

.. code-block:: css

  #left {
    width: 200px;
    float: left;
  }
  #right {
    margin-left: 200px;
    /* Change this to whatever the width of your left column is*/
  }
  .clear {
    clear: both;
  }

The above is from `here <https://stackoverflow.com/questions/5573855/how-to-make-a-stable-two-column-layout-in-html-css>`_ and can be `seen here in this jsfiddle <http://jsfiddle.net/FVLMX/>`_.

Here is a `slight variation <http://jsfiddle.net/d5Lq2j14/>`_ that shows the two columns are not the same height. The structure adds a footer to delineate the bottom of the container and its two columns:

.. code-block:: html

  <body>
    <div id="container">
      <div id="left">
        <p>Hello.</p>

        <p>Once upon a time, they lived happily ever after.</p>

        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
      </div>
      <div id="right">
        <div class="child-element" style="background-color: red;">
          <p>Hello!</p>

          <p>Nunc auctor consectetur velit. Suspendisse quis mauris vitae neque vestibulum dapibus.</p>
        </div>
      </div>
      <div class="clear"></div>
    </div>
    <footer>The End.</footer>
  </body>

Here's the styling:

.. code-block:: css

  #container {
    overflow: hidden
  }

  #left {
    width: 200px;
    float: left;
  }

  #right {
    margin-left: 200px;
    /* Change this to whatever the width of your left column is*/
  }

  .child-element {
    box-sizing: border-box;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    -ms-box-sizing: border-box;
  }

  .clear {
    clear: both;
  }

***********************
A Simple Flexbox Layout
***********************

`Simple flexbox layout <http://jsfiddle.net/m5Xz2/100/>`_. This one seems to work well. Both columns background color extend to same height.

.. code-block:: html

  <div class="container">
    <div class="left">
      <p>Cras a arcu ut leo dapibus faucibus nec nec ante. Proin iaculis vel urna id pulvinar. Proin et dolor consectetur lacus suscipit aliquet ut vel nisi.</p>
    </div>
    <div class="right">
      <p>
        Once upon a time, I had a very short column.
      </p>
    </div>
  </div>

.. code-block:: css

  .container {
      display: flex;
  }
  .container > div {
      border:1px solid black;
  }

  .left {
      width: 200px;
      background: lightgray;
  }

  .right {
      width: 100%;
      background: azure;
  }

*****************************
Two Column Layout with Floats
*****************************

There's a good article from 2010 covering `two column layouts with floats <https://www.smashingmagazine.com/2010/11/equal-height-columns-using-borders-and-negative-margins-with-css/>`_. It covers several layouts whose common feature is equal height columns.

I'm interested in the first two layouts which present different ways of creating a two-column layout. The first one describes `centering columns without a wrapper`_. It uses the ``<body>`` element as the wrapper. It has limitations, but it works.

The second `uses a wrapper <two columns with a wrapper_>`_.

Centering Columns without a Wrapper
===================================

Its claim to being interesting is that it only uses borders and negative margins. Also, it doesn't use a wrapper ``<div>`` element to center columns. It uses the background color of `<body>` and the border of one of the columns to create background colors that vertically fill the "row".

The presentation and layout is in parts:

- `Placing the Elements`_
- `Block Formatting Context for Main ID`_
- `Uncover the Sidebar`_
- `Add Basic Styling`_
- `Consolidate the Styles`_

When using ``<body>`` as a wrapper, there are two things to remember:

- always style ``HTML`` with a background to prevent the background of ``<body>`` from extending beyond its boundaries and be painted across the viewport.
- never style ``HTML`` with ``height: 100%`` or the background of ``<body>`` will be painted no taller than the viewport.

The presumed layout is just five parts, a header, a footer, a left column for a sidebar, and a right column for the main content.

.. code-block:: html

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

Placing the Elements
--------------------

Here's some CSS to place the elements. These rules

- will style ``<html>`` with a background to prevent the browser from painting the background color of body outside our layout.
- will style ``<body>`` with auto margin to center the layout; the width is set using percentage. The background declaration is for ``#main``.
- will style the background of ``#header`` and ``#footer`` to mask the background color of body.
- set the background color of ``#sidebar`` to match the border color of ``#main``. This is the trick to make our columns appear as being of equal height.
- set the footer to clear any previous ``float`` so it stays below the columns, at the bottom of the layout.

.. code-block:: css

  html {
    background: #45473f;
  }

  body {
    width: 80%;
    margin: 20px auto;
    background: #ffe3a6;
  }

  #header {
    background: #9c9965;
  }

  #sidebar {
    float: left;
    width: 200px;
    background: #d4c37b;
  }

  #main {
    border-left: 200px solid #d4c37b;
  }

  #footer {
    clear: left;
    background: #9c9965;
  }

As `this jsfiddle shows <https://jsfiddle.net/dbc60/uo0fp7wn/12/>`_, it's not quite right. The sidebar is not vertically aligned with the main content and there is a gap above and below the sidebar. This is because out of these two containers, only one is a `block formatting context`_. So margins do not collapse in ``#sidebar`` while they do in ``#main``. This also means that ``#main`` will not contain floats and that applying ``clear:left`` to any nested element in there will clear ``#sidebar`` as well.

Block Formatting Context for Main ID
------------------------------------

So to prevent any float and margin collapsing issues we make all the main boxes block formatting contexts.

.. code-block:: css

  #header,
  #footer {
    overflow: hidden;
    zoom: 1;
  }

  #main {
    float: left;
  }

  #sidebar {
    margin-right: -200px;
  }

`Now we see <https://jsfiddle.net/dbc60/uo0fp7wn/13/>`_ that the border of ``#main`` hides ``#sidebar``. This is because of the stacking context. In the flow (tree order), ``#main`` comes after ``#sidebar`` so the former overlaps the latter.

Note that ``zoom: 1;`` is an old hack to work around bugs in IE6 and IE7. It is non-standard. Don't use it! I don't think there's any valid reason to support these ancient, buggy browsers. Per `CSS Tricks zoom <https://css-tricks.com/almanac/properties/z/zoom/>`_:

  In the days of IE6, zoom was used primarily as a hack. Many of the rendering bugs in both IE6 and IE7 could be fixed using zoom. As an example, ``display: inline-block`` didn't work very well in IE6/7. Setting ``zoom: 1`` fixed the problem. The bug had to do with how IE rendered its layout. Setting ``zoom: 1`` turned on an internal property called `hasLayout <https://stackoverflow.com/questions/1794350/what-is-haslayout>`_, which fixed the problem.

Uncover the Sidebar
-------------------

Positioning ``#sidebar`` brings it up in the stack.

.. code-block:: css

  #sidebar {
    position: relative;
  }

Note: if you make ``#main`` a new containing block you’ll revert to the original stack order. In this case, you’ll need to use ``z-index`` to keep ``#sidebar`` on top of ``#main``. This seems pretty fragile to me.

Add Basic Styling
-----------------

The last step in this process is to add some basic styling. These rules allow us to

- reset the height on html so the background of #main is not cut-off at the fold (this styling is inherited from the base styles sheet).
- draw a border all around the layout.
- create gaps at the bottom of the main boxes via padding, because the base styles sheet only sets top margins.

Note: The rule for ``<html>`` is shown here, but it makes more sense to remove that rule from the base styles sheet rather than overwriting the declaration here.

.. code-block:: css

  html {
    height: auto;
  }

  body {
    border: 1px solid #efefef;
  }

  #header,
  #main,
  #sidebar,
  #footer {
    padding-bottom: 2em;
  }

Consolidate the Styles
----------------------

The final CSS is:

.. code-block:: css

  html {
    height: auto;
    background: #45473f;
  }

  body {
    border: 1px solid #efefef;
    width: 80%;
    margin: 20px auto;
    background: #ffe3a6;
  }

  #header,
  #main,
  #sidebar,
  #footer {
    padding-bottom: 2em;
  }

  /* rules specific to a simple two-column layout */

  #header {
    background: #9c9965;
  }

  #sidebar {
    float: left;
    width: 200px;
    background: #d4c37b;
    margin-right: -200px;
    position: relative;
  }

  #main {
    border-left: 200px solid #d4c37b;
    float: left;
  }

  #header,
  #footer {
    clear: left;
    background: #9c9965;
    overflow: hidden;
    zoom: 1;
  }

The result can be seen here `in jsfiddle 19 <https://jsfiddle.net/dbc60/uo0fp7wn/19/>`_.

Add a Base Stylesheet
---------------------

In the final demo, the author added a base stylesheet to make links and other formatting consistent. `This jsfiddle shows the final result <https://jsfiddle.net/dbc60/uo0fp7wn/20/>`_. His stylesheet was:

.. code-block:: css

  /*
   * base.css | v0.6 (04252011) | Thierry Koblentz
   *
   * The purpose of this styles sheet is to set default styles for common browsers and address common issues (missing scrollbar, extended buttons in IE, gap below images, etc.)
   *
   * See: http://thinkvitamin.com/design/setting-rather-than-resetting-default-styling/
   *
   * Changes in  v0.6 (04252011):
   *    - swaped text-bottom for bottom and vice-versa for checkboxes and radio buttons (duh!)
   *
   * Changes in  v0.5 (03302011):
   *    - zeroing out line-height on sup and sub to avoid messing up with vertical space between lines
   *    - font and text-transform set to "inherit" for input, button, textarea, select, optgroup and option
   *    - background-color for select to fix a bug (inheritance) in webkit/mac
   *
   * Changes in  v0.4 (06132010):
   *    - input, button, textarea, select, optgroup, option {line-height: 1.4 !important;} (to override FF's default styling)
   *    - styling <ol> inside <ul> (merci Goulven)
   */

  /*
   * in webkit/Mac, select fails to inherit color, font-*, etc if there is no other styling like background for example (border will do to)
   */
  select {
  	background-color:transparent;
  }


  /* using height:100% on html and body allows to style containers with a 100% height
   * the overflow declaration is to make sure there is a gutter for the scollbar in all browsers regardless of content
   * note that there is no font-size declaration set in this rule. If you wish to include one, you should use font-size: 100.01% to prevent bugs in IE and Opera
   */
  html {
    height: 100%;
    overflow-y: scroll;
  }
  /* not all browsers set white as the default background color
   * color is set to create not too much contrast with the background color
   * line-height is to ensure that text is legible enough (that there is enough space between the upper and lower line)
   */
  body {
    height: 100%;
    background: #fff;
    color: #444;
    line-height: 1.4;
  }

  /* this choice of font-family is supposed to render text the same across platforms
   * letter-spacing makes the font a bit more legible
   */
  body, input, button, textarea, select {
    font-family: "Palatino Linotype", Freeserif, serif;
    letter-spacing: .05em;
  }
  h1, h2, h3, h4, h5, h6 {
    font-family: Georgia, "DejaVu Serif", serif;
    letter-spacing: .1em;
  }
  pre, tt, code, kbd, samp, var {
    font-family: "Courier New", Courier, monospace;
  }

  /* These should be self explanatory
   */
  h1 {font-size: 1.5em;}
  h2 {font-size: 1.4em;}
  h3 {font-size: 1.3em;}
  h4 {font-size: 1.2em;}
  h5 {font-size: 1.1em;}
  h6 {font-size: 1em;}

  h1, h2, h3, h4, h5 {font-weight: normal;}

  /* styling for links and visited links as well as for links in a hovered, focus and active state
   * make sure to keep these rules in that order, with :active being last
   * text-decoration: none is to make the links more legible while they are in a hovered, focus or active state
   * a:focus and :focus are used to help keyboard users, you may change their styling, but make sure to give users a visual clue of the element's state.
   * outline:none used with the pseudo-class :hover is to avoid outline when a user clicks on links
   * note that these last rules do not do anything in IE as this browser does not support "outline"
   */
  a:link {color: #000;}
  a:visited {text-decoration: none;}
  a:hover {text-decoration: none;}
  a:focus {text-decoration: none;}
  a:focus,:focus {outline: 1px dotted #000;}
  a:hover,a:active {outline: none;}

  /*
   * This one is commented out as it may be overkill (users who use both a mouse and the keyboard would lose keyboard focus)
   * Besides, this may create a performance issue
   * html:hover a {outline: none;}
   */

  /* margin and padding values are reset for all these elements
   * you could remove from there elements you do not used in your documents, but I don't think it'd worth it
   */
  body, p, dl, dt, dd, ul, ol, li, h1, h2, h3, h4, h5, h6, pre, code, form, fieldset, legend, input, button, textarea, blockquote, th, td {
    margin: 0;
    padding: 0;
  }

  /* this is to prevent border from showing around fieldsets and images (i.e., images inside anchors)
   */
  fieldset, img {
    border: 0;
  }

  /* to prevent a gap from showing below images in some browsers
   */
  img {vertical-align: bottom;}

  /* Styling of list items
   * This styles sheet contains a class to apply on lists to reset list-type and margin on LIs
   */
  ol li,
  ul ol li {list-style-type: decimal;}
  ul li {list-style-type: disc;}
  ul ul li {list-style-type: circle;}
  ul ul ul li {list-style-type: square;}
  ol ol li {list-style-type: lower-alpha;}
  ol ol ol li {list-style-type: lower-roman;}

  /* These should be self explanatory
   * I believe *most* UAs style sub and sup like this by default so I am not sure there is value to include these rules here
   * zeroing out line-height should prevent this from messing with the gap between lines
   */
  sub {
  	line-height:0;
    vertical-align: sub;
    font-size: smaller;
  }

  sup {
  	line-height:0;
    vertical-align: super;
    font-size: smaller;
  }

  /* color is to make that element stands out (see color set via body)
   * padding is used so Internet Explorer does not cut-off descenders in letters like p, g, etc.)
   */
  legend {
    color: #000;
    padding-bottom: .5em;
  }

  /* according to Eric Meyer's reset: tables still need 'cellspacing="0"' in the markup
   */
  table {
    border-collapse: collapse;
    border-spacing: 0;
  }

  /* caption and summary are very important for tabular data but because caption is nearly impossible to style across browsers many authors do not use it or use display:none to "hide" it (which is almost the same as not using it).
   * so to prevent such workaround, I am positioning this element off-screen
   */
  caption {
    position: absolute;
    left: -999em;
  }

  /* all th should be centered unless they are in tbody (table body)
   */
  th {text-align: center;}
  tbody th {text-align: left;}

  /* See Eric Meyer's article about Fixed Monospace Sizing
   * http://meyerweb.com/eric/thoughts/2010/02/12/fixed-monospace-sizing/
   */
  code {color: #06f;}
  code, pre {font-family: "Courier New", monospace, serif; font-size: 1em;}

  /* This should be self explanatory
   */
  blockquote, q, em, cite, dfn, i, cite, var, address {
    font-style: italic;
  }

  /* to prevent some browsers from inserting quotes on "q" and "p" ("p" in blockquotes)
   */
  blockquote p:before, blockquote p:after, q:before, q:after {content: '';}

  /* These should be self explanatory
   */
  th, strong, dt, b {
    font-weight: bold;
  }

  ins {
    text-decoration: none;
    border-bottom: 3px double #333;
  }

  del {text-decoration: line-through;}

  abbr,
  acronym {
    border-bottom: 1px dotted #333;
    font-variant: normal;
  }

  /* Creating white space (vertical gutters) via padding
   * most authors do not set right/left padding or margin on these elements, they rather use an extra wrapper or style the container with padding to create the left and right gap/gutter they need
   * I find that the latter creates less robust layouts because it leads authors to mix padding with width which creates issue with the broken box model (IE5 or IE6 in quirks mode)
   * so imho, setting this style using the child combinator (i.e., div > h1) should be the best way to do it, but unfortunately IE 6 does not support such syntax, so I have to go with the following + a reset (see next rule)
   */
  h1, h2, h3, h4, h5, h6, p, pre, ul, ol, dl, fieldset, address {padding:0 30px;}

  /* this is to reset the left/right gaps (created by the previous and next rules) on nested elements
   */
  dd p, dd pre, dd ul, dd ol, dd dl, li p, li pre, li ul, li ol, li dl, fieldset p, fieldset ul, fieldset ol {
    padding-right: 0;
    padding-left: 0;
  }

  /* These should be self explanatory
   */
  dd {
    padding-left: 20px;
    margin-top: .5em;
  }

  li {margin-left:30px;}

  /* we cannot use padding on a table to create left and right gaps (as we do with the elements above), instead we use margin
   */
  table {
    margin-right: 30px;
    margin-left: 30px;
  }

  /* we use margin for hr for the same reason we do for table
   */
  hr {
    margin-right: 30px;
    margin-left: 30px;
    border-style: inset;
    border-width: 1px;
  }

  /* top margin solution */
  /* this is my approach to create white space between elements, you do not have to adhere to it
   * rather than stylling these elements with top and bottom margin, or simply bottom margin I only use top margin
   */
  h1, h2, h3, h4, h5, h6, p, pre, dt, li, hr, legend, input, button, textarea, select, address, table {margin-top: 1.2em;}

  /* top padding solution */
  /* this is a different approach which may be less frustrating for novice because it avoids running into collapsing margin and allows to clear floats while preserving space above the element
   * if you decide to give this a try, then comment out the above rule and uncomment the two next ones
   */
   /*
   h1, h2, h3, h4, h5, h6, p, pre, dt, dd, li, legend, address {padding-top: 1.2em;}
   hr, input, button, textarea, select, table {margin-top: 1.2em;}
   */

  /* form elements
   * this should not affect the layout of the labels unless you style them in a way that padding applies
   * if I include this here it is mostly because when labels are styled with float and clear, top padding creates a gap between labels (bottom margin would, but not top margin)
   */
  label {padding-top: 1.2em;}

  /* line height helps to set the vertical alignment of radio buttons and check boxes (remember to group these in fieldsets)
   */
  fieldset {line-height: 1;}

  /* vertical alignment of checkboxes (a different value is served to IE 7)
   */
  input[type="checkbox"] {
    vertical-align: text-bottom;
    *vertical-align: baseline;
  }

  /* vertical alignment of radio buttons
   */
  input[type="radio"] {vertical-align: bottom;}

  /* vertical alignment of input fields for IE 6
   */
  input {_vertical-align: text-bottom;}

  /* all values set to 'inherit"
   * the line-height is to override FF's default styling
   */
  input, button, textarea, select, optgroup, option {
    font: inherit;
  	text-transform:inherit;
  	line-height: inherit !important;
  }
  /*
   * in webkit/Mac, select fails to inherit color, font-*, etc if there is no other styling like background for example (border will do to)
   */
  select {
  	background-color:transparent;
  }

  /* this is to fix IE 6 and 7 which create extra right/left padding on buttons
   * IMPORTANT: because IE 6 does not understand the first selector below, you need to apply the class "inputButton" to all input of type="button" in your documents
   * the first declaration is for IE 6 and 7, the second one for IE 6 only, the third one is for all browsers.
   */
  button,
  input[type="submit"],
  input[type="reset"],
  input[type="button"],
  .inputButton {
    *overflow: visible;
    _width: 0;
    padding: .2em .4em;
  }

  /* classes
   * to style elements with the default padding and margin we set on headings, paragraphs, lists, etc.
   * for example, this class could be used on a DIV inside a blockquote or a DIV inside a FORM, etc.
   */
  .block {
    padding: 0 30px;
    margin-top: 1.2em;
  }

  /* to swap padding for margin
   * for example, this class could be used on a heading you'd style with a bottom border
   */
  .padding2margin {
    margin-right: 30px;
    margin-left: 30px;
    padding-right: 0;
    padding-left: 0;
  }

  /* list items are styled by default with markers (disc, etc.) and left margin
   * if you apply the class "noMarker" to a list, its items won't display markers and won't have left margin
   */
  .noMarker li {
    list-style: none;
    margin-left: 0;
  }

  /*
       FILE ARCHIVED ON 00:27:09 Feb 22, 2012 AND RETRIEVED FROM THE
       INTERNET ARCHIVE ON 13:45:33 Jul 21, 2019.
       JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

       ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
       SECTION 108(a)(3)).
  */

.. _block formatting context: {{< ref "../../note/web/block-formatting-contexts/" >}}

Two Columns with a Wrapper
==========================

The markup for this example is very much like the original. The difference is ``#sidebar`` and ``#main`` are wrapped in a ``<div>`` with ``id="wrapper"``:

.. code-block:: html

  <div id="header">
      <h2><a href="#">Header</a></h2>
      <p>Lorem ipsum...</p>
  </div>

  <div id="wrapper">
    <div id="sidebar">
      <h2><a href="#">Sidebar</a></h2>
      <p>Lorem ipsum...</p>
    </div>
    <div id="main">
      <h2><a href="#">Main</a></h2>
      <p>Lorem ipsum...</p>
    </div>
  </div>

  <div id="footer">
      <h2><a href="#">Footer</a></h2>
      <p>Lorem ipsum...</p>
  </div>

#######
Sidebar
#######

It might be nice to have a sidebar to hold the navigation menu, and to use the categories list as a table of contents. I'd also like to have an expandable list of blog posts by year. I had that on my original blog, and I think it was handy.

******************
Sidebar Navigation
******************

The drop-caps component worked out okay. Next I will try to organize a sidebar and place the navigation menu there. I have a head start in that I have a partial for navigation, ``layouts/partials/nav.html``. It is included in ``layouts/_default/baseof.html``. I might have to make a ``body`` or ``grid`` component to contain a sidebar and another "main" section. Probably a grid with rows and columns to layout the sidebar, header, footer, and main areas.

Note that Hugo has its own `convention for defining a site menu <https://gohugo.io/content-management/menus/>`_. Menus *can* be defined in ``config.toml`` and referenced in partials through Hugo's template system. For example, placing ``range .Site.Menus.nav`` between template open (``{{``) and close (``}}``) pairs. I don't think Hugo *requires* menus to be defined this way. I think it exists as a convenience for website and theme developers.

While I'm working on this, the `Drupal Charity Theme`_ is worth looking at. Its components are organized per the BEM methodology. Likewise for the `Drupal Greek Theme`_.

A sidebar component could have elements like a title, and modifiers such as ``left`` and ``right``. Notionally, CSS following the BEM methodology would look like:

.. code-block:: css

    /* Block component */
    .sidebar{}

    /* Element that depends upon the block */
    .sidebar__title{}

    /* Modifier that changes the style of the block */
    .sidebar-left{} .sidebar-right{}

###################################
Code Blocks and Syntax Highlighting
###################################

The HTML for code blocks generated from markdown files embeds CSS styling. I'd rather have it generate HTML with a "well known" (i.e., predefined) set of class attributes. For example, this code block:

.. code-block:: text

    ```css
    code, tt.docutils.literal, pre {
      margin: 0.5em 0rem 0.5em 0rem;
      overflow: auto;
      overflow-y: hidden;
      font-family: "Inconsolata", monospace;
    }

    code, tt.docutils.literal {
      padding: 2px 4px;
      vertical-align: text-bottom;
    }

    pre {
      padding: 1em;
      background-color: gainsboro;
      border-bottom: 1px solid silver;
      border-left: 2px solid slategray;
    }
    ```

will generate this kind of HTML output:

.. code-block:: html

    <pre style="color:#f8f8f2;background-color:#272822;-moz-tab-size:4; -o-tab-size:4;tab-size:4">
      <code class="language-css" data-lang="css">
        <span style="color:#f92672">code</span>
        <span style="color:#f92672">,</span>
        <span style="color:#f92672">tt</span>.

Putting the same CSS in a code block in a reStructuredText file, like so:

.. code-block:: css

    code, tt.docutils.literal, pre {
      margin: 0.5em 0rem 0.5em 0rem;
      overflow: auto;
      overflow-y: hidden;
      font-family: "Inconsolata", monospace;
    }

    code, tt.docutils.literal {
      padding: 2px 4px;
      vertical-align: text-bottom;
    }

    pre {
      padding: 1em;
      background-color: gainsboro;
      border-bottom: 1px solid silver;
      border-left: 2px solid slategray;
    }

results in this kind of HTML output:

.. code-block:: html

    <pre class="code css literal-block">
    <span class="name tag">code</span>
    <span class="operator">,</span>
    <span class="name tag">tt</span>
    <span class="name class">.docutils.literal</span>
    <span class="operator">,</span>
    <span class="name tag">pre</span>
    <span class="punctuation">{</span>
      <span class="keyword">margin</span>
      <span class="operator">:</span>
      <span class="literal number">0.5em</span>
    </pre>

which is much easier to reason about, and I can define my own styling rules. It also shows the shortcomings of my current CSS definitions (margins and padding aren't correct).

Hugo's opinions about HTML output may be too strong. I would prefer having more control over style and syntax highlighting. On the other hand, I may just be ignorant of the correct tuning knobs.

##################
Social Media Links
##################

I like the sidebar social media links at `spf13 <https://spf13.com/>`_. His site is powered by Hugo and `on GitHub <https://github.com/spf13/spf13.com>`_. Look there to see how he created and styled those links.

#########
Resources
#########

- `BEM`_
- `Hugo 1.0 Roadmap`_
- `The Difference between Blog Categories and Blog Tags <blog categories vs tags_>`_
- `Categories and Tags`_
- `Organize Your Blog Design with Categories and Tags`_
- `Blog Planning <{{< ref "blog-planning.md" >}}>`_.
- `Drupal Charity Theme`_
- `Drupal Greek Theme`_
- `Learn Theme for Hugo`_ is a highly customizable theme to help you learn how to create custom styles using Hugo.

.. _bem: https://en.bem.info/
.. _hugo 1.0 roadmap: https://discourse.gohugo.io/t/roadmap-to-hugo-v1-0/2278
.. _blog categories vs tags: https://www.bloggingbasics101.com/what-is-the-difference-between-blog-categories-and-blog-tags/
.. _categories and tags: https://www.websitemuscle.com/top-10-must-dos-for-good-blog-posts-9-categories-and-tags/
.. _organize your blog design with categories and tags: https://www.dummies.com/social-media/blogging/organize-your-blog-design-with-categories-and-tags/
.. _drupal charity theme:  https://github.com/ShuvoHabib/charity-theme
.. _drupal greek theme: https://github.com/ShuvoHabib/Geek-Theme
.. _learn theme for hugo: https://learn.netlify.com/en/basics/style-customization/

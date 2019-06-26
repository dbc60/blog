---
layout: post
title: Web Design
date: 2015-12-30
draft: true
categories: blog
tags: [typography, design]
excerpt: A study of various web designs with the hope of bringing a good one to this website.
---

## Contents
{:.no_toc}

- TOC
{:toc}

## Document History


| Date | Author | Summary of Changes |
|-----------:|-------------:|:------------|
| 2016.03.07 | Doug Cuthbertson | Initial draft. |
| 2016.07.31 | Doug | Renamed file from 2016-03-07-typography.md to 2016-07-31-web-design.md |

## My Multiple Theme Design

- `index.html` has YAML front matter specifying the default layout (`_layout/default.html`).
- The default layout has a Liquid template line to include `head.html` ({% raw %}`{% include head.html %}` {% endraw %})
- `head.html` includes a stylesheet for a particular theme, such as: `<link rel="stylesheet" href="{{ site.baseurl }}css/themes/default-theme/default-theme.css" type="text/css" media="screen">`. The Sass code for these themes lives in subdirectories of the `css` directory. Jekyll compiles them and copies the resulting artifacts to `_site/css`. Each theme imports (from the `scss` directory):

- `base/normalize` to set some consistent defaults.
- `base/svg-icons` to add <abbr title="Scalable Vector Graphics">SVG</abbr> icons for various popular websites.
- 'modules/color-contrast' to add some functions to calculate luminance and create contrasting colors.
- 'themes/<theme-name>/variables' which sets theme-specific variables and imoports `modules/variables` for default values that aren't already set by the theme.
- `themes/<theme-name>/style` to set the style for the theme.

In turn, `_main.scss` sets `charset` to `UTF-8` and imports:

- `base/_svg-icons.scss`, SVG icons for various social media sites
- `modules/_color-contrast.scss`, functions for calculating luminance and contrasting colors
- `modules/_variables.scss`, default color values and font faces
- `base/_config.scss` defines the styles for body, headings, and various elements, classes and ids. It would be nice if I could figure out how to make these part of the themes. I think I'd have to change the theme=specific CSS to import icons, modules and variables from its own directory and not import `base/_config.scss`.

I think each theme should have its own copy of `base/_config.scss`, `modules/_variables.scss` and `base/_style.scss`. Most, if not all of what they have in common should be unique. The only thing they all share is the HTML elements, classes and ids they style.

One thing I want to change immediately is the fact that `header.html` "hardwires" my Gravatar:

```html
<header role="banner" id="banner">
    <h1 id="site-title">{{ site.title }}</h1>
    <h2 id="site-sub-title">{{ site.description }}</h2>
    <a href="{{ site.baseurl }}" class="site-avatar">
        <img src="{{ site.avatar }}" alt="Gravatar" id="header-img"/>
    </a>
</header>
```

It should have elements that allow CSS/SCSS to style it with text and images. The style should determine whether or not the Gravatar is part of the heading.

CSS Zen Garden starts with an "intro" `<section>` that contains a `<header>` and two `<div>` blocks, "summary" and "preamble". The header block is often used as title, subtitle and in various designs.

```html
<section class="intro" id="zen-intro">
    <header role="banner">
      <h1>Title</h1>
      <h2>Subtitle</h2>
    </header>

    <div class="summary" id="zen-summary" role="article">
      <p></p>
      <p></p>
    </div>

    <div class="preamble" id="zen-preamble" role="article">
      <h3>Preamble Heading</h3>
      <p></p>
      <p></p>
      <p></p>
    </div>
  </section>
```

### Update August 16th

- `index.html` uses the default layout.
- `default.html` includes head.html.
- `head.html` has a `<link>` element that references our theme, `{{ site.baseurl }}css/themes/default-theme/default-theme.css`.
- The default theme imports several Sass files. Among them are the theme-specific files `_variables.scss` and `_style.scss`.
- `_variable.scss` imports a base set of theme-specific colors from `_colors.scss`, sets the value of some variables and imports `modules/_variables.scss` to fill in the remaining variable definitions.

I need to consolidate these variable definitions into a reasonable set. There are far too many. The goal is to create a reasonably flexible layout that uses a small set of variable definitions for colors, element sizes, padding, borders and margins.

### My HTML Layout
The layout starts with `_layouts/default.html`. The `<body>` component is:

```html
<body>
    <div id="container">
        <header class="site-header">
            {% raw %}
            {% include header.html %}
            {% include navigation.html %}
            {% endraw %}
        </header>   <!-- end class="site-header" -->
        <div id="boxes">  <!-- New div wrapper around the two boxes whose height we want to match -->
            <main id="left-column">
            {% raw %}
                {{ content | replace: '<li>[ ]', '<li class="checkbox">' | replace: '<li>[x]', '<li class="checkbox_done">'  }}
            {% endraw %}
            </main>
            {% raw %}
            {% include sidebar.html %}
            {% endraw %}
        </div>  <!-- end id="boxes" -->
        {% raw %}
        {% include footer.html %}
        {% endraw %}
    </div>  <!-- end id="container" -->
    <!-- analytics.html is just a script, so it doesn't need to be in the div container -->
    {% raw %}
    {% include analytics.html %} {% endraw %}
</body>
```

### Comparison to CSS Zen Garden
Comparing this to [CSS Zen Garden](#css-zen-garden-html-layout), we see:

The `body` element needs an `id` attribute so different layouts can be styled differently. When I create a new layout, even if it has the same structure as `_layouts/default.html`, it can have a different `id` in its body element. Per [ID Your Body for Greater CSS Control and Specificity](https://css-tricks.com/id-your-body-for-greater-css-control-and-specificity/), I don't need a separate stylesheet for pages using an alternate layout. If the contact page has a body element like `<body id="contact-page">`, then elements on that page could be given unique styles. For example, links could be red instead of blue:

```css
a {
  color: blue;
}

#contact-page a {
  color: red;
}
```

The first `div` element should have a class, like `"page-wrapper"` instead of the `"container"` id. It's a little more descriptive.

The `header` should have a `role` attribute whose value is `banner`. Predefined role attributes are listed in the <abbr title="World Wide Web Consortium">W3C</abbr> document [XHTML Role Attribute Module](https://www.w3.org/TR/2007/WD-xhtml-role-20071004/). The `banner` role is used for content that typically contains the site logo and other key advertisements for the site. It think it also means that my navigation content should be outside of the banner header.

Inside its `page-wrapper`, CSS Zen Garden starts with a `<section>` element (whose class is 'intro' and id is 'zen-intro') that contains a `<header>` and two `<div>` elements. The `<header>` has a role of 'banner' and wraps the title and subtitle. The two `<div>` elements that follow the `<header>` are for a page summary and preamble, and are given class attributes of those same names. After the `<section>` block, it continues with a sequence of `<div>` elements, one for each major part of the page. The `<div>`s for those parts are labeled with the following class attributes:

- main supporting
- participation
- benefits
- requirements

In contrast, I have one `div` element (boxes) containing a `main` element, whose `id` is `"left-column"`, and a sidebar wrapped in an `aside` element (see `_includes/sidebar.html`), whose `id` is `"right-column"`. This is more rigid, because it's built with a two-column layout in mind.

On the other hand, CSS Zen Garden has a `footer` element in the `div` `class="main supporting"` which contains some icons and links to the W3 HTML and CSS validators, its Github repository and others. After the `class="main supporting"` `div`, it ends with an `<aside class="sidebar" role="complementary">` element. This element contains a `<div class="wrapper">` which contains three more `div` sections:

-  `<div class="design-selection" id="design-selection">`: a list of links to specific CSS designs. This list is wrapped in a `nav` element whose role is `"navigation"`.
- `<div class="design-archives" id="design-archives">`: a list of links to the next and previous sets, and a link to a "view all" page. This list is wrapped in a `nav` element whose role is `"navigation"`.
- `<div class="zen-resources" id="zen-resources">`: a list of links to resources. This section is a simple list with no `<nav>` wrapper.

## CSS Zen Garden HTML Layout
[CSS Zen Garden](http://www.csszengarden.com/) is a beautiful gallery of designs that are done entirely in CSS. I suspect the layout of its HTML helps make the site flexible enough to support an incredibly rich and diverse set of designs. The site has a few tips on building your CSS file:

- go responsive; test your layout at multiple screen sizes.
- your browser testing baseline: IE9+, recent Chrome/Firefox/Safari, and iOS/Android
- Graceful degradation is acceptable, and in fact highly encouraged.
- use classes for styling. Don't use ids.
- web fonts are cool, just make sure you have a license to share the files.
- use `:first-child`, `:last-child` and `:nth-child` to get at non-classed elements
- use `::before` and `::after` to create pseudo-elements for extra styling
- use multiple background images to apply as many as you need to any element
- use the Kellum Method for image replacement, if still needed. [Kellum Method](http://goo.gl/GXxdI)
- don't rely on the extra `divs` at the bottom. Use `::before` and `::after` instead.

### The Kellum Method
The Kellum Method is CSS styling to hide text. The general idea is to ensure long strings of text will never flow into the container. The CSS shown below will cause text to flow away from the container:

```css
.hide-text {
  text-indent: 100%;
  white-space: nowrap;
  overflow: hidden;
}
```

### The HTML Layout
Here is the `body` of the HTML:

```html
<body id="css-zen-garden">
<div class="page-wrapper">

  <section class="intro" id="zen-intro">
    <header role="banner">
      <h1>CSS Zen Garden</h1>
      <h2>The Beauty of
        <abbr title="Cascading Style Sheets">CSS</abbr>
        Design
      </h2>
    </header>

    <div class="summary" id="zen-summary" role="article">
      <p>
        <abbr title="Cascading Style Sheets">CSS</abbr>
      </p>
      <p>
        <a href="/examples/index" title="This page's source HTML code, not to be modified.">html file</a>
        <a href="/examples/style.css" title="This page's sample CSS, the file you may modify.">css file</a>
      </p>
    </div>

    <div class="preamble" id="zen-preamble" role="article">
      <h3>Preamble</h3>
      <p>
        <abbr title="Document Object Model">DOM</abbr>
        <abbr title="Cascading Style Sheets">CSS</abbr>
      </p>
      <p>
        <abbr title="World Wide Web Consortium">W3C</abbr>
        <abbr title="Web Standards Project">WaSP</abbr>
      </p>
      <p></p>
    </div>
  </section>

  <div class="main supporting" id="zen-supporting" role="main">
    <div class="explanation" id="zen-explanation" role="article">
      <h3>About?</h3>
      <p>
        <abbr title="Cascading Style Sheets">CSS</abbr>
        <abbr title="HyperText Markup Language">HTML</abbr>
        <abbr title="Cascading Style Sheets">CSS</abbr>
      </p>
      <p>
        <abbr title="Cascading Style Sheets">CSS</abbr>
      </p>
    </div>

    <div class="participation" id="zen-participation" role="article">
      <h3>Participation</h3>
      <p></p>
      <p></p>
      <p></p>
    </div>

    <div class="benefits" id="zen-benefits" role="article">
      <h3>Benefits</h3>
      <p></p>
    </div>

    <div class="requirements" id="zen-requirements" role="article">
      <h3>Requirements</h3>
      <p></p>
      <p></p>
      <p>We&#8217;re well past the point of needing another garden-related design.</p>
      <p></p>
      <p role="contentinfo">
        <a href="http://www.mezzoblue.com/">Dave Shea</a>
        <a href="http://www.mediatemple.net/">mediatemple</a>
        <a href="http://www.amazon.com/exec/obidos/ASIN/0321303474/mezzoblue-20/">Zen Garden, the book</a>
      </p>
    </div>

    <footer>
      <a
        href="http://validator.w3.org/check/referer"
        title="Check the validity of this site&#8217;s HTML"
        class="zen-validate-html">
        HTML
      </a>
      <a
        href="http://jigsaw.w3.org/css-validator/check/referer"
        title="Check the validity of this site&#8217;s CSS"
        class="zen-validate-css">
        CSS
      </a>
      <a
        href="http://creativecommons.org/licenses/by-nc-sa/3.0/"
        title="View the Creative Commons license of this site: Attribution-NonCommercial-ShareAlike."
        class="zen-license">
        CC
      </a>
      <a
        href="http://mezzoblue.com/zengarden/faq/#aaa"
        title="Read about the accessibility of this site"
        class="zen-accessibility">
        A11y
      </a>
      <a
        href="https://github.com/mezzoblue/csszengarden.com"
        title="Fork this site on Github"
        class="zen-github">
        GH
      </a>
    </footer>

  <!-- end of <div class="main supporting" id="zen-supporting" role="main"> -->
  </div>


  <aside class="sidebar" role="complementary">
    <div class="wrapper">

      <div class="design-selection" id="design-selection">
        <h3 class="select">Select a Design:</h3>
        <nav role="navigation">
          <ul>
            <li>
              <a href="/221/" class="design-name">Mid Century Modern</a>
              <a href="http://andrewlohman.com/" class="designer-name">Andrew Lohman</a>
            </li>          <li>
              <a href="/220/" class="design-name">Garments</a>
              <a href="http://danielmall.com/" class="designer-name">Dan Mall</a>
            </li>
            <li>
              <a href="/219/" class="design-name">Steel</a>
              <a href="http://steffen-knoeller.de" class="designer-name">Steffen Knoeller</a>
            </li>
            <li>
              <a href="/218/" class="design-name">Apothecary</a>
              <a href="http://trentwalton.com" class="designer-name">Trent Walton</a>
            </li>
            <li>
              <a href="/217/" class="design-name">Screen Filler</a>
              <a href="http://elliotjaystocks.com/" class="designer-name">Elliot Jay Stocks</a>
            </li>
            <li>
              <a href="/216/" class="design-name">Fountain Kiss</a>
              <a href="http://jeremycarlson.com" class="designer-name">Jeremy Carlson</a>
            </li>
            <li>
              <a href="/215/" class="design-name">A Robot Named Jimmy</a>
              <a href="http://meltmedia.com/" class="designer-name">meltmedia</a>
            </li>
            <li>
              <a href="/214/" class="design-name">Verde Moderna</a>
              <a href="http://www.mezzoblue.com/" class="designer-name">Dave Shea</a>
            </li>
          </ul>
        </nav>
      </div>

      <div class="design-archives" id="design-archives">
        <h3 class="archives">Archives:</h3>
        <nav role="navigation">
          <ul>
            <li class="next">
              <a href="/214/page1">
                Next Designs <span class="indicator">&rsaquo;</span>
              </a>
            </li>
            <li class="viewall">
              <a
                href="http://www.mezzoblue.com/zengarden/alldesigns/"
                title="View every submission to the Zen Garden.">
                View All Designs
              </a>
            </li>
          </ul>
        </nav>
      </div>

      <div class="zen-resources" id="zen-resources">
        <h3 class="resources">Resources:</h3>
        <ul>
          <li class="view-css">
            <a
              href="style.css"
              title="View the source CSS file of the currently-viewed design.">
              View This Design&#8217;s <abbr title="Cascading Style Sheets">CSS</abbr>
            </a>
          </li>
          <li class="css-resources">
            <a
              href="http://www.mezzoblue.com/zengarden/resources/"
              title="Links to great sites with information on using CSS.">
              <abbr title="Cascading Style Sheets">CSS</abbr>
            </a>
          </li>
          <li class="zen-faq">
            <a
              href="http://www.mezzoblue.com/zengarden/faq/"
              title="A list of Frequently Asked Questions about the Zen Garden.">
              <abbr title="Frequently Asked Questions">FAQ</abbr>
            </a>
          </li>
          <li class="zen-submit">
            <a
              href="http://www.mezzoblue.com/zengarden/submit/"
              title="Send in your own CSS file.">
              Submit a Design
            </a>
          </li>
          <li class="zen-translations">
            <a
              href="http://www.mezzoblue.com/zengarden/translations/"
              title="View translated versions of this page.">
              Translations
            </a>
          </li>
        </ul>
      </div>
    </div>
  </aside>

<!-- end of <div class="page-wrapper"> -->
</div>

<!--

  These superfluous divs/spans were originally provided as catch-alls to add extra imagery.
  These days we have full ::before and ::after support, favour using those instead.
  These only remain for historical design compatibility. They might go away one day.

-->
<div class="extra1" role="presentation"></div>
<div class="extra2" role="presentation"></div>
<div class="extra3" role="presentation"></div>
<div class="extra4" role="presentation"></div>
<div class="extra5" role="presentation"></div>
<div class="extra6" role="presentation"></div>

</body>
```

## Web Design in 4 Minutes
These are my notes from [Web Design in 4 Minutes](http://jgthms.com/web-design-in-4-minutes/). That site lists some simple guidelines for making a website. I've written only the ones I think are good.

Note that this site is somewhat disingenuous. There's [a lot more CSS](http://jgthms.com/web-design-in-4-minutes/website.css) to style the elements than presented here. I think most of the 'extra' CSS is due to the buttons at the end of the article. There is also some JavaScript that is not even mentioned in the article. So, to get similar results, a lot more work needs to be done.

It might be worth considering a pure CSS framework, like [Tachyons](http://tachyons.io/).

### Create Content
The first thing you should work on is the *content* of the site. The purpose of design is to enhance the presentation of the content to which it is applied. If there's no content, then there's no reason for a design.

### Style the Text Blocks
The first `css` rule you can write for your new content ready to be published is one to center the text. Long lines are hard to read. Setting a limit of characters per line greatly enhances readability and appeal of a wall of text.

```css
body {
    margin: 0 auto;
    max-width: 50em;
}
```

### Set a Font Family
The author claims browsers default to "`Times`", which can look unappealing because it is the "unstyled" font. He recommends specifying `Helvetica`, `Arial` and `sans-serif`:

```css
body {
    font-family: "Helvetica", "Arial", sans-serif;
}
```

The commenters on [HN](https://news.ycombinator.com/item?id=12167758) recommend specifying just `sans-serif`, because it *will* be the browser default font which the user can change, which is even better. One says, "For the small group that don't force their font choices by default yet change their default font settings, it is better to use serif/sans-serif instead of specifying a font family to respect the user's choices." So lets have:

```css
body {
    font-family: sans-serif;
}
```

### Set the Spacing
Here's a recommendation for space around and within your site's content to increase the appeal of each page:

```css
body {
    line-height: 1.5;
    padding: 4em 1em;
}

h2 {
    margin-top: 1em;
    padding-top: 1em;
}
```

### Color and Contrast
Here is what *not* to do. Do not set the body color to a medium gray, like `#555` and set heading text to a dark gray, like `#333`. These setting provide insufficient contrast.

### Color for Code Excerpts
Here's the author's suggestion. Offset code blocks with a light gray background and extra padding:

```css
code,
pre {
    background: #eee;
}

code {
    padding: 2px 4px;
    vertical-align: text-bottom;
}

pre {
    padding: 1em;
}
```

N.B.: the bottom padding of `2px` in the `code` specification above will probably screw up the base alignment of regular text with inline `code`.

### Primary and Secondary Colors
The author says, "Most brands have a **primary color** that acts as a visual accent. On a website, this accent can be used to provide emphasis on interactive elements, like links." and gives an example of coloring CSS links with a primary color:

```css
a {
    color: #e81c4f;
}
```

To keep a balance, some secondary colors are needed to complement the accent color with more *subtle* shades. These shades can be used on borders, backgrounds or even body text.

```css
body {
  color: #566b78;
}

code,
pre {
  background: #f5f7f9;
  border-bottom: 1px solid #d8dee9;
  color: #a7adba;
}

pre {
  border-left: 2px solid #69c;
}
```

### Consider Custom Fonts
If you want to use a custom font, one like `Roboto` can be included:

```css
@import 'https://fonts.googleapis.com/css?family=Roboto:300,400,500';

body {
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
}
```

### Consider Adding Images
Use graphics and icons as ornaments to support your content, or as active parts in the message you want to convey. Here's an example of adding a background image from [Unsplash](https://unsplash.com/photos/qH36EgNjPJY) to the header:

```css
header {
  background-color: #263d36;
  background-image: url("header.jpg");
  background-position: center top;
  background-repeat: no-repeat;
  background-size: cover;
  line-height: 1.2;
  padding: 10vw 2em;
  text-align: center;
}
```

Here's an example of adding a logo:

```css
header img {
  display: inline-block;
  height: 120px;
  vertical-align: top;
  width: 120px;
}
```

Here are some examples to enhance the text styles:

```css
header h1 {
  color: white;
  font-size: 2.5em;
  font-weight: 300;
}

header a {
  border: 1px solid #e81c4f;
  border-radius: 290486px;
  color: white;
  font-size: 0.6em;
  letter-spacing: 0.2em;
  padding: 1em 2em;
  text-transform: uppercase;
  text-decoration: none;
  transition: none 200ms ease-out;
  transition-property: color, background;
}

header a:hover {
  background:  #e81c4f;
  color: white;
}
```

### Share Buttons
This is the HTML used to create three buttons near the bottom of the page:

```html
<h2>Share the love!</h2>
<nav class="buttons">
  <a class="button github" href="https://github.com/jgthms/web-design-in-4-minutes" target="_blank">
    <em>Download on</em> <strong>GitHub</strong>
  </a>
  <a
    class="button facebook"
    href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fjgthms.com%2Fweb-design-in-4-minutes%2F"
    rel="nofollow"
    target="_blank"
    >
    <em>Share on</em> <strong>Facebook</strong>
  </a>
  <a
    class="button twitter"
    data-social-network="Twitter"
    data-social-action="tweet"
    data-social-target="http://jgthms.com/web-design-in-4-minutes/"
    href="https://twitter.com/intent/tweet?text=Web%20Design%20in%204%20minutes&url=http%3A%2F%2Fjgthms.com%2Fweb-design-in-4-minutes%2F&via=jgthms"
    rel="nofollow"
    target="_blank"
    >
    <em>Share on</em> <strong>Twitter</strong>
  </a>
</nav>
```

There is [a lot of css](http://jgthms.com/web-design-in-4-minutes/website.css) to style them.

## Modular Scales for Typography
[More Meaningful Typography](http://alistapart.com/article/more-meaningful-typography) is an interesting article about applying modular scales to web design.

## Color Contrast Rule of Thumb
Look to the [Snook Colour Contrast Check](http://snook.ca/technical/colour_contrast/colour.html) to verify color difference and brightness difference if you want to ensure your choices are within the [Web Content Accessibility Guidelines 2.0](https://www.w3.org/TR/WCAG20/) (WCAG). Here is a link to the [WCAG contrast ratio formula](http://www.w3.org/TR/2008/REC-WCAG20-20081211/#visual-audio-contrast-contrast).

- If the goal is to maintain consistent contrast between heading text and body text vs the background color, then use a darker color for the body text than the heading. Large blocks of text tend to appear darker than smaller text of the same color.
- Don't use anything lighter than `#222` for body text. Anything lighter is too low contrast on light backgrounds.
- new paragraphs should be indicated by either extra space above the new paragraph *or* indentation, but not both. One might prefer indentation, because it saves vertical space.

## Better Motherfucking Website Style
The [Better Motherfucking Website](http://bettermotherfuckingwebsite.com) uses the following styles:

```css
body {
  margin: 40px auto;
  max-width: 650px;
  line-height: 1.6;
  font-size: 18px;
  color:#444;
  padding:0 10px
}

h1,h2,h3 {
  line-height: 1.2
}
```

This sets the minimum line height of 1.6 for body copy and makes the top three headings smaller. It sets the contrast lower than plain black on white, but it is within the limits of acceptable contrast.

It also sets the size of the minimum body copy to 18px to make it more readable. Perhaps that size is why lower contrast text works.

Delightfully, it sets the maximum width of the body to 650px. The goal is to keep lines between 60 and 80 characters in length.

## The Best Motherfucking Website Style
The [Best Motherfucking Website](https://bestmotherfucking.website) claims the perfect website's attributes are:

- Lightweight and loads fast.
- Fits on all screen sizes.
- Looks the same in all browsers.
- Accessible to everyone who visits your site.
- Legible and gets the point across.

Design is to plan and make something for a specific purpose. The most basic purpose of text on a website is to be read.

It uses the following styles:

```css
body {
  margin: 1em auto;
  max-width: 40em;
  padding: 0 0.62em;
  font: 1.2em/1.62em sans-serif;
}

h1, h2, h3 {
  line-height: 1.2em;
}

@media print {
  body {
    max-width: none
  }
}
```

In contrast to the [Better Motherfucking Website](#better-motherfucking-website-style), this site uses real black-on-white text, uses `em` (which are scalable units) instead of `px` (which are fixed size and depend on the size and resolution of the screen) to set `margin`, `max-width` `padding` and `font-size`.

Interestingly, it sets the font size to `1.2em/1.62em`, which is about `0.74em`. To help understand this setting, look to the Mozilla Developer Network article on [CSS font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size). It has a lot to say about `em` and other measures. Specifically:

> Another way of setting the font size is with `em` values. The size of an `em` value is dynamic. When defining the `font-size` property, an `em` is equal to the size of the font that applies to the parent of the element in question. If you haven't set the font size anywhere on the page, then it is the browser default, which is probably `16px`. So, by default `1em = 16px`, and `2em = 32px`. If you set a `font-size` of `20px` on the body element, then `1em = 20px` and `2em - 40px`. Not that the value `2` is essentially a multiplier of hte current `em` size.

In order to calculate the em equivalent to any pixel value required, you can use this formula:

```
em = desired element pixel value / parent element font-size in pixels
```

For example, suppose the `font-size` of the body of the page is set to `1em`, with the browser standard of `1em = 16px`; if the `font-size` you want is `12px`, then you should specify `0.75em (because `12/16 = 0.75`). Similarly, if you want a font size of `10px`, then specify `0.625em` (`10/16 = 0.625`), for `22px`, specify `1.275em` (`22/16`).

A popular technique to use throughout the document is to set the `font-size` of the body to `62.5%` (that is 62.5% of the default of `16px`), which equates to `10px`, or `0.625em`. Now you can set the `font-size` for any elements using `em` units, with an easy-to-remember conversion, by dividing the `px` value by `10`. This way `6px = 0.6em`, `8px = 0.8em`, `12px = 1.2em`, `14px = 1.4em`, `16px = 1.6em`. For example:

```css
body {
  font-size: 62.5%; /* font-size 1em = 10px on default browser settings */
}
span {
  font-size: 1.6em; /* 1.6em = 16px */
}
```

## References
- [Snook Colour Contrast Check](http://snook.ca/technical/colour_contrast/colour.html)
- [WebAIM Color Contrast Checker](http://webaim.org/resources/contrastchecker/)
- [HTML CSS Color Picker](http://www.htmlcsscolor.com/) provides names of the nearest color to a given color, provides shades similar to the given color, and other capabilities.
- [Web Content Accessibility Guidelines 2.0](https://www.w3.org/TR/WCAG20/)
- [WCAG contrast ratio formula](http://www.w3.org/TR/2008/REC-WCAG20-20081211/#visual-audio-contrast-contrast)
- [Contrast - WCAG compliant (sass) at CodePen](http://codepen.io/MadeByMike/pen/sDpxg/).
- [Paletton](http://paletton.com/#uid=1000u0kllllaFw0g0qFqFg0w0aF)
- The Elements of Typographic Style, by Robert Bringhurst
- Thinking with Type, by Ellen Lupton
- The Complete Manual of Typography, by James Felici
- On Book Design, by Richard Hendel
- Typographers on Type, by Ruari McLean.
- [The Elements of Typographic Style Applied to the Web](http://webtypography.net/toc/). It's a work in progress for many years, and the entire site is available [on GitHub](https://github.com/clagnut/webtypography)
- [Interactive Guide to Blog Typography](http://www.kaikkonendesign.fi/typography/)
- [Hack Design courses](http://hackdesign.org/courses/) have some offerings on typography.
- [Designing for the Web](http://designingfortheweb.co.uk/book/) is a free online version of the book by the same name.
- [Web Design in 4 Minutes](http://jgthms.com/web-design-in-4-minutes/). The site is also available on [GitHub](https://github.com/jgthms/web-design-in-4-minutes).
- [Show HN: Web Design in 4 minutes](https://news.ycombinator.com/item?id=12166687) has commentary on [Web Design in 4 Minutes](http://jgthms.com/web-design-in-4-minutes/). Most of it is about how low-contrast text and backgrounds make sites more difficult to read.
- [Contrast Rebellion](http://contrastrebellion.com/) which is about low-contrast font color and unreadable text.
- [Chrome Accessibility Audit](https://chrome.google.com/webstore/detail/accessibility-developer-t/fpkknkljclfencbdbgkenhalefipecmb?hl=en)
- [Web Content Accessibility Guidelines - Distinguishable](https://www.w3.org/TR/WCAG/#visual-audio-contrast)
- [Motherfucking Website](http://motherfuckingwebsite.com/)
- [Better Motherfucking Website](http://bettermotherfuckingwebsite.com/)
- [Best Motherfucking Website](https://bestmotherfucking.website/)
- [Hugo Tunius](https://hugotunius.se/), an example of a lightweight website.
- [The Website Obesity Crisis](http://idlewords.com/talks/website_obesity.htm)
- [Tachyons Framework](http://tachyons.io/) for creating fast loading, highly readable, 100% responsive interfaces with as little `css` as possible. It's also on [GitHub](https://github.com/tachyons-css/tachyons). It's a `css`-only framework (no JavaScript), and it's distributed under the MIT open-source license. Very cool.
- [MarkSheet](http://marksheet.io/) is a free HTML and CSS tutorial by the same person who wrote "Web Design in 4 Minutes."
- [Bulma](http://bulma.io/) is a CSS framework based on Flexbox and created by the same person who wrote "Web Design in 4 Minutes."
- [The Web's Grain](http://www.frankchimero.com/writing/the-webs-grain/), a view on designing for the web.
- [What Screen's Want](http://www.frankchimero.com/writing/what-screens-want/), some thoughts on digital canvases.
- [Typeplate](http://typeplate.com/) is a typographic starter kit. It contains a stripped-down Sass library that defines proper markup with extensible styling for common typographic patterns.

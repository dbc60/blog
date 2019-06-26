---
layout: post
title: CSS and Sass
categories: notes
tags: [css, compass, sass]
excerpt: I can't memorize 30 separate CSS selectors, unless they're organized.
---

## Contents
{:.no_toc}

- TOC
{:toc}

## Give Your Project Some Structure
There are several ways to organize your Sass files. A good structure will make small projects easy to manage, and continue to work as they grow. [Vinay Raghu](http://www.sitepoint.com/look-different-sass-architectures/) reviewed some of the techniques in use to provide some sort of logic to the structure of the files and folders in use as of August 2014. I looked at one from Dale Sande, who [went over it in depth](https://www.youtube.com/watch?v=EmNcD3b3ZtI) at [SASS Conf 2013](https://www.youtube.com/watch?v=z-TEqa0MPlY&list=PLXrTmSPkhnXsd_MGL5Y__7IoRemarkRVi). He also [wrote about](http://gist.io/4436524) what he covered in his talk. He also has a [series of guidelines](http://coderecipez.roughdraft.io/) for developers who are new to Sass. Dale looks to be an intense resource of knowledge for writing and structuring Sass files.

### Anant Dabhi's Directory Layout
[Anant Dabhi](http://stackoverflow.com/users/1460657/anant-dabhi) provided a [thoughtful answer](http://stackoverflow.com/questions/24199004/best-practice-to-organize-javascript-library-css-folder-structure) to the question of creating an easy to manage directory structure for an HTML5 application. He places an index file (`index.html`) at the root of the project directory, and includes two folders; **resources** and **vendords**. The HTML, CSS and JavaScript files that comprise your application will go into these folders. The enables you to group your files into a set of application-specific resources and general-purpose resources. Here is the directory tree he recommends:

```
project/
|-- resources/
|   |-- css/
|   |   |-- blue-theme/     (images and other files specific to this theme, which overrides the default)
|   |   |   \-- background.png
|   |   |
|   |   |-- images/         (images used by the default stylesheet)
|   |   |   \-- background.png
|   |   |
|   |   |-- blue-theme.css  (this theme is either an alternative to the default, or overrides it)
|   |   |-- default.css     (the default theme)
|   |   \-- index.css       (page-specific styling, used only by index.html)
|   |
|   |-- data/
|   |   |-- some-data.json
|   |   |-- more-data.xml
|   |   |-- table-data.csv
|   |   \-- extra-data.txt
|   |
|   |-- images/ (images used by index.html)
|   |   |-- products/
|   |   |   |-- computer.jpg
|   |   |   |-- cellphone.png
|   |   |   \-- printer.jpg
|   |   |
|   |   |-- my-company-logo-small.jpg
|   |   \-- my-company-log-large.png
|   |
|   \-- js/
|       |-- index.js            (page-specific code, used only by index.html)
|       |-- my-contact-info.js  (page-specific code, used only by my-contact-info.html)
|
|-- vendors/
|   |-- jquery/
|   |   |-- images/
|   |   |   |-- ajax-loader.gif
|   |   |   \-- icons-18-white.png
|   |   |
|   |   |-- jquery.min.js
|   |   |-- jquery.mobile-1.1.0.min.css
|   |   \-- jquery.mobile-1.1.0.min.js
|   |
|   |-- some-css-library/
|   \-- some-plugin.jquery/
|
|-- about.html
|-- index.html
|-- my-contact-info.html
|-- my-products.html
```

### Sass Directory Layout
[The Sass Way](http://thesassway.com) recommends the following [directory structure](http://thesassway.com/beginner/how-to-structure-a-sass-project) for Sass projects.

```
stylesheets/
|
|-- modules/              # Common modules
|   |-- _all.scss         # Include to get all modules
|   |-- _utility.scss     # Module name
|   |-- _colors.scss      # Etc...
|   ...
|
|-- partials/             # Partials
|   |-- _base.sass        # imports for all mixins + global project variables
|   |-- _buttons.scss     # buttons
|   |-- _figures.scss     # figures
|   |-- _grids.scss       # grids
|   |-- _typography.scss  # typography
|   |-- _reset.scss       # reset
|   ...
|
|-- vendor/               # CSS or Sass from other projects
|   |-- _colorpicker.scss
|   |-- _jquery.ui.core.scss
|   ...
|
\-- main.scss            # primary Sass file
```

- The **modules** directory is reserved for Sass code that doesn't cause Sass to uotput CSS. These are things like mixin declarations, functions and variables.
- The **partials* directory holds CSS where each file or directory is for a category or component. The stylesheets can be divided into, for example, header, content, sidebar, and footer components. Others like to segregate their CSS into more fine-grain categories like button, typography, textboxes, selectboxes, and others.
- The **vendor** directory is for third-party CSS. Place your pre-packaged components here.

See [How to Structure a Sass Project](http://thesassway.com/beginner/how-to-structure-a-sass-project) for descriptions of these directories and their intended purpose.

### One Rule of Thumb for a CSS Directory Layout
File names like `helpers`, `styles`, `functions` might not be as useful as creating a directory layout that makes the contents and purpose of the files more apparent. Something like the following enables the designer to navigate the stylesheets more easily:

```
stylesheets/
|-- settings/
|   \-- colors/     # place stylesheets that define variables for colors and themes here
|
|-- generic/        # boilerplate
|   \-- normalize.scss
|
|-- objects/        # place files and directories specific to the kinds of elements being styled
    |-- paragraph.scss
    |-- list.scss
    \-- figure.scss
```

The above should probably be combined with the notions of `vendor` and `resources` directories. In the case of [Sass](#sass-directory-layout), we probably want to have separate directories for `modules` and `partials` where the files are named for the kinds of things being styled.

### Dale Sande's Directory Layout
Here is a directory structure that works for Dale Sande:

```
_sass/
|-- buttons/
|   \-- color/
|
|-- forms/
|-- layouts/
|-- modules/
|-- typography/
|-- ui_patterns/
|-- vendor/
|-- _buttons.scss
|-- _config.scss
|-- _forms.scss
|-- _reset.scss
|-- _typography.scss
|-- style.scss
```

### A Directory Layout for Multiple Themes
In [How to use Sass to Build One Project with Multiple Themes](http://webdesign.tutsplus.com/tutorials/how-to-use-sass-to-build-one-project-with-multiple-themes--cms-22104), Tim Hartman suggested the following directory layout:

```
_scss/
|-- _base/
|   \--_config.scss
|
|-- _layouts/
|   |-- _l-grid.scss
|   \-- _l-default.scss
|
|-- _modules/
|   |-- _m-accordions.scss
|   \-- _m-teasers.scss
|
|-- _themes/
|   |-- _light-theme/
|       \-- light.scss
|
\-- application.scss
```

#### Base Configuration for Multiple Themes
Here's some sample content for `_scss/_base/_config.scss`. The key here is to use the `!default` flag after the variable declarations. Doing this allows you to overwrite them within the theme `.scss` files. The `!default` flag says "use this value if it isn't defined elsewhere".

```scss
@charset "UTF-8";
 
// Colors
$black: #000;
$white: #fff;
$red: #e2061c;
$gray-light: #c9c8c8;
$gray: #838282;
$gray-dark: #333333;
$blue: #253652;
 
// Corp-Colors
$corp-color: $blue !default;
$corp-color-dark: darken($corp-color, 15%) !default;
$corp-color-second: $red !default;
$corp-color-second-dark: darken($corp-color-second, 15%) !default;
 
// Font
$base-font-size: 1.8 !default;
$base-font-family: Helvetica, Arial, Sans-Serif !default;
$base-font-color: $gray-dark !default;
 
// Border
$base-border-radius: 2px !default;
$rounded-border-radius: 50% !default;
$base-border-color: $gray !default;
```

#### Background Images
If you write URLs to images, try creating a variable that represents the path to the image. Do this in the configuration file and mark them as default. It will be easy to override them in specific themes.

```scss
// Images
$sprite:                '../images/base/sprite.png' !default;
$colorbox-background:   '../images/base/colorbox-background.png' !default;
```

#### Application.scss for Multiple Themes

```scss
@charset 'UTF-8';
 
// 1.Base
@import '_base/_config.scss';
 
// 2.Layouts
@import '_layouts/_l-grid',
        '_layouts/_l-default';
 
// 3.Modules
@import '_modules/_m-accordions',
        '_modules/_m-teasers';
```

#### One Theme Among Many
The following code could be used in `_sass/_themes/_light-theme/light.scss`. Note that it ties together the application with the variable definitions and styling.

```scss
@charset 'UTF-8';
 
// 1.Overwrite stuff
$corp-color: $gray;
$corp-color-darken: darken($corp-color, 10%);
$corp-color-second: $blue;
$corp-color-second-dark: darken($corp-color-second, 10%);
  
$base-font-size: 1.6;
$base-font-family: Droid Sans, Georgia, Arial;
  
$base-border-radius: 0px;
$base-border-color: $gray-light;
  
// Images
$sprite:              '../images/light/sprite.png';
$colorbox-background: '../images/light/colorbox-background.png';
  
$accordion-bgcolor: $gray-light;
 
// 2. Import basic theme
@import '../../application';
```

## Partials and Manifests
Keep subdirectories neat. Use partials and manifests. The `style.scss` file contains all of the imports. It might look like:

```scss
// The following sequence will load the necessary Stipe libraries
// --------------------------------------------------------------
@import "compass/css3";     // Include the Compass CSS3 mixins
@import "stipe/manifest";
##import "vendor/**/*";

// This is where you start building your own styles
// ------------------------------------------------
@import "typography";
@import "forms";
@import "buttons";
@import "design";
@import "ui_patters/**/*";  // manifest files
@import "modules/**/*";     // manifest files
@import "layouts/*";        // manifest files
```

## Manual vs GLOG-Imports
There is no right or wrong here. Here are two examples of a primary manifest in the `grid` directory. The first manually imports all of the necessary Sass files, while the other uses the asterisk to globally match all the files in the `grid/lib/` directory.

The only concern with GLOB-matching is the Sass files will be added in alphabetical order. If code in one file depends on a value in another that doesn't precede the first alphabetically, your Sass files won't compile.

There is one strong guideline for subdirectories: try not to nest them more than three levels deep. Beyond that management becomes difficult.

manual:

```
@import "grid/lib/the_grid";
@import "grid/lib/grid_placement";
@import "grid/lib/grid_margin";
@import "grid/lib/push_logic";
@import "grid/mixins";
@import "grid/extends";
```

glob:

```
@import "grid/lib/*";
@import "grid/mixins";
@import "grid/extends";
```

## Configuration Options
One set of configuration variables to rule them all! Use the `_config.scss` file to contain all of the configuration variables that the rest of your Sass files depend on. Here's an example:

```scss
/////// Typography Configuration ///////
// -------------------------------------
$font_size: 12;
//
$heading_1: 46;
$heading_2: 32;
$heading_3: 28;
$heading_4: 18;
$heading_5: 18;
$heading_6: 18;
//
$line: $font_size * 1.5;
//
$small_point_size: 10;
$large_point_size: 14;
//
$primary_font_family: #{"Helvetica Neue", Arial, sans-serif};
$secondary_font_family: #{"Helvetica Neue", Arial, sans-serif};
$heading_font_family: #{"Helvetica Neue", Arial, sans-serif};

$icon_font_alpha: #{'FontAwesome'};
$icon_font_bravo: #{'zocal'};;

/////// Default webfont directory ///////
// ---------------------------------------
$webfont_directory: "/fonts/";
```

Note: There should be no CSS in a configuration file. It should contain logic only.

## Element Partials
Your foundational UI should be all CSS - NO LOGIC!

```scss
button {
    font-size: em(16);

    @include background-image(linear-gradient(top, #1e57990 05,#2989d8 50%,#207cca 51%, #7db9e8 100%));

    .no-cssgradients & {
        background-color: #1e5799;
    }
    border: 1px solid $primary_button_border_color;
    border-radius: em(3);
    color: $white;
    padding: em(6) em(10);
    margin: 0;

    @media #{$mobile} {
        width: 100%;
    }
}
```

You've spent a lot of time building a framework from which you'll build a website. You've built all the logical pieces in a set of neat directories and configured them using `_config.scss`. For the partials, you actually build your website, so you don't use any logic (that is, calculations). It's all execution of your logical files.

## Your Custom Code
Here's the anatomy of one of your custom files:

- `_buttons.scss`: this is the manifest that imports files from the buttons directory.
- `buttons/`: the folder that contains Sass files related to buttons
- `_mixins.scss`: one of the functional files contained in the `buttons/` directory.
- `_extends.scss`: another functional file contained in the `buttons/` directory.

The root `_buttons.scss` file might look like this:

```scss
// Functional Part
// Custom button extends and mixins
// -------------------------------------------------------------
@import "buttons/mixins";
@import "buttons/extends";

// Presentational Part
// buttons
// -------------------------------------------------------------
/* toadstool buttons */
button, a.button {
    @include button($button-color);
}
```

## Modules and UI Patterns
This is more of a gray area as far as the definitions are concerned.

- Module: a functional piece of code that is going to exist in the website.
- UI Pattern: something a module will take advantage of.

Suppose we need a tab bar in the UI. That tab bar has a UI pattern associated with it. The pattern defines aspects of the tab bar, such as what the tabs look like, whether they have different states or not, borders, backgrounds, colors, etc.

The tab bar is not a module. You're never going to use it verbatim in the application. Instead, you're going to apply the aesthetic of the tab bar to a module. That module will have functionality associated with it, and that's what will actually be put in the application.

UI patterns are subject to your personal interpretation. In practice, small UI patterns begin to emerge. It is practical to try and encapsulate these smaller patterns for reuse, but don't lose sleep over them.

Another example is suppose you have "content bubbles". You could encapsulate a pattern that defines the color, border and shape (say rounded corners with a 3px radius). That pattern is then applied to instances (each of which could be in different states) of the content bubble in the UI. If a designer came along later and said change the background color of all the content bubbles from red to green, you could do it in one place.

### Module Directory Structure
Here's one way to organize the modules directory:

```
modules/
|-- registration/
|   |-- _extends.scss
|   |-- _functions.scss
|   |-- _mixins.scss
|   |-- _module_registration.scss    // primary module for the registration family (named by convention)
|   \-- _module_personalinfo.scss
|
\-- purchase/
    |-- _extends.scss
    |-- _functions.scss
    |-- _mixins.scss
    |-- _module_order-summary.scss
    \-- _module_purchase.scss    // this is the primary module for the purchase family (named by convention)
```

The files `_extends.scss`, `functions.scss` and `_mixins.scss` contain code that the developer abstracted away, and which he can apply to the various modules that fall under the family represented by the name of the directory that contains those files. For example, the `_module_registration.scss` and `_module_personalinfo.scss` files contain modules that are part of the registration family.

### Name-space by the Module Itself

```scss
%order-summary {
    .form-header {
        border-radius: em(5) em(5) 0 0;
        margin-bottom: 0;
    }
    .order-summary-container {
        @extend %Grid4ThreeSideBox;
    }
    .initial-assetListing {
        @media #{mobile} {
            display: none;
        }
    }
    .price {
        text-align: right;
    }
    .total {
        font-size: em($large_point_size);
    }
}
```

If this is written as a "placeholder selector", there is even more opportunity to reuse this (I don't know how - See [Dale Sande's presentation](https://www.youtube.com/watch?v=EmNcD3b3ZtI)). It's done by assembling the layout.

## Assembling the Layout
Here we try to bring the picture into focus (whatever that means). The modules should be designed to take up 100% of the width of whatever they will be fit into, and with as much vertical space as that particular chunk of content needs.

When we get to the layout, think of it as a bunch of holes into which various pieces of content are placed. We just want to be concerned with the question, "What is that grid? What is that box of holes that makes up the layout?"

The layout is more or less dictated by the informational architecture of what needs to go into each slot in order to get the most impact of your message to your users. In this way, when someone comes along and says we need a different piece of information in a particular location, you can grab a different module and place it in that slot!

Example: Checkout-Experience Module:

```scss
.checkout-experience {
    .customer-checkout {
        @extend %checkout;  // extending the checkout module
        @extend %grid_7;    // extending grid_7 for the grid system in use

        @media @{$tablet_portrait} {
            @include grid(10, $grid_context: 10);
        }
    }
    .order-summary {
        @extend %order-summary;
        @extend %grid_5;

        @media @{$tablet_portrait} {
            @include grid(10, $grid_context: 10);
        }

        @media @{$mobile} {
            @include grid(10, $grid_context: 4);
        }
    }
}
```

This level is probably the best level to start writing responsive code, thus the `@media` queries are included. This enables your layout to change in response to the device that is reading your website.

## Design Intent
An article by Nate Berkopec popped up on [Hacker News](http://news.ycombinator.com). It's about how the judicious use of WebFonts made the [RubyGems site much faster](https://www.nateberkopec.com/2015/11/30/how-changing-webfonts-made-rubygems-10x-faster.html.). Berkopec used the intent of the site's design to determine where WebFonts needed to be used, and other system fonts could be substituted to make the site load faster. One of the conclusions reached was to use Google Fonts, in no small part due to the way these fonts are cached.

Here's the CSS for including a thin, 100 weight version of the very popular Roboto font.

```css
@font-face {
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 100;
  src: local('Roboto Thin'), local('Roboto-Thin'), url(https://fonts.gstatic.com/s/roboto/v15/2tsd397wLxj96qwHyNIkxHYhjbSpvc47ee6xR_80Hnw.woff2) format('woff2');
}
```

What's the intent of the design for my site and how can I use that to guide font selection and styling? I'm not sure, but one thing I can do is set a [vertical rhythm](https://24ways.org/2006/compose-to-a-vertical-rhythm).


## CSS Selectors
I found a set of 30 CSS selectors in the article "[The 30 CSS Selectors You Must Memorize](http://code.tutsplus.com/tutorials/the-30-css-selectors-you-must-memorize--net-16048)." I can't memorize 30 separate items easily, but these selectors can be classified into coherent groups. First, here's the list of all 30 selectors from the article:

1. `*`: `universal`
2. `#X`: `id`
3. `.X`: `class`
4. `X Y`: `descendant`
5. `X`: `type`
6. `X:visited and X:link`: pseudo-classes
7. `X + Y`: `adjacent`
8. `X > Y`: direct-child-of
9. `X ~ Y`: `sibling combinator`
10. `X[title]`: `attributes`
11. `X[href="foo"]`: `attributes`
12. `a[href*="example"]`: `attributes`
13. `a[href^="http"]`: `attributes`
14. `a[href$=".jpg"]`: `attributes`
15. `X[data-*="foo"]`: `custom attributes`
16. `X[foo~="bar"]`: `attributes`
17. `X:checked`: `pseudo-class`
18. `X:after`: `pseudo-class`
19. `X:hover`: `pseudo-class` (for a user action)
20. `X:not(selector)`: `pseudo-class` (negation)
21. `X::pseudoElement`: `pseudo-element`
22. `X:nth-child(n)`: `pseudo-class`
23. `X:nth-last-child(n)`: `pseudo-class`
24. `X:nth-of-type(n)`: `pseudo-class`
25. `X:nth-last-of-type(n)`: `pseudo-class`
26. `X:first-child`: `pseudo-class`
27. `X:last-child`: `pseudo-class`
28. `X:only-child`: `pseudo-class`
29. `X:only-of-type`: `pseudo-class`
30. `X:first-of-type`: `pseudo-class`

The Mozilla Developer's Network (MDN)

These 30 selectors fall into five groups:

- [Basic Selectors](#the-basic-css-selectors): items 1, 2, 3 and 5.
- [Cascading Selectors](#the-cascading-selectors): items 4, 7, 8 and 9.
- [Pseudo-class Selectors](#pseudo-class-selectors): items 6 and 17-20 and 22-30.
- [Attribute Selectors](#attribute-selectors): items 10-16.
- The [Pseudo-element Selector](#the-pseudo-element-selector): item 22.

There is also a selector that the article failed to mention: the grouping selector. It is one of the basic selectors, enabling you to style several selectors the same way. The syntax is `X, Y`.

I don't know yet, if there are any other selectors. I have a lot to learn, but this is certainly a good start.

### The Basic CSS Selectors
The basic selectors are:

- Universal: `*`. The asterisk selects all HTML elements.
- ID: `#X`, where `X` stands for the value of the `id` attribute of a single HTML element.
- Class: `.X`, where `X` stands for the value of the `class` attribute of the HTML elements.
- Type: `X`, where `X` is a kind of HTML element, like `p` or `h1`.
- Group: `X, Y`, where `X` and `Y` are any kind of selectors.

### The Cascading Selectors
You can set the typeface for every element on every page of the website like this:

```css
body {
    font-family: Helvetica;
}
```

Every element is a child of the `body`, so those elements will inherit the font family unless that property is overridden with a more specific rule. For example, you might want to use Georgia in the sidebar. To reset the font-family rule for the sidebar (assuming you use the `aside` element for the content in the sidebar), you can write:

```css
body aside {
    font-family: Georgia;
}
```

The article [CSS: Taking Control of the Cascade](https://signalvnoise.com/posts/3003-css-taking-control-of-the-cascade) uses this example as a warning about how complicated CSS can become. Each time we reset a style using a more specific rule, overriding that style on a subsequent child element requires an even more specific selector. The selectors become increasingly long and complicated.

To deal with this complexity, the author suggests some techniques that fall into three categories: compiled CSS, structured mark-up and what he calls "a neglected CSS selector."

Compiled CSS refers to using a CSS pre-processor or extension language, like [Sass](http:/sass-lang.com) or [Less](http://lesscss.org).

### Grouping Selectors
There are a variety of selectors, the most basic of which are HTML elements. If you want to style all paragraphs, specify the `p` element and place the CSS style properties between a pair of braces:

```css
p {
    type-family: Helvetica, serif;
    color: black;
}
```

If you want to style several elements the same way, then combine the elements (for that matter, any kinds of selectors) in a comma-separated list. The following will color all the headings blue:

```css
h1, h2, h3, h4, h5, h6 {
    color: blue;
}
```

### CSS Selectors for MathML
So good to have a reference: [CSS Token Elements for MathML](https://www.w3.org/TR/mathml-for-css/#d2e2482) from the [MathML for CSS Profile](https://www.w3.org/TR/mathml-for-css/).

There are many more elements than the few listed below. However, it was the `mi` and `mo` elements that were colliding with the color definitions in the SCSS definitions for the pygments syntax highlighting files (`pygments/_default.scss`, `pygments/_manni.scss`, `pygments/_monokai.scss` and `pygments/_paraiso-dark.scss`). I don't think I should use these files for syntax highlighting anymore.

- Identifier `<mi>`: an `mi` element represents a mathematical identifier; its rendering consists of the text context displayed in a typeface corresponding to the `mathinvariant` attribute.
- Number `<mn>`: an `mn` element represents a "numeric literal" or other data that should be rendered as a numeric literal. Generally speaking, a numeric literal is a sequence of digits, perhaps including a decimal point, representing an unsigned integer or real number.
- Operator `<mo>`: an `mo` element represents an operator or anything that should be rendered as an operator.
- Text `<mtext>`: an `mtext` element is intended to denote commentary text.
- Space `<mspace>`: an `mspace` element represents a blank space of any desired size, as set by its attributes.
- String Literal `<ms>`: The `ms` element is used to represent "string literals" in expressions meant to be interpreted by computer algebra systems or other systems containing "programming languages." Be default, string literals are displayed surrounded by double quotes.

## Pseudo-Element Selectors
Reference: https://www.w3.org/community/webed/wiki/Advanced_CSS_selectors

CSS3 pseudo-element double colon syntax. Please note that the new CSS3 way of writing pseudo-elements is to use a double colon. For example `a::after { ... }`, to set them apart from pseudo-classes. You may see this sometimes in CSS. CSS3 however also still allows for single colon pseudo-elements, for the sake of backwards compatibility, and we would advise that you stick with this syntax for the time being.

## Pseudo-Class Selectors
Reference: https://developer.mozilla.org/en-US/docs/Web/CSS/:root

The `:root` CSS pseudo-class matches the root element of a tree representing the document. Applied to HTML, `:root` represents the `<html>` element and is identical to the selector `html`, except that its [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity) is higher.

## Custom CSS Mixins
Per [Styling local DOM](https://www.polymer-project.org/1.0/docs/devguide/styling.html), it's possible to define a set of CSS properties as a single custom property and then allow all properties in the set to be applied to a specific CSS rule in an element's local DOM. The extension enables this with a mixin capability that is analogous to `var`, but which allows an entire set of properties to be mixed in. This extension adheres to the [CSS @apply rule](http://tabatkins.github.io/specs/css-apply-rule/) proposal. For example:

```css
:root {
  --grid {
    display: flex;
    flex-wrap: wrap;
  }
  --cell {
    box-sizing: border-box;
    flex-shrink: 0;
  }
}

.Grid            { @apply --grid; }
.Cell            { @apply --cell; }
```

## CSS Flexible Boxes (flexbox)
I started looking at grid systems, and found a very simple one called Grd. It has no media queries to respond to various screen sizes, but that would be easy to add. Perhaps all that's really needed is to learn about the CSS flexbox API. Here are some references:

- [Using CSS flexible boxes](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Using_CSS_flexible_boxes)
- [A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/).
- [Dive into Flexbox](https://bocoup.com/weblog/dive-into-flexbox).
- [Putting Flexbox into Practice](http://zomigi.com/blog/flexbox-presentation/).
- [Solved by Flexbox](http://philipwalton.github.io/solved-by-flexbox/) has lots of good example uses. All of the code samples on this site show how to solve a particular design problem with Flexbox. They show just the code that's needed to make the demos work in a spec-compliant browser.
- [CSS Flexbox Please!](http://demo.agektmr.com/flexbox/).
- [Flexy Boxes](http://the-echoplex.net/flexyboxes/).
- [Flexplorer](http://bennettfeely.com/flexplorer/).
- [SCSS Flex Grid](https://github.com/matthewsimo/scss-flex-grid) on GitHub and the related [Flex Grid SCSS](http://matthewsimo.github.io/scss-flex-grid/) blog post.
- [Flexbox Grid Sass](http://hugeinc.github.io/flexboxgrid-sass/) and the [code on Github](https://github.com/hugeinc/flexboxgrid-sass).
- [Flexbox Grid](http://flexboxgrid.com/), a grid system based on the flex display property. It's also [on Github](https://github.com/kristoferjoseph/flexboxgrid).


## References
- [Styling local DOM](https://www.polymer-project.org/1.0/docs/devguide/styling.html)
- [CSS @apply rule](http://tabatkins.github.io/specs/css-apply-rule/)
- [Name your Sass Variables Modularly](http://webdesign.tutsplus.com/articles/quick-tip-name-your-sass-variables-modularly--webdesign-13364)
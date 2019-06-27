---
title: "Enduring Css"
date: 2019-06-03T05:44:18-04:00
draft: true
categories: [software]
tags: [design, web]
---

`Enduring CSS`_ is an approach to organizing and developing Cascading Style
Sheets (CSS) for enduring and rapidly changing web applications. Long-term
maintainability is the main concern of this approach.
<!--more-->

As such, it doesn't
prescribe the Don't Repeat Yourself (DRY) practice, which has a goal of
minimizing the code base so each variable, propery, function, and other
objects are defined just once. Instead, Enduring CSS values independent
components where some components may look very similar to others, but their
code bases can be manipulated independently with impunity. That is, you can be
sure that modifying one component will have no unintended side effects on
another.

#############
Naming Things
#############

The author's naming convention from his `blog post <enduring css blog post_>`_ is::

    [namespace]-[CompnentPart]_[Variant]-[optional-adjuster]

A real selector might look like ``sc-Wrapper`` or ``sc-InnerItem_Gold``. It is
based on `Nicolas Gallagher's naming convention <https://github.com/suitcss/suit/blob/master/doc/naming-conventions.md>`_, which looks like:

.. code-block:: html

    <div class="namespace-ComponentName--modifierName-descendantName"></div>

He replaced the double dash (`--`) from BEM with an underscore (``_``) for two reasons. First, the double dash sometimes messed up syntax highlighting in some editors. Second, the HTML5 Validator complained about the double dashes preventing the HTML from being mapped to XML. The latter is not really important, but it's irritating when the validator says something is wrong.

So the class above in CSS would look like:

.. code-block:: css

    .namespace-ComponentName_ModifierName-variant-label {
    }

I'm not sure how ``variant-label`` maps to ``descendantName``, but I guess it
works for him.

In Frain's `book <enduring css_>`_, an ECSS selector is:

* namespace : This is a required part of every selector. The micro-namespace
  should be all lowercase/train-case. It is typically an abbreviation to
  denote context or originating logic.
* ModuleOrComponent : This is a upper camel case/pascal case. It should always
  be preceded by a hyphen character (``-``).
* ChildNode : This is an optional section of the selector. It should be upper
  camel case/pascal case and preceded by an underscore (``_``).
* variant : This is a further optional section of the selector. It should be
  written all lowercase/train-case.

*********
Namespace
*********

The namespace is used to prevent collisions and provide some soft isolation
for easier maintenance of rules.

*******************
Module or Component
*******************

This is the visual module or piece of logic that created the selector. It
should be written in upper camel case. The name can be more effective if it
directly references the name of the file that creates it. For example, a file
called "CallOuts.js" could have a selector such as ``sw-CallOuts`` (where
``sw-`` is a micro namespace denoting the module/component is intended to be
used "Site Wide"). This removes any ambiguity for future developers as to the
origin point of this element.

**********
Child Node
**********

If something UpperCamelCase is preceded by an underscore (``_``) it is a child
node of a module or component. For example:

.. code-block:: css

    .sc-Item_Header {}

Here, ``_Header`` is indicating that this node is the "Header" child node of
the "Item" module or component that belongs to the 'sc' namespace. If it is a
component, then that namespace could indicate the parent module.

*******
Variant
*******

If something is all lowercase/train-case and not the first part of a class
name it is a variant flag. The variant flag is reserved for eventualities
where many variants of a selector need to be referenced.

Suppose we have a module that needs to display a different background image
depending upon what category number has been assigned to it. We might use the
variant indicator like this:

.. code-block:: css

    .sc-Item_Header-bg1 {} /* Image for category 1 */
    .sc-Item_Header-bg2 {} /* Image for category 2 */
    .sc-Item_Header-bg3 {} /* Image for category 3 */

Here the ``-bg3`` part of the selector indicates that this ``.sc-Item_Header``
is the category 3 version (and can therefore have an appropriate style
assigned).

An example of how something like this would be used in practice is this markup:

.. code-block:: html

    <div class="sc-Item_Header sc-Item_Header-bg1">
        <!-- Stuff -->
    </div>

Here we would set the universal styles for the element with ``sc-Item_Header``
and then the styles specific to the variant with ``sc-Item_Header-bg1``.

##############
BEM Comparison
##############

For comparison, the `BEM`_ naming convention uses all lowercase letters, and
words within names are separated by dashes (rather than camelCase, PascalCase,
snake_case). Separating words with a hyphen is called train-case or kebab-case.

There is no separate namespace in BEM. The block name serves as the namespace.
Elements are separated from the block name by two underscores (``__``), the
modifier is separated from the block or element name by a single underscore,
and finally, the modifier value is separated from the modifier name by a
single underscore (``_``). Boolean modifiers have only a name. The value is
assumed/intrinsic.

An example of a BEM style selector would be a menu (block name) item (element
name) in the style of a radio button (``type_radio`` is the modifier name and
value). The following example also uses a visibility modified selector for the
menu item.

.. code-block:: html

    <span class="menu__item menu__item_visible menu__item_type_radio"></span>

.. code-block:: css

    .menu__item_visible {}
    .menu__item_type_radio { color: blue; }

Frain emphasizes that your naming convention becomes so embedded in your
projects, that you need to choose one that works for you. It affects not only
the readability and intelligibility of the selectors, but also the HTML
classes that will litter your templates and markup.

Develop and enforce a naming convention. There is no "right" naming convention. The current de factor standard is the `classic BEM method <https://en.bem.info/methodology/key-concepts/>`_. Whatever naming convention you consider, ask:

* Does it match the way you work?
* Does it seem immediately clear to you?

Name with intent. Classes like ``.WarnUser`` and ``.sc-CurrencyDropDown`` are
descriptive, it's easy to discern the intent, and therefore it is easy to
figure out that they can be visually different in different contexts.

#################################
Block Element Modifier Discussion
#################################

Ben Frain, the author of `Enduring CSS`_ says that BEM was the most useful of
the methodologies he tried. Specifically, he likes these aspects of BEM:

* All elements get the same specificity; a class is added to all the elements.
* There is no use of type selectors so HTML structure isn't tightly coupled to
  the styles.
* It's easy to reason about what the parent of an element is, whether viewing
  the Document Object Model (DOM) tree in the browser developer tools or the
  CSS in a code editor.

.. sidebar:: Block Element Modifier

    The key points of `BEM`_ is that the methodology works around the notion that key areas of a page can be defined as 'Blocks'. In turn, those key areas are made up of Elements. We can then represent the relationship between the Block and its Elements in the way we name things.

    BEM also has the notion of 'modifiers'. A modifier is something that gets added to the Block to modify its appearance.


The BEM documents dictate the use of a single underscore character to identify
a Modifier for a Block. This modifier class must always be used alongside the
block name. For example, you must do this:

.. code-block:: html

    <div class="media media_dark">

And not this:

.. code-block:: html

    <div class="media_dark">

Frain said:

    I see the value in using modifiers in this manner but it proved
    problematic for me. Often the things I was styling needed to behave
    differently in a more traditional manner. Perhaps visuals needed to
    display differently depending upon the context they were being used, or if
    another class was being added above it in the DOM. Or due to certain media
    query conditions, or indeed any combination of those scenarios. I needed a
    way to author styles that was pragmatic enough to deal with the non-ideal
    situations that occurred. Some way to keep some sanity in the authoring
    style sheets no matter what was thrown at them.

In other words, BEM worked great for specific blocks, but left something to be
desired when a block's styling changed depending on the styling of parent or
sibling blocks.

He also said:

    I couldn't find a clear way of understanding how that eventuality should
    be handled. Or how I could contain those kinds of overrides in the
    authoring style sheets. I wanted to define items and encapsulate all the
    eventualities that may occur on a particular item.

Problems with BEM:

* encapsulation: need to encapsulate all eventualities that may occur on an
  item.
* syntax: confusing to reason over when glancing at classes, because modifiers
  and elements are written very similarly.
* context: he wanted a way to communicate and facilitate module contexts. In
  other words, he wanted to be able to make the specific usagee and style of a
  logical item clear for each context in which it is used.

###########
Terminology
###########

**module:**
    The widest, visually identifiable area of functionality and the code used
    to create it. For example, the header of a website.

**component:**
    A nested piece of functionality included within a module. For example,
    drop down menus or search boxes could be components of a header module.

**child node:**
    A part that makes up a component. A child node is typically a node in the
    DOM.

*********
Why ECSS?
*********

The primary goal with ECSS is to isolate styles as opposed to abstracting
them. The author explains:

    Ordinarily, it makes sense to create CSS classes that are abstractions of
    common functionality. The benefit being that they can then be re-used and
    re-applied on many varied elements. That's sound enough in principle. The
    problem is, on larger and more complicated user interfaces, it becomes
    impossible to make even minor tweaks and amendments to those abstractions
    without inadvertently effecting things you didn't intend to. A guiding
    principle with ECSS therefore was to isolate styles to the intended
    target. Depending upon your goals, even at the cost of repetition,
    isolation can buy you greater advantages; allowing for predictable styling
    and simple decoupling of styles.

I don't have enough experience with CSS, so without understanding the pitfalls,
I wonder if it would be a good idea to apply the DRY principle to a base layer,
and build a module layer on top of that. My first guess is that the base layer
becomes unused, more of a reference, as the module layer copies base
components as is or as variants for individual modules. Also, Frain states
that in his experience, he could code out designs far faster when starting from
scratch than attempting to build them from any number of vague abstractions.

A secondary goal of ECSS is to negate issues surrounding specificity. To this
ends, it adopts the widely used approach of insisting all selectors use a
single (or as close to that ideal as possible) class-based selector.

Structural HTML elements (with the exception of pseudo-elements) are NEVER
referenced in the style sheets as type selectors. In addition ID selectors are
completely avoided in ECSS. Not because ID selectors are bad per se, but
because we need a level playing field of selector strength.

###############
Organizing Code
###############

The basic rules for naming and organizing components is FUN:

* Flat hierarchy of selectors
* Utility styles
* Name-spaced components

***************************
Flat Hierarchy of Selectors
***************************

The benefits of a flat hierarchy of selectors is `well justified <shoot to kill css selector intent_>`_. Three important practices to apply to your CSS are:

1. Use only classes for selectors except in specific circumstances.
2. Never nest selectors unless essential.
3. Always avoid using IDs as styling hooks.

**************
Utility Styles
**************

Utility styles are single responsibility styles. They should have no reliance
on other selectors or specific structures. For example, ``w100`` would set
``width: 100%;``, and ``Tbl`` would be ``display: table; table-layout: fixed;``

.. note::

    Some people prefix their utility styles with a `u`, for example `u-100`.
    However, name them to your own convention. For me, if it is lower case
    with with no hyphens either side, it’s a utility style.

The only rigid rule with the utility styles is that once made and used, they
cannot, ever, be amended or removed. Make as many utility styles as you need
but ensure they can be used for as long as you can possibly imagine as they
will sit in the CSS of the project for EVER.

**********************
Name-spaced Components
**********************

Name-spacing the CSS of each visual component can be used to create some form
of isolation. By preventing name collisions with other components, chunks of
CSS can be more easily moved one environment to another (from prototype to
production for example).

One scheme is a simple 2–3 letter namespace for each component. Building a
shopping cart? Try .sc- as your namespace prefix. Building the next version of
that same shopping cart? That’ll be .sc2- then. It’s just enough to isolate
your component styles and allow the styles to be more self documenting. For
example, a wrapper for the shopping cart could be something like .sc-Wrapper.
Is there a remove item button? Something like .sc-RemoveItem would be suitable.

***************************
Module Organization Example
***************************

Suppose we have a module. Its job is to load the sidebar area of our site. The
directory structure might initially look like this::

    SidebarModule/ => everything SidebarModule related lives in here
      /assets => any assets (images etc) for the module
      /css => all CSS files
      /min => minified CSS/JS files
      /components => all component logic for the module in here
      css-namespaces.json => a file to define all namespaces
      SidebarModule.js => logic for the module
      config.json => config for the module

In terms of the example markup structure this Module should produce, we would
expect something like this initially:

.. code-block:: html

    <div class="sb-SidebarModule">

    </div>

The CSS that styles this initial element should live inside the css folder
like this::

    SidebarModule/
      /assets
      /css
        /components
        SidebarModule.css
      /min
      /components
      css-namespaces.json
      SidebarModule.js
      config.json

Now, suppose we have a component inside the SidebarModule that creates a
header for the SidebarModule. We might name the component with a file called
``Header.js`` and store it inside the ``components`` sub-folder of our
SidebarModule like this::

    SidebarModule/
      /assets
      /css
        /components
        SidebarModule.css
      /min
      /components
        Header.js
      css-namespaces.json
      SidebarConfig.js
      SidebarModule.js
      config.json

With that in place, the Header.js might render markup like this::

    <div class="sb-SidebarModule">
        <div class="sb-Header">
            <div class="sb-Header_Logo"></div>
        </div>
    </div>

Note how the Header component, due to being within the context of the
SidebarModule carries the ``sb-`` micro-namespace to designate its parentage.
The nodes created by this new component are named according to the logic that
creates them.

The general conventions to follow:

Components should carry the micro-namespace of the originating logic. If you
are creating a component that sits within a module, it should carry a/the
namespace of the originating module (possible namespaces for a module are
defined in ``css-namespaces.json``).

HTML classes/CSS selectors should be named according to the file name/
components that generated them. For example, if we created another component
inside our module called 'HeaderLink.js' which renders its markup inside a
child of the ``Header.js`` component, then the markup it generates and the
applicable CSS selectors should match this file name.

For example::

    <div class="sb-SidebarModule">
        <div class="sb-HeaderPod">
            <div class="sb-HeaderPod_Logo"></div>
        </div>
        <div class="sb-HeaderPod_Nav">
            <div class="sb-HeaderLink">Node Value</div>
            <div class="sb-HeaderLink">Node Value</div>
            <div class="sb-HeaderLink">Node Value</div>
            <div class="sb-HeaderLink">Node Value</div>
        </div>
    </div>

In terms of the folder structure, it would now look like this::

    SidebarModule/
      /assets
      /css
        /components
          Header.css
          HeaderLink.css
        SidebarModule.css
      /min
      /components
        Header.js
        HeaderLink.js
      css-namespaces.json
      SidebarConfig.js
      SidebarModule.js
      tsconfig.json

Notice how there is a 1:1 correlation between component logic, *the .js file, and the associated styles, the.css files* – both sit within a ``components`` sub-folder. Although both logic and styles don't share the same immediate parent folder, they both live within the same module folder, making removal of the entire module simple if needed.

################
Other Guidelines
################

Don't specify vendor prefixes in the authoring style sheets. The level of
browser support you require will change over time, resulting in redundant code
in your authoring style sheets. The prefixing of CSS properties can be handled
in a few lines with an authoring tool, and will be more accurate than you. It
won't take long to set up such a tool, so it is well worth the effort.

Avoid library mixins. Author wherever possible in W3C compliant CSS code. This
makes the authoring styles more portable if you decide to switch pre-processor
or copy code to a new project.

Don't put markup samples in CSS comments. While comments are important,
examples are likely to become obsolete and confusing. Instead, the template
stub that sits along side the style sheet should provide all the markup. As
this template is necessary for the application, it will always be up-to-date.

Keep CSS, Sass, SCSS, etc. simple. Mixins and logical loops are sometimes
preferable and advantageous, but don't over use them. For example, creating a
number of utility table width styles could be achieved liek this in Sass and
typifies the limit of what the author deems sensible in terms of complexity;

.. code-block:: css

    /* ======================================================================
       Table modifiers
       ===================================================================== */
    $widths: 5 10 20 30 40 50 60 70 80 90 100;
    %Tbl-base {
        display: table;
        float: left;
        vertical-align: middle;
    }
    @each $width in $widths {
        .tbl#{$width} {
            @extend %Tbl-base;
            width: $width * 1%;
        }
    }

As a counter example, a mixin for creating buttons that requires three or more
arguments to be passed just to set border styles, background colour and text
size is probably a needless over complication.

Be wary of ``@extent``. This final one is very Sass centric. Don’t extend
anything other than a placeholder selector (e.g. ``%Placeholder``) and don’t
place any nested styles within the place holder. It seldom creates the CSS you
imagine.

Finally, review your production CSS files. From time to time, actually open
the CSS file that is getting compiled (rather than merely the authoring style
sheets). Run through it manually, lint it with your own version of CSS Lint
(to catch what you actually care about). There are almost always unintended
chunks of code. Failure to check the final product you are producing is a sure
fire way to create sub-standard CSS files.

***********
Other Terms
***********

Frain uses some terms with which I'm not familiar. The first is "*authoring
style sheet*". I found a definition in `Implementing ATAG 2,0 <https://www.w3.org/TR/IMPLEMENTING-ATAG20/>`_, a guide to understanding and
implementing Authoring Tool Accessibility Guidelines 2.0:

**authoring style sheet:**
    This style sheet is only used to control the rendering of the web content
    in the author's editing-view. The style sheet does not make changes to the
    content markup being edited and is not published to end users.

Also, in `Chapter 9 <https://ecss.io/chapter9.html>`_ Frain says

    A build system of some sort is required to compile the authoring style
    sheets (with their variables, mixins and the like) into plain CSS. There
    are many tools available to perform this task e.g Grunt, Gulp and Brocolli
    to name just a few....

So he is probably refering to documents written in a CSS preprocessor language,
like Less or Sass, which are compiled to CSS.

**********
References
**********

* `Block Element Modifier <bem_>`_
* `Structured Authoring`_

.. _shoot to kill css selector intent: https://csswizardry.com/2012/07/shoot-to-kill-css-selector-intent/
.. _enduring css: https://ecss.io/
.. _enduring css blog post: https://benfrain.com/enduring-css-writing-style-sheets-rapidly-changing-long-lived-projects/
.. _bem: https://en.bem.info/
.. _structured authoring: https://everypageispageone.com/2013/12/05/changing-the-what-in-wysiwyg/

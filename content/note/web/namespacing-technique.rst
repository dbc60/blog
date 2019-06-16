---
title: "Namespacing Technique"
date: 2019-06-04T05:50:26-04:00
draft: true
categories: [software]
tags: [design, web]
cssDetail: drop-caps-cheshire
---

In `Battling BEM CSS`_, David Berner recommends using namespaces. He says
namespaces have made his code more readable. He borrows from Harry Robert's
`namespacing technique <ui code with namespaces_>`_ to form his own namespace
convention.

* Component: ``c-``. Examples: ``c-card``, ``c-checklist``. Form the backbone
  of an application and contain all of the cosmetics for a standalone
  component.
* Layout Module: ``l-``. Examples: ``l-grid``, ``l-container``. These modules
  have no cosmetics and are purely used to position ``c-`` components and
  structure an application’s layout.
* Helpers: ``h-``. Examples: ``h-show``, ``h-hide``. These utility classes
  have a single function, often using ``!important`` to boost their
  specificity. (Commonly used for positioning or visibility.)
* States: ``is-``, ``has-``. Examples: ``is-visible``, ``has-loaded``.
  Indicate different states that a ``c-`` component can have. Sometimes you
  want JavaScript to manage states. In that case, see JavaScript Hooks, next.
* JavaScript Hooks: ``js-``. Example: ``js-tab-switcher``. These indicate that
  JavaScript behavior is attached to a component. No styles should be
  associated with them; they are purely used to enable easier manipulation
  with script.

***************
Naming Wrappers
***************

Some components require a parent wrapper or container that dictates the layout
of children. In these cases, abstract the layout into a layout module, such as
``l-grid``, and insert each component as the contents of each ``l-grid_item``.
Here's Berner's example of how he would lay out a list of four ``c-card``
components:

.. code-block:: html

    <ul class="l-grid">
        <li class="l-grid__item">
            <div class="c-card">
                <div class="c-card__header">
                    […]
                </div>
                <div class="c-card__body">
                    […]
                </div>
            </div>
        </li>
        <li class="l-grid__item">
            <div class="c-card">
                <div class="c-card__header">
                    […]
                </div>
                <div class="c-card__body">
                    […]
                </div>
            </div>
        </li>
        <li class="l-grid__item">
            <div class="c-card">
                <div class="c-card__header">
                    […]
                </div>
                <div class="c-card__body">
                    […]
                </div>
            </div>
        </li>
        <li class="l-grid__item">
            <div class="c-card">
                <div class="c-card__header">
                    […]
                </div>
                <div class="c-card__body">
                    […]
                </div>
            </div>
        </li>
    </ul>

In some instances, this isn’t possible. If, for example, your grid isn’t going
to give you the result you want or you simply want something semantic to name
a parent element, what should you do? Berner tends to opt for the word
``container`` or ``list``, depending on the scenario. Sticking with his cards
example, he might use ``<div class=“l-cards-container”>[…]</div>`` or
``<ul class=“l-cards-list”>[…]</ul>``, depending on the use case. The key is
to be consistent with your naming convention.

***************************************************
A Component's Styling or Position Depends on Parent
***************************************************

Simurai covers `styling nested components`_ in detail. Berner summarizes the
techniques he prefers. Assume we want to add a ``c-button`` into the
``card__body`` of the previous example. The button is already its own
component and is marked up like this:

.. code-block:: html

    <button class="c-button c-button--primary">Click me!</button>

If there are no styling differences in the regular button component, then
there is no problem. We would just drop it in like so:

.. code-block:: html

    <div class="c-card">
        <div class="c-card__header">
            <h2 class="c-card__title">Title text here</h3>
        </div>

        <div class="c-card__body">

            <img class="c-card__img" src="some-img.png">
            <p class="c-card__text">Lorem ipsum dolor sit amet, consectetur</p>
            <p class="c-card__text">Adipiscing elit. Pellentesque.</p>

            <!-- Our nested button component -->
            <button class="c-button c-button--primary">Click me!</button>

        </div>
    </div>

However, what happens when there are a few subtle styling differences - for
example, we want to make it a bit smaller, with fully rounded corners, but
only when it’s a part of a ``c-card`` component?

He previously thought that a cross-component class to be the most robust
solution. For example:

.. code-block:: html

    <div class="c-card">
        <div class="c-card__header">
            <h2 class="c-card__title">Title text here</h3>
        </div>

        <div class="c-card__body">

            <img class="c-card__img" src="some-img.png">
            <p class="c-card__text">Lorem ipsum dolor sit amet, consectetur</p>
            <p class="c-card__text">Adipiscing elit. Pellentesque.</p>

            <!-- My *old* cross-component approach -->
            <button class="c-button c-card__c-button">Click me!</button>

        </div>
    </div>

The BEM website calls ``c-card__c-button`` a "mix". The problem with this mix
is ``c-card__c-button`` class is trying to modify one or more properties of
``c-button``, but it will depend on the source ordering (or event specificity)
to successfully apply them. The ``c-card__c-button`` class will work only if
it is declared after the ``c-button`` block in the source code. This can
become difficult to manage as soon as you build more of these cross-components.

The cosmetics of a truly modular UI element should be totally agnostic of the
element’s parent container — it should look the same regardless of where you
drop it. Adding a class from another component for bespoke styling, as the
“mix” approach does, violates the
`open/closed <https://en.wikipedia.org/wiki/Open/closed_principle>`_ principle
of component-driven design — i.e there should be no dependency on another
module for aesthetics.

He instead recommends us to use a modifier for these small cosmetic
differences, because you may well find that you wish to reuse them elsewhere
as your project grows.

.. code-block:: html

  <button class="c-button c-button--rounded c-button--small">Click me!</button>

*******************************
Writing CSS Selectors with Sass
*******************************

One way to write a selector like ``https://benfrain.com/writing-modular-css-bemoocss-selectors-sass-3-3/`` is:

.. code-block:: css

    .namespace {
            &-ComponentName{
                width: 100%;
                &_ModifierName {
                    color: hotpink;
                    &-variant-label {
                            color: pink;
                    }
                }
            }
    }

It compiles to:

.. code-block:: css

    .namespace-ComponentName {
      width: 100%;
    }

    .namespace-ComponentName_ModifierName {
      color: hotpink;
    }

    .namespace-ComponentName_ModifierName-variant-label {
      color: pink;
    }

While this technique adheres to the DRY convention, Ben Frain, in
`Writing Modern CSS Selectors with Sass 3.3`_ considers other approaches by
other authors.

##########
References
##########

* `More Transparent UI Code with Namespaces <ui code with namespaces_>`_
* `Battling BEM CSS`_: 10 Common Problems and How to Avoid Them.
* `State Hooks`_
* `BEM for Small Projects`_
* `Writing Modern CSS Selectors with Sass 3.3`_
* `SUIT CSS Naming Conventions`_
* `The story <bbc rwd story_>`_ behind the 4 years of work on the `BBC News <https://www.bbc.com/news>`_ website using Responsive Web Design (RWD).
* `Scalable and Modular Architecture for CSS <smacss_>`_

.. _ui code with namespaces: https://csswizardry.com/2015/03/more-transparent-ui-code-with-namespaces/
.. _battling bem css: https://www.smashingmagazine.com/2016/06/battling-bem-extended-edition-common-problems-and-how-to-avoid-them/
.. _bem for small projects: https://www.smashingmagazine.com/2014/07/bem-methodology-for-small-projects/
.. _state hooks: https://github.com/chris-pearce/css-guidelines#state-hooks
.. _styling nested components: http://simurai.com/blog/2015/05/11/nesting-components
.. _writing modern css selectors with Sass 3.3: https://benfrain.com/writing-modular-css-bemoocss-selectors-sass-3-3/
.. _suit css naming conventions: https://github.com/suitcss/suit/blob/master/doc/naming-conventions.md
.. _bbc rwd story: https://responsivenews.co.uk/post/114413142693/weve-made-it
.. _smacss: http://smacss.com/

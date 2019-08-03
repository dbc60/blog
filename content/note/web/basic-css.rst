---
title: "Basic CSS"
date: 2019-04-23T06:02:55-04:00
draft: true
categories: [software]
tags: [web]
---

These notes are from `MDN Introduction to CSS <https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS>`_. See also the `MDN CSS Reference`_ as there are more than `300 different properties <mdn css reference_>`_.
<!--more-->

.. _contents:

.. contents:: Contents
   :class: sidebar

**********************
Terms and Basic Syntax
**********************

* A *property* is a human-readable identifier that indicates which stylistic
  feature (e.g. font, width, background color) you want to change.
* A *value* indicates how you want to change a stylistic feature (e.g. to what
  you want to change the font, width or background color).
* A *CSS Declaration* is a property paired with a value. A colon (``:``) separates them.
* A *CSS Declaration Block* is indicated by a pair of open and close braces (``{`` and ``}``) with zero or more CSS declarations in between. Each declaration is separated from the next by a semicolon (``;``). A semicolon after the last declaration in a block is optional, but good style practice includes it to guard against syntax errors if you extend the block later.
* CSS declaration blocks are paired with *selectors* to produce *CSS Rulesets* (or simply *CSS Rules*).

.. code-block:: css

    selectorlist {
      property: value;
      [more property:value; pairs]
    }

******************
Types of Selectors
******************

* `Simple selectors`_ match one or more elements based on element type, ``class``, or ``id``.
* `Attribute selectors`_ match one or more elements based on their attributes and/or attribute values.
* `Pseudo-classes <pseudo-classes and pseudo-elements_>`_ match one or more elements that exist in a certain state, such as an element that is being hovered over by the mouse pointer, or a checkbox that is currently disabled or checked, or an element that is the first child of its parent in the DOM tree.
* `Pseudo-elements <pseudo-classes and pseudo-elements_>`_ match one or more parts of content that are in a certain position in relation to an element, for example the first word of each paragraph, or generated content appearing just before an element.
* `Combinators <combinators and multiple selectors_>`_ are not exactly selectors themselves, but ways of combining two or more selectors in useful ways for very specific selections. So for example, you could select only paragraphs that are direct descendants of divs, or paragraphs that come directly after headings.
* `Multiple selectors <combinators and multiple selectors_>`_ also are not separate selectors; the idea is that you can put multiple selectors on the same CSS rule, separated by commas, to apply a single set of declarations to all the elements selected by those selectors.

******************
Selector Operators
******************

The CSS selector operators are:

- descendant: " " (a space).
- direct descendant: ">".
- adjacent siblings: "+".
- grandchild or later descendant: "*"

Each operator is described below. The CSS used to demonstrate the operator is based on this HTML block:

.. code-block:: html

  <div id="lvl0">
    <p>Child One</p>
    <div id="lvl1">
      <p>Grandchild One</p>
      <p>Grandchild Two</p>
      <div id="lvl2">
        <p>Great Grandchild One</p>
      </div>
    </div>
    <p>Child Two</p>
    <p>Child Three</p>
    <p>Child Four</p>
  </div>

The examples below can be seen `at this Code Pen <https://codepen.io/dbc60/pen/mNMbZV>`_.

Descendant Operator
===================

The space is the descendant selector. In the example below, the target is all ``p`` elements within the container ``div``.

.. code-block:: css

  div#lvl0 p {
    background-color: lightgray;
  }

Direct Descendant
=================

The ">" operator selects the direct descendant of an element. For example:

.. code-block:: css

  div#lvl0 > p {
    border: 2px solid red;
  }

selects only the paragraphs "Child One", "Child Two", "Child Three" and "Child Four", because they are direct descendants of the lvl0 ``div``. The "Grandchild" paragraphs are descended two levels below the lvl0 ``div``, so they are not selected.

Adjacent Siblings
=================

The "+" operator selects adjacent siblings. It will select only the first element of the second type that is immediately preceded by the former selector.

.. code-block:: css

  div + p {
    font-weight: 800;
  }

The example above selects only paragraph "Child Two", because it immediately follows a ``div`` element (the one with ``id=lvl1``).

Grandchild or Later Descendant
==============================

The "*" operator selects grandchildren and later descendants. For example,

.. code-block:: css

  div#lvl0 > p {
    border: 2px solid red;
  }

selects paragraphs "Grandchild One", "Grandchild Two", and "Great Grandchild One".

.. _mdn css reference: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference
.. _simple selectors: https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Selectors/Simple_selectors
.. _attribute selectors: https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Selectors/Attribute_selectors
.. _pseudo-classes and pseudo-elements: https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Selectors/Pseudo-classes_and_pseudo-elements
.. _combinators and multiple selectors: https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Selectors/Combinators_and_multiple_selectors

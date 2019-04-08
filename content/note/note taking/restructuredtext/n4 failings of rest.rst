################
Failings of reST
################

****************************
Poor Support for UI Elements
****************************

The use of Liquid Templates in Jekyll make it easier to present some simple UI elements, like checkboxes. There is no direct support for checkboxes in restructuredText. The best we can do is fake it.

- [ ]
- [x]

Jekyll uses Liquid template to help with filtering HTML and CSS. There is `an article <http://blog.winddweb.info/implement-github-like-checkbox>`_ on how to use ``{{ content }}`` to filter text like ``[ ]``, and replace it with special classes to add a checkbox element.

They edit the layout (``_layouts/post.html``) to include a Liquid template filter:

.. code-block:: html

    <div class="post-content markdown-body" itemprop="articleBody">
      {{ content | replace: '<li>[ ]', 
        '<li class="box task-list-item">
        <input type="checkbox" class="task-list-item-checkbox" disabled>'
        | replace: '<li>[x]', 
        '<li class="box_done task-list-item">
        <input type="checkbox" class="task-list-item-checkbox" value="on" disabled checked>'
      }}
    </div>
 
and a custom style (file ``_sass/_custom-styles.scss``):

.. code-block:: scss

    // styles for checkbox
    .box,
    .box_done,
    .task-list-item {
        list-style-type: none;
    }
    
    .task-list-item input {
      margin: 0 0.2em 0.25em -1.6em;
      vertical-align: middle;
    }
    
    .task-list-item+.task-list-item {
      margin-top: 3px;
    }

Maybe something can be adapted from the `Reauthoring Toolkit`_.

.. _reauthoring toolkit: https://latte.ee.usyd.edu.au/Reauthoring/

**************
Bold & Italics
**************

There doesn't seem to be an easy way to have both *italics* and **bold**. It's either **one** or *the other*. Maybe there's a way to define a role.

**********
No Modules
**********

I'd like to be able to defines roles in one place (file) and use them anywhere.

Ah Ha! This can be done. Use ``rst_prolog`` or ``rst_epilog`` in ``conf.py`` to open a ``.rst`` file containing the set of definitions, roles, and whatnot you desire.

********
Headings
********

The heading syntax is okay, and is very much like `one form of markdown <https://daringfireball.net/projects/markdown/syntax#header>`_. Still, I'd like the option of being able to write atx-style headers where 1-6 hash characters start the line::

  # This is an H1

  ## This is an H2

  ###### This is an H6

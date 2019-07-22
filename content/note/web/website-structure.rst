---
title: "Website Structure"
date: 2019-04-14T09:32:09-04:00
categories: [software]
tags: [design, web]
---

These notes are from `MDN Document and Website Structure`_.

<!--more-->

.. _contents:

.. contents:: Contents
   :class: sidebar

Some of the more common components of web pages are:

header
    Usually a big strip across the top with a big heading and/or logo. This is
    where the main common information about a website usually stays from one
    webpage to another.

navigation bar
    Links to the site's main sections; usually represented by menu buttons,
    links, or tabs. Like the header, this content usually remains consistent
    from one webpage to another — having an inconsistent navigation on your
    website will just lead to confused, frustrated users. Many web designers
    consider the navigation bar to be part of the header rather than a
    individual component, but that's not a requirement; in fact some also argue
    that having the two separate is better for accessibility, as screen readers
    can read the two features better if they are separate.

main content
    A big area in the center that contains most of the unique content of a given
    webpage, for example the video you want to watch, or the main story you're
    reading, or the map you want to view, or the news headlines, etc. This is
    the one part of the website that definitely will vary from page to page!

sidebar
    Some peripheral info, links, quotes, ads, etc. Usually this is contextual to
    what is contained in the main content (for example on a news article page,
    the sidebar might contain the author's bio, or links to related articles)
    but there are also cases where you'll find some recurring elements like a
    secondary navigation system.

footer
    A strip across the bottom of the page that generally contains fine print,
    copyright notices, or contact info. It's a place to put common information
    (like the header) but usually that information is not critical or secondary
    to the website itself. The footer is also sometimes used for SEO purposes,
    by providing links for quick access to popular content.

To implement semantic mark up HTML provides dedicate tags to use.

* **header**: ``<header>``
* **navigation bar**: ``<nav>``
* **main content**: ``<main>``, with various content subsections represented by
  ``<article>``, ``<section>``, and ``<div>`` elements.
* **sidebar**: ``<aside>``, often placed inside ``<main>``
* **footer**: ``<footer>``

***********************************
HTML Layout Elements in More Detail
***********************************

* `<main> <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main>`_ is for content unique to this page. Use ``<main>`` only once per page, and put it directly inside ``<body>``. Ideally this shouldn't be nested within other elements.
* `<article> <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article>`_ encloses a block of related content that makes sense on its own without the rest of the page (e.g., a single blog post).
* `<section> <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section>`_ is similar to ``<article>``, but it is more for grouping together a single part of the page that constitutes one single piece of functionality (e.g., a mini map, or a set of article headlines and summaries). It's considered best practice to begin each section with a heading (``<h1>``, ``<h2>``, etc.); also note that you can break up ``<article>s`` into different ``<section>s``, or ``<section>s`` into different ``<article>s``, depending on the context.
* ``<aside>`` contains content that is not directly related to the main content
  but can provide additional information indirectly related to it (glossary
  entries, author biography, related links, etc.).
* ``<header>`` represents a group of introductory content. If it is a child of
  ``<body>`` it defines the global header of a webpage, but if it's a child of
  an ``<article>`` or <section> it defines a specific header for that section
  (try not to confuse this with titles and headings).
* ``<nav>`` contains the main navigation functionality for the page. Secondary
  links, etc., would not go in the navigation.
* ``<footer>`` represents a group of end content for a page.

*********************
Non-semantic Elements
*********************

For cases where there isn't a suitable semantic element, HTML provides the ``<div>`` and ``<span>`` elements. You should use these preferably with a suitable ``class`` attribute, to provide some kind of label for them so they can be easily targeted.

``<span>`` is an inline non-semantic element, which you should only use if you can't think of a better semantic text element to wrap your content, or don't want to add any specific meaning. For example::

    <p>The King walked drunkenly back to his room at 01:00, the beer doing nothing to aid
    him as he staggered through the door <span class="editor-note">[Editor's note: At this point in the
    play, the lights should be down low]</span>.</p>

``<div>`` is a block level non-semantic element, which you should only use if you can't think of a better semantic block element to use, or don't want to add any specific meaning.

``<br>`` creates a line break in a paragraph; it is the only way to force a rigid structure in a situation where you want a series of fixed short lines, such as in a postal address or a poem. For example:

.. code-block:: html

    <p>There once was a man named O'Dell<br>
    Who loved to write HTML<br>
    But his structure was bad, his semantics were sad<br>
    and his markup didn't read very well.</p>

which renders as:

.. raw:: html

    <p>There once was a man named O'Dell<br>
    Who loved to write HTML<br>
    But his structure was bad, his semantics were sad<br>
    and his markup didn't read very well.</p>

<hr> elements create a horizontal rule in the document that denotes a thematic change in the text (such as a change in topic or scene). Visually it just looks like a horizontal line. As an example:

.. code-block:: html

    <p>Ron was backed into a corner by the marauding netherbeasts. Scared, but determined to protect his friends, he raised his wand and prepared to do battle, hoping that his distress call had made it through.</p>
    <hr>
    <p>Meanwhile, Harry was sitting at home, staring at his royalty statement and pondering when the next spin off series would come out, when an enchanted distress letter flew through his window and landed in his lap. He read it hazily and sighed; "better get back to work then", he mused.</p>

Would render like this:

.. raw:: html

    <p>Ron was backed into a corner by the marauding netherbeasts. Scared, but determined to protect his friends, he raised his wand and prepared to do battle, hoping that his distress call had made it through.</p>
    <hr>
    <p>Meanwhile, Harry was sitting at home, staring at his royalty statement and pondering when the next spin off series would come out, when an enchanted distress letter flew through his window and landed in his lap. He read it hazily and sighed; "better get back to work then", he mused.</p>

*******************************
Links to Miscellaneous Elements
*******************************

* `<address> <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/address>`_
* `<time> <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time>`_

****************************
Planning a My Simple Website
****************************

These steps are take from `MDN Document and Website Structure`_. They are probably overkill for my simple blog. Certainly, the first three steps are applicable. After that, I'm not so sure.

#. Write down the elements that are to be common to most, if not all pages.

   * A header with the site title, subtitle, and maybe a logo. I might have a background image as well.
   * Navigation: Home, Notes, About, Now, Tags, Categories, RSS.
   * A main part, The Home page will have a list of blog posts. The Notes page will have a list of pages with notes on various topics, but aren't blog posts. They're mostly for reference. Tags and Categories will list those items. RSS does whatever RSS does.
   * A footer with the copyright notice and links to my accounts on various social media sites

#. Draw a rough sketch of what you might want the structure of each page to
   look like.
#. Brainstorm all the other (not common to every page) content you want to have
   on your website — write down a big list.

    * Equations in notes and blog posts where math is needed.
    * Graphics and images as needed. Some will be generated by D3js, because it
      looks like fun.
    * A table of contents for long notes and posts, presented in a sidebar.

#. Next, try to sort all these content items into groups, to give you an idea
   of what parts might live together on different pages. This is very similar
   to a technique called `Card sorting <https://developer.mozilla.org/en-US/docs/Glossary/Card_sorting>`_.
#. Sketch a rough sitemap — have a bubble for each page on your site, and draw
   lines to show the typical workflow between pages. The homepage will probably
   be in the center, and link to most if not all of the others; most of the
   pages in a small site should be available from the main navigation, although
   there are exceptions. You might also want to include notes about how things
   might be presented.

*******************
Categories and Tags
*******************

Categories are meant for broad grouping of your posts. Think of these as
general topics or the table of contents for your site. Categories are there to
help identify what your blog is really about. It is to assist readers finding
the right type of content on your site. Categories are hierarchical, so you can
sub-categories.

Tags are meant to describe specific details of your posts. Think of these as
your site’s index words. They are the micro-data that you can use to
micro-categorize your content. Tags are not hierarchical.

For example if you have a personal blog where you write about your life. Your
categories can be something like: Music, Food, Travel, Rambling, and Books. Now
when you write a post about something that you ate, you will add it in the Food
category. You can add tags like pizza, pasta, steak etc.

One of the biggest difference between tags and categories is that for WordPress
you MUST categorize your post. You are not required to add any tags. If you do
not categorize your post, then it will be categorized under the “uncategorized”
category. People often rename the uncategorized category to something like
Other, ramblings etc.

Categories are meant to encompass a group of posts. It is always best to start
with generic categories and work your way down with subcategories as your site
grows. After having run multiple blogs, we have heared that blogs evolve. There
is no way that you can come up with all the right categories. Chances are when
starting out, you are only writing one post a day. Or maybe 3-5 posts a day.
Having 30 top categories is pointless especially when some of them will only
have one or two posts. You are better off with 5 generic categories that have
fresh content rather than 30 top categories where the majority are not updated.

Here are some links with advice on how to use categories and tags:

* `Categories vs Tags SEO Best Practices <wpbeginner categories and tags_>`_.
* `Tags and Categories on Yoast <yoast tags and categories_>`_.

.. _wpbeginner categories and tags: https://www.wpbeginner.com/beginners-guide/categories-vs-tags-seo-best-practices-which-one-is-better/
.. _yoast tags and categories: https://yoast.com/tags-and-categories-difference/

*************
My Categories
*************

#. career: interviewing, job search, etc.
#. hobbies: photography, model railroading, woodworking
#. math: anything primarily about mathematics.
#. projects: home/personal projects.
#. software: anything to do with software development, planning, testing, etc.
#. misc: the catch all for stuff that's hard to categorize.

Should I make a tag or category for any of these topics?

* writing
* skills (life skills)

*******
My Tags
*******

* design
* web

************
Continuation
************

From here, continue with `MDN Structuring a Page of Content`_.

**************
Disappointment
**************

It looks like inline monospace text in ``.rst`` files is rendered with
``<tt></tt>`` elements. The `MDN Presentational Elements`_ page says it's
obsolete.

.. _mdn document and website structure: https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Document_and_website_structure
.. _mdn presentational elements: https://wiki.whatwg.org/wiki/Presentational_elements_and_attributes
.. _mdn structuring a page of content: https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Structuring_a_page_of_content

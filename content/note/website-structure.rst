---
title: "Website Structure"
date: 2019-04-14T09:32:09-04:00
categories: [software]
tags: [web, design]
---

These notes are from MDN `Document and Website Structure <https://
developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/
Document_and_website_structure>`_.

<!--more-->

*****************
General Structure
*****************

Some of the more common components of web pages are:

header
    Usually a big strip across the top with a big heading and/or logo. This is where the
    main common information about a website usually stays from one webpage to another.

navigation bar
    Links to the site's main sections; usually represented by menu buttons, links, or
    tabs. Like the header, this content usually remains consistent from one webpage to
    another — having an inconsistent navigation on your website will just lead to
    confused, frustrated users. Many web designers consider the navigation bar to be part
    of the header rather than a individual component, but that's not a requirement; in
    fact some also argue that having the two separate is better for accessibility, as
    screen readers can read the two features better if they are separate.

main content
    A big area in the center that contains most of the unique content of a given webpage,
    for example the video you want to watch, or the main story you're reading, or the map
    you want to view, or the news headlines, etc. This is the one part of the website
    that definitely will vary from page to page!

sidebar
    Some peripheral info, links, quotes, ads, etc. Usually this is contextual to what is
    contained in the main content (for example on a news article page, the sidebar might
    contain the author's bio, or links to related articles) but there are also cases
    where you'll find some recurring elements like a secondary navigation system.

footer
    A strip across the bottom of the page that generally contains fine print, copyright
    notices, or contact info. It's a place to put common information (like the header)
    but usually that information is not critical or secondary to the website itself. The
    footer is also sometimes used for SEO purposes, by providing links for quick access
    to popular content.

To implement semantic mark up HTML provides dedicate tags to use.

* **header**: ``<header>``
* **navigation bar**: ``<nav>``
* **main content**: ``<main>``, with various content subsections represented by
  ``<article>``, ``<section>``, and ``<div>`` elements.
* **sidebar**: ``<aside>``, often placed inside ``<main>``
* **footer**: ``<footer>``

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

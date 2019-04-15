---
title: "Website Structure"
date: 2019-04-14T09:32:09-04:00
---

These notes are from MDN `Document and Website Structure <https://
developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/
Document_and_website_structure>`_.

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

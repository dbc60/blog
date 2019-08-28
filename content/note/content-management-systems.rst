---
title: "Content Management Systems"
date: 2019-08-28T05:19:34-04:00
draft: true
categories: [software development]
tags: [web]
---

After reading `Using a Static Site Generator: Lessons Learned <https://www.smashingmagazine.com/2016/08/using-a-static-site-generator-at-scale-lessons-learned/>`_, I've become more aware of the scope of what the term "vendor lock-in" encompasses. One area where vendor lock-in shows up is in a Content Management System (CMS) that provides a front-end UI tied to its primary back-end service.

Some CMSs are now separating their primary service from the front end in a trend called headless CMSs.
<!--more-->

Per `Headless CMS Explained in 5 Minutes <https://www.storyblok.com/tp/headless-cms-explained>`_, a headless CMS has only one focus: storing and delivering structured content. It remains an interface to add content and a RESTful API to deliver content when you need it. Instead of being all-powerful, all-in-one solutions, the new generation of CMSs focus on actual management, dropping the rendering process in favor of structured output via an API.

I thought `Ghost <https://ghost.org/>`_ was a full-fledged content publishing platform. It probably is, but it also provides a content API `so it becomes a headless CMS <https://ghost.org/blog/jamstack/>`_. Its traditional front-end theme layer can be, for example, replace with a web front end based on `Gatsby <https://www.gatsbyjs.org/>`_. Ghost has also recently shown the static site generator `Eleventy <https://www.11ty.io/>`_ (a JavaScript alternative to Jekyll) can consume content from Ghost to build out a blog.

#########
Resources
#########

* `Cockpit <https://getcockpit.com>`_, an open source, headless CMS.
* `Headless CMS <https://headlesscms.org/>`_.
* `The Static-Site Revolution <https://ghost.org/blog/jamstack/>`_.
* `Working with Gatsby <https://ghost.org/docs/api/v2/gatsby/>`_ - Using the Ghost API with a Gatsby front end.
* `Eleventy is a simpler static site generator <https://www.11ty.io/>`_
* `Static Sites go all Hollywood – Phil Hawksworth / Front-Trends 2016 <https://www.youtube.com/watch?v=_cuZcnJIjls>`_ - a talk on YouTube concerning static site generation.
* `StaticGen <https://www.staticgen.com/>`_ lists lots of static site generators.

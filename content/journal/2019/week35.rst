---
title: "Week35"
date: 2019-08-25T09:26:18-04:00
draft: true
---

Week 35 is from Monday, August 26, 2019 through the end of Sunday, September 1, 2019.

#######################
Monday, August 26, 2019
#######################

For some reason this morning, I started thinking about comments and how to handle them in a static blog. There are a few interesting solutions with tradeoffs like handling comments via a 3rd party app or platform (like twitter, or discus), hosting software on a server (discourse), and using a CMS, some of which offer free tiers, but may inject ads into the comment stream, collect analytics for serving ads in some other fashion (like on Facebook).

`Derek Kay <https://darekkay.com/>`_ provides a description of several options in his article, `Various Ways to Include Comments on Your Static Site <https://darekkay.com/blog/static-site-comments/>`_. He lists 3rd party providers like `Disqus <https://disqus.com>`_ and `Facebook comments <https://developers.facebook.com/docs/plugins/comments>`_, and includes options for off-site hosting, where you completely outsource the responsibility for collecting and managing comments, and self hosted solutions, where you own all responsibility for the collection and management of comments.

`Using a Static Site Generator: Lessons Learned <https://www.smashingmagazine.com/2016/08/using-a-static-site-generator-at-scale-lessons-learned/>`_ is an interesting article that is tangentially related to the subject of managing comments. The author isn't focused on the needs of bloggers. Rather, he was part of a five person team who used Jekyll to manage a company's sites for brand, documentation, and marketing.

His team liked static sites because they are secure, load fast, easier to modify the layout and other aspects than a CMS, and its easy to add and publish new content (add to a Git branch during the week, and merge to master on Monday morning).

The challenges he found were:

* the larger your page, the longer it took to build. Jekyll, in particular, is not fast, and they were generating all sizes of their auto-generated and auto-optimized responsive images.
* Choosing a static site generator is a bit of a risk. It can speed you up at first, but slow you down when you find a need it doesn't meet. What needs won't a static site generator meet?
* There are occasional cases when you need dynamic content.
* Not all editors are tech-savvy enough to work with content as if it were source code.

Build times were much too long, about 2 hours for a test site of 40 pages and 300 images. The steps they took to reduce build times were:

* split all websites into distinct content packages and tech repositories based on independent content (like German-language vs English-language versions of a site) and update frequencies (blogs are updated many times per day, main website is updated many times per week, documentation - about every two weeks, and the Java performance book only once or twice per year).

  * The content packages were Git repositories that contained everything an author or editor could or should touch: markdown files, images, additional data lists. For each entity, they created a content repository with the same structure.
  * tech repositories contained everything meant for developers: front-end code, templates, content plugins, and the build process (probably scripts) for static site generation.
* use incremental builds. They used `Gulp <http://gulpjs.com/>`_ for image processing and found a plug-in to detect when a file had changed so only changed files would be processed after the first build.

Another goal ws to avoid technology lock-in. For example, Jekyll turned out to not meet their needs as well as they initially thought, they could move on to another static site-generator.

It turns out that Jekyll, with its ecosystem of plug-ins, is not just a static site generator, but a full-fledged build system. Using the benefits of that build system comes at the cost of performance, build time and technology lock-in. You have to write and maintain (in Rugy) anything not included in Jekyll or one of the plug-ins.

To avoid being locked in to Jekyll and custom Ruby code (they were not well versed in the Ruby programming language), they removed all build responsibilities from Jekyll that had nothing to do with generating HTML, except for keeping a check for an assets's existence. They used Gulp builds ahead of invoking Jekyll to generate images, compile JavaScript, and run Sass to compile their style sheets. The benefits were:

* Asset compilation: they could replace Sass if they ever needed to by changing one part of their build file instead of the entire static site generation. Similarly for compilation of other assets.
* Asset independence: if JavaScript changed, but not the styles, they could rebuild just the JavaScript and save time by not rebuilding the style sheets.
* Remove Jekyll without affecting the other key parts of their build.
* Remove post-processing steps (like creating hashed URLs for JavaScript, style sheets, and images) from Jekyll, thus clarifying its purpose.

Jekyll's responsibilities were reduced to converting Markdown and Liquid to HTML pages. Everything else was being done by Gulp. That made them realize three things:

* The self-written plug-ins for custom sectioning elements were being done in Ruby (the only Ruby dependency still there)
* They were still using Liquid templates, which they considered to be an exotic templating language.
* Jekyll is not meant to be included in a build process. Jekyll was created to be the build process. Jekyll opens and analyzes every file during a build. Once you strip away everything from Jekyll that isn't HTML creation, you have to take care of Jekyll's built-in features like incremental builds by yourself.

The author also addresses the occasional need for dynamic content such as comments on blogs. One way to deliver dynamic content is to run JavaScript to download the content from a service. However, JavaScript and internet connections can fail unexpectedly, so such content (like comments on blogs) shouldn't be a critical feature of your website.

Another way to deliver dynamic content is through your own server. They ran a small Node.js application using nginx upstream. Before hitting the static websites, a proxy directs a subset of URLs to the Node.js app, hiding possible static websites underneath. In other words, requests are first sent to the app, which responds as well as it can. Requests the app can't serve fall through to the static website. While they were migrating content from the old CMS to the static website, any content that couldn't be served there,, an nginx proxied the request through to the old server architecture.

A partial nginx configuration to retrieve dynamic content from a Node.js application::

  # This upstream points to a Node.js server running locally
  # on port 3000.
  upstream nodejs-backend {
    server   127.0.0.1:3000
  }

  # Later, we pointed dedicated routes to this Node.js back end
  # when defining locations.
  location /search/ {
    proxy_pass http://nodejs-backend;
  }

The application handles session IDs, calls to the single-sign-on service and a small website search feature implemented with `Lunr <https://lunrjs.com/>`_. The important thing here is that they’re not modifying existing content, but rather providing additional content on top of it.

A partial nginx configuration to retrieve the static content, and proxy the old CMS server for any content that had not yet been migrated to the static site::

  # An upstream server pointing to an IP address where the old
  # CMS output is
  upstream old-cms {
    server  192.168.77.22;
  }

  # This server fetches all requests and fetches the static
  # documents. Should a document not be available, it falls
  # back to the old CMS output.

  server {
    listen 80;
    server_name your-domain.com;

    # the fallback route
    location @fallback {
      proxy_pass  http://old-cms;
    }

    # Either fetch the available document or go back to the
    # fallback route.
    location / {
      try_files   $uri $uri/ @fallback;
    }
  }

It was interesting to see how their design progressed as they discovered what their needs were. For example, they discovered they didn't need Jekyll. They migrated to a JavaScript framework for static site generation called `MetalSmith <http://metalsmith.io/>`_. It distinguishes itself by requiring plug-ins to handle the build logic, and write a simple JavaScript program to chain them together. The plug-ins are all written in JavaScript, so if you're familiar with JavaScript it eliminates the friction of dealing with different languages for different tasks.

A large part of what finally drove them to replace Jekyll was that it could generate edits quickly. Tech-savvy editors and content providers were taught how to use Git, Github, and Atom for creating and pushing content live.

They created a content editing and publishing interface inspired by `Ghost <https://ghost.org/>`_ for those who weren't tech-savvy. Through this interface, these people could get an instant preview of what they were writing.

Once the Ghost-like interface was in place, Jekyll lost what little benefit it had left. Migrating to MetalSmith not only allowed them to replace unfamiliar Ruby plug-ins with plug-ins written in more familiar JavaScript, but they could replace Jekyll's Liquid Template engine with one of their choice (handlebars, in this case). It saved them development time, and kept the output of their content-editing application and static site generator consistent.

*********
Resources
*********

* `Talkyard <https://talkyard.io>`_ is a comment system for blogs.
* `Utterances <https://utteranc.es/>`_ is a lightweight comment widget built on GitHub issues.
* `Hugo has a built-in Disqus template <https://gohugo.io/content-management/comments/>`_ to support comments, but there are alternatives:

  * `Static Man <https://staticman.net/>`_.
  * `Talkyard <https://talkyard.io>`_.
  * `txtpen <https://txtpen.github.io/hn/>`_.
  * `IntenseDebate <https://intensedebate.com/>`_.
  * `Graph Comment <https://graphcomment.com/>`_.
  * `Muut <https://muut.com/>`_.
  * `isso <https://posativ.org/isso/>`_.
  * `Utterances <https://utteranc.es/>`_.
  * `Remark <https://github.com/umputun/remark>`_ (open source, written in Go).
  * `Commento <https://commento.io/>`_.
  * `justComments <https://just-comments.com/>`_.
  * `Talk <https://coralproject.net/talk/>`_.
  * `Discourse <https://www.discourse.org/>`_.

*******************************************
Designing the Glob Pattern Matching Library
*******************************************

It has to run in the kernel, but it would be nice to have unit tests for it. I don't want to create a new set of test messages for the minifilter. It's bad enough it has a ping-pong message built in.

I think I could create a new static library (a ``.lib`` file) that could be linked into the FIM minifilter and a ``.sys`` file that is just for testing, say ``test-glob.sys``. It could accept a message that contains a glob-pattern and returns a value to indicate whether the pattern is valid or not. Another message would provide a glob-pattern and a string to match it against. It would return a value indicating whether or not the string (actually, a file/directory path) was valid or not. Since paths in FIM rules can be marked recursive, the message should also provide a Boolean value indicating whether or not the pattern should be matched recursively against the path.

########################
Tuesday, August 27, 2019
########################

***********
Work Agenda
***********

* 9:30-10:00 Eng/Prod/Support triage in Charlestown
* 10:00-10:30 Ticket Grooming in North End
* 11:05-11:55 one-on-one with Coop.

One-on-One
==========

Intense. Life review. Radical Candor.

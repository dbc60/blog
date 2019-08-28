---
title: Project Sampler
date: 2017-02-17
draft: true
categories: project
tags: [software, idea]
---

I was just thinking this morning of a project to display what I can do on Windows. Mostly, it covered using Windows I/O APIs (graphics, sound, input from a keyboard, mouse, game controller or pen and tablet). I then had a wild idea to expand on that and make a code sampler, something like an embroidery sampler done to show off a needleworkers skill.
<!--more-->

In this case, the sampler would consists of working code examples to demonstrate I/O, graphics and sound on computer, web and handheld mobile devices. The samples would have to work on several operating systems where possible. I should aim for Windows, FreeBSD, Linux and Mac OSX for desktop and server samples. For client-side samples, I should include Android and IOS.

I want to display I/O using graphic and sound APIs native to the particular OS, as well as through the web. To demonstrate back-end code, I should strive to have servers running Windows, FreeBSD and Linux. Keep common code common to the greatest extent possible.

Demonstrate various designs for web applications. Some will present static web sites and others will use databases. Contrast PostgreSQL and some distributed data store, like (possibly) RethinkDB, or some [combination of a database, caching and a document store](http://www.sarahmei.com/blog/2013/11/11/why-you-should-never-use-mongodb/comment-page-1/). Maybe PostgresQL is enough to start with. It has a fast key/value store called [hstore](https://www.postgresql.org/docs/9.0/static/hstore.html), and there's a [tutorial](http://www.postgresqltutorial.com/postgresql-hstore/) for it.

My vision, of course, exceeds my reach. I don't have skills in all of the areas I envision. I'll start with things I know really well and develop those skill I need to have a project, or set of projects, where I can graphically display data transactions in various parts of the system. I'd like a web page, for example, that displayed metrics of some desktop or mobile application. Perhaps there could also be a desktop application that taps into the same information stream that supplies the web page with its data, so the desktop app could also present metrics.

Perhaps there could be a chat or remote desktop application built from open source components. One goal could be to see how a variety of robust distributed applications could be built from the fewest components in the smallest set of appropriate programming languages. What if all we needed was C/C++, HTML, CSS and JavaScript? Of course, there would have to be a selection of libraries - some cross-platform and others not. Implementations in other languages could be compared and contrasted for various metrics (performance being one).

This sampler should include a variety of tools, from scripts written in batch, shell or powershell, to Integrated Development Environments (IDEs), and other things in between - version control, static code analysis, memory leak detectors, performance analysis, editors, text search and editing, graphics editors, sound editors, compilers, interpreters, preprocessors, network configuration, packet tracing, virtualization, visualization, package management, installers, and tools to help design and wire together components to create new applications.

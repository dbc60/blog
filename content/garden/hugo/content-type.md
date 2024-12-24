---
title: "Content Type"
date: 2024-12-24T04:38:35-05:00
2024: ["12"]
tags: [hugo]
---
A content type is a way to organize your content. Hugo resolves the content type from either the type in front matter or, if not set, the first directory in the file path. For example, `content/blog/my-first-event.md` will be of type `blog` if no type is set.
<!--more-->
A content type is used to

- Determine how the content is rendered. See Template Lookup Order and Content Views for more.
- Determine which archetype template to use for new content.

The path to this file is `content/garden/hugo/content-type.md` and there's no type set in the front matter, so its type is `garden`.

The breadcrumbs path is Home > Garden > Hugo > Content Type.

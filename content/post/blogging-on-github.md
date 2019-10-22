---
title: A Blog on GitHub
date: 2015-12-30
2015: ["12"]
categories: blog
tags: [jekyll, github]
---

What do you really need to know to setup a blog on GitHub?
<!--more-->

I want a platform to write about software development, design patterns, and anything else that came to mind. [GitHub user pages](https://help.github.com/articles/user-organization-and-project-pages/) looked like a good place to start. I've toyed with [Jekyll](https://jekyllrb.com/) and [Compass](http://compass-style.org/) in the past, so I thought it would be easy to setup. For the most part, it is. Along the way, I discovered a few stumbling blocks that I will share.

## Initial Setup
The initial steps (create a GitHub repository, install and configure Jekyll) were easy. The first stumbling block I ran into was ensuring the versions of my Ruby gems and my Jekyll configuration were consistent with what GitHub supported. GitHub doesn't yet support Jekyll v3, which is what I have installed on my desktop.

Fortunately they provide excellent [documentation](https://help.github.com/articles/using-jekyll-with-pages/). The most important part is to add `gem 'github-pages'` to your `Gemfile`. By running `bundle install`, you get Jekyll and all the dependencies in the correct version to be compatible with Jekyll on GitHub.

I also installed [Compass](http://compass-style.org/). It's a nice tool that watches the files in the repository for changes, and recompiles the .scss files as needed. GitHub doesn't use Compass, so you have to commit the CSS files it generates to the repository.

## Creating a Blog
Reading and following the documentation for GitHub pages, Jekyll and Compass will establish all of the scaffolding you need to start a blog. It will not provide any scaffolding for the structure and contents of the blog itself.

I thought I'd be able to make a cool blog with responsive CSS so it would be readable on a variety of screen sizes. I learned quickly to keep things simple. I just don't know enough CSS right now to make that happen. I stumbled upon (Googled for "html5 sidebar layout") [one good tutorial](http://multimedia.journalism.berkeley.edu/tutorials/css-layout/) that enabled me to create the basic structure for this blog. Warning: I had to insert `p script { display: block;}` to display the code blocks. Each code block is wrapped in a `<script>` element and is written in an XML `<![CDATA[...]]>` block. The user agent stylesheet sets `script {display: none; }`, so I couldn't see the code.

I made a few adjustments to the styling and HTML to suit my taste. One thing I was delighted to learn was how to make the content area and the sidebar the same height. The tutorial presented a solution in JavaScript, but that didn't work for posts. The disqus comment block wasn't included in the calculation.

The main content area and the sidebar are both included in `div` section with the ID `boxes` (`<div id="boxes">`). All I had to do was style the `div` with `display: flex;`. Here's the code and comment from my stylesheet.

```
/* Using display: flex; to make the sidebar column the same length as the main content.
   See: http://tutorialzine.com/2014/10/easiest-way-equal-height-sidebar/ for details.
   */
#boxes {
    display: flex;
}
```

## More To Do
There's a lot of work that goes into making a web page look presentable. At the very least, text should be readable, sections should be well aligned, and the color theme should be pleasing to the eye. There is a lot to fiddle with, but I think I've done an okay job for now. I glad I have a place to write down ideas, write about projects I want to pursue and share some thoughts in general.

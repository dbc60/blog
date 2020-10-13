---
title: "Restart"
date: 2020-02-11T05:48:36-05:00
2020: ["02"]
categories: [post]
publishDate: 2020-02-15
---

Creating a blog is hard. I admire those who are able to design their own and write regular posts, so much so that I'm trying again to create my own blog. I started this blog late in 2015. After writing a few posts, I became discouraged. I didn't like the way it looked, the tools often broke, and I didn't have a clear idea of what I wanted to write, or why I was blogging.
<!--more-->

Recently I was inspired by a post by Mattias Ott from May 12, 2019, [Into the Personal-Website-Verse](personal website verse_]. He encouraged people to create their own personal website to write, create, share what you like, and to tinker with new technologies.

Your own blog is supposed to be a place where you can make mistakes and learn without pressure. With that in mind, I'm declaring this blog as my soapbox. My space to say what ever I want. My laboratory for experiments in web technologies. My window into my own experience from which I can reflect upon my past, figure out what's of interest now and navigate to a better future. If I'm lucky, I might engage someone who wishes to share their own thoughts and experiences, and I'll learn something new.

## Rebuilding from Jekyll to Hugo

My first priority was to find good tools for creating a static site. The original experiment was, in part, to use [Jekyll] to build the site from Markdown files and publish it from [GitHub Pages]. I was familiar with git, had been using [GitHub] for years, and [Jekyll] and [GitHub Pages] were advertised as a hand-in-glove fit for each other, and they are.

I installed and configured Ruby (Jekyll is written in Ruby, but is not a standalone executable), Bundler to keep Ruby gems up-to-date, Compass to generate CSS from SASS/SCSS, and Jekyll of course, and settled in to learn how to create a blog. After reading a lot of docs, and experimenting a lot with HTML and SCSS, I had a working blog. It was kind of ugly, but it was functional. It had two columns, the left for posts and the right for links to posts by year. As I recall, it took quite a bit of effort to put together the markup, styling, and learn how to use the Liquid Template engine to pull together things like lists of posts by year, month, and day.

At first, the writing and learning experience was delightful. I have a note from March 7, 2016 that says, "Jekyll is really easy to install and use. What takes time is learning enough about its bells and whistles, markdown, HTML, CSS, and Sass to make a blog or website you're own."

I had a couple of `.bat` files to update and launch Jekyll and Compass. The first was `_build\start.bat`:

```html
  @echo off
  REM Update all the gems and then start Compass and Jekyll
  call bundle update
  SET PROJECT_PATH=%~dp0
  call %PROJECT_PATH%quick-start.bat
```

The second was `quick-start.bat`:

```sh
  @echo off
  REM Start Compass and Jekyll without updating gems
  start bundle exec compass watch

  REM Give compass a few seconds to start before launching jekyll.
  @ping 192.0.2.2 -n 1 -w 4000 > nul

  start bundle exec jekyll s --port 4000
```

All I had to do was run `build\start.bat` and open a browser to `http://localhost:4000`. Each time I edited and saved a file, the view in the browser would update after a second or so. Blogging life was good.

Later came a series of annoyances. It started with Compass crashing a lot when editing scss files. Compass was valuable for its math library. I found the exponentiation and logarithm functions most valuable. I used them for calculating the luminance of a color and the contrast ratio between two colors.

The crashes got so annoying that I stopped using Compass in September of 2016. Compass wasn't being maintained anymore, and I wasn't about to start learning Ruby just to be able to write a blog. Fortunately, I learned that Jekyll had a built-in sass compiler. I also figured out how to write the color luminance and contrast ratio functions in pure sass, so I didn't need Compass' math library either. I don't use scss currently. I guess (hope) luminance and contrast ratios are built-in functions by now, but in case they aren't, [here's a gist](https://gist.github.com/dbc60/451f16c588b806967b706b45829e49dc) with those functions and a few others. Feel free to use it as you will.

In October of 2016, the `--watch` option being disabled for Windows in version 3.3.0 of Jekyll. That option was originally intended for BASH on Windows, but was extended to the default `cmd.exe` and PowerShell. I found a fix among the [comments](https://github.com/jekyll/jekyll/issues/5462#issuecomment-253982908) in [Jekyll issue 5462](https://github.com/jekyll/jekyll/issues/5462). The comments said the underlying problem in BASH on Windows has been fixed, so `--watch` will be enabled in a later release. A temporary fix was to open `vendor\bundle\gems\jekyll-3.3.0\lib\jekyll\commands\build.rb` and replace the line `if Utils::Platforms.windows?` with `unless Utils::Platforms.windows?`.

I wasn't comfortable at all with manually modifying gem files. I didn't know Ruby, and those files were managed by Bundler. It just seemed like a bad idea. Still, I was still able to use live-reload and see the effects of edits on HTML and SCSS a few seconds after they happened. Fast feedback loops are truly invaluable when learning anything new.

My last post was in November of 2016 after the US presidential election. I don't remember exactly why I stopped, but part of the reason was that Jekyll was slow, and it felt like the Windows implementation was treated as a second-class citizen.

Besides blogging, I was also using it as a notetaking system. I loved that I could write a markdown file, and Jekyll could turn my notes into a nice looking web page. However, when I had a few dozen notes it would take several seconds to see edits appear in a browser. I wasn't very good with using HTML and CSS, so I became frustrated as I tried to use my notes repository to experiment with layout and design. The feedback loop was irritatingly slow.

I spent months looking into other solutions. I read about [Luhmann's Zettelkasten](http://takingnotenow.blogspot.com/2007/12/luhmanns-zettelkasten.html) for organizing my files, and [Sphinx](http://www.sphinx-doc.org/en/stable/), the tool used by the Python programming language for generating all of their documentation.

Sphinx turned out to be a bit of a rabbit hole, a good one. The source documents for Sphinx are written in reStructuredText (rST). I was curious why that file format was chosen over Markdown or plain text. While rST has its issues and limitations, it is a much more rich markup language than Markdown. Also, Sphinx is a programmable environment. If it doesn't have a directive you need, there's a way to define new ones.

The possibilities just wowed me. I ported all my old notes from Markdown to rST and dove into Sphinx, directives, and roles. I spent a lot of time learning, writing, and even played around with CSS a little bit. Even so, Sphinx presented a kind of impedance mismatch between what I was trying to do - just have a tool that builds nice web pages from my notes - and keeping a Python environment up-to-date as I wanted to try new features added to later releases of Sphinx.

My success with Sphinx for notes left me with a desire to blog again. I was probably suffering from myopia, but at the time I didn't realize that Jekyll is not necessary to build GitHub pages, and I didn't know how or if Sphinx could be configured to work with GitHub pages.

Well, I spent a lot of time in 2018 learning [Go](golang_] for a new project at work. It's a very nice programming language. Late in 2018, I came across [Hugo]. It looked interesting, and what do you know, it's written in Go! I had to give it a try. I figured even if it's not to my liking, I can look at the source code, and learn something more about Go.

It turns out that not only is Hugo useful, it is fast, not too hard to integrate MathJax for nice looking equations, has a powerful template language, and it is even possible to write pages in rST - though it requires integration with the Python script [rst2html5].

That's enough for now. I'll cover my adventures using [Hugo] in a future post.

[personal website verse]: https://matthiasott.com/articles/into-the-personal-website-verse
[dbc60]: https://douglascuthbertson.com
[jekyll]: https://jekyllrb.com/
[github pages]: https://pages.github.com/
[github]: https://github.com/
[rst2html5]: https://pypi.org/project/rst2html5/
[golang]: https://golang.org/
[hugo]:  https://gohugo.io/

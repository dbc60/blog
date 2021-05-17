---
title: "Welcome! Have a Look Around"
date: 2021-05-08T06:50:11-04:00
2021: ["05"]
tags: [100DaysToOffload,draft]
draft: true
publishDate: 2021.06.04
featuredImage: "images/banners/motif-number-1.jpg"
featuredDescription: "Motif No. 1"
---
This blog is a result of tinkering with HTML, CSS, and Go/Hugo templates. I have had more fun with that than actually writing about things.

## Planning

What do I want to write about here?

- That Hugo is programmable?
  - talk about using templates in the layout?
  - talk about shortcodes to make writing things easier?
  - talk about Markdown and that adding shortcodes makes writing posts better/faster?
- HTML and the structure/layout of this blog?
- CSS, using CSS variables to help make style more consistent?
- Compare what I've created to HTML5 Boilerplate?
- Inspirations like [gwern](https://gwern.net) for styling and drop-caps, or [Hyde Stevenson](https://lazybear.io/)'s site for the images associated with each post?

TBD: I'm going to need to import a picture for this post. Motif No. 1 is the default image for my blog. I'd like to have a different one for this post.

I'm going to describe the structure of this site and see if I can connect the HTML, layout templates, and CSS to be sure I understand how it really works.

## A Little About This Site

It grew from a simple desire to have a corner of the web where I could write whatever I wanted. There aren't many posts here mostly because I had more fun learning HTML and CSS. Some of my previous posts show how I [tried a few platforms and site generators]({{< ref "/post/serving-a-blog" >}}) and [how I came to settle]({{< ref "/post/restart" >}}) on GitHub pages with Hugo as the static site generator.

The overall structure of a web page in a nutshell is `<!DOCTYPE html><html><head></head><body></body></html>`. What goes between those start andend tags is what matters. This site has, what I hope are, some reasonable values for a variety of `<meta>` and `<link>` tags. Unlike [Manuel Matuzovic](https://www.matuzo.at/blog/html-boilerplate/), I don't have an explanation for why I chose what's there. I just gathered it along the way while learning about HTML. Some of the info came from [How to Section Your HTML](https://css-tricks.com/how-to-section-your-html/) and similar articles. I did my best to make this site accessible and usable. It is a hobby, so there's lots more to do.

Which reminds me, I have only a "screen" media stylesheet. I really should have one for ["print" media](https://www.matuzo.at/blog/i-totally-forgot-about-print-style-sheets/) or at least add a section to my CSS for `@media print {}`.

Ignoring the boilerplate for `<!DOCTYPE html>` and `<head>`, the `<body>` section defines the overall structure of what you see. It has a masthead, a wrapper around a couple of columns forming the sidebar and main content, and a footer at the end. The masthead consists of the site title and subtitle, a menu for major areas of this blog, and a line for breadcrumb navigation.

{{< highlight html "linenos=inline" >}}
<body>
  <div class="masthead">
    <header class="main-head">
      <div class="title-content">
        <h1 class="siteTitle"><a href="{{ .Site.BaseURL }}">{{ .Site.Title }}</a></h1>
        <h1 class="siteSubTitle"><a href="https://blacklivesmatter.com/" target="_blank">{{- .Site.Params.homeText -}}</a></h1>
      </div>
    </header>
    <nav class="main-nav">
      <div class="main-nav__items">
        <!--template code to extract menu items from config.toml -->
      </div>
    </nav>
    <nav class="nav-breadcrumbs" aria-label="Breadcrumb">
      <ul class="crumb-trail">
        <li class="crumb">
          <a class="crumb-link" href="/">Home</a>
        </li>
        <!--
          more template code to recursively add the following list item to the
          breadcrumb trail based on the path to the current page.
        -->
        <li class="crumb">
          <a class="crumb-link" href="{{ .currentPage.Permalink }}">{{ .currentPage.Title }}</a>
        </li>
      </ul>
    </nav>
  </div>
  <div class="wrapper-content">
    <div class="sidebar-content">
    </div>
    <main class="main-content">
      <img class="featured-image" src="{{.Site.BaseURL}}{{ $featuredImage }}" alt={{ $featuredDescription }}>
      {{ block "main" . -}}
      <h2>Default Main (Should Never Appear)</h2>
      {{- end }}
    </main>
    <div class="wrapper-footer">
      <footer class="main-footer">
        <div class="container">
          {{ .Site.Params.footerText | printf "%s. %s." .Site.Params.copyright | markdownify }}
            <div class="social">
              {{- partial "social-follow.html" . -}}
            </div>
        </div>
      </footer>
      <!--
        optional scripts that can wait to load until the end, like
        <script type="type/x-mathjax-config">...</script>
      -->
    </div>
</body>
{{< /highlight >}}

Continue here with something about the CSS used to style the content; particularly something about keeping the masthead, content, and footer stacked properly while enabling the sidebar and main content to lay side-by-side. Think about mentioning the featured image and how it stacks on top the main content, but leaves the sidebar alone so navigation isn't pushed down and out of reach. In fact, that was the main reason for not putting the featured image up in the masthead or the top of the content wrapper.

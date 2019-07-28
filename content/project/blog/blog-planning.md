---
title: "Blog Planning"
date: 2019-06-25T05:53:03-04:00
draft: true
categories: planning
tags: [blog, blog content, categories, tags]
---

What steps are left to actually launch this blog even though there are styling, presentation, and organizational issues I would like to address?
<!--more-->

What should the cadence of blog posts be? Can I create weekly posts? I think I should be able to post at least monthly.

What content should I post? Just technical or should I include family events? Initially, I think posts should be mostly technical, but I get the feeling that intermixing some personal elements would be okay. Things like my background, where I'm working, my struggles with the commute, my sister's situation, how proud I am of my daughter and son, far away family, friends (my Dojo family in particular), gaming, etc.

- [ ] Consider bringing forward a few of the old posts
  - [A Blog on GitHub](http://douglascuthbertson.com/blog/2015/12/30/blogging-on-github/)
  - Tuck away [A Quick Note on Python](http://douglascuthbertson.com/blog/2016/01/04/a-quick-note-on-python/) as a note until I decide to pursue Python again.
  - maybe keep [Serving a Blog](http://douglascuthbertson.com/blog/2016/09/04/serving-a-blog-site/)
  - [A Dangerous Spectacle](http://douglascuthbertson.com/blog/2016/11/09/the-spectacle/)
- [ ] At least 3 articles exploring the same subject. For example, D3, Python, Go, Project Planning, Hugo, CSS and SCSS, Markdown and reStructuredText, Blogging in general.
- [ ] Have at least 12 articles "in the can" for publication so you have time to work on more.
- [ ] Learn how to use Twitter to annouce new articles, link to news reports so I can express my rage at the Trump administration, and retweet interesting tweets from others.
- [ ] Make tickets on GitHub for work to update the presentation of this blog. These don't have to be done before relaunch. Their purpse is to track changes I want to make.
- [ ] ensure the blog is presentable w/o JavaScript (noscript extension)
- [ ] make a sidebar component and place the navigation menu there.
- [ ] consider a header image. Rotate through 12 monthly, 24 semi-monthly, or as many as 52 weekly header images.
- [ ] I have a lot of notes. I should create series of articles with similar themes. and move them to post with publication dates where possible. It is also okay to have a single post on a single subject - perhaps posting such things between series.
- [ ] Consider subdirectories for the `note/project` folder to help organize project notes. I can see a few directory names:
  - [ ] `anki`. Keep notes about learning, using, and styling anki cards.
  - [ ] `hugo`. Keep notes about learning, using, and configuring it.
  - [ ] `web`. Move `note/web` under `note/project` and write about HTML, CSS, SCSS, and file organization in web projects (like this blog).
  - [ ] `filing`. Write about struggles with keeping paper files organized.
  - [ ] `budget` or `finanaces`. Ways of keeping a budget, making investments, and managing money.
  - [ ] `gaming`. Play. Games online and offline.
  - [ ] `game development`. Handmade Hero, and other inspirations. Tools. Techniques. Although, either the `project` directory may be enough or put this under the `project` directory.
  - [ ] `graphics`. D3, sketching, and related thoughts on visual design and presetation.
  - [ ] `home renovation`. The kitchen cabinet project, and others.
  - [ ] `book reviews`. That might motivate me to read more and take notes on technical books.

I think I want to get rid of the title and subtitle. I also want two columns, where the left column is a narrow, vertical menu and the right is the main content. The main content can be a list of blog posts for a given "section", or an individual post.

A "section" is a Hugo-defined section, where each page in the section can be found in a directory under the `content` directory that is named for the section. For example, all markdown or reStructuredText files under `content/notes/` are in the `notes` section.

## Categories

Think of categories as entries in a table of contents for your website, and tags as index entries. Use categories sparingly. Each blog post should have one or no more than two categories assigned. `One site <organize your blog design with categories and tags_>`_ recommends limitiing yourself to a total of 10 categories across the site.

One way to display categories is to list the applicable ones at the top of each blog post. Another way is to place them in a sidebar, perhaps in a column like a table of contents. You can certainly do both.

My goal is to assign a category to each post and note. Here is my initial list.

1. [x] career: experiences on the job, titles, job search, promotion, and progression.
1. [ ] devops: windows, linux, computer administration, scripts, and automation, but not general programming.
1. [ ] food: dining, recipes, and other food-related topics.
1. [ ] games: all about games, their design, processes for creating them, gameplay, game development, and playing games. This is not necessarily the software aspect of game development.
1. [ ] hobbies: photography, woodworking, sketching, art, design, writing, blogging, model railroads, steampunk.
1. [ ] martial arts: kempo, karazempo goshin jitsu, kendo, Indonesian stick and knife, etc.
1. [ ] math: notes focused entirely on math.
1. [ ] personal finance: money, budgeting, saving, spending.
1. [ ] personal goals: my notes on what I want to achieve in the coming years, months, and weeks.
1. [ ] personal productivity: planning projects; organizing projects, and files and file plans; removing clutter; how to get things done.
1. [ ] personal projects: kitchen renovation, home office, and other projects.
1. [ ] software: reviews of software tools and programs for various tasks. These could include ledger, excel, anki, hugo, krita, blender, visual studio, editors, etc.
1. [ ] software development: the acts of dreaming, planning, designing, and writing software. I should probably include computer science related topics, such as AI, neural networks, data structures, and algorithms. Also, consider including tools and processes like version control, continuous deployment, continuous integration, programming, and parallel programming and concurrency.

I had considered "learning" to be a category, but the more I think about it, the more I think it should be a tag to apply to posts and notes in other categories.

## Tags

Tags are more like index entries. Several tags are likely to apply to each post, so they should be used more generously than categories. To help you choose tags that fit a post, think of an index and what entries you would like to see there to use to find that post.

One way to display tags is to list the applicable ones at either the top or bottom of a blog post. I suppose it wouldn't hurt to have a tag page that lists the complete set of tags across all posts. It might be easier than having a tag cloud or other arrangement in a sidebar.

## Progress

- 2019.07.05: I created a draft blog post, [Evidence-Based Software Engineering]({{< ref "evidence-based-software-engineering.md" >}}). It needs some refinement. I should review and probably condense the sections describing the process, and make my own opions stand out - maybe by placing them at the beginning of each section as an introduction, just before parroting the original article.

## Hugo Rules

The base layout template must be named `baseof.html`. Hugo looks for this template in the following places in this order:

1. `/layouts/section/<TYPE>-baseof.html`
1. `/themes/<THEME>/layouts/section/<TYPE>-baseof.html`
1. `/layouts/<TYPE>/baseof.html`
1. `/themes/<THEME>/layouts/<TYPE>/baseof.html`
1. `/layouts/section/baseof.html`
1. `/themes/<THEME>/layouts/section/baseof.html`
1. `/layouts/_default/<TYPE>-baseof.html`
1. `/themes/<THEME>/layouts/_default/<TYPE>-baseof.html`
1. `/layouts/_default/baseof.html`
1. `/themes/<THEME>/layouts/_default/baseof.html`

Variables are denoted by capitalized text set within `<>`. Note that Hugo’s default behavior is for `type` to inherit from `section` (where `section` is the directory name) unless otherwise specified.

## Current Structure

Several templates are used to organize the content of this site. The main file, `layouts/_default/baseof.html` provides the overall structure of each page. That structure is:

```html
<!DOCTYPE html>

<html>
    <!--
      contents of layouts/partials/head.html which includes the <head> element
    -->
  <body class="base">
    <!--
      default content from layouts/partials/site-header.html which includes
      a <header id="site-header"> element. This can be overriden if a template defines a "header" block.
    -->
    <!--
      content from the partials nav.html and breadcrumbs.html. Each of these
      should be wrapped in a Hugo block so they can be overriden.
    -->
    <main>
      <!-- a main block -->
    </main>
      <!--
        include the partials footer.html and script.html. Agein, these should
        be wrapped in a footer block, or separate footer and end-script blocks.
      -->
    </body>
  </html>
```

The template `layouts/index.html` ranges over pages of type "post" and provides a list of current posts, each with a summary. It produces content like this:

```html
    <main>
      <article class="article-main">
        <!-- _index.md front matter -->
        <p>This is the blog of Douglas Cuthbertson</p>
        <ul>
          <li><a href="note">Notes</a></li>
          <li><a href="project">Projects</a></li>
        </ul>

        <h2 class="title-article">
          <a href="link-to-article">article title</a>
        </h2>
        <div class="article-meta-data">
          <div class="post-meta-data">
            <time datetime="format">Timestamp</time>
            text
          </div>
          <div class="post-metadata">last updated:</div>
          <div class="post-metadata"><a class="tag" href="#">tag</a></div>
        </div>

        <span class="post-summary">
          <!-- variable data -->
        </span>
        <footer class="read-more">
          <a href="#">
            <span class="read-more">...</span>
          </a>
        </footer>

        <!-- repeat with <h2> through </footer> for each article -->
      </article>
    </main>
```

At first glance, it seems to me that ``<article class="article-main">`` should wrap each article summary, and something else should wrap the entire list of articles.

I also think I need to remove some ``id="..."`` attributes and use a class definition other than ``class="container">``. Make some distinct classes, so the different blocks with that attribute can be changed independently of each other.

## Block Structure

Hugo blocks look like a promising feature to help organize the HTML for my site. Block declarations seem to work only from `baseof.html`. That may be okay, but I'm going to have to carefully plan what blocks I need.

I currently have only one, `{{ block "main" . }}`, with no default content. It's great for all of the `single.html` and `list.html` files. Each defines a `main` block and its content is dropped in to place.

I think I should define other blocks just to break up the structure of my master template, `baseof.html` into manageable size parts. For example, `baseof.html` contains a large partial, `head.html`. Maybe `head.html` could be `head.html` could be separated into smaller blocks, where each block is declared in `baseof.html` and default partials are included in each block declaration.

2019.07.26: I've updated `layouts/default/baseof.html` to use Hugo blocks with partials as default content:

```text
<!DOCTYPE html>
{{ $lang := .Site.Language.Lang | default "en" }}
<html lang="{{ $lang }}">
  {{- block "head" . -}}
  {{- partial "head.html" . -}}
  {{- end -}}
  <body class="base">
    {{- block "header" . -}}
        {{- partial "siteHeader.html" . -}}
    {{- end -}}
    {{- block "nav" . -}}
      {{- partial "nav.html" . -}}
    {{- end -}}

    {{ block "nav__breadcrumbs" . }}
      {{- partial "nav__breadcrumbs.html" . -}}
    {{ end }}
    <main>
      {{- block "main" . -}}{{- end }}
    </main>
    {{ "<!-- possibly wrap footer and script in blocks -->" | safeHTML }}
    {{ block "footer" . }}
      {{ partial "footer.html" . -}}
    {{ end }}

    {{ block "postScript" . }}
      {{ partial "postScript.html" . -}}
    {{ end }}
  </body>
</html>
```

## HTML Structure

My use of sectioning and other elements may be crazy wrong! See [How to Section Your HTML](https://css-tricks.com/how-to-section-your-html/)and [Mocup Page Layout for Sectioning Your HTML](https://codepen.io/aardrian/pen/BgQqrQ) for explanations of how to use sectioning elements. There may also be clues on how and when to use the `<header>` element and others.

There is more information in [MDN Using Sections and Outlines](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Using_HTML_sections_and_outlines#Defining_sections).

- [HTML Spec Sectioning Content](https://html.spec.whatwg.org/multipage/dom.html#sectioning-content)
- [HTML Spec Section Outlines](https://html.spec.whatwg.org/multipage/sections.html#outline)
- [HTML Spec Headings and Sections](https://html.spec.whatwg.org/multipage/sections.html#outline)

Sectioning roots are:

- `blockquote`
- `body`
- `details`
- `dialog`
- `fieldset`
- `figure`
- `td`

Sectioning content elements:

- `article`
- `aside`
- `nav`
- `section`

are always considered subsections of their nearest ancestor sectioning root. [MDN's HTML page](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header) has some usage notes for `<header>`:

> The `<header>` element is not sectioning content and therefore does not introduce a new section in the outline. That said, a `<header>` element is intended to usually contain the surrounding section's heading (an `h1–h6` element), but this is not required.

The article makes a nice BEM analogy for `<article>` and`<section>` elements. It states `<article>` is like "block", and `<section>` is like "element".

This means each entry in my list layouts should be wrapped in an `<article>` element. Similarly, each tweet in a list of tweets on Twitter and each item on a search results page would be considered an `<article>` element.

## HTML Example Structure

The structure below (from [this Code Pen](https://codepen.io/aardrian/pen/BgQqrQ) by [Adrian Roselli](http://adrianroselli.com/)) is a rework of [this mock up](https://codepen.io/daniel-tonon/pen/WBybNo) from the CSS-Trick article, [How to Section Your HTML](https://css-tricks.com/how-to-section-your-html/). Apparently, some of the recommendations in that article resulted in a poor experience for users of screen readers. The new structure reduces redundant elements as well as "noise" in screen readers.

```html
<header class="header">

  <!-- Removed the title attribute -->
  <!-- It is an anti-pattern -->
  <a class="logo" href="#">Logo</a>

  <!-- Removed the aria-label -->
  <!-- Its position implies it is primary -->
  <!-- Its presence adds noise for SR users -->
  <nav class="primary-nav">
    <ul>
      <li><a href="#">Primary nav</a></li>
      <li><a href="#">Primary nav</a></li>
      <li><a href="#">Primary nav</a></li>
    </ul>
  </nav>

  <!-- Removed the aria-label -->
  <!-- Purpose implied by only one on page -->
  <!-- Its presence adds noise for SR users -->
  <form class="search" role="search">

    <!-- Got rid of <span> -->
    <!-- It appeared to serve no purpose -->
    <label>
      Search
      <input type="search"/>
    </label>
    <button type="submit">Submit</button>

  </form>

</header>

<nav class="secondary-nav" aria-label="Secondary">
  <ul>
    <li><a href="#">Secondary nav</a></li>
    <li><a href="#">Secondary nav</a></li>
    <li><a href="#">Secondary nav</a></li>
    <li><a href="#">Secondary nav</a></li>
    <li><a href="#">Secondary nav</a></li>
  </ul>
</nav>

<main>

  <!-- Removed the <article> -->
  <!-- It is redundant, adds no value -->
  <!-- If poorly scoped, can create noise -->
  <h1>Main article heading</h1>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quae sunt igitur communia vobis cum antiquis, iis sic utamur quasi concessis; Nihil acciderat ei, quod nollet, nisi quod anulum, quo delectabatur, in mari abiecerat. Unum est sine dolore esse,
    alterum cum voluptate. Laboro autem non sine causa; Theophrasti igitur, inquit, tibi liber ille placet de beata vita? Nihil opus est exemplis hoc facere longius. Duo Reges constructio interrete. Graecum enim hunc versum nostis omnes Suavis laborum
    est praeteritorum memoria. Haec et tu ita posuisti, et verba vestra sunt.</p>
  <h2>Article secondary heading</h2>
  <p>Nos commodius agimus. A mene tu? Tantum dico, magis fuisse vestrum agere Epicuri diem natalem, quam illius testamento cavere ut ageretur. Tenesne igitur, inquam, Hieronymus Rhodius quid dicat esse summum bonum, quo putet omnia referri oportere? Nihilo
    beatiorem esse Metellum quam Regulum. Sed quanta sit alias, nunc tantum possitne esse tanta. Philosophi autem in suis lectulis plerumque moriuntur. Esse enim, nisi eris, non potes.</p>
  <p>Sunt enim quasi prima elementa naturae, quibus ubertas orationis adhiberi vix potest, nec equidem eam cogito consectari. Id Sextilius factum negabat. Quorum sine causa fieri nihil putandum est. Quae autem natura suae primae institutionis oblita est?</p>

</main>

<!-- Removed the aria-label -->
<!-- Purpose implied by only one on page -->
<!-- Its presence adds noise for SR users -->
<aside>

  <section class="share">
    <h2>Share</h2>
    <ul>
      <li><a href="#">Facebook</a></li>
      <li><a href="#">Twitter</a></li>
      <li><a href="#">Email</a></li>
    </ul>
  </section>

  <!-- Not sure <section> adds value here -->
  <!-- Leaving as it does not add SR noise -->
  <section class="recommended">
    <h2>Recommended</h2>
    <ul>
      <li>
        <!-- Removed unnecessary <article> -->
        <!-- The content is in a list item, -->
        <!-- in a list, under a heading, in a region -->
        <!-- This is overkill -->
        <!-- Removed unnecessary <h3> -->
        <!-- See preceding reasons -->
        <!-- Left in a <p> so no need to rely on CSS -->
        <!-- that would still cause SRs to run it together -->
        <p><a href="#">Related article</a></p>
        <p>Article description</p>
      </li>
      <li>
        <!-- Removed unnecessary <article> -->
        <!-- The content is in a list item, -->
        <!-- in a list, under a heading, in a region -->
        <!-- This is overkill -->
        <!-- Removed unnecessary <h3> -->
        <!-- See preceding reasons -->
        <!-- Left in a <p> so no need to rely on CSS -->
        <!-- that would still cause SRs to run it together -->
        <p><a href="#">Related article</a></p>
        <p>Article description</p>
      </li>
    </ul>
  </section>

</aside>

<footer>
  <ul>
    <li><a href="#">Footer link</a></li>
    <li><a href="#">Footer link</a></li>
    <li><a href="#">Footer link</a></li>
    <li><a href="#">Footer link</a></li>
    <li><a href="#">Footer link</a></li>
  </ul>
</footer>
```

The original example is [on Code Pen](https://codepen.io/daniel-tonon/pen/WBybNo), and a counter-example that reduces screen-reader noise [is also on Code Pen](https://codepen.io/aardrian/pen/BgQqrQ).

NOTE: If you see references to the DOA, it is a reference to the [Document Outlining Algorithm](http://adrianroselli.com/2016/08/there-is-no-document-outline-algorithm.html), not "Dead on Arrival".

### Guidelines

For single-topic pages, `<h#>` elements should be based on content structure, not code structure, with a single `<h1>` that corresponds to the _page's topic_ (emphasis mine). There are few reasons to have a landmakr/region without a `<h#>`. Otherwise you are excluding some audience and/or not use regiouns/landmarks well.

## Resources

- [Hugo Blog Styling]({{< ref "hugo-blog-styling.rst" >}})
- [Base Templates and Blocks](https://gohugo.io/templates/base/)
- [Content Sections](https://gohugo.io/content-management/sections/). Sections seem to map to directories under the `content/` directory.
- [How to Section Your HTML](https://css-tricks.com/how-to-section-your-html/)
- [Mocup Page Layout for Sectioning Your HTML](https://codepen.io/aardrian/pen/BgQqrQ)

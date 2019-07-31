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

The structure below (from [this CodePen](https://codepen.io/aardrian/pen/BgQqrQ) by [Adrian Roselli](http://adrianroselli.com/)) is a rework of [this mock up](https://codepen.io/daniel-tonon/pen/WBybNo) from the CSS-Trick article, [How to Section Your HTML](https://css-tricks.com/how-to-section-your-html/). Apparently, some of the recommendations in that article resulted in a poor experience for users of screen readers. The new structure reduces redundant elements as well as "noise" in screen readers.

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

Now that I've copied Roselli's rework here, I want the original to compare with it.

```html

<body>
  <header class="header">
    <!-- Fake logo markup, see article for real markup--><a class="logo" href="#" title="Go to home page">Logo</a>
    <nav class="primary-nav" aria-label="Primary">
      <ul>
        <li><a href="#">Primary nav</a></li>
        <li><a href="#">Primary nav</a></li>
        <li><a href="#">Primary nav</a></li>
      </ul>
    </nav>
    <form class="search" role="search" aria-label="site">
      <label><span>Search</span>
        <input type="search"/>
      </label>
      <button type="submit">Submit</button>
    </form>
  </header>
  <nav class="secondary-nav" aria-label="Secondary">
    <ul>
      <li><a href="#">Secondary nav		</a></li>
      <li><a href="#">Secondary nav		</a></li>
      <li><a href="#">Secondary nav		</a></li>
      <li><a href="#">Secondary nav		</a></li>
      <li><a href="#">Secondary nav		</a></li>
    </ul>
  </nav>
  <main>
    <article>
      <h1>Main article heading</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quae sunt igitur communia vobis cum antiquis, iis sic utamur quasi concessis; Nihil acciderat ei, quod nollet, nisi quod anulum, quo delectabatur, in mari abiecerat. Unum est sine dolore esse, alterum cum voluptate. Laboro autem non sine causa; Theophrasti igitur, inquit, tibi liber ille placet de beata vita? Nihil opus est exemplis hoc facere longius. Duo Reges constructio interrete. Graecum enim hunc versum nostis omnes Suavis laborum est praeteritorum memoria. Haec et tu ita posuisti, et verba vestra sunt.</p>
      <h2>Article secondary heading</h2>
      <p>Nos commodius agimus. A mene tu? Tantum dico, magis fuisse vestrum agere Epicuri diem natalem, quam illius testamento cavere ut ageretur. Tenesne igitur, inquam, Hieronymus Rhodius quid dicat esse summum bonum, quo putet omnia referri oportere? Nihilo beatiorem esse Metellum quam Regulum. Sed quanta sit alias, nunc tantum possitne esse tanta. Philosophi autem in suis lectulis plerumque moriuntur. Esse enim, nisi eris, non potes.</p>
      <p>Sunt enim quasi prima elementa naturae, quibus ubertas orationis adhiberi vix potest, nec equidem eam cogito consectari. Id Sextilius factum negabat. Quorum sine causa fieri nihil putandum est. Quae autem natura suae primae institutionis oblita est?</p>
    </article>
  </main>
  <aside aria-label="Sidebar">
    <section class="share">
      <h2>Share</h2>
      <ul>
        <li><a href="#">Facebook</a></li>
        <li><a href="#">Twitter</a></li>
        <li><a href="#">Email</a></li>
      </ul>
    </section>
    <section class="recommended">
      <h2>Recommended</h2>
      <ul>
        <li>
          <article>
            <h3><a href="#">Related article</a></h3>
            <p>Article description</p>
          </article>
        </li>
        <li>
          <article>
            <h3><a href="#">Related article</a></h3>
            <p>Article description</p>
          </article>
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
</body>
```

NOTE: If you see references to the DOA, it is a reference to the [Document Outlining Algorithm](http://adrianroselli.com/2016/08/there-is-no-document-outline-algorithm.html), not "Dead on Arrival".

The CSS from the [original example](https://codepen.io/daniel-tonon/pen/WBybNo) seems to work on [Roselli's reworked version](https://codepen.io/aardrian/pen/BgQqrQ). It is this:

```css
.visually-hidden {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

body {
  max-width: 120ch;
  min-width: 800px;
  margin: 20px auto;
  padding: 20px;
  padding-bottom: 0;
  display: grid;
  grid-template: "header  header  header" "divider divider divider" "nav     main    sidebar" "footer  footer  footer" / 200px    1fr    200px;
  grid-gap: 20px 40px;
}
body::before {
  content: '';
  display: block;
  grid-area: divider;
  border-bottom: 1px dashed #000;
}
body > header {
  grid-area: header;
}

.header {
  display: grid;
  grid-template: "logo ........... ......" 1fr "logo primary-nav search" auto "logo ........... ......" 1fr / 200px 1fr         200px;
  grid-gap: 0 40px;
}

.primary-nav {
  grid-area: primary-nav;
  display: flex;
}
.primary-nav ul {
  flex-grow: 1;
  display: flex;
  list-style: none;
  padding: 0;
  margin-left: -20px;
}
.primary-nav li {
  margin-left: 20px;
  flex-grow: 1;
  display: flex;
  text-align: center;
}
.primary-nav a {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  background-color: #000;
  color: #fff;
  text-decoration: none;
  padding: 10px 20px;
}

.logo {
  grid-area: logo;
  border: 3px solid #000;
  padding: 10px 20px;
  font-size: 2em;
  margin: 0;
  text-align: center;
  text-decoration: none;
  color: #000;
}

.search {
  grid-area: search;
  display: flex;
  align-items: flex-end;
}
.search input {
  width: 100%;
}

.secondary-nav {
  grid-area: nav;
  background-color: lightgray;
  padding: 20px;
  flex-grow: 1;
}
.secondary-nav ul {
  list-style: none;
  padding: 0;
  display: grid;
  width: 100%;
  grid-template-columns: 1fr;
  grid-gap: 10px;
}
.secondary-nav li {
  display: flex;
  width: 100%;
}
.secondary-nav a {
  background: #fff;
  flex-grow: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #000;
  text-decoration: none;
  font-weight: bold;
  padding: 28px 0;
}

main {
  grid-area: main;
}
main p:last-child {
  margin-bottom: 0;
}

aside {
  grid-area: sidebar;
  background: lightgray;
  padding: 20px;
}
aside section {
  margin-bottom: 2.5em;
}
aside h2 {
  margin: 0;
  margin-bottom: 0.5em;
  font-size: 1.2em;
}

.share ul {
  background: #fff;
  padding-top: 5px;
  padding-bottom: 15px;
}
.share li {
  margin-top: 0.5em;
}

.recommended ul {
  list-style: none;
  padding: 0;
}
.recommended li {
  background: #fff;
  padding: 10px;
  margin-top: 10px;
}
.recommended h3 {
  margin: 0;
  margin-bottom: 0.5em;
}
.recommended p {
  margin: 0;
}

footer {
  grid-area: footer;
  padding: 20px;
  border-top: 1px dashed #000;
  margin-top: 20px;
}
footer ul {
  display: block;
  list-style: none;
  padding: 0;
  text-align: center;
}
footer li {
  display: inline-block;
  margin-left: 10px;
}
footer a {
  color: #000;
  text-decoration: none;
}

h1 {
  margin: 0;
  font-size: 2.5em;
}

h2 {
  font-size: 1.5em;
}

ul {
  margin: 0;
}

a {
  color: #000;
}
```

### Guidelines

For single-topic pages, `<h#>` elements should be based on content structure, not code structure, with a single `<h1>` that corresponds to the _page's topic_ (emphasis mine). There are few reasons to have a landmakr/region without a `<h#>`. Otherwise you are excluding some audience and/or not use regiouns/landmarks well.

## Blog Structure

Here is my blog's structure in HTML:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <!-- BEGIN meta.html -->
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="author" content="">
  <meta property="og:description" name="description" content="">
  <!-- END meta.html -->

  <!-- The four required og properties are og:title, og:type, -->
  <!-- og:url, and og:image. See Open Graph Protocol (ogp.me) -->
  <!-- I used https://realfavicongenerator.net/ to generate the -->
  <!-- icons and https://realfavicongenerator.net/social/ to -->
  <!-- generate the og metadata -->
  <meta property="og:title" content="Dream Sketch Code">
  <meta property="og:type" content="website">
  <meta property="og:url" content="http://douglascuthbertson.com">
  <meta property="og:image:width" content="279">
  <meta property="og:image:height" content="279">
  <meta property="og:image" content="http://douglascuthbertson.com/images/og-image.jpg">

  <meta name="twitter:title" content="Dream, Sketch, Code">

  <!-- BEGIN hugo.Generator -->
  <meta name="generator" content="Hugo 0.56.0-DEV" />
  <!-- END hugo.Generator -->

  <meta name="robots" content="index, follow">
  <link rel="alternate" type="application/rss&#43;xml" href="http://localhost:1313/index.xml">
  <meta name="msapplication-TileColor" content="#da532c">
  <meta name="msapplication-config" content="/images/browserconfig.xml">
  <meta name="theme-color" content="#ffffff">

  <link rel="apple-touch-icon" sizes="180x180" href="http://localhost:1313/images/apple-touch-icon.png">
  <link rel="icon" type="image/png" sizes="32x32" href="http://localhost:1313/images/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="http://localhost:1313/images/favicon-16x16.png">
  <link rel="manifest" href="http://localhost:1313/site.webmanifest">
  <link rel="mask-icon" href="http://localhost:1313/images/safari-pinned-tab.svg" color="#4aa7c1">
  <link rel="shortcut icon" href="http://localhost:1313/images/favicon.ico">
  <link rel="stylesheet" href="http://localhost:1313/style/style.css" integrity="" media="screen">

  <title>
    Dream Sketch Code
  </title>
  <!-- BEGIN head-scripts.html -->
  <!-- END head-scripts.html -->
</head>

<body>
  <!-- BEGIN layouts/partials/siteHeader.html -->
  <header>
    <h1 class="siteTitle">Dream Sketch Code</h1>
    <p class="siteSubtitle">It&rsquo;s What I Do</p>
    <nav class="siteNav">
      <a class="navLink navLink-active" href="http://localhost:1313/">Home</a>
      <a class="navLink " href="http://localhost:1313/note/">Notes</a>
      <a class="navLink " href="http://localhost:1313/project/">Projects</a>
      <a class="navLink " href="http://localhost:1313/about/">About</a>
      <a class="navLink " href="http://localhost:1313/now/">Now</a>
      <a class="navLink " href="http://localhost:1313/tags/">Tags</a>
      <a class="navLink " href="http://localhost:1313/categories">Categories</a>
      <a class="navLink " href="http://localhost:1313/index.xml">RSS</a>
    </nav>
  </header>
  <!-- END layouts/partials/siteHeader.html -->
  <ul class="breadcrumb">
    <li class="breadcrumb__item"><a href="http://localhost:1313/">home</a></li>
  </ul>

  <main>
    <h1>All Posts</h1>
    <!-- Paginates through content/post/*.md -->
    <article>
      <h2 class="title-article"><a href="http://localhost:1313/evidence-based-software-engineering/">Evidence-Based
          Software Engineering</a></h2>
      <header class="article-meta-data">
        <div class="post-metadata">
          <time datetime="2019-07-01">Monday Jul 1, 2019</time>
          - 11 min read - 2231 words.
          <time class="post-metadata" datetime="2019-07-05T11:44">Last updated: Friday Jul 5, 2019 11:44</time>
        </div>
        <div class="post-metadata"><a class="tag" href="http://localhost:1313/tags/ebse">ebse</a><a class="tag"
            href="http://localhost:1313/tags/spi">spi</a></div>
      </header>
      <!-- this renders based on layouts/_default/summary.html (either the local one, or the one in a theme -->
      <blockquote>
        <p>The aim of EBSE is to provide the means by which current best evidence from research can be integrated with
          practical experience and human values in the decision making process regarding the development and maintenance
          of software.</p>

        <p>&mdash; Kitchenham et al., 2004 </p>
      </blockquote>
      <footer class="read-more">
        <a href='http://localhost:1313/evidence-based-software-engineering/'><span class="read-more">Read more
            →</span></a>
      </footer>
    </article>

    <article>
      <h2 class="title-article"><a href="http://localhost:1313/basic-web-design/">Basic Web Design</a></h2>
      <header class="article-meta-data">
        <div class="post-metadata">
          <time datetime="2019-04-13">Saturday Apr 13, 2019</time>
          - 23 min read - 4842 words.
          <time class="post-metadata" datetime="2019-07-22T17:47">Last updated: Monday Jul 22, 2019 17:47</time>
        </div>
        <div class="post-metadata"><a class="tag" href="http://localhost:1313/tags/design">design</a><a class="tag"
            href="http://localhost:1313/tags/web">web</a></div>
      </header>
      <!-- this renders based on layouts/_default/summary.html (either the local one, or the one in a theme -->
      <div class="document">


        <p>How much structure is really needed to make a web page. I have a lot to learn.</p>
      </div>
      <footer class="read-more">
        <a href='http://localhost:1313/basic-web-design/'><span class="read-more">Read more →</span></a>
      </footer>
    </article>

    <article>
      <h2 class="title-article"><a href="http://localhost:1313/a-dangerous-spectacle/">A Dangerous Spectacle</a></h2>
      <header class="article-meta-data">
        <div class="post-metadata">
          <time datetime="2016-11-09">Wednesday Nov 9, 2016</time>
          - 1 min read - 148 words.
          <time class="post-metadata" datetime="2019-07-02T07:41">Last updated: Tuesday Jul 2, 2019 07:41</time>
        </div>
        <div class="post-metadata"><a class="tag" href="http://localhost:1313/tags/2016">2016</a><a class="tag"
            href="http://localhost:1313/tags/president">president</a><a class="tag"
            href="http://localhost:1313/tags/election">election</a><a class="tag"
            href="http://localhost:1313/tags/usa">usa</a></div>
      </header>
      <!-- this renders based on layouts/_default/summary.html (either the local one, or the one in a theme -->
      <p>I&rsquo;m truly saddened by the outcome of the 2016 presidential election.</p>
      <footer class="read-more">
        <a href='http://localhost:1313/a-dangerous-spectacle/'><span class="read-more">Read more →</span></a>
      </footer>
    </article>

    <article>
      <h2 class="title-article"><a href="http://localhost:1313/serviing-a-blog/">Serving a Blog</a></h2>
      <header class="article-meta-data">
        <div class="post-metadata">
          <time datetime="2016-09-04">Sunday Sep 4, 2016</time>
          - 4 min read - 800 words.
          <time class="post-metadata" datetime="2019-07-02T07:41">Last updated: Tuesday Jul 2, 2019 07:41</time>
        </div>
        <div class="post-metadata"><a class="tag" href="http://localhost:1313/tags/css">css</a><a class="tag"
            href="http://localhost:1313/tags/layout">layout</a><a class="tag"
            href="http://localhost:1313/tags/design">design</a></div>
      </header>
      <!-- this renders based on layouts/_default/summary.html (either the local one, or the one in a theme -->
      <p>I want a blog where I control the design and layout. I want to be able to change the way it works and appears
        so I can experiment with various ideas, learn by attempting to replicate other designs and see what happens.</p>
      <footer class="read-more">
        <a href='http://localhost:1313/serviing-a-blog/'><span class="read-more">Read more →</span></a>
      </footer>
    </article>

    <article>
      <h2 class="title-article"><a href="http://localhost:1313/fixing-the-width/">Fixing the Width</a></h2>
      <header class="article-meta-data">
        <div class="post-metadata">
          <time datetime="2016-03-10">Thursday Mar 10, 2016</time>
          - 2 min read - 333 words.
          <time class="post-metadata" datetime="2019-07-14T09:48">Last updated: Sunday Jul 14, 2019 09:48</time>
        </div>
        <div class="post-metadata"><a class="tag" href="http://localhost:1313/tags/jekyll">jekyll</a><a class="tag"
            href="http://localhost:1313/tags/yaml">yaml</a><a class="tag"
            href="http://localhost:1313/tags/liquid-templates">liquid-templates</a><a class="tag"
            href="http://localhost:1313/tags/markdown">markdown</a><a class="tag"
            href="http://localhost:1313/tags/html">html</a><a class="tag"
            href="http://localhost:1313/tags/css">css</a><a class="tag" href="http://localhost:1313/tags/git">git</a><a
            class="tag" href="http://localhost:1313/tags/mathjax">mathjax</a><a class="tag"
            href="http://localhost:1313/tags/bundler">bundler</a></div>
      </header>
      <!-- this renders based on layouts/_default/summary.html (either the local one, or the one in a theme -->
      <p>What an ugly, fragile blog.</p>
      <footer class="read-more">
        <a href='http://localhost:1313/fixing-the-width/'><span class="read-more">Read more →</span></a>
      </footer>
    </article>

    <article>
      <h2 class="title-article"><a href="http://localhost:1313/pursuit-of-happiness/">The Pursuit of Happiness Gels in
          the Imagination</a></h2>
      <header class="article-meta-data">
        <div class="post-metadata">
          <time datetime="2016-03-09">Wednesday Mar 9, 2016</time>
          - 3 min read - 433 words.
          <time class="post-metadata" datetime="2019-07-02T07:41">Last updated: Tuesday Jul 2, 2019 07:41</time>
        </div>
        <div class="post-metadata"><a class="tag" href="http://localhost:1313/tags/happiness">happiness</a><a
            class="tag" href="http://localhost:1313/tags/imagination">imagination</a><a class="tag"
            href="http://localhost:1313/tags/inspiration">inspiration</a><a class="tag"
            href="http://localhost:1313/tags/comics">comics</a></div>
      </header>
      <!-- this renders based on layouts/_default/summary.html (either the local one, or the one in a theme -->
      <p>Imagination is good, but action needs to be taken in the real world.</p>
      <footer class="read-more">
        <a href='http://localhost:1313/pursuit-of-happiness/'><span class="read-more">Read more →</span></a>
      </footer>
    </article>

    <article>
      <h2 class="title-article"><a href="http://localhost:1313/a-quick-note-on-python/">A Quick Note on Python</a></h2>
      <header class="article-meta-data">
        <div class="post-metadata">
          <time datetime="2016-01-04">Monday Jan 4, 2016</time>
          - 2 min read - 361 words.
          <time class="post-metadata" datetime="2019-07-02T07:41">Last updated: Tuesday Jul 2, 2019 07:41</time>
        </div>
        <div class="post-metadata"><a class="tag" href="http://localhost:1313/tags/python">python</a><a class="tag"
            href="http://localhost:1313/tags/programming">programming</a></div>
      </header>
      <!-- this renders based on layouts/_default/summary.html (either the local one, or the one in a theme -->
      <p>I saw an amusing Python tutorial.</p>
      <footer class="read-more">
        <a href='http://localhost:1313/a-quick-note-on-python/'><span class="read-more">Read more →</span></a>
      </footer>
    </article>

    <article>
      <h2 class="title-article"><a href="http://localhost:1313/blogging-on-github/">A Blog on GitHub</a></h2>
      <header class="article-meta-data">
        <div class="post-metadata">
          <time datetime="2015-12-30">Wednesday Dec 30, 2015</time>
          - 3 min read - 567 words.
          <time class="post-metadata" datetime="2019-07-02T07:41">Last updated: Tuesday Jul 2, 2019 07:41</time>
        </div>
        <div class="post-metadata"><a class="tag" href="http://localhost:1313/tags/jekyll">jekyll</a><a class="tag"
            href="http://localhost:1313/tags/yaml">yaml</a><a class="tag"
            href="http://localhost:1313/tags/liquid-templates">liquid-templates</a><a class="tag"
            href="http://localhost:1313/tags/markdown">markdown</a><a class="tag"
            href="http://localhost:1313/tags/html">html</a><a class="tag"
            href="http://localhost:1313/tags/css">css</a><a class="tag"
            href="http://localhost:1313/tags/javascript">javascript</a><a class="tag"
            href="http://localhost:1313/tags/compass">compass</a><a class="tag"
            href="http://localhost:1313/tags/sass">sass</a><a class="tag"
            href="http://localhost:1313/tags/git">git</a><a class="tag"
            href="http://localhost:1313/tags/mathjax">mathjax</a><a class="tag"
            href="http://localhost:1313/tags/bundler">bundler</a><a class="tag"
            href="http://localhost:1313/tags/dns">dns</a></div>
      </header>
      <!-- this renders based on layouts/_default/summary.html (either the local one, or the one in a theme -->
      <p>What do you really need to know to setup a blog on GitHub?</p>
      <footer class="read-more">
        <a href='http://localhost:1313/blogging-on-github/'><span class="read-more">Read more →</span></a>
      </footer>
    </article>
  </main>

  <!-- I might want to wrap footer and script in blocks -->
  <footer class="mt-auto text-left text-muted">
    <div class="container">&copy; Douglas Cuthbertson 2015. Made with HTML, CSS, and perseverance. Generated by <a
        href="https://gohugo.io/">Hugo</a>.</div>
    <a href="https://github.com/dbc60" title="Github"> <span class="social-link fab fa-github"></span> </a>
    <a href="http://stackoverflow.com/users/165347/doug-cuthbertson" title="Stack Overflow"> <span
        class="social-link fab fa-stack-overflow"></span> </a>
    <a href="https://www.linkedin.com/in/douglas-cuthbertson-0487001/" title="LinkedIn"> <span
        class="social-link fab fa-linkedin"></span> </a>
    <a href="https://twitter.com/DougCuthbertson" title="Twitter"> <span class="social-link fab fa-twitter"></span> </a>
    <a href="https://www.reddit.com/user/dbc60" title="reddit"> <span class="social-link fab fa-reddit"></span> </a>
    <a href="https://www.instagram.com/dbc60/" title="Instagram"> <span class="social-link fab fa-instagram"></span>
    </a>
    <a href="https://www.pinterest.com/dougcuthbertson/" title="pinterest"> <span
        class="social-link fab fa-pinterest"></span> </a>
    <a href="https://dbc60.tumblr.com" title="Tumblr"> <span class="social-link fab fa-tumblr"></span> </a>
    <a href="https://www.youtube.com/channel/UCjYq4zK5Pc2vxwpCWUotPxg?view_as=subscriber" title="YouTube"> <span
        class="social-link fab fa-youtube"></span> </a>
    <a href="mailto:doug.cuthbertson@gmail.com" title="E-mail"> <span class="social-link fas fa-envelope"></span> </a>
  </footer>
  <script data-no-instant>document.write('<script src="/livereload.js?port=1313&mindelay=10"></' + 'script>')</script>
</body>
</html>
```

### Class Inventory

What a hodgepodge of elements with class attributes and without. What do I have?

- `<body>`
- `<header>` that wraps the site title, subtitle, and primary navigation.
  - `<h1 class="siteTItle">` for site title.
  - `<p class="siteSubtitle">` for site subtitle.
  - `<nav class="siteNav">` for primary navigation.
    - `<a class="navLink">` links for primary navigation.
- `<ul class="breadcrumb">` breadcrumbs.
  - `<li class="breadcrumb__item">` breadcrumb.
- `<main>`for list of articles (posts).
  - `<h1>` top section heading.
  - `<nav class="secondary-nav">` exists for subfolder/section content.
    - `<ul>` starts the list of subdirectories.
      - `<li>` a subdirectory entry.
        - `<h2 class="title-section">` a title for a subdirectory.
          - `<a>` the link to a subdirectory.
  - `<article>` surrounds each article summary on the home-page listing of all posts.
  - `<h2 class="title-article">` for article title.
    - `<a>` link to article.
  - `<header class="article-meta-data">` for article metadata.
    - `<div class="post-metadata">`wrapper around post time, word count, and last updated.
      - `<time>` for post date.
      - `<time class="post-metadata">` for last updated. The class feels wrong.
    - `<div class="post-metadata">` wrapper around tag links.
      `<a class="tag">` tag link (repeat for each tag on the article).
  - The summary content which could be one of several different kinds of content. For example:
    - `<p>summary</p>` (from markdown source).
    - `<div class="document"><p>summary</p></div>` (from reStructuredText source doc).
    - `<blockquote><p>summary</p></blockquote>` (from markdown that starts with a blockquote).
  - `<footer class="read-more">` after the summary.
    - `<a>` for the "read more" link.
      `<span class="read-more">` around `Read more →`.
- `<footer class="mt-auto text-left text-muted">` after the end of `<main>`.
  - `<div class="container">` for copyright notice.
    - `<a>` for link to Hugo.
  - `<a>` for social link (repeat for each social media link used).
    `<span class="social-link fab fa-github">` for social link icons. The `fa-*` class changes depending on the desired icon.

I have some questions:

- should I wrap posts in an `<article>` element?
- the home page list wraps each item in an `<article>`. Should the section list also wrap each of its listed items in an `<article>` element?
- should each post, note, and project "article" be wrapped in an `<article>` element?
- what should their classes be? Same or different?

## Resources

- [Hugo Blog Styling]({{< ref "hugo-blog-styling.rst" >}})
- [Base Templates and Blocks](https://gohugo.io/templates/base/)
- [Content Sections](https://gohugo.io/content-management/sections/). Sections seem to map to directories under the `content/` directory.
- [How to Section Your HTML](https://css-tricks.com/how-to-section-your-html/)
- [Mocup Page Layout for Sectioning Your HTML](https://codepen.io/aardrian/pen/BgQqrQ)

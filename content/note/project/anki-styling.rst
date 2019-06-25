---
title: "Anki Styling"
date: 2019-06-08T06:23:59-04:00
draft: true
categories: [tools]
tags: [anki, css, web]
---

How do people make card templates for Anki?
<!--more-->

############################
Card Type: What's the Answer
############################

**************
Front Template
**************

The front of the card is:

.. code-block:: html

    <!-- Simple card =====

        - Type: What's the answer?
        - Docs: https://github.com/badlydrawnrob/anki/tree/master/source/docs/simple/index.md
        - Key:  ★ Required
                ☆ Optional (recommended)
                ✎ Optional (notes, markdown)

    ===== -->

    <div id="front" class="anki-Front">
      <section class="simple simple-front">
        <header class="simple-Header">
          <h1 class="simple-Header_Title">
            {{{★ Title}}}
          </h1>
          {{#☆ Subtitle}}
            <h2 class="simple-Header_Subtitle">
              {{{☆ Subtitle}}}
            </h2>
          {{/☆ Subtitle}}
          {{#☆ Syntax (inline code)}}
            <p class="simple-Header_Code">
              <code>{{{☆ Syntax (inline code)}}}</code>
            </p>
          {{/☆ Syntax (inline code)}}
        </header>
        <div class="simple-Sample">
          {{{★ Sample (code block or image)}}}
        </div>
      </section>
    </div>

The top-level ``<div>`` has the ``front`` id. The set of classes are:

* ``anki-front``
* ``simple``
* ``simple-front``
* ``simple-Header``
* ``simple-Header_Title``
* ``simple-Header_Subtitle``
* ``simple-Header_Code``
* ``simple-Sample``

It also uses several fields. These are listed in the Fields. They are documented `here <https://github.com/badlydrawnrob/anki/blob/master/source/docs/simple/index.md>`_:

* ``{{{★ Title}}}``
* ``{{#☆ Subtitle}}``
* ``{{{☆ Subtitle}}}``
* ``{{/☆ Subtitle}}``
* ``{{#☆ Syntax (inline code)}}``
* ``{{{☆ Syntax (inline code)}}}``
* ``{{/☆ Syntax (inline code)}}``
* ``{{{★ Sample (code block or image)}}}``

*************
Back Template
*************

.. code-block:: html

    <div class="anki-Reverse">
      {{FrontSide}}  {{! Anki only }}

      <section id="answer" class="simple simple-reverse">
        <div class="simple-KeyPoint">
          <div class="simple-KeyPoint_Code">
            {{{★ Key point (code block or image)}}}
          </div>
          <div class="simple-KeyPoint_Notes">
            {{{★ Key point notes}}}
          </div>
        </div>
        {{#✎ Other notes}}
          <footer class="simple-Notes">
            {{{✎ Other notes}}}
          </footer>
        {{/✎ Other notes}}
      </section>
    </div>

The top-level div doesn't have a CSS ID like the front template. Instead, it
just has a class, and the child ``<section>`` has the CSS ID ``answer``. Here
are the CSS classes used in the back template:

* ``anki-Reverse``
* ``simple``
* ``simple-reverse``
* ``simple-KeyPoint``
* ``simple-KeyPoint_Code``
* ``simple-KeyPoint_Notes``
* ``simple-Notes``

It also has several templates:

* ``{{FrontSide}}``
* ``{{! Anki only }}``
* ``{{{★ Key point (code block or image)}}}``
* ``{{{★ Key point notes}}}``
* ``{{#✎ Other notes}}``
* ``{{{✎ Other notes}}}``
* ``{{/✎ Other notes}}``

************
Card Styling
************

.. code-block:: css

    /*
     * == Print First CSS ==========================================================
     * MIT License | https://github.com/badlydrawnrob/print-first-css
     * == Heavily based on Cardinal CSS by @cbracco: http://bit.ly/2iDzOZi =========
     */
    /* normalize.css v8.0.1 | MIT License | github.com/necolas/normalize.css */
    html {
      line-height: 1.15;
      /* 1 */
      -webkit-text-size-adjust: 100%;
      /* 2 */
    }
    body {
      margin: 0;
    }
    main {
      display: block;
    }
    h1 {
      font-size: 2em;
      margin: 0.67em 0;
    }
    hr {
      box-sizing: content-box;
      /* 1 */
      height: 0;
      /* 1 */
      overflow: visible;
      /* 2 */
    }
    pre {
      font-family: monospace, monospace;
      /* 1 */
      font-size: 1em;
      /* 2 */
    }
    a {
      background-color: transparent;
    }
    abbr[title] {
      border-bottom: none;
      /* 1 */
      text-decoration: underline;
      /* 2 */
      text-decoration: underline dotted;
      /* 2 */
    }
    b,
    strong {
      font-weight: bolder;
    }
    code,
    kbd,
    samp {
      font-family: monospace, monospace;
      /* 1 */
      font-size: 1em;
      /* 2 */
    }
    small {
      font-size: 80%;
    }
    sub,
    sup {
      font-size: 75%;
      line-height: 0;
      position: relative;
      vertical-align: baseline;
    }
    sub {
      bottom: -0.25em;
    }
    sup {
      top: -0.5em;
    }
    img {
      border-style: none;
    }
    button,
    input,
    optgroup,
    select,
    textarea {
      font-family: inherit;
      /* 1 */
      font-size: 100%;
      /* 1 */
      line-height: 1.15;
      /* 1 */
      margin: 0;
      /* 2 */
    }
    button,
    input {
      /* 1 */
      overflow: visible;
    }
    button,
    select {
      /* 1 */
      text-transform: none;
    }
    button,
    [type="button"],
    [type="reset"],
    [type="submit"] {
      -webkit-appearance: button;
    }
    button::-moz-focus-inner,
    [type="button"]::-moz-focus-inner,
    [type="reset"]::-moz-focus-inner,
    [type="submit"]::-moz-focus-inner {
      border-style: none;
      padding: 0;
    }
    button:-moz-focusring,
    [type="button"]:-moz-focusring,
    [type="reset"]:-moz-focusring,
    [type="submit"]:-moz-focusring {
      outline: 1px dotted ButtonText;
    }
    fieldset {
      padding: 0.35em 0.75em 0.625em;
    }
    legend {
      box-sizing: border-box;
      /* 1 */
      color: inherit;
      /* 2 */
      display: table;
      /* 1 */
      max-width: 100%;
      /* 1 */
      padding: 0;
      /* 3 */
      white-space: normal;
      /* 1 */
    }
    progress {
      vertical-align: baseline;
    }
    textarea {
      overflow: auto;
    }
    [type="checkbox"],
    [type="radio"] {
      box-sizing: border-box;
      /* 1 */
      padding: 0;
      /* 2 */
    }
    [type="number"]::-webkit-inner-spin-button,
    [type="number"]::-webkit-outer-spin-button {
      height: auto;
    }
    [type="search"] {
      -webkit-appearance: textfield;
      /* 1 */
      outline-offset: -2px;
      /* 2 */
    }
    [type="search"]::-webkit-search-decoration {
      -webkit-appearance: none;
    }
    ::-webkit-file-upload-button {
      -webkit-appearance: button;
      /* 1 */
      font: inherit;
      /* 2 */
    }
    details {
      display: block;
    }
    summary {
      display: list-item;
    }
    template {
      display: none;
    }
    [hidden] {
      display: none;
    }
    html {
      box-sizing: border-box;
    }
    *,
    *:before,
    *:after {
      box-sizing: inherit;
    }
    a,
    abbr,
    acronym,
    address,
    applet,
    article,
    aside,
    b,
    blockquote,
    body,
    caption,
    center,
    cite,
    code,
    dd,
    del,
    details,
    dfn,
    div,
    dl,
    dt,
    em,
    fieldset,
    figcaption,
    figure,
    footer,
    form,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    header,
    hgroup,
    hr,
    html,
    i,
    iframe,
    img,
    ins,
    kbd,
    label,
    legend,
    li,
    main,
    menu,
    nav,
    object,
    ol,
    p,
    pre,
    q,
    s,
    samp,
    section,
    small,
    span,
    strong,
    sub,
    summary,
    sup,
    table,
    tbody,
    td,
    tfoot,
    th,
    thead,
    time,
    tr,
    u,
    ul,
    var {
      margin: 0;
      padding: 0;
      border: 0;
    }
    html {
      color: #000;
      font-family: system-ui, sans-serif;
      font-size: 1rem;
      line-height: 1.5;
      background: transparent;
    }
    body {
      min-height: 100%;
    }
    blockquote,
    dl,
    figure,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    hr,
    menu,
    ol,
    p,
    pre,
    summary,
    table,
    ul {
      margin-bottom: 1.5rem;
    }
    caption,
    p,
    table,
    td,
    textarea,
    th {
      word-wrap: break-word;
      hyphens: auto;
    }
    blockquote {
      font-style: normal;
      padding: 1.5rem;
      border: 0.0625rem solid #000;
    }
    @media screen {
      blockquote {
        padding: 0 0 0 1.5rem;
        border-width: 0 0 0 0.125rem;
      }
    }
    blockquote p {
      margin: 0;
    }
    blockquote p + p {
      margin-top: 1.5rem;
    }
    blockquote cite {
      font-style: normal;
      font-size: 1rem;
    }
    code,
    kbd,
    pre,
    samp {
      font-family: monospace, monospace;
      font-size: 1rem;
      font-style: normal;
      line-height: 1.5;
    }
    code,
    kbd {
      margin: 0;
      padding: 0.25rem;
      white-space: nowrap;
    }
    @media screen {
      code,
      kbd {
        border-radius: 0.125rem;
        background-color: #f1f1f1;
      }
    }
    pre {
      position: relative;
      overflow: auto;
      padding: 1.5rem;
      white-space: pre-wrap;
      word-wrap: normal;
      word-break: normal;
      tab-size: 4;
      hyphens: none;
      border: 0.0625rem solid #000;
    }
    pre + pre {
      border-top: transparent;
      margin-top: -1.5rem;
    }
    @media screen {
      pre {
        white-space: pre;
        background: #f1f1f1;
        border-color: transparent;
      }
    }
    pre code {
      display: block;
      overflow: auto;
      height: 100%;
      margin: 0;
      padding: 0;
      white-space: pre;
      color: inherit;
      border: none;
      border-radius: 0;
      background: transparent;
    }
    button,
    input[type="checkbox"],
    input[type="file"],
    input[type="image"],
    input[type="radio"],
    input[type="reset"],
    input[type="submit"],
    label,
    select {
      cursor: pointer;
    }
    input[type="color"],
    input[type="range"] {
      vertical-align: middle;
    }
    fieldset {
      min-width: 0;
      margin: 0;
      padding: 0;
      border: 0;
    }
    input[type="checkbox"],
    input[type="image"],
    input[type="radio"] {
      display: inline-block;
      width: auto;
    }
    input[type="file"] {
      max-width: 100%;
      cursor: pointer;
    }
    input[type="search"] {
      box-sizing: border-box;
      appearance: none;
    }
    input[type="submit"],
    input[type="button"],
    input[type="image"],
    input[type="reset"],
    select {
      border-radius: 0;
    }
    legend {
      font-weight: 700;
      width: 100%;
      padding: 0;
      border: 0;
    }
    textarea {
      max-width: 100%;
      height: auto;
      resize: vertical;
    }
    h1 {
      margin-bottom: 3rem;
      font-weight: normal;
      font-size: 3rem;
      line-height: 1;
      text-transform: none;
      letter-spacing: 0rem;
    }
    h2 {
      margin-bottom: 1.75rem;
      font-weight: normal;
      font-size: 2.125rem;
      line-height: 1;
      text-transform: none;
      letter-spacing: normal;
    }
    h3 {
      margin-bottom: 1.25rem;
      font-weight: normal;
      font-size: 1.5rem;
      line-height: 1.25;
      text-transform: none;
      letter-spacing: normal;
    }
    h4 {
      margin-bottom: 1.5rem;
      font-weight: 700;
      font-size: 1.25rem;
      line-height: 1;
      text-transform: none;
      letter-spacing: 0.009375rem;
    }
    h5 {
      margin-bottom: 0;
      font-weight: 700;
      font-size: 1rem;
      line-height: 1.5;
      text-transform: none;
      letter-spacing: normal;
    }
    h6 {
      margin-bottom: 0;
      font-weight: 700;
      font-size: 1rem;
      line-height: 1.5;
      text-transform: none;
      letter-spacing: normal;
    }
    hr {
      display: block;
      padding: 0;
      border: 0;
      border-top: 0.25rem solid #000;
    }
    img {
      font-style: italic;
      vertical-align: middle;
      max-width: 100%;
    }
    figcaption {
      margin-top: 1.5rem;
      font-size: 0.75rem;
      font-style: normal;
    }
    figcaption > img {
      display: block;
    }
    dl dt {
      font-weight: 700;
    }
    dl dd {
      margin: 0;
    }
    ol li,
    ul li {
      margin-left: 1.5rem;
    }
    ol {
      list-style: decimal;
    }
    ol ol {
      list-style: upper-alpha;
    }
    ol ol ol {
      list-style: lower-roman;
    }
    ol ol ol ol {
      list-style: lower-alpha;
    }
    ol ol,
    ul ol,
    ol ul,
    ul ul {
      margin-bottom: 0;
    }
    audio,
    canvas,
    iframe,
    svg,
    video {
      vertical-align: middle;
    }
    audio,
    canvas,
    video {
      width: 100%;
      height: auto;
    }
    @media print {
      a,
      a:visited {
        color: #000;
        text-decoration: underline;
      }
      a[href]:after {
        content: " (" attr(href) ")";
      }
      abbr[title]:after {
        content: " (" attr(title) ")";
      }
      a[href^="#"]:after,
      a[href^="javascript:"]:after {
        content: "";
      }
      pre,
      blockquote {
        page-break-inside: avoid;
      }
      thead {
        display: table-header-group;
      }
      tr,
      img {
        page-break-inside: avoid;
      }
      p,
      h2,
      h3 {
        orphans: 3;
        widows: 3;
      }
      h2,
      h3 {
        page-break-after: avoid;
      }
    }
    table {
      width: 100%;
      table-layout: fixed;
      empty-cells: show;
    }
    tr {
      vertical-align: baseline;
    }
    th,
    tfoot td {
      text-align: left;
    }
    th,
    td {
      overflow: visible;
    }
    abbr,
    acronym,
    dfn[title] {
      cursor: help;
    }
    abbr a {
      text-decoration: none;
    }
    del {
      font-style: normal;
      text-decoration: line-through;
    }
    details {
      cursor: pointer;
    }
    em,
    i,
    cite {
      font-style: italic;
    }
    /*# sourceMappingURL=print-first.css.map */
    :root {
      --color-bbbb: #000;
      --color-bbb: #000;
      --color-bb: #ccc;
      --color-b: #f9f9f9;
      --color-card-l: #fff;
      --color-card-ll: #eceff1;
      --color-card-lll: #bdbdbd;
      --color-card-llll: #757575;
      --color-code-light-background: #ffffcc;
      --color-code-light-base: #586e75;
      --color-code-light-comment: #93a1a1;
      --color-code-light-error: #93a1a1;
      --color-code-light-highlight: #dc322f;
      --color-code-light-int: #2aa198;
      --color-code-light-key: #859900;
      --color-code-light-lowlight: #268bd2;
      --color-code-light-op: #859900;
      --color-code-light-str: #2aa198;
      --color-code-light-var: #268bd2;
      --color-code-dark-background: #272822;
      --color-code-dark-base: #f8f8f8;
      --color-code-dark-comment: #777;
      --color-code-dark-error: #960050;
      --color-code-dark-highlight: #ec7b20;
      --color-code-dark-int: #a877ff;
      --color-code-dark-key: #70d8ef;
      --color-code-dark-lowlight: #ec7b20;
      --color-code-dark-op: #f12056;
      --color-code-dark-str: #e5de73;
      --color-code-dark-var: #aae626;
      --spacing-increment: var(--spacing-pp);
      --spacing-pppppppp: 128 / 16;
      --spacing-ppppppp: 112 / 16;
      --spacing-pppppp: 96 / 16;
      --spacing-ppppp: 80 / 16;
      --spacing-pppp: 64 / 16;
      --spacing-ppp: 48 / 16;
      --spacing-pp: 32 / 16;
      --spacing-p: 24 / 16;
      --spacing-base: 16 / 16;
      --spacing-m: 8 / 16;
      --spacing-mm: 4 / 16;
      --spacing-mmm: 2 / 16;
      --spacing-mmmm: 1 / 16;
      --spacing-eight: calc(var(--spacing-pppppppp) * 1rem);
      --spacing-seven: calc(var(--spacing-ppppppp) * 1rem);
      --spacing-six: calc(var(--spacing-pppppp) * 1rem);
      --spacing-five: calc(var(--spacing-ppppp) * 1rem);
      --spacing-four: calc(var(--spacing-pppp) * 1rem);
      --spacing-three: calc(var(--spacing-ppp) * 1rem);
      --spacing-two: calc(var(--spacing-pp) * 1rem);
      --spacing: calc(var(--spacing-p) * 1rem);
      --spacing-one: calc(var(--spacing-base) * 1rem);
      --spacing-half: calc(var(--spacing-m) * 1rem);
      --spacing-quarter: calc(var(--spacing-mm) * 1rem);
      --spacing-micro: calc(var(--spacing-mmm) * 1rem);
      --spacing-px: calc(var(--spacing-mmmm) * 1rem);
      --ios: 'San Francisco';
      --android: 'Noto', 'Roboto';
      --ios-mono: 'San Francisco Mono';
      --android-mono: 'Noto Mono', 'Roboto Mono';
      --font-family: var(--ios), var(--android), sans-serif;
      --font-family-mono: var(--ios-mono), var(--android-mono), monospace;
      font-family: var(--font-family);
      --font-size-pppppp: calc((96 / 16) * 1rem);
      --font-size-ppppp: calc((60 / 16) * 1rem);
      --font-size-pppp: calc((48 / 16) * 1rem);
      --font-size-ppp: calc((34 / 16) * 1rem);
      --font-size-pp: calc((24 / 16) * 1rem);
      --font-size-p: calc((20 / 16) * 1rem);
      --font-size: calc((16 / 16) * 1rem);
      --font-size-m: calc((14 / 16) * 1rem);
      --font-size-mm: calc((12 / 16) * 1rem);
      --font-size-mmm: calc((10 / 16) * 1rem);
      --line-height-eight: calc(var(--spacing-pppppppp));
      --line-height-seven: calc(var(--spacing-ppppppp));
      --line-height-six: calc(var(--spacing-pppppp));
      --line-height-five: calc(var(--spacing-ppppp));
      --line-height-four: calc(var(--spacing-pppp));
      --line-height-three: calc(var(--spacing-ppp));
      --line-height-two: calc(var(--spacing-pp));
      --line-height: calc(var(--spacing-p));
      --line-height-one: calc(var(--spacing-base));
      --line-height-half: calc(var(--spacing-m));
      --line-height-quarter: calc(var(--spacing-mm));
      --border-radius: var(--spacing-micro);
    }
    pre,
    pre code {
      text-align: left;
      color: var(--color-code-dark-base);
      font-family: var(--font-family-mono);
      background: var(--color-code-dark-background);
    }
    pre code b,
    pre code strong {
      color: var(--color-code-dark-op);
    }
    pre code i,
    pre code em {
      color: var(--color-code-dark-int);
    }
    pre code s,
    pre code u {
      color: var(--color-code-dark-str);
    }
    pre code span,
    pre code sup {
      color: var(--color-code-dark-key);
    }
    pre code var,
    pre code sub {
      color: var(--color-code-dark-var);
    }
    pre code small {
      color: var(--color-code-dark-comment);
    }
    pre code q {
      color: var(--color-code-dark-lowlight);
    }
    pre code mark {
      color: var(--color-code-dark-highlight);
    }
    code {
      font-family: var(--font-family-mono);
      background: var(--color-code-light-background);
      white-space: pre;
      white-space: pre-wrap;
    }
    code:empty {
      margin: 0;
      padding: 0;
      background: transparent;
      border-color: transparent;
    }
    code i,
    code em,
    code b,
    code strong,
    code sup,
    code sub,
    code var,
    code small,
    code s,
    code u,
    code q,
    code mark {
      font-size: inherit;
      font-style: inherit;
      font-weight: inherit;
      text-decoration: none;
      background: none;
    }
    code b,
    code strong {
      color: var(--color-code-light-op);
    }
    code i,
    code em {
      color: var(--color-code-light-int);
    }
    code s,
    code u {
      color: var(--color-code-light-str);
    }
    code span,
    code sup {
      color: var(--color-code-light-key);
    }
    code var,
    code sub {
      color: var(--color-code-light-var);
    }
    code small {
      color: var(--color-code-light-comment);
    }
    code q {
      color: var(--color-code-light-lowlight);
    }
    code mark {
      color: var(--color-code-light-highlight);
    }
    img {
      max-width: 100%;
      height: auto;
    }
    .anki-Reverse .simple-Sample pre {
      margin-bottom: 0;
    }
    .simple {
      border-radius: var(--border-radius);
    }
    .simple-front {
      margin-top: var(--spacing);
    }
    .simple-Header {
      position: relative;
      display: flex;
      flex-wrap: wrap;
      text-align: center;
      justify-content: space-evenly;
      align-items: baseline;
      background: var(--color-card-ll);
      border: var(--spacing-px) solid var(--color-card-ll);
      border-bottom-color: transparent;
      border-top-left-radius: var(--border-radius);
      border-top-right-radius: var(--border-radius);
    }
    .simple-Header_Title {
      flex: 0 0 100%;
      margin: 0 0 var(--spacing-one);
      padding: var(--spacing-half);
      font-weight: 700;
      font-size: var(--font-size-p);
      line-height: var(--line-height);
      text-transform: none;
      letter-spacing: normal;
      border-bottom: var(--spacing-px) solid var(--color-card-lll);
      background: var(--color-card-l);
    }
    .simple-Header_Title::before {
      content: '★';
    }
    .simple-Header_Subtitle {
      margin: 0 0 var(--spacing-half);
      padding: var(--spacing-half);
      font-weight: normal;
      font-size: var(--font-size);
      line-height: var(--line-height);
      text-transform: none;
      letter-spacing: normal;
      background: var(--color-card-ll);
      border-top-left-radius: var(--border-radius);
      border-top-right-radius: var(--border-radius);
    }
    .simple-Header_Code {
      margin: 0 0 var(--spacing-half) 0;
      padding: var(--spacing-half);
    }
    .simple-KeyPoint_Code pre {
      margin: 0;
    }
    .simple-KeyPoint_Notes {
      margin-bottom: var(--spacing);
      padding: var(--spacing) var(--spacing-one);
      background: var(--color-card-ll);
    }
    .simple-KeyPoint_Notes ul > li,
    .simple-KeyPoint_Notes ol > li {
      margin-left: var(--spacing-one);
    }
    .simple-Notes {
      margin-bottom: var(--spacing);
      color: var(--color-card-llll);
      font-size: var(--font-size-m);
      font-style: italic;
      line-height: var(--line-height-one);
    }
    .missing {
      border-radius: var(--border-radius);
    }
    .missing-front {
      margin-top: var(--spacing);
    }
    .missing .cloze {
      color: var(--color-code-dark-op) !important;
      font-weight: 700;
      background: var(--color-code-light-background);
      padding: var(--spacing-quarter);
      border-radius: var(--border-radius);
    }
    .missing-Header {
      position: relative;
      display: flex;
      flex-wrap: wrap;
      text-align: center;
      justify-content: space-evenly;
      align-items: baseline;
      background: var(--color-card-ll);
      border: var(--spacing-px) solid var(--color-card-ll);
      border-bottom-color: transparent;
      border-top-left-radius: var(--border-radius);
      border-top-right-radius: var(--border-radius);
    }
    .missing-Header_Title {
      flex: 0 0 100%;
      margin: 0 0 var(--spacing-one);
      padding: var(--spacing-half);
      font-weight: 700;
      font-size: var(--font-size-p);
      line-height: var(--line-height);
      text-transform: none;
      letter-spacing: normal;
      border-bottom: var(--spacing-px) solid var(--color-card-lll);
      background: var(--color-card-l);
    }
    .missing-Header_Title::before {
      content: '★';
    }
    .missing-Header_Subtitle {
      margin: 0 0 var(--spacing-half);
      padding: var(--spacing-half);
      font-weight: normal;
      font-size: var(--font-size);
      line-height: var(--line-height);
      text-transform: none;
      letter-spacing: normal;
      background: var(--color-card-ll);
      border-top-left-radius: var(--border-radius);
      border-top-right-radius: var(--border-radius);
    }
    .missing-Header_Code {
      margin: 0 0 var(--spacing-half) 0;
      padding: var(--spacing-half);
    }
    .missing-KeyPoint_Code pre {
      margin: 0;
    }
    .missing-KeyPoint_Notes {
      margin-bottom: var(--spacing);
      padding: var(--spacing) var(--spacing-one);
      background: var(--color-card-ll);
    }
    .missing-KeyPoint_Notes ul > li,
    .missing-KeyPoint_Notes ol > li {
      margin-left: var(--spacing-one);
    }
    .missing-Notes {
      margin-bottom: var(--spacing);
      color: var(--color-card-llll);
      font-size: var(--font-size-m);
      font-style: italic;
      line-height: var(--line-height-one);
    }
    .test-Anki {
      margin: var(--spacing-one);
    }
    @media (min-width: 840px) {
      .test-Anki {
        width: 60%;
        margin: 0 auto;
      }
    }
    .test-AnkiCard-Front {
      margin-bottom: calc(var(--spacing-eight) * 4);
    }
    .test-AnkiCard-Reverse .simple-Sample pre {
      margin-bottom: 0;
    }
    .test-AnkiCard-Button {
      display: inline-block;
      margin: var(--spacing) 0;
      padding: var(--spacing);
      width: 100%;
      color: inherit;
      font-family: var(--font-family);
      font-weight: 700;
      font-size: var(--font-size-m);
      text-align: center;
      text-transform: uppercase;
      text-decoration: none;
      letter-spacing: normal;
      line-height: var(--line-height-half);
      vertical-align: middle;
      white-space: nowrap;
      cursor: pointer;
      background-color: #f5f5f5;
      border: 0 none;
      border-radius: var(--border-radius);
      box-shadow: 0 1px 3px 1, 0 1px 2px 1;
    }
    .test-AnkiCard-Button:hover {
      background-color: #f5f5f5;
    }
    .test-AnkiCard-Button:active {
      background-color: #e0e0e0;
      box-shadow: 0 3px 6px 1, 0 3px 6px 1;
    }
    .test-AnkiCard-Button:active:focus {
      outline: 0 none;
    }
    .test-AnkiCard-Button:disabled {
      color: var(--color-bb);
      cursor: not-allowed;
      pointer-events: none;
      box-shadow: none;
      text-shadow: none;
    }

---
title: Fixing the Width
date: 2016-03-10
draft: true
math: true
category: blog
tags:
    - jekyll
    - yaml
    - liquid-templates
    - markdown
    - html
    - css
    - git
    - mathjax
    - bundler
---
What an ugly, fragile blog.
<!--more-->

All I wanted to do was make the page a little wider. Suddenly the widths of the left and right columns were varying in size depending on content. Headings were crazy sizes. Both headings and paragraphs had awkward line spacing. While syntax highlighting is a great feature, poor color choices make code very hard to read. It was a mess.

I spend a lot of time trying to figure out what was going wrong. One of the problems was using `flex-grow: 1;` for the left column and `width: auto;` on the right. These settings left too many decisions up to the browser. I now calculate the column widths and margins based on the width of the whole body. The code also floats the two columns to the left and right, respectively. It may not be the best solution, but it will do until I learn how to responsive grid systems work.

I also got rid jQuery and some other JavaScript. It was a holdover from another website I created a while ago. The only JavaScript remaining is for MathJax, which I plan to use for - what else? - math!

\[
    \begin{bmatrix}
      a & b & c & d \\\\\
      e & f & g & h \\\\\
      i & j & k & l \\\\\
      m & n & o & p
    \end{bmatrix}
    \times
    \begin{bmatrix}
      x \\\\\
      y \\\\\
      z \\\\\
      w
    \end{bmatrix}
    =
    \begin{bmatrix}
      ax + by + cz +dw  \\\\\
      ex + fy + gz + hw \\\\\
      ix + jy + kz +lw  \\\\\
      mx + ny + oz + pw
    \end{bmatrix}
\]

This blog is still quite ugly, but I'm feeling better about it after putting in a couple of days work to make the width behave the way I want it to. Now to learn more about layout design, typography, Sass, CSS and how best to put to use semantic HTML5 tags, like  `<main>`, `<aside>`, `<header>` and others.

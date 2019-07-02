---
title: Designing My Blog
date: 2016-03-07
draft: true
categories: design
tags: [blog, inspiration]
---

Thoughts and inspirations to be used toward designing my blog.
<!--more-->

## New Inspiration
I looked at a Jekyll theme called [hyde](https://github.com/JuanjoSalvador/hyde). It has several simplifications I like, so I'm going to try to pull in some of its CSS/SCSS to my notes and my blog. As I do that, I will keep in mind the four principles of design from Robin William's book, The Non-Designer's Design Book:

- Contrast
- Repetition
- Alignment
- Proximity

One of the things wrong with my current design is the content stays centered on the browser. I will left align the entire page. I also want to put my sidebar on the left. However, it currently contains the yearly index. The Hyde theme pushes it's left sidebar up above the main content. I think I want my sidebar to drop to the end as it does now. The index can happily drop to the end, I think. I'd only have the sidebar pop up to the top if I changed its purpose. I'd still have to find a place for an index. I consider it valuable for navigating my notes. Maybe a menu link. I'll have to think about it.

## Inspirations for the Overall Layout and Design
The [Modern Studio Pro](http://my.studiopress.com/themes/modern-studio/#demo-full) theme for wordpress uses a 300x300 px logo. The logo, heading and navigation bar look good for this theme. I also like the layout of the left sidebar. It has blocks with nice headings for About Me, Connect, Newletter, Recent Posts, Instagram, or whatever you want to put down the column.

On the other hand, I like the footer of [Eleven40 Pro](http://my.studiopress.com/themes/eleven40/#demo-full), as well as being able to place an image to the left, right or on top of a post. The footer has large three sections across the majority of its space:

- Recent Posts containing a list of the six most recent posts.
- About with a short, three sentence description.
- Tag and Social Icons are stacked in the third column.

There's a second row that spans all three columns with a copyright statement and links to social network sites. The demo includes Dribbble, Facebook, Google+, Instagram, Twitter and Contact, the last of which could be a link to another page, or just to `mail://myemailaddress@example.com`.

I extracted the following CSS from the Modern Studio theme, because I'm curious about the Unicode values. These are not valid Unicode characters. For example [FileFormat.info](http://www.fileformat.info/index.htm) shows ["\e915"](http://www.fileformat.info/info/unicode/char/e915/index.htm) as invalid. In fact, the range [from U+E000 to U+F8FF](http://www.fileformat.info/info/unicode/block/private_use_area/index.htm) is designated as the 'Private Use Area'.

```css
.icon-logo-genesis:before {
  content: "\e914";
}
.icon-logo-rm:before {
  content: "\e915";
}
.icon-logo-sp-outline:before,
.icon-StudioPress:before {
  content: "\e916";
}
.icon-logo-sp:before {
  content: "\e917";
}
.icon-logo-wp:before {
  content: "\e918";
}

// FYI: logo.png is a 300x300 px image
.logo {
  background: url(images/logo.png) no-repeat;
  display: block;
  height: 16px;
}
```

## Inspiration for Logos and Icons
I want an icon that portrays the concepts of dreaming, sketching and coding. It should fit in a 300x300 pixel image. I'm thinking of a sketch of a pencil and pad of paper, where the sketch on the paper includes the moon and stars (dreaming) and several lines of colored bars so the colors look like syntax highlighted lines of source code.

- [The Making of an Icon](http://www.pixelresort.com/blog/the-making-of-an-icon/).
- [Inspirational Examples of Icon Sketching](http://speckyboy.com/2013/09/18/icon-sketching/)
- [Hand Drawn Sketch Icon Set](http://www.webiconset.com/hand-drawn-sketch-icon-set/).
- [User Interface Designs](http://userinterfacedesigns.blogspot.com/2010_10_01_archive.html) contains several sheets of sample icons.
- [100+ Sketch Style Free Vector Icons](http://graphicdesignjunction.com/2013/12/line-style-free-vector-icons/).
- [Icon Design: A Showcase of Sketched Vs. Ready](http://www.hongkiat.com/blog/sketched-final-icon-design/).

Icons should come in several standard sizes. The standard sizes are all square, but are different depending on the particular operating system:

|         |         |          |       |       |       |           |   Windows  |
| OS/Size | Windows | Mac OS X | Linux | iOS 6 | iOS 8 | Android L |    Phone   |
|--------:|:-------:|:--------:|:-----:|:-----:|:-----:|:---------:|:----------:|
| 1024    |         |    x     |       |   x   |   x   |           |            |
|  512    |         |    x     |       |       |       |     x     |            |
|  256    |    x    |    x     |       |       |       |           |            |
|  200    |         |          |       |       |       |           |      x     |
|  192    |         |          |       |       |       |     x     |            |
|  180    |         |          |       |       |   x   |           |            |
|  173    |         |          |       |       |       |           |      x     |
|  152    |         |          |       |       |   x   |           |            |
|  144    |         |          |       |   x   |       |           |            |
|  128    |         |     x    |       |       |       |           |            |
|  120    |         |          |       |       |   x   |           |            |
|  114    |         |          |       |   x   |       |           |            |
|  100    |         |          |       |   x   |       |           |            |
|   99    |         |          |       |       |       |           |      x     |
|   96    |         |          |   x   |       |       |           |            |
|   80    |         |          |       |       |   x   |           |            |
|   76    |         |          |       |       |   x   |           |            |
|   72    |         |          |       |   x   |       |           |            |
|   64    |         |     x    |       |       |       |           |            |
|   62    |         |          |       |       |       |           |      x     |
|   60    |         |          |       |       |   x   |           |            |
|   58    |         |          |       |   x   |   x   |           |            |
|   57    |         |          |       |   x   |       |           |            |
|   50    |         |          |       |   x   |       |           |            |
|   48    |    x    |          |   x   |       |       |     x     |            |
|   40    |         |          |       |       |   x   |           |            |
|   32    |    x    |     x    |       |       |       |           |            |
|   29    |         |          |       |   x   |   x   |           |            |
|   24    |    x    |          |   x   |       |       |     x     |            |
|   16    |    x    |     x    |   x   |       |       |           |            |

## Other Resources
- [Basic Guidelines to Product Sketching](http://www.hongkiat.com/blog/basic-guidelines-to-product-sketching/)

---
"2026":
  - "03"
title: Three-Color Design Principle
date: 2026-03-19T00:00:00-05:00
years:
  - "2026"
tags:
  - blog
  - design
weight: 10
---
The 3 color rule is a guideline for choosing colors when designing websites. It states that for visual harmony, websites should contain no more than 3 main colors. This color palette typically consists of a dominant color, secondary color, and an accent color. [This site](https://www.colorwithleo.com/what-is-3-color-rule/) suggests that the dominant color should cover about 60% of the visual space, the secondary color should cover about 30%, and an accent color covers the remaining 10%.

I read somewhere that each category can be a family of related tones rather than a single literal color. That's what I'm going with, because stridently adhering to only three colors is too harsh.

<!--more-->
{{< table_of_contents >}}

## The Victorian Newspaper Palette

This blog's palette is intended to evoke a Victorian newspaper aesthetic. It uses cream paper, black ink, and a colored accent for interaction and decoration.

### Dominant: Warm Victorian Cream

Claude Code helped me develop this theme. After a lot of back and forth, I decided that this set of colors looked good to represent a family of aged-newsprint tones:

| Color             | Hex       | Used For                       |
| ----------------- | --------- | ------------------------------ |
| Warm cream        | `#ebe8e0` | Body background                |
| Lighter cream     | `#f5f5f0` | Main content area, masthead    |
| Gradient base     | `#f0f0eb` | Sidebar headers, nav gradients |
| Tag/badge surface | `#e8e5dd` | Victorian tags, date badges    |
| Code blocks       | `#e2ded7` | Pre/code backgrounds           |

### Secondary: Printer's Ink

A range of near-blacks and dark grays handles all structural elements:

- `#000`, `#1a1a1a`, `#222`: headings, titles
- `#333`, `#2a2a2a`: navigation links, borders, rules, ornaments
- `#444`, `#555`, `#666`: subdued metadata, dates, decorative separators

### Accent: Blue with Warm Rust Complement

The blue family (`#24599d`, `#2f75cc`, `#193e6d`) handles all interactive elements (links and active navigation states).

A warm amber/rust family (`#a36b25`, `#cc862f`, `#a32c25`) serves as a decorative complement for hover states and drop caps. Being roughly complementary to blue on the color wheel, these two work as a coherent accent pair rather than a fourth independent color role (at least, that's my excuse for using another color).

#### Why Blue?

It looks good. I could spend days playing with color wheels like [this one](https://color.adobe.com/create/color-wheel) from Adobe, and never settling on a set of colors. It was much easier to ask Claude for a set of colors and telling it whether I wanted something darker or lighter until it looked good to me. It made sure that the color had sufficient contrast that text remained readable.

FWIW, Claude justified it's choice by saying that the dominant cream sits around 36–40° on the color wheel. Its complement is roughly 210–220°, which lands squarely in blue. Blue ink on warm parchment has 500 years of history behind it for exactly this reason. I'm just not that into color theory.

#### Syntax Highlighting Constraint

Monokai, used for syntax highlighting uses bright cyan for keywords and bright violet for literals. Both candidate zones for an alternative accent color. The current blue (`#24599d`) sits in the best available gap: darker and less saturated than those tokens, and further disambiguated by context (prose vs. code block).

## Tables and Blockquotes

The blue accent was originally overused on structural surfaces. These were replaced with warm parchment tones to keep blue exclusively for interactive elements:

| Element               | Hex       | Notes                                 |
| --------------------- | --------- | ------------------------------------- |
| Table headers/footers | `#4a3a16` | Dark warm amber; cream text at 9.18:1 |
| Table odd rows        | `#f7f2e6` | Light parchment; black text ~18:1     |
| Table even rows       | `#e8d9bc` | Medium parchment; black text ~14:1    |
| Blockquotes           | `#f0e6d0` | Warm parchment; black text ~15:1      |

The blockquote parchment (`#f0e6d0`) is the midpoint of a three-step warm amber family spanning table headers through body rows.

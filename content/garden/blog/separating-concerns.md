---
title: "Separating Presentation from Layout"
date: 2024-01-14T08:24:59-05:00
years: ["2024"]
tags: [blog]
weight: 10
---
I want to separate the presentation of my blog from the content so, with any luck, I can create a theme and possibly substitute a more professionally-designed theme for the one I've hacked together. I first need to better understand the structure of what I've wrought here before I can reasonably refactor it, or do any major overhaul.
<!--more-->
{{< table_of_contents >}}

I asked ChatGPT to recommend a method for documenting the various aspects of my blog, including the HTML layout, partials, shortcodes, and CSS that currently exist. It replied with the following method that I'm adapting to my needs.

## 1 Markdown Documentation

- [x] Create a new projects directory for documentation.
- [x] Inside projects, create markdown files for each aspect I want to document (HTML layout, partials, shortcodes, CSS).
- [ ] Use clear headings and subheadings to organize information. This is an ongoing process. I guess it will be done when I'm satisfied with steps 2–5.

## 2 HTML Layout

- [ ] Describe the overall structure of this site's HTML layout.
- [ ] Include details about the main layout file and any custom layouts for different sections or content types.
- [ ] Mention Hugo variables and functions used in the HTML files.

## 3 Partials

- [ ] List and describe each partial used.
- [ ] Explain where these partials are included and how they contribute to the overall layout.

## 4 Shortcodes

- [ ] Document the shortcodes I've created or are using in my content.
- [ ] Provide examples of shortcode usage and explain their purpose.

## 5 CSS

- [ ] Detail the structure of my CSS files.
- [ ] I haven't used a preprocessor like Sass, but if I did I'd want to document the file structure and how styles are organized.
- [ ] Include information about any third-party libraries or frameworks (e.g., MathJax).

## 6 Theme Creation

- [ ] Outline the steps to create a theme based on my current documentation.
- [ ] Include guidelines on how to separate presentation from content.
- [ ] Suggest best practices for theming in Hugo.

## 7 Professional Theme Integration

- [ ] Research and choose a professionally created Hugo theme that aligns with my design preferences.
- [ ] Document the steps to integrate the new theme into this site.
- [ ] Provide instructions for customizing the theme according to my needs.

## 8 Version Control

- [ ] Use version control.
- [ ] Keep the documentation up-to-date as this site evolves.

## 9 Include Examples and Screenshots

- [ ] Add examples of code snippets, shortcode usage, and screenshots of my site to make the documentation more visual and user-friendly.

## 10 Test the Documentation

- [ ] After creating the documentation, test it by having someone else follow the steps to ensure clarity and completeness.

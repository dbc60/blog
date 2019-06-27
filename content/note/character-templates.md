---
title: Character Templates
date: 2016-03-07
draft: true
categories: blog
tags: [writing, characters]
---

Wikipedia has [tables called infoboxes](https://en.wikipedia.org/wiki/Help:Infobox) which are designed to present a summary of some unifying aspect that articles share. It turns out there are [templates](https://en.wikipedia.org/wiki/Wikipedia:List_of_infoboxes) for lots of different kinds of infoboxes, including [fictional characters](https://en.wikipedia.org/wiki/Template:Infobox_character).
<!--more-->

It seems to me these are ready-made tools for creating a log or database of characters and their traits for a story or metaverse.

Here is a template based on the Wikipedia infobox for fictional characters.
<!-- need to escape the liquid template mark-up by defining a liquid template variable and then
     displaying the value of that variable. -->
{% assign infobox-character-template = '
{{Infobox character
| name             = Character name
| series           = Name of the television series, fictional world or story in which character appears
| image            = Image of the character.
| image_size       =
| alt              = Alt text
| caption          = Caption to display below image
| first            = First appearance of the character
| last             = Last appearance of the character
| creator          = Name of the person who invented the character
| fullname         =
| nickname         =
| alias            = Any aliases used by the character
| species          =
| gender           =
| occupation       =
| affiliation      =
| title            =
| family           =
| spouse           =
| significantother =
| children         =
| relatives        =
| religion         =
| nationality      =
}}
' %}

```
{{ infobox-character-template }}
```

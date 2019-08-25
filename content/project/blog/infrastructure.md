---
title: "Infrastructure"
date: 2019-07-12T07:19:16-04:00
draft: true
categories: design
tags: [blog]
---

My goal is to minimize the amount of change to content (markdown and reStructuredText) and layout files (HTML) any time I want to change the presentation of this blog. For example, if I want to change from a single column format to two columns. I think it will help to have a clear description of the directory heirarchy, file naming convention, and guidelines for organizing content, structure, and presentation assets.
<!--more-->

## File Naming Convention

Right now, I'm leaning toward using an Atomic Design prefix - atom (`a`), molecule (`m`), and organism (`o`) follwed by a BEM-like naming convention for files. However, instead of using a hyphen between words of block, element, or modifier, I will follow the recommendation of Daniel Tonon [^1] who makes a good case for camel case (camelCase) names. Elements will be separated from blocks by a double underscore (`__`) and modifiers will be separated from blocks and elements by a double hyphen (`--`).

The Atomic Design prefixes relate to the relative sizes of components, and whether a component is a parent to other. The size comes down to how much HTML a component is made from. For instance,

- one to a few HTML tags (e.g., a form label, an input, or a button) is likely to be an atom. Remember that an atom can also be a more abstract element, like a color palette, a font, or an animation.
- three to ten lines of HTML is likely a molecule. Molecules are groups of atoms bonded together and are the smallest fundamental units of a compound. These molecules take on their own properties and serve as the backbone of our design systems. For example, a form label, input or button aren’t too useful by themselves, but combine them together as a form and now they can actually do something together.
- any more is likely to be an organism. Molecules give us some building blocks to work with, and we can now combine them together to form organisms. Organisms are groups of molecules joined together to form a relatively complex, distinct section of an interface.

Atomic Design also talks about templates and pages. Templates consist mostly of groups of organisms stitched together to form pages. It’s here where we start to see the design coming together and start seeing things like layout in action. The first three categories are part of the author's chemistry analogy. Templates is where we leave behind the idea of a periodic table.

Pages are specific instances of templates. Here, placeholder content is replaced with real representative content to give an accurate depiction of what a user will ultimately see.

## Resources

[^1]: [ABEM A More Useful Adaptation of BEM](https://css-tricks.com/abem-useful-adaptation-bem/)

- [BEM Mixins](https://css-tricks.com/snippets/sass/bem-mixins/)
- [BEM and Atomic Design](https://www.lullabot.com/articles/bem-atomic-design-a-css-architecture-worth-loving)
- [Atomic Design](http://bradfrost.com/blog/post/atomic-web-design/)
- [Element Collages](http://v3.danielmall.com/articles/rif-element-collages/)
- [How to Section Your HTML](https://css-tricks.com/how-to-section-your-html/)
- [Mock up Page Layout for Sectioning Your HTML](https://codepen.io/aardrian/pen/BgQqrQ)

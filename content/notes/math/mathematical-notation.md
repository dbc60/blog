+++
title = "Math Notes"
date = 2019-04-08T10:32:30-05:00
draft = true
math = true

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["math"]
categories = ["math"]
+++

## Using MathJax in a Web Page

The first thing that must be done is to include the following script somewhere before the `</body>` tag:

```html
<!-- Load MathJax -->
<script async type="text/javascript"
  src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async>
</script>
```

## Mathematical Notation

The phrase "There exists an or $x$, element of $X$, such that
predicate $P(x)$ holds (i.e., is true)" can be written in a few ways.
Note that either $:$, '$\ni$', or '$\text{s.t.}$' can be
used to represent "such that", and that they are optional:

* shortest: $\exists{x} \in X(P(x))$
* with '$\ni$': $\exists{x} \in X \ni P(x)$
* with '$:$': $\exists{x} \in X : P(x)$
* with '$\text{s.t.}$': $\exists{x} \in X\ \text{s.t.}\  P(x)$
* an explicit version: $\exists{x}(x \in X \land P(x))$
* fully parenthesized and explicit: $(\exists{x})(x \in X \land P(x))$

Here are some square symbols defined in MathJax. See [MathJax supported
commands](http://docs.mathjax.org/en/latest/tex.html#supported-latex-commands)
or [TeX commands available in MathJax](http://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm)
for more details.


$$\begin{array}{l c l}\hline \text{Command} & \text{Symbol}  & \text{Package} \\\ \hline & & \\\ \text{\square} & \square & \text{amssymb} \\\ \text{\blacksquare} & \blacksquare   & \text{amssymb} \\\ \text{\Box} & \Box & \text{amssymb} \\\ \text{\boxminus} & \boxminus & \text{amssymb} \\\ \text{\boxplus} & \boxplus & \text{amssymb} \\\ \text{\boxtimes} & \boxtimes & \text{amssymb} \\\ \hline \end{array}$$

And an equation with an underbrace:

`$${\bf I_n} = \underbrace{\left(\sqrt{2}+\sqrt{3}\right)^2 \}$$`

$${\bf I_n} = \underbrace{\left(\sqrt{2}+\sqrt{3}\right)^2 \}$$

`\\[{\bf I_n} = \underbrace{\left(\sqrt{2}+\sqrt{3}\right)^2 \}\\]`

\\[{\bf I_n} = \underbrace{\left(\sqrt{2}+\sqrt{3}\right)^2 \}\\]

An empty array with an underbrace and a right brace:

\\[{\bf I_n} = \underbrace{\left.\left(\vphantom{\begin{array}{c}1\\\1\\\1\\\1\\\1\end{array}}\right) \right\\} }\\]

An array:

\\[{\bf I_n} = \begin{array}{ccccc} 1&0&0&\cdots &0\\\ 0&1&0&\cdots &0\\\ 0&0&1&\cdots &0\\\ \vdots&&&\ddots&\\\ 0&0&0&\cdots &1 \end{array}\\]

An array wrapped in parentheses:

\\[{\bf I_n} = \left(\begin{array}{ccccc} 1&0&0&\cdots &0\\\ 0&1&0&\cdots &0\\\ 0&0&1&\cdots &0\\\ \vdots&&&\ddots&\\\ 0&0&0&\cdots &1 \end{array}\right)\\]

A vphantom array wrapped in parentheses:

\\[{\bf I_n} = \left(\vphantom{\begin{array}{c}1\\\1\\\1\\\1\\\1\end{array}} \begin{array}{ccccc} 1&0&0&\cdots &0\\\ 0&1&0&\cdots &0\\\ 0&0&1&\cdots &0\\\ \vdots&&&\ddots&\\\ 0&0&0&\cdots &1 \end{array}\right)\\]

A vphantom array followed by an underbraced array:

\\[{\bf I_n} = \left(\vphantom{\begin{array}{c}1\\\1\\\1\\\1\\\1\end{array}} \underbrace{ \begin{array}{ccccc} 1&0&0&\cdots &0\\\ 0&1&0&\cdots &0\\\ 0&0&1&\cdots &0\\\ \vdots&&&\ddots&\\\ 0&0&0&\cdots &1 \end{array} } \right)\\]<br>

A vphantom array followed by an underbraced array with a right brace (have to add both `\left.` and `\right\\}`):

\\[{\bf I_n} = \left.\left(\vphantom{\begin{array}{c}1\\\1\\\1\\\1\\\1\end{array}} \underbrace{ \begin{array}{ccccc} 1&0&0&\cdots &0\\\ 0&1&0&\cdots &0\\\ 0&0&1&\cdots &0\\\ \vdots&&&\ddots&\\\ 0&0&0&\cdots &1 \end{array} } \right) \right\\}\\]<br>

Add row label:

\\[{\bf I_n} = \left.\left(\vphantom{\begin{array}{c}1\\\1\\\1\\\1\\\1\end{array}} \underbrace{ \begin{array}{ccccc} 1&0&0&\cdots &0\\\ 0&1&0&\cdots &0\\\ 0&0&1&\cdots &0\\\ \vdots&&&\ddots&\\\ 0&0&0&\cdots &1 \end{array} } \right) \right\\}\,n\text{ rows}\\]<br>

Smash inner matrix:

\\[{\bf I_n} = \left.\left(\vphantom{\begin{array}{c}1\\\1\\\1\\\1\\\1\end{array}} \smash{\underbrace{ \begin{array}{ccccc} 1&0&0&\cdots &0\\\ 0&1&0&\cdots &0\\\ 0&0&1&\cdots &0\\\ \vdots&&&\ddots&\\\ 0&0&0&\cdots &1 \end{array} } } \right) \right\\}\,n\text{ rows}\\]<br>

Finally, put in a column label

\\[{\bf I_n} = \left.\left(\vphantom{\begin{array}{c}1\\\1\\\1\\\1\\\1\end{array}} \smash{\underbrace{ \begin{array}{ccccc} 1&0&0&\cdots &0\\\ 0&1&0&\cdots &0\\\ 0&0&1&\cdots &0\\\ \vdots&&&\ddots&\\\ 0&0&0&\cdots &1 \end{array}}\_{n\text{ columns}}} \right) \right\\}\,n\text{ rows}\\]<br>

The column label was the hardest part. I couldn't just add `_{n\text{ columns}}`. I had to replace the `$$` wrappers with `\\[` and `\\]` and escape the underscore (`\_{n\text{ columns}}`). Also, a `<br>` had to be added so this paragraph wouldn't overwrite "$n\ \text{columns}$". For whatever reason, there's not enough space between the end of an equation and the first line of plain text.

The rules of writing \\(\LaTeX\\) with the current markdown parser, and whatever settings are used in this theme seem to be:

* display math: wrap code in `\\[`, `\\]` pairs
* inline math: wrap code in `\\(`, `\\)` or `$`,`$` pairs (the latter might have issues with subscripts)
* escape end-of-line (`\\`) in arrays with one backslash (`\\\`)
* escape the underscore for a subscript with a backslash (`_` becomes `\_`)
* The escaped braces, such as `\left\{` and `\right\}` used when they have to be sized dynamically, have to be escaped with an additional backslash: `\left\\{` and `\right\\}`

Here are a pair of (dynamically-sized) braces \\(\left\\{\right\\}\\) inlined with this sentence. Right clicking on it and selecting "Show Math As" -> "TeX Commands" from the pop-up menu will show `\left\{\right\}`, but the actual text is `\\(\left\\{\right\\}\\)`.

# Reference

* [A Survey of Math Syntax in Markdown](https://github.com/cben/mathdown/wiki/math-in-markdown)

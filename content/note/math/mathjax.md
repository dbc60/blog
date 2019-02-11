+++
title = "MathJax and Markdown"
date = 2019-04-08T10:32:30-05:00
draft = true
math = true
tags = ["mathjax", "math"]
categories = ["mathjax"]
+++

Here are some notes on using MathJax and Markdown to create pages with really beautiful equations.

<!--more-->

## Using MathJax in a Web Page

The first thing that must be done is to include a couple of scripts somewhere before the `</body>` tag. The first one is optional. It will configure MathJax to automatically number equations on a page. The second script loads MathJax from Cloudflare. If the first is included, it must precede the second.

```html
<!-- Configure MathJax for automatic equation numbering. See
   http://docs.mathjax.org/en/latest/tex.html#automatic-equation-numbering
   for details
-->
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<!-- Load MathJax -->
<script async type="text/javascript"
  src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async>
</script>
```

## MathJax Caveats

With any luck, you can see the \\(\LaTeX\\) commands for any of the examples below you by right clicking on it and selecting "Show Math As" -> "\\(\TeX\\) Commands" from the pop-up menu. The original markdown code required a lot of extra backslashes to escape the ones in the \\(\LaTeX\\) code. The general rules are:

* display math: wrap code in `\\[`, `\\]` pairs
* inline math: wrap code in `\\(`, `\\)` pairs
* escape array end-of-row markers, `\\` with three backslashes: `\\\\\`
* escape the underscore for a subscript with a backslash (`_` becomes `\_`)
* The escaped the backslashes in dynamically-sized braces, so `\left\{` and `\right\}` become `\left\\{` and `\right\\}`, respectively.

## MathJax Examples

The phrase "There exists an \\(x\\), element of \\(X\\), such that
predicate \\(P(x)\\) holds (i.e., is true)" can be written in a few ways.
Note that "such that" can be represented by any of these notations: \\(:\\), \\(\ni\\), or \\(\text{s.t.}\\), and that they are optional:

* shortest: \\(\exists{x} \in X(P(x))\\)
* with \\(\ni\\): \\(\exists{x} \in X \ni P(x)\\)
* with \\(:\\): \\(\exists{x} \in X : P(x)\\)
* with \\(\text{s.t.}\\): \\(\exists{x} \in X\ \text{s.t.}\  P(x)\\)
* an explicit version: \\(\exists{x}(x \in X \land P(x))\\)
* fully parenthesized and explicit: \\((\exists{x})(x \in X \land P(x))\\)

Here are some square symbols defined in MathJax. See [MathJax supported
commands](http://docs.mathjax.org/en/latest/tex.html#supported-latex-commands)
or [TeX commands available in MathJax](http://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm)
for more details.

\\[
  \begin{array}{l c l}
    \hline
    \text{Command} & \text{Symbol}  & \text{Package} \\\\\
    \hline
    \text{\square} & \square & \text{amssymb} \\\\\
    \text{\blacksquare} & \blacksquare   & \text{amssymb} \\\\\
    \text{\Box} & \Box & \text{amssymb} \\\\\
    \text{\boxminus} & \boxminus & \text{amssymb} \\\\\
    \text{\boxplus} & \boxplus & \text{amssymb} \\\\\
    \text{\boxtimes} & \boxtimes & \text{amssymb} \\\\\
    \hline
  \end{array}
\\]

And an equation with an underbrace:

\\[
  \begin{equation}
  {\bf I_n} = \underbrace{\left(\sqrt{2}+\sqrt{3}\right)^2 \}
  \end{equation}
\\]

An empty array surounded by dynamically-size parentheses, an underbrace, and a right brace:

\\[
  \begin{equation}
  {\bf I_n} =
  \underbrace{
    \left.
    \left(
    \begin{array}{}
    \end{array}
    \right)
    \right\\}
  }
  \end{equation}
\\]

Here's a simple array.

\\[
  \begin{equation}
  {\bf I_n} =
  \begin{array}{ccccc}
    1               &      0 &      0 & \cdots & 0 \\\\\
    0               &      1 &      0 & \cdots & 0 \\\\\
    0               &      0 &      1 & \cdots & 0 \\\\\
    \vdots & \vdots & \vdots & \ddots \\\\\
    0      &        0        &      0 & \cdots & 1
  \end{array}
  \end{equation}
\\]

Let's wrap it in parentheses.

\\[
  \begin{equation}
  {\bf I_n} =
  \left(
  \begin{array}{ccccc}
    1               &      0 &      0 & \cdots & 0 \\\\\
    0               &      1 &      0 & \cdots & 0 \\\\\
    0               &      0 &      1 & \cdots & 0 \\\\\
    \vdots & \vdots & \vdots & \ddots \\\\\
    0      &        0        &      0 & \cdots & 1
  \end{array}
  \right)
  \label{eq:wrapped}
  \end{equation}
\\]

Add a right brace and an underbrace.

\\[
  \begin{equation}
  {\bf I_n} =
  \underbrace{
    \left.
    \left(
    \begin{array}{ccccc}
      1               &      0 &      0 & \cdots & 0 \\\\\
      0               &      1 &      0 & \cdots & 0 \\\\\
      0               &      0 &      1 & \cdots & 0 \\\\\
      \vdots & \vdots & \vdots & \ddots \\\\\
      0      &        0        &      0 & \cdots & 1
    \end{array}
    \right)
    \right\\}
  }
  \end{equation}
\\]

Note how the underbrace envelopes the parentheses and the right brace. It would look better if it was restricted to the columns of the array. To fix that, we first need to add a vphantom array inside the parentheses.

\\[
  \begin{equation}
  {\bf I_n} =
  \left.
  \left(
  \vphantom{
    \begin{array}{c}
      1 \\\\\
      1 \\\\\
      1 \\\\\
      1 \\\\\
      1
    \end{array}
  }
  \underbrace{
    \begin{array}{ccccc}
      1               &      0 &      0 & \cdots & 0 \\\\\
      0               &      1 &      0 & \cdots & 0 \\\\\
      0               &      0 &      1 & \cdots & 0 \\\\\
      \vdots & \vdots & \vdots & \ddots \\\\\
      0      &        0        &      0 & \cdots & 1
    \end{array}
  }
  \right)
  \right\\}
  \end{equation}
\\]

That looks better, but it's still not quite right. The parentheses are supposed to delineate the array, but they're wrapping the underbrace and are taller than the right brace. Let's add labels to the braces to exagerate the problem.

\\[
  \begin{equation}
  {\bf I_n} =
  \left.
  \left(
    \vphantom{
      \begin{array}{c}
        1 \\\\\
        1 \\\\\
        1 \\\\\
        1 \\\\\
        1
      \end{array}
    }
    \underbrace{
      \begin{array}{ccccc}
        1               &      0 &      0 & \cdots & 0 \\\\\
        0               &      1 &      0 & \cdots & 0 \\\\\
        0               &      0 &      1 & \cdots & 0 \\\\\
        \vdots & \vdots & \vdots & \ddots \\\\\
        0      &        0        &      0 & \cdots & 1
      \end{array}
    }\_{n\text{ columns}}
    \right)
  \right\\}\,n\text{ rows}
  \end{equation}
\\]

Using the `\smash` command we can set the vertical space of the box containing the array and underbrace to zero. This will resize the parentheses to be closer to what we intended.

\\[
  \begin{equation}
  {\bf I_n} =
  \left.
  \left(
  \vphantom{
    \begin{array}{c}
      1 \\\\\
      1 \\\\\
      1 \\\\\
      1 \\\\\
      1
    \end{array}
  }
  \smash{
    \underbrace{
      \begin{array}{ccccc}
        1               &      0 &      0 & \cdots & 0 \\\\\
        0               &      1 &      0 & \cdots & 0 \\\\\
        0               &      0 &      1 & \cdots & 0 \\\\\
        \vdots & \vdots & \vdots & \ddots \\\\\
        0      &        0        &      0 & \cdots & 1
      \end{array}
    }\_{n\text{ columns}}
  }
  \right)
  \right\\}\,n\text{ rows}
  \end{equation}
\\]
<br>

Finally, I'm going to add one more row to the vphantom array for aesthics. It will stretch the parentheses just a little bit more, so the equation looks more like the one in \\(\eqref{eq:wrapped}\\) above.

\\[
  \begin{equation}
  {\bf I_n} =
  \left.
  \left(
  \vphantom{
    \begin{array}{c}
      1 \\\\\
      1 \\\\\
      1 \\\\\
      1 \\\\\
      1 \\\\\
      1
    \end{array}
  }
  \smash{
    \underbrace{
      \begin{array}{ccccc}
        1               &      0 &      0 & \cdots & 0 \\\\\
        0               &      1 &      0 & \cdots & 0 \\\\\
        0               &      0 &      1 & \cdots & 0 \\\\\
        \vdots & \vdots & \vdots & \ddots \\\\\
        0      &        0        &      0 & \cdots & 1
      \end{array}
    }\_{n\text{ columns}}
  }
  \right)
  \right\\}\,n\text{ rows}
  \end{equation}
\\]
<br>


Now that I've learned more about the interactions between Markdown and \\(\LaTeX\\), I must say \\(\LaTeX\\) should be wrapped in `\\[` and `\\]` for math blocks (display math) and pairs of `\\(` and `\\)` for inline math. Do not use `$$` for display math nor `$` wrappers for inline math. It just doesn't work so well. Also, subscripting requires the underscore to be escaped (`\_{n\text{ columns}}`). Lastly, sometimes a `<br>` is needed to separate the end of an equation from the next paragraph of text. In examples above, smashing vertical space is probably the cause.

# Reference

* [A Survey of Math Syntax in Markdown](https://github.com/cben/mathdown/wiki/math-in-markdown)
* [Automatic Equation Numbering](http://docs.mathjax.org/en/latest/tex.html#automatic-equation-numbering) in MathJax

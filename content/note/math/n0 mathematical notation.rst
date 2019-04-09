---
title: Mathematical Notation
date: 2019-04-08T09:57:48-04:00
draft: true
categories: math
math: true
---

These are examples of mathematical notation taken from a talk on `Post's
Theorem and Blockchain Languages <https://www.youtube.com/watch?
=TGE6jrVmt_I>`_, where the speaker was kind enough to clearly read the
equation. These are equations where I was uncertain of the notation, their
meaning, and how to *read* them.

* :math:`P:(State, Transaction) \to Bool`: :math:`P` is a predicate that is
  some function of a State and a Transaction we would like to apply to that
  state. The predicate returns **true** or **false**, as to whether that
  transaction will be allowed to act on the state.
* :math:`F:(State, Inputs) \to Transaction`: A function :math:`F` which takes
  some input and the current state, and produces a Transaction.
* \\(P(s, (i, t)) := F(s, i) \stackrel{?}{=} t\\): predicate :math:`P` with
  arguments state :math:`s` and a transaction object :math:`(i, t)`, where
  :math:`i` is some input and :math:`t` is a transaction, is defined as the
  result of a function :math:`F` whose arguments are the state :math:`s` and
  input :math:`i` compared to the original transaction :math:`t`. So, the
  predicate :math:`P` is **true** if the function :math:`F` produces the
  original transaction :math:`t` from the :math:`s` and :math:`i`.
* :math:`\mathbb{N}`: the set of natural numbers (:math:`\mathbb{N} = \lbrace 0
  1, 2, 3, \ldots \rbrace`).
* Connectives: :math:`p \land q`, :math:`p \lor q`, :math:`p \implies q`,
  :math:`\lnot p`. These are read as conjunction ("p and q"), disjunction ("p or
  q", implication (p implies q), and negation (not p).
* Bound Quantifiers: :math:`\exists x < t.p`, :math:`\forall x < t.p`. These
  are read as There exists some :math:`x` less than some term :math:`t` such
  that predicate :math:`p` holds, and For all :math:`x` less than some term
  :math:`t` such that predicate :math:`p` holds.
* Unbound Quantifiers:

  * :math:`\exists x \in \mathbb{N}.p`: There exists some :math:`x` in the set
    of natural numbers such that predicate :math:`p` holds.
  * :math:`\forall x \in \mathbb{N}.p`: For all :math:`x` in the set of natural
    numbers, predicate :math:`p` holds.

* :math:`\forall x < z. \exists y < z.x + y = z`: For all :math:`x` less than
  something (:math:`z`), there exists :math:`y` less than something* (:math:`z`
  , such that :math:`x + y = z`.
* :math:`\exists x \in \mathbb{N}.p`: There exists an :math:`x` in
  :math:`\mathbb{N}` such that predicate :math:`p` holds.
* :math:`\exists x \in \mathbb{N}.\forall y < z.x + y = z`: There exists an
  :math:`x` in :math:`\mathbb{N}` such that for all :math:`y < z`, such that the
  relation :math:`x + y = z` holds.

By the way, use ``\ldots`` for an ellipsis. It ensures the dots are correctly
placed for a *typographical ellipsis*.

Sets and Predicate Logic Notation
*********************************

Predicate logic extends propositional logic with two quantifiers:

.. math::

  \begin{align*}    \forall && \text{universal quantification (for all)} \\    \exists && \text{existential quantification (there exists)}  \end{align*}

The phrase "There exists an :math:`x`, element of :math:`X`, such that
predicate :math:`P(x)` holds (i.e., is true)" can be written in a few ways.
Note that either ':math:`:`', ':math:`\ni`', or ':math:`\text{s.t.}`' can be
used to represent "such that", and that they are optional:

* shortest: :math:`\exists{x} \in X(P(x))`
* with ':math:`\ni`': :math:`\exists{x} \in X \ni P(x)`
* with ':math:`:`': :math:`\exists{x} \in X : P(x)`
* with ':math:`\text{s.t.}`': :math:`\exists{x} \in X\ \text{s.t.}\  P(x)`
* an explicit version: :math:`\exists{x}(x \in X \land P(x))`
* fully parenthesized and explicit: :math:`(\exists{x})(x \in X \land P(x))`

Some boxes:

Here are some square symbols defined in MathJax. See `MathJax supported
commands`_ or `TeX commands available in MathJax`_ for more details.

.. math::

  \begin{array}{l c l}
    \hline                                                \\
    \text{Command}      & \text{Symbol}  & \text{Package} \\
    \hline              &                &                \\
    \text{\square}      & \square        & \text{amssymb} \\
    \text{\blacksquare} & \blacksquare   & \text{amssymb} \\
    \text{\Box}         & \Box           & \text{amssymb} \\
    \text{\boxminus}    & \boxminus      & \text{amssymb} \\
    \text{\boxplus}     & \boxplus       & \text{amssymb} \\
    \text{\boxtimes}    & \boxtimes      & \text{amssymb} \\
    \hline
  \end{array}

You can also place boxes around equations using the ``\boxed`` command:

.. math::

  \begin{array}{l c}
    \hline                                                          \\
    \text{Command}                    & \text{Result}               \\
    \text{\boxed{c_i = \sum_jA_{ij}}} & \boxed{c_i = \sum_jA_{ij}}  \\
    \hline
  \end{array}

Truth Tables
============

Negation, And, Or, Xor
----------------------

.. math::

  \begin{array}{c c c c c c c}
    P & Q & \neg P & \neg Q & P \land Q & P \lor Q & P \oplus Q\\
    \hline                    \\
    T & T & F & F & T & T & F \\
    T & F & F & T & F & T & T \\
    F & T & T & F & F & T & T \\
    F & F & T & T & F & F & F \\
    \hline
  \end{array}

Implication, If/Then
--------------------

Implication is a conditional statement written as either :math:`P \to Q` or
:math:`P \implies Q`, and read
as "if P then Q". It is logically equivalent to :math:`\neg P \lor Q`. In other
words,
:math:`P \to Q \iff \neg P \lor Q` where :math:`\iff` is a metalogical symbol
representing
"can be replaced in a proof with." We can also say :math:`P \to Q` is
equivalent to :math:`\neg P \lor Q` by writing :math:`P \to Q \equiv \neg P
\lor Q`.

.. math::

  \begin{array}{c c c c c c}
      &   &        &        & P \to Q \\
      &   &        &        & P \implies Q \\
    P & Q & \neg P & \neg Q & \neg P \lor Q \\
    \hline                                      \\
    T & T & F & F & T                       \\
    T & F & F & T & F                       \\
    F & T & T & F & T                       \\
    F & F & T & T & T                       \\
    \hline
  \end{array}

The material implication rule may be written in sequent notation:

.. math::

  (P \to Q) \vdash (\neg P \lor Q)

where :math:`\vdash` is a metalogical symbol meaning that
:math:`(\neg P\lor Q)` is a syntactic consequence of :math:`(P \to Q)` in some
logical system.

Note: Use ``\implies`` (as in :math:`p \implies q`) instead of ``\Rightarrow``
or ``\Longrightarrow`` (as in :math:`p \Rightarrow q`, or
:math:`p \Longrightarrow q` for implication. It provides correct kerning for
improved readability of formulas.

Likewise, use ``\iff`` (:math:`p \iff q`) instead of ``\Leftrightarrow``
(:math:`p \Leftrightarrow q`) for better readability.

:math:`\LaTeX` Notes and Examples
*********************************

Spacing
=======

* A necessary space: :math:`[ \text{Let}\ x=\text{number of cats}. ]`. We need
  a space between :math:`\text{Let}` and :math:`x=\text{number of cats}`, so we
  use ":math:`\text{\\ }`", as in ``[ \text{Let}\ x=\text{number of cats}. ]``.
* Space after a comma v1: :math:`(10,000, 20,000, 30,000)` - ``(10,000, 20,000,
  30,000)`` is wrong - there is too much space after the thousands separator.
* Space after a comma v2: :math:`(10{,}000, 20{,}000, 30{,}000)` - ``(10{,}000,
  20{,}000, 30{,}000)`` has good spacing.
* Space after a comma v3: :math:`(10{,}000\text{, } 20{,}000\text{, } 30{,}000
  ` - ``(10{,}000\text{, } 20{,}000\text{, } 30{,}000)`` has slightly more space
  between set elements, but may just be an example of us working too hard.
* Space after a comma v4: :math:`(10{,}000,\ 20{,}000,\ 30{,}000)` -
  ``(10{, 000,\ 20{,}000,\ 30{,}000)`` is okay, but may be putting too much
  space between set elements.

The vertical bar doesn't seem to stand out in set notation well enough. I think
it needs a little extra space.

* :math:`\{y | \exists x \bullet y = f(x) \land x \in C\}` is ``\{y | \exists x
  \bullet y = f(x) \land x \in C\}``
* :math:`\{y \text{ | }\exists x \bullet y = f(x) \land x \in C\}` is ``\{y
  \text{ | }\exists x \bullet y = f(x) \land x \in C\}``
* :math:`\{y \mid \exists x \bullet y = f(x) \land x \in C\}` is ``\{y \mid
  \exists x \bullet y = f(x) \land x \in C\}``

Delimiter Height
================

Match the height of delimiters to their contents by using ``\left`` and
``\right`` just before the delimiters. For example, the parentheses in
following equation match the height of their contents: :math:`\underline{q} =
\left( \begin{array}{c} q_1 \\ q_2 \end{array} \right)`

It looks like ``\underline{q} = \left( \begin{array}{c} q_1 \\ q_2 \end{array}
\right)`` is more simply written as ``\underline{q} = \begin{pmatrix} q_1 \\
q_2 \end{pmatrix}``: :math:`\underline{q} = \begin{pmatrix} q_1 \\ q_2 \end
{pmatrix}`.

If there is more than one element in each row of a matrix, place an ampersand (
) between each element to separate them. For example, if we write::

    \begin{bmatrix}
        x_{11}       & x_{12} & x_{13} & \dots & x_{1n} \\
        x_{21}       & x_{22} & x_{23} & \dots & x_{2n} \\
        \dots        & \dots  & \dots  & \dots & \dots  \\
        x_{d1}       & x_{d2} & x_{d3} & \dots & x_{dn}
    \end{bmatrix}
    =
    \begin{bmatrix}
        x_{11} & x_{12} & x_{13} & \dots  & x_{1n} \\
        x_{21} & x_{22} & x_{23} & \dots  & x_{2n} \\
        \vdots & \vdots & \vdots & \ddots & \vdots \\
        x_{d1} & x_{d2} & x_{d3} & \dots  & x_{dn}
    \end{bmatrix}

the result is:

.. math::

    \begin{bmatrix}
        x_{11}       & x_{12} & x_{13} & \dots & x_{1n} \\
        x_{21}       & x_{22} & x_{23} & \dots & x_{2n} \\
        \dots        & \dots  & \dots  & \dots & \dots  \\
        x_{d1}       & x_{d2} & x_{d3} & \dots & x_{dn}
    \end{bmatrix}
    =
    \begin{bmatrix}
        x_{11} & x_{12} & x_{13} & \dots  & x_{1n} \\
        x_{21} & x_{22} & x_{23} & \dots  & x_{2n} \\
        \vdots & \vdots & \vdots & \ddots & \vdots \\
        x_{d1} & x_{d2} & x_{d3} & \dots  & x_{dn}
    \end{bmatrix}

Examples of double subscripts and dotted double subscripts:

.. math::

    \begin{align*}
        {v_{k}}_d               && \text{\{v_\{k\}\}_d}                 && \text
        {awkward}\\
        v_{kd}                  && \text{v_\{kd\}}                      && \text
        {better}\\
        {{}\dot{v}_{k}}_{d}     && \text{\{\{\}\dot\{v\}_\{k\}\}_\{d\}} && \text
        {awkward}\\
        {{}\dot{v}_{kd}}        && \text{\{\{\}\dot\{v\}_\{kd\}\}}      && \text
        {another way}\\
        (v_{k})_{d}             && \text{(v_\{k\})_\{d\}}               && \text
        {change the notation}\\
        (\dot{v}_{k})_{d}       && \text{(\dot\{v\}_\{k\})_\{d\}}       && \text
        {add the dot}\\
        \dot{v}_{kd}            && \text{\dot\{v\}_\{kd\}}              && \text
        {seems the simplest}
    \end{align*}

Other Math Examples
===================

.. math::

    W^{3\beta}_{\delta_1 \rho_1 \sigma_2} \approx U^{3\beta}_{\delta_1 \rho_1}

Two equations:

.. math::

  \begin{equation} \label{eq1}
  \begin{split}
  A & = \frac{\pi r^2}{2} \\
   & = \frac{1}{2} \pi r^2
  \end{split}
  \end{equation}

Tables
******

Use an array for a table::

  \begin{array}{|c|c|c|}
  \hline \\
    & \text{Column A} & \text{Column B} \\ \hline
  \text{Row 1} & 5 & \oplus \\ \hline
  \text{Row 2} & \int & 8 \\ \hline
  \end{array}

results in:

.. math::

    \begin{array}{|c|c|c|}
    \hline \\
     & \text{Column A} & \text{Column B} \\ \hline
    \text{Row 1} & 5 & \oplus \\ \hline
    \text{Row 2} & \int & 8 \\ \hline
    \end{array}

The prime symbol (:math:`'`) may be rendered with either ``^{\prime}`` or its
shortcut, a single quote (``'``). Some people use the former to avoid typos. I
find the latter convenient.

Underbraces
***********

Here are some examples.

The underbrace embraces the right-side "rows" brace.

.. math::

    {\bf I_n} = \underbrace{
                    \left.\left(
                          \begin{array}{ccccc}
                                 1&0&0&\cdots &0\\
                                 0&1&0&\cdots &0\\
                                 0&0&1&\cdots &0\\
                                 \vdots&&&\ddots&\\
                                 0&0&0&\cdots &1
                          \end{array}
                    \right)\right\}
                  }_{n\text{ columns}}
                  \,n\text{ rows}

In the next example, the underbrace is more controlled. It embraces only the
matrix. The ``\vphantom`` line creates a box whose height is equal to an nx1
array of 1's. The ``\smash`` around the matrix typesets the matrix (including
the underbrace) but makes its height and depth zero. Put these together and you
have a box which includes the underbrace, but whose width and height are equal
to that of the matrix without the underbrace. See `"A complement to \smash,
\llap, and \rlap" by Alexander R. Perlis in TUGBoat (pdf)
<http://math.arizona.edu/~aprl/publications/mathclap/perlis_mathclap_24Jun2003
pdf>`_ for more on all of these commands and also ``\mathclap``.

.. math::

    \mathbf{I}_n = \left.\left(
                      \vphantom{\begin{array}{c}1\\1\\1\\1\\1\end{array}}
                      \smash{\underbrace{
                          \begin{array}{ccccc}
                                 1&0&0&\cdots &0\\
                                 0&1&0&\cdots &0\\
                                 0&0&1&\cdots &0\\
                                 \vdots&&&\ddots&\\
                                 0&0&0&\cdots &1
                          \end{array}
                          }_{n\text{ columns}}}
                  \right)\right\}
                  \,n\text{ rows}

.. I need an extra blank line (the vertical bar with a leading and a trailing
.. blank line) to separate the end of the equation above from the text below.

|

Here are a few underbraces under parts of an equation.

.. math::

    \underbrace{
        \begin{pmatrix}
            q_{sum} \\
            q_{dif}
        \end{pmatrix}
      }_{\boldsymbol{\tilde{q}}}
    =
    \underbrace{
        \begin{pmatrix}
            \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
            -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}}
        \end{pmatrix}
      }_{\boldsymbol{R}}
    \underbrace{
        \begin{pmatrix}
            q_1 \\
            q_2
        \end{pmatrix}
      }_{\boldsymbol{q}}

Phrases in Mathematical Proofs
******************************

"It follows easily that"
The use of "It follows easily that" means

    *One can now check that the next statement is true with a certain amount of
    essentially mechanical, though perhaps laborious, checking.  I, the author,
    could do it, but it would use up a large amount of space and perhaps not
    accomplish much, since it'd be best for you to go ahead and do the
    computation to clarify for yourself what's going on here.  I promise that
    no new ideas are involved, though of course you might need to think a
    little in order to find just the right combination of good ideas to apply.*

"It follows easily that" does not mean

    *if you can't see this at once, you're a dope*,

neither does it mean

    *this shouldn't take more than two minutes*,

but a person who doesn't know the lingo might interpret the phrase in the wrong
way, and feel frustrated.

Defining Binary Operators and Relations
***************************************

This section is from a Stack Exchange question on `\mathbin vs \mathrel
<https://tex.stackexchange
com/questions/38982/what-is-the-difference-between-mathbin-vs-mathrel>`_. While
the answer is clear, the example doesn't seem to show any noticeable
difference. It could be due to a limitation in MathJax and HTML to display such
tiny differences (just over :math:`1.1`pts. The original code, written in
:math:`\LaTeX`, is able to display the amount of space, in points, taken by
each example.

Use ``\mathbin`` and ``mathrel`` to designate some text as a binary operator or
binary relation, respectively. While ``\mathbin`` modifies the spacing around
something so that it adheres to that of a binary operator, ``\mathrel``
modifies the spacing to denote that of a binary relation. Here is an elementary
approach at showcasing the difference:

.. math::

  \begin{array}{c}
  \text{Relations}        \\
    \begin{array}{l l l}
      \LaTeX  & \text{Typeset}                & Width             \\
      \hline                                                      \\
      \text{x=x}              & x=x           & \text{24.76376pt} \\
      \text{\mathbin\{x=x\}}  & \mathbin{x=x} & \text{23.65268pt} \\
      \text{\mathrel\{x=x\}}  & \mathrel{x=x} & \text{24.76376pt} \\
      \hline
    \end{array}           \\
  \\
  \text{Binary Operators} \\
    \begin{array}{l l l}
      \LaTeX  & \text{Typeset}                & Width             \\
      \hline                                                      \\
      \text{x+x}              & x+x           & \text{23.65268pt} \\
      \text{\mathbin\{x+x\}}  & \mathbin{x+x} & \text{23.65268pt} \\
      \text{\mathrel\{x+x\}}  & \mathrel{x+x} & \text{24.76376pt} \\
      \hline
    \end{array}
  \end{array}


Limitations of MathJax
**********************

MathJax doesn't handle text, only math. To get a left fancy double quote
I have to manually insert the unicode character in math-mode. For example::

  .. math::

    \begin{align*}
      (x \to P)  && \text{(pronounced "x then P")}
    \end{align*}

will produce:

.. math::

  \begin{align*}
    (x \to P)  && \text{(pronounced "x then P")}
  \end{align*}

To make the left double quote face the correct direction, insert the unicode
character ``x201C`` and an extra space just before it::

  .. math::

    \begin{align*}
      (x \to P)  && \text{(pronounced}\ \unicode{x201C} \text{x then P")}
    \end{align*}

so we get:

.. math::

  \begin{align*}
    (x \to P)  && \text{(pronounced}\ \unicode{x201C} \text{x then P")}
  \end{align*}

Or use two single quotes on the left::

  .. math::

    \begin{align*}
      (x \to P)  && \text{(pronounced}\ \unicode{x2018}\unicode{x2018} \text{x
      then P")}
    \end{align*}

so we get:

.. math::

  \begin{align*}
    (x \to P)  && \text{(pronounced}\ \unicode{x2018}\unicode{x2018} \text{x
    then P")}
  \end{align*}

Or use two single quotes on the left and right::

  .. math::

    \begin{align*}
      (x \to P)  && (\text{pronounced}\ \unicode{x2018}\unicode{x2018} \text{x
      then P}\unicode{x2019}\unicode{x2019})
    \end{align*}

so we get:

.. math::

  \begin{align*}
    (x \to P)  && (\text{pronounced}\ \unicode{x2018}\unicode{x2018} \text{x
    then P}\unicode{x2019}\unicode{x2019})
  \end{align*}

References
**********

* `MathJax Demo Page <http://www.mathjax.org/demos/>`_
* `MathJax Supported Commands`_
* `TeX Commands Available in MathJax`_
* `How to Read Mathematics`_
* `LaTeX Symbols`_

.. _how to read mathematics: http://www.people.vcu.edu/~dcranston/490/handouts/math-read.html
.. _mathjax supported commands: http://docs.mathjax.org/en/latest/tex.html#supported-latex-commands
.. _tex commands available in mathjax: http://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm
.. _latex symbols: https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols

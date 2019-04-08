##############
MathJax Graphs
##############

I'm not sure how this works, but it does create a weird little graph.

.. math::

  \require{enclose}
  \def\uline#1#2{\enclose{updiagonalstrike}{\phantom{\Rule{#1em}{#2em}{0em}}}}
  \def\dline#1#2{\enclose{downdiagonalstrike}{\phantom{\Rule{#1em}{#2em}{0em}}}}
  %
  \def\place#1#2#3{\smash{\rlap{\hskip{#1em}\raise{#2em}{#3}}}}
  %
  \hskip 1em
  %
  \place{0}{12}{\bullet}
  \place{2}{0}{\bullet}
  \place{4}{4}{\bullet}
  \place{6}{0}{\bullet}
  \place{8}{8}{\bullet}
  \place{10}{0}{\bullet}
  \place{12}{4}{\bullet}
  \place{14}{0}{\bullet}
  \place{16}{12}{\bullet}
  %
  \place{.3}{4.4}{\dline{3.6}{7.6}}
  \place{2.3}{.5}{\uline{1.6}{3.6}}
  \place{4.3}{.4}{\dline{1.6}{3.6}}
  \place{4.3}{4.4}{\uline{3.6}{3.7}}
  \place{8.3}{4.4}{\dline{3.6}{3.6}}
  \place{10.3}{.5}{\uline{1.6}{3.6}}
  \place{12.3}{.4}{\dline{1.6}{3.6}}
  \place{12.2}{4.4}{\uline{3.7}{7.6}}
  %
  \place{-1}{12.5}{\frac01}
  \place{1}{-.5}{\frac13}
  \place{2.75}{4}{\frac12}
  \place{6.5}{-.5}{\frac23}
  \place{7.75}{9.5}{\frac11}
  \place{9}{-.5}{\frac32}
  \place{12.75}{4}{\frac21}
  \place{14.5}{-.5}{\frac31}
  \place{16.5}{12.5}{\frac10}
  %
  \hskip18em\Rule{0em}{14em}{1.5em}

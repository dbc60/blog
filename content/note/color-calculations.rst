---
title: "Color Calculations"
date: 2019-05-22T05:28:06-04:00
draft: true
math: true
categories: [software, math]
tags: [css, design, web]
---

033-0129426448
<!--more-->

**************
Verify MathJax
**************

.. math::

   \begin{equation}
   {\bf I_n} =
   \begin{array}{ccccc}
     1               &      0 &      0 & \cdots & 0 \\\\\\
     0               &      1 &      0 & \cdots & 0 \\\\\\
     0               &      0 &      1 & \cdots & 0 \\\\\\
     \vdots          & \vdots & \vdots & \ddots &   \\\\\\
     0               &      0 &      0 & \cdots & 1
   \end{array}
   \end{equation}


*******************
Complimentary Color
*******************

To get the compliment of a color where the color is represented as the values
from 0 to 255 for each color component Red :math:`(R)`, Green :math:`(B)`, and
Blue :math:`(B)`, subtract each component from 255:

.. math::

    \begin{array}{l c l}
      R_c & = & 255 - R \\
      G_c & = & 255 - G \\
      B_c & = & 255 - B
    \end{array}

Here is some inline math: :math:`\sqrt{3x-1} + (1+x)^2`

Is this an array?

.. math::

    \begin{array}{cc}
      a & b \\
      c & c
    \end{array}

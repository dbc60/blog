---
title: Matrix Operations
date: 2017-12-14T05:47:30-04:00
draft: true
categories: math
tags: [matrices]
---

*******
Inverse
*******

By definition, the inversion of matrix :math:`\boldsymbol{A}` is a matrix :math:`\boldsymbol{B}` such that :math:`\boldsymbol{AB} = \boldsymbol{BA} = \boldsymbol{I}`, where :math:`\boldsymbol{I}` is the identity matrix.

See `Invertible matrix <https://en.wikipedia.org/wiki/Invertible_matrix>`_

*********
Transpose
*********

The transpose of a matrix :math:`\boldsymbol{A}`, denoted :math:`\boldsymbol{A}^{T}` is an operation on :math:`A` that swaps the row and column indices of :math:`A`. It can be achieved by any of these three ways:

* reflect :math:`\boldsymbol{A}` over its main diagoonal (which runs from top-left to bottom-right).
* write the rows of :math:`\boldsymbol{A}` as the columns of :math:`\boldsymbol{A}^{T}`.
* write the columns of :math:`\boldsymbol{A}` as the rows of :math:`\boldsymbol{A}^{T}`.

If :math:`\boldsymbol{A}` is an :math:`n \times m` matrix, the :math:`\boldsymbol{A}^{T}` is an :math:`m \times n` matrix.

Examples
========

.. math::

    \left[
        \begin{array}{cc}
            1 & 2
        \end{array}
    \right]^{T}
    =
    \left[
        \begin{array}{c}
            1 \\
            2
        \end{array}
    \right]

Properties
==========

For matrices :math:`\boldsymbol{A}`, and :math:`\boldsymbol{B}`, and scalar *c* we have the following properties of transpose:

1. self-inverse: :math:`(\boldsymbol{A}^{T})^{T} = \boldsymbol{A}`
2. the transpose respects addition: :math:`(\boldsymbol{A} + \boldsymbol{B})^{T} = \boldsymbol{A}^{T} + \boldsymbol{B}^{T}`
3. :math:`(\boldsymbol{AB})^{T} = \boldsymbol{B}^{T} \boldsymbol{A}^T`. Note that the order of the factors reverses. From this one can deduce that a square matrix :math:`\boldsymbol{A}` is invertible if and only if :math:`\boldsymbol{A}^{T}` is invertible. In this case, we have :math:`(\boldsymbol{A}^{-1})^{T} = (\boldsymbol{A}^{T})^{-1}`. By induction, this result extends to the general case of multiple matrices, where we find that :math:`(\boldsymbol{A}_1 \boldsymbol{A}_2 \ldots \boldsymbol{A}_{k - 1} \boldsymbol{A}_{k})^{T} = \boldsymbol{A}_{k}^{T} \boldsymbol{A}_{k - 1}^{T} \ldots \boldsymbol{A}_{2}^{T} \boldsymbol{A}_{1}^{T}`.

See `Transpose matrix <https://en.wikipedia.org/wiki/Transpose>`_

---
title: Monomial
date: 2018-10-09T04:27:30-04:00
draft: true
categories: math
tags: [monomials]
---

<!--more-->
From Wikipedia's `definition of a monomial
<https://en.wikipedia.org/wiki/Monomial>`_:

.. _monomial:

Two definitions of a monomial may be encoutered:

#. A monomial, also called **power product**, is a product of powers of
   variables with nonnegative integer exponents, or, in other words, a product
   of variables, possibly with repetitions. The constant 1 is a monomial, being
   equal to the empty product and :math:`x^0` for any variable :math:`x`. If
   only a single variable :math:`x` is considered, this means that a monomial
   is either 1 or a power :math:`x^n` of x, with :math:`n` a positive integer.
   If several variables are considered, say, :math:`x,y,z`, then each can be
   given an exponent, so that any monomial is of the form
   :math:`x^{a}y^{b}z^{c}` with :math:`a,b,c` non-negative integers (taking
   note that any exponent 0 makes the corresponding factor equal to 1).
#. A monomial is a monomial in the first sense multiplied by a nonzero constant,
   called the coefficient of the monomial. A monomial in the first sense is a
   special case of a monomial in the second sense, where the coefficient is
   :math:`1`. For example, in this interpretation :math:`-7x^{5}` and
   :math:`(3-4i)x^{4}yz^{{13}}` are monomials (in the second example, the
   variables are :math:`x,y,z`, and the coefficient is a complex number).

What is interesting about monomials? The first fact is that any polynomial is a linear combination of monomials. This means they form a *basis* of the vector space of all polynomials.

basis
    In mathematics, a set of elements (vectors) in a vector space V is called a
    basis, or a set of basis vectors, if the vectors are linearly independent
    and every vector in the vector space is a linear combination of this set.
    In more general terms, a basis is a linearly independent spanning set.

linear independence
    In the theory of vector spaces, a set of vectors is said to be *linearly
    dependent* if one of the vectors in the set can be defined as a linear
    combination of the others; if no vector in the set can be written in this
    way, then the vectors are said to be *linearly independent*.

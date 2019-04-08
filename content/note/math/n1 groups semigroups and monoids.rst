###############################
Groups, Semigroups, and Monoids
###############################

.. _monoid:

*******
Monoids
*******

Today I learned that a monoid is simply a set with an associative binary operation, and an identity element. In other words, it is a `semigroup <semigroups_>`_ with an identity element.

For example, the set of integers under addition forms a monoid, because addition is associative and zero is the identity element. Similarly, integers and reals form monoids under addition and multiplication (where the identity elements are zero and one, respectively).

.. _group:

******
Groups
******

A group is an algebraic structure consisting of a set of elements and an operation that combines any two elements (that is, it's a *binary operation*) to form a third element, and that satisfies four conditions call the group axioms, namely closure, associativity, identity, and invertability.

For the definitions below, assume we have a binary operator :math:`\odot`, a set :math:`G` and elements of that set :math:`A`, :math:`B`, and :math:`C`, and a special element :math:`I` called the *identity element*.

.. closure:

Closure
=======

If :math:`A` and :math:`B` are two elements of set :math:`G`, then the product :math:`A \odot B` is also in :math:`G`.

.. _associativity:

Associativity
=============

For all :math:`A`, :math:`B`, and :math:`C` in :math:`G`, :math:`(A \odot B) \odot C = A \odot (B \odot C)`.

.. _identity:

Identity
========

There is a special element, :math:`I` in :math:`G`, called the *identity element*, such that :math:`I \odot A = A \odot I = A`. for every :math:`A \in G`.

Invertability
=============

There must be an inverse of each element. Therefore, for each element :math:`A` in :math:`G`, the set contains an element :math:`B = A^{-1}` such that :math:`A \odot A^{-1} = A^{-1} \odot A = I`.

.. _semigroup:

**********
Semigroups
**********

A semigroup is like a group, but more general. It casts off the axioms of identity and invertibility. The only remaining axioms on the binary operation are closure and associativity.

Another way of looking at it, is to understand that a `magma`_ is a set with a binary operation, and its only axiom is `closure`_ - the operation must be closed on the set. A semigroup, therefore, is a magma where the axiom of `associativity`_ applies.

*************
The Hierarchy
*************

* A `magma`_ is a set with a binary operation that is closed on the set.
* A `semigroup`_ is a magma where the binary operation is `associative <associativity_>`_.
* A `monoid`_ is a semigroup with an `identity`_ element.
* A `group`_ is a monoid where each element of the set has an inverse element under the given binary operation.

**********
References
**********

* `Magma`_. Note: a magma is a set with a binary operation that is closed under that operation. A unital magma is a magma with an identity element. A magma is also called a groupoid.
* `Zygohistomorphic Prepromorphisms`_
* `Taxonimization of Recursion Schemes`_
* `Real-world use of Zygohistomorphic Prepromorphisms`_
* `Maximally Dense Segments`_. Be prepared for a sliding window zygomorphism!

.. _magma: https://en.wikipedia.org/wiki/Magma_(algebra)
.. _zygohistomorphic prepromorphisms: https://wiki.haskell.org/Zygohistomorphic_prepromorphisms
.. _taxonimization of recursion schemes: https://www.quora.com/What-are-Zygohistomorphic-prepromorphisms-and-how-are-they-used
.. _real-world use of zygohistomorphic prepromorphisms: https://stackoverflow.com/questions/5057136/real-world-applications-of-zygohistomorphic-prepromorphisms
.. _maximally dense segments: http://www.iis.sinica.edu.tw/~scm/2010/functional-pearl-maximally-dense-segments/

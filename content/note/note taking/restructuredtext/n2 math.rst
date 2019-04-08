################################
Math, Equations, and Math Blocks
################################

We can write::

    \frac{\sum_{t=0}^{N}f(t,k)}{N}

and get: :math:`\frac{\sum_{t=0}^{N}f(t,k)}{N}`


Here's the same equation in a math block:

.. math::

    \frac{\sum_{t=0}^{N}f(t,k)}{N}

We can align equations::

    .. math::

        (a + b)^2  &=  (a + b)(a + b) \\
                    &=  a^2 + 2ab + b^2


.. math::

   (a + b)^2  &=  (a + b)(a + b) \\
              &=  a^2 + 2ab + b^2

The syntax is the same as :math:`\LaTeX`, except that you don't need to enclose math with ``$$``.

See `Math Support in Sphinx <http://www.sphinx-doc.org/en/stable/ext/math.html>`_ for details.

MathJax
=======

See `MathJax basic tutorial and quick reference <https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference>`_ for some of the basics.

* ``\mathbb`` stands for blackboard bold, and is used to create the set notation fonts for real numbers, natural numbers, and the like: :math:`\mathbb{CHNQRZ}`.


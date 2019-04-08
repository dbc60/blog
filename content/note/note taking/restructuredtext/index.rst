#################
reStructuredText
#################

.. toctree::
    :maxdepth: 2
    :caption: Table of Contents

    n0 titles and headings
    n1 links
    n2 math
    n3 roles extensions directives
    n5 tables
    n6 miscellaneous notation
    n4 failings of rest

I use Visual Studio Code (vscode) to edit my notes. The reStructuredText extension uses a Python module called `doc8 <doc8 on conda-forge_>`_. Every time I need to install/re-install MiniConda, I need to ensure both ``sphinx`` and ``doc8`` are installed.

Sphinx can be installed by running ``conda install sphinx``. It will be installed along with all of its dependencies. On the other hand, there is a more `up-to-date version on conda-forge <sphinx on conda-forge_>`_. Install it by running:

.. code-block:: doscon

  conda install -c conda-forge sphinx

Likewise, `doc8 <doc8 on conda-forge_>`_ is installed by running:

.. code-block:: doscon

  conda install -c conda-forge doc8

**********
References
**********

* `Quick Reference <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_
* `Footnotes`_
* `Using variables in pandoc templates <http://pandoc.org/MANUAL.html#using-variables-in-templates>`_
* `pandoc templates <https://github.com/jgm/pandoc-templates>`_
* `Lexer aliases that Pygments supports <pygment lexers_>`_
* `Reauthoring Toolkit`_
* `Docutils Hacker's Guide <docutils hackers guide_>`_
* `Problems with Structured Text`_
* `reST Directives`_
* `Interpreted Text Roles`_
* `Creating Interpreted Text Roles`_
* `Sphinx Documentation Contents`_

.. _pygment lexers: http://pygments.org/docs/lexers/
.. _Footnotes: http://docutils.sourceforge.net/docs/user/rst/quickref.html#footnotes
.. _reauthoring toolkit: https://latte.ee.usyd.edu.au/Reauthoring/
.. _docutils hackers guide: http://docutils.sourceforge.net/docs/dev/hacking.html
.. _problems with structured text: http://docutils.sourceforge.net/docs/dev/rst/problems.html
.. _interpreted text roles: http://docutils.sourceforge.net/docs/ref/rst/roles.html
.. _creating interpreted text roles: http://docutils.sourceforge.net/docs/howto/rst-roles.html
.. _rest directives: http://docutils.sourceforge.net/docs/ref/rst/directives.html
.. _sphinx documentation contents: http://www.sphinx-doc.org/en/stable/contents.html
.. _doc8 on conda-forge: https://anaconda.org/conda-forge/doc8
.. _conda-forge: https://anaconda.org/conda-forge
.. _sphinx on conda-forge: https://anaconda.org/conda-forge/sphinx

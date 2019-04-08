.. index:: ! note taking

###########
Note Taking
###########

.. toctree::
    :maxdepth: 2
    :caption: Table of Contents

    n0 an ideal note taking app
    restructuredtext/index
    zettelkasten/index

This is my first experiment in note taking using reStructuredText and my best interpretation of what a :doc:`Zettelkasten <zettelkasten/index>` is.

Each note should have just three things

* A unique ID. My notes' IDs will start with the letter ``n`` followed by a natural number (``{0, 1, 2, 3, ...}``).
* A title. My titles will be formatted as the note's unique ID, a space and the subject of the note.
* Content.

A note's title and base file name should match. Any extension to the file name will indicate the kind of markup used to format its content. For example, ``.rst`` is used for reStructuredText, and ``.md`` is used for Markdown.

I'd like to have more meta data, like the date and time (a timestamp) the note was created and a timestamp for when it was last modified. I think that can be derived from the file system on which the note is stored.

For the sake of record keeping this note was created on March 26, 2017 at about 5:29 AM EDT. The timestamp I'd create for it would look something like 201703260529EDT, I think.

*********
New Notes
*********

My new notes are written with the Zettelkasten method, and use reStructuredText for formatting. There are lots of notes I'll want to convert from Markdown, so I installed `pandoc <https://github.com/jgm/pandoc/releases/tag/1.19.2.1>`_. The conversion is a one-liner. To convert ``README.md`` to ``README.rst``::

    pandoc --template=template-file --from=markdown --to=rst --output=README.rst README.md

See :ref:`pandoc-template-file` for an example template that helps to convert markdown to restructuredText.

Instead of `Jekyll <http://jekyllrb.com/>`_, my new notes rely on `Sphinx <http://www.sphinx-doc.org/en/stable/index.html>`_, which requires python. I installed Python 3.4 from `Anaconda <https://www.continuum.io/downloads>`_, and ran ``conda install sphinx`` to install Sphinx 1.5.1.

Per the `documentation <http://www.sphinx-doc.org/en/stable/tutorial.html>`_, I ran ``sphinx-quickstart`` to set up my new notes directory. Among other things, it created a file called ``make.bat``. All I have to do to build HTML files from my content is run ``make html``.

.. index::
    single: reStructuredText

*************************
Sphinx & reStructuredText
*************************

Here are some examples of how to use reStructuredText and Sphinx directives to get some nicely formatted output.

Quote blocks do not preserve line breaks. They are created by indenting each line of text:

    Once upon a time,
    They lived happily ever after

    The End.

Literal code blocks are displayed exactly as written. The special marker ``::`` is used to introduce them. They must be indented and separated from the preceding paragraph by a blank line::

    Once upon a time
    They lived happily ever after

    The End.

We can add syntax highlighting by using the Sphinx directive ``.. code-block:: <language>``. There are some rules for what the ``<language>`` part can contain. It can be ``none``, ``python``, ``guess``, ``rest``, ``c`` and any other `lexer alias that Pygments supports <http://pygments.org/docs/lexers/>`_. Here is a JSON code block, for example:

.. code-block:: json

    {
        "editor.tabSize": 4,
        "editor.insertSpaces": true,
        "editor.detectIndentation": false,
        "editor.suggestOnTriggerCharacters": false,
        "explorer.autoReveal": false,
        "editor.acceptSuggestionOnEnter": "off",
        "editor.wordWrap": "bounded",
        "editor.wordWrapColumn": 132,
        "workbench.iconTheme": "vs-seti",
        "editor.minimap.enabled": true,
        "markdownlint.config": {
            "MD022": false
        },
        "editor.fontSize": 14,
        "editor.fontFamily": "Consolas, 'Courier New', monospace",
        "editor.fontLigatures": false,
        "window.zoomLevel": 1,
        "files.eol": "\n",
        "files.exclude": {
            "**/.git": false
        },
        "[cpp]": {
            "editor.quickSuggestions": false
        },
        "[c]": {
            "editor.quickSuggestions": false
        },
        "editor.quickSuggestions": false,
        "C_Cpp.intelliSenseEngine": "Default"
    }

How about a ``C++`` code block with syntax higlighting:

.. code-block:: c++

    template <T>
    class Foo : public T {
        std::vector<std::string> vs_;

    public:
        Foo();
        ~Foo();

        get(int i);
    };

See the documentation on showing `code examples <http://www.sphinx-doc.org/en/stable/markup/code.html>`_ for more details.

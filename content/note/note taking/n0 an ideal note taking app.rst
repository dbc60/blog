---
title: An Ideal Note Taking Application
date: 2018-03-26T09:17:30-04:00
draft: true
categories: note taking
tags: [design, requirements]
---
I'd like to have a note taking application where I can write text, mathematical equations, and describe charts and graphs, and have the documents typeset as well as :math:`\LaTeX` does. However, I don't want to lug around hundreds of megabytes of tools and libraries, such as :math:`MiKTeX`, just to be able to read what I wrote.

<!--more-->

The `Sphinx Documentation Generator <http://www.sphinx-doc.org/en/stable/>`_ is a nice tool, and it has a MathJaX extention that renders equations beautifully in the browser. I haven't figured out how to include charts and graphs, or if it is even possible.

`TiddlyWiki <http://tiddlywiki.com/>`_ is also a nice tool for capturing notes. It has a the `KaTeX plugin <https://khan.github.io/KaTeX/>`_ for typesetting math. It also has a `D3 plugin <http://tiddlywiki.com/plugins/tiddlywiki/d3/>`_ for rendering all kinds of graphics. The `railroad diagram plugin <https://github.com/tabatkins/railroad-diagrams>`_ is also cool.

TiddlyWiki looks like an ideal solution, but it produces a monolithic file. I don't like the idea of one file for all notes. After a while, the file becomes unwieldy, and the browser becomes unresponsive.

I like Sphinx's and `Jekyll's <https://jekyllrb.com/>`_ approach where all documents are kept in a single directory, and there is a naming convention to distinguish input, configuration, and output files and directories. Among other things, it means version control can be handled by git with a simple ``.gitignore`` file to control what get's committed to the respository.

************
Requirements
************

Generally, there should be a set of good conventions applied to minimize the amount of configuration required to set up a note-project.

* Good markup with a nice, regular syntax, or be like TiddlyWiki and hide or embed the markup.
* Modules with lexical scope. I'd like to define links and directives once, and then be able to include and use them in other modules.
* Code blocks with syntax highlighting (perhaps with `Pygments <http://pygments.org/docs/lexers/>`_).
* Inline code, or at least be able to specify fixed-width text inline.
* An easy way to specify and change display/rendering themes.
* Automatic linking between documents in the same project directory, even if it's just a previous-next link. The linking should be based on what's in the table of contents for the parent document.
* Enforce a convention where there's a default or preferred "main" document, similar to the way "index.html" is chosen by browsers and web servers when a URI/URL points to a directory.
* Render beautiful mathematics using :math:`LaTeX` or similarly powerful markup.
* Be able to embed charts, graphs, and other graphics in a reasonably powerful markup language, or use a programming language with a library whose API is reasonable, and regular.
* Generate charts, graphs, and other graphics from markup or directives based on data. The data can be in a code-block-like section, or imported from another file.
* Edit within a browser. If that's not possible, then edit with a text editor, and have a fast build step - bonus points if the browser can be automatically updated/refreshed after each run of the build tool.
* Automatically generate a table of contents, glossary, list of figures, list of tables, bibliography, index, and so forth.
* A configurable table of contents to control the depth.
* Easy to add contents to the table of contents, index, or other list. Perhaps items could be added via a reference markup of some kind.
* Footnotes.
* Margin notes.
* Front Matter.

  * Title
  * Author
  * Publisher
  * Date of publication.

* Back matter.

  * Appendices.
  * Glossary.
  * Endnotes.
  * Reference Lists.
  * Bibliography.
  * List of Symbols.
  * Index.

*****************
Optional Features
*****************

I'm not sure a note taking system needs me, but some systems have these, and they could be fun.

* Show and hide sections similar to the way TiddlyWiki shows and hides tiddlers.

***********
Inspiration
***********

There's a `demo of DocTool <https://www.youtube.com/watch?v=Yiyszxw8feY>`_ that shows how you can add doxygen-like comment blocks to your code, and generate documentation that pulls in the code, uses the comment blocks as plain text commentary, and shows the code with syntax highlighting. The result is a more simple HTML representation of documented code than what doxygen generates, but allows for additional control through a separate ``.doc`` file that imports the commented C++ source code.

Additionally, each run of DocTool_ can compile the associated C++ source code and execute it. The console output from executing the code will be captured in the final HTML page. The compilation and execution instructions are contained within a "shell box", so DocTool is parsing the contents of the shell box, interpreting it as a sequence of shell commands, executing them, and capturing the output.

DocTool_ is an interesting take on documenting source code.

*********
Questions
*********

The note taking system should be standalone, and not require any network connection to work. How should it be viewed? One way is to have a standalone program for displaying and editing the notes. There are lots of examples of such programs, like Microsoft OneNote, MS Word, TiddlyWiki uses a browser, Google Keep, Evernote, and many others (for example, see `this list <https://zapier.com/blog/best-note-taking-apps/>`_). Even a simple text editor will work if you don't mind writing and viewing notes in plain text.

Another way is to use a static site generator, like `Jekyll <http://jekyllrb.com/>`_ or Sphinx_. It might even be possible to generate output other than web pages, as pandoc does, so a browser is only one kind of viewer. I can use a plain text editor and some kind of markup language (like markdown or reStructuredText), run the generator, and view my notes in a browser. If carefully done, the appropriate libraries (such as MathJaX) can be made available locally, so no network connection is needed.

Yet another way is to build the editor in JavaScript and run it in a web browser. This is the way TiddlyWiki works. The differences between TiddlyWiki and what I want are things like an explorer view of the files in the project, generation of a table of contents for each page, be able to mark sections, tables, and figures for inclusion in tables of content, a list of tables, a list of figures, and an index.

I'd like to be able to view notes in different ways depending on their purpose. For example, :math:`\LaTeX` defines several document classes, like article, book, letter, and report. Wouldn't it be nice to collect several :doc:`notes <zettelkasten/n0 zettelkasten method>` or excerpts from them, and fold them into a single viewable document?

******
Markup
******

Part of what a good note taking system needs is reasonable markup. Sphinx uses reStructuredText (reST, or rst), which has a lot of capability, but is maybe too terse. It's hard to remember where an underscore belongs when defining internal and external links. Similarly, I find it difficult to remember the syntax for setting references and entries for the index.

On the other hand, markdown, even GitHub markdown, is too simple. It doesn't provide for math, references between documents and a few other features I like in restructuredText. It does allow you to embed HTML, but that doesn't necessarily translate to other output formats, and looks awful.

******
Design
******

At first blush, it looks to me like a solution might consist of HTML, CSS, and some JavaScript to implement an editor, include MathJaX or KaTeX for rendering math markup, and D3js for rendering other graphics. It will take a lot of study to learn how to embed JavaScript (probably NodeJS and some other libraries) to create an editor, and automate the creation of front and back matter.

How should the HTML core be designed? What CSS and/or Sass ID and class selectors will be needed? If I want to go with Sass, do I need `an external tool <http://sass-lang.com/libsass>`, or is there a decent `JavaScript parser for it <https://github.com/medialize/sass.js>`_?

**********
References
**********

* `Technical Writing Design - Back Matter <https://en.wikibooks.org/wiki/Professional_and_Technical_Writing/Design/Back_Matter>`_
* `Libsass`_
* `node-sass`_ Node.js bindings to `libsass`_
* :doc:`Sass and CSS <../software development/web programming/n0 sass and css>`
* DocTool_ is a tool for writing documentation and tutorials. It uses a reStructuredText dialect where you can embed shell scripts and C++ code in your documents. DocTool_ will execute them and include the output in the HTML.
* Docutils_ is the parsing and translating suite used by Sphinx_ to generate documentation from reStructuredText.
* Sphinx_ is the tool Python programmers to document their source code.

.. _doctool: https://github.com/michael-lehn/DocTool
.. _docutils: http://docutils.sourceforge.net/
.. _node-sass:  https://github.com/sass/node-sass
.. _libsass: https://github.com/sass/libsass
.. _sphinx: http://www.sphinx-doc.org/en/stable/

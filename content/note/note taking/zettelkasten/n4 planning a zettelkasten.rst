#######################
Planning a Zettelkasten
#######################

need a program to help automate some of the tasks, like adding tags to notes in such a way that I can call up a list of notes that have one or more tags. I'd also like my notes to be written in plain text, so I can use nice text editors like Visual Studio Code (vscode), Atom, Vim, Emacs, Notepad++ and others. I'd like to keep my notes in a version control system like git or hg.

I could write one note per file. How do I create links between notes? If I use `Markdown <http://daringfireball.net/projects/markdown/>`_, `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ (rST), `Textile <https://www.promptworks.com/textile>`_, `YAML <http://yaml.org/>`_ or some other markup language, then I could embed links in notes. How do I create note sequences? Maybe I need a separate (somewhat automated) note to record a sequence of notes along a particular topic. That sequence note would be the one that gets a tag - the guideline being to limit tags to mark entry points into the note system rather than trying to include every applicable tag to every note.

Should I keep files that belong to a note sequence in a directory? That might make storing and searching for branches of note sequences awkward. Each directory would need a subdirectory for each branch. Finding a referencing notes among branches would require links across nested subdirectories, which isn't so bad. However, viewing notes at the file-system level becomes awkward as the individual files are hidden in subdirectories.

If I have sequencing notes, then should my relational links be recorded in an external file, too? Probably not. I think I want to be able to reference other notes inline, like a wiki. Keeping relational links external is what one would do with a relational database, but that gets in the way of the flow of thought.

What information should be recorded on each note? Some of these features preclude using a plain text editor. It would be a pain in the butt, for example, to have to remember to edit a timestamp for the last time a note was updated. Maybe that meta data isn't so important - or, if each note is contained in a distinct file, the file system will keep track of that.

* Does each note need its own title?
* A unique ID. I like the convention of creating one file per note, where the file name is the ID followed by a title/subject. I found this idea while reading about `one person <http://zettelkasten.de/posts/one-note-review/>`_, who uses Microsoft OneNote for his Zettelkasten. He assigns a number in sequence, starting with ``1`` for the first note. He puts the letter ``n`` in front of each number ID, so his ID sequences are ``n1``, ``n2``, ``n3``, and so on. When he searches for notes by ID, he might searche for ID ``n268``. Each title is prefixed by the note ID, so not only does he find a note like ``n268. Mindfulness ...``, but he finds notes with a link to that note. They are displayed in a list like:

  * ``n95. Mindfulness & Creativity``
  * ``n71. Living in the past``
  * ``n70. Living for the future``
  * ``n61. Eating``

* If each note is contained in its own file, what is the file name? Should it represent the note's title, ID, creation date or should it be based on something else?
* Creation timestamp (date and time in some nice format). Rely on the file system.
* A timestamp for the last time it was updated. Rely on the file system.
* The content of the note. I suppose most notes will be plain text, but some could be code snippets in some programming language, and other files could be supporting data in a variety of formats including binary data, like images, sound, video, executables, etc.

So, I think I'll start with a file name convention of ``n# Title.ext``, where each file name starts with the letter ``n``, ``#`` is the number of the note, the Title is basically the subject of the note, and ``.ext`` is the file name extension. I'll use conventional file name extensions, like ``.txt``, ``.md``, ``.rst`` and others as needed.

The next convention is to use some kind of markup to indicate a reference to another note. I'll use Markdown's or reStructuredText's built-in capability to link between documents, depending on the content of the file.

Initially, I'll keep the system as simple as possible with a set of plain text files in a directory. Maybe I can migrate all my notes from org-mode and Jekyll into something a little easier to navigate.

---
title: Software Development and Note Taking Platform
date: 2016-06-19
draft: true
categories: [projects]
tags: [software]
---

Jekyll isn't a horrible tool for generating sites from markdown, but it is a bit fickle and I don't enjoy some of the conventions baked in. It's also slow. It takes nearly 8 seconds to rebuild my notes for even the smallest change. I don't have so much content here, so why does it take so much time? Is there another way?
<!--more-->

## What I Want
I want a tool of set of tools that enable me to write documentation in a text editor using markup, and render it in HTML and PDF. For the HTML version, I'd like to see the results as I edit - it doesn't even have to render in real-time as I type. Updating the browser after each save is often enough. PDF output is more of an afterthought. It might be nice to have, but for most of my notes well-styled HTML is fine. Other output formats are a bonus.

I think Markdown, RestructuredText, AsciiDoc are fine input formats. The toolchain should allow for one or more of those with CSS, Sass and similar formats for styling. I'll even consider Scribble, LaTeX and styling macros. Under no circumstances will I tolerate XML as an input format.

## The Zettelkasten Method
3/19/17: I've recently come across a method, and even philosophy, of [note taking called Zettelkasten](http://takingnotenow.blogspot.com/2007/12/luhmanns-zettelkasten.html). In the original method, created by the German sociologist Niklas Luhmann (1927-1998), index cards are used for recording short notes. What's fascinating about the method is that Luhmann claimed his file was something of a collaborator in his work. The index cards were organized in such a way that it enabled him to discover new connections among different thoughts and subjects.

Each card is indexed with a number independent of the information on it, starting with 1. Index cards are small, so it's often necessary to continue a thought on other cards. The first cards would be numbered `1/1`, the next `1/2`, `1/3`, and so on. He wrote these numbers in black ink at the top of the card so they could easily be seen in the file, and returned to the correct place.

In addition to recording a linear continuation of a topic on different cards, Luhmann also introduced a notation for branching topics. When he felt a term needed to be further discussed or he wanted to add more information, he would start a new card that had the same number as the card from which he was supplementing and would add a letter to the new card's index. To branch from card `1/6`, he would create a new card and mark it as `1/6a`. Branches might require further continuations, so there would be cards marked `1/6a1`, `1/6a2`, `1/6a3`, and so on. Of course, any of these continuations could be branched again. He wound up with labels as long as `21/3d26g53` - the number of a card discussing his academic rival, Jurgen Habermas.

It seems that the method is to write down a thought on a card and assign the next number followed by `/1`. For example, `1/1` for your first card. If the thought won't fit on a single card, then continue it on another card and label that `1/2`.

While reflecting on cards you've written, if you need to expand on a topic, then create another card, label it with the label from the original card and append `a1`. Similarly, to follow a train of thought in a different direction from the same card, you'd label a new card with the label from the original card and append `b1` to it. So, two separate trains of thought from card `12/3` would start with `12/3a1` and `12/3b1`. If each of those trains of thoughts required more than one card, the `a1` sequence of cards would be labeled `12/3a2`, `12/3a3`, ..., while the `b2` sequence would be labeled `12/3b2`, `12/3b3`, etc.

In addition to sequencing cards for a single train of thought, and branching from a card to a more detailed treatment of some aspect of a topic, cards can directly reference each other. Just record one card's label in the body of another cards to create a link. By this method, Luhmann created a manual for of Hypertext and the World Wide Web, but just for his thoughts and interests.

### The Term Folgezettel
A Folgezettel is a note sequence. It refers to the fact that Luhmann's cards are kept physically in sequence, and those containing a single thought are labeled as `12/3b/1`, `12/3b/2`, `12/3b/3`, and so on. It initially seemed to me that the physical placement of cards and the sequence of labels were needed to keep together one thought that didn't fit on a single card.

#### Sascha's Take on Folgezettel
One person, Sascha, writes in [No, Luhmann was not about Folgezettel](http://zettelkasten.de/posts/luhmann-folgezettel-truth/) that he and his friend Christian used to translate Folgezettel as "sequence of notes", but now he says to think of Folgezettel as "a child to his parent note."

Sascha claims that another person, Daniel, who created a program called [Zkn3](http://zettelkasten.danielluedecke.de/en/index.php) to implement Zettelkasten on a computer, is that Folgezettel is the main concept behind Luhmann's Zettelkasten: "This means that you develop an idea in a linear way and branch off if the next thought doesn't fit into the prevous string of ideas.

Sascha notes that one Zettel can directly reference another, so the physical position of each Zettel is not so important. It seems to me the labels and the fact that they represent the physical position of each Zettel are important for locating each Zettel in a physical Zettelkasten. Also, if Zettels are stored in separate files, you'll need an indexing system to reference and locate Zettels.

Sascha says that Folgezettel (the specific and intended connection between Zettel, realized through their position in the archive) can have more than one purpose:

- continue a thought
- continue an idea to a thought
- exclude a thought from the existing line of thoughts (Folgezettel could mark a blind end - that is, what conclusion to *not* make).

Sascha notes that the intent of a Folgezettel is not always clear and because we don't have a physical Zettelkasten, he concludes there is no good reason for Folgezettel. A Folgezettel can be replaced by a link with an annotation added to convey its intent. He goes on to say that instead of using Folgezettel, one can use tags on Zettels indication to which categories they belong.

Sascha's annotated links are realized as follows. He prefixes the ID of a Zettel with a "§" to indicate a (parent) link to that Zettel. If he wants to see all the children of a particular note (as if they were part of a Folgezettel), he searches for its ID with a "§" prefix. If he wants a Zettel to be an addition or a continuation of a Zettel, he links to it and marks the new Zettel as a continuation.

#### Daniel's Take on Folgezettel
Daniel responded to [Sascha's post](http://zettelkasten.de/posts/luhmann-folgezettel-truth/) in his post titled [You Underestimate the Power of the Dark Folgezettle](https://strengejacke.wordpress.com/2015/11/01/you-underestimate-the-power-of-the-dark-folgezettel/). He says that Sascha overlooked to aspects of Folgezettel:

1. A Folgezettel or note sequence was not primarily used by Luhmann due to the physical limitations of small paper notes. Writing very short notes is a technique itself.
1. A manual link or reference between two notes is something different than continuing an idea via Folgezettel (note sequences).

Links or references do not emphasize the relationship between notes (ideas, concepts). The context of connections usually remains unclear due to arbitrary relationships. Fogezettel, however, create specific relationships - adding manual links (references) to these relationships create relationships of relationships, the core aspect of Luhmann's working principle.

Daniel goes on to say that all notes in a note sequence are on the same level. They do not represent a parent-child relationship of thoughts. Also, there are no categories. There is a keyword register which is functionally equivalent to categories, but more powerful and allows multiple storage. It defines certain notes as thematic "entrances" into the Zettelkasten. That's cool.

### Keyword Register
Luhmann maintained a separate register with core keywords (tags), which referenced selected notes. The purpose of this register was to find an "entrance" or starting point into the Zettelkasten. In certain cases, the notes also had tags, but _tags don't have the primary purpose to create links between notes_.

### General Notes on Zettelkasten

Placing notes in categories doesn't scale. More often than not, a note will belong to more than one category. Tagging has been used to in several editors as a substitute for categories. Each note can have multiple tags, where tags represent categories. The problem with tags is collecting or linking notes with identical tags can be difficult. The spelling must be identical to enable basic text searches to automatically link notes via tags. Also, the number of tags can easily become unmanageable, making it hard to remember which tags have been used so new notes link with previous ones.

The principle of links and references is one solution for managing notes. Like a wiki, creating direct links between notes allows for both thematic and non-thematic linkage. It makes it possible to explore notes that are not directly related via the link path, by navigating over a set of ordered notes within a theme. The problem with links is that it is difficult to retrive specific notes. Workflow may be poor, due to the limited scope of linkage - I'm not sure what Daniel means by this.

Luhmann's principle of organizing Zettelkasten has four parts. No categories; use linkage/references among notes; Use a register of tags; Allow arbitrary branching of note sequences.

No categories, because categories for an internal structure on the notes, and are not flexible. It does mean that each note must have fixed position in the collection and a unique ID indicating its position. A fixed position creates an implicit linkage among related notes, and enables fast retrieval of specific notes. If one note references another, its easy to find that note. Daniel says that an electronic Zettelkasten doesn't require notes to have fixed positions. I'm not sure about that. Even though an electronic Zettlekasten can follow links, how do you manually find the specific note to which you want to create a link? There must be some way to search, or some kind of index that can be referenced. I'd like such a system to inform me rather than requiring me to search for what I want.

Use linkage/reference among notes. Unique IDs allow selective or specific links/references between notes. The number of links/references, in theory, is unlimited. It solves the problem of "multiple storage"; that is, if a note does not fit into a single category, build relations between multiple notes with links/references. Links and references also enables one to put notes in different contexts.

Use a register of tags instead of tagging each note. A separate register lists core keywords (the tags), and each tag lists selected (not all) notes that are considered entrance/starting points for the subject/category represented by the tag. Generally, notes don't contain tags. The tags exist only in this register. In other words, tags don't exist to create links between notes. Their primary purpose is to mark starting points for a category. From the example Daniel provides, the register is also made up of short notes (Zettels), so each one has a unique, positional ID. Instead of a note on a subject, the registers Zettels contain lists of keywords, where each keyword is followed by one or more references to notes. It's possible that several keywords will reference the same note. Brilliant!

Arbitrary "branching" of note sequences. Notes can be concatenated, resulting in note sequences. This is necessary in a physical Zettelkasten due to limited space on note papers. In an electronic Zettelkasten, no text limits for notes, however it is also recommened to keep notes short. New topics or subtopics can branch off from ntoes in a sequence, leading to a tree structure of note relationships. Branching and note sequences allow for "story telling". To some degree, branching and sequences are developing or evolving texts on a specific topic (sequence) or side topics (branching). Branching allows reduction of complexity concerning tags and the register (fewer entrance points).

The key to Luhmann's Zettelkasten is to combine all of these techniques: note sequences and branching, in combination with tags in a register and links/references. Here's what Luhmann did:

- Write down an idea
- Develop the idea with an implicit sequence of notes and note IDs.
- Add side topics or subtopics as the idea develops. The form of his unique IDs show how the sequence of notes branch to related topics/subtopics. It keeps their relationships intact.
- Add manual links/references between relevant notes, creating a system/network of "relationships of relationships". It shows the "story" from one topic to a side or sub topic is linked or related to the story of that first topic to another side or sub topic.
- Add keywords to the register

To summarize his princeiples, we should write small notes using note sequences to develop an idea or topic. Where possible or necessary (that is, if an idea can be considered as the start of a new note sequence, but does not fit into the current linear line of thought), branch off a new idea path. Check if a similar topic or story line has been written elsewhere. If so, add manual links/references between the two (I'd guess between the two starting notes). Identify relevant notes that function as starting points, and add these to the tag register.

Another view of a workflow:

- Think about the topic or subject where a new note fits
- Find a starting point in the Zettelkasten realted to this topic and start reading/exploring your existing notes (sequences).
- Decide whether the note is
  - the start of a new topic/sequence
  - fits into an existing note sequence (continuing an existing note sequence)
  - fits into an existing not sequence (but branching off a new subtopic)

Depending on where the note joins or fits into the Zettelkasten, think about tagging your note. Which (parallel) note sequences are related to this note? Are there relevant notes in other sequences? If yes, add manual links between notes. Less is beautiful: Better use fewer keywords. For example, use keywords only for notes that start a new note sequence, for those notes that branch off inside a sequence, or for very important "key notes."

### An Electronic Zettelkasten
It would be nice to have a tool that kept an index of notes similar to Zettelkasten. What I think I'd want from such a tool, is:

- ID: assign a unique identifier to each note and sequence of notes for a particular thought
- Branching: keep links for branches of a particular thought in a topic tree
- Links/References: allow me to make direct links from one card to another in a different branch of the tree to help me remember relationships between branches
- also have a backlink so I can see which cards link to a given card.
- Tag Register: be able to create cards which contain links to other cards like a bibliography
- be able to embed the contents of a card (either in its entirety or just one or more selected section - in which case the referenced card should probably be divided into a sequence of cards). Remember the Sheets Hypercode Editor (by Robert Stockton and Nick Kramer) that was a kind of literate programming environment? It operated by dividing code into small self-contained objects called _fragments_ and organizing them within file-like containers the authors called _sheets_. That was quite an experiment. I imagine that notes could be organized in a similar fashion, and possibly more successfully than code. There was also "Code Bubbles" which
- Record and retain meta data, like a timestamp for when a note was created, and when it was last modified. Certainly, the note's ID and the IDs of notes it references should be accessible. Maybe even backlinks, so one can see which notes references a given one. I don't think version history is necessary.
- Keep tables/lists of links, note sequences (perhaps in an outline format), keywords (the tag register), authors (for keeping a list of references when writing books or articles), a titles section containing a complete list of notes, clusters and bookmarks. Clusters could be related topics that are being put together for the development of an article or a book.
- generate an index of cards
- accept plain text input formats, such as [reStructuredText](http://docutils.sourceforge.net/rst.html) (RST, ReST or [reST](https://en.wikipedia.org/wiki/ReStructuredText)) and Markdown.
- be able to display more than plain text
  - computer source code
  - execute algorithms ala' jupyter notebooks
  - mathematical equations
  - animations
  - graphs
  - musical notation
  - sounds from sound files, or generated by algorithms
  - images from image files, or generated by algorithms
  - videos from video files, or generated by algorithms
  - SIMILE Timelines

Perhaps have a WYSIWYG mode as well as being able to write markup directly. I know I find [Jekyll](https://jekyllrb.com/) somewhat irritating because it takes a very long time to generate a freshly updated page. ConnectedText has a feature that lets you select custom colors for specific markup. Basically, it's a way to customize its syntax highlighter. Coloring the markup might make it easier to read content, as your eyes can skip over markup for things like comments, internal and external links, headings, includes and other commands.

Can a note's ID be just a number, where each new note is assigned the next integer is a global sequence? Does a more complicated ID scheme, like the one Luhmann used for his physical Zettelkasten, add any functionality without adding any undue complexity? Probably not. It should be easy for an electronic Zettelkasten to keep notes along the same thought in sequence. In fact, it could be a feature where each new note is created as a continuation of a thought or a branch. Of course, you shouldn't have to determine the new notes position in a sequence before its written, and you should be able to move it around or somehow designate a collection of notes as a sequence, if you so desire - even reordering the notes within a sequence at some later time.

### External, Internal and Back Links, Oh My!
There are at least three types of links that can be used in a Zettelkasten. There are external links, such as hyperlinks to external resources - like a page on a website.

Another common link is an internal link. It connects one note to another.

Finally, there are backlinks that should be automatically generated. It can be handy to have backlinks that show which notes refer to a given note.

### When to Start a New Note
Say you're starting a fresh Zettelkasten, or you learn more about an existing topic. You write your note and expand the text. You get to a point where you ask yourself, should I create a new Zettel? Should I split up this one? Can I attach detail there?

It's easy to answer these questions, as the scenarios are limited.

If you have no notes yet, then start with anything you feel fits into a note right now. You'll learn when to split notes, with time.

If you already have notes, search your archive for similar notes or topics. What you do next depends on the outcome. One outcome is that you have no notes related to the topic. In this case, create a new Zettel as if your Zettelkasten were empty. Your search revealed it won't affect the existing notes anyway.

On the other hand, if you have notes related to the topic, you should skim or read those notes to figure out how your new information fits. In this case, you'll have to remember to create links between the existing notes and the new information. Regardless of the links, you'll find one of three possible cases apply. The first possibility is that the existing notes don't fit the new idea. In this case, create a new note, but adhere to existing keywords. That is, put it in a sequence that represents the given topic.

In the next possibility, you find a few notes roughly match the new information. Maybe your new thought doesn't warrant its own Zettel now, so create a new note to compile the existing knowledge (a compilation note), comment the compilation and make sure to add the new detail, and create links in both directions.

Finally, one note is about the exact same topic. If it contains everything, then you're done. If you found something new, such as a new reference, citattion or other detail, then incorporate the new information into the existing note.


### Planning a Zettelkasten
I need a program to help automate some of the tasks, like adding tags to notes in such a way that I can call up a list of notes that have one or more tags. I'd also like my notes to be written in plain text, so I can use nice text editors like Visual Studio Code (vscode), Atom, Vim, Emacs, Notepad++ and others. I'd like to keep my notes in a version control system like git or hg.

I could write one note per file. How do I create links between notes? If I use Markdown, [reStructuredText](http://docutils.sourceforge.net/rst.html) (rST), [Textile](https://www.promptworks.com/textile), YAML or some other markup language, then I could embed links in notes. How do I create note sequences? Maybe I need a separate (somewhat automated) note to record a sequence of notes along a particular topic. That sequence note would be the one that gets a tag - the guideline being to limit tags to mark entry points into the note system rather than trying to include every applicable tag to every note.

If I have sequencing notes, then should my relational links be recorded in an external file, too? Probably not. I think I want to be able to reference other notes inline, like a wiki. Keeping relational links external is what one would do with a relational database, but that gets in the way of the flow of thought.

What information should be recorded on each note? Some of these features preclude using a plain text editor. It would be a pain in the butt, for example, to have to remember to edit a timestamp for the last time a note was updated. Maybe that meta data isn't so important - or, if each note is contained in a distinct file, the file system will keep track of that.

- Does each note need its own title?
- A unique ID. I like the convention of creating one file per note, where the file name is the ID followed by a title/subject. I found this idea while reading about [one person](http://zettelkasten.de/posts/one-note-review/), who uses Microsoft OneNote for his Zettelkasten. He assigns a number in sequence, starting with `1` for the first note. He puts the letter `n` in front of each number ID, so his ID sequences are `n1`, `n2`, `n3`, and so on. When he searches for notes by ID, he might searche for ID `n268`. Each title is prefixed by the note ID, so not only does he find a note like `n268. Mindfulness ...`, but he finds notes with a link to that note. They are displayed in a list like:
  - `n95. Mindfulness & Creativity`
  - `n71. Living in the past`
  - `n70. Living for the future`
  - `n61. Eating`
- If each note is contained in its own file, what is the file name? Should it represent the note's title, ID, creation date or should it be based on something else?
- Creation timestamp (date and time in some nice format). Rely on the file system.
- A timestamp for the last time it was updated. Rely on the file system.
- The content of the note. I suppose most notes will be plain text, but some could be code snippets in some programming language, and other files could be supporting data in a variety of formats including binary data, like images, sound, video, executables, etc.

So, I think I'll start with a file name convention of `n# Title.ext`, where each file name starts with the letter `n`, `#` is the number of the note, the Title is basically the subject of the note, and `.ext` is the file name extension. I'll use conventional file name extensions, like `.txt`, `.md`, `.rst` and others as needed.

The next convention is to use some kind of markup to indicate a reference to another note. It can be as simple as `==>n42` to link to note `n42`, or for a Markdown file, I might link to another file using Markdown syntax: [n42](n42 My fun idea.md).

Initially, I'll keep the system as simple as possible with a set of plain text files in a directory. Maybe I can migrate all my notes from org-mode and Jekyll into something a little easier to navigate.

### Zettelkasten References

- [Niklas Luhmann's Index Card System Prefigures Hypertext, 1956](http://www.ft.com/cms/s/0/fbbbf0c2-bdb6-11dd-bba1-0000779fd18c.html?ft_site=falcon&desktop=true)
- [Luhmann's Zettelkasten](http://takingnotenow.blogspot.com/2007/12/luhmanns-zettelkasten.html)
- [A Faithful Electronic Version of Luhmann's Zettelkastern](http://takingnotenow.blogspot.com/2007/12/faithful-electronic-version-of-luhmanns.html).
- [Zkn3](http://zettelkasten.danielluedecke.de/en/index.php).
- [Synapsen - a hypertextual Card Index](http://www.verzetteln.de/synapsen/index_e.html)
- [Create a Zettelkasten for your Notes to Improve Thinking and Writing](http://zettelkasten.de/posts/zettelkasten-improves-thinking-writing/)
- [ConnectedText](http://www.connectedtext.com/).
- [ConnectedText tutorials](https://drandus.wordpress.com/connectedtext-tutorials/).
- [Long Term Usage review of ConnectedText](https://pauljmiller.wordpress.com/2015/01/25/long-term-usage-review-of-connectedtext/), a review from 2015.
- [Setting up ConnectedText](https://drandus.wordpress.com/2012/09/30/setting-up-connectedtext/).
- [Ultra Recall](http://www.kinook.com/UltraRecall/).
- [Review of Ultra Recall](https://pauljmiller.wordpress.com/2014/02/22/review-of-ultra-recall/) from 2014.
- [MyInfo 6 free form personal organizer](http://www.milenix.com/myinfo).
- [Review of MyInfo](https://pauljmiller.wordpress.com/2013/11/16/review-of-myinfo/) from 2013.
- [InfoQube Information Management Software](http://www.infoqube.biz/).
- [Haystack](http://groups.csail.mit.edu/haystack/)
- [Haystack blog](http://haystack.csail.mit.edu/blog/).

## The Semantic Web
Is it all about structured data? If so, then some notes here might apply to what I'm trying to make with my note taking efforts and learning about Zettelkasten. There's an article on the Haystack blog, [Keynote at ESWC Part 3: What's Wrong with Semantic Web Research, and Some Ideas to Fix it](http://haystack.csail.mit.edu/blog/2013/06/10/keynote-at-eswc-part-3-whats-wrong-with-semantic-web-research-and-some-ideas-to-fix-it/), that seems interesting at first glance. Note that this blog post is from Monday, June 10, 2013.

It starts as a rant about the lack of end-user applications that can be used with any schema, permitting end users to adapt their schemas as they see fit.

- The curent state of tools for end users to cpature, manage, and communicate their information is terrible.
- The Semantic Web presents a key part of the answer to building better tools.
- Not enough work is being directed toward this problem by the community.

Everyone seems to be working on theories and studies of knowledge representation, inference and ontologies. These are areas studied by the AI community, and may not be so important for the Semantic Web.

    We have to describe specific end-user problems and demonstrate specific Semantic Web applications taht will solve those problems. ... If we fail to do that, if we create hammers without nails, I doubt we'll ever build the right hammers. Someone else will solve those problems without using Semantic Web tools, and the Semantic Web will be lieft behind.

The author lists four example applications that solve real end-user problems (and I think he went more deeply into those applications in [part 2](http://haystack.csail.mit.edu/blog/2013/06/06/keynote-at-eswc-part-2-how-the-semantic-web-can-help-end-users/)). The apps are:

- Haystack, which enables personal information management and integration under your own schema. See the paper "End-User Application Development for the Semantic Web.
- Related Worksheets, which is supposed to make spreadsheets work better (see the paper "A Spreadsheet-Based User Interface for Managing Plural Relationships in Structured Data).
- Exhibit for publishing cool interactive data visualizations. See the [Exhibit website](http://simile-widgets.org/exhibit/). It says Exhibit lets you easily create web pages with advanced text search and filtering functionalities, with interactive maps, timelines, and other visualizations. Also, refer to
  - [Exhibit version 2](http://www.simile-widgets.org/exhibit2/)
  - [Exhibit 3.0](http://www.simile-widgets.org/exhibit3/), a publishing framework for large-scale data-rich interactive web pages.
- Automate to automatically cope with incoming information streams. See the paper "Automate It! End-user Context-Senstive Automation using Heterogeneous Information Sources on the Web"

## Toolchain Contenders

- [Jekyll](http://jekyllrb.com/)
- [Compass](http://compass-style.org/)
- [AsciiDoctor](http://asciidoctor.org/)
- [Scribble](https://docs.racket-lang.org/scribble/index.html)
- [Pollen](http://docs.racket-lang.org/pollen/)
- [Sphinx](http://www.sphinx-doc.org/en/stable/)
- [Madoko](https://www.madoko.net/) ([souce code](http://madoko.codeplex.com/))
- [Pandoc](http://pandoc.org/)

## Jekyll: The Good and the Bad
Jekyll has a lot of good things going for it. It turns Github Markdown into HTML and it can automatically update the output files. By adding the `Hawkins` gem, Jekyll will inject `LiveReload.js` so the browser will automatically refresh without needing to install the LiveReload browser extension.

The configuration file, `_config.yml`, is in [YAML](http://yaml.org/) and each post has YAML front matter which can override defaults in the configuration file. The default directories for layouts, include files and posts are a good idea, too.

On the other hand, Jekyll is slow and has touchy dependencies and configuration. I'd also like a tool that allows me to explore formats other than Markdown and Textile. Specifically, I'd like to use [reStructuredText](http://docutils.sourceforge.net/rst.html), [Asciidoc](http://asciidoc.org/) and possibly LaTeX.

The documentation still leaves a lot of unanswered questions.

- What's the `_data` directory for and how does it get processed?
- Defaults are not well documented, nor are global settings and what the YAML front matter can override.
- Why does the [plugins page](https://jekyllrb.com/docs/plugins/) say GitHub pages are generated with the `--safe` option to disable custom plugins, but there's no documentation or even acknowledgement of such an option when I run `bundle exec jekyll help build`?
- The [plugins page](https://jekyllrb.com/docs/plugins/) talks about adding gems to your `_config.ym` file and shows `jekyll-watch` as an example, but there's no mention of what `jekyll-watch` does. Is this an obsolete gem?

I also don't like that each post file must have a date in its name. This naming convention makes it more difficult to find a post on a specific topic.

Posts written for the Jekyll ecosystem are text files with mixed markup. They have YAML front matter, Github-style Markdown for most text and can embed Liquid Template code/markup, such as I have done to create a table of contents for this post.

Personally, I'd like to get off the Ruby ecosystem. Bundler and its Gemfile configuration system does help, but I'm finding Jekyll and its support system of gems are too slow for a small set of notes. I can't see it handling all that I want to write.

## Compass
Similar to Jekyll, Compass has a watch-mode (`compass watch`) to update CSS stylesheets when the Sass files change. Like Jekyll, the authors wrote Compass in Ruby. Its configuration file is `config.rb`. My version looks like:

```ruby
require 'compass/import-once/activate'
# Require any additional compass plugins here.

# Set this to the root of your project when deployed:
http_path = "/"
css_dir = "css"
sass_dir = "_sass"
images_dir = "img"
javascripts_dir = "js"
fonts_dir = "fonts"
```

All of the Sass files are in `_sass`, while the output is in `css`. It looks like Compass comes with some predefined mixins and stylesheets. See the [GitHub repo](https://github.com/Compass/compass) for details. Sadly, Compass has not been updated in the last two years. The its limitations (like only supporting `.png` sprites using [chunky_png](https://github.com/wvanbergen/chunky_png)) will remain. Hopefully, Compass will continue to work with the gems on which it depends.

## AsciiDoctor
Like Markdown, AsciiDoc is a plain-text markup language. [AsciiDoctor](http://asciidoctor.org/) is like Jekyll. It is part of a toolchain for [rendering and creating a live preview](http://asciidoctor.org/docs/editing-asciidoc-with-live-preview/) in HTML of the AsciiDoc documents you write. It is also a Ruby gem, so you can use bundler to add it and the file monitoring tools `guard` and `guard-shell` to your environment.

## Scribble
[Scribble](https://docs.racket-lang.org/scribble/index.html) is a collection of tools for creating prose documents. It is written in Racket Scheme and seems to be very sophisticated. I think I can use it to write documents that look good, but I'll have to provide a web server, for example, to view the HTML output in a browser. Its advantage is it renders output in a variety of formats. The web page lists:

- Text
- Markdown
- HTML
- LaTeX
- PDF
- Contract (Blue boxes)

So, Scribble enables me to write documents in its format and translate them into HTML, PDF and other forms. It doesn't enable me to author documents in reStructuredText, Asciidoc or Markdown. On the other hand, I could probably figure out how to modify the HTML renderer so it injects `LiveReload.js`.

## Pollen
Pollen is a publishing system written on top of Scribble. Its purpose is to help authors make functional and beautiful digital books. Also, because digital books are software, an author shouldn't think of a book as merely data. The book is a program. The way we make digital books better than their predecessors is by exploiting this programmability.

You create Pollen books starting with the markup-based Pollen language. WHen you want to automate repetitive tasks, add cross-references, or pull in data from other sources, you access a full programming language, Racket, from within the text.

It has a built-in web server. The browser will automatically refresh when a source files changes. Matthew Butterick is the author of Pollen, and one of his goals is to replace LaTeX with Pollen. He'd like to make Pollen produce PDF output.

The lozenge character, ◊, is the "command" character. Its Unicode value is U+25CA.

To type Unicode characters on Windows, first create the registry value `EnableHexNumpad` of type `REG_SZ` under the registry key `HKEY_CURRENT_USER\Control Panel\Input Method`. Set its value to 1 and reboot. Now Unicode characters can be entered while holding down the `Alt` key, pressing `+` on the number pad and typing the hexadecimal value of the character. When you release the `Alt` key the character will appear.

## Requirements
Wouldn't it be nice if the editor could just render a view of the final document in another window? [Visual Studio Code](https://code.visualstudio.com/) and [Atom](https://atom.io/) will do that for Markdown files.

The tools I want will also be a record of my thoughts on building software development environments for exploring various aspects of software. For example, I want an environment for exploring game mechanics. What's the minimum framework I need? How much does ones choice of programming language matter? What tools work well together? What tools do I need to generate assets, or just load assets that already exist?

Live coding is a real need. One cool thing about the [Hawkins gem](https://github.com/awood/hawkins) is that it works. Once that gem is installed and the browser has the [LiveReload extension](https://github.com/livereload/livereload-extensions) installed, I just run `bundle exec Jekyll liveserve --port 4004`. Each time I save a post or other watched file, the browser updates after Jekyll has regenerated the site. It still takes seven or eight second to regenerate and it doesn't work under the `--incremental` command-line option.

NOTE: try running `bundle exec jekyll liveserve --reload-port 35730 --port 4000` to make LiveReload listen on another port (its default port is 35729).

Tools should process changes to code or documentation quickly and display the results. If it's a markup language and the output is HTML, then the tools should render the HTML quickly and make it available for a browser to display. If it is new code, then compile or interpret it quickly so the developer can see the results nearly instantly.

## Ideas
Jekyll embodies a lot of good ideas on setting conventions. It also uses other tools to get some things done. For example, it uses kramdown for syntax highlighting, and it has a [liquid templates](https://shopify.github.io/liquid/) engine which makes it easy to create templates for web pages and fill them in with chunks of HTML.

I think one way to go is to create templates and template engines for each aspect of software or notes I want to explore. The Liquid template engine, [sadly written in Ruby](https://github.com/Shopify/liquid), allows one to create consistent web pages with variable content. Sass is a tool for creating better and more consistent CSS.

I like C and C++. I'd like to explore Python 3, Haskell and some other programming languages. I like the idea of programmable tools. Take a look at the [Spaceship Generator](https://github.com/a1studmuffin/SpaceshipGenerator/) project. It is a procedural generation algorithm written in Python to drive Blender produce 3D spaceships. It's an inspiration for creating prototypes and exploring design.

Why not apply similar ideas to writing and software development. I'm not sure where to start, but templates, engines to parse the templates and generate output seem like a good model. An architecture must allow for extensions and plug-ins, and for separating the format of inputs and outputs.

There's a [YAML parser](https://github.com/jbeder/yaml-cpp/) written in C++ that parses the latest version of YAML 1.2, also known as the 3rd edition. It also has an emitter for creating well-formed YAML to a stream. The [YAML site](http://yaml.org/) has links to several other YAML parsers.

Tools should be programmable through a scripting language like Python or [Lua](https://www.lua.org).

### Keep the Environment Organized
A good directory layout can help keep files organized. Jekyll does this well. The Go programming language and the simple directory hierarchy Casey Muratori uses for [Handmade Hero](https://handmadehero.org/) are also good models.

#### Go Workspace
Go code is kept in a _workspace_. A workspace contains _many_ source repositories (that is, `git` or `mercurial` repositories). The Go tool understands the layout of a workspace. You don't need a `Makefile`. The file and directory layout contain all the necessary information.

A Go workspace looks like this:

```term
$GOPATH/
    src/
        github.com/user/repo/
            mypkg/
                mysrc1.go
                mysrc2.go
            cmd/mycmd/
                main.go
    bin/
        mycmd
```

Making a workspace is as simple as:

```term
mkdir /tmp/gows
GOPATH=/tmp/gows
```

The `GOPATH` environment variable tells the Go tool where your workspace is.

You can find more information about Go workspaces here:

- [Organizing Go Code](https://talks.golang.org/2014/organizeio.slide#1)
- [How to Write Go Code](https://golang.org/doc/code.html)

#### Handmade Hero Workspace
It's as simple a directory layout as anyone could ask for. There are four directories. A `/handmade/code` directory for all C source files and headers, `/handmade/misc` for shell scripts, editor configuration and other stuff, `/handmade/data` for test assets and `/build` where all the build results go.

```term
w:\
    handmade\
        code\
        data\
        misc\
    build\
```

## Resources & References

- [Gwern](https://www.gwern.net/index) is a blog that has just about everything I want for my blog. Its technological distinctiveness should be carefully added to this blog's own. Resistance is futile. Note that the site uses jQuery, and the tablesorter.js is probably the one [documented here](https://mottie.github.io/tablesorter/docs/) and [listed here](https://plugins.jquery.com/tablesorter/).
- [Hugo ReStructured](https://github.com/fisodd/hugo-restructured) a fisodd github repo.
- [A ReStructuredText Primer](https://www.fisodd.org/rest/quickstart/) a fisodd.org blog post.
- [reStructuredText Demonstration](https://www.fisodd.org/rest/rst-demo/) a fisodd.org blog post.
- [Hugo and reStructuredText](https://www.fisodd.org/rest/hugo-and-restructuredtext/) a fisodd.org blog post.
- [Support in Hugo for using reST](https://github.com/gohugoio/hugo/issues/472) a (closed) Hugo issue.
- [Abandoned go-rst parser](https://github.com/demizer/go-rst). It implements 28 of 283 items of the official specification. It does [have a breakdown](https://github.com/demizer/go-rst/blob/master/doc/README.rst) of what's implmented, and a [roadmap](https://github.com/demizer/go-rst/blob/master/doc/implementation.rst#roadmap). It might be worth taking over.
- [Discussion of native reST parser for Hugo](https://github.com/gohugoio/hugo/issues/1436) has some interesting background.
- [hhatto/gorst](https://github.com/hhatto/gorst) is another attempt to create a Go-based parser for reST.
- [rst2html5](https://pypi.org/project/rst2html5/) generates (X)HTML5 documents from standalone reStructuredText sources. It is a complete rewrite of the docutils’ ``rst2html`` and uses new HTML5 constructs such as ``<section>`` and ``<aside>``. Install: ``pip install rst2html5``. Usage: ``rst2html5 [options] SOURCE``.
- [reStructuredText Markup Specification](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html).
- [Reference reST Parser](https://repo.or.cz/docutils.git/tree/HEAD:/docutils/docutils/parsers/rst).
- [Problems with StructuredText](https://docutils.readthedocs.io/en/sphinx-docs/dev/rst/problems.html).
- [reST tests](https://repo.or.cz/docutils.git/tree/HEAD:/docutils/test/test_parsers/test_rst) from the [reference implmentation](https://repo.or.cz/docutils.git).
- [Sphinx Documentation Generator](http://www.sphinx-doc.org/en/stable/) renders HTML, LaTeX, ePub, Texinfo, manual pages and plain text from reStructuredText.
- [Scribble: The Racket Documentation Tool](https://docs.racket-lang.org/scribble/index.html)
- [LiveReload Application](https://github.com/livereload/LiveReload) source code.
- [LiveReload.js](https://github.com/livereload/livereload-js). If this script is on your web page, and an appropriately configured web server is running, then it creates a web socket and listens for incoming change notifications. When someone changes a CSS or image file, the script refreshes the effected portions of the web page w/o reloading the page. When you change any other file, the script reloads the page. The server notifies the client (this script) when to refresh the page. Available servers are:
  - [LiveReload app for Mac](http://livereload.com/).
  - [rack-livereload](https://github.com/johnbintz/rack-livereload).
  - [guard-livereload](https://github.com/guard/guard-livereload).
  - [grunt-contrib-watch](https://github.com/gruntjs/grunt-contrib-watch).
  - Jekyll with the [Hawkins gem](https://github.com/awood/hawkins) plug-in.
  - write your own: refer to the [LiveReload protocol](http://help.livereload.com/kb/ecosystem/livereload-protocol).
- Other LiveReload Resources
  - [LiveReload Plugin Repository](https://github.com/livereload/livereload-plugins).
  - [LiveReload JavaScript Client Code](https://github.com/livereload/livereload-js).
  - [LiveReload Browser Extensions Repository](https://github.com/livereload/livereload-extensions).
  - [The Story of LiveReload](http://tarantsov.com/blog/2011/07/the-story-of-livereload-the-first-anniversary/).
  - [LiveReload Screencast Walkthrough](https://www.youtube.com/watch?v=EZ8vy_cNMVQ).
- [Janson Repository](https://github.com/akheron/jansson). [Jansson](http://www.digip.org/jansson/) is a C library for encoding, decoding and manipulating JSON data. LiveReload 2 depends on it.
- [WebPutty Repository](https://github.com/FogCreek/WebPutty/).
- [WebPutty Overview Video](https://www.youtube.com/watch?v=FNaN789JsUc).
- [HTML5 Web Socket Implementation Powered by Flash](https://github.com/gimite/web-socket-js). Hawkins can optionally use `WebSocketMain.swf`, but doesn't have to. The source code for `WebSocketMain.swf` is in this repo.

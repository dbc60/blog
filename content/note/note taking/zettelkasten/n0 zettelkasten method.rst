.. index:: ! zettelkasten
.. _zettelkasten method:

###################
Zettelkasten Method
###################

I've recently (March 19, 2017) come across a method, and even philosophy, of `note taking called Zettelkasten <http://takingnotenow.blogspot.com/2007/12/luhmanns-zettelkasten.html>`_. In the original method, created by the German sociologist Niklas Luhmann (1927-1998), index cards are used for recording short notes. What's fascinating about the method is that Luhmann claimed his file was something of a collaborator in his work. The index cards were organized in such a way that it enabled him to discover new connections among different thoughts and subjects.

Each card is indexed with a number independent of the information on it, starting with 1. Index cards are small, so it's often necessary to continue a thought on other cards. The first cards would be numbered ``1/1``, the next ``1/2``, ``1/3``, and so on. He wrote these numbers in black ink at the top of the card so they could easily be seen in the file, and returned to the correct place.

In addition to recording a linear continuation of a topic on different cards, Luhmann also introduced a notation for branching topics. When he felt a term needed to be further discussed or he wanted to add more information, he would start a new card that had the same number as the card from which he was supplementing and would add a letter to the new card's index. To branch from card ``1/6``, he would create a new card and mark it as ``1/6a``. Branches might require further continuations, so there would be cards marked ``1/6a1``, ``1/6a2``, ``1/6a3``, and so on. Of course, any of these continuations could be branched again. He wound up with labels as long as ``21/3d26g53`` - the number of a card discussing his academic rival, Jurgen Habermas.

It seems that the method is to write down a thought on a card and assign the next number followed by ``/1``. For example, ``1/1`` for your first card. If the thought won't fit on a single card, then continue it on another card and label that ``1/2``.

While reflecting on cards you've written, if you need to expand on a topic, then create another card, label it with the label from the original card and append ``a1``. Similarly, to follow a train of thought in a different direction from the same card, you'd label a new card with the label from the original card and append ``b1`` to it. So, two separate trains of thought from card ``12/3`` would start with ``12/3a1`` and ``12/3b1``. If each of those trains of thoughts required more than one card, the ``a1`` sequence of cards would be labeled ``12/3a1``, ``12/3a2``, ``12/3a3``, ..., while the ``b1`` sequence would be labeled ``12/3b1``, ``12/3b2``, ``12/3b3``, etc.

In addition to sequencing cards for a single train of thought, and branching from a card to a more detailed treatment of some aspect of a topic, cards can directly reference each other. Just record one card's label in the body of another cards to create a link. By this method, Luhmann created a manual form of Hypertext and the World Wide Web, but just for his thoughts and interests - or maybe a mind map.

************************************************
Luhmann's Principle of Organizing a Zettelkasten
************************************************

Luhmann's principle of organizing Zettelkasten has four parts.

* No categories
* Use linkage/references among notes
* Use a register of tags
* Allow arbitrary branching of note sequences.

Categories and Tagging
======================

Placing notes in categories doesn't scale. More often than not, a note will belong to more than one category. Tagging has been used to in several editors as a substitute for categories. Each note can have multiple tags, where tags represent categories. The problem with tags is collecting or linking notes with identical tags can be difficult. The spelling must be identical to enable basic text searches to automatically link notes via tags. Also, the number of tags can easily become unmanageable, making it hard to remember which tags have been used so new notes link with previous ones.

No categories, because categories for an internal structure on the notes, and are not flexible. It does mean that each note must have fixed position in the collection and a unique ID indicating its position. A fixed position creates an implicit linkage among related notes, and enables fast retrieval of specific notes. If one note references another, it's easy to find that note.

Daniel says that an electronic Zettelkasten doesn't require notes to have fixed positions. I'm not sure about that. Even though an electronic Zettlekasten can follow links, how do you manually find the specific note to which you want to create a link? There must be some way to search, or some kind of index that can be referenced. I'd like such a system to inform me rather than requiring me to search for what I want.

Links and References
====================

The principle of links and references is one solution for managing notes. Like a wiki, creating direct links between notes allows for both thematic and non-thematic linkage. It makes it possible to explore notes that are not directly related via the link path, by navigating over a set of ordered notes within a theme. The problem with links is that it is difficult to retrive specific notes. Workflow may be poor, due to the limited scope of linkage - I'm not sure what Daniel means by this.

Use linkage/reference among notes. Unique IDs allow selective or specific links/references between notes. The number of links/references, in theory, is unlimited. It solves the problem of "multiple storage"; that is, if a note does not fit into a single category, build relations between multiple notes with links/references. Links and references also enables one to put notes in different contexts.

There are at least three types of links that can be used in a Zettelkasten. There are external links, such as hyperlinks to external resources - like a page on a website. 

Another common link is an internal link. It connects one note to another.

Finally, there are backlinks that should be automatically generated. It can be handy to have backlinks that show which notes refer to a given note.

.. _keyword-register:

The Keyword Register
====================

Luhmann maintained a separate register with core keywords (tags), which referenced selected notes. The purpose of this register was to find an "entrance" or starting point into the Zettelkasten. In certain cases, the notes also had tags, but *tags don't have the primary purpose to create links between notes*.

Use a register of tags instead of tagging each note. A separate register lists core keywords (the tags), and each tag lists selected (not all) notes that are considered entrance/starting points for the subject/category represented by the tag.

Generally, notes don't contain tags. The tags exist only in this register. In other words, tags don't exist to create links between notes. Their primary purpose is to mark starting points for a category. From the example Daniel provides, the register is also made up of short notes (Zettels), so each one has a unique, positional ID. Instead of a note on a subject, the register's Zettels contain lists of keywords, where each keyword is followed by one or more references to notes. It's possible that several keywords will reference the same note.

Brilliant! Yet, how does one control the proliferation of tags?

Allow Arbitrary Branching of Note Sequences
===========================================

Notes can be concatenated, resulting in note sequences. This is necessary in a physical Zettelkasten due to limited space on note papers. In an electronic Zettelkasten, no text limits for notes, however it is also recommened to keep notes short. New topics or subtopics can branch off from ntoes in a sequence, leading to a tree structure of note relationships. Branching and note sequences allow for "story telling". To some degree, branching and sequences are developing or evolving texts on a specific topic (sequence) or side topics (branching). Branching allows reduction of complexity concerning tags and the register (fewer entrance points).

*****************************
Combining all Four Techniques
*****************************

The key to Luhmann's Zettelkasten is to combine all of these techniques: note sequences and branching, in combination with tags in a register and links/references. Here's what Luhmann did:

* Write down an idea
* Develop the idea with an implicit sequence of notes and note IDs.
* Add side topics or subtopics as the idea develops. The form of his unique IDs show how the sequence of notes branch to related topics/subtopics. It keeps their relationships intact.
* Add manual links/references between relevant notes, creating a system/network of "relationships of relationships". It shows the "story" from one topic to a side or sub topic is linked or related to the story of that first topic to another side or sub topic.
* Add keywords to the register

To summarize his principles, we should write small notes using note sequences to develop an idea or topic. Where possible or necessary (that is, if an idea can be considered as the start of a new note sequence, but does not fit into the current linear line of thought), branch off a new idea path. Check if a similar topic or story line has been written elsewhere. If so, add manual links/references between the two (I'd guess between the two starting notes). Identify relevant notes that function as starting points, and add these to the tag register.

Another view of a workflow:

* Think about the topic or subject where a new note fits
* Find a starting point in the Zettelkasten realted to this topic and start reading/exploring your existing notes (sequences).
* Decide whether the note is

  * the start of a new topic/sequence
  * fits into an existing note sequence (continuing an existing note sequence)
  * fits into an existing not sequence (but branching off a new subtopic)

Depending on where the note joins or fits into the Zettelkasten, think about tagging your note. Which (parallel) note sequences are related to this note? Are there relevant notes in other sequences? If yes, add manual links between notes. Less is beautiful: Better use fewer keywords. For example, use keywords only for notes that start a new note sequence, for those notes that branch off inside a sequence, or for very important "key notes."

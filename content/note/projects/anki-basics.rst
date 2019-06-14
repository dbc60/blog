---
title: "Anki Basics"
date: 2019-06-08T07:29:35-04:00
draft: true
categories: [tools]
tags: [anki, css, web]
---

The `Anki manual <https://apps.ankiweb.net/docs/manual.html>`_ covers lots of details about Anki. Here are some notes `about the basics <https://apps.ankiweb.net/docs/manual.html#the-basics>`_.
<!--more-->

###########
Definitions
###########

**Card:**
    A question and answer pair. It is similar to a paper flashcard, with a
    question on one side and an answer on the other.

    In Anki, a card is built from each card type in a note.

**Deck:**
    A collection of cards. Each deck can have different settings, such as how
    many new cards to show each day, or how long to wait until cards are shown
    again.

    Decks can contain other decks on a parent-child relationship. A deck
    within another deck is called a subdeck. A deck containing other decks is
    called either the parent deck or the superdeck.

**Note:**
    A note seems to be a collection of fields and card types. Notes can be
    managed separately from the cards built from them. In Anki, click on the
    Tools menu and select Manage Note Types (or press ``Ctrl+Shift+N``) to
    open the Note Types dialog.

    The Anki manual says a note contains information that will be displayed on
    each card built from the note, and fields which will be filled in by each
    card. For example, a deck of cards for studying French and English might
    be built from a note containing a field for a word in French and another
    field for the English word. A fancier note might contain fields for a
    sample sentence using the word, or two audio fields to hold a recording of
    the word, one in French and the other in English.

**Field:**
    A field is a piece of information that can be included in a note.

**Card Type:**
    A blueprint for a card that says which fields from a note should be
    displayed on the front or back of each card.

    Each card type has two *templates*, one for the question and one for the answer.

    Each type of note can have one or more card types; when you add a note,
    Anki will create one card for each card type.

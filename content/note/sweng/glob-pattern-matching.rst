---
title: "Glob Pattern Matching"
date: 2019-08-15T12:50:06-04:00
draft: true
---

In computer programming glob patterns specify sets of filenames with wildcard characters. The `Wikipedia article <https://en.wikipedia.org/wiki/Glob_(programming)>`_ lists the common wildcards.
<!--more-->

The most common wildcards are ``*``, ``?``, ``[...]``.

.. table:: Wildcards
    :widths: auto

    ========  ==================================================================  =========== ========================================  ============================
    Wildcard  Description                                                         Example     Matches                                   Does Not Match
    ========  ==================================================================  =========== ========================================  ============================
    \*        Matches zero or more characters                                     Law*        Law, Laws, or Lawyer                      GrokLaw, La, or aw
    ?         Matches any single character                                        ?at         Cat, cat, Bat, or bat                     at
    [abc]     Matches one character given in the bracket                          [CB]at      Cat or Bat                                cat or bat
    [a-z]     Matches one character in the locale-dependent range in the bracket  Letter[0-9] Letter0, Letter1, Letter2, up to Letter9  Letters, Letter, or Letter10
    [!a]      Matches one character not declared in the bracket                   [!abcx-z]0  d0, w0, A0, X0                            a0, b0, c0. x0, y0, z0
    ========  ==================================================================  =========== ========================================  ============================

Globs do not include syntax for the Kleene star which specifies zero-or-more repetitions of the preceding part of the expression; thus globs are not regular expressions. What *looks* like a Kleene star is just a pattern for any sequence of characters up to a delimitor (such as a path separator). It is equivalent to the regular expression ``.*/?``, where ``/?`` is a path separator - or, for example, ``.*[/\\]?``, where both ``/`` and ``\`` are delimiting path separators.

When it comes to matching file and directory paths, ``*`` matches any number of characters except for a path separator. The wildcard only counts inside a file or folder name, so ``models/*.cfc`` will only match ``.cfc`` files in the root of the ``models`` folder. Likewise, ``?`` will match any character except a path separator.

Some glob matchers extend the set of wildcards to include ``**``, which will match any number of characters including path separators. To extend the previous example, if we did ``models/**.cfc`` that would match any ``.cfc`` file in any subdirectory, no matter how deep.

Here's some more examples of how the wildcards work::

  Match any file or folder starting with "foo":
  foo*

  Match any file or folder starting with "foo" and ending with ".txt":
  foo*.txt

  Match any file or folder ending with "foo":
  *foo

  Match "a/b/z" but not "a/b/c/z":
  a/*/z

  Match "a/z" and "a/b/z" and "a/b/c/z":
  a/**/z

  Match "hat" but not "ham" nor "h/t":
  h?t

I was thinking it might be okay to allow ``*`` to match any number of subdirectories, but that could get very confusing. You'd have to require something like ``models/*.txt`` to match within the ``models`` directory only, and ``models/*/*.txt`` to match any directory or sequence of subdirectories between ``models`` and ``*.txt``. There wouldn't be an easy way to specify just one subdirectory down.

There's a `Go glob pattern matching repo <https://github.com/gobwas/glob>`_ where delimitors can be defined. The README gives examples with different delimitors, such as a period or a letter. It defines ``**`` as an "super-asterisk" that ignores deliminitors.

It claims to be faster than regexes. Why is it so fast? Does it build a DFA for each glob? Does it do something more simple than regexes?

Note that globbing patterns have equivalent regular expressions, so it may be appropriate to implement globbing on top of an implementation of regular expressions. The mapping from globs to regexes is:

.. table:: Equivalent Globs and Regexes
    :widths: auto

    ============  ============================= =============================================================
    Glob Pattern  Equivalent Regular Expression Description
    ============  ============================= =============================================================
    ``?``         ``[!/\\]``                    matches any single character except for a path separator
    ``*``         ``[!/\\]*``                   matches zero or more characters except for path separators
    ``**``        ``.*``                        matches zero or more files to any directory depth.
    ``[abc]``     ``[abc]``                     matches one character given in the bracket.
    ``[a-z]``     ``[a-z]``                     matches one character from the (locale-dependent) range given in the bracket.
    ``[!abc]``    ``[!abc]``                    matches one character that is not given in the bracket.
    ``[!a-z]``    ``[!a-z]``                    matches one character that is not from the range given in the bracket.
    ============  ============================= =============================================================

#############################
Simple and Fast Glob Matching
#############################

It turns out `glob matching <glob matching can be simple and fast_>`_, too. The obvious implementation of glob pattern matching against a single path element is to walk the pattern and the name together, matching letters or wildcards in the pattern to letters in the name. If the walk reaches the end of the pattern at the same time as the end of the name, they match.

What may be more fruitful is to implment the glob pattern matching of Go's `filepath.Match method <https://golang.org/src/path/filepath/match.go>`_ in the kernel. It splits split the pattern on stars and then considers each of the star-separated subpatterns in turn, special-casing the first subpattern and the last, which must be anchored at the start and end of the string, respectively.

Here is one implementation. Each time the code encounters a star, it implements the repeated trials needed for that star by recording in ``nextPx``, ``nextNx`` where to restart the search if the current match fails. Each subsequent star encountered overwrites the restart information for the previous star, in effect locking in the choice made for the previous star.

.. code-block:: go

  // Match a name against a pattern. Return true/false to indicate whether the
  // name is matched by the pattern.
  func match(pattern, name string) bool {
    px := 0       // pattern index
    nx := 0       // name index
    nextPx := 0
    nextNx := 0
    for px < len(pattern) || nx < len(name) {
      if px < len(pattern) {
        c := pattern[px]
        switch c {
        default: // ordinary character
          if nx < len(name) && name[nx] == c {
            px++
            nx++
            continue
          }
        case '?': // single-character wildcard
          if nx < len(name) {
            px++
            nx++
            continue
          }
        case '*': // zero-or-more-character wildcard
          // Try to match at nx.
          // If that doesn't work out,
          // restart at nx+1 next.
          nextPx = px
          nextNx = nx + 1
          px++
          continue
        }
      }
      // Mismatch. Maybe restart.
      if 0 < nextNx && nextNx <= len(name) {
        px = nextPx
        nx = nextNx
        continue
      }
      return false
    }
    // Matched all of pattern to all of name. Success.
    return true
  }

An alternative implementation is to split the pattern on stars and then consider each of the star-separated subpatterns in turn, special-casing the first subpattern and the last, which must be anchored at the start and end of the name, respectively. This is how Go's `filepath/match.go <https://golang.org/src/path/filepath/match.go>`_ implementation is written.

Go's code uses a single ``scanChunk`` function that records if the pattern starts with one or more stars and then scans the pattern up to the next star or the end of the pattern. It returns three items:

* a boolean indicating the chunk is preceded by a star
* the chunk as a string
* the rest of the pattern as a string.


********************
QUESTIONABLE CONTENT
********************

We have four kinds of star patterns to handle instead of one, so our scan function could return an enum indicating which it found.

.. code-block:: c

  typedef enum StarPattern {
    StarPatternSingle,      // *
    StarPatternDouble,      // /**/
    StarPatternDoubleStart, // **/
    StarPatternDoubleEnd    // /**
  } StarPattern;

Do any of these cases need special handling? The first thing ``scanChunk`` does is collect multiple stars into a single star. It then collects characters and range patterns until it encounters another star that is not in a range pattern (between ``[`` and ``]``).

The ``Match`` function first handles the case of the chunk being just ``*``, which will match the remainder of the path unless the remainder contains a path separator.

Go's implementation of `filepath/match.go <https://golang.org/src/path/filepath/match.go>`_ follows.

.. code-block:: go

  // Match reports whether name matches the shell file name pattern.
  // The pattern syntax is:
  //
  //  pattern:
  //    { term }
  //  term:
  //    '*'         matches any sequence of non-Separator characters
  //    '?'         matches any single non-Separator character
  //    '[' [ '^' ] { character-range } ']'
  //                character class (must be non-empty)
  //    c           matches character c (c != '*', '?', '\\', '[')
  //    '\\' c      matches character c
  //
  //  character-range:
  //    c           matches character c (c != '\\', '-', ']')
  //    '\\' c      matches character c
  //    lo '-' hi   matches character c for lo <= c <= hi
  //
  // Match requires pattern to match all of name, not just a substring.
  // The only possible returned error is ErrBadPattern, when pattern
  // is malformed.
  //
  // On Windows, escaping is disabled. Instead, '\\' is treated as
  // path separator.
  //
  func Match(pattern, name string) (matched bool, err error) {
  Pattern:
    for len(pattern) > 0 {
      var star bool
      var chunk string
      star, chunk, pattern = scanChunk(pattern)
      if star && chunk == "" {
        // Trailing * matches rest of string unless it has a /.
        return !strings.Contains(name, string(Separator)), nil
      }
      // Look for match at current position.
      t, ok, err := matchChunk(chunk, name)
      // if we're the last chunk, make sure we've exhausted the name
      // otherwise we'll give a false result even if we could still match
      // using the star
      if ok && (len(t) == 0 || len(pattern) > 0) {
        name = t
        continue
      }
      if err != nil {
        return false, err
      }
      if star {
        // Look for match skipping i+1 bytes.
        // Cannot skip /.
        for i := 0; i < len(name) && name[i] != Separator; i++ {
          t, ok, err := matchChunk(chunk, name[i+1:])
          if ok {
            // if we're the last chunk, make sure we exhausted the name
            if len(pattern) == 0 && len(t) > 0 {
              continue
            }
            name = t
            continue Pattern
          }
          if err != nil {
            return false, err
          }
        }
      }
      return false, nil
    }
    return len(name) == 0, nil
  }

  // scanChunk gets the next segment of pattern, which is a non-star string
  // possibly preceded by a star.
  func scanChunk(pattern string) (star bool, chunk, rest string) {
    for len(pattern) > 0 && pattern[0] == '*' {
      pattern = pattern[1:]
      star = true
    }
    inrange := false
    var i int
  Scan:
    for i = 0; i < len(pattern); i++ {
      switch pattern[i] {
      case '\\':
        if runtime.GOOS != "windows" {
          // error check handled in matchChunk: bad pattern.
          if i+1 < len(pattern) {
            i++
          }
        }
      case '[':
        inrange = true
      case ']':
        inrange = false
      case '*':
        if !inrange {
          break Scan
        }
      }
    }
    return star, pattern[0:i], pattern[i:]
  }

  // matchChunk checks whether chunk matches the beginning of s.
  // If so, it returns the remainder of s (after the match).
  // Chunk is all single-character operators: literals, char classes, and ?.
  func matchChunk(chunk, s string) (rest string, ok bool, err error) {
    for len(chunk) > 0 {
      if len(s) == 0 {
        return
      }
      switch chunk[0] {
      case '[':
        // character class
        r, n := utf8.DecodeRuneInString(s)
        s = s[n:]
        chunk = chunk[1:]
        // We can't end right after '[', we're expecting at least
        // a closing bracket and possibly a caret.
        if len(chunk) == 0 {
          err = ErrBadPattern
          return
        }
        // possibly negated
        negated := chunk[0] == '^'
        if negated {
          chunk = chunk[1:]
        }
        // parse all ranges
        match := false
        nrange := 0
        for {
          if len(chunk) > 0 && chunk[0] == ']' && nrange > 0 {
            chunk = chunk[1:]
            break
          }
          var lo, hi rune
          if lo, chunk, err = getEsc(chunk); err != nil {
            return
          }
          hi = lo
          if chunk[0] == '-' {
            if hi, chunk, err = getEsc(chunk[1:]); err != nil {
              return
            }
          }
          if lo <= r && r <= hi {
            match = true
          }
          nrange++
        }
        if match == negated {
          return
        }

      case '?':
        if s[0] == Separator {
          return
        }
        _, n := utf8.DecodeRuneInString(s)
        s = s[n:]
        chunk = chunk[1:]

      case '\\':
        if runtime.GOOS != "windows" {
          chunk = chunk[1:]
          if len(chunk) == 0 {
            err = ErrBadPattern
            return
          }
        }
        fallthrough

      default:
        if chunk[0] != s[0] {
          return
        }
        s = s[1:]
        chunk = chunk[1:]
      }
    }
    return s, true, nil
  }

#########
Resources
#########

* `Regular Expression Matching in the Wild`_
* Runaway Regular Expressions: `Catastrophic Backtracking`_.

.. _regular expression matching in the wild: https://swtch.com/~rsc/regexp/regexp3.html
.. _russ cox: https://swtch.com/~rsc/
.. _catastrophic backtracking: https://www.regular-expressions.info/catastrophic.html
.. _glob matching can be simple and fast: https://research.swtch.com/glob

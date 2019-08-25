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
    ========  ==================================================================  =========== ========================================  ============================

Globs do not include syntax for the Kleene star which specifies zero-or-more repetitions of the preceding part of the expression; thus they are not considered regular expressions. What *looks* like a Kleene star is just a pattern for any sequence of characters up to a delimitor (such as a path separator). It is equivalent to the regular expression ``.*/?``, where ``/?`` is a path separator - or, for example, ``.*[/\\]?``, where both ``/`` and ``\`` are delimiting path separators.

When it comes to matching files in directory paths, ``*`` matches any number of characters within a file or folder name. The wildcard only counts inside a file or folder name, so ``models/*.cfc`` will only match ``cfc`` files in the root of the ``models`` folder. Likewise, ``?`` will match any character except a directory separator.

Some glob matchers extend the set of wildcards to include ``**``, which will match any number of characters across all directories. To extend the previous example, if we did ``models/**.cfc`` that would match any ``cfc`` file in any subdirectory, no matter how deep.

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

  Matches "hat" but not "ham" nor "h/t":
  /h?t

I was thinking it might be okay to allow ``*`` to match any number of subdirectories, but that could get very confusing. You'd have to require something like ``models/*.txt`` to match within the ``models`` directory only, and ``models/*/*.txt`` to match any directory or sequence of subdirectories between ``models`` and ``*.txt``. There wouldn't be an easy way to specify just one subdirectory down.

There's a `Go glob pattern matching repo <https://github.com/gobwas/glob>`_ where delimitors can be defined. The README gives examples with different delimitors, such as a period or a letter. It defines ``**`` as an "super-asterisk" that ignores deliminitors.

It claims to be faster than regexes. Why is it so fast? Does it build a DFA for each glob? Does it do something more simple than regexes?

Note that globbing patterns have equivalent regular expressions, so it may be appropriate to implement globbing on top of an implementation of regular expressions. The mapping from globs to regexes is:

.. table:: Equivalent Globs and Regexes
    :widths: auto

    ============  ============================= =============================================================
    Glob Pattern  Equivalent Regular Expression Description
    ============  ============================= =============================================================
    ``?``         ``.``                         matches any single character
    ``*``         ``.*``                        matches zero or more characters except for path separators
    ``**``        ``(.+/)*``                    matches zero or more files to any directory depth.
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

Here is one implementation. Each time the code encounters a star, it implements the repeated trials needed for that star by recording in nextPx, nextNx where to restart the search if the current match fails. Each subsequent star encountered overwrites the restart information for the previous star, in effect locking in the choice made for the previous star.

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

#########################
Regular Expression Syntax
#########################

The simplest regular expression is a single literal character. Except for metacharacters, literal characters match themselves. The metacharacters are ``*+?()|.\``. To match a metacharacter, escape it with a backslash. For example, ``\+`` matches a literal plus character, and ``\\`` matches a literal backslash.

Operators are the metacharacters ``*+?``, also known as repetition characters. For a regular expression :math:`e_1`

  * :math:`e_1*` matches a sequence of zero or more (possibly different) strings, each of which match :math:`e_1`.
  * :math:`e_1+` matches one or more.
  * :math:`e_1?` matches zero or one.

Parentheses, ``(`` and ``)`` are used to override operator precedence, and to make the order of operators explicit. For example, a sequence that starts with ``a`` and continues with zero or more ``b``'s is recognized by the regular expression ``ab*``. However, if you want to define a regular expression that recognizes zero or more sequences of ``a`` followed by ``b``, you would write ``(ab)*``.

The vertical bar, ``|``, defines a choice, or alternate regular expression. It represents the union of two regular expressions. For example, :math:`e_1|e_2` defines a regular expression that matches strings in the set of those matched by either :math:`e_1` or :math:`e_2`.

The period, ``.``, is a regular expression that matches a single character or rune.

The backslash, ``\`` is the escape character. It is used to match a literal metacharacter, as described above.

Concatenation is an operation that doesn't have an explicit metacharacter to denote its operation. It is simply defined by following one regular expression by another. Thus, :math:`e_1e_2` defines a regular expression that matches :math:`e_1` first, followed by :math:`e_2`.

Operator precedence, from highest to lowest, is

* repetition operators
* concatenation
* alternation

I'm not sure if any fancier regular expressions, such as character classes (like ``[a-z]``) or anchoring (i.e,  ``^`` and ``$`` for matching the beginning and end of a line) are needed. Think about character classes, though. They may provide a useful optimization over alternating among several runes or a range of runes.

######################################
Converting Regular Expressions to NFAs
######################################

In his 1951 research memorandum, Representation Of Events In Nerve Nets And Pinite Automata, Stephen Kleene proved that regular expressions and finite automata both describe regular languages. They are exactly equivalent in power. Every regular expression has an equivalent NFA (they match the same strings) and vice versa. It turns out that DFAs are also equivalent in power to NFAs and regular expressions.

There are multiple ways to translate regular expressions into NFAs. The method described here was first described by Thompson in his 1968 CACM paper.

`Russ Cox`_ describes the implementation of his regular expression library `RE2 <http://code.google.com/p/re2/source/browse/LICENSE>`_ in his article `Regular Expression Matching in the Wild`_. There he states

  In retrospect, I think the tree form and the Walker might have been a mistake. If recursion is not allowed (as is the case here), it might work better to avoid the recursive representation entirely, instead storing the parsed regular expression in `reverse Polish notation <http://en.wikipedia.org/wiki/Reverse_Polish_notation>`_ as in `Thompson's 1968 paper <http://swtch.com/~rsc/regexp/regexp1.html#thompson>`_ and this `example code <http://swtch.com/~rsc/regexp/nfa.c.txt>`_. If the RPN form recorded the maximum stack depth used in the expression, a traversal would allocate a stack of exactly that size and then zip through the representation in a single linear scan.

This sounds like a good idea. I think I'll try it. I also want to keep in mind that the minifilter may be able to get a performance boost by combining all rule paths into a single regular expression (adding alternation of all enabled rule paths). It should be possible for each match state to record the particular rule that was matched, as the rule ID is part of a FIM event.

I think the plan is:

#. Design a regular expression algorithm along the lines of Thompson's paper.
   * Convert a regular expression to postfix
   * Generate a NFA from the postfix representation
   * Convert the NFA to a DFA
   * Write an implementation in Go with the hope that a DFA can be built in user-space, packed into a single block of memory and passed to the kernel minifilter for use.
   * Write another implementation in C. At least the part that executes the DFA will have to be written in C so the minifilter will be able to execute it.
   * Execute the DFA to match against test strings
#. Convert glob patterns to regular expressions
#. Convert a set of glob patterns to a single regular expression, and then convert that to a DFA (via the algorithms developed above) where match states map to the rule(s) where the original globs were defined.

Converting a set of glob patterns to a single regular expression shouldn't be hard. It amounts to converting each glob to a regex, and then logically or-ing them together. Many regular expression packages implement this feature via a ``+`` or ``|`` operator

Caveat on converting a NFA to a DFA. It is important to learn what can be done and what Thompson did to mitigate a possible explosion of states in the DFA. Creating a NFA from a regular expression of length :math:`m` results in a NFA with :math:`O(m)` nodes. That's fine, but I've read in a couple of places that converting the NFA to a DFA can result in a DFA with :math:`O(2^m)` states. I suspect that is a naive conversion, and that at least for some pathological regular expressions, the number of states can be greatly reduced.

##############################
Initial Regex Algorithm Design
##############################

Thompson defined a three-stage, regular-expression compiler. Likewise, we'll conver the regex into an NFA in three steps. The first step is to ensure only syntactically correct regular expressions are accepted. The second step is to convert a regular expression from infix to reverse Polish notation (RPN, a.k.a, postfix form), while keeping track of the maximum stack-depth used by the regex.

RPN can be parsed recursively or with a stack. We use a stack for two related reasons. First, so-called "pathological" regular expressions can create deep recursive calls, possibly blowing the call stack. Second, with an explicit stack, we can more easily control its depth and set limits to mitigate the fallout from pathological cases.

Consider these operators when tokenizing a regex:

* RegexNoMatch: matches no strings
* RegexEmptyMatch: matches the empty string
* RegexLiteral: matches one rune (a character that could be UTF-8 or UTF-16. The kernel will use UTF-16 for matching runes).
* RegexLiteralString: matches a string, a sequence of runes.
* RegexConcat: matches the concatenation of two regexes.
* RegexAlternate: matches the union of two regexes.
* RegexStar: matches a regex zero or more times.
* RegexPlus: matches a regex one or more times.
* RegexOptional: (the question mark) matches a regex zero times or once.
* RegexAnyRune: (the period) matches any single rune.
* RegexErrorParse: an error has occurred while parsing the regex string.

****************
Infix to Postfix
****************

The general algorithm for converting an infix expression to a postfix expression uses a stack for holding operators. The idea is to scan the infix expression from beginning to end moving operands directly and using the stack to hold operators until they can be placed in the postfix expression.

An actual implementation that processes simple regular expressions (the repetition operators, alternation, and parenthesized subexpressions) doesn't need an explicit operator stack. Instead it can maintain a count of operands appended to the postfix expression, a count of alternation operators in process, and a stack of those values to handle parenthesized subexpressions. Proceed as follows:

* If the token is an operand (a character that is not an operator):

  * if there is more than one operand in the postfix expression, append a concatenation operator and decrement the count of operands.
  * append the new operand to the postfix expression and increment the operand count.

* if the token is one of the repetition operators (``*``, ``+``, or ``?``) it is already a postfix operator.

  * If there is at least one atom in the postfix expression, append the repetition operator to it.
  * otherwise, return an error indicating the regular expression is malformed.

* If the token is a left parenthesis:

  * if there is more than one operand in the postfix expression, append a concatenation operator to it and decrement the operand count.
  * push the count of operands and count of alternation operators on to the subexpression stack. Reset those counts to zero, so we can start counting them for the subexpression.

* If the token is a right parenthesis:

  * if there are no values on the subexpression stack, or if the operand count is zero, return an error about a malformed regular expression.
  * otherwise:

    * in a loop, decrement the operand count and if it is greater than zero append a concatenation operator to the postfix expression. Repeat until the operand count is zero.
    * in a loop, while the count of alternation operators is greater than zero, append an alternation operator to the postfix expression and decrement the count.
    * pop the counts of operands and alternation operators off the subexpression stack, restoring the previous counts.
    * increment the operand count due to the subexpression just processed.

* if the token is an alternation operator:

  * if the operand count is zero, return an error indicating the regular expression is malformed.
  * otherwise:

    * in a loop, decrement the operand count and as long as it's greater than zero, append a concatenation operator to the postfix expression.
    * increment the count of alternation operators.

* When the infix expression has been completely processed:

  * if the subexpression stack is not empty, return a malformed expression error.
  * otherwise:

    * in a loop, decrement the count of operands, and while it is greater than zero, append a concatenation operator to the postfix expression.
    * in a loop, while the alternation count is greater than zero, append an alternation operator to the postfix expression and then decrement the count of alternation operators.

.. code-block:: go

  package regex

  type RegexTokenType int

  const (
    RegexNoMatch        RegexTokenType = iota
    RegexEmptyMatch
    RegexLiteral
    RegexLiteralString
    RegexConcat
    RegexAlternate
    RegexStar
    RegexPlus
    RegexOptional
    RegexAnyRune
    // Parser errors
    RegexErrorParse
    RegexBadEscape          // bad escape sequence
    RegexBadCharClass       // bad character class
    RegexBadCharRange       // bad character class range
    RegexMissingBracket     // missing closing ]
    RegexMissingParen       // missing closing )
    RegexTrailingBackslash  // at end of regexp
    RegexRepeatArgument     // repeat argument missing, e.g. "*"
    RegexRepeatSize         // bad repetition argument
    RegexRepeatOp           // bad repetition operator
    RegexBadPerlOp          // bad perl operator
    RegexBadUTF8            // invalid UTF-8 in regexp
    RegexBadNamedCapture    // bad named capture  )

  type RegexToken struct {
    Type RegexTokenType
    Value string
  }

  func infixToPostfix(infixRegex string) chan *RegexToken {
    out := make(chan *RegexToken)
    go func(regex string) {
      // iterate over the runes
      for pos, r := range regex {
        switch r {
          case '(':
            // insert a concatentation operator iff not first value
            if pos > 0 {
              out <- &RegexToken{RegexConcat, "("}
            }
        }
      }
    }(infixRegex)
    return out
  }

################################
Pathological Regular Expressions
################################

One such case is ``(x+x+)+y``, which is equivalent to ``xx+y``. It means:

* One or more of the character X
* One or more of the character X
* One or more of the previous two matches combined
* Followed by a single character Y

Running this regex over a string of ``x``'s that doesn't end in ``y`` results in exponential backtracking for naive implementations.

Another pathological case is ``a*a*a*a*a*a*a*a*a*a*``, which is equivalent to ``a*``. In a naive implementation, this regular expression can generate a DFA with an excessive number of states, on the order of :math:`2^{20}`, instead of just a handful of states.

#########
Resources
#########

* `Regular Expression Matching in the Wild`_
* Runaway Regular Expressions: `Catastrophic Backtracking`_.

.. _regular expression matching in the wild: https://swtch.com/~rsc/regexp/regexp3.html
.. _russ cox: https://swtch.com/~rsc/
.. _catastrophic backtracking: https://www.regular-expressions.info/catastrophic.html
.. _glob matching can be simple and fast: https://research.swtch.com/glob

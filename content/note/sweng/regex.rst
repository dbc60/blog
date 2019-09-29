---
title: "Regular Expressions"
date: 2019-09-28T08:41:16-04:00
draft: true
---

These are some notes on regular expressions I gathered while I was working on a glob pattern-matching algorithm and implementation. I briefly considered creating a glob implementation with a regular expression implementation under the covers. That way I'd get two pattern-matching tools in one library. I later learned that there is an easier way to implement `glob pattern matching`_.
<!--more-->

.. _glob pattern matching:  {{< relref "glob-pattern-matching.rst" >}}

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

One such case is ``(x+x+)+y``, which is equivalent to ``(xx)+y``. It means:

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

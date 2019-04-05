---
title: Lexical Scanning in Go
date: 2019-04-05T05:26:00-05:00
draft: true
tags: [lexing, Scanning,golang]
categories: [programming]
---

Notes from Rob Pike's talk on [Lexical Scanning in Go][lexscantalk]

<!--more-->

## Template System
In the talk, he shows how the lexer works in Go's [text template system][gotexttemplate]. Here's some background on what the template system does.

Actions are contained within two pairs of braces. For example ``{{.Title}}`` will evaluate the field of some structure ``.Title``. There is an implicit context within which ``.Title`` is evaluated.

There are constants and function. For example, if you write ``{{printf "%g: %#3X" 1.2+2i 123}}```, the template system knows how to format the values and print/display the result.

There are also control structures, such as ``{{range $s.Text}} {{.}} {{end}}``` for looping.

## Lexing

To create tokens for a parser we must tokenize things like:

    the stuff outside actions
    action delimiters
    identifiers
    numeric constants
    string constants
    and others

Lexed items (lexemes) are represented by a type and a value. Where the value is concerned, all we need is a string:

```go
/// item represents a token returned from the scanner.
type item struct {
    typ itemType    // Type, such as itemNumber.
    val string      // Value, such as "23.2".
}
```

The type is just an integer constant.

```go
// itemType identifies the type of lex items.
type itemType int

const (
    itemError itemType = iota   // error occurred;
                                // value is text of error
    itemDot                     // the cursor, spelled '.'
    itemEOF
    itemElse        // else keyword
    itemEnd         // end keyword
    itemField       // identifier, starting with '.'
    itemIdentifier  // identifier
    itemIf          // if keyword
    itemLeftMeta    // left meta-string
    itemNumber      // number
    itemPipe        // pipe symbol
    itemRange       // range keyword
    itemRawString   // raw quoted string (includes quotes)
    itemRightMeta   // right meta-string
    itemString      // quoted string (includes quotes)
    itemText        // plain text
)
```

To print lexed values, define a ``String()`` method for ``item``:

```go
func (i item) String() string {
    switch i.typ {
        case itemEOF:
            return "EOF"
        case itemError:
            return i.val
    }
    // Avoid displaying really long values, such as big blocks of text.
    if len(i.val) > 10 {
        return fmt.Sprintf("%.10q...", i.val)
    }
    return fmt.Sprintf("%q", i.val)
}
```

## Tokenization

Typically people write a state machine via a switch statement:

```go
// one iteration:
switch state {
    case state1:
        state = action1()
    case state2:
        state = action2()
    case state3:
        state = action3()
}
```

The problem with this is that each time an action returns, we momentarily lose which state we're in. The code has to return to the switch statement and branch on the saved state to figure out which action is the next one to call.

What is a state, and what is an action? A state represetnts where we are and what we expect. An action represents what we do, and actions result in a new state.

Define a State Function that combines the concept of a state and an action. It executes an action, and returns the next state as a state function.

```go
// stateFn represents the state of the scanner
// as a function that returns the next state.
type stateFn func(*lexer) stateFn
```

The run loop looks like this.

```go
// run lexes the input by executing state functions
// until the state is nil.
func run() {
    for state := startState; state != nil; {
        state = state(lexer)
    }
}
```

## The Lexer

The problem is nowhere does any code pick up tokens. Tokens can emerge at times that are inconvenient to stop to return to the caller. Use concurrency. Run the state machine in a goroutine, and emit token values on a channel. The client (a parser, for example), receives those tokens on the channel. This allows the lexer and the parser to proceed at their own separate paces and synchronize when the lexer emits a token and the parser is ready to consume it.

Here is the definition of the ``lexer`` type. The important part is the channel of items.

```go
// lexer holds the state of the scanner.
type lexer struct {
    name    string      // used only for error reports.
    input   string      // the string being scanned.
    start   int         // start position of this item.
    pos     int         // current position in the input.
    width   int         // width of last run read.
    items   chan item   // channel of scanned items.
}
```

### Starting the Lexer

A lexer initializes ifself to lex a string and launches the state machine as a goroutine, returning the lexer itself and a channel of items. The API will change, don't worry about it now. This is a very early version of the code (circa 2011).

```go
func lex(name, input string) (*lexer, chan item) {
    l := &lexer{
        name:   name,
        input:  input,
        items:  make(chan item),
    }
    go l.run()  // Concurrently run state machine.
    return l, l.items
}
```

The real ``run`` routine is this.

```go
// run lexes the input by executing state functions until
// the state is nil.
func (l *lexer) run() {
    for state := lexText; state != nil; {
        state = state(l)
    }
    close(l.items)  // No more tokens will be delivered.
}
```

The emit method uses the lexer's ``start`` and ``pos`` fields to slice the input text string.

```go
// emit passes an item back to the client.
func (l *lexer) emit(t itemType) {
    l.items <- item{t.l.input[l.start:l.pos]}
    l.start = l.pos
}
```

Now we need a start state, which is the function ``lexText``. We define a constant, ``leftMeta``, which is what ``lexText`` will look for.

```go
const leftMeta = "{{"
```

The ``lexText`` function is fairly simple.

```go
func lexText(l *lexer) stateFn {
    for {
        // If a leftMeta is found, it means everything between start and
        // that leftMeta string is plain text, so emit an itemText token.
        if strings.HasPrefix(l.input[l.pos:], leftMeta) {
            if l.pos > l.start {
                l.emit(itemText)
            }
            return lexLeftMeta  // next state
        }
        if l.next() == eof { break }
    }
    // Correcly reached EOF.
    if l.pos > l.start {
        l.emit(itemText)
    }
    l.emit(itemEOF) // Useful to make EOF a token.
    return nil      // Stop the run loop.
}
```

The ``lexLeftMeta`` state function is trivial. When we get here, we know there's a ``leftMeta`` in the input.

```go
func lexLeftMeta(l *lexer) stateFn {
    l. pos += len(leftMeta)
    l.emit(itemLeftMeta)
    return lexInsideAction  // Now inside {{ }}.
}
```

[lexscantalk]: https://www.youtube.com/watch?v=HxaD_trXwRE
[gotexttemplate]: https://golang.org/pkg/text/template/

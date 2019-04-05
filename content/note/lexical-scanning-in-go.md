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

The ``lexInsideAction`` function is more representative of standard lexer code. The method ``l.next()`` returns the next rune, and then ``lexInsideAction`` asks several questions. Is the input at this point

- a ``rightMeta``?
- an end-of-file or end-of-line?
- a space?
- a pipe?
- etc.

Here's a snippet from the actual implementation.

```go
func lexInsideAction(l *lexer) stateFn {
    // Either number, quoted string, or identifier.
    // Spaces separate and are ignored.
    // Pipe symbols separate and are emitted.
    for {
        if strings.HasPrefix(l.input[l.pos:], rightMeta) {
            return lexRightMeta
        }
        switch r := l.next(); {
        case r == eof || r == '\n':
            return l.errorf("unclosed action")
        case isSpace(r):
            l.ignore()
        case r == '|':
            l.emit(itemPipe)
        case r == '"':
            return lexQuote
        case r == '`':
            return lexRawQuote
        case r == '+' || r == '-' || '0' <= r && r <= '9':
            l.backup()
            return lexNumber
        case isAlphaNumeric(r):
            l.backup()
            return lexIdentifier
```

Helper functions.

```go
// next returns the next rune in the input.
func (l *lexer) next() (rune int) {
    if l.pos >= len(l.input) {
        l.width = 0
        return eof
    }
    rune, l.width =
        utf8.DecodeRuneInString(l.input[l.pos:])
    l.pos += l.width
    return rune
}

// ignore skips over the pending input before this point.
func (l *lexer) ignore() {
    l.start = l.pos
}

// backup steps back one rune.
// Can be called only once per call of next.
func (l *lexer) backup() {
    l.pos -= l.width
}

// peek returns but does not consume
// the next rune in the input.
func (l *lexer) peek() int {
    rune := l.next()
    l.backup()
    return rune
}
```

The accept functions. The first one is a method on ``lexer``. Give it a string of characters you think is okay to have next. It will return ``true`` if the next input is one of the characters in the string. Otherwise it returns ``false``. The other accept function, ``acceptRun`` will accept a run of characters from the provided string.

```go
// accept consumes the next rune
// if it's from the valid set.
func (l *lexer) accept(valid string) bool {
    if strings.IndexRune(valid, l.next()) >= 0 {
        return true
    }
    l.backup()
    return false
}
// acceptRun consumes a run of runes from the valid set.
func (l *lexer) acceptRun(valid string) {
    for strings.IndexRune(valid, l.next()) >= 0 {
    }
    l.backup()
}
```

### Lexing a Number

```go
func lexNumber(l *lexer) stateFn {
    // Optional leading sign.
    l.accept("+-")
    // Is it hex?
    digits := "0123456789"
    if l.accept("0") && l.accept("xX") {
        digits = "0123456789abcdefABCDEF"
    }
    l.acceptRun(digits)
    if l.accept(".") {
        l.acceptRun(digits)
    }
    if l.accept("eE") {
        l.accept("+-")
        l.acceptRun("0123456789")
    }
    // Is it imaginary?
    l.accept("i")
    // Next thing mustn't be alphanumeric.
    if isAlphaNumeric(l.peek()) {
        l.next()
        return l.errorf("bad number syntax: %q",
            l.input[l.start:l.pos])
    }
    l.emit(itemNumber)
    return lexInsideAction
}
```

### Handling Errors

Errors are easy to handle. Just emit the bad token and shut down the machine.

```go
// error returns an error token and terminates the scan
// by passing back a nil pointer that will be the next
// state, terminating l.run.
func (l *lexer) errorf(format string, args ...interface{})
  stateFn {
    l.items <- item{
        itemError,
        fmt.Sprintf(format, args...),
    }
    return nil
}
```

## The Problem

When you want to create a global variable in a Go program, like a template for an HTML server, and you want to deliver stuff to the user using a parsed template that's ready to run, you want to build that template at initialization time. You can't do that in Go, because that would be running a goroutine at initialization time, which is forbidden by the language specification.

That means we can't lex & parse a template during initialization. The goroutine is the problem, but it's not really necessary.

The work si done by the design; now we just adjust the API. We can change the API to hide the channel, provide a function to get the next token, and rewrite the run function.

The new API hides the channel and buffers it slightly, turning it into a ring buffer.

```go
// lex creates a new scanner for the input string.
func lex(name, input string) *lexer {
    l := &lexer{
        name:   name,
        input:  input,
        state:  lexText,
        itmes:  make(chan item, 2), // Two items are sufficient.
    }
    return l
}
```

The ``nextItem`` method needs to be modified.

```go
// nextItem returns the next item from the input.
func (l *lexer) nextItem() item {
    for {
        select {
        // Return lexed items to the caller
        case item := <-l.items:
            return item
        // If nothing is ready for the caller, keep the state machine running.
        // Essentially, this is the loop from the run() method of the old lexer
        // API.
        default:
            l.state = l.state(l)
        }
    }
    panic("not reached")
}
```

In summary, we now have a traditional API for a lexer with a simple, concurrent implementation under the covers. Even though the implementation is no longer truly concurrent, it still has all the advantages of concurrent design.

We wouldn't have such a clean, efficient design if we hadn't thought about the problem in a concurrent way, without worrying about "restart".

Concurrency is a design concept. Using it for the lexer completely removes concerns about "structural mismatch" between lexers and parsers.

Concurrency is not about parallelism. It enables parallelism, but doesn't require parallelism. It is a way to design a program by decomposing it into indepenedently executing pieces. The result can be clean, efficient, and very adaptable.

Note: if there is an efficiency problem, a traditional ring buffer (in the form of  list or array) could be used in place of the channel.

One modification would be to use a Reader interface instead of a string. It would make the implementation more general. The ``lexer`` struct, change the ``nextItem`` method to use the Reader. Backing up might be a little trickier. Do it in the abstract by turning the string into a Reader, and use a Reader for everything. Any input would work.

While this technique might work for a parser, it would be a lot of work. Pike says that the template lexer has only around 15 states. On the other hand, a parser can easily have hundreds of states. You probably want a machine to generate such a parser.

## References

- [GO Lexer API](https://github.com/iNamik/go_lexer)
- Someone wrote a three part series based on [Pike's lecture][lexscantalk]. Sadly, it doesn't go beyond the basics in the lecture. It really should have included a Reader interface.
  - [Writing a Simple Lexer and Parser in Go](https://adampresley.github.io/2015/04/12/writing-a-lexer-and-parser-in-go-part-1.html), Part 1 of 3.
  - [Writing a Simple Lexer and Parser in Go](https://adampresley.github.io/2015/05/12/writing-a-lexer-and-parser-in-go-part-2.html), Part 2 of 3.
  - [Writing a Simple Lexer and Parser in Go](https://adampresley.github.io/2015/06/01/writing-a-lexer-and-parser-in-go-part-3.html), Part 3 of 3.

[lexscantalk]: https://www.youtube.com/watch?v=HxaD_trXwRE
[gotexttemplate]: https://golang.org/pkg/text/template/

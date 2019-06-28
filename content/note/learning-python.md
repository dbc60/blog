---
title: Learn to Program with Python
date: 2016-03-09
draft: true
categories: note
tags: [python]
---

Here is where I see what Python can do. The book "Automate the Boring Stuff with Python" seems like a good place to start. The author claims I can save a lot of time by writing programs in Python, assuming I pick the right problems I guess. So, what are the problems the book tries to solve?
<!--more-->

## First, Learn to Program in Python
The [book](#sweigart)

### The Interactive Shell, Math Operators, Data Types and Variable Names
The [book](#sweigart) starts off with basic usage of the interactive shell and lists the math operators available in Python:

- `**`: exponent
- `%`: modulus/remainder
- `//`: integer division
- `/`: division
- `*`: multiplication
- `-`: subtraction
- `+`: addition

It then introduces some of the data types built-in to the language; integer, floating-point and string, and also introduces the concept of a variable and the rules for naming a variable.

Finally, the [book](#sweigart) moves on to the ubiquitous "Hello world" example:

```python
## This program says hello and asks for my name.

print('Hello world!')
print('What is your name?') # ask for their name
myName = input()
print ('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
```

It not only prints `'Hello world!'`, but exemplifies a few built-in functions (`print`, `input`, `len`, `str` and `int`) and how to write comments.

## Flow Control
There are some key concepts that must be discussed before learning about how flow control works in Python. These are the comparison operators, Boolean operators and code blocks.

### Comparison Operators
It all starts with the Boolean values `True` and `False`, so programs can make decisions. Here's the list of comparison operators:

- `==`: equal to
- `!=`: not equal to
- `<`: less than
- `>`: greater than
- `<=`: less than or equal to
- `>=`: greater than or equal to
- `is`: object identity
- `is not`: negated object identity

The last two operators are in the [Python 3 docs](https://docs.python.org/3/library/stdtypes.html#comparisons), but not yet mentioned by "Automate the Boring Stuff". It's probably to early to introduce them for people new to programming.

The first two operators work with values of any data type. For example, we can use them to determine if two strings are the same or not. There are other built-in types, not yet mentioned. I don't really think that statement applies to all of them.

The [documentation for Python 3](https://docs.python.org/3/library/stdtypes.html) says the built-in types are numerics (int, float and complex), sequences (`list`, `tuple`, `range`, `str`, `bytes`, `bytearray`, `memoryview`), set types (`set` and `frozenset`), mappings (`dict`), `contextmanager`, classes, instances, exceptions, modules, functions, methods, code objects, type objects, null object (`None`), ellipsis object (`Ellipsis`), `NotImplemented` object, Boolean values (`True` and `False`) and [internal objects](https://docs.python.org/3/reference/datamodel.html#types) which describe stack frame objects, traceback objects and slice objects. That's a lot of data types, a few of which have only a single instance.

### Boolean Operators
There are three Boolean operators, `and`, `or` and `not`. The `not` operator has the highest precedence, followed by `and` and then `or`. `not`'s precedence is lower than non-Boolean operators, so `not a == b` is interpreted as `not (a == b)` and `a == not b` is a syntax error.

### Code Blocks
There's one more concept, blocks of code and how they're written, that must be discussed before we're able to talk about how to express flow control in Python. Lines of code can be grouped together in *blocks*. There are three rules for writing blocks of code:

1. A new block begins when the indentation increases.
2. A block can contain other blocks.
3. A block ends when the indentation decreases to the level it was before the block began (which could be a containing block's indentation level), or it decreases to zero.

### Flow Control Statements

`if`
: takes the form `if <condition>:`. For examle, `if name == 'Mary':` The next line is indented to start a new [code block](#code-blocks).

'else'
: takes the for `else:`. It optionally follows an `if` clause at the same indentation level as the `if` statement it matches.

`elif`
: combines `else` and `if` into one statement and takes the same form as an `if` statement.

Example:

```python
    if name == 'Alice':
        print ('Hi Alice.')
    elif age < 12:
        print('You are not Alice, kiddo')
    else:
        print("Are you sure you're not Alice?")
```

while loop
: Like the `if` statement, a while loop statement takes the form `while <condition>:` and the next line is indented to start a new code block.

break statement
: causes a program to exit a `while` loop's clause.

Example:

```python
name = ''
attempts = 3
while name != 'your name':
    if attempts == 0:
        print("I'm sorry, that is not the correct input. Three strikes, you're out.")
        break
    else:
        attempts = attempts -1
    print('Please type your name')
    name = input()
print('Thank you')
```

Another way to write this without a `break` statement:

```python
name = ''
attempts = 3
while name != 'your name' and attempts > 0:
    attempts = attempts - 1
    print('Please type your name')
    name = input()
if attempts > 0:
    print("I'm sorry, that is not the correct input. Three strikes, you're out.")
else:
    print('Thank you')
```

I think the latter is more clear, because the loop-exit conditions are all spelled out in one place.

`range` function and `for` loops
: The `range` function can be used to create a `for`-loop that will iterate over a code block for given number of times.

```python
print('My name is')
## Prints for i equal to 0 up to, but not including 5.
for i in range(5):
    print(str(i) + '. ' + 'Douglas ' * (i + 1))
```

The output is:

    My name is
    0. Douglas
    1. Douglas Douglas
    2. Douglas Douglas Douglas
    3. Douglas Douglas Douglas Douglas
    4. Douglas Douglas Douglas Douglas Douglas

## Modules
A module is a file containing a related group of Python definitions (such as functions) and statements. The file name is the module name with the suffix `.py` appended. Within a module, the module's nameis available as a string via variable `__name__`.

The definitions and statements defined in a module can be embedded in your programs. Python comes with a set of modules called the *standard library*. Use the `import` statement to add a module to your program. Here's an example from the [Python documentation](https://docs.python.org/3/tutorial/modules.html):

```python
## Fibonacci numbers module
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
```

If this code is contained in the file `fibo.py`, then it can be imported and used:

```python
import fibo

print('The name of the fibo module is: "' + fibo.__name__ + '"')
fibo.fib(1000)
x = fibo.fib2(100)
print(x)
```

The result is:

    The name of the fibo module is: "fibo"
    1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

## Python Project Directory Layout
See [Python Patterns, Take One](https://taoofmac.com/space/blog/2013/08/11/2300) for the reasoning behind this project layout. It get's into some of the tools the author uses to do stuff.

```
+-- dev.py                # Stub to run Bottle while coding
+-- app.py                # WSGI entry point
+-- tasks.py              # Celery entry point
+-- fabfile               # Fabric deployment/build scripts
+-- Vagrantfile           # never leave home without it
+-- etc
|    +-- config.json      # my main configuration file
+-- api
|    +-- [model].py       # RESTful routes for each model
+-- controllers
|    +-- [behavior].py    # controllers used by routes
+-- lib
|    +-- bottle.py        # more bang than Flask
|    +-- peewee.py        # almost as nice as the Django ORM
|    +-- config.py        # loads up the JSON file
|    +-- utils            # my little bag of tricks
|    |    +-- core.py
|    |    +-- urlkit.py
|    |    +-- stringkit.py
|    |    +-- datekit.py
|    +-- [dependencies]   # Include ALL the dependencies locally
+-- env                   # virtualenv for "fat" dependencies
+-- puppet                # Puppet manifests and deployment stuff
+-- models
|    +-- db.py            # Base models and database initialisation
|    +-- [store].py       # Other data stores (Redis, etc.)
+-- batch                 # Celery tasks
|    +-- [worker].py      # Separate modules per worker, if needed
+-- static                # Static assets (HTML and sundry)
|    +-- css
|    |    +-- ink.css     # I love it
|    +-- js
|    |    +-- app.js      # Everything starts here
|    |    +-- ink-all.js  # Our in-house library
|    |    +-- knockout.js # I love data binding
|    |    +-- zepto.js    # I hate jQuery
|    +-- img
|    +-- font             # Usually Roboto
+-- views
     +-- layout.tpl       # Base layout for templates
     +-- [group]          # Partials for each entity/screen
```

## References
- <a id="sweigart"></a>[Automate the Boring Stuff with Python](https://automatetheboringstuff.com/): Practical Programming for Total Beginners, by Al Sweigart.
- <a id="python3docs"></a>[Python 3 Documentation](https://docs.python.org/3/contents.html)
- [Automate the Boring Stuff with Python Resources](https://www.nostarch.com/automatestuffresources)
- [Invent with Python](http://inventwithpython.com/)
    - [Page 14, Common Python error messages](http://inventwithpython.com/appendixd.html)
    - [Page 117, Complete source code for tic-tac-toe](http://inventwithpython.com/chapter10.html)
    - [Page 165, Bitwise operators](https://wiki.python.org/moin/BitwiseOperators/)
    - [Page 246, CSS Selector Tutorials](https://automatetheboringstuff.com/list-of-css-selector-tutorials/)
        - [W3C Selector Reference](http://www.w3.org/TR/CSS2/selector.html)
        - [Ryan's Tutorials: CSS Selectors](http://ryanstutorials.net/css-tutorial/css-selectors.php)
        - [HTML Dog: CSS Selectors](http://htmldog.com/guides/css/beginner/selectors/)
    - [Page 328, List of JSON APIs](https://automatetheboringstuff.com/list-of-json-apis/)
        - [Twitter API](https://dev.twitter.com/)
        - [Facebook Social Graph API](https://developers.facebook.com/docs/graph-api)
        - [Flickr](https://www.flickr.com/services/api/response.json.html)
        - [YouTube](https://developers.google.com/youtube/2.0/developers_guide_json?csw=1)
        - [OpenStreetMap](https://wiki.openstreetmap.org/wiki/Api)
        - [Google Maps](https://developers.google.com/maps/)
        - [Imagur API](https://api.imgur.com/)
        - [26 Weather APIs](http://www.programmableweb.com/news/26-weather-apis-12-support-json/2012/01/11)
        - [Rotten Tomatoes](http://developer.rottentomatoes.com/docs/read/JSON)
        - [Reddit](http://www.reddit.com/dev/api)
    - [Page 349, Beginner's tutorial on multi-threaded programming](http://inventwithpython.com/blog/2013/04/22/multithreaded-python-tutorial-with-threadworms/)
    - For the discussion on pp.354-355 and the practice problem on p.359: [List of Scheduler tutorials](https://automatetheboringstuff.com/schedulers/)
    - For the practice problem on p.360: a [list of web comics](https://automatetheboringstuff.com/list-of-web-comics/)
    - Page 365, Setting up application-specific [passwords for Google accounts](https://support.google.com/accounts/answer/185833?hl=en/)
    - Page 372, [Advanced searching in Gmail](https://support.google.com/mail/answer/7190?hl=en/)
    - Page 382, [Twilio status messages](https://www.twilio.com/help/faq/sms/what-do-the-sms-statuses-mean/)
    - Page 382, [Receiving text messages with Twilio:](https://www.twilio.com/docs/quickstart/php/sms/hello-monkey/)
    - Page 386, Controlling your computer through email project: See torrentStarter.py.
    - Page 389, [RGB color values](https://en.wikipedia.org/wiki/Web_colors)
    - Page 431, [Generic web form](http://autbor.com/form)
    - Page 439, [Building a Python bot that plays web games](http://inventwithpython.com/blog/2014/12/17/programming-a-bot-to-play-the-sushi-go-round-flash-game/)
    - Page 447, [List of websites with programming practice problems:](https://automatetheboringstuff.com/list-of-programming-practice-sites/)
- [Anaconda Distribution](https://docs.continuum.io/anaconda/?utm_source=housefile&utm_medium=email&utm_campaign=onboarding_cheat_sheet&mkt_tok=eyJpIjoiTjJFM05XSmlaVFE0TVdOayIsInQiOiJVaEloTzkyakpLMWNPaEUwV1B0WFRyRUVCa3JmQk11ck1FcUdiNDZYd0xBOXFNTFZKZnBpZkxcL3d5MjArczhiNHA4RStVR2hIbE5rUXV5aVQ4czN3Q1BDUHN6SDliZ1Y1blcyVDJTMjNwRjQ9In0%3D)
- [Using R Language with Anaconda](https://docs.continuum.io/anaconda/r_language?utm_source=housefile&utm_medium=email&utm_campaign=onboarding_cheat_sheet&mkt_tok=eyJpIjoiTjJFM05XSmlaVFE0TVdOayIsInQiOiJVaEloTzkyakpLMWNPaEUwV1B0WFRyRUVCa3JmQk11ck1FcUdiNDZYd0xBOXFNTFZKZnBpZkxcL3d5MjArczhiNHA4RStVR2hIbE5rUXV5aVQ4czN3Q1BDUHN6SDliZ1Y1blcyVDJTMjNwRjQ9In0%3D)
- [Anaconda Webinars](https://www.continuum.io/webinars?utm_source=housefile&utm_medium=email&utm_campaign=onboarding_cheat_sheet&mkt_tok=eyJpIjoiTjJFM05XSmlaVFE0TVdOayIsInQiOiJVaEloTzkyakpLMWNPaEUwV1B0WFRyRUVCa3JmQk11ck1FcUdiNDZYd0xBOXFNTFZKZnBpZkxcL3d5MjArczhiNHA4RStVR2hIbE5rUXV5aVQ4czN3Q1BDUHN6SDliZ1Y1blcyVDJTMjNwRjQ9In0%3D)
- [Anaconda Whitepapers](https://www.continuum.io/whitepapers?utm_source=housefile&utm_medium=email&utm_campaign=onboarding_cheat_sheet&mkt_tok=eyJpIjoiTjJFM05XSmlaVFE0TVdOayIsInQiOiJVaEloTzkyakpLMWNPaEUwV1B0WFRyRUVCa3JmQk11ck1FcUdiNDZYd0xBOXFNTFZKZnBpZkxcL3d5MjArczhiNHA4RStVR2hIbE5rUXV5aVQ4czN3Q1BDUHN6SDliZ1Y1blcyVDJTMjNwRjQ9In0%3D)

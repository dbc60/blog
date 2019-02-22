---
title: Monitoring Windows Volumes and Directory Paths
date: 2016-12-17
draft: true
categories: [programming]
tags:
    - windows
    - directories
    - file system
    - paths
---

Matching real paths to rules containing paths to be matched. These rules may contain an asterisk representing zero or more characters in the path.
<!--more-->

## Rules for Directory Paths

Directory paths will typically take the form of a string starting with a volume name (a letter followed by a colon), a backslash and a sequence of characters where backslashes represent directory separators. Customers would like to place an asterisk between a pair of backslashes to represent any directory path starting with the path preceding the asterisk and ending with the path succeeding the asterisk. Of course, the path may also begin or end with an asterisk, too. For example, `C:\Users\*\AppData\Local` represents a path on the `C:` volume that starts with `\Users\`, and continues with any directory or sequence of directories that end in `AppData\Local`.

These rules will be matched against real paths of the form `\Device\<DeviceName>\<Path>`, where `<DeviceName>` might be `HarddiskVolume2`, `CdRom0` or some similar DOS device name. I believe `<path>` is a normal directory path.

I'd like to convert the rules into a representation where they could easily be used to determine if a DOS device path matched one of the rules. If `C:\Users\*\AppData\Local` or `C:\Users\*\AppData\Local\` is a rule how can determine if the path `\Device\HarddiskVolume2\Users\Bob\AppData\Local\Temp\foo.txt` matches it? I'd also like that path to match against the following rules:

- `C:\Users\Bob\` if it's marked as a recursive rule
- `\Users\*\AppData\Local`: this should match even though the volume name is not specified.
- `*\Users\*\Local\`: the `Users` directory may appear at any level on any volume.
- `C:\*\Local`: the `Local` directory may appear at any level on the `C:` volume.
- `C:\Users\Bob\AppData\*`: match any path on the `C:` volume that starts with `\Users\Bob\AppData\`.
- `C:\Users\*\AppData\L*`: match paths starting with the letter `L` in the `AppData` directory, where the path is on the `C:` volume and it starts with `\Users\`. Don't assume `L*` represents a file. It could be one or more directories. In which case, all files in those matching directories will match the rule.

In other words, the asterisk can be placed at the beginning, middle or end of a rule, the volume name does not have to be specified (in which case all volumes are match candidates), and if the trailing slash is missing what's there is either a directory or a file.

Note that a kleene closure is a regular expression where the character (or regular expression) preceding the asterisk may be repeated zero or more times. Here we use the asterisk to represent a directory path of zero or more characters. If it's placed between a pair of directory separators (`Foo\*\Baz`), then the paths `Foo\Bar\Baz` and `Foo\Baz` will both match the rule. The pair of directory separators may be combined into one when there are no directories separating the higher and lower level paths on either side of the asterisk.

### Requirements

I don't want the minifilter converting each rule from "volume\path" to `\device\<device name>\path` each time it tries to match a given path. That would be a huge waste of time. Therefore, each rule should be converted to some path or set of paths that can be easily compared against a real path.

A path on the NTFS file system, as represented in the kernel, seems to be made from two components; the device and the directory path. The device takes the form of `\Device\<device name>` and is separated from the directory path by a directory separator, the backslash(`\`).

### Algorithms

There are a surprising number of algorithms for matching strings against multiple patterns. Of course, each comes with a set of assumptions and limitations. I need to find one that will quickly decide whether a given path matches one of the patterns and return a value that indicates which of the patterns it matched. If the string matches more than one pattern, I'm not sure I care which one of the matches it returns. At the moment, I don't think it matters.

#### PHP Example from Stackoverflow

[This stackoverflow question](http://stackoverflow.com/questions/4038885/how-to-design-a-string-matching-algorithm-where-the-input-is-the-exact-string-an) on string-matching against regex-like patterns recommends the Aho-Corasick algorithm where there are no wildcards in the patterns. For those with wildcards, one answer suggests first breaking up the patterns into the "constant string" parts. Put those strings in the list of ones you are searching for separately. Only if the text matches all of the constant parts for a particular pattern do you then do more processing to make sure it has the parts in the desired order.

Another answer takes the example of matching URL patterns like:

- `https://users.stackoverflow.com`
- `https://www.stackoverflow.com/users`
- `https://www.stackoverflow.com/users/120262`
- `*/users/*`
- `www.stackoverflow.com/users/239289`
- `*.stackoverflow.com/questions/ask`
- `*/questions/*`
- `developer.*.com`

Other assumptions are:

1. A URL is a list of tokens. To get them, we drop the protocol, drop the query string and find the first `/` (and if none, add it to the end). The stuff before the `/` is the hostname, and the stuff after `/` is the path.
1. We get teh hostname tokens by splitting on `.`.
1. We get the path tokens by splitting on `/`.

The URL `www.stackoverflow.com/users/230289` is split into the tokens: `www`, `stackoverflow`, `com`, `/`, `users`, and `239289`. Note that the only `/` we allow is the one separating the hostname and path.

Here's some PHP code to tokenize a URL:

```php
function tokenize_url($url) {
    $pos = strpos($url, '/');
    if ($pos === 0) {
        // It's a path-only entry.
        $hostname = '*';
        $path = substr($url, 1);
    } else if ($pos !== false) {
        // It's a normal URL with hostname and path.
        $hostname = substr($url, 0, $pos);
        $path = substr($url, $pos + 1);
        if ($path === false) {
            $path = '';
        }
    } else {
        // No slash found, assume it's a hostname only.
        $hostname = $url;
        $path = '';
    }

    if ($hostname !== '') {
        $hostname_tokens = explode('.', $hostname);
    } else {
        $hostname_tokens = array();
    }

    if ($path !== '') {
        $path_tokens = explode('/', $path);
    } else {
        $path_tokens = array();
    }

    return array_merge($hostname_tokens, array('/'), $path_tokens);
}
```

So, first we pre-process the list of URL patterns into a directed graph (a nested associative array) of tokens using the function above. This way, we only have to traverse teh graph once for exact matches, and a bit more to find wildcard matches. We mark the end of our patterns against which to match by hanging a special symbol, such as "`%!%!%`" off that node.

Here's the function to build the graph:

```php
function compile_site_list($site_list) {
    $root = array();

    foreach ($site_list as $url) {
        $tokens = tokenize_url($url);
        $node = &$root;

        for ($i = 0; $i < count($tokens); $i++) {
            // The "%" forces PHP to evaluate this as a string, no matter what.
            // Sadly, casting to a string doesn't do it!
            $token = $tokens[$i] . '%';

            // If this is our first time seeing this string here, make a
            // blank node.
            if (!(isset($node[$token]))) {
                $node[$token] = array();
            }

            if ($i < (count($tokens) - 1)) {
                // If we're not at the end yet, keep traversing down.
                $node = &$node[$token];
            } else {
                // If we're at the end, mark it with our special marker.
                $node[$token]['%!%!%'] = 1;
            }
        }
    }

    return $root;
}
```

Once you have your list of URLs to match against, call `compile_site_list()` to create your graph.

To match a URL against this graph, first clean it up (remove the protocol and query string, and ensure there is a backslash between the hostname and path):

```php
function scrub_url($url) {
    // Get rid of the protocol (if present).
    $pos = strpos($url, '://');
    if ($pos !== false) {
        $url = substr($url, $pos + 3);
    }

    // Get rid of any query string (if present).
    $pos = strpos($url, '?');
    if ($pos !== false) {
        $url = substr($url, 0, $pos);
    }

    return $url;
}
```

To search the graph, we take the tokens for the URL we're matching against and look for the recursively in the graph. As soon as we find "`%!%!%`", we have a match. However, if we get to the end of our tokens and haven't matched, we go back up and look for wildcards. If we find the wildcard, we let it consume as many tokens as it wants (except for "`/`") and see if that results in a match. If there's still no match, the URL isn't recognized.

Here's the matching code:

```php
function search_compiled_list($url, $compiled_site_list) {
    $url = scrub_url($url);
    $tokens = tokenize_url($url);

    return do_search($tokens, $compiled_site_list);
}

function do_search($tokens, $compiled_site_list) {
    // Base cases for recursion:
    if (isset($compiled_site_list['%!%!%'])) {
        // If we're at a node that has our marker hanging off it - we found it!
        return true;
    } else if (count($tokens) === 0) {
        // Otherwise, if we got somewhere and have no tokens left, we didn't
        // find it.
        return false;
    }

    // The "%" on the end forces PHP to evaluate this as a string, no
    // matter what.
    $token = $tokens[0] . '%';

    if (isset($compiled_site_list[$token])) {
        // Found an exact match!
        $result = do_search(array_slice($tokens, 1),
            $compiled_site_list[$token]);
        if ($result === true) {
            return true;
        }
    }

    // Didn't find an exact match - let's check for wildcards.
    if ((isset($compiled_site_list['*%'])) && ($tokens[0] !== '/')) {
        // If we're matching the wildcard, let it consume as many tokens
        // as it wants.  The only thing it can't consume is /.
        for ($i=1; $i<count($tokens); $i++) {
            $result = do_search(array_slice($tokens, $i),
                $compiled_site_list['*%']);
            if ($result === true) {
                return true;
            }
        }
    }

    return false;
}
```

So to see the whole thing in action - if you have `$site_list` which is an array of your URLs, you'd do:

```php
$url_to_check = "http://www.stackoverflow.com/users/120262?tab=accounts";
$compiled_site_list = compile_site_list($site_list);
$result = search_compiled_list($url_to_check, $compiled_site_list);
var_dump($result);
```

#### Aho-Corasick

This is a multiple string-matching algorithm that constructs a finite-state machine from a pattern (a list of keywords), then uses the machine to locate all occurrences of the keywords in a body of text. Construction of the machine takes time proportional to the sum of the lengths of the keywords. The machine is used to process the text string in a single pass. The number of transitions made by the machine is independent of the nubmer of keywords.

## File Integrity Monitoring Service

The File Integrity Monitoring (FIM) service must not only match directory paths against rules such as those above, but it must have a default set of exclusion paths so it doesn't report against it's own files and directories. This is most important for the logging directory.

I think the easiest way to do this is to create a file containing a set of default rules. The first rule would exclude the installation directory (usually `C:\Program Files\Threat Stack\`) and its two subdirectories `etc` and `logs`.

Perhaps this could be a signed file to make it more difficult to tamper with. The FIM service would have to verify the file against its signature. I don't know how to do that right now, so signing and verification can be a goal for a future release.

## References

- [Aho-Corasick](https://xlinux.nist.gov/dads/HTML/ahoCorasick.html) on NIST's [Dictionary of Algorithms and Data Strucctures](https://www.nist.gov/dads/) website.
- [How to efficiently match an input string against several regular expressions at once?](http://stackoverflow.com/questions/7049894/how-to-efficiently-match-an-input-string-against-several-regular-expressions-at). This question was asked on [Stackoverflow](https://stackoverflow.com). The accepted answer references:
  - The [Aho-Corasick algorithm](https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm) on [Wikipedia](https://en.wikipedia.org).
  - A GNU Lesser GPL license [implementation in Python](https://code.google.com/archive/p/esmre/) that handles regular expressions.
  - The source for [Snort](https://www.snort.org/) may have an implementation in C. It would be licensed under the GPL.
  - [RE2 regular expression engine](https://github.com/google/re2) in C++ in a 3-clause BSD license. There is a [tour through the source code](https://swtch.com/~rsc/regexp/regexp3.html), too.
- [Approximate GREP](https://github.com/Wikinaut/agrep) source code in C (3-clause BSD-like license).
- [AGREP](https://www.tgries.de/agrep/) website.
- [Glimpse](https://github.com/gvelez17/glimpse) source code in C. It is a tool to search an entire file system. Using a very small index, it allows very flexible full-text retrieval including Boolean queries, approximate matching (allowing for misspellings) and searching for regular expressions.
- [Webglimpse](https://github.com/gvelez17/webglimpse) source code in Perl.
- [Pattern Matching Pointers](http://www.cs.ucr.edu/~stelo/pattern.html) is a page with lots of links to information about combinatorial pattern matching.
- Even though [this implementation](https://github.com/mischasan/aho-corasick) of Aho-Corasick is LGPL licensed, it's worth a look, because its design might take into account the use of L1/L2 cache for a performance boost. That said, there's no way the code should ever be used directly. There are no tests, it contains `goto`s and it contains lots of 2- and 3-letter variables making the code difficult for a human to parse.
- [String matching against regex-like patterns](http://stackoverflow.com/questions/4038885/how-to-design-a-string-matching-algorithm-where-the-input-is-the-exact-string-an) has a good answer for handling patterns both with and without wildcards.
- [Trie](https://en.wikipedia.org/wiki/Trie), also called a **digital tree**, **radix tree** or **prefix tree**. It is pronounced like "tree", as in re*trie*val.

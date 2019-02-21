---
title: Jekyll Configuration
date: 2016-03-07
draft: true
categories:
  - blog
  - web
tags:
  - jekyll
  - yaml
---

Jekyll is easy to get up and running.
<!--more-->

It really is easy to install and use. What takes time is learning enough about its bells and whistles, markdown, HTML, CSS and Sass to make a blog or website you're own. Also, I need a place to host my blog. I may eventually create my own web server, perhaps on a [DigitalOcean](https://www.digitalocean.com/) droplet (mostly because they don't cost very much and a small server in a cloud is adequate for a static website). For now, I'm using [GitHub pages](https://pages.github.com/).

I like using [Compass](http://compass-style.org/) to compile Sass files to CSS. Both Compass and Jekyll are written in Ruby, so it's also a good idea to use a tool like [Bundler](http://bundler.io/) to keep your Ruby gems up to date.

## Installing Ruby, Bundler, Jekyll and Compass
Head over to the [Ruby](https://www.ruby-lang.org/en/) site and download the [latest installer](https://www.ruby-lang.org/en/documentation/installation/) or use the appropriate package manager for your operating system.

According to the [Jekyll website](https://jekyllrb.com) all you have to do to install Jekyll, create a new blog project and start a web server that watches for changes is:

```shell
gem install jekyll
jekyll new my-blog
cd my-blog
jekyll serve
```

I've found [Bundler](http://bundler.io/) is useful for keeping gems up-to-date. Each project can have its own set of gems and even have its own versions of the same gems independent of other projects. So, first check that you have Ruby verion 2.0 or later installed (`ruby --version`), and then install Bundler by running `gem install bundler`.

Create a git repository on your local computer:

```shell
E:\> git init my-jekyll-site-project
Initialized empty Git repository in E:/Users/Doug/Projects/my-jekyll-site-project/.git/
```

Change the current directory to the new repository (`cd my-jekyll-site-project`), and create a new branch (`git checkout -b configure-jekyll`).

Now we can prepare to install Jekyll using Bundler. Ruby and Bundler will use a Gemfile to track dependencies among various gems, so create or edit a Gemfile in your favorite editor. It must start with:

```shell
source 'https://rubygems.org'
```

If your site will use Github Pages, then include:

```yaml
# github-pages will ensure the supported version of Jekyll and its dependencies are installed.
gem 'github-pages', group: :jekyll_plugins
```

If the site doesn't need Github pages, then DO NOT USE `gem 'github-pages'`. The `github-metadata` will want a reference to the Github repository. Instead, consider the following gems (extracted from the [Github Pages dependencies list](https://pages.github.com/versions/)):

```yaml
gem 'jekyll'
gem 'jekyll-feed'       # generates an Atom feed of your Jekyll posts
gem 'jekyll-paginate'   # Built-in pagination generator for Jekyll
gem 'jekyll-sass-converter' # A basic Sass converter for Jekyll (or use Compass)

# jekyll-seo-tag will add metadata tags for search engines and social networks to
# better index and display your site's content. It seems to be necessary.
gem 'jekyll-seo-tag'
gem 'jekyll-sitemap'    # Automatically generates sitemap.xml
gem 'kramdown'      # a fast markdown parser
gem 'liquid'        # a template engine
gem 'listen'        # listens to file modifications and notifies you about the changes
gem 'rouge'         # a syntax highligher
gem 'safe_yaml'     # parse YAML safely
gem 'sass'          # Sass makes CSS fun again

# This could be fun if it works outside of Github
gem 'jemoji'    # Github-flavored emoji plug-in for Jekyll.
```

I also like Compass for generating CSS from Sass/Scss files:

```yaml
gem 'compass'
```

2016.09.19 Update: I no longer use Compass. It crashed too many times while I was experimenting with Sass, and it is no longer being maintained. While it has a large Sass library, it's main usefulness to me was its math library that made it possible to use exponentiation and logarithms in calculating luminance. I figured out how to write those functions in pure Sass and Jekyll has its own Sass compiler, so I don't need or want Compass anymore.

Finally, I found a few more gems make writing docs easier:

```yaml
# Added asciidoctor and asciidoctor-diagram to create SVG diagrams from AsciiDoc/PlanUML text.
gem 'asciidoctor'
gem 'asciidoctor-diagram'

# Added in response to a warning from Jekyll
gem 'wdm', '>= 0.1.0' if Gem.win_platform?

# Add the modular scale calculator built into your Sass from http://modularscale.com
# and https://github.com/modularscale/modularscale-sass. If you want to use it, remember to
# include it in your 'config.rb' (require 'modular-scale' and import it in one of your .scss
# files, such as style.scss (@import 'modular-scale').
gem 'modular-scale'
```

Generate a Jekyll site on your local computer (or fork and clone an existing site from a git repository). Use `bundle exec jekyll new . --force` to create a new site. Once it's created, make some small adjustments for Compass:

1. Move `css/main.scss` to `_sass/main.scss` and edit it to remove the YAML front matter.
2. Create `config.rb` with the following content:

```yaml
require 'compass/import-once/activate'
# Require any additional compass plugins here.

# Add the modular scale calculator built into your Sass from http://modularscale.com
# and https://github.com/modularscale/modularscale-sass. If you want to use it, remember to
# include it in your 'config.rb' (require 'modular-scale' and import it in one of your .scss
# files, such as style.scss (@import 'modular-scale').
require 'modular-scale'

# Set this to the root of your project when deployed:
http_path = "/"
css_dir = "css"
sass_dir = "_sass"
images_dir = "img"
javascripts_dir = "js"
fonts_dir = "fonts"

# You can select your preferred output style here (can be overridden via the command line):
# output_style = :expanded or :nested or :compact or :compressed

# To enable relative paths to assets via compass helper functions. Uncomment:
# relative_assets = true

# To disable debugging comments that display the original location of your selectors. Uncomment:
# line_comments = false
```

Create a `_build` directory at the same level as the Jekyll directories and then create two `.bat` scripts there to run `bundler`, `compass` and `jekyll`. The first is `start.bat`:

```shell
@echo off
REM Update all the gems and then start Compass and Jekyll
call bundle update
SET PROJECT_PATH=%~dp0
call %PROJECT_PATH%quick-start.bat
```

The second is `quick-start.bat`:

```shell
@echo off
REM Start Compass and Jekyll without updating gems
start bundle exec compass watch

REM Give compass a few seconds to start before launching jekyll.
@ping 192.0.2.2 -n 1 -w 4000 > nul

start bundle exec jekyll s --port 4000
```

Run `_build\start.bat` and open a web browser to [http://localhost:4000](http://localhost:4000), you'll see the default site that `jekyll new` created.

The thing with GitHub pages is that you have to run Bundler to ensure you have a set of gems installed that are compatible with GitHub. Since that set of gems doesn't currently include the most recent version of Jekyll, you have to run something like `bundle exec jekyll server`.

## The Jekyll Configuration File
The `_config.yml` file contains the site configuration information. The first topic I'd like to get a handle on is how Jekyll should create the URL for each post.

According to [this Whiteboard Friday](https://moz.com/blog/subdomains-vs-subfolders-rel-canonical-vs-301-how-to-structure-links-optimally-for-seo-whiteboard-friday) article on Mozilla's blog, it's not a good idea, from an SEO point of view, to put content in a subdomain. Mozilla also has an article on [structuring URLs](https://moz.com/blog/15-seo-best-practices-for-structuring-urls) for SEO. With this information in mind, I'm setting `permalink: date`, which is a built-in style that is equivalent to `/:categories/:year/:month/:day/:title.html`. That will enable me to designate some posts going to `/blog/`, others to `/notes/` and others to different directory paths all by setting the `category` or `categories` variable in the YAML front matter of each post.

I think I'm okay with the other values I've set in my [_config.yml](https://github.com/dbc60/dbc60.github.io/blob/master/_config.yml) file.

## YAML Front Matter
The [YAML specification](http://www.yaml.org/spec/1.2/spec.html) has all the details on what a YAML document can contain. Here are some highlights:

YAML uses three dashes ("`---`") to separate directives from document content. For example, this post starts with:

```yaml
---
layout: post
title: Jekyll Configuration
categories: blog
tags: [jekyll, yaml]
---
Jekyll is so ...
```

You can add comments to the front matter. Each YAML comment starts with a hash mark ("`#`"). If there are any more details about YAML or Jekyll, they can be gleaned from the documentation.

## Tags and Filters

The [templates](https://jekyllrb.com/docs/templates/) page lists a set of filters that are available in Jekyll. It also says that Jekyll supports all of the standard Liquid [tags](https://shopify.github.io/liquid/tags/) and [filters](https://shopify.github.io/liquid/filters/).

Be very careful to use only these links as references to filters and tags. I spent a few hours trying to use `concat:` only to discover it's not supported. I was looking at Shopify's reference for [array filters](https://help.shopify.com/themes/liquid/filters/array-filters), which includes filters, such as `concat` that are not part of the standard set Liquid template filters.

## Updating to Version 3.3.0
The `--watch` option is disabled for Windows in version 3.3.0 of Jekyll. It was intended for BASH on Windows, but was extended to the default `cmd.exe` and PowerShell. Why? I don't know. It can work just fine from `cmd.exe`.

A temporary fix is to open `vendor\bundle\gems\jekyll-3.3.0\lib\jekyll\commands\build.rb` and replace the line `if Utils::Platforms.windows?` with `unless Utils::Platforms.windows?`.

I found this fix among the [comments](https://github.com/jekyll/jekyll/issues/5462#issuecomment-253982908) in [Jekyll issue 5462](https://github.com/jekyll/jekyll/issues/5462). There are some comments that say the underlying problem in BASH on Windows has been fixed, so `--watch` will be enabled in a later release.

The other major change is in the handling of `post_url`. It is no longer enough to provide the file name. The subdirectory containing the `_posts` directory must also be specified. For example, if I have a post `projects\_posts\2016-03-07-foo.md`, I must reference it as `/projects/2016-03-07-foo` in the Liquid markup.

## Rouge Values for Fenced Code Blocks
Run `rougify list` to get the latest list of languages supported by Rouge for fenced code blocks.

```shell
> rougify list
```

### Available Lexers
Here is a list of languages that rouge understands for the purpose of syntax highlighting in fenced code blocks.

- `actionscript`: ActionScript [aliases: as,as3]
- `apache`: configuration files for Apache web server
- `apiblueprint`: Markdown based API description language. [aliases: apiblueprint,apib]
- `applescript`: The AppleScript scripting language by Apple Inc. (http://developer.apple.com/applescript/) [aliases: applescript]
- `biml`: BIML, Business Intelligence Markup Language
- `c`: The C programming language
- `ceylon`: Say more, more clearly.
- `cfscript`: CFScript, the CFML scripting language [aliases: cfc]
- `clojure`: The Clojure programming language (clojure.org) [aliases: clj,cljs]
- `cmake`: The cross-platform, open-source build system
- `coffeescript`: The Coffeescript programming language (coffeescript.org) [aliases: coffee,coffee-script]
- `common_lisp`: The Common Lisp variant of Lisp (common-lisp.net) [aliases: cl,common-lisp,elisp,emacs-lisp]
- `conf`: A generic lexer for configuration files [aliases: config,configuration]
- `coq`: Coq (coq.inria.fr)
- `cpp`: The C++ programming language [aliases: c++]
- `csharp`: a multi-paradigm language targeting .NET [aliases: c#,cs]
- `css`: Cascading Style Sheets, used to style web pages
- `d`: The D programming language(dlang.org) [aliases: dlang]
- `dart`: The Dart programming language (dartlang.com)
- `diff`: Lexes unified diffs or patches [aliases: patch,udiff]
- `eiffel`: Eiffel programming language
- `elixir`: Elixir language (elixir-lang.org) [aliases: elixir,exs]
- `erb`: Embedded ruby template files [aliases: eruby,rhtml]
- `erlang`: The Erlang programming language (erlang.org) [aliases: erl]
- `factor`: Factor, the practical stack language (factorcode.org)
- `fortran`: Fortran 95 Programming Language
- `gherkin`: A business-readable spec DSL ( github.com/cucumber/cucumber/wiki/Gherkin ) [aliases: cucumber,behat]
- `glsl`: The GLSL shader language
- `go`: The Go programming language (http://golang.org) [aliases: go,golang]
- `gradle`: A powerful build system for the JVM
- `groovy`: The Groovy programming language (http://www.groovy-lang.org/)
- `haml`: The Haml templating system for Ruby (haml.info) [aliases: HAML]
- `handlebars`: the Handlebars and Mustache templating languages [aliases: hbs,mustache]
- `haskell`: The Haskell programming language (haskell.org) [aliases: hs]
- `html`: HTML, the markup language of the web
- `http`: http requests and responses
- `ini`: the INI configuration format
- `io`: The IO programming language (http://iolanguage.com)
- `java`: The Java programming language (java.com)
- `javascript`: JavaScript, the browser scripting language [aliases: js]
- `jinja`: Django/Jinja template engine (jinja.pocoo.org) [aliases: django]
- `json`: JavaScript Object Notation (json.org)
- `json-doc`: JavaScript Object Notation with extenstions for documentation
- `jsonnet`: An elegant, formally-specified config language for JSON
- `julia`: The Julia programming language [aliases: jl]
- `kotlin`: Kotlin <http://kotlinlang.org>
- `liquid`: Liquid is a templating engine for Ruby (liquidmarkup.org)
- `literate_coffeescript`: Literate coffeescript [aliases: litcoffee]
- `literate_haskell`: Literate haskell [aliases: lithaskell,lhaskell,lhs]
- `llvm`: The LLVM Compiler Infrastructure (http://llvm.org/)
- `lua`: Lua (http://www.lua.org)
- `make`: Makefile syntax [aliases: makefile,mf,gnumake,bsdmake]
- `markdown`: Markdown, a light-weight markup language for authors [aliases: md,mkd]
- `matlab`: Matlab [aliases: m]
- `moonscript`: Moonscript (http://www.moonscript.org) [aliases: moon]
- `nasm`: Netwide Assembler
- `nginx`: configuration files for the nginx web server (nginx.org)
- `nim`: The Nim programming language (http://nim-lang.org/) [aliases: nimrod]
- `objective_c`: an extension of C commonly used to write Apple software [aliases: objc]
- `ocaml`: Objective CAML (ocaml.org)
- `pascal`: a procedural programming language commonly used as a teaching language.
- `perl`: The Perl scripting language (perl.org) [aliases: pl]
- `php`: The PHP scripting language (php.net) [aliases: php,php3,php4,php5]
- `plaintext`: A boring lexer that doesn't highlight anything [aliases: text]
- `powershell`: powershell [aliases: posh]
- `praat`: The Praat scripting language (praat.org)
- `prolog`: The Prolog programming language (http://en.wikipedia.org/wiki/Prolog) [aliases: prolog]
- `properties`: .properties config files for Java
- `protobuf`: Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data [aliases: proto]
- `puppet`: The Puppet configuration management language (puppetlabs.org) [aliases: pp]
- `python`: The Python programming language (python.org) [aliases: py]
- `qml`: QML, a UI markup language [aliases: qml]
- `r`: The R statistics language (r-project.org) [aliases: r,R,s,S]
- `racket`: Racket is a Lisp descended from Scheme (racket-lang.org)
- `ruby`: The Ruby programming language (ruby-lang.org) [aliases: rb]
- `rust`: The Rust programming language (rust-lang.org) [aliases: rs]
- `sass`: The Sass stylesheet language language (sass-lang.com)
- `scala`: The Scala programming language (scala-lang.org) [aliases: scala]
- `scheme`: The Scheme variant of Lisp
- `scss`: SCSS stylesheets (sass-lang.com)
- `sed`: sed, the ultimate stream editor
- `shell`: Various shell languages, including sh and bash [aliases: bash,zsh,ksh,sh]
- `shell_session`: A generic lexer for shell session and command line [aliases: terminal,console]
- `slim`: The Slim template language
- `smalltalk`: The Smalltalk programming language [aliases: st,squeak]
- `smarty`: Smarty Template Engine [aliases: smarty]
- `sml`: Standard ML [aliases: ml]
- `sql`: Structured Query Language, for relational databases
- `swift`: Multi paradigm, compiled programming language developed by Apple for iOS and OS X development. (developer.apple.com/swift)
- `tap`: Test Anything Protocol [aliases: tap]
- `tcl`: The Tool Command Language (tcl.tk)
- `tex`: The TeX typesetting system [aliases: TeX,LaTeX,latex]
- `toml`: the TOML configuration format (https://github.com/mojombo/toml)
- `tulip`: The tulip programming language http://github.com/jneen/tulip [aliases: tlp]
- `twig`: Twig template engine (twig.sensiolabs.org)
- `typescript`: TypeScript, a superset of JavaScript [aliases: ts]
- `vb`: Visual Basic [aliases: visualbasic]
- `verilog`: The System Verilog hardware description language
- `viml`: VimL, the scripting language for the Vim editor (vim.org) [aliases: vim,vimscript,ex]
- `xml`: <desc for="this-lexer">XML</desc>
- `yaml`: Yaml Ain't Markup Language (yaml.org) [aliases: yml]

## References

- [Various Methods of Syntax Highlighting w/ Jekyll](https://gist.github.com/zakkain/3203448)
- [How to use highlight.js](https://highlightjs.org/usage/)
- [Jekyll Templates](https://jekyllrb.com/docs/templates/)
- [Standard Liquid Tags](https://shopify.github.io/liquid/tags/)
- [Standard Liquid Filters](https://shopify.github.io/liquid/filters/)

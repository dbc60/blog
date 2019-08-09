---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: true
---

**Insert Lead paragraph here.**
<!--more-->

## New Posts

{{ range first 10 ( where .Site.RegularPages "Type" "project" ) }}
* [{{ .Title }}]({{ .Permalink }})
{{ end }}

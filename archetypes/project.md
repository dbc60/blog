---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
{{ dateFormat "2006: [\"01\"]" .Date }}
categories: [project]
tags: []
---

Place excerpt here.
<!--more-->

## New Posts

{{ range first 10 ( where .Site.RegularPages "Type" "project" ) }}
* [{{ .Title }}]({{ .Permalink }})
{{ end }}

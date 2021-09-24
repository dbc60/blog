---
title: "Store Site Data"
date: 2021-09-23T14:24:22-04:00
2021: ["09"]
---
```go-html-template
<!--
  .Site.Data isn't a path. It's a map of all the files in the data folder,
  its subfolders and their files, and the contents of all those files.
-->
{{- $data := .Site.Data -}}
```
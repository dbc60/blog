---
title: "Src File Path"
date: 2021-09-23T14:26:52-04:00
2021: ["09"]
---

```go-html-template
{{- $src := .Get "src" -}}
{{- $pathComponents := split $src "/" -}}
```

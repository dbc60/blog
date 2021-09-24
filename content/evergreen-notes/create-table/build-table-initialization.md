---
title: "Build Table Initialization"
date: 2021-09-23T14:21:15-04:00
2021: ["09"]
---
```go-html-template
<!-- Table data is always a map -->
  {{- $table := . -}}
  {{- $haveHead := false -}}
  {{- $haveBody := false -}}
  {{- $captionValue := "" -}}
  {{- $colGroupValue := "" -}}
  {{- $bodyValue := "" -}}
  {{- $headValue := "" -}}
  {{- $footValue := "" -}}
```

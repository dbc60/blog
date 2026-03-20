---
title: "Template Create Rows"
date: 2021-09-23T17:23:13-04:00
years: ["2021"]
---
<!--more-->

```go-html-template
<!-- Use within <table>, <tbody>, or <tfoot> elements, but not within <thead>;
  this will generate <tr><td>...</td><td>...</td>...</tr> row sequences
-->
{{- define "createRows" -}}
  {{- $rows := . -}}
  {{- range $idx, $row := $rows -}}
    {{- if and (not (reflect.IsMap $row)) (not (reflect.IsSlice $row)) -}}
      <!-- row value is a scalar -->
      <td>{{- $row -}}</td>
    {{- else if reflect.IsMap $row -}}
      <!-- row value is a map -->
      {{- template "processMap" $row -}}
    {{- else if reflect.IsSlice $row}}
      <!-- row value is a slice -->
      {{- template "createRows" $row -}}
    {{- else -}}
      <!-- row value type is unknown -->
      {{- $idx -}} (rows-unknown): {{- $row -}}
    {{- end -}}
  {{- end -}}
{{- end -}}
```

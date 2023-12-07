---
title: "Template Create Rows Head"
date: 2021-09-23T17:20:53-04:00
2021: ["09"]
---
<!--more-->

```go-html-template
<!-- Use only within thead elements. This will generate
   <tr><th>...</th><th>...</th>...</tr> row sequences
-->
{{- define "createRowsHead" -}}
  {{- $rows := . -}}
  {{- range $idx, $row := $rows -}}
    {{- if and (not (reflect.IsMap $row)) (not (reflect.IsSlice $row)) -}}
      <!-- row value is a scalar -->
      <th>{{- $row -}}</th>
    {{- else if reflect.IsMap $row -}}
      <!-- row value is a map -->
      {{- template "processMapHead" $row -}}
    {{- else if reflect.IsSlice $row}}
      <!-- row value is a slice -->
      {{- template "createRowsHead" $row -}}
    {{- else -}}
      <!-- row value type is unknown -->
      {{- $idx -}} (head-row-unknown): {{- $row -}}
    {{- end -}}
  {{- end -}}
{{- end -}}
```

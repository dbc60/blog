---
title: "Template Create Colgroup"
date: 2021-09-23T17:15:15-04:00
2021: ["09"]
---
```go-html-template
{{- define "createColgroup" -}}
  {{- $colgroup := . -}}
  {{- range $idx, $col := $colgroup}}
    <col{{range $attr, $val := $col}} {{$attr}}="{{$val}}" {{end}}>
  {{- end -}}
{{- end -}}
```

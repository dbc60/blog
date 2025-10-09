---
title: "Template Process Map Head"
date: 2021-09-23T17:33:06-04:00
years: ["2021"]
---
<!--more-->

```go-html-template
{{- define "processMapHead" -}}
  {{- $row := . -}}
  {{- range $k, $v := $row -}}
    {{- if and (not (reflect.IsMap $v)) (not (reflect.IsSlice $v)) -}}
      <td>{{- $k -}} (map->scalar): ({{$v}})</td>
    {{- else if reflect.IsMap $v -}}
      <tr class="head">{{- $k -}} (map-map): {{- template "processMapHead" $v -}}</tr>
    {{- else if reflect.IsSlice $v}}
      <tr class="head">{{- template "createRowsHead" $v -}}</tr>
    {{- else -}}
      <td>{{$k}} (map-unknown): {{- $v -}}</td>
    {{- end -}}
  {{- end -}}
{{- end -}}
```

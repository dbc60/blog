---
title: "Template Process Map"
date: 2021-09-23T17:39:44-04:00
2021: ["09"]
---

```go-html-template
{{- define "processMap" -}}
  {{- $row := . -}}
  {{- range $k, $v := $row -}}
    {{- if and (not (reflect.IsMap $v)) (not (reflect.IsSlice $v)) -}}
      <td>{{- $k -}} (map->scalar): ({{$v}})</td>
    {{- else if reflect.IsMap $v -}}
      <tr class="body">{{- $k -}} (map-map): {{- template "processMap" $v -}}</tr>
    {{- else if reflect.IsSlice $v}}
      <tr class="body">{{- template "createRows" $v -}}</tr>
    {{- else -}}
      <td>{{$k}} (map-unknown): {{- $v -}}</td>
    {{- end -}}
  {{- end -}}
{{- end -}}
```

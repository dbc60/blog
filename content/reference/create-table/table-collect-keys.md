---
title: "Table Collect Keys"
date: 2021-09-23T14:36:45-04:00
years: ["2021"]
---
<!--more-->

```go-html-template
  <!-- collect all the keys in the map -->
  {{- range $key, $val := $table -}}
    {{- if eq $key "body" -}}
      {{- if $haveBody -}}
        {{- $haveBody = $haveBody | append $val -}}
      {{- else -}}
        {{- $haveBody = true -}}
        {{- $bodyValue = $val}}
      {{- end -}}
    {{- else if eq $key "caption" -}}
      {{- $captionValue = $val -}}
    {{- else if eq $key "colgroup" -}}
      {{- $colGroupValue = $val -}}
    {{- else if eq $key "head" -}}
      {{- $haveHead = true -}}
      {{- $headValue = $val -}}
    {{- else if ne $key "foot" -}}
      {{- if $haveBody -}}
        {{- $bodyValue = $bodyValue | append $val -}}
      {{- else -}}
        {{- $haveBody = true -}}
        {{- $bodyValue = $val}}
      {{- end -}}
    {{- else -}}<!-- key is foot -->
      {{- $footValue = $val -}}
    {{- end -}}
  {{- end -}}
```

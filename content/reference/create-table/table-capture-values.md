---
title: "Table Capture Values"
date: 2021-09-23T14:41:10-04:00
years: ["2021"]
---
<!--more-->

```go-html-template
  {{- if ne $captionValue "" -}}
    <caption>{{- $captionValue -}}</caption>
  {{- end -}}
  {{- if ne $colGroupValue "" -}}
    <colgroup>
      {{- template "createColgroup" $colGroupValue -}}
    </colgroup>
  {{- end -}}
  {{- if ne $headValue "" -}}
    <thead>
      {{- template "createRowsHead" $headValue -}}
    </thead>
  {{- end -}}
  {{- if ne $bodyValue "" -}}
    <tbody>
      {{- template "createRows" $bodyValue -}}
    </tbody>
  {{- end -}}
  {{- if ne $footValue "" -}}
    <tfoot>
      {{- template "createRows" $footValue -}}
    </tfoot>
  {{- end -}}
```

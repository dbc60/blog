---
title: "Src File Data"
date: 2021-09-23T14:28:43-04:00
2021: ["09"]
---

```go-html-template
<!--
  Use the components of the src path to rummage through the map-of-maps in
  $data to get the src table's contents.
-->
{{- range $component := $pathComponents -}}
  {{- if ne $data nil -}}
    {{- $data = index $data $component -}}
  {{- end -}}
{{- end -}}
```

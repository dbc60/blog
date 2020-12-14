---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
{{ dateFormat "2006: [\"01\"]" .Date }}
categories: [projects]
---

<!--more-->
{{< table-of-contents >}}

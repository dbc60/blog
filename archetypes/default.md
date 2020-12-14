---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
{{ dateFormat "2006: [\"01\"]" .Date }}
categories: [uncategorized]
---

<!--more-->
{{< table-of-contents >}}

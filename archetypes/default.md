---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
{{ dateFormat "2006: [\"01\"]" .Date }}
tags: [uncategorized]
---

<!--more-->
{{< table_of_contents >}}

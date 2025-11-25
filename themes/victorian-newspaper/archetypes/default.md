---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
{{ dateFormat "2006: [\"01\"]" .Date }}
tags: [uncategorized]
# Featured image (optional)
# featuredImage: ""
# featuredImageDescription: "Descriptive alt text for screen readers"
# featuredCopyright: ""
---

<!--more-->
{{< table_of_contents >}}

<!--
ACCESSIBILITY REMINDER:
- Use descriptive alt text for all images
- Decorative images: use empty alt=""
- Example: ![Descriptive alt text](image.jpg)
-->

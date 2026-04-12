---
title: "Faultline"
subtitle: "A Fault-Injection Framework"
date: 2026-04-11T08:13:11-04:00
2026: ["04"]
tags: [c, testing]
draft: true
# Featured image (consider finding an image of a fault from an earthquake)
# featuredImage: ""
# featuredImageDescription: "Descriptive alt text for screen readers"
# featuredCopyright: ""
---
C has been the language of operating systems, embedded systems, compilers, databases, and networking infrastructure for fifty years. It has been successful for so long, because it's a great fit for building software systems. The ecosystem of tools, the portability, the predictability of the runtime model, the ability to work close to the metal without fighting the language are things C genuinely does well.
<!--more-->
{{< table_of_contents >}}

[BUT](https://github.com/dbc60/but) was a pretty good unit test framework. I hadn't [noticed its warts yet]({{< ref "post/simple-unit-test-framework.md#top" >}}), in part because it was built with Visual Studio 2022 only. I'll address the limitation of VS2022 and the problem it hid in a moment. For now I was quite please with BUT, its exception handling mechanism, and the style for building test suites that it imposed.
<!--
ACCESSIBILITY REMINDER:
- Use descriptive alt text for all images
- Decorative images: use empty alt=""
- Example: ![Descriptive alt text](image.jpg)
-->

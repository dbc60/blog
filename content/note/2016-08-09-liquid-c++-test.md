---
layout: post
title: Test Liquid & C++
date: 2016-08-09
draft: true
categories: blog
tags: [test]
excerpt: A comparison of fenced code blocks and raw liquid markup.
---

```cpp
return { std::forward<Begin>(begin.list), value };
```

{% highlight cpp %}
{% raw %}
return {{ std::forward<Begin>(begin.list), value }};
{% endraw %}
{% endhighlight %}

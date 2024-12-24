---
title: "Generate Backlinks"
date: 2024-12-24T11:45:32-05:00
2024: ["12"]
tags: [hugo]
---
I think the only way to have Hugo generate backlinks to a page is to include a partial that loops over all of the content files.
<!--more-->
Many thanks to whoever wrote [Parsing Backlinks in Hugo](https://scripter.co/parsing-backlinks-in-hugo) for a partial to create backlinks. The partial is:

```go-template
{{ $backlinks := slice }}
{{ $path_base := .page.File.ContentBaseName }}
{{ $path_base_re := printf `["/(]%s["/)]` $path_base }}

{{ range where site.RegularPages "RelPermalink" "ne" .page.RelPermalink }}
    {{ if (findRE $path_base_re .RawContent 1) }}
        {{ $backlinks = $backlinks | append . }}
    {{ end }}
{{ end }}

{{ with $backlinks }}
    <section class="backlinks">
        {{ printf "%s" ($.heading | default "<h2>Backlinks</h2>") | safeHTML }}
        <nav>
            <ul>
                {{ range . }}
                    <li><a href="{{ .RelPermalink }}#top">{{ .Title }}</a></li>
                {{ end }}
            </ul>
        </nav>
    </section>
{{ end }}
```

I added `#top` to the `.RelPermalink` URL. Other than that, it's unchanged. They warn that this template is inefficient. I'll revisit it eventually. There's [a discussion in the Hugo forum](https://discourse.gohugo.io/t/parsing-backlinks-in-hugo/38281) about it. Perhaps there are clues to a more efficient implementation there.



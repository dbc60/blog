---
title: Serving a Blog
date: 2016-09-04
2016: ["09"]
tags: [blog]
---

I want a blog where I control the design and layout. I want to be able to change the way it works and appears so I can experiment with various ideas, learn by attempting to replicate other designs and see what happens.
<!--more-->

I've tried CMS solutions running on Linux-based servers. One of the first ones I tried many years ago was [Apache Cocoon][1]. I was enticed by how flexible and programmable it was with its pipeline architecture. It seemed anything was possible. Ultimately, trying to program using XML and XSLT, and configure Java servlets proved to be too complicated. The languages and processes needed to keep the site up and running were too far removed from those for adding content.

The mechanics of site maintenance took too much time away from just plain writing. I didn't realize that was the problem at the time, so I allowed myself to be lured into other complex solutions. I tried [Plone][2] for a short while, but got tired of configuration bugs (the bugs were probably mine, and I was too impatient to figure out how to make Plone work correctly). I had a short run with [web2py][3] and a long one with [Drupal][4] 5 and 6. Drupal was fun and I did get it to work fairly well. The only real problem was keeping up with patches for the core system as well as all of the plug-ins. They made it relatively easy to do, but it was another time consuming annoyance.

I ran each of these CMS solutions from a Windows box at home and a dynamic DNS provider. Besides being cheap and rickety, there were always quirks running on Windows as most of these systems were designed and tested on Linux. Windows support varied from very well to an after thought.

## Simplicity

I've come around to thinking that if I'm going to have a corner of the web to express my thoughts, the tooling and maintenance of it should be as simple and low-overhead as possible. Static sites are very appealing in this respect. Post a little content wrapped in some HTML, give it some style with CSS and it's done.

Still, nothing is ever quite simple when it comes to digital information. I'm always concerned about having copies of data to prevent loss. I'd like be able to look back and see how I got to where I am today - especially when it comes to reverting changes that, upon reflection, weren't so good. I also don't have a lot of spare cash to spend, so most cloud servers are out of the questions.

I did use a small [Digital Ocean][5] droplet for a while - only $5.00 USD/month. It addressed the cash issue very well, and I used [Fossil SCM][6] for version control. I also have a server running [FreeNAS][7] where I backup all my data.

To build anything on a computer, you need good tools. For static site generation, I settled on [Jekyll][8], a static site generator that turns [Markdown][9], HTML and CSS (and even [Sass][10] into a website. I made changes locally, and ran Jekyll to see the results. When I was satisfied, I'd check-in  the changes to Fossil and copy, via SSH, the `_site` folder to my droplet where [nginx][11] would serve the content. I thought it was as simple as it could get.

It does get more simple. [GitHub][12] is an amazing site that lets anyone make a [git][13] repository. If you don't mind it being publicly available, then their service is *free*! They also make it easy, with Jekyll, to create a personal website. I no longer have to be (directly) concerned with web server configuration and security. That's offloaded to the experts at GitHub. Also, uploading changes to my site is easier. All I have to do to update my blog is to commit the changes to my local repository and execute `git push origin`.

## The Remaining Complexity

At this stage, I can't imagine how it could be easier (and certainly it can't be cheaper). The only complexity left is figuring out how to make my blog appear pleasing to the eye. That's a matter of laying out some HTML, writing content marked up with [Github Flavored Markdown][14] and using CSS and [SCSS][15] to give it some style.

I originally had a complex mess inherited from previous attempts at making a personal site with varying goals. I've now pared it down to something much easier to manage. I'll post again about my current, more modest goals, what inspired the current design and how I'm going about the process of reaching them.

## References

- [Apache Cocoon][1]
- [Plone][2]
- [web2py][3]
- [Drupal][4]
- [Digital Ocean][5]
- [Fossil Source Control Management][6]
- [FreeNAS][7]
- [Jekyll Static Site Generator][8]
- [Markdown Markup Language][9]
- [Sass Stylesheet Language][10]
- [nginx web server][11]
- [GitHub][12]
- [git][13]
- [GitHub Flavored Markdown][14]
- [SCSS][15]

[1]: http://cocoon.apache.org/
[2]: https://plone.org/
[3]: http://www.web2py.com/
[4]: https://www.drupal.org/
[5]: https://www.digitalocean.com/
[6]: http://fossil-scm.org/index.html/doc/trunk/www/index.wiki
[7]: http://www.freenas.org/
[8]: http://jekyllrb.com/
[9]: https://daringfireball.net/projects/markdown/
[10]: http://sass-lang.com/
[11]: https://www.nginx.com/
[12]: https://github.com/
[13]: https://git-scm.com/
[14]: https://guides.github.com/features/mastering-markdown/
[15]: http://thesassway.com/editorial/sass-vs-scss-which-syntax-is-better

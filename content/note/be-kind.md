---
title: Be Kind
date: 2016-10-14
draft: true
categories: blog
tags:
  - kindness
  - trust
---

I read a really nice, concise article on what happens when we remember that we all make mistakes.
<!--more-->

This post, [Be Kind](https://www.briangilham.com/blog/2016/10/10/be-kind) by Brian Gilham, is right on target. I have experienced what happens when, not only an individual is not kind, but a company's culture is unkind and unforgiving of errors and dissent.

When I started worked at *previous employer* as a Sustaining Engineer, things were moving fast. The development team was hard at work on the next big thing. Nevertheless, they were always helpful, supportive and would point us sustainers in the most likely direction that would solve a technical issue with each release. Still, customer problem reports would fly in at amazing rates after a new release. I worked hard, and picked up on their technology. By the end of three months, I was making significant contributions to resolving customer problems and was reducing the support load on the development team.

After about seven months of work, I was asked to support *previous employer's* other product. The technology was completely different, as was the development team. One other sustaining engineer and I were pushed hard to come up to speed. I made a couple of mistakes along the way - especially pushing changes out to customers. We had a critical error that a very important customer had run into. I was tasked with getting a patch out within 24 hours. I found that our development branch didn't have the issue, so pulled some code from there into a patch for a production release. Oh, and there was no formal patch process. It consisted of a python script and some file/directory conventions hacked together by the lead developer to create and ship patches in a zip file.

I followed his process, since that was the only one we had. This time, because I pulled code from the development tree instead of writing something myself, I had made some kind of unforgivable transgression. I thought I was merely doing what they asked, and solving the customer's problem as quickly as possible. There were no unit, integration nor system tests. All I could do was setup a few virtual machines, attempt to recreate the problem, and once found, see that the new code no longer demonstrated the issue. Not only did that process take several days, I was unable to reproduce the initial problem - nor was I able to be sure I had the exact release the customer was using. The source code repository hadn't been tagged with that release. One of the developers looked at the git log and helped me make a best guess as to which commit was the right one. It was a totally messed up process.

Regardless of all the development and repository issues, I was able to find a section of code that looked like it could be the problem if circumstances were just right. I replaced it with some development code that handled a variety of "corner cases", and showed that I couldn't reproduce the issue with that either.

I was already a couple of days late, and my boss was pushing hard for a patch, so I assembled a patch by mirroring the hack I had been given as a template. We shipped it, but when word got back to the developers on what I had used a couple of them were seriously upset with the process and where the code came from. Instead of being kind and working with me to create a new patch process (and maybe add a step for peer code review, like a good engineering team would have), I was put on a 45-day improvement program. I've since found out from others who have been put on that program, that it amounts to a CYA process where *previous employer* can fire you without fear of a lawsuit, as they've "documented" your failings.

It's a terrible way to treat employees and made me feel horrible for a long time. They could have been kind. They could have admitted that part of the problem was theirs. We could have worked together to find a better process. It would have been better for us both if they had.

I'm still angry with them. Poor training. Poor configuration management. An unending head-long rush to quell customer complaints and no regard for employees, the value to the company nor their quality of life. I'm really happy to be away from that infuriating chaos.

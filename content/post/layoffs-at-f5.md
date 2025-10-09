---
title: "Layoffs at F5"
date: 2023-04-25T07:43:42-04:00
years: ["2024"]
tags: ["life"]
lastmod: 2023-11-18
---
In April 2023, I was laid of from [F5, Inc.][F5]. It was a significant layoff of about 9% of the workforce, or 623 employees, worldwide. Given that the economy, at least here in the United States, doesn't seem all that bad, I was surprised to see so many good engineers, product managers, sales people, and others let go.
<!--more-->
I started working for F5 after it acquired Threat Stack on October 1st, 2021. At the time I worked in the Application Infrastructure Protection (AIP) division doing pretty much what I was working on before—adding features to the Windows, Linux, containerized, and Fargate agents.

It's not just the layoff that upset me. I really enjoyed working in the Agent Team and particularly on the Windows agent, but now I hear that the company intends to disband AIP, and everything that Threat Stack built over the past decade or so will be gone.

The agents were all well built tools providing telemetry to a backend platform that analyzed events to detect anomalous behavior. Several years ago, an intern and I developed the Windows agent from scratch. The team and I enhanced its capabilities through the years. I thought it had a few clever designs, especially when it came to monitoring activity in the file system.

File system monitoring was accomplished with a quite capable and efficient kernel minifilter. It had a glob pattern-matcher for comparing file activity against a set of rules that defined what behavior was "interesting". Among other things, it could accurately detect file deletions, which is hard to do on NTFS. The minifilter had its own memory allocator and tagged allocations based on what the memory was used for. By running `poolmon`, it was easy to determine which components were allocating memory, how much they were allocating, and also ensure that there were no memory leaks at all.

The agent also monitored running processes, associated those processes with the accounts they were running under, watched network connections being established and broken, and looked for significant security-related events. All of this information was relayed to the backend platform for analysis. It was a good system that provided our customers with the situational awareness they needed to mitigate attacks and even stop attacks before a serious incident occurred.

**Update November 2023**: Yeesh! F5 had another round of layoffs earlier this month. More of my friends and previous coworkers are now looking for work. It just feels wrong. Yes, there have been a lot of layoffs from much larger tech companies, but they are still raking in lots of money. I suspect F5 is still doing very well, too. They are probably eliminating projects (and thus the employees who were working on them) that don't directly support their core hardware business and (I assume) their aspirations to develop virtual network devices and their own cloud.

[f5]: https://f5.com

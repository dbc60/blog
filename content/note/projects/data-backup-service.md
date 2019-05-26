---
title: Make Digital Data Backup Service
date: 2016-09-05T07:33:00-05:00
draft: true
categories: [projects, software]
tags: [data backup, service, cloud, application]
---

I'd like to see if I can make a data backup service.
<!--more-->

## Things To Do

- Planning
- Architecture
- Features

## Project Goals

There are two, or possibly three backup service levels for which I'd like to provide:

1. Public Cloud: A cloud backup service, where each host runs an agent that connects to the cloud service. This is subscription based, and I maintain the servers where backups are stored.
1. Private Cloud: An in-house backup service, where I sell the server-software that enables customers to run their own backup service. Income will come from the sale of the server software, subscriptions to support plans, and licensing of client software.
1. Standalone: A consumer-level product that runs on a single desktop and backs up files to an external drive (such as a USB drive) or a network drive. It is a standalone product. Customers pay once and get updates for bug fixes. As new, major releases become available, current customers can upgrade for a modest fee.
    - Consider how licensing works here. Do I want to allow multiple installations?
    - Maybe this could be a low-cost "gateway" to entice people into buying in to the subscription cloud service. The pitch being, if you like the backup/recovery features of the standalone product, then get event greater data-security by using the subscription service.

Additional Goals:

- Create a standalone backup tool that copies files from the host to one or more external drives or a network storage device. All that will be necessary to communicate between the agent and the storage device is a network connection. No server software required.
- Create a cloud backup service that is subscription-based.
- Create a backup service that will run on a LAN. This consists of server software that receives data from one or more agents running on the LAN, and agent software running on each host. The sales model might be akin to an arms dealer. Don't get involved in the daily prosecution of the war/backup effort - just provide the tools necessary to effect prosecution.
- The agents should run on Windows, FreeBSD, Linux and OS X. It would also be nice to have a mobile app (that runs on iPhone and Android) for users to monitor the state of their backups and control their accounts - add/remove services, monitor costs, pay bills, etc.
- The LAN service should run on Windows, FreeBSD, Linux and OS X so customers can have their own in-house backup service instead of a cloud subscription. The in-house service will come with an optional subscription for various levels of support.

## Three Levels of Encryption
We need three levels of encryption for communications between clients and the server(s). The outer most level will be SSL/TLS, which is what makes HTTPS communications secure. Sometimes SSL/TLS fails, as in the case of the [Heartbleed](https://en.wikipedia.org/wiki/Heartbleed) bug in OpenSSL and as in the case of [Cloudbleed](https://blog.cloudflare.com/incident-report-on-memory-leak-caused-by-cloudflare-parser-bug/) where Cloudflare was leaking uninitialized memory on some of its services.

[1Password](https://blog.agilebits.com/1password-apps/) wrote a [blog post](https://blog.agilebits.com/2017/02/23/three-layers-of-encryption-keeps-you-safe-when-ssltls-fails/) stating that their customers data is safe despite the Cloudflare bug. First, they use [Secure Remote Password](https://en.wikipedia.org/wiki/Secure_Remote_Password_protocol) (SRP) protocol during sign-in. That means no secrets are transmitted between 1Password clients and [1Password.com](https://1password.com/). Instead, the server and client prove their identity to each other without transmitting secrets.

1Password's three layers are:

1. SSL/TLS.
2. Their own transport layer authenticated encryption using a session key that is generated using SRP during sign-in. The secret session key is never transmitted.
3. The core encryption of their clients' data. Except for when you're viewing your data on your system, it is encrypted with keys that are derived from your Master Password and your Secret Account Code. This is the most important layer, as it would protect you even if 1Password's servers were to be breached (and their servers have _not_ been breached).

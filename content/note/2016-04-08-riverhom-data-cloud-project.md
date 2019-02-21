---
title: Riverhom Cloud Bank Project
date: 2016-04-08
draft: true
categories: projects
tags:
  - design
  - project
  - backup
---

A data backup project. I might rename it to just Riverhom with a slogan/subtitle of "Data Storage".
<!--more-->

## Design Summary

> "Um those [backups] got really expensive, so we stopped doing them about a month ago"
>
> -- Hotmail Administrator, after a buggy janitor program wiped out the in-boxes of 25% of their customers, instead of cleaning the trash.

What makes Riverhom Cloud Bank unique? Riverhom focuses on security. All data stored on Riverhom servers is encrypted and can be retrieved only by those customers' who placed it on Riverhom. There will be an option to store keys, but they will be encrypted using a key generated from the customer's ID, password and other information used to verify the customer's identity.

Riverhom Cloud Bank uses space-efficient means to store customer data. Each copy of the same data will be identified by a unique ID, so the actual data, compressed and encrypted, will be stored only once per server node. It will be possible to also create redundant copies of data on the Riverhom servers to reduce the possibility of data loss from hardware or other failures.

Customers will also be able to share any of their data with anyone they wish by creating a unique key. That key will provide access to and decrypt a selected file or set of files to make them available to another individual or group.

### Elevator Pitch

Riverhom Cloud Bank is an island of security in a flood of mishaps. It provides peace-of-mind knowing that your valuable photos, videos and all other digital content can be securely recovered when disaster occurs. The customer has complete control over his or her data. They can decide to keep it all private, in which case noone else can access it from the Cloud Bank. They can also decide with whom to share data and exactly which files and folders will be shared.

### Storyboard

When potential customers accesses the Riverhom Cloud Bank website, they will be given information about Riverhom Cloud Bank and a link to download the installer for the Riverhom Client. Persons who choose to, may download the installer and install the Client. Once the client is installed and running, the client will give them the option to log into an existing account or create a new one.

Account creation involves filling out a form to submit just enough contact information to get started (name, email, phone). Billing information will come into play when the person decides to subscribe to the backup service.

A trial period of 30 days is allowed where the person may backup and recover a limited amount of data, probably around 5 GB or so, to try the service before subscribing to it. In fact, the client provides tools to simulate failure and recovery. It will backup a folder of their choosing, move or rename it, restore the data from the Cloud Bank and compare it with the original. It will display graphs or tables with data showing the time and cost of backup, storage and recovery. Once the trial period is over, no further backup nor recovery actions will be allowed. The customer will be given a grace period (perhaps 15 days) to subscribe before their data is completely wiped from Riverhom Cloud Bank. If the customer subscribes within the trial period or the grace period, the data will remain to reduce bandwidth.

Those who decline the service may remove their data and account information immediately, if they are online, by uninstalling the Client. If they are not online, the data stored during the trial period will be automatically deleted from Riverhom.

Customers may use the Client program to select which files and folders they wish to backup, and the backup schedule. They may choose a schedule that fits their needs. There are ranges from Continuous, which will upload modified files every few seconds, to various backup intervals and scheduled times and dates when backup events may occur.

### Unique Selling Proposition

What makes this product stand out from the competition? We don't have the keys, so we can't give your data to anyone else, including government agencies, nor can thieves steal it. Billilng information and personal details are handled on separate servers on a separate network to reduce the possibility of a breach on one system compromising the entire system.

## Design Details

Include a subsection for each aspect of the product; what the users have, what they can do with it and what the expected outcomes are. Also discuss the architecture of the product. If it's a client/server model, flesh out the design of the client and server components, how they interact, what operating system(s) they run on, components on which they depend and the provisions required (machine capacities, network load, etc.).

## Designer Notes

### 2016.04.09

I've started a storyboard that roughly discusses a client/server version of Riverhom Cloud Bank, but I also want to have a standalone version for people who, instead of subscribing to a cloud service, wish backup their data to their own server(s). There should be a personal version, where data is backed up to a local drive, such as a USB drive or even a Network Attached Storage (NAS) device.

There should also be a client/server version where customers can host their own server(s) on their own network. This is the private cloud offering. The server or cluster of servers will have license packs, which can be purchased in a variety of sizes, to allow up to a given number of clients to connect and backup their data. Revenue will be generated from the sale of the server, license packs and support subscriptions. Eventually, I'll make support will be available in a variety of levels, each with its own Service Level Agreement (SLA). Details to follow, but not for a while.

My first priority is to get a personal version out. Keep it simple, but provide some options to hint at what will be available via the cloud service and the private cloud offering. For example, the personal version will have options to compress, encrypt and de-duplicate the copies on the backup location (whether it be a USB disk or a NAS device).

## Business Model

Discuss how revenue is acquired. Is it subscription based, freemium (free to play, but in-game content other than basic content must be paid for), supported by advertising or donations, pay-once and play forever or some other model?

## Competition

In my post on [businesses and startups](/notes/2016-11-04-business-and-startups), I copied a list of the best backup software of 2016 from PC Magazine's article [The Best Online Backup Services of 2016]((http://www.pcmag.com/article2/0,2817,2288745,00.asp) (note: I need to look at PC Magazine's article [The Best Backup Software of 2016](http://www.pcmag.com/article2/0,2817,2278661,00.asp). One of the best services is [CrashPlan](https://www.crashplan.com/en-us/).

I installed the standalone version of CrashPlan, and I think I can easily beat its performance. Instead of keeping a list of changed files, it scans the entire harddisk once each day. I think I can use the NTFS journal to keep track of which files have changed, and just update the backup copy of those files.

Acronis True Image 2017 might be harder to beat. The 2016 version is an Editor's Choice in [The Best Backup Software of 2016](http://www.pcmag.com/article2/0,2817,2278661,00.asp). I'm downloading a free 30-day trial to test it. One hour into backing up the whole machine, Acronis True Image 2017 estimates another 15 hours. That's very good.

## Connecting to a NAS for Backup

Today (Saturday, 2017.01.07) I learned that Windows doesn't allow more than [one SMB connection](https://support.microsoft.com/en-us/kb/938120) to Network Attached Storage (NAS). That caused all kinds of problems when I attempted to use my FreeNAS server as a backup target for Acronis True Image ATI). At some point, I had mapped `W:` to `\\FreeNAS\Workstations`.

I have no idea what credentials I used to map the drive - they should be no username nor password, becuase I set it up to use `guest` privileges. Still, it made no difference what credentials I fed to ATI. It would not connect. Once I deleted the drive mapping (via `net use w: /delete`), ATI was able to connect. I gave it my username, `Doug`, and my password. It finally connected.

[This Stackoverflow question](http://superuser.com/questions/95872/sambawindows-allow-multiple-connections-by-different-users) has a few good answers for dealing with this limitation. First, you can make one connection via the network share, such as `\\FreeNAS\Workstations`, and another via the server's IP address, such as `\\192.168.1.180\Workstations`.

Another workaround is to edit you're `hosts` file (`C:\Windows\system32\drivers\etc\hosts`). Run the editor as an administrator, or you won't be able to save your changes. You can use some variation of this idea. Say you have three samba shares on your NAS server (running on `192.168.1.180`), like `docs`, `stuff`, and `pics`. You want to connect as `tom` to `docs`, as `fred` to `stuff` and as `jon` to `pics`. Add the following lines to the `hosts` file:

```text
192.168.1.180   tomsdocs    tomsdocs
192.168.1.180   fredstuff   fredstuff
192.168.1.180   jonspics    jonspics
```

Once you save and close the hosts file, you can map three separate network drives like so:

```text
\\tomsdocs\docs as user tom
\\fredstuff\stuff as user fred
\\jonspics\pics as user jon
```

Finally, you can edit the `smb.conf` file on the server. Add the following entry to the `[global]` section:

```text
[global]
...
netbios aliases = alias1 alias2 readonly
```

though, I'm not sure about the `readonly` setting. After restarting `smbd` and `nmbd` you should be able to access the new server aliases using UNC notation in Windows Explorer. Note that it may take a minute or so for the aliases to show up in the Window Network.

## References

- *The* Indie Game Development Survival Guide

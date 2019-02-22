---
title: Windows Server Core Administration
date: 2016-11-11
draft: true
categories: operating systems
tags:
    - windows
    - core
    - cli
---

Here are some key commands for running Windows Update and other tools on Windows Server 2012 R2 Core.
<!--more-->

## Configure Windows Update

Log in as an administrator and `cd \Windows\System32`. It seems to be the place where scripts and services are located. Run the following commands to set Windows Update to run automatically, and to automatically detect new updates.

```doscon
C:\Windows\System32>Cscript SCregEdit.wsf /Au /v
Microsoft (R) Windows Script Host Version 5.8
Copyright (C) Microsoft Corporation. All rights reserved.

SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update AUOptions
Value not set.

C:\Windows\System32>net stop wuauserv
The Windows Update service is stopping.
The Windows Update service was stopped successfully.

C:\Windows\System32>cscript SCregEdit.wsf /AU 4
Microsoft (R) Windows Script Host Version 5.8
Copyright (C) Microsoft Corporation. All rights reserved.

Registry has been updated.

C:\Windows\System32>net start wuauserv
The Windows Update service is starting.
The Windows Update service was started successfully.

C:\Windows\System32>wuauclt.exe /detectnow

C:\Windows\System32>
```

## Configure Passwords to Never Expire

Run `net accounts /maxpwage:unlimited` in an admin console.

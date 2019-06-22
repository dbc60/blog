---
title: Remote Debugging with Visual Studio
date: 2016-10-20
draft: true
categories: software
tags: [debugging, software development, visual studio]
---

Remote debugging is a useful technique for debugging Windows services. First, the remote host needs to be properly configured.
<!--more-->

The idea is to install `msvsmon.exe` on a remote host so Visual Studio 2015 can
attach to it and perform remote debugging tasks. Please refer to the [full
instructions](https://msdn.microsoft.com/en-us/library/y7f5zaaa.aspx). Note
that if Visual Studio is already installed on the remote host, then
`msvsmon.exe` is already installed and is located at `<Visual Studio
installation directory>\Common7\IDE\Remote Debugger\(x64, x86, Appx)
\msvsmon.exe`. However, the Remote Debugger Configuration Wizard (rdbgwiz.exe)
is installed only when you download and install the tools, and you may need to
use it for configuration later, especially if you want the remote debugger to
run as a service.

## Setup

First, on the target machine, download [Remote Tools for Visual Studio 2015]
(https://www.visualstudio.com/downloads/#remote-tools-for-visual-studio-2015)

## Configuration

Use `rdbgwiz.exe` to set `mscsmon.exe` to run as a service.

## Debugging

[Attach to running processes with the Visual Studio debugger](https://
msdn.microsoft.com/en-us/library/3s68z0b3.aspx).

## Debugging Windows Services

We need to prevent the Windows Service Control Manager (SCM) from killing the
service while we're debugging it. Create a registry DWORD key called
`ServicesPipeTimeout` under
`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control` and set its value to
`86400000` (the number of milliseconds in 24 hours) and reboot so the SCM can
pick up the new value. This will prevent the SCM from killing the service
during debugging.

---
title: Miscellaneous Windows Settings
date: 2016-09-12T09:45:00-05:00
draft: true
categories: windows
tags: [kernel, debug, boot, config]
---

Registry, boot (bcdedit), and other settings
<!--more-->

## Registry Settings

## Boot Settings

These may overlap with those in [Kernel Debugging](2016-07-29-kernel-debugging).

To help with [Window does not appear in front](http://answers.microsoft.com/en-us/windows/forum/windows_7-performance/windows-7-explorer-window-does-not-appear-in-front/1199682e-2415-4a7a-bf21-f57a972122ee), see the following links:

- [Foreground Lock Timeout](https://technet.microsoft.com/en-us/library/cc957208.aspx)
- [Foreground Flash Count](https://technet.microsoft.com/en-us/library/cc957205.aspx?f=255&MSPPError=-2147217396)

Windows 10 hides error codes when there's a Blue Screen of Death (BSOD). To make display the error code, open the registry editor and navigate to ``HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\CrashControl``. Create a new DWORD value named **DisplayParameters** and set it to 1. Restart and next time it BSOD's the error code will be diplayed.

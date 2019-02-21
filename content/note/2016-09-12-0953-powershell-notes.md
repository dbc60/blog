---
title: PowerShell Notes
date: 2016-09-12T09:53:00-05:00
draft: true
categories: programming
tags: [powershell]
---

Powershell notes, examples, links and reference material.
<!--more-->

## Escape Sequences

Today I learned that to escape double quotes in PowerShell scripts they must be preceded by a backtick (`` ` ``). For example:

```ps1
$cmd="\\server\toto.exe -batch=B -param=`"sort1;parmtxt='Security ID=1234'`""
```

`$cmd` is returned as:

```ps1
\\server\toto.exe -batch=B -param="sort1;parmtxt='Security ID=1234'"
```

## Automatic Variables

- `$PSScriptRoot`: Contains the directory from which a script is being run.
- `$PSCommandPath`: Contains the full path and file name of the script that is being run. This variable is valid in all scripts.
- `$MyInvocation`: Contains information about the current command, such as the name, parameters, parameter values, and information about how the command was started, called, or "invoked," such as the name of the script that called the current command.

$MyInvocation is populated only for scripts, function, and script blocks. You can use the information in the System.Management.Automation.InvocationInfo object that $MyInvocation returns in the current script, such as the path
and file name of the script ($MyInvocation.MyCommand.Path) or the name of a function ($MyInvocation.MyCommand.Name) to identify the current command. This is particularly useful for finding the name of the current script.

Beginning in Windows PowerShell 3.0, $MyInvocation has the following new properties.

- `PSScriptRoot`: Contains the full path to the script that invoked the current command. The value of this property is populated only when the caller is a script.
- `PSCommandPath`: Contains the full path and file name of the script that invoked the current command. The value of this property is populated only when the caller is a script.
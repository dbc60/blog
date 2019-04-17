---
title: Real Time Linux
date: 2016-03-07
draft: true
categories: [projects]
tags: [linux]
---

My goal is to learn how to install a real-time Linux kernel and use it to build and run real-time applications.
<!--more-->

## Getting Started
I'm starting out by running CentOS 7 on a VirtualBox VM. I used the minimal install to keep things as clean and simple as possible. One of the first things I did was to update the kernel via ```yum -y update kernel```. After rebooting, the kernel version is:

    > uname -r
    3.10.0-229.el7.x86_64

Now to prepare to build a custom kernel:

    [doug@new-host-3 ~]$ sudo yum groupinstall "Development Tools"
    [doug@new-host-3 ~]$ sudo yum install ncurses-devel
    [doug@new-host-3 ~]$ sudo yum install hmaccalc zlib-devel binutils-devel elfutils-libelf-devel
    [doug@new-host-3 ~]$ mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
    [doug@new-host-3 ~]$ echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros
    [doug@new-host-3 ~]$ sudo yum install rpm-build redhat-rpm-config asciidoc hmaccalc perl-ExtUtils-Embed pesign xmlto
    [doug@new-host-3 ~]$ sudo yum install audit-libs-devel binutils-devel elfutils-devel elfutils-libelf-devel
    [doug@new-host-3 ~]$ sudo yum install ncurses-devel newt-devel numactl-devel pciutils-devel python-devel zlib-devel

Install the kernel source RPM package as an ordinary user, not root:

    > rpm -i http://vault.centos.org/7.1.1503/os/Source/SPackages/kernel-3.10.0-229.el7.src.rpm 2>&1 | grep -v exist

Here's what's installed:

    [doug@new-host-3 ~]$ rpm -q kernel | sort
    kernel-3.10.0-229.20.1.el7.x86_64
    kernel-3.10.0-229.el7.x86_64

I think I'm going to restart this project by first building Linux From Scratch.

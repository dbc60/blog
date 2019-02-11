---
layout: page
title: Vagrant
author: Douglas Cuthbertson
categories: notes
tags:
    - vagrant
    - devops
excerpt: Using vagrant to create, and manipulate virtual machines.
---

## Contents
{:.no_toc}

- TOC
{:toc}

## Document History

| Date | Author | Summary of Changes |
|-----------:|-------------:|:------------|
| 2016.03.18 | Douglas Cuthbertson | Initial draft |

## Running an Established Vagrant Environment
A recent vagrant session.

```
C:\> P:

P:\> cd Vagrant

P:\> cd vagrant_getting_started
```

Display the `Vagrantfile` (`type Vagrantfile`):

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.provision :shell, path: "bootstrap.sh"
  config.vm.network :forwarded_port, guest: 80, host:4567
  # I'm not sure this is needed to set the MAC address
  #config.vm.base_mac = "080027880CA6"
  # Other possibilities from stackoverflow:
  # config.vm.network :bridged , :mac => "080027XXXXXX"
  # config.vm.network "public_network", :bridge => 'enp4s0', :mac => "5CA1AB1E0001"
end
```

Start the VM:

```shell
P:\> vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Checking if box 'hashicorp/precise64' is up to date...
==> default: Clearing any previously set forwarded ports...
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 80 (guest) => 4567 (host) (adapter 1)
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: Warning: Remote connection disconnect. Retrying...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: The guest additions on this VM do not match the installed version of
    default: VirtualBox! In most cases this is fine, but in rare cases it can
    default: prevent things such as shared folders from working properly. If you see
    default: shared folder errors, please make sure the guest additions within the
    default: virtual machine match the version of VirtualBox you have installed on
    default: your host and reload your VM.
    default:
    default: Guest Additions Version: 4.2.0
    default: VirtualBox Version: 5.0
==> default: Mounting shared folders...
    default: /vagrant => P:/Vagrant/vagrant_getting_started
==> default: Machine already provisioned. Run `vagrant provision` or use the `--provision`
==> default: flag to force provisioning. Provisioners marked to run always will still run.
```

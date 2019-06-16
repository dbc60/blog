---
title: About Electronic Files
date: 2016-03-07
draft: true
categories: [software]
tags: [files]
cssDetail: drop-caps-cheshire
---

If you can get a collection of important files, their attributes and contents, what kinds of things can you do with that information?

<!--more-->

One can hash the contents to create a unique identifier.

- MD5 + file size should be unique and very fast
- SHA1 will be less likely to create a hash collision
- SHA256 will be even less likely to create a hash collision.

Other actions:

- Find files and folders based on attributes such as size, last access time, last modification time, owner, or whether or not the file is hidden.
- Find and possibly eliminate duplicates.
- Backup files and determine if a file has changed since it was last copied to one or more backup locations.
- Create different views of the contents of the file system. The views could be based on a number of file attributes.
- File Sharing

  - Access your own files from your own devices (desktop, laptop, tablet, mobile devices)
  - Enable others to access your files from their devices.
  - Control when files can be accessed and by whom.
  - Control the kind of access others may have (read, write, delete, move, rename, etc.).

Note that *read* means copy to another device so the user of that device can access the contents of the file. Unless the app provides a Snapchat like feature that will delete the file after some period of time, the person who reads the file will have their own copy and will likely be able to modify that copy to their hearts content. They will *not* be able to modify the shared original, unless they are given write access. Delete controls who can delete the shared file. It has no bearing on the copy that is created to share the file.

What if file sharing means there is a copy of a file that's actually shared. If the copy gets modified or deleted, it will not necessarily mean that the original is modified or deleted. How can file synchronization be controlled and managed? It could be like distributed version control repositories where the cloud version is considered to be a central repository, and copies of files on other devices are considered to be relatively independent satellite repositories. In this case, one person or role has control over the contents of the central repository while others are granted different kinds of access to the central repository, but have full control over their local copies.

Once you can uniquely identify a file, you can find duplicates. What do you do with duplicates? One copy could be kept and the others deleted to save space on disk. One copy could be considered the *true* instance and the others could each be replaced by a link to the one true instance. This saves disk space and continues to make the file available from various locations in the file system. It does mean that if the *true* copy is modified, all other "copies" will always be the same.

One can use this information to find files and directories by size or by other attributes. Sometimes, I want to know which files or directories are taking the most space. Perhaps there are files I no longer need, so I can save space by deleting them, and I might as well start looking for the ones that take the most space, or perhaps are the oldest, or haven't been touched/accessed within some period of time.

## Component Processes
What components need to exist so one can view the landscape of their files and control access to them?

- Inventory. One needs to be able to create an inventory that is searchable, can be filtered on various axes and kept up-to-date.
- Encryption for secure transfer and storage of information.
- Authentication for identity management.
- Authorization for access control.
- Change management and version control.
- Logging to maintain a history of state changes to the system.
- Auditing to ensure the state of the system can be reviewed and is consistent with the user's expectations.
- Monitoring to provide alerts for such things as resource depletion or unexpected/undesirable events.
- Command & Control to provide operational visibility, perhaps in the form of dashboards and summary reports (graphical user interfaces, web pages, electronic displays, email notifications, generated report files, etc.)
- Modeling, testing and simulation so one can better explore and plan for various "what if" scenarios.
- Scripting to create recipes for common sets of actions that can be shared across the system.
- Volume Shadow copy Service (VSS) interface to ensure files contents are consistent in the face of other processes modifying them during a copy or backup operation.

### Inventory Creation and Maintenance
None of this is possible without an inventory of files and directories within a host system. I'm first going to consider a host running some relatively recent version of the Microsoft Windows operating system (at least Windows XP, or Server 2003) and NTFS format version 3.1. The file system, NTFS, is the real focus. It is a journaling file system, which means it keeps track of changes not yet committed to permanent storage. That is, the journaling feature works to ensure the file system will remain consistent in the event of a system crash, and allow for easy rollback of uncommitted changes to critical data structures when the volume is remounted.

I've read that there are a few ways to enumerate all the volumes, folders and files within NTFS. Some are faster than others.

#### How to Enumerate Volumes, Folders and Files
More to come ...

## References

- [NTFS overview on Wikipedia](https://en.wikipedia.org/wiki/NTFS).

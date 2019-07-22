---
title: "Windows Drivers"
date: 2019-07-17T20:54:05-04:00
draft: true
---

If you’re not a file system dev, you’re probably thinking “How complicated can delete be?  You just… delete the file, right?”  Well, not in Windows, no.
<!--more-->

From [An Introduction to Standard and Isolation Minifilters](https://www.osr.com/nt-insider/2017-issue2/introduction-standard-isolation-minifilters/):

The native Windows API doesn’t actually have a specific delete file operation.  Rather, the intention to delete a file is indicated by issuing a Set Information operation (ZwSetInformationFile)  to set the file’s Disposition (FILE_DISPOSITION_INFORMATION).  This allows the caller to specify whether he wants the file to be deleted when its closed.  However, it’s important to note that the file is not actually deleted until the last handle to the file has been closed.  This means that an application can open a file and call the Win32 DeleteFile API, but this doesn’t actually delete the file.  It just set the file’s Disposition of the file to be deleted on close.  Even when the app subsequently closes the file, this still doesn’t necessarily mean that the file will actually be deleted.  Consider what could happen if another application has the file open when our example app opens it.  That application can also set the file’s Disposition at any time.  If after our example app has set the file’s Disposition to be delete on close, the other app sets the file’s Disposition so that it’s no longer marked for delete on close, the file will not be deleted.  And yes… it happens.

---
title: Minifilters
date: 2019-04-04T11:11:11-05:00
draft: true
tags:
  - windows
  - kernel
  - minifilter
---

Notes on writing a Windows minifilter
<!--more-->

9269044

## Part I: Fundamentals of IRP_MJ_CREATE

Each service in the OS has its own protocol. A stateful protocol must have some kind of context object to pass from function to function to maintain the current state of the "conversation."

In the case of the file system, that object is a ``FILE_OBJECT``. It represents the state associated with the OS talking to a ``DEVICE_OBJECT``. Note that there is no ``IRP_MJ_OPEN``, because there is no way to open an existing ``FILE_OBJECT``. In order to get a ``FILE_OBJECT`` one must either create it or already have a reference to it.

## Part II: How IO Flows

Here's a partial callstack for a file create operation from ``nt!NtCreateFile`` to the filter manager's ``FltpCreate`` function:

    00 9b5c5a70 828484bc fltmgr!FltpCreate
    01 9b5c5a88 82a4c6ad nt!IofCallDriver+0x63
    02 9b5c5b60 82a2d26b nt!IopParseDevice+0xed7
    03 9b5c5bdc 82a532d9 nt!ObpLookupObjectName+0x4fa
    04 9b5c5c38 82a4b62b nt!ObOpenObjectByName+0x165
    05 9b5c5cb4 82a56f42 nt!IopCreateFile+0x673
    06 9b5c5d00 8284f44a nt!NtCreateFile+0x34

A user program's create function will eventually reach ``nt!NtCreateFile``, which is where the OS receives a request to open a file or a device. ``NtCreateFile`` is just a wrapper over the internal function ``IopCreateFile``. At this stage, a file name like ``C:\Foo\Bar.txt`` has already had the ``\??\`` prefix added to it, so ``NtCreateFile`` sees ``\??\C:\Foo\Bar.txt``.

``nt!IopCreateFile`` opens a file or device at the IO manager level. This is an internal function where most requests to open a file or device end up. This is what happens here:

1. The parameters for the operation are validated and checked to see if they make sense. If not (like you've asked for ``DELETE_ON_CLOSE``, but don't have ``DELETE`` access), it returns ``STATUS_INVALID_PARAMETERS``.
2. The ``OPEN_PACKET`` structure is allocated, and the create parameters are copied in.
3. The IO manager calls the OB manager to open the device (``ObOpenObjectByName``).
4. After ``ObOpenObjectByName`` returns, this function cleans up and returns.

When the IO manager calls ``ObOpenObjectByName``, the OB manager creates a handle for the object. Processing proceeds roughly as follows:

1. Capture the security context for this open, so that whoever needs to open the actual object can perform access checks. This also means that the file system itself doesn't rely on the thread context being the same and instead uses the context captured here. So minifilters should do the same when they care about the security context of a create.
2. Call the actual function that looks up the path in the namespace (``ObpLookupObjectName``).
3. If ``ObpLookupObjectName`` was able to find an object then a handle is created for that object (since this was an open type function).

When ``ObpLookupObjectName`` is called, the OB manager looks in the namespace for the path it needs to open (``\??\C:\Foo\Bar.txt`` in the example above). There are details on how the path is parsed in [About IRP_MJ_CREATE and minifilter design considerations - Part 2](http://fsfilters.blogspot.com/2010/12/since-weve-discussed-concepts-last-time.html). It involves getting to "``\Device\HarddiskVolume2``", a ``DEVICE_OBJECT`` object and calling its parse procedure. The parse procedure for a ``DEVICE_OBJECT`` is ``IopParseDevice``.

``IopParseDevice`` receives the remaining path, "``\Foo\Bar.txt``." This is where the difference between a file and a device becomes relevant. If there is no remaining path, this is treated as an open to the device. If there is a path, then this is assumed to be a file (or directory) open. This is a pretty involved function with many special cases. The interesting steps for a minifilter are:

1. Get the context for this create, which is the ``OPEN_PACKET`` structure from before (it's passed from ``IopCreateFile`` to ``IopParseDevice``).
2. Check to see if a file system is mounted on this device and if not, mount it.
3. Process the device hint, if there is any.
4. Allocate the ``IRP_MJ_CREATE`` IRP.
5. Allocate the ``FILE_OBJECT`` that will represent the open file.
6. Call the ``FastIoQueryOpen`` function (which the minifilter will see as an ``IRP_MJ_NETWORK_QUERY_OPEN``). The IRP parameter to this call is the IRP that was just allocated.
7. If the ``FastIoQueryOpen`` didn't work, send the full IRP to the file system stack by calling ``IoCallDriver``.
8. Wait for the IRP to complete (the IRP is synchronized by the IO manager).
9. If the request was a ``STATUS_REPARSE``, then first check if it is a directory junction or a symlink and do some additional processing for those. Copy the new name to open the ``FILE_OBJECT`` (the actual name to open is passed in and out of this function through a parameter).
10. If the status from the IRP was not a success status or it was a ``STATUS_REPARSE``, clean up the ``FILE_OBJECT`` and release the references associated with it. The IRP is always released anyway.
11. Return the status. If this was successful, the ``FILE_OBJECT`` will be the one used to reqpresent the file.

## Part III

Things to note when the OS takes a create request and sends an IRP to the file system:

1. CREATE operations must be synchronized by the OS. The CREATE operation simply means "hey everyone, there will be some requests in this context for this object so you'd better set up your contexts so you know what we're talking about when you get the next request". So the requestor can't really do anything until the request is complete since they don't even have a handle. This means that the IO manager will pretty much execute in a single thread and when it needs to wait for some other service (like the FS). It will send a request (the ``IRP_MJ_CREATE`` IRP) and wait for it to come back.
2. The FS stack is layered. The implication of this is that while the user can treat the CREATE operation as synchronous, the layers involved in processing that create can't. For file system filters (legacy and minifilters), there are 3 distinct steps:

    1. The work that takes place before the request makes it to the minifilter (before the ``preCreate`` operation is called).
    2. The minifilter's ``preCreate`` callback is called, and the work that takes place after the ``preCreate`` callback, but before the ``postCreate`` callback. At this stage, the minifilter has seen the request, but doesn't know whether it will complete successfully or not.
    3. The minifilter's ``postCreate`` callback is called and the work that takes place after that callback has returned. The minifilter knows the request has completed, but the IO manager doesn't yet know about it.

This places limitations on what each layer of the OS knows about the request. For example, during a ``preCreate`` callback the minifilter has an instance of a ``FILE_OBJECT`` (created by the IO manageer), but the file system (FS) doesn't yet know about it. Trying to use it to request something from the FS (like reading, writing, or even queries) will fail, because the FS has no idea what the ``FILE_OBJECT`` is supposed to represent. NOTE: the information about which stream on disk the ``FILE_OBJECT`` will represent is stored in the create IRP, and not the ``FILE_OBJECT``.

Similarly, during the ``postCreate`` callback, the filter knows how the FS ahndled the request (whether it was successful or not), but the IO manager doesn't. Trying to call a function that involves the IO manager for that ``FILE_OBJECT`` (e.g., ``ObOpenObjectByPointer``, which wants to create a ``HANDLE`` given an object) will fail.

## References

* [About IRP_MJ_CREATE and minifilter design considerations - Part 1](http://fsfilters.blogspot.com/2010/12/about-irpmjcreate-and-minifilter-design.html)
* [About IRP_MJ_CREATE and minifilter design considerations - Part 2](http://fsfilters.blogspot.com/2010/12/since-weve-discussed-concepts-last-time.html)
* [About IRP_MJ_CREATE and minifilter design considerations - Part 3](http://fsfilters.blogspot.com/2010/12/about-irpmjcreate-and-minifilter-design_30.html)
* [About IRP_MJ_CREATE and minifilter design considerations - Part 4](http://fsfilters.blogspot.com/2011/01/about-irpmjcreate-and-minifilter-design.html)
* [About IRP_MJ_CREATE and minifilter design considerations - Part 5](http://fsfilters.blogspot.com/2011/01/about-irpmjcreate-and-minifilter-design_13.html)
* [About IRP_MJ_CREATE and minifilter design considerations - Part 6](http://fsfilters.blogspot.com/2011/01/about-irpmjcreate-and-minifilter-design_20.html)

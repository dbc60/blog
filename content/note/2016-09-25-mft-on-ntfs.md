---
layout: post
title: The NTFS Master File Table
categories: windows
tags: [mft, ntfs]
---

How to find and read the Master File Table (MFT) on NTFS
<!--more-->

## Objectives

A program must have administrator or system privileges to access the master file table. I think what's best is to create a service to do the hard work, and a client program to access the results. I'd like to create a program similar to Everything from voidtools.com that lists all files in a volume. In fact, it should list all volumes attached to the local host as well as all files on each volume. I'll deal with network attached drives and mapped volumes later.

How can I present that information to the user? I need either a native GUI app or a web server/browser interface. They both require some design and interface decisions. The former requires some decisions regarding GUI libraries, or writing the interface from scratch, ala Handmade Hero. The latter requires knowledge of HTTP(S), CSS, JavaScript (or some language that compiles to JavaScript, like [TypeScript](https://www.typescriptlang.org/)), REST API development and maybe some kind of RPC interface.

While I feel completely comfortable writing the low-level code for reading and interpreting master file tables, I am completely out of my comfort zone when it comes to graphics. I'll have to learn, I guess. In fact, I'm going to guess that I can learn something about graphical user interface design and development if I learn how mobile apps are designed and developed.

I'll start with Android. [Android Studio](https://developer.android.com/studio/index.html) is the official IDE for Android development. The Android Studio site has [training for developing Android apps](https://developer.android.com/training/index.html).

## Project Details & Status

- Project Location: `E:\Users\Doug\Projects\DragonStash\trunk`
- Main Code: `src\win32_scratch_code.cpp`
- To Run: `build\vs2015\win32_dragonstash\x64\Debug\scratch.exe > data\disk_data_user-2016.11.15.0506.txt`
- Latest Admin Run: `data\disk_data_admin-2016.11.21.0624.txt`
- Latest User Run: `\data\disk_data_user-2016.11.15.0506.txt`

## Work Status
I'll list all the structures I need to read here and have two subsections; one to describe what's been done and another to describe what's left to be done. The master list will just be a high-level indicator as to what's been done and a list of the remaining work.

- [x] size of each MFT entry (1024 bytes).
- [x] layout of `struct MftEntry`, which is a header for a MFT entry.
- [x] Representing a MFT entry as its header, `MftEntry`, followed by an array of bytes called the `UpdateSequenceArray`.
- [x] Enumerate optical disks (CD/DVD/BluRay). Note that the code for getting the alignment descriptor worked in September, but now fails in November with "Error: 1, Incorrect function".
- [x] Enumerate physical drives.
- [x] Get information about the Master Boot Record (MBR).
- [x] Retrieve the NTFS Volume Boot Record.
- [x] Enumerate the Master File Table (MFT) entries.
- [x] Display Attribute Record Headers.
- [x] Display Standard Information (`ATTR_TYPE_STANDARD_INFORMATION`, `0x0010`).
- [x] Display Attribute List (`ATTR_TYPE_ATTRIBUTE_LIST`, `0x0020`), both Resident and Nonresident.
- [x] Detect File Name attributes (`ATTR_TYPE_FILE_NAME`, `0x0030`), which seem to be Resident only.
- [x] Display the file name stored in a File Name attribute.
- [ ] Display the data the `parent_ref_` field of a `struct AttributeFileNameEntry` links to.
- [x] Detect an Object ID attribute (`ATTR_TYPE_OBJECT_ID`, `0x0040`).
- [ ] Display the data contained in an Object ID attribute.

## In-memory Tree Data Structures

I need a way to represent the file system in memory. Perhaps I could use the actual vales for representing directory and file locations on disk, but keep them in arrays. Text editors solved the array problem a long time ago, so I could probably use some kind of buffer-gap structure to handle changes to the file system while keeping information as contiguous as possible.

In general, people recommend using a tree data structure where a folder is represented as a list, set or map of children. Each child can be a file or a folder. [One person on StackOverflow](http://stackoverflow.com/questions/13230439/efficient-data-structure-for-associating-data-with-filesystem-paths) recommended a [Patricia Trie](http://en.wikipedia.org/wiki/Radix_tree), also known as a Radix Tree, for it's use of memory. He/She also noted several options for implementing it, as memory consumption really depends on how you store the children of a given notde:

- look at the data as a sequence of binary digits, so you have at most 2 child nodes. It's easy to implement.
- maintain an array of 256 nodes. It's usually the most efficient way tof direct lookup, but also consumes the most memory and is slow if you need to iterate through all the children.
- store an array of pairs (`letter`, `child node`). This is probably the mot memory efficient, because it only stores the objects you actually care about, and it also has a good performance for iteratin through all children. However, you have to check all pairs for direct lookup - which is usually fine far from the root, but could be a problem near the root.
- store some kind of dictinalry inside each node that maps a letter to a child node. That's the most balanced with respect to performance - it gives you reasonably good speeds for operations and is somewhat memory efficient.
- if you  construct the whole collection up-front and then just query it, there is an approach for storing the child links based on [Tarjan tables]({{ site.url }}/assets/data structures/CS-TR-78-683.pdf) that will probably increase the construction time, but will save memory and query time later.

## NTFS MetaFiles

The metafiles are stored in the root directory ("`.`"). The shell hides them from the user, so they are less likely to be damaged. The files are:

- File 0: `$MFT`. The `$MFT` tells us where all the pieces of the actual Master File Table (MFT) are located. The MFT is part of the `$MFT` file. Also, the `$MFT` is contained within the MFT.
  - `$MFT` - a file in the Master File Table (MFT).
  - MFT - the table that contains all the file records.
- File 1: `$MFTMirr`. This file tells us the location of a backup of the first few files in the MFT. In data recovery situations, where the beginning of the MFT is damaged, this mirror can help save the day.
- File 2: `$LogFile`. This is a journal of the NTFS's metadata transactions. Like most metafiles, it is not human readable and not meant for use by the user. Corruption of this file can cause you not to be able to mount the file system. This can be easily fixed by simply resizing the file. These two commands can assist with that:
  - `chkdsk <drive:> /L` to find the current size of t `$LogFile`.
  - `chkdsk <drive:> /f /L:<new size>` to resize `$LogFile`.
- File 3: `$Volume`. This file keeps record of the NTFS version, volume information, and volume label.
- File 4: `$AttrDef`. The `$AttrDef` file defines the different attributes that the file system can have. Here is a list of the attribute types available.
  - `$STANDARD_INFORMATION       (0x0010)`
  - `$ATTRIBUTE_LIST             (0x0020)`
  - `$FILE_NAME                  (0x0030)`
  - `$VOLUME_VERSION             (0x0040)`, Windows NT only
  - `$OBJECT_ID                  (0x0040)`, Windows 2K and later
  - `$SECURITY_DESCRIPTOR        (0x0050)`
  - `$VOLUME_NAME                (0x0060)`
  - `$VOLUME_INFORMATION         (0x0070)`
  - `$DATA                       (0x0080)`
  - `$INDEX_ROOT                 (0x0090)`
  - `$INDEX_ALLOCATION           (0x00A0)`
  - `$BITMAP                     (0x00B0)`
  - `$SYMBOLIC_LINK              (0x00C0)`, Windows NT only
  - `$REPARSE_POINT              (0x00C0)`, Windows 2K and later
  - `$EA_INFORMATION             (0x00D0)`
  - `$LOGGED_UTILITY_STREAM      (0x0100)`
- File 5: `.`. The dot is the root directory for the volume. When you issue a `dir` command on `C:\`, you are looking at the root (`.`) directory.
- File 6: `$Bitmap`. This file keeps track of all the clusters of the volume and whether or not a cluster is currently in use.
- File 7: `$Boot`. This file contains the boot sector and the boot strap code (the first 16 sectors of the volume). The boot sector contains the location of the `$MFT` and `$MFTMirr`. The file starts in the MFT and points back to the beginning of the volume for its `$Data` attribute, which contains the boot strap code. It si the boot strap code that tells us what boot loader we are using (NTLDR for Windows XP/2003 and BOOTMGR for Vista/2008). Also the boot sector tells us the location of the MFT. This is part of how Windows is able to locate files during the early stages of bootup, before the NTFS.SYS driver actually loads.
- File 8: `$BadClus`. Keeps a record of the clusters on your volume that contain physically bad sectors. Windows marks them as bad so it doesn't try to use them. If you ever run `chkdsk` with a `/r` switch, then you are telling `cxhkdsk` to update `$BadClus` with any new bad sectors that are found.
- File 9: `$Secure`. Contains security information.
- File 10: `$UpCase`. Contains the casing table.
- File 11: `$Extend`. A directory that can house files used for optional extensions.

Microsoft reserves files 12-16 for additional files, so you won't see any normal files until file entry 17.

## Changes in the Latest Release of Windows 10

I noticed on Thursday, November 17th, the device IO control `IOCTL_STORAGE_QUERY_PROPERTY` with a storage property ID of `StorageAccessAlignmentProperty` fails with "`Error: 1, Incorrect function.`" for CD ROM devices. It succeeded on September 24th. Perhaps, the data was meaningless as there wasn't even a CD in the drive.

I also found that for USB drives, while `StorageAccessAlignmentProperty` succeeds, `PropertyStandardQuery` fails, also with "`Error: 1, Incorrect function.`"

## How to Find the Master File Table

The goal is to find and read the MFT on each device that can contain one. There is more than one way to find the physical drives on a host. The first process described below will find internal drives, but fails for drives attached to external buses, like USB. The only way I've found to enumerate drives attached to USB is to assume they each have a volume name already assigned, and to test each volume name to see if it maps to a drive.

The first thing we must do is get a list of appropriate devices on the host. Once we figure out which devices represent physical drives, we'll look at the disk geometry to determine the sector size. We can then find the Master Boot Record (MBR), which will lead us to the NTFS Partition Boot Sector. The Partition Boot Sector contains the NTFS BIOS Parameter Block (BPB) which describes the physical layout of the data the current partition. We will use the MFT Logical Cluster value and the size of a sector to locate the MFT.

- Call `SetupDiGetClassDevs` to get an HDEVINFO object. It is a handle to the set of devices presenting a disk interface that are also present on the system. Each device is indexed starting from zero.
- Call `SetupDiEnumDeviceInterfaces` providing a zero-based index to get an `SP_DEVICE_INTERFACE_DATA` object for each device in the set.
- For each `SP_DEVICE_INTERFACE_DATA` object, get a handle (`HANDLE`) to the physical device: Use the `HDEVINFO` handle and the `SP_DEVICE_INTERFACE_DATA` to get a handle to the physical device:
  - Call `SetupDiGetDeviceInterfaceDetail` to get an `SP_DEVICE_INTERFACE_DETAIL_DATA` object. It will have to be called twice. The first time to get the size of the buffer needed, and the second time to fill the buffer with the object.
  - Pass the `DevicePath` of the `SP_DEVICE_INTERFACE_DETAIL_DATA` object to `CreateFile` to get a `HANDLE` to the physical device.
  - Release the memory allocated for the `SP_DEVICE_INTERFACE_DETAIL_DATA`. It's no longer of interest.
  - Note: the device path will look something like "`\\?\ide#diskwdc_wd1001fals-00y6a0___________________05.01d05#4&11a28ece&0&0.0.0#{53f56307-b6bf-11d0-94f2-00a0c91efb8b}`".
- Pass `IOCTL_STORAGE_GET_DEVICE_NUMBER` to `DeviceIoControl` to retrieve a [STORAGE_DEVICE_NUMBER](https://msdn.microsoft.com/en-us/library/windows/desktop/bb968801(v=vs.85).aspx) object. It contains three fields: `DeviceType`, `DeviceNumber` and `PartitionNumber`. The value of `DeviceNumber` can be appended to the string "`\\.\PhysicalDrive`" to create a path to the physical drive.
- Get a HANDLE to the physical drive:
  - Create a path to the physical drive by appending the `deviceNumber` to "`\\.\PhysicalDrive`"
  - Pass the path to the physical drive to `CreateFile` to get the handle.
- Get the sector size
  - DISK_GEOMETRY_EX: Pass the handle to the physical disk and I/O control `IOCTL_DISK_GET_DRIVE_GEOMETRY_EX` to `DeviceIoControl`.
    - NOTE: `DISK_GEOMETRY_EX` gets the logical sector size, but not the physical sector size. This may be important.
  - `STORAGE_ACCESS_ALIGNMENT_DESCRIPTOR`: Pass the handle for the physical disk, I/O control `IOCTL_STORAGE_QUERY_PROPERTY` and a `STORAGE_QUERY_PROPERTY` (with its `PropertyId` field set to `StorageAccessAlignmentProperty`, and `QueryType` set to `PropertyStandardQuery`) to `DeviceIoControl` to get the `STORAGE_ACCESS_ALIGNMENT_DESCRIPTOR`.
    - NOTE: This structure reports both the logical and physical sector sizes. However, `DeviceIoControl` fails with error `ERROR_INVALID_FUNCTION` (1) for USB connected external drives.
  - Calling `GetDiskFreeSpace` looked promising, because it returns a value for bytes per sector. Alas, it is the logical sector size regardless of whether the disk is internal or external.
  - It seems the only way to do this and get close results is to first try to get a `STORAGE_ACCESS_ALIGNMENT_DESCRIPTOR` and fall back to `DISK_GEOMETRY_EX` if that fails.
- `MBRModern`: Read the MBR from disk using the `HANDLE` to the physical disk, the size of a sector and, if the STORAGE_ACCESS_ALIGNMENT_DESCRIPTOR was obtain, the offset into the sector (for large sectors) where the first sector is located.
- Get the location of a partition from the MBR (the first one should be valid): `MBRModern->pe1`.
- Read the NTFS Partition Boot Sector using `Partition.dwRelativeSector` as the relative offset to the appropriate sector. Call `SetFilePointerEx()` before calling `ReadFile` to advance the file pointer to the correct location on disk. Note that the NTFS Boot Sector contains a structure called the NTFS BPB. The BPB is the BIOS Parameter Block. [Wikipedia says](https://en.wikipedia.org/wiki/BIOS_parameter_block) it is a data structure in the volume/partition boot record describing the physical layout of a data storage volume. On partitioned devices, such as hard disks, the BPB describes the volume partition. On devices that are not partitioned, such as floppy disks, it describes the entire medium.
- Use the MFT Logical Cluster value and the size of a sector to locate the MFT.

Those were my original list of steps. Let's try again to make it more clear.

We can enumerate all of the physical disks on the host, this way:

1. Enumerate the physical disks
   1. Get a handle (`HDEVINFO`) to the device information set for disks that are present.
   1. Use the handle to get interface data (`SP_DEVICE_INTERFACE_DETAIL_DATA`) for each disk.
      It contains a path to the physical disk.
1. Get the device. Note that `DiskClassGuid` is declared in `winioctl.h`

```cpp
diskClassDevices = ::SetupDiGetClassDevs(&DiskClassGuid,
                                         NULL,
                                         NULL,
                                         DIGCF_PRESENT | DIGCF_DEVICEINTERFACE);
if (INVALID_HANDLE_VALUE != diskClassDevices)
{
    // We're good to go.
    SP_DEVICE_INTERFACE_DATA deviceInterfaceData = {};
    uint32                   deviceIndex = 0;

    deviceInterfaceData.cbSize = sizeof deviceInterfaceData;
    while (::SetupDiEnumDeviceInterfaces(diskClassDevices,
                                         NULL,
                                         &DiskClassGuid,
                                         deviceIndex++,
                                         &deviceInterfaceData))
    {
        // For each device get the details from the interface data.
```

Next we need to get a handle to the physical disk device. We have to call `SetupDiGetDeviceInterfaceDetail`, but we don't know the size of the buffer we need to hold the data. In typical `Win32` fashion, we call the API twice; once with a null pointer to the buffer to get the buffer size, and again with a newly allocated buffer:

```cpp
// Determine how much memory space is required
::SetupDiGetDeviceInterfaceDetail(diskClassDevices,
                                  interfaceData,
                                  NULL,
                                  0,
                                  &requiredSize,
                                  NULL);
st = GetLastError();
if (ERROR_INSUFFICIENT_BUFFER == st)
{
    STORAGE_DEVICE_NUMBER deviceNumber = {};
    deviceInterfaceDetail = reinterpret_cast<PSP_DEVICE_INTERFACE_DETAIL_DATA>(new uint8[requiredSize]);
    if (deviceInterfaceDetail)
    {
        // Note that cbSize MUST be the size of the data structure, not the buffer.
        deviceInterfaceDetail->cbSize = sizeof SP_DEVICE_INTERFACE_DETAIL_DATA;
        bool32 success = ::SetupDiGetDeviceInterfaceDetail(diskClassDevices,
                                                           interfaceData,
                                                           deviceInterfaceDetail,
                                                           requiredSize,
                                                           NULL,
                                                           NULL);
        if (success)
        {
            // We now need to call CreateFile to open a handle to the device.  The DevicePath field of
            // deviceInterfaceDetailData has the path to pass to CreateFile. That handle will then be
            // passed to DeviceIoControl with the IOCTL_STORAGE_GET_DEVICE_NUMBER I/O control code to
            // get the STORAGE_DEVICE_NUMBER record, which contains the DeviceType, DeviceNumber and
            // PartitionNumber for the disk. Finally, the DeviceNumber can be appended to
            // "\\.\PhysicalDrive" to get the physical drive path/name.
            result = CreateFile(deviceInterfaceDetail->DevicePath,
                                GENERIC_READ | GENERIC_WRITE,       // Just read data from the disk
                                FILE_SHARE_READ | FILE_SHARE_WRITE,    // share
                                0,                  // security attributes
                                OPEN_EXISTING,      // Yes, it exists.
                                //FILE_ATTRIBUTE_NORMAL,
                                0,                  // dwFlagsAndAttributes
                                0);                 // unused template handle
```

We need to get a handle to the physical drive (which is NOT the same has a handle to the physical device). The path will look like "`\\.\PhysicalDriveX`", where `X` is the device number. To get the device number call `DeviceIoControl` and pass in the handle to the _device_ and the I/O control code `IOCTL_STORAGE_GET_DEVICE_NUMBER`. This will return a `STORAGE_DEVICE_NUMBER` structure:

```c
typedef struct _STORAGE_DEVICE_NUMBER {
  DEVICE_TYPE DeviceType;
  ULONG       DeviceNumber;
  ULONG       PartitionNumber;
} STORAGE_DEVICE_NUMBER, *PSTORAGE_DEVICE_NUMBER;
```

In the code below, the value of `physicalDevice` is the handle returned from `CreateFile`, above.

```cpp
    HANDLE physicalDevice;
    uint32 result;
    STORAGE_DEVICE_NUMBER deviceNumber = {};
    bool32 success;
    DWORD bytesReturned;
    uint32 result = ERROR_SUCCESS;

    /*
      IMPORTANT: The values in the STORAGE_DEVICE_NUMBER structure are guaranteed to
      remain unchanged until the device is removed or the system is restarted.  They are
      not guaranteed to be persistent across device or system restarts.
    */
    success = DeviceIoControl(physicalDevice,
                              IOCTL_STORAGE_GET_DEVICE_NUMBER,
                              0,
                              0,
                              &deviceNumber,
                              sizeof deviceNumber,
                              &bytesReturned,
                              0);
    if (success)
    {
        // NOTE: If DeviceType == FILE_DEVICE_DISK (7), then it's a disk device.
        // NOTE: The DeviceNumber field is the index of the physical drive.
        // NOTE: If PartitionNumber is -1, then the device cannot be partitioned.
        // Otherwise, it is the partition number of the device. Zero is a valid partition number.
        result = deviceNumber.DeviceNumber;
```

## References

- Threads
  - [Avoiding and Identifying False Sharing Among Threads](https://software.intel.com/en-us/articles/avoiding-and-identifying-false-sharing-among-threads)
  - [Avoiding and Identifying False Sharing Among Threads (PDF)]({{ site.url }}/assets/Threads/3-4-MemMgt_-_Avoiding_and_Identifying_False_Sharing_Among_Threads.pdf)
  - [How to implement zero-copy tcp using lock-free ciruclar buffer in C++](http://stackoverflow.com/questions/11295474/how-to-implement-zero-copy-tcp-using-lock-free-circular-buffer-c)
  - [Effective Concurrency: Eliminate False Sharing](https://herbsutter.com/2009/05/15/effective-concurrency-eliminate-false-sharing/)
  - [Eliminate False Sharing](http://www.drdobbs.com/parallel/eliminate-false-sharing/217500206)
- File Systems
  - [Basic External Memory Data Structures]({{ site.url }}/assets/data structures/external.pdf)
  - [Algorithms and Data Structures for Flash Memories]({{ site.url }}/assets/data structures/10.1.1.66.2145.pdf)
  - [NTFS Docs]({{ site.url }}/assets/NTFS/ntfsdoc.pdf)
  - [NTFS Documentation](http://inform.pucp.edu.pe/~inf232/Ntfs/ntfs_doc_v0.5/index.html) that is part of the Linux-NTFS Project.
  - [pyMFTGrabber](https://github.com/jeffbryner/pyMFTGrabber) is tool to extract `$MFT` from a volume. It is written in Python 2, but fails due to an integer overflow. Apparently Python 2 requires python integers to be mapped to C long (which is only 32-bits). `pyMFTGrabber` might work if it was ported to Python 3, but it has issues with the Py2 module '`StringIO`' being replace with the Py3 '`io`' module. It creates _huge_ files (before it failed with the overflow error, it created a file over 800MB).
  - [analyzeMFT](https://github.com/dkovar/analyzeMFT) is a Python 2 program that can read a file that has been created by a tool to extract the `$MFT` from a volume and convert it to a CSV text file. This tool also needs to be converted to Python 3. I think only the `print` statements need to be converted to `print` function calls. Even so, I'll need to find an editor that can open very large files. Update: Apparently notepadd++ can do this (at least for a text file - it did not work on the original binary file generated by `pyMFTGrabber`)!
  - [NTFS Metafiles](https://blogs.technet.microsoft.com/askcore/2009/12/30/ntfs-metafiles/)
  - [The Four Stages of NTFS File Growth](https://blogs.technet.microsoft.com/askcore/2009/10/16/the-four-stages-of-ntfs-file-growth/)
  - [The Four Stages of NTFS File Growth, Part 2](https://blogs.technet.microsoft.com/askcore/2015/03/12/the-four-stages-of-ntfs-file-growth-part-2/)
  - [The Promise of Advanced Format Hard Drives](http://windowsitpro.com/windows/promise-advanced-format-hard-drives) is about sector sizes, how 4K sector drives can emulate 512-byte sector drives, and how drives whose sector sizes are 512-bytes can still be formatted with 4K sectors in Windows NTFS.
  - [ntfs_layout.h]({{ site.url }}/assets/NTFS/ntfs_layout.h.html)

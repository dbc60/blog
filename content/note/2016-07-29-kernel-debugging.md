---
layout: page
title: Kernel Debugging
tags:
  - kernel
  - debugging
  - windbg
excerpt: Using windbg to debug kernel drivers, such as the FIM mini filter.
---

## Contents
{:.no_toc}

* TOC
{:toc}

## Document History

| Date | Author | Summary of Changes |
|-----------:|-------------:|:------------|
| 2016.07.29 | Douglas Cuthbertson | Initial draft |

## Running Windbg against VM2
See [Setting Up Kernel-Mode Debugging over a Network Cable](https://msdn.microsoft.com/en-us/library/windows/hardware/hh439346%28v=vs.85%29.aspx?f=255&MSPPError=-2147217396) for details.

First, make sure you can ping the IP address of the host computer from the target computer. Next, on the target computer, run `bcdedit /debug on` and `bcdedit /dbgsettings net hostip:w.x.y.z port:n`. For example, if the host computer's IP address is `192.168.1.137`:

```terminal
> bcdedit /debug on
> bcdedit /dbgsettings net hostip:192.168.1.137 port:50500
```

2017.03.20:

- IP: 192.168.0.58
- key: 2e66e0ucoz48s.1dmf6gmay7xk9.3b96yqmcnd39s.1w0h1ju7m4tot

The command will print out a key, such as `3nhs6jf46pi4k.370rq4gpgkfxf.1wjvy2fkm4mzf.wfrfsr0t7o3a`. This will make it possible for `windbg` running on the host computer to connect.

On the host computer, launch `windbg` with the same port number and key:

```terminal
windbg -k net:port=50500,key=xjduq2ysrb0k.2utttn53q7ngn.24b65jduczrip.1cdkiyd8fely2
```

You might also want to turn on testsigning to test/debug the minifilter: run `bcdedit /set TESTSIGNING ON`

## WinDBG Commands

### Initial Analysis
These commands typically give you an overview of what happened so you can dig further. In the dase dealing withlibraries, where you don't have source, sending the ersulting log file to the vendor along with the build number of the binary library should be sufficient for them to trace it to a known issue if there is one.

- `!analyze -v`
- `.logopen <filename>`: (see also .logappend)
- `.logclose`: close the log file
- `.lastevent`: See why the process halted and on what thread
- `u`: List of disassembly near $eip on offending thread
- `~`: Status of all threads
- `kb`: List the call stack, including parameters
- [lm](http://msdn.microsoft.com/en-us/library/windows/hardware/ff552026(v=vs.85).aspx): list loaded modules.
- `!locks [Options] [Address]`: [!locks (!kdext*.locks)](http://msdn.microsoft.com/en-us/library/windows/hardware/ff563980(v=vs.85).aspx): The locks extension in Kdextx86.dll and kdexts.dll displays information about kernel ERESOURCE locks. Use `!kdext2.help` to get help on the `!locks` command!
- [!memusage](http://msdn.microsoft.com/en-us/library/windows/hardware/ff564043(v=vs.85).aspx): display summary statistics about physical memory use.
- [!vm](http://msdn.microsoft.com/en-us/library/windows/hardware/ff565602(v=vs.85).aspx): display summary information about virtual memory use.
- [!errlog](http://msdn.microsoft.com/en-us/library/windows/hardware/ff562994(v=vs.85).aspx): display the contents of any pending entries in the I/O system's error log.
- [!process /Process/ /Flags/](http://msdn.microsoft.com/en-us/library/windows/hardware/ff564717(v=vs.85).aspx): display information about all the processes with some flags:
  - `0x1`: Time and priority statistics
  - `0x2`: Display a list of threads and events associated with the process, and their wait states.
  - `0x4`: A list of threads threads associated with a process. If this is included without 0x2, each thread is displayed on a single line. If this is included along with 0x2, each thread is displayed with a stack trace.
  - `0x8`: Display the return address, the stack pointer and (on Itanium-based systems) the bsp register value for each function. The display of function arguments is suppressed.
  - `0x10`: Set the process context equal to the specified process for the duration of this command. This results in a more accurate display of thread stacks. Because this flag is equavalent to using [.process /p /r (set process context)](http://msdn.microsoft.com/en-us/library/windows/hardware/ff564723(v=vs.85).aspx) for the specified process, any existing user-mode module list will be discarded. If *Process* is zero, the debugger displays all processes, and the process context is changed for each one. If you are only displaying a sigle process and its user-mode state has already been refreshed (for example, with `.process /p /r`), it is not necessary to use this flag. This flag is only effective when used with `0x1`.
- [!stacks](http://msdn.microsoft.com/en-us/library/windows/hardware/ff565379(v=vs.85).aspx): display information about the kernel stacks. Followed by 0 (zero), it displays a summary. 1 displays stacks that are currently paged out, as well as the current kernel stacks. 2 displays the full parameters for all stacks as well as stacks that are currently paged out and the current kernel stacks. Use ~!stacks 2 parity~ to find the interesting stacks for the parity driver.
- [!thread <Address <Flags> >](http://msdn.microsoft.com/en-us/library/windows/hardware/ff565440(v=vs.85).aspx): Display summary information about a thread, including EBLOCK information.
- `!fltkd.help`: list the commands for the Filter Manager Debugging Extensions.
  - Note that `[detail]` specifies the level of detail to show. It can be either 0 or 1, and the default is 0.
  - The `[flags]` option controls what information is displayed. The default is 0, so minimal information is displayed.
  - `cbd [addr] [flags] [detail]`
    - dump `IRP_CRTL` or `CALLBACK_DATA`
    - `[flags]` specify what information to dump. Use 0x00000001 for extended detail on each completion stack.
  - `irpctrl [addr] [flags] [detail]`: seems to be the same as `cbd`
  - `contextlist [addr] [detail]`: dump `CONTEXT_LIST_CTRL`
  - `ctx [addr] [detail]`: dump `CONTEXT_NODE`
  - `fileList [addr] [flags] [detail]`: dump `FILE_LIST_CTRL` given `fileObject` or `FileList` address. Set flags to 0x1 to dump the file list cotrl's file context info.
  - `filter [addr] [flags] [detail]`: dump `FLT_FILTER` where `[flags]` specifies what information to dump:
    - `0x0001`: basic filter information
    - `0x0002`: filter's context registration information
    - `0x0004`: filter's context usage information
    - `0x0008`: filter's object usage/reference information
    - `0x0010`: filter's verifier information
    - `0x0020`: filter's port information
  - `filters [flags] [detail]`: dumps all the filters registered in the system
  - `fltobj [addr] [detail]`
  - `frame [addr] [flags] [detail]`
  - `frames [flags] [detail]`
  - `instance [addr] [flags] [detail]`
  - `msgq [addr] [flags] [detail]`
  - `namecachelist [addr] [detail]`
  - `oplock [addr] [flags]`
  - `port [addr]`
  - `portlist [filter object addr] [flags] [detail]`
  - `relobjs [addr]`
  - `tree [addr] [detail]`
  - `streamList [addr] [flags] [detail]`
  - `traceflags [flags]`: Sets trace flags. Displays current setting if not supplied.
  - `tracelevel [level]`: Sets trace level. Displays current setting if not supplied.
  - `volume [addr] [flags] [detail]`
  - `volumes [flags] [detail]`: Dumps all the volumes to which the filter manager is attached.
  - `work [flags] [detail]`: Dump Throttled worker queue information
  - `stats`: Dumps statistics

## Setting Breakpoints

- `bl`: list all breakpoints
- `bu`: set an unresolved breakpoint (`bu MyModule!MyFunction`)
- `bc`: clear a breakpoint, or clear all breakpoints
    - `bc 2` will clear breakpoint 2
    - `bc *` will clear all of the breakpoints

## Displaying Objects
Here are a couple of examples of how to use the `dx` command to view memory as a C or C++ object.

```terminal
kd> dx (*(ThreatStackFIM!FIM_RULE *)(0xffffe001`9b3e3948))
(*(ThreatStackFIM!FIM_RULE *)(0xffffe001`9b3e3948))                 [Type: FIM_RULE]
    [+0x000] RuleId           : {2C6D89AB-C2F9-11E6-8B3B-55553F93DC1E} [Type: _GUID]
    [+0x010] Enabled          : 0x1 [Type: unsigned long]
    [+0x014] Events           : 0x0 [Type: unsigned long]
    [+0x018] Size             : 0x5b0 [Type: unsigned long]
    [+0x01c] ExclusionPathCount : 0x1 [Type: unsigned short]
    [+0x01e] InclusionPathCount : 0xd [Type: unsigned short]
    [+0x020] ExclusionSize    : 0x6c [Type: unsigned long]
    [+0x024] InclusionSize    : 0x51c [Type: unsigned long]
    [+0x028] Paths            [Type: _FIM_PATH [1]]
```

```terminal
kd> dx (*(ThreatStackFIM!FIM_RULE *)(0xffffe001`9b3e3948 + 0x5b0))
(*(ThreatStackFIM!FIM_RULE *)(0xffffe001`9b3e3948 + 0x5b0))                 [Type: FIM_RULE]
    [+0x000] RuleId           : {FD274E95-C600-11E6-A896-2D11D9E5A7A6} [Type: _GUID]
    [+0x010] Enabled          : 0x1 [Type: unsigned long]
    [+0x014] Events           : 0x0 [Type: unsigned long]
    [+0x018] Size             : 0x100 [Type: unsigned long]
    [+0x01c] ExclusionPathCount : 0x0 [Type: unsigned short]
    [+0x01e] InclusionPathCount : 0x2 [Type: unsigned short]
    [+0x020] ExclusionSize    : 0x0 [Type: unsigned long]
    [+0x024] InclusionSize    : 0xd8 [Type: unsigned long]
    [+0x028] Paths            [Type: _FIM_PATH [1]]
```


## Symbol Search Path
If you're local to both t2 and the engineering server, then use the following symbol path:

```sh
SRV*\\t2\bitbucket\symbols*http://msdl.microsoft.com/download/symbols;
SRV*\\eng-file-server\builds\symbols;
SRV*\\eng-file-server\releases\symbols;
```

If you're remote, then create a directory, like C:\LocalSymbols, to cache the symbols you'll need for debugging and use the following symbol path:

```sh
SRV*C:\LocalSymbols*http://msdl.microsoft.com/download/symbols;
SRV* C:\LocalSymbols*\\eng-file-server\builds\symbols;
SRV* C:\LocalSymbols*\\eng-file-server\releases\symbols;
```

As of [2015-05-08 Fri]:

```sh
SRV*\\t2\bitbucket\symbols*http://msdl.microsoft.com/download/symbols;
SRV*\\eng-file-server\builds\symbols;
SRV*\\eng-file-server\releases\symbols;
SRV*\\t2\bitbucket\symbols*http://msdl.microsoft.com/download/symbols;
E:\LocalSymbols;
cache*E:\SymbolCache;srv*http://msdl.microsoft.com/download/symbols;
\\t2\bitbucket\symbols;
\\eng-file-server\releases\symbols
```

## Source Search Path
Place the following path in Windbg's source search path:

```sh
SRV*\\t2\bitbucket\source
```

## Workspace
Remember to save these values (both the source and symbol search paths) in a workspace for future use. Select ~File > Save Workspace As...~. When prompted, proved a name for the workspace, like Bit9. On any subsequent run of Windbg, the workspace can be loaded by selecting ~File > Open Workspace...~ and entering the appropriate name when prompted.

## Evaluate C++ Expression
Use the ~??~ command. For example, =?? Parity!g_ParityFilterInterfaces= returns:

```sh
3: kd> ?? Parity!g_ParityFilterInterfaces
struct ParityFilterInterfaces
   +0x000 m_pMiniFilter    : 0xf73185a8 MiniFilter
   +0x004 m_pRegistryHook  : 0xf73189a0 RegistryHook
   +0x008 m_pObjectHook    : 0xf7318c98 ObjectHook
   +0x00c m_pConfigProps   : 0xf7318de0 ConfigProps
   +0x010 m_pABCache       : 0xf7318fc8 ABCache
   +0x014 m_pRuleEngine    : 0xf7319020 RuleEngine
   +0x018 m_pProcessTracking : 0xf7319730 ProcessTracking
   +0x01c m_pDirtyTracking : 0xf73197f0 DirtyTracking
   +0x020 m_pNormalization : 0xf7319a00 Normalization
   +0x024 m_pDeviceTracking : 0xf7319be8 DeviceTracking
   +0x028 m_pWatchdogServices : 0xf7319ca0 WatchdogServices
   +0x02c m_pControl       : 0xf7318430 Control
```

In that simple example, ~??~ produces the same results as the ~dt~ command:

```sh
3: kd> dt Parity!g_ParityFilterInterfaces
   +0x000 m_pMiniFilter    : 0xf73185a8 MiniFilter
   +0x004 m_pRegistryHook  : 0xf73189a0 RegistryHook
   +0x008 m_pObjectHook    : 0xf7318c98 ObjectHook
   +0x00c m_pConfigProps   : 0xf7318de0 ConfigProps
   +0x010 m_pABCache       : 0xf7318fc8 ABCache
   +0x014 m_pRuleEngine    : 0xf7319020 RuleEngine
   +0x018 m_pProcessTracking : 0xf7319730 ProcessTracking
   +0x01c m_pDirtyTracking : 0xf73197f0 DirtyTracking
   +0x020 m_pNormalization : 0xf7319a00 Normalization
   +0x024 m_pDeviceTracking : 0xf7319be8 DeviceTracking
   +0x028 m_pWatchdogServices : 0xf7319ca0 WatchdogServices
   +0x02c m_pControl       : 0xf7318430 Control
```

### Parity Configuration properties

```sh
3: kd> ?? Parity!g_ParityFilterInterfaces.m_pConfigProps
class ConfigProps * 0xf7318de0
   +0x000 __VFN_table : 0xf730bde8 
   +0x004 m_bVerbose       : 0
   +0x008 m_PoolTag        : 0x70673942
   +0x00c m_ReferenceCount : 0n0
   +0x010 m_MarkedForDeletion : 0
   +0x014 m_Initialized    : 1
   +0x015 m_Running        : 1
   +0x016 m_Connected      : 1
   +0x017 m_Enabled        : 1
   +0x018 m_ShutdownFailure : 0
   +0x01c m_Name           : 0xf730a7a0  "ConfigProps"
   +0x020 m_PoolType       : 1 ( PagedPool )
   +0x024 m_PoolTag        : 0x70673942
   +0x028 m_ProcessExclusions : 0
   +0x02c m_ExecuteExclusions : 0xffffffff
   +0x030 m_Flags          : 0
   +0x034 m_Seccon         : 14 ( DAS_SECCON_20 )
   +0x038 m_DisconnectedSecCon : 14 ( DAS_SECCON_20 )
   +0x03c m_bRunningButDisabled : 0
   +0x040 m_DefaultMediaType : 1 ( MEDIA_TYPE_FIXED )
   +0x044 m_Platform       : 0x5020200
   +0x048 m_BuildPlatform  : 0x5020100
   +0x04c m_BuildPlatformString : 0xf72ffba0  "Platform: Windows Server 2003 x86 Release"
   +0x050 m_BlockAndAskTimeoutMs : 0x1b7740
   +0x054 m_ABCacheMissLocalMs : 0x7530
   +0x058 m_ABCacheMissNetworkMs : 0xea60
   +0x05c m_MaxParityAnalysisStallMs : 0x61a8
   +0x060 m_MaxStartupDelayMs : 0xea60
   +0x064 m_MinNormalizationLocalStack : 0x2000
   +0x068 m_MinNormalizationNetworkStack : 0
   +0x06c m_MaxReparseAttempts : 5
   +0x070 m_ConnectWaitTimeMs : 0x1388
   +0x074 m_DirtyNotifyDelayMs : 0x64
   +0x078 m_FileOpDebounceTriggerCount : 0
   +0x07c m_FileOpDebounceMsSinceLastTrigger : 0x7530
   +0x080 m_RegOpDebounceTriggerCount : 0
   +0x084 m_RegOpDebounceMsSinceLastTrigger : 0
   +0x088 m_ObjectOpDebounceTriggerCount : 0
   +0x08c m_ObjectOpDebounceMsSinceLastTrigger : 0
   +0x090 m_bShouldAllowInMonitor : 0
   +0x094 m_VersionInfo    : VersionInfo
   +0x0e4 m_ProcessStartedCreateMs : 0x7530
   +0x0e8 m_ProcessLastImageLoadMs : 0x2710
   +0x0ec m_ProcessFirstImageLoadMs : 0x1f4
   +0x0f0 m_DeadlockTimeoutMs : 0x3a98
   +0x0f4 m_DepPolicy      : 2
   +0x0f8 m_DepSupported   : 0
   +0x0fc m_PreviousModeOffset : 0
   +0x100 m_WatchdogIntervalMs : 0x800
   +0x104 m_WindowsUpdateServicePid : 0xa54
   =f72b6000 MaximumKernelStack : 0x905a4d
   +0x108 m_PropertyLock   : PushLock
   +0x114 m_VerbosePattern : UnicodeString
   +0x11c m_StartupDelayPattern : UnicodeString
   +0x124 m_ReadExcludePattern : UnicodeString
   +0x12c m_WriteExcludePattern : UnicodeString
   +0x134 m_ProcessExcludePattern : UnicodeString
   +0x13c m_ProcessExcludePattern2 : UnicodeString
   +0x144 m_ParityBinDirectory : UnicodeString
   +0x14c m_ParityDataDirectory : UnicodeString
   +0x154 m_ProgramFilesDirectory : UnicodeString
   +0x15c m_Bit9ProgramDataDirectory : UnicodeString
   +0x164 m_Bit9ProgramFilesDirectory : UnicodeString
   +0x16c m_bHaveEverConnected : 1
   +0x170 m_OldBuildNumber : 0x30040124
   +0x174 m_BuildNumber    : 0x30040124
   =f72b6000 s_RuleClassesAllowedWhenDisconnected : 0x905a4d
   +0x178 m_CounterThresholdLock : PushLock
   +0x188 m_CounterThresholds : List
   +0x1d8 m_ConnectedRuleClassFlags : 2
   +0x1dc m_DisconnectedRuleClassFlags : 6
   +0x1e0 m_bDefaultPoliciesEnabled : 0
   =f730f110 s_ConfigProps    : [0] KERNEL_CONFIG_PROP
```

### Parity Driver Version Information

```sh
3: kd> ?? Parity!g_ParityFilterInterfaces.m_pConfigProps->m_VersionInfo
struct VersionInfo
   +0x000 major            : 0n6
   +0x002 minor            : 0n0
   +0x004 point            : 0n2
   +0x008 build            : 0n292
   +0x00c date             : [64]  "Sep  7 2011 18:13:15"
   +0x04c debug            : 0
```

## Commands

- `.ignore_missing_pages`: Suppress Missing Page Errors. It can be followed by a zero or one. Without an argument it will display the present state of this setting.
  - `.ignore_missing_pages 0`: Displays all missing page errors while debugging a Kernel Memory Dump. This is the default behavoir of the debugger.
  - `.ignore_missing_pages 1`: Suppresses the display of missing page errors while debugging a Kernel Memory Dump.
- `d*`: [display memory](https://msdn.microsoft.com/en-us/library/windows/hardware/ff542790(v=vs.85).aspx) - display the contents of memory in the given range
  - `d`: This displays data in the same format as the most recent d* command. If no previous d* command has been issued, d has the same effect as db.
  - ASCII characters. Up to 48 characters.
  - `db`: Byte values and ASCIII characters.
  - `dc`: Double-word values (4 bytes) and ASCII characters
  - `dd`: Double-word values (4 bytes)
    - `dds`: DWORD values and symbols
  - `dD`: Double-precision floating-point numbers (8 bytes)
  - `df`: Single-precision floating-point numbers (4 bytes)
  - `dp`: Point-sized values. This command is equavalent to dd or dq, depending on whether the target computer's processor architecture is 32-bit or 64-bit, respectively. The default count is 32 DWORDS or 16 quad-words.
    - `dpp`: similar to ~dps~, below. It's useful for looking up C++ objects with vtables on the stack (in case the debugger cannot find locals or parameters automatically, which is common in optimized builds).
    - `dps`: [Pointer-size values and symbols](http://blogs.msdn.com/b/doronh/archive/2006/03/28/563557.aspx). It can be used to dump a:
      - vtable
      - jump table
      - call stack
  - `dq`: Quad-word values.
  - `dt`: displays information about a local variable, global variable or data type.
  - `du`: Unicode characters.
  - `dw`: Word values (2 bytes)
  - `dW` (Word values (2 bytes) and ASCII characters.
  - `dyb`: Binary values and byte values.
  - `dyd`: Binary values and double-word values (4 bytes)
- `.ecxr` tells the debugger to switch the current context to the one stored in the crash dump's exception information. After we have executed ~.ecxr~, we can reliable access to the call stack and the values of local variables at the moment when the exception was raised.
- `!for_each_frame dv /t` displays the values of function parameters and local variables for every function on the call stack.
- `~*kL 20` - look at the stack of all the threads to find what the majority of the threads are doing.
  - `~*` lists all threads
  - `k L 20` displays the stack frame, where "L" means omit source lines, and "20" is the number of stack frames to display.
- These commands are useful when taskmgr is used to snap a dump on a [32-bit process running on a 64-bit host](http://stackoverflow.com/questions/8168098/unable-to-read-crash-dump-in-windbg):
  - `.load wow64exts`
  - `.effmach x86`

### Using dt Recursively
The `dt` command can recursivly display the subtype fields of a struct or class:

```conf
3: kd> dt Parity!g_ParityFilterInterfaces -r2
   +0x000 m_pMiniFilter    : 0xf73185a8 MiniFilter
      +0x000 __VFN_table : 0xf730c59c 
      +0x004 m_bVerbose       : 0
      +0x008 m_PoolTag        : 0x6c663942
      +0x00c m_ReferenceCount : 0n0
      +0x010 m_MarkedForDeletion : 0
      +0x014 m_Initialized    : 1
      +0x015 m_Running        : 1
      +0x016 m_Connected      : 1
      +0x017 m_Enabled        : 1
      +0x018 m_ShutdownFailure : 0
      +0x01c m_Name           : 0xf730a744  "MiniFilter"
      +0x020 m_PoolType       : 1 ( PagedPool )
      +0x024 m_PoolTag        : 0x6c663942
      =f7319d94 s_FilterHandle   : 0x8ae7ebb0 _FLT_FILTER
      =f7319d98 s_ParityProcessId : 0x000008ac Void
      =f7319d9c s_AgentProtocolVersion : 0n1
      =f7319da0 s_UserModeReady  : 1
      =f7319da1 s_HaveEnabledState : 1
      +0x028 m_AgentPort      : 0xe1a7c668 AgentPort
         +0x000 __VFN_table : 0xf730b2bc 
         +0x008 m_SelfReference  : 0xe1a7c668 Void
         +0x00c m_ClientPort     : 0x80002064 _FLT_PORT
         +0x010 m_ServerPort     : 0x800000ec _FLT_PORT
         +0x014 m_MaxConnections : 0n1
         +0x018 m_PortName       : UnicodeString
         +0x020 m_MessageNumber  : 0n1557
         +0x028 m_PostMessageList : _LIST_ENTRY [ 0xe1a7c690 - 0xe1a7c690 ]
         +0x030 m_PostMessageListLock : Mutex
         +0x03c m_PostMessageWorker : 0x800051f8 Void
         +0x040 m_PostMessageEvent : 0x8af240d8 _KEVENT
         +0x044 m_Terminate      : 0
         +0x048 m_MessageTime    : PeakCounter
         +0x080 m_MessageRetries : PeakCounter
         +0x0b8 m_MessageBytesSentTotal : PeakCounter
         +0x0f0 m_MessageBytesSentVariable : PeakCounter
         +0x128 m_MessageBytesReceived : PeakCounter
         +0x160 m_MessageCounts  : [38] Counter
      +0x02c m_CliPort        : 0xe199ad28 CLIPort
         +0x000 __VFN_table : 0xf730b410 
         +0x008 m_SelfReference  : 0xe199ad28 Void
         +0x00c m_ClientPort     : (null) 
         +0x010 m_ServerPort     : 0x800000e8 _FLT_PORT
         +0x014 m_MaxConnections : 0n1
         +0x018 m_PortName       : UnicodeString
         +0x020 m_MessageNumber  : 0n0
         +0x028 m_PostMessageList : _LIST_ENTRY [ 0xe199ad50 - 0xe199ad50 ]
         +0x030 m_PostMessageListLock : Mutex
         +0x03c m_PostMessageWorker : (null) 
         +0x040 m_PostMessageEvent : 0x8aed9b38 _KEVENT
         +0x044 m_Terminate      : 0
         +0x048 m_MessageTime    : PeakCounter
         +0x080 m_MessageRetries : PeakCounter
         +0x0b8 m_MessageBytesSentTotal : PeakCounter
         +0x0f0 m_MessageBytesSentVariable : PeakCounter
         +0x128 m_MessageBytesReceived : PeakCounter
      +0x030 m_RunningTime    : Timestamp
         +0x000 __VFN_table : 0xf730b028 
         +0x008 m_StartTicks     : _LARGE_INTEGER 0x219
         +0x010 m_TimestampType  : 2 ( TimestampTypeTickCount )
      +0x048 m_ConnectedTime  : Timestamp
         +0x000 __VFN_table : 0xf730b028 
         +0x008 m_StartTicks     : _LARGE_INTEGER 0x257e
         +0x010 m_TimestampType  : 2 ( TimestampTypeTickCount )
      +0x060 m_TotalConnectedTime : Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
      +0x078 m_AnalysisStallTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0xffffffff`ffffffff
         +0x020 m_MaxValue       : 0
         +0x028 m_Total          : 0
         +0x030 m_Count          : 0
      +0x0b0 m_AnalysisStallTimeouts : Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
      +0x0c8 m_AcquireForSectionSynchronizationPreOpTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0x19a08
         +0x028 m_Total          : 0x137a8a
         +0x030 m_Count          : 0x521a8
      +0x100 m_CreatePreOpTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0x8b67
         +0x028 m_Total          : 0x2e427
         +0x030 m_Count          : 0x34f39d
      +0x138 m_CreatePostOpTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0x4575
         +0x028 m_Total          : 0x38aa8
         +0x030 m_Count          : 0x34f397
      +0x170 m_SetInfoPreOpTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0x9ec0
         +0x028 m_Total          : 0x46a90
         +0x030 m_Count          : 0x38d1
      +0x1a8 m_SetInfoPostOpTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0x1f
         +0x028 m_Total          : 0x79
         +0x030 m_Count          : 0x2b0
      +0x1e0 m_SetSecurityPreOpTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0
         +0x028 m_Total          : 0
         +0x030 m_Count          : 0x5f
      +0x218 m_CleanupPreOpTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0x808a
         +0x028 m_Total          : 0x37dc4
         +0x030 m_Count          : 0x2bffe5
      +0x250 m_CleanupPostOpTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0xf
         +0x028 m_Total          : 0xb4
         +0x030 m_Count          : 0x14a0
      +0x288 m_WritePreOpTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0xad47
         +0x028 m_Total          : 0x93ece
         +0x030 m_Count          : 0x40634
      +0x2c0 m_ReadPreOpTime  : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0x280
         +0x028 m_Total          : 0xeec
         +0x030 m_Count          : 0x38d29
      +0x2f8 m_OpTime1        : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0xffffffff`ffffffff
         +0x020 m_MaxValue       : 0
         +0x028 m_Total          : 0
         +0x030 m_Count          : 0
      +0x330 m_OpTime2        : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0xffffffff`ffffffff
         +0x020 m_MaxValue       : 0
         +0x028 m_Total          : 0
         +0x030 m_Count          : 0
      +0x368 m_OpTime3        : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0xffffffff`ffffffff
         +0x020 m_MaxValue       : 0
         +0x028 m_Total          : 0
         +0x030 m_Count          : 0
      +0x3a0 m_OpTime4        : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0xffffffff`ffffffff
         +0x020 m_MaxValue       : 0
         +0x028 m_Total          : 0
         +0x030 m_Count          : 0
      +0x3d8 m_CachedOpHits   : Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0x39fb1
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
      +0x3f0 m_ConnectedEvent : 0x8af34e18 _KEVENT
         +0x000 Header           : _DISPATCHER_HEADER
   +0x004 m_pRegistryHook  : 0xf73189a0 RegistryHook
      +0x000 __VFN_table : 0xf730cda8 
      +0x004 m_bVerbose       : 0
      +0x008 m_PoolTag        : 0x6f723942
      +0x00c m_ReferenceCount : 0n0
      +0x010 m_MarkedForDeletion : 0
      +0x014 m_Initialized    : 1
      +0x015 m_Running        : 1
      +0x016 m_Connected      : 1
      +0x017 m_Enabled        : 1
      +0x018 m_ShutdownFailure : 0
      +0x01c m_Name           : 0xf730a75c  "RegistryHook"
      +0x020 m_PoolType       : 1 ( PagedPool )
      +0x024 m_PoolTag        : 0x6f723942
      +0x028 m_CreateKeyTime  : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0xbb
         +0x028 m_Total          : 0x4a8
         +0x030 m_Count          : 0x94cb
      +0x060 m_DeleteKeyTime  : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0xf
         +0x028 m_Total          : 0x87
         +0x030 m_Count          : 0x784
      +0x098 m_SetValueKeyTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0x3c8
         +0x028 m_Total          : 0x85a
         +0x030 m_Count          : 0xa44b
      +0x0d0 m_QueryValueKeyTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0x1f4
         +0x028 m_Total          : 0x4984
         +0x030 m_Count          : 0x55b0d6
      +0x108 m_DeleteValueKeyTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0xffffffff`ffffffff
         +0x020 m_MaxValue       : 0
         +0x028 m_Total          : 0
         +0x030 m_Count          : 0
      +0x140 m_RenameKeyTime  : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0xffffffff`ffffffff
         +0x020 m_MaxValue       : 0
         +0x028 m_Total          : 0
         +0x030 m_Count          : 0
      +0x178 m_callbacks      : [47] RegistryCallback
         +0x000 pCallback        : 0xf72ee820           long  Parity!RegistryCallbacks::FilterRegistryPreDeleteKey+0
         +0x004 pContext         : (null) 
      +0x2f0 m_Cookie         : _LARGE_INTEGER 0x01cfc97d`5eb2d24a
         +0x000 LowPart          : 0x5eb2d24a
         +0x004 HighPart         : 0n30394749
         +0x000 u                : <unnamed-tag>
         +0x000 QuadPart         : 0n130544454513906250
   +0x008 m_pObjectHook    : 0xf7318c98 ObjectHook
      +0x000 __VFN_table : 0xf730c96c 
      +0x004 m_bVerbose       : 0
      +0x008 m_PoolTag        : 0x6f6f3942
      +0x00c m_ReferenceCount : 0n0
      +0x010 m_MarkedForDeletion : 0
      +0x014 m_Initialized    : 1
      +0x015 m_Running        : 1
      +0x016 m_Connected      : 1
      +0x017 m_Enabled        : 1
      +0x018 m_ShutdownFailure : 0
      +0x01c m_Name           : 0xf730a750  "ObjectHook"
      +0x020 m_PoolType       : 1 ( PagedPool )
      +0x024 m_PoolTag        : 0x6f6f3942
      +0x028 m_RegistrationHandle : (null) 
      +0x030 m_OpenProcessTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0xf
         +0x028 m_Total          : 0x483
         +0x030 m_Count          : 0xb3b15
      +0x068 m_OpenThreadTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0
         +0x028 m_Total          : 0
         +0x030 m_Count          : 0x78
      +0x0a0 m_DuplicateProcessTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0
         +0x028 m_Total          : 0
         +0x030 m_Count          : 0x2e2
      +0x0d8 m_DuplicateThreadTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0
         +0x028 m_Total          : 0
         +0x030 m_Count          : 0x370e
      +0x110 m_ProtectMemoryTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0x1f
         +0x028 m_Total          : 0x30e
         +0x030 m_Count          : 0x472f
   +0x00c m_pConfigProps   : 0xf7318de0 ConfigProps
      +0x000 __VFN_table : 0xf730bde8 
      +0x004 m_bVerbose       : 0
      +0x008 m_PoolTag        : 0x70673942
      +0x00c m_ReferenceCount : 0n0
      +0x010 m_MarkedForDeletion : 0
      +0x014 m_Initialized    : 1
      +0x015 m_Running        : 1
      +0x016 m_Connected      : 1
      +0x017 m_Enabled        : 1
      +0x018 m_ShutdownFailure : 0
      +0x01c m_Name           : 0xf730a7a0  "ConfigProps"
      +0x020 m_PoolType       : 1 ( PagedPool )
      +0x024 m_PoolTag        : 0x70673942
      +0x028 m_ProcessExclusions : 0
      +0x02c m_ExecuteExclusions : 0xffffffff
      +0x030 m_Flags          : 0
      +0x034 m_Seccon         : 14 ( DAS_SECCON_20 )
      +0x038 m_DisconnectedSecCon : 14 ( DAS_SECCON_20 )
      +0x03c m_bRunningButDisabled : 0
      +0x040 m_DefaultMediaType : 1 ( MEDIA_TYPE_FIXED )
      +0x044 m_Platform       : 0x5020200
      +0x048 m_BuildPlatform  : 0x5020100
      +0x04c m_BuildPlatformString : 0xf72ffba0  "Platform: Windows Server 2003 x86 Release"
      +0x050 m_BlockAndAskTimeoutMs : 0x1b7740
      +0x054 m_ABCacheMissLocalMs : 0x7530
      +0x058 m_ABCacheMissNetworkMs : 0xea60
      +0x05c m_MaxParityAnalysisStallMs : 0x61a8
      +0x060 m_MaxStartupDelayMs : 0xea60
      +0x064 m_MinNormalizationLocalStack : 0x2000
      +0x068 m_MinNormalizationNetworkStack : 0
      +0x06c m_MaxReparseAttempts : 5
      +0x070 m_ConnectWaitTimeMs : 0x1388
      +0x074 m_DirtyNotifyDelayMs : 0x64
      +0x078 m_FileOpDebounceTriggerCount : 0
      +0x07c m_FileOpDebounceMsSinceLastTrigger : 0x7530
      +0x080 m_RegOpDebounceTriggerCount : 0
      +0x084 m_RegOpDebounceMsSinceLastTrigger : 0
      +0x088 m_ObjectOpDebounceTriggerCount : 0
      +0x08c m_ObjectOpDebounceMsSinceLastTrigger : 0
      +0x090 m_bShouldAllowInMonitor : 0
      +0x094 m_VersionInfo    : VersionInfo
         +0x000 major            : 0n6
         +0x002 minor            : 0n0
         +0x004 point            : 0n2
         +0x008 build            : 0n292
         +0x00c date             : [64]  "Sep  7 2011 18:13:15"
         +0x04c debug            : 0
      +0x0e4 m_ProcessStartedCreateMs : 0x7530
      +0x0e8 m_ProcessLastImageLoadMs : 0x2710
      +0x0ec m_ProcessFirstImageLoadMs : 0x1f4
      +0x0f0 m_DeadlockTimeoutMs : 0x3a98
      +0x0f4 m_DepPolicy      : 2
      +0x0f8 m_DepSupported   : 0
      +0x0fc m_PreviousModeOffset : 0
      +0x100 m_WatchdogIntervalMs : 0x800
      +0x104 m_WindowsUpdateServicePid : 0xa54
      =f72b6000 MaximumKernelStack : 0x905a4d
      +0x108 m_PropertyLock   : PushLock
         +0x000 __VFN_table : 0xf730b078 
         +0x004 m_LockName       : 0xf72ff830  "Properties"
         +0x008 m_PushLock       : 0
      +0x114 m_VerbosePattern : UnicodeString
         +0x000 m_String         : _UNICODE_STRING ""
      +0x11c m_StartupDelayPattern : UnicodeString
         +0x000 m_String         : _UNICODE_STRING "*userinit.exe"
      +0x124 m_ReadExcludePattern : UnicodeString
         +0x000 m_String         : _UNICODE_STRING ""
      +0x12c m_WriteExcludePattern : UnicodeString
         +0x000 m_String         : _UNICODE_STRING ""
      +0x134 m_ProcessExcludePattern : UnicodeString
         +0x000 m_String         : _UNICODE_STRING ""
      +0x13c m_ProcessExcludePattern2 : UnicodeString
         +0x000 m_String         : _UNICODE_STRING ""
      +0x144 m_ParityBinDirectory : UnicodeString
         +0x000 m_String         : _UNICODE_STRING "\device\harddiskvolume1\program files\bit9\parity agent\"
      +0x14c m_ParityDataDirectory : UnicodeString
         +0x000 m_String         : _UNICODE_STRING "\device\harddiskvolume1\documents and settings\all users\application data\bit9\parity agent\"
      +0x154 m_ProgramFilesDirectory : UnicodeString
         +0x000 m_String         : _UNICODE_STRING "C:\program files\"
      +0x15c m_Bit9ProgramDataDirectory : UnicodeString
         +0x000 m_String         : _UNICODE_STRING "\device\harddiskvolume1\documents and settings\all users\application data\bit9"
      +0x164 m_Bit9ProgramFilesDirectory : UnicodeString
         +0x000 m_String         : _UNICODE_STRING "\device\harddiskvolume1\program files\bit9"
      +0x16c m_bHaveEverConnected : 1
      +0x170 m_OldBuildNumber : 0x30040124
      +0x174 m_BuildNumber    : 0x30040124
      =f72b6000 s_RuleClassesAllowedWhenDisconnected : 0x905a4d
      +0x178 m_CounterThresholdLock : PushLock
         +0x000 __VFN_table : 0xf730b078 
         +0x004 m_LockName       : 0xf72ff800  "CounterThresholds"
         +0x008 m_PushLock       : 0
      +0x188 m_CounterThresholds : List
         +0x000 __VFN_table : 0xf730c460 
         +0x008 m_PoolTag        : 0x74633942
         +0x00c m_pListHead      : (null) 
         +0x010 m_NumElements    : 0
         +0x014 m_pFreeFn        : 0xf72d3430           void  Parity!List::DeleteElement+0
         +0x018 m_Counter        : PeakCounter
      +0x1d8 m_ConnectedRuleClassFlags : 2
      +0x1dc m_DisconnectedRuleClassFlags : 6
      +0x1e0 m_bDefaultPoliciesEnabled : 0
      =f730f110 s_ConfigProps    : [0] KERNEL_CONFIG_PROP
         +0x000 m_pPropertyName  : 0xf730bd70  "SecCon"
         +0x004 m_RegKeyType     : 4
         +0x008 m_pAddFn         : 0xf72bfd30           bool  Parity!ConfigProps::SetSecCon+0
         +0x00c m_pRevertFn      : 0xf72bcbd0           void  Parity!ConfigProps::RevertSecCon+0
         +0x010 m_pLogFn         : 0xf72bea90           void  Parity!ConfigProps::LogSecCon+0
         +0x014 m_pDumpFn        : 0xf72beae0           void  Parity!ConfigProps::DumpSecCon+0
   +0x010 m_pABCache       : 0xf7318fc8 ABCache
      +0x000 __VFN_table : 0xf730b214 
      +0x004 m_bVerbose       : 0
      +0x008 m_PoolTag        : 0x62613942
      +0x00c m_ReferenceCount : 0n0
      +0x010 m_MarkedForDeletion : 0
      +0x014 m_Initialized    : 1
      +0x015 m_Running        : 1
      +0x016 m_Connected      : 1
      +0x017 m_Enabled        : 1
      +0x018 m_ShutdownFailure : 0
      +0x01c m_Name           : 0xf730a798  "ABCache"
      +0x020 m_PoolType       : 1 ( PagedPool )
      +0x024 m_PoolTag        : 0x62613942
      +0x028 m_AbCache        : 0xe1a34680 HashTable<ABEntry>
         +0x000 __VFN_table : 0xf730bfc8 
         +0x008 m_InternalLock   : SharedLock
         +0x01c m_ExternalLock   : Unlocked
         +0x024 m_Lock           : 0xe1a3469c LockObject
         +0x028 m_PoolType       : 1 ( PagedPool )
         +0x02c m_PoolTag        : 0x62613942
         +0x030 m_Hits           : Counter
         +0x048 m_Misses         : Counter
         +0x060 m_Inserts        : Counter
         +0x078 m_Removes        : Counter
         +0x090 m_CurrentEntries : PeakCounter
         =f72b6000 MaximumTableBuckets : 0n9460301
         =f72b6000 MinimumTableBuckets : 0n9460301
         =f72b6000 DefaultTableBuckets : 0n9460301
         +0x0c8 m_BucketCount    : 0x2000
         +0x0cc m_Buckets        : 0xe1ac4004 HashBucket<ABEntry>
         +0x0d0 m_Collisions     : 0x314e
      +0x02c m_Lock           : PushLock
         +0x000 __VFN_table : 0xf730b078 
         +0x004 m_LockName       : 0xf72fefc0  ""
         +0x008 m_PushLock       : 0
      +0x038 m_Instance       : 0xa490
      +0x03c m_PublisherCache : 0xe1a04008 HashTable<PublisherEntry>
         +0x000 __VFN_table : 0xf730bfc8 
         +0x008 m_InternalLock   : SharedLock
         +0x01c m_ExternalLock   : Unlocked
         +0x024 m_Lock           : 0xe1a04024 LockObject
         +0x028 m_PoolType       : 1 ( PagedPool )
         +0x02c m_PoolTag        : 0x62703942
         +0x030 m_Hits           : Counter
         +0x048 m_Misses         : Counter
         +0x060 m_Inserts        : Counter
         +0x078 m_Removes        : Counter
         +0x090 m_CurrentEntries : PeakCounter
         =f72b6000 MaximumTableBuckets : 0n9460301
         =f72b6000 MinimumTableBuckets : 0n9460301
         =f72b6000 DefaultTableBuckets : 0n9460301
         +0x0c8 m_BucketCount    : 0x40
         +0x0cc m_Buckets        : 0xe1a66114 HashBucket<PublisherEntry>
         +0x0d0 m_Collisions     : 0
      +0x040 m_Misses         : Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0x1f
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
   +0x014 m_pRuleEngine    : 0xf7319020 RuleEngine
      +0x000 __VFN_table : 0xf730da2c 
      +0x004 m_bVerbose       : 0
      +0x008 m_PoolTag        : 0x75723942
      +0x00c m_ReferenceCount : 0n0
      +0x010 m_MarkedForDeletion : 0
      +0x014 m_Initialized    : 1
      +0x015 m_Running        : 1
      +0x016 m_Connected      : 1
      +0x017 m_Enabled        : 1
      +0x018 m_ShutdownFailure : 0
      +0x01c m_Name           : 0xf730a76c  "RuleEngine"
      +0x020 m_PoolType       : 1 ( PagedPool )
      +0x024 m_PoolTag        : 0x75723942
      +0x028 m_StallTime      : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0x12b60
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0x15f90
         +0x028 m_Total          : 0xd0e0e
         +0x030 m_Count          : 0x1f
      +0x060 m_TimedOutStalls : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 6
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 1
         +0x020 m_MaxValue       : 6
         +0x028 m_Total          : 0x15
         +0x030 m_Count          : 6
      +0x098 m_InactiveStallHits : Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 6
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
      +0x0b0 m_PotentialStallOnFileOpen : Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
      +0x0c8 m_Blocks         : [4] Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 4
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
      +0x128 m_Prompts        : [4] Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
      +0x188 m_WouldBlocks    : [4] Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
      +0x1e8 m_WouldPrompts   : [4] Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
      +0x248 m_StalledOps     : List
         +0x000 __VFN_table : 0xf730c460 
         +0x008 m_PoolTag        : 0x75723942
         +0x00c m_pListHead      : (null) 
         +0x010 m_NumElements    : 0
         +0x014 m_pFreeFn        : (null) 
         +0x018 m_Counter        : PeakCounter
      +0x298 m_StalledOpsLock : Mutex
         +0x000 __VFN_table : 0xf730c428 
         +0x004 m_LockName       : 0xf7308390  "Stalled Operations"
         +0x008 m_Mutex          : 0x8aebe150 _FAST_MUTEX
      +0x2a8 m_ClassLists     : [9] List
         +0x000 __VFN_table : 0xf730c460 
         +0x008 m_PoolTag        : 0x70673942
         +0x00c m_pListHead      : 0xe18a21e8 ListElement
         +0x010 m_NumElements    : 7
         +0x014 m_pFreeFn        : 0xf72d3430           void  Parity!List::DeleteElement+0
         +0x018 m_Counter        : PeakCounter
      +0x578 m_pFileOpRules   : 0xe2a9e7e8 RuleList
         +0x000 __VFN_table : 0xf730d9f4 
         +0x004 m_bVerbose       : 0
         +0x008 m_PoolTag        : 0x75723942
         +0x00c m_ReferenceCount : 0n1
         +0x010 m_MarkedForDeletion : 0
         +0x018 m_List           : List
         +0x068 m_RuleListId     : 1
         +0x06c m_RuleType       : 1 ( FileOpRules )
         +0x070 m_RuleListName   : UnicodeString
      +0x57c m_FileOpRulesLock : PushLock
         +0x000 __VFN_table : 0xf730b078 
         +0x004 m_LockName       : 0xf730d268  "FileOpRules"
         +0x008 m_PushLock       : 0
      +0x588 m_pPathPolicies  : 0xe2dc3dc0 RuleList
         +0x000 __VFN_table : 0xf730d9f4 
         +0x004 m_bVerbose       : 0
         +0x008 m_PoolTag        : 0x75723942
         +0x00c m_ReferenceCount : 0n1
         +0x010 m_MarkedForDeletion : 0
         +0x018 m_List           : List
         +0x068 m_RuleListId     : 0x12
         +0x06c m_RuleType       : 2 ( PathPolicyRules )
         +0x070 m_RuleListName   : UnicodeString
      +0x58c m_PathPoliciesLock : PushLock
         +0x000 __VFN_table : 0xf730b078 
         +0x004 m_LockName       : 0xf730d234  "PathPolicies"
         +0x008 m_PushLock       : 0
      +0x598 m_pRegistryRules : 0xe2453830 RuleList
         +0x000 __VFN_table : 0xf730d9f4 
         +0x004 m_bVerbose       : 0
         +0x008 m_PoolTag        : 0x75723942
         +0x00c m_ReferenceCount : 0n1
         +0x010 m_MarkedForDeletion : 0
         +0x018 m_List           : List
         +0x068 m_RuleListId     : 0x12
         +0x06c m_RuleType       : 3 ( RegistryRules )
         +0x070 m_RuleListName   : UnicodeString
      +0x59c m_RegistryRulesLock : PushLock
         +0x000 __VFN_table : 0xf730b078 
         +0x004 m_LockName       : 0xf730d218  "RegistryRules"
         +0x008 m_PushLock       : 0
      +0x5a8 m_pObjectRules   : 0xe194f220 RuleList
         +0x000 __VFN_table : 0xf730d9f4 
         +0x004 m_bVerbose       : 0
         +0x008 m_PoolTag        : 0x75723942
         +0x00c m_ReferenceCount : 0n1
         +0x010 m_MarkedForDeletion : 0
         +0x018 m_List           : List
         +0x068 m_RuleListId     : 0x12
         +0x06c m_RuleType       : 4 ( ObjectRules )
         +0x070 m_RuleListName   : UnicodeString
      +0x5ac m_ObjectRulesLock : PushLock
         +0x000 __VFN_table : 0xf730b078 
         +0x004 m_LockName       : 0xf730d250  "ObjectRules"
         +0x008 m_PushLock       : 0
      +0x5b8 m_TrustedUserSids : List
         +0x000 __VFN_table : 0xf730c460 
         +0x008 m_PoolTag        : 0x75723942
         +0x00c m_pListHead      : (null) 
         +0x010 m_NumElements    : 0
         +0x014 m_pFreeFn        : 0xf72d3430           void  Parity!List::DeleteElement+0
         +0x018 m_Counter        : PeakCounter
      +0x608 m_TrustedUserLock : PushLock
         +0x000 __VFN_table : 0xf730b078 
         +0x004 m_LockName       : 0xf7308370  "Trusted Users"
         +0x008 m_PushLock       : 0
      +0x618 m_TargetInfoCache : HashTable<TargetInfo>
         +0x000 __VFN_table : 0xf730bfc8 
         +0x008 m_InternalLock   : SharedLock
         +0x01c m_ExternalLock   : Unlocked
         +0x024 m_Lock           : 0xf7319654 LockObject
         +0x028 m_PoolType       : 1 ( PagedPool )
         +0x02c m_PoolTag        : 0x69743942
         +0x030 m_Hits           : Counter
         +0x048 m_Misses         : Counter
         +0x060 m_Inserts        : Counter
         +0x078 m_Removes        : Counter
         +0x090 m_CurrentEntries : PeakCounter
         =f72b6000 MaximumTableBuckets : 0n9460301
         =f72b6000 MinimumTableBuckets : 0n9460301
         =f72b6000 DefaultTableBuckets : 0n9460301
         +0x0c8 m_BucketCount    : 0x40
         +0x0cc m_Buckets        : 0xe1a9300c HashBucket<TargetInfo>
         +0x0d0 m_Collisions     : 0
      +0x6f0 m_TargetInfoLock : PushLock
         +0x000 __VFN_table : 0xf730b078 
         +0x004 m_LockName       : 0xf7308340  "Target Info Cache"
         +0x008 m_PushLock       : 0
      +0x6fc m_ParityAnalysisList : 0xe19f5e78 HashTable<ParityAnalysisEntry>
         +0x000 __VFN_table : 0xf730bfc8 
         +0x008 m_InternalLock   : SharedLock
         +0x01c m_ExternalLock   : Unlocked
         +0x024 m_Lock           : 0xe19f5e94 LockObject
         +0x028 m_PoolType       : 1 ( PagedPool )
         +0x02c m_PoolTag        : 0x75723942
         +0x030 m_Hits           : Counter
         +0x048 m_Misses         : Counter
         +0x060 m_Inserts        : Counter
         +0x078 m_Removes        : Counter
         +0x090 m_CurrentEntries : PeakCounter
         =f72b6000 MaximumTableBuckets : 0n9460301
         =f72b6000 MinimumTableBuckets : 0n9460301
         =f72b6000 DefaultTableBuckets : 0n9460301
         +0x0c8 m_BucketCount    : 0x40
         +0x0cc m_Buckets        : 0xe1a78984 HashBucket<ParityAnalysisEntry>
         +0x0d0 m_Collisions     : 0x5f
      +0x700 m_ParityAnalysisLock : PushLock
         +0x000 __VFN_table : 0xf730b078 
         +0x004 m_LockName       : 0xf72fefc0  ""
         +0x008 m_PushLock       : 0
      =f73164ec s_RuleClassStrings : [9] 0xf730d2d0  "ABState"
   +0x018 m_pProcessTracking : 0xf7319730 ProcessTracking
      +0x000 __VFN_table : 0xf730cb98 
      +0x004 m_bVerbose       : 0
      +0x008 m_PoolTag        : 0x74703942
      +0x00c m_ReferenceCount : 0n0
      +0x010 m_MarkedForDeletion : 0
      +0x014 m_Initialized    : 1
      +0x015 m_Running        : 1
      +0x016 m_Connected      : 1
      +0x017 m_Enabled        : 1
      +0x018 m_ShutdownFailure : 0
      +0x01c m_Name           : 0xf730a788  "ProcessTracking"
      +0x020 m_PoolType       : 1 ( PagedPool )
      +0x024 m_PoolTag        : 0x74703942
      =f72b6000 ExpiredProcessLingerMs : 0n9460301
      =f72b6000 ExpiredProcessExtraLingerMs : 0n9460301
      =f72b6000 ExpiredProcessMaximumCount : 0n9460301
      =f72b6000 ExpiredProcessAgeWithChildrenMs : 0n9460301
      =f72b6000 ExpiredProcessAgeIntervalMs : 0n9460301
      +0x028 m_TableLock      : PushLock
         +0x000 __VFN_table : 0xf730b078 
         +0x004 m_LockName       : 0xf7306ae0  "ProcessTrackingTable"
         +0x008 m_PushLock       : 0
      +0x034 m_ProcessTable   : 0xe1982538 TreeTable<ProcessInfo>
         +0x000 __VFN_table : 0xf730c3f8 
         +0x008 m_InternalLock   : SharedLock
         +0x01c m_ExternalLock   : Unlocked
         +0x024 m_Lock           : 0xe1982554 LockObject
         +0x028 m_PoolType       : 1 ( PagedPool )
         +0x02c m_PoolTag        : 0x74703942
         +0x030 m_Hits           : Counter
         +0x048 m_Misses         : Counter
         +0x060 m_Inserts        : Counter
         +0x078 m_Removes        : Counter
         +0x090 m_CurrentEntries : PeakCounter
         +0x0c8 m_Table          : _RTL_AVL_TABLE
      +0x038 m_Timer          : Timer
         +0x000 m_pTimer         : 0x8aec2ac0 _KTIMER
         +0x004 m_pDPC           : 0x8ac9f140 _KDPC
         +0x008 m_pTimerContext  : 0x8add2be8 TimerContext
         +0x00c m_Initialized    : 0n1
      +0x048 m_ScriptProcessorsDone : 1
      +0x04c m_ScriptProcessorLock : PushLock
         +0x000 __VFN_table : 0xf730b078 
         +0x004 m_LockName       : 0xf72fefc0  ""
         +0x008 m_PushLock       : 0
      +0x058 m_ImageDescriptorsDone : 1
      +0x05c m_ImageDescriptorLock : PushLock
         +0x000 __VFN_table : 0xf730b078 
         +0x004 m_LockName       : 0xf72fefc0  ""
         +0x008 m_PushLock       : 0
      +0x068 m_UsingExNotify  : 0
      +0x06c m_NtKernel       : KernelModuleInfo
         +0x000 m_Base           : (null) 
         +0x004 m_Length         : 0
      +0x074 m_NtDll          : KernelModuleInfo
         +0x000 m_Base           : (null) 
         +0x004 m_Length         : 0
      +0x080 m_ExpiredProcesses : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0x68
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0xb
         +0x020 m_MaxValue       : 0x68
         +0x028 m_Total          : 0x33a5
         +0x030 m_Count          : 0xae
      +0x0b8 m_ExpiredProcessCount : 0x68
      +0x0bc m_ZwQueryVirtualMemoryFn : 0x90909000        long  +ffffffff90909000
   +0x01c m_pDirtyTracking : 0xf73197f0 DirtyTracking
      +0x000 __VFN_table : 0xf730bf80 
      +0x004 m_bVerbose       : 0
      +0x008 m_PoolTag        : 0x74643942
      +0x00c m_ReferenceCount : 0n0
      +0x010 m_MarkedForDeletion : 0
      +0x014 m_Initialized    : 1
      +0x015 m_Running        : 1
      +0x016 m_Connected      : 1
      +0x017 m_Enabled        : 1
      +0x018 m_ShutdownFailure : 0
      +0x01c m_Name           : 0xf730a778  "DirtyTracking"
      +0x020 m_PoolType       : 1 ( PagedPool )
      +0x024 m_PoolTag        : 0x74643942
      =f72b6000 s_DeletionStallMs : 0x905a4d
      =f72b6000 DirtyTimerEntriesPerMs : 0x905a4d
      =f72b6000 DirtyTimerMinimumSleepMs : 0x905a4d
      =f72b6000 DirtyTimerMaximumSleepMs : 0x905a4d
      +0x028 m_TimerThread    : 0x800000e4 Void
      +0x02c m_WakeTimerEvent : 0x8afddd48 _KEVENT
         +0x000 Header           : _DISPATCHER_HEADER
      +0x030 m_TimerStartTime : Timestamp
         +0x000 __VFN_table : 0xf730b028 
         +0x008 m_StartTicks     : _LARGE_INTEGER 0x9b340
         +0x010 m_TimestampType  : 2 ( TimestampTypeTickCount )
      +0x048 m_DirtyThreadTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0xf
         +0x028 m_Total          : 0x1e
         +0x030 m_Count          : 0x5d8
      +0x080 m_TransitionsDuringWalks : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 1
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0x6a
         +0x028 m_Total          : 0x85c
         +0x030 m_Count          : 0x494
      +0x0b8 m_TimerAction    : 2 ( DirtyTimerUpdate )
      +0x0bc m_SleepMilliseconds : 0xffffffff
      +0x0c0 m_LastUpdateTimeout : 0
      +0x0c4 m_ShortestWaitMilliseconds : 0xffffffff
      +0x0c8 m_TableLock      : PushLock
         +0x000 __VFN_table : 0xf730b078 
         +0x004 m_LockName       : 0xf72fefc0  ""
         +0x008 m_PushLock       : 0
      +0x0d4 m_DirtyTable     : 0xe1a909b8 HashTable<DirtyEntry>
         +0x000 __VFN_table : 0xf730bfc8 
         +0x008 m_InternalLock   : SharedLock
         +0x01c m_ExternalLock   : Unlocked
         +0x024 m_Lock           : 0xe1a909d4 LockObject
         +0x028 m_PoolType       : 1 ( PagedPool )
         +0x02c m_PoolTag        : 0x74643942
         +0x030 m_Hits           : Counter
         +0x048 m_Misses         : Counter
         +0x060 m_Inserts        : Counter
         +0x078 m_Removes        : Counter
         +0x090 m_CurrentEntries : PeakCounter
         =f72b6000 MaximumTableBuckets : 0n9460301
         =f72b6000 MinimumTableBuckets : 0n9460301
         =f72b6000 DefaultTableBuckets : 0n9460301
         +0x0c8 m_BucketCount    : 0x200
         +0x0cc m_Buckets        : 0xe1aed004 HashBucket<DirtyEntry>
         +0x0d0 m_Collisions     : 0x148
      +0x0d8 m_DirectoryCountTable : 0xe1a67ba0 HashTable<DirectoryCountEntry>
         +0x000 __VFN_table : 0xf730bfc8 
         +0x008 m_InternalLock   : SharedLock
         +0x01c m_ExternalLock   : Unlocked
         +0x024 m_Lock           : 0xe1a67bbc LockObject
         +0x028 m_PoolType       : 1 ( PagedPool )
         +0x02c m_PoolTag        : 0x74643942
         +0x030 m_Hits           : Counter
         +0x048 m_Misses         : Counter
         +0x060 m_Inserts        : Counter
         +0x078 m_Removes        : Counter
         +0x090 m_CurrentEntries : PeakCounter
         =f72b6000 MaximumTableBuckets : 0n9460301
         =f72b6000 MinimumTableBuckets : 0n9460301
         =f72b6000 DefaultTableBuckets : 0n9460301
         +0x0c8 m_BucketCount    : 0x200
         +0x0cc m_Buckets        : 0xe1af0004 HashBucket<DirectoryCountEntry>
         +0x0d0 m_Collisions     : 4
      +0x0e0 m_UnsentRegularDirties : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 8
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0x26
         +0x028 m_Total          : 0x8b97
         +0x030 m_Count          : 0x627
      +0x118 m_UnsentFileDeletions : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0x2e
         +0x028 m_Total          : 0x223c
         +0x030 m_Count          : 0x24d
      +0x150 m_UnsentDirectoryDeletions : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0x12
         +0x028 m_Total          : 0x23c
         +0x030 m_Count          : 0x89
      +0x188 m_UnsentFileRenames : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 1
         +0x028 m_Total          : 0x39
         +0x030 m_Count          : 0x73
      +0x1c0 m_UnsentDirectoryRenames : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0
         +0x028 m_Total          : 0
         +0x030 m_Count          : 1
      +0x1f8 m_TimedOutDirties : Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0x1ba
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
   +0x020 m_pNormalization : 0xf7319a00 Normalization
      +0x000 __VFN_table : 0xf730c900 
      +0x004 m_bVerbose       : 0
      +0x008 m_PoolTag        : 0x616e3942
      +0x00c m_ReferenceCount : 0n0
      +0x010 m_MarkedForDeletion : 0
      +0x014 m_Initialized    : 1
      +0x015 m_Running        : 1
      +0x016 m_Connected      : 1
      +0x017 m_Enabled        : 1
      +0x018 m_ShutdownFailure : 0
      +0x01c m_Name           : 0xf730a7ac  "Normalization"
      +0x020 m_PoolType       : 1 ( PagedPool )
      +0x024 m_PoolTag        : 0x616e3942
      =f72b6000 NormalizationTimerMinimumSleepMs : 0x905a4d
      +0x028 m_IntermediateNameFromRelated : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0xffffffff`ffffffff
         +0x020 m_MaxValue       : 0
         +0x028 m_Total          : 0
         +0x030 m_Count          : 0
      +0x060 m_NoRelatedObject : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0xffffffff`ffffffff
         +0x020 m_MaxValue       : 0
         +0x028 m_Total          : 0
         +0x030 m_Count          : 0
      +0x098 m_NoRelatedStreamContext : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0xffffffff`ffffffff
         +0x020 m_MaxValue       : 0
         +0x028 m_Total          : 0
         +0x030 m_Count          : 0
      +0x0d0 m_LastDirectoryRenameTime : Timestamp
         +0x000 __VFN_table : 0xf730b028 
         +0x008 m_StartTicks     : _LARGE_INTEGER 0x219
         +0x010 m_TimestampType  : 2 ( TimestampTypeTickCount )
      +0x0e8 m_LastDirectoryRenameCounter : Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
      +0x100 m_NormalizeFromFilterTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0x808a
         +0x028 m_Total          : 0x54cc5
         +0x030 m_Count          : 0x50ba56
      +0x138 m_NormalizeFromPathTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0x7ca2
         +0x028 m_Total          : 0x11c17
         +0x030 m_Count          : 0x2de7
      +0x170 m_NormalizeFromFileObjectTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0xffffffff`ffffffff
         +0x020 m_MaxValue       : 0
         +0x028 m_Total          : 0
         +0x030 m_Count          : 0
      +0x1a8 m_TimerThread    : 0x800000f4 Void
      +0x1ac m_WakeTimerEvent : 0x8aecf068 _KEVENT
         +0x000 Header           : _DISPATCHER_HEADER
      +0x1b0 m_TimerStartTime : Timestamp
         +0x000 __VFN_table : 0xf730b028 
         +0x008 m_StartTicks     : _LARGE_INTEGER 0x9635d
         +0x010 m_TimestampType  : 2 ( TimestampTypeTickCount )
      +0x1c8 m_TimerAction    : 2 ( NormalizationTimerUpdate )
      +0x1cc m_SleepMilliseconds : 0xffffffff
      +0x1d0 m_ShortestWaitMilliseconds : 0xffffffff
      +0x1d4 m_TableLock      : PushLock
         +0x000 __VFN_table : 0xf730b078 
         +0x004 m_LockName       : 0xf72fefc0  ""
         +0x008 m_PushLock       : 0
      +0x1e0 m_NormalizationCache : 0xe1aab248 HashTable<NormalizationEntry>
         +0x000 __VFN_table : 0xf730bfc8 
         +0x008 m_InternalLock   : SharedLock
         +0x01c m_ExternalLock   : Unlocked
         +0x024 m_Lock           : 0xe1aab264 LockObject
         +0x028 m_PoolType       : 1 ( PagedPool )
         +0x02c m_PoolTag        : 0x616e3942
         +0x030 m_Hits           : Counter
         +0x048 m_Misses         : Counter
         +0x060 m_Inserts        : Counter
         +0x078 m_Removes        : Counter
         +0x090 m_CurrentEntries : PeakCounter
         =f72b6000 MaximumTableBuckets : 0n9460301
         =f72b6000 MinimumTableBuckets : 0n9460301
         =f72b6000 DefaultTableBuckets : 0n9460301
         +0x0c8 m_BucketCount    : 0x200
         +0x0cc m_Buckets        : 0xe1ac1004 HashBucket<NormalizationEntry>
         +0x0d0 m_Collisions     : 1
   +0x024 m_pDeviceTracking : 0xf7319be8 DeviceTracking
      +0x000 __VFN_table : 0xf730bed0 
      +0x004 m_bVerbose       : 0
      +0x008 m_PoolTag        : 0x65643942
      +0x00c m_ReferenceCount : 0n0
      +0x010 m_MarkedForDeletion : 0
      +0x014 m_Initialized    : 1
      +0x015 m_Running        : 1
      +0x016 m_Connected      : 1
      +0x017 m_Enabled        : 1
      +0x018 m_ShutdownFailure : 0
      +0x01c m_Name           : 0xf730a7bc  "DeviceTracking"
      +0x020 m_PoolType       : 1 ( PagedPool )
      +0x024 m_PoolTag        : 0x65643942
      =f73103fc s_MediaCodeStrings : [0] 0xf730ae2c  "Unknown"
      +0x028 m_TableLock      : PushLock
         +0x000 __VFN_table : 0xf730b078 
         +0x004 m_LockName       : 0xf7300030  "DeviceTrackingTable"
         +0x008 m_PushLock       : 0
      +0x034 m_DeviceTable    : 0xe1a48db0 HashTable<DeviceInfo>
         +0x000 __VFN_table : 0xf730bfc8 
         +0x008 m_InternalLock   : SharedLock
         +0x01c m_ExternalLock   : Unlocked
         +0x024 m_Lock           : 0xe1a48dcc LockObject
         +0x028 m_PoolType       : 1 ( PagedPool )
         +0x02c m_PoolTag        : 0x65643942
         +0x030 m_Hits           : Counter
         +0x048 m_Misses         : Counter
         +0x060 m_Inserts        : Counter
         +0x078 m_Removes        : Counter
         +0x090 m_CurrentEntries : PeakCounter
         =f72b6000 MaximumTableBuckets : 0n9460301
         =f72b6000 MinimumTableBuckets : 0n9460301
         =f72b6000 DefaultTableBuckets : 0n9460301
         +0x0c8 m_BucketCount    : 0x40
         +0x0cc m_Buckets        : 0xe1a82624 HashBucket<DeviceInfo>
         +0x0d0 m_Collisions     : 0
      +0x038 m_Mounts         : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0xec
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 1
         +0x020 m_MaxValue       : 0xec
         +0x028 m_Total          : 0x6d3e
         +0x030 m_Count          : 0xec
      +0x070 m_Dismounts      : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0xe8
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 1
         +0x020 m_MaxValue       : 0xe8
         +0x028 m_Total          : 0x6994
         +0x030 m_Count          : 0xe8
      +0x0a8 m_FlushRemovedTimer : Timer
         +0x000 m_pTimer         : 0x8aec1200 _KTIMER
         +0x004 m_pDPC           : 0x8af138d0 _KDPC
         +0x008 m_pTimerContext  : 0x8aec01f8 TimerContext
         +0x00c m_Initialized    : 0n1
   +0x028 m_pWatchdogServices : 0xf7319ca0 WatchdogServices
      +0x000 __VFN_table : 0xf730cc40 
      +0x004 m_bVerbose       : 0
      +0x008 m_PoolTag        : 0x72643942
      +0x00c m_ReferenceCount : 0n0
      +0x010 m_MarkedForDeletion : 0
      +0x014 m_Initialized    : 1
      +0x015 m_Running        : 1
      +0x016 m_Connected      : 1
      +0x017 m_Enabled        : 1
      +0x018 m_ShutdownFailure : 0
      +0x01c m_Name           : 0xf730a7cc  "Watchdog"
      +0x020 m_PoolType       : 1 ( PagedPool )
      +0x024 m_PoolTag        : 0x72643942
      +0x028 m_TimerThread    : 0x800000fc Void
      +0x02c m_WakeTimerEvent : 0x8af2c248 _KEVENT
         +0x000 Header           : _DISPATCHER_HEADER
      +0x030 m_TimerStartTime : Timestamp
         +0x000 __VFN_table : 0xf730b028 
         +0x008 m_StartTicks     : _LARGE_INTEGER 0xa3b72
         +0x010 m_TimestampType  : 2 ( TimestampTypeTickCount )
      +0x048 m_TableLock      : PushLock
         +0x000 __VFN_table : 0xf730b078 
         +0x004 m_LockName       : 0xf72fefc0  ""
         +0x008 m_PushLock       : 0
      +0x054 m_WatchdogTable  : 0xe1a71f00 TreeTable<WatchdogEntry>
         +0x000 __VFN_table : 0xf730c3f8 
         +0x008 m_InternalLock   : SharedLock
         +0x01c m_ExternalLock   : Unlocked
         +0x024 m_Lock           : 0xe1a71f1c LockObject
         +0x028 m_PoolType       : 1 ( PagedPool )
         +0x02c m_PoolTag        : 0x72643942
         +0x030 m_Hits           : Counter
         +0x048 m_Misses         : Counter
         +0x060 m_Inserts        : Counter
         +0x078 m_Removes        : Counter
         +0x090 m_CurrentEntries : PeakCounter
         +0x0c8 m_Table          : _RTL_AVL_TABLE
      +0x058 m_WatchdogExpirations : Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
   +0x02c m_pControl       : 0xf7318430 Control
      +0x000 __VFN_table : 0xf730be34 
      +0x004 m_bVerbose       : 0
      +0x008 m_PoolTag        : 0x6c663942
      +0x00c m_ReferenceCount : 0n16
      +0x010 m_MarkedForDeletion : 0
      +0x014 m_Initialized    : 1
      +0x015 m_Running        : 1
      +0x016 m_Connected      : 1
      +0x017 m_Enabled        : 1
      +0x018 m_ShutdownFailure : 0
      +0x01c m_Name           : 0xf730a73c  "Control"
      +0x020 m_PoolType       : 1 ( PagedPool )
      +0x024 m_PoolTag        : 0x6c663942
      +0x028 m_FileTypeCounters : FileTypeCounters
         =f72b6000 MaxFileTypeFormatLength : 0n9460301
         =f72b6000 DefaultFileTypeFormatCh : 77 'M'
         +0x000 m_FileTypeThreshold : 0x80
         +0x004 m_MaxFileTypeChLen : 4
         +0x008 m_PoolTag        : 0x6c663942
         +0x00c m_PoolType       : 1 ( PagedPool )
         +0x010 m_FileTypeCountersTableLock : PushLock
         +0x01c m_FileTypeCountersTable : 0xe1a777a8 TreeTable<FileTypeCountersEntry>
      +0x048 m_StringCounter  : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0x2e
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0xffff
         +0x028 m_Total          : 0x00000002`8bd18d72
         +0x030 m_Count          : 0x479cde7
      +0x080 m_DeferredWorkTime : PeakCounter
         +0x000 __VFN_table : 0xf730b260 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
         +0x018 m_MinValue       : 0
         +0x020 m_MaxValue       : 0xf
         +0x028 m_Total          : 0x2d
         +0x030 m_Count          : 0x10c
      +0x0b8 m_ExceptionCountRegistryHook : Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
      +0x0d0 m_ExceptionCountNormalization : Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
      +0x0e8 m_ExceptionCountProcessInfo : Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
      +0x100 m_ExceptionCountObjectHook : Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
      +0x118 m_ExceptionCountFileHook : Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
      +0x130 m_ExceptionCountDeferredWork : Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
      +0x148 m_ExceptionCountUserModeMemory : Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
      +0x160 m_MemoryAllocationCountFailures : Counter
         +0x000 __VFN_table : 0xf730b02c 
         +0x008 m_Value          : 0
         +0x010 m_NumViolations  : 0
         +0x014 m_Id             : 0
```

## References
- [Common windbg commands (Thematically Grouped)](http://windbg.info/doc/1-common-cmds.html)
- [Common Wndbg Commands: breakpoints](http://windbg.info/doc/1-common-cmds.html#13_breakpoints)

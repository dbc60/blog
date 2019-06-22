---
title: An Editor and Debugger for Windows Installers
date: 2016-12-09
draft: true
categories: [projects, software]
tags: [editor, debugger]
---

I have been completely frustrated with the [WiX Toolset](https://wixtoolset.org). There is no visibility into what is actually taking place in the installer when one describes it using XML. The candle and light tools provide insufficient warning and error messages. Installers fail during runtime and the failure logs do not help enough to uncover the errors.
<!--more-->

## Windows Installer
The [Roadmap to the Documentation](https://msdn.microsoft.com/en-us/library/aa371366(v=vs.85).aspx) for Windows Installer is my starting point for understanding the API and the elements of the installer database.

There are different versions of Windows installer. Windows installer 5.0 was released with and requires Windows Server 2012, Windows 8, Windows Server 2012 R2 or Windows 7. Windows Installer 4.5 requires Windows Server 2008, Windows Vista, Windows XP with Service Pack 2 (SP2) and later. I do not care about earlier versions.

## Concepts
There are a lot of [concepts and terms](https://msdn.microsoft.com/en-us/library/windows/desktop/aa370566(v=vs.85).aspx) to learn about Windows Installers. Here are some of the important ones.

[Installation Package](https://msdn.microsoft.com/en-us/library/windows/desktop/aa369294(v=vs.85).aspx). This contains all of the information that the Windows Installer requires to install or uninstall an application or prodcut and to run the setup user interface. Each installation package includes an `.msi` file, containing an installation database, a summary information stream, and data streams for various parts of the installation. The .msi file can also contain one or more transforms, internal source files and external source files or cabinet files required by the installation.

[Components and Features](https://msdn.microsoft.com/en-us/library/windows/desktop/aa368003(v=vs.85).aspx). The Windows Installer organizes an installatino around the concept of components and features. A feature is a part of the application's total functionality that a user may decide to install independently. A component is a piece of tha pplication or product to be installed. The installer always installs or removes a component from a user's computer as a coherent piece. Components are usually hidden from the user. When a user selects a feature for installation, the installer determines which components must be installed to provide that feature.

[Installation Mechanism](https://msdn.microsoft.com/en-us/library/windows/desktop/aa369288(v=vs.85).aspx). The isntallation process has two main phases: acquisition and execution. If the installation fails, a rollback phase may occur.

At the beginning of the acquisition phase, an application or a user instructs the installer to install a feature or an application. The installer works through the actions specified in the sequence tables of the installation database. These actions query the installation database and generate a script that gives a step-by-step procedure for performing the installation.

During the execution phase, the installer passes the information to a process with elevated privileges and runs the script.

In the case of an unsuccessful installation, the installer restores the original state of the computer. Whent the installer processes the installation script, it simultaneously generates a rollback script.

[Component Management](https://msdn.microsoft.com/en-us/library/windows/desktop/aa368006(v=vs.85).aspx). The installation database tracks which applications require a particular component, which files comprise each component, where each file is installed on the system and where component sources are located. This enables authors to provide a number of benefits outlined in the linked documentation.

[Advertisment](https://msdn.microsoft.com/en-us/library/windows/desktop/aa367548(v=vs.85).aspx). The installer enables the advertisement of application and features according to the operting system. This means shortcuts and icons can be installed. File name extensions can be assigned to applications. Shell commands and verbs can be registered.

[Installation on Demand](https://msdn.microsoft.com/en-us/library/windows/desktop/aa369293(v=vs.85).aspx). This capability works in conjuction with Advertisment to enable users and applications to install functionality or entire products automatically. When a user or application activates an advertized feature or product, the installer proceeds with installation of the needed components. Installation on demand shortens the configuration process, because additional functionality can be accessed without having to exit and rerun another setup procedure.

## Organization of an Installer
Microsoft recommends that developers use a standard procedure for choosing components. See [Organizing Applications into Components](https://msdn.microsoft.com/en-us/library/windows/desktop/aa370561(v=vs.85).aspx) for more information.

Package authors can use third-party package creation tools, or a table editor and the Windows Installer SDK to populate the installation database. All installation packages need to be validated for internal consistency. For more information, see [Package Validation](https://msdn.microsoft.com/en-us/library/windows/desktop/aa370569(v=vs.85).aspx).


## References

- [Windows Installer](https://msdn.microsoft.com/en-us/library/windows/desktop/cc185688(v=vs.85).aspx)
- [Role-based Guide to Windows Installer Documentation](https://msdn.microsoft.com/en-us/library/aa371367(v=vs.85).aspx)
- [Windows Installer Examples](https://msdn.microsoft.com/en-us/library/aa372837(v=vs.85).aspx)
- [Other Sources of Windows Installer Information](https://msdn.microsoft.com/en-us/library/aa370563(v=vs.85).aspx). This page has tons of links to various resources, knowledge base articles and whitepapers.
- [Orca Documentation](https://msdn.microsoft.com/en-us/library/aa370557(v=vs.85).aspx). Note: "Although Orca provides access to all features of the Windows Installer, it is not intended to replace a fully featured package-authoring environment. In many cases, it is easier to create a Windows Installer installation for an application by using one of the commercial package-creation tools available from independent software vendors."
- [InstallSite](http://www.installsite.org/)
- [msi2xml](http://msi2xml.sourceforge.net/) is a pair of tools for converting a Windows Installer Database (.msi/.msm) to text-based XML and vice versa.
- [MSXML](https://msdn.microsoft.com/en-us/library/ms763742(v=vs.85).aspx) is Microsoft XML Core Services, which provides a set of W3C compliant XML APIs for building high-performance XML-based applications.
-[Advanced Installer User Guide](http://www.advancedinstaller.com/user-guide/tutorial-ai-ext-vs.html). This may be a better tool for creating installers.

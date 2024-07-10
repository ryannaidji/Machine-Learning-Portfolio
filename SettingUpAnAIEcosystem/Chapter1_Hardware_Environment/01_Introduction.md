# Installation and Introduction to Linux Operating System

1. Why Use Linux For AI?
2. Advantages of Linux Over Windows
3. Installing and Discovering a Linux OS
4. Introduction to the Linux File System
5. Introduction to the Shell
6. Basic Commands

---

## Why Use Linux for AI?

Linux is the operating system of choice for many AI practitioners and enterprises for several reasons:

1. **Open Source**: Linux is open-source, which means it is free to use, modify, and distribute. This encourages innovation and collaboration within the AI community.
2. **Customization**: The open nature of Linux allows for extensive customization, enabling users to optimize their systems for specific AI workloads.
3. **Performance**: Linux is known for its stability and performance. It can handle intensive computations and large datasets efficiently, which is crucial for AI applications.
4. **Community Support**: There is a large and active community of developers and researchers contributing to Linux, ensuring continuous improvements and support.
5. **Compatibility**: Many AI frameworks and tools, such as TensorFlow, PyTorch, and Keras, are designed to run optimally on Linux. Additionally, Linux supports a wide range of hardware, from GPUs to high-performance computing clusters.

---

## Advantages of Linux Over Windows

While Windows is a popular operating system, Linux offers several advantages for AI development and deployment:

1. **Resource Efficiency**: Linux is lightweight and can run on older or less powerful hardware, making it more efficient in resource usage compared to Windows.
2. **Security**: Linux has a robust security model and is less prone to viruses and malware, providing a safer environment for sensitive AI data and applications.
3. **Flexibility**: Linux allows users to automate tasks and create custom scripts using powerful tools like Bash, which can streamline AI workflows.
4. **Server and Cloud Integration**: Linux is the dominant OS in the server and cloud environments. This seamless integration makes it easier to deploy AI models in production.
5. **Package Management**: Linux distributions come with package managers (e.g., apt, yum) that simplify the installation and management of software dependencies.

---

## Installing and Discovering a Linux OS

### Installation

1. **Choosing a Distribution**: Popular distributions include Ubuntu, Fedora, and Debian.
2. **Downloading the ISO**: Visit the official website of the chosen distribution to download the ISO file.
3. **Creating a Bootable USB**: Use tools like Rufus (Windows) or Etcher (Mac/Linux) to create a bootable USB drive.
4. **Booting from USB**: Restart your computer and boot from the USB drive.
5. **Installation Process**: Follow the on-screen instructions to install the Linux OS on your system.

> [!NOTE]
>
> We will see in the next chapter that we can use virtual machines with a Linux OS instead of using booting keys.
> 
### Discovering Linux OS

1. **Logging In**: After installation, log in with the username and password created during setup.
2. **Exploring the Desktop Environment**: Familiarize yourself with the desktop environment (GNOME, KDE, etc.).
3. **System Updates**: Run system updates to ensure all packages are up-to-date.

---

## Introduction to the Linux File System

### Overview

1. **Hierarchical Structure**: The Linux file system is organized in a hierarchical structure.
2. **Root Directory (`/`)**: The root directory is the top-level directory.
3. **Common Directories**:
   - `/bin`: Essential binary files
   - `/etc`: Configuration files
   - `/home`: User home directories
   - `/var`: Variable data files
   - `/tmp`: Temporary files
   - `/usr`: User programs and data

### Permissions

1. **File Permissions**: Linux uses a permission system to control access to files and directories.
2. **Permission Types**: Read (`r`), write (`w`), and execute (`x`).
3. **Changing Permissions**: Use the `chmod` command to change file permissions.

---

## Introduction to the Shell

### What is the Shell?

1. **Definition**: The shell is a command-line interface that allows users to interact with the operating system.
2. **Types of Shells**: Common shells include Bash, Zsh, and Fish.

### Basic Shell Usage

1. **Opening the Terminal**: Access the terminal through the applications menu or by pressing `Ctrl+Alt+T`.
2. **Command Syntax**: Commands follow a syntax of `command [options] [arguments]`.

---

## Basic Commands

### File and Directory Commands

1. **Listing Files**: `ls`
2. **Changing Directory**: `cd`
3. **Creating a Directory**: `mkdir`
4. **Removing a File**: `rm`
5. **Copying Files**: `cp`
6. **Moving Files**: `mv`

### System Commands

1. **Checking Disk Usage**: `df`
2. **Checking Memory Usage**: `free`
3. **Viewing Running Processes**: `ps`
4. **Killing a Process**: `kill`

### Network Commands

1. **Checking Network Configuration**: `ifconfig`
2. **Pinging a Host**: `ping`
3. **Tracing a Route**: `traceroute`

### Helpful Commands

1. **Manual Pages**: `man` - Access the manual pages for commands.
2. **Command History**: `history` - View previously entered commands.

---

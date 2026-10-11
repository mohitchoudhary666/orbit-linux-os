# Architecture

Orbit Linux is a small Linux distribution assembled by Buildroot. Buildroot downloads and cross-compiles a Linux kernel and user-space packages, then combines them into a root filesystem image.

```text
QEMU x86_64 machine
  +-- Linux kernel (serial console on ttyS0)
  +-- Buildroot root filesystem (ext2)
        +-- BusyBox init and applets
        +-- serial getty and shell
        +-- /etc/init.d/S99orbitos boot banner
        +-- /usr/bin/orbitos learning commands
```

The scripts configure Buildroot's QEMU x86_64 defconfig, add this project's root filesystem overlay, build the kernel and image, and launch QEMU. Buildroot and its packages remain upstream; Orbit Linux owns the configuration and overlay.

This project packages the Linux kernel; it does not implement a kernel. x86_64 QEMU is the first target. A desktop, package updates, persistent user management, and production hardening are outside the initial scope.

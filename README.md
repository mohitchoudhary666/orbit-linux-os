# Orbit Linux

**A small, bootable Linux distribution for learning how an operating system is assembled.**

Orbit Linux is a Buildroot-based x86_64 system with the Linux kernel, BusyBox, a serial-console shell, and a few useful first-boot commands. It targets QEMU and education; it is not a new kernel or a production server distribution.

![Build](https://github.com/mohitchoudhary666/orbit-linux-os/actions/workflows/build.yml/badge.svg)
![Architecture](https://img.shields.io/badge/architecture-x86__64-6f42c1)
![License](https://img.shields.io/badge/project%20files-MIT-2ea44f)

## What works

- Builds a Linux kernel and root filesystem for x86_64 using Buildroot 2026.08.
- Boots the kernel and disk image in QEMU.
- Starts BusyBox init and a login shell on the serial console.
- Includes `orbitos`, `orbitos-health`, and a welcome message.
- Builds in GitHub Actions and uploads boot files as a workflow artifact.

## Quick start

On Debian or Ubuntu, install the host tools:

```sh
sudo apt-get update
sudo apt-get install -y bc build-essential cpio file git make python3 qemu-system-x86 rsync unzip wget
```

Build and boot:

```sh
git clone https://github.com/mohitchoudhary666/orbit-linux-os.git
cd orbit-linux-os
sh ./scripts/build.sh
sh ./scripts/run-qemu.sh
```

The first build downloads Buildroot and its upstream source packages and may take several minutes. At the login prompt, enter `root` (the local QEMU image has no root password). **Do not expose this image to a network or use it for production.**

For Windows, use WSL 2 with Ubuntu and run both commands inside WSL.

## Try the system

```sh
orbitos help
orbitos about
orbitos health
```

The image is intentionally small. It has no graphical desktop, package manager, additional user accounts, or network-facing services.

## Project layout

```text
board/orbitos/       Root filesystem overlay and post-build setup
docs/                Architecture and security notes
scripts/             Build and QEMU launcher
.github/workflows/   Reproducible CI build
```

## Contributing

Everyone is welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md), browse issues marked `good first issue`, or open an issue before a larger change. Keep pull requests focused, describe how to reproduce the change, and never commit build output, credentials, or private keys.

## License

The configuration, scripts, and documentation here are MIT licensed. Buildroot, Linux, BusyBox, and any other bundled upstream components retain their own licenses; see [docs/THIRD_PARTY.md](docs/THIRD_PARTY.md).

#!/bin/sh
set -eu
SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
PROJECT_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)"
KERNEL="$PROJECT_ROOT/dist/orbit-linux-bzImage"
ROOTFS="$PROJECT_ROOT/dist/orbit-linux-rootfs.ext2"
command -v qemu-system-x86_64 >/dev/null 2>&1 || { echo 'Install qemu-system-x86_64 first.' >&2; exit 1; }
[ -s "$KERNEL" ] && [ -s "$ROOTFS" ] || { echo 'Run ./scripts/build.sh first.' >&2; exit 1; }
exec qemu-system-x86_64 -machine pc -m 512 -kernel "$KERNEL" \
    -drive "file=$ROOTFS,format=raw,if=virtio" \
    -append "root=/dev/vda rootwait rw console=ttyS0" -serial stdio

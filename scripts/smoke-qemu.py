#!/usr/bin/env python3
"""Boot the built image and require the Orbit init banner on serial."""

from __future__ import annotations

import os
import selectors
import subprocess
import sys
import time
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    kernel = root / "dist/orbit-linux-bzImage"
    disk = root / "dist/orbit-linux-rootfs.ext2"
    if not kernel.is_file() or not disk.is_file():
        print("Orbit Linux images are missing; build the image first.", file=sys.stderr)
        return 2

    command = [
        "qemu-system-x86_64",
        "-machine", "pc",
        "-m", "512",
        "-kernel", str(kernel),
        "-drive", f"file={disk},format=raw,if=virtio",
        "-append", "root=/dev/vda rootwait rw console=ttyS0",
        "-display", "none",
        "-monitor", "none",
        "-serial", "stdio",
    ]
    try:
        process = subprocess.Popen(
            command,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            bufsize=0,
        )
    except FileNotFoundError:
        print("qemu-system-x86_64 is required for the boot smoke check.", file=sys.stderr)
        return 2

    output = bytearray()
    selector = selectors.DefaultSelector()
    assert process.stdout is not None
    selector.register(process.stdout, selectors.EVENT_READ)
    deadline = time.monotonic() + 120
    banner = b"Orbit Linux is up. Log in as root"
    try:
        while time.monotonic() < deadline:
            if process.poll() is not None:
                break
            for key, _ in selector.select(timeout=1):
                chunk = os.read(key.fd, 4096)
                if chunk:
                    output.extend(chunk)
                    if banner in output:
                        print("QEMU booted and Orbit init started on the serial console.")
                        return 0
        print("Orbit Linux did not reach its init banner within 120 seconds.", file=sys.stderr)
        print(output[-8000:].decode("utf-8", errors="replace"), file=sys.stderr)
        return 1
    finally:
        selector.close()
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Apply Orbit settings to a Buildroot qemu_x86_64 defconfig."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def read_symbol(text: str, name: str) -> str | None:
    match = re.search(rf"^{re.escape(name)}=(.*)$", text, re.MULTILINE)
    return match.group(1) if match else None


def set_symbol(text: str, name: str, value: str) -> str:
    pattern = re.compile(rf"^(?:{re.escape(name)}=.*|# {re.escape(name)} is not set)$", re.MULTILINE)
    line = f"{name}={value}"
    if pattern.search(text):
        return pattern.sub(line, text, count=1)
    return text.rstrip() + "\n" + line + "\n"


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: configure_buildroot.py BUILDROOT_CONFIG PROJECT_ROOT", file=sys.stderr)
        return 2
    config_path = Path(sys.argv[1])
    project_root = Path(sys.argv[2]).resolve()
    text = config_path.read_text(encoding="utf-8")

    settings = {
        "BR2_TARGET_GENERIC_HOSTNAME": json.dumps("orbit-linux"),
        "BR2_TARGET_GENERIC_ISSUE": json.dumps("Welcome to Orbit Linux - a small system for learning."),
        "BR2_TARGET_GENERIC_GETTY": "y",
        "BR2_TARGET_GENERIC_GETTY_PORT": json.dumps("ttyS0"),
        "BR2_TARGET_GENERIC_GETTY_BAUDRATE_115200": "y",
        "BR2_ROOTFS_OVERLAY": json.dumps(str(project_root / "board/orbitos/rootfs-overlay")),
    }

    # Preserve any board-specific post-build hook installed by the base defconfig.
    existing = read_symbol(text, "BR2_ROOTFS_POST_BUILD_SCRIPT")
    hooks: list[str] = []
    if existing:
        try:
            hooks.extend(json.loads(existing).split())
        except json.JSONDecodeError:
            hooks.extend(existing.strip('"').split())
    orbit_hook = str(project_root / "board/orbitos/post-build.sh")
    if orbit_hook not in hooks:
        hooks.append(orbit_hook)
    settings["BR2_ROOTFS_POST_BUILD_SCRIPT"] = json.dumps(" ".join(hooks))

    for name, value in settings.items():
        text = set_symbol(text, name, value)
    config_path.write_text(text, encoding="utf-8", newline="\n")
    print(f"Applied Orbit Linux settings to {config_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

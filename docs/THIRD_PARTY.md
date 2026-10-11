# Third-party components

Buildroot downloads and builds upstream components at build time. They retain their original licenses.

| Component | Role | License |
| --- | --- | --- |
| Buildroot 2026.08 | Build system and package recipes | GNU GPL-2.0-or-later |
| Linux kernel | Operating-system kernel | GNU GPL-2.0-only (with documented exceptions) |
| BusyBox | Init, shell, and user-space utilities | GNU GPL-2.0-only |

This list is not exhaustive: the configuration may include additional transitive packages. Consult Buildroot's generated legal information and each upstream package's license files before redistributing a binary image. Orbit-specific files are MIT licensed.

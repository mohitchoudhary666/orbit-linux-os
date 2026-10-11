# Security notes

- The default root account is passwordless for convenient local emulator access.
- The image has no SSH server enabled and should be treated as offline-only.
- Do not use it for production, store secrets in it, or bridge QEMU to an untrusted network.
- Discuss network services or login changes in an issue before implementing them.

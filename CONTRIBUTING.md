# Contributing

Thanks for helping make Orbit Linux better. Everyone is welcome, including first-time contributors.

## Workflow

1. Search existing issues and pull requests first.
2. Open an issue before a large design change.
3. Fork the repository and create a focused branch such as `docs/improve-qemu-guide`.
4. Follow the README build steps for image or configuration changes.
5. Open a pull request with a clear summary, the commands you ran, and relevant logs or screenshots.

GitHub Actions builds the image for every pull request. If the build cannot run locally, explain that in the PR; documentation-only contributions are welcome too.

## Guidelines

- Keep the default image small and suitable for an offline emulator.
- Do not add telemetry, secrets, passwords, SSH keys, or network services without prior discussion.
- Preserve upstream licenses and record new third-party components in `docs/THIRD_PARTY.md`.
- Be respectful and constructive in all project spaces.

By contributing, you agree that your changes are provided under this repository's MIT license, except for files that clearly retain another upstream license.

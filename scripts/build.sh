#!/bin/sh
set -eu
SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
PROJECT_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)"
BUILDROOT_DIR="$PROJECT_ROOT/.build/buildroot"
BUILDROOT_URL="https://gitlab.com/buildroot.org/buildroot.git"
BUILDROOT_VERSION="2026.08"
JOBS="${JOBS:-$(getconf _NPROCESSORS_ONLN 2>/dev/null || echo 2)}"

for tool in git make python3; do
    command -v "$tool" >/dev/null 2>&1 || { echo "Missing required tool: $tool" >&2; exit 1; }
done

if [ ! -d "$BUILDROOT_DIR/.git" ]; then
    mkdir -p "$PROJECT_ROOT/.build"
    git clone --depth 1 --branch "$BUILDROOT_VERSION" "$BUILDROOT_URL" "$BUILDROOT_DIR"
fi

cd "$BUILDROOT_DIR"
make qemu_x86_64_defconfig
python3 "$PROJECT_ROOT/scripts/configure_buildroot.py" "$BUILDROOT_DIR/.config" "$PROJECT_ROOT"
make olddefconfig
make -j"$JOBS"

IMAGE_DIR="$BUILDROOT_DIR/output/images"
for image in bzImage rootfs.ext2; do
    [ -s "$IMAGE_DIR/$image" ] || { echo "Missing expected image: $IMAGE_DIR/$image" >&2; exit 1; }
done
mkdir -p "$PROJECT_ROOT/dist"
cp "$IMAGE_DIR/bzImage" "$PROJECT_ROOT/dist/orbit-linux-bzImage"
cp "$IMAGE_DIR/rootfs.ext2" "$PROJECT_ROOT/dist/orbit-linux-rootfs.ext2"
printf 'Orbit Linux images are ready in %s/dist\n' "$PROJECT_ROOT"

#!/bin/sh
set -eu

target_dir="${1:?Buildroot must pass the target directory}"
chmod 0755 "$target_dir/usr/bin/orbitos"
chmod 0755 "$target_dir/usr/bin/orbitos-health"
chmod 0755 "$target_dir/etc/init.d/S99orbitos"

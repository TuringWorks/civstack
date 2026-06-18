#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
SOURCE="$SCRIPT_DIR/parametric-torso.scad"
OUTPUT_DIR="${1:-$SCRIPT_DIR/generated-dxf}"
LAYER_COUNT="${LAYER_COUNT:-34}"

if ! command -v openscad >/dev/null 2>&1; then
  echo "OpenSCAD is required: https://openscad.org/" >&2
  exit 1
fi

mkdir -p "$OUTPUT_DIR"

for ((i = 0; i < LAYER_COUNT; i++)); do
  printf -v layer_name "torso-layer-%02d.dxf" "$i"
  openscad \
    -o "$OUTPUT_DIR/$layer_name" \
    -D 'mode="layer"' \
    -D "layer_index=$i" \
    -D "layer_count=$LAYER_COUNT" \
    "$SOURCE"
done

echo "Exported $LAYER_COUNT layers to $OUTPUT_DIR"


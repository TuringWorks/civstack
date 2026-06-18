#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
xmllint --noout "$SCRIPT_DIR/generated/lamina-v06.urdf"
joint_count="$(xmllint --xpath 'count(/robot/joint)' "$SCRIPT_DIR/generated/lamina-v06.urdf")"
if [[ "$joint_count" != "31" ]]; then
  echo "Expected 31 joints; found $joint_count" >&2
  exit 1
fi
echo "URDF validation passed: 31 controlled joints."


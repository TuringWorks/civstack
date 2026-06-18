#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 validate_project.py
./simulation/validate.sh

if [ "${1:-}" = "--deep-freecad" ]; then
  ./cad/freecad/generate-and-validate.sh --validate-only
  ./prototype-joint-rig/cad/generate-and-validate.sh --validate-only
else
  echo "FreeCAD containers and saved reports validated statically."
  echo "Use ./validate-project.sh --deep-freecad to rerun geometry checks in FreeCAD."
fi

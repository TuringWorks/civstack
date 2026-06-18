#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
FREECADCMD="${FREECADCMD:-/Applications/FreeCAD.app/Contents/Resources/bin/freecadcmd}"

run_script() {
  local path="$1"
  "$FREECADCMD" -c "p=r'''$path'''; exec(compile(open(p).read(),p,'exec'),{'__file__':p,'__name__':'__main__'})"
}

if [[ "${1:-}" != "--validate-only" ]]; then
  run_script "$SCRIPT_DIR/generate_joint_rig.py"
  run_script "$SCRIPT_DIR/finalize_joint_gui.py"
  run_script "$SCRIPT_DIR/generate_pose_study.py"
  run_script "$SCRIPT_DIR/finalize_pose_gui.py"
fi
run_script "$SCRIPT_DIR/validate_joint_rig.py"

echo "J1 FreeCAD artifact validation completed."

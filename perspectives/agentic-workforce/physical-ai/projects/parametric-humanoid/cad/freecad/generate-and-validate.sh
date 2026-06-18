#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
FREECADCMD="${FREECADCMD:-/Applications/FreeCAD.app/Contents/Resources/bin/freecadcmd}"

if [[ ! -x "$FREECADCMD" ]]; then
  echo "FreeCAD command runtime not found: $FREECADCMD" >&2
  echo "Set FREECADCMD to your FreeCAD command-line executable." >&2
  exit 1
fi

run_freecad_script() {
  local script_path="$1"
  "$FREECADCMD" -c "p=r'''$script_path'''; exec(compile(open(p).read(),p,'exec'),{'__file__':p,'__name__':'__main__'})"
}

if [[ "${1:-}" != "--validate-only" ]]; then
  run_freecad_script "$SCRIPT_DIR/generate_lamina_v4.py"
  run_freecad_script "$SCRIPT_DIR/generate_lamina_v5.py"
  run_freecad_script "$SCRIPT_DIR/finalize_gui_visibility.py"
fi
run_freecad_script "$SCRIPT_DIR/validate_generated.py"

echo "Lamina FreeCAD validation completed."

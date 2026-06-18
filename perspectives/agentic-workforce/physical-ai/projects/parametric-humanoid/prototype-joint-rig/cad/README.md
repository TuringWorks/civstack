# J1 CAD and Cutting Files

## Primary files

- `generated/Lamina-J1-Tendon-Joint-Rig.FCStd` — visible native FreeCAD assembly.
- `generated/Lamina-J1-Tendon-Joint-Rig.step` — neutral assembly interchange file.
- `generated/dxf/` — one laser-cut DXF per unique plywood part.
- `generate_joint_rig.py` — authoritative geometry generator.
- `finalize_joint_gui.py` — saves visible FreeCAD view providers and renders the preview.

## Material mapping

| Thickness | Parts |
|---|---|
| 12 mm | Base, upright ×2, swing-arm cheek ×2, motor plate, spacers |
| 6 mm | Bearing retainer ×4, sector outer ×2, sector groove ×1, capstan outer ×2, capstan groove ×1, fit coupon |

## Critical fabrication notes

- Measure actual sheet thickness and laser kerf before cutting production parts.
- The nominal 28.2 mm bearing pocket is intentionally a starting value; tune it using the supplied fit coupon.
- Do not force bearings into an incorrect wooden pocket. Split, clamp, or retain the bearing using bolted outer rings.
- Ream/drill shaft and fastener clearances only with an appropriate guarded tool and fixture if the laser result is unsuitable.
- Verify that the chosen motor shaft matches the capstan bore before cutting the final capstan.


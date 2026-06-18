# J1 CAD and Cutting Files

## Primary files

- `generated/Lamina-J1-Tendon-Joint-Rig.FCStd` — visible native FreeCAD assembly.
- `generated/Lamina-J1-Tendon-Joint-Rig.step` — neutral assembly interchange file.
- `generated/dxf/` — one laser-cut DXF per unique plywood part.
- `generate_joint_rig.py` — authoritative geometry generator.
- `finalize_joint_gui.py` — saves visible FreeCAD view providers and renders the preview.

## Material mapping

| Thickness | DXF | Quantity |
|---|---|---:|
| 12 mm | `base-12mm.dxf` | 1 |
| 12 mm | `upright-12mm.dxf` | 2 |
| 12 mm | `swing-arm-cheek-12mm.dxf` | 2 |
| 12 mm | `motor-plate-nema23-12mm.dxf` | 1 |
| 12 mm | `spacer-12mm.dxf` | 4 |
| 6 mm | `bearing-retainer-6mm.dxf` | 4 |
| 6 mm | `sector-outer-6mm.dxf` | 2 |
| 6 mm | `sector-groove-6mm.dxf` | 1 |
| 6 mm | `capstan-outer-6mm.dxf` | 2 |
| 6 mm | `capstan-groove-6mm.dxf` | 1 |
| 6 mm | `fit-coupon-6mm.dxf` | 1 |

Regenerate and validate everything with `./generate-and-validate.sh`.

## Critical fabrication notes

- Measure actual sheet thickness and laser kerf before cutting production parts.
- The nominal 28.2 mm bearing pocket is intentionally a starting value; tune it using the supplied fit coupon.
- Do not force bearings into an incorrect wooden pocket. Split, clamp, or retain the bearing using bolted outer rings.
- Ream/drill shaft and fastener clearances only with an appropriate guarded tool and fixture if the laser result is unsuitable.
- Verify that the chosen motor shaft matches the capstan bore before cutting the final capstan.

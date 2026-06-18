# Lamina FreeCAD Package

This is the primary CAD package for the latest Lamina design. It uses native FreeCAD documents and STEP exports rather than requiring OpenSCAD.

## Generated artifacts

Run `generate_lamina_v4.py` using FreeCAD's command-line runtime. It creates:

- `generated/Lamina-Slender-Biped-v4.FCStd` — master architecture model.
- `generated/Lamina-Slender-Biped-v4.step` — neutral-pose interchange export.
- `generated/Lamina-Hollow-Torsion-Link-v1.FCStd` and `.step`.
- `generated/Lamina-Adaptive-Gripper-v1.FCStd` and `.step`.
- `generated/Lamina-Rear-Safety-Module-v1.FCStd` and `.step`.
- `generated/Lamina-Torso-Rib-v1.FCStd` and `.step`.

## Open the latest robot

Open [generated/Lamina-Slender-Biped-v5.FCStd](generated/Lamina-Slender-Biped-v5.FCStd) in FreeCAD. This version is visually aligned to the latest open-truss concept render. The model tree separates:

- Laser-cut wooden structure
- Purchased joint hardware
- Actuator envelopes
- Tendon-routing envelopes
- Sensors and rubber contact surfaces
- Independent safety hardware
- Reference geometry

The rear shoulder-level E-stop and the independent overhead tether anchor are separate objects in the `Safety` group.

## Regenerate on macOS

From this folder, run the wrapper:

```bash
./generate-and-validate.sh
```

The generator is the editable parametric source. Design dimensions are grouped near the top of the generated FreeCAD document under `DesignParameters`, and the source dimensions live in `generate_lamina_v4.py`.

The wrapper regenerates all five `.FCStd` documents, adds explicit GUI visibility metadata, renders a smoke-test preview, exports STEP files, validates every solid, checks the master scale, and writes `generated/validation-report.txt`.

## Model maturity

This is **architecture CAD**, suitable for:

- Proportion and packaging studies
- Module decomposition
- FreeCAD navigation and visual review
- Preliminary clearances
- Establishing a native CAD baseline

It is not yet suitable for cutting a human-carrying or ladder-climbing robot. Joint loads, shaft diameters, bearing selection, tendon paths, plywood grain direction, fastener edge distances, fatigue, fall loads, motor sizing, collision envelopes, and tolerances still require engineering analysis and physical prototypes.

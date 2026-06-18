# CAD Files

## Primary workflow

- [FreeCAD package](freecad/README.md) — native master model and reusable v4 component documents for the latest slender biped.

## Available now

- [Parametric torso OpenSCAD source](parametric-torso.scad) — generates the original fixed-base torso rib stack in assembly, individual-layer, or sheet-layout mode.
- [DXF layer export script](export-layers.sh) — exports one DXF per torso layer when OpenSCAD is installed.

## Legacy OpenSCAD scope note

The OpenSCAD file is the **v0 torso generator**. It remains for reference, but FreeCAD is now the primary CAD workflow.

## Intended biped CAD package

The next CAD increment should contain:

1. Shared material, kerf, fastener, bearing, and shaft parameters.
2. Reusable torsion-box link generator.
3. Standard modular joint interface and replaceable cheek plates.
4. Hip, knee, ankle, shoulder, elbow, wrist, waist, and neck assemblies.
5. Adaptive three-finger gripper and tendon routing.
6. Pelvis and torso motor-bank layouts.
7. Rear shoulder-level E-stop plate and separate tether anchor.
8. Flat-sheet nesting and DXF export for each plywood thickness.
9. Assembly model with joint limits and collision clearances.

OpenSCAD was not installed in the current environment, so the existing torso source has been syntax-reviewed but not rendered or exported here.

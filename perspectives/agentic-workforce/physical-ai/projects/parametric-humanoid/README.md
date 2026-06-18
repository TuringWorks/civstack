# Parametric Humanoid — Build Package v0.1

This package turns the idea of an animated, sliced sculpture into a buildable robotics program. The working name is **Lamina**: a serviceable robot skeleton wearing a replaceable, laser-cut parametric body.

## Product thesis

The sculpture and robot should cooperate without pretending to be the same subsystem:

- **Skeleton:** carries loads, defines joint axes, hard stops, wiring, and service access.
- **Laminae:** create the visible body from plywood, acrylic, cardboard, or aluminum slices.
- **Reflex controller:** runs deterministic closed-loop motor control and safety.
- **Local brain:** interprets language, perceives the scene, and requests bounded motion skills.
- **Safety chain:** can remove actuator power without consulting either language model.

The primary mushroom E-stop is mounted on the fixed upper-back structure at shoulder height. It must be reachable from behind and from either side, remain clear of arm sweep and the fall-arrest tether, and never move with a decorative shell panel.

An LLM never produces torque, PWM, or arbitrary joint trajectories. It may request a named skill with typed parameters; a deterministic executive checks state, limits, collision rules, and authorization before motion.

## Recommended first machine

Build a **fixed-base upper torso with one 3-DOF arm and a 2-DOF head**, initially under 24 VDC and limited to slow, low-force movement. This proves the distinctive parts of the idea before taking on balance and fall safety.

| Attribute | v0 target |
|---|---|
| Form | Fixed-base torso, one arm, head |
| Height | 700–900 mm above base |
| Moving axes | Head yaw/pitch; shoulder pitch/roll; elbow flexion |
| Payload | Foam hand only; no grasping payload initially |
| Shell | 6 mm plywood ribs, 12–18 mm spacing |
| Control | Smart servos over RS-485 or CAN; MCU at 500–1,000 Hz |
| Brain | Linux computer on a separate process/power domain |
| Operating envelope | Bench-mounted, guarded, one trained operator |

## Artifacts

- [Concept and decisions](01-concept-and-decisions.md)
- [Control architecture](02-control-architecture.md)
- [Prototype build plan](03-prototype-build-plan.md)
- [Safety state machine](firmware/safety-state-machine.md)
- [Starter bill of materials](hardware/v0-bom.csv)
- [Slender biped v3 bill of materials](hardware/slender-biped-v3-bom.csv)
- [Motion-intent JSON Schema](interfaces/motion-intent.schema.json)
- [Valid example intents](interfaces/example-intents.jsonl)
- [Parametric torso CAD source](cad/parametric-torso.scad)
- [Layer export helper](cad/export-layers.sh)
- [Latest FreeCAD package](cad/freecad/README.md)
- [Concept image archive](images/README.md)

## Immediate use

1. Open `cad/parametric-torso.scad` in OpenSCAD and set `mode = "assembly"` to inspect proportions.
2. Set `mode = "layer"` and choose `layer_index` to inspect a laser-cut rib.
3. Run `cad/export-layers.sh` on a machine with OpenSCAD to generate one DXF per layer.
4. Cut five cheap cardboard layers first. Measure kerf and rod-hole fit before cutting plywood.
5. Build the actuator-and-link test rig from Phase 0 of the build plan before fabricating a complete body.

## Non-goals for v0

- Dynamic walking or untethered balance
- Human lifting, caregiving contact, or use near children
- Autonomous tool use
- LLM-generated low-level motion
- Hiding every mechanism; visible engineering is part of the aesthetic

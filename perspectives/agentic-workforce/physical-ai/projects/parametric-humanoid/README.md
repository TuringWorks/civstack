# Parametric Humanoid — Lamina pre-fabrication package v0.6

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

The current fabrication release begins even smaller: the J1 tendon-joint rig. The
full humanoid remains the target architecture, but cutting it is gated by measured
transmission, structural and lower-body evidence. See [project readiness](PROJECT-READINESS.md).

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

- [Project readiness and release gates](PROJECT-READINESS.md)
- [Engineering baseline index](engineering/README.md)
- [Engineering workbook](engineering/Lamina-Engineering-Baseline-v06.xlsx)
- [System requirements](engineering/system-requirements.md)
- [Hardware gates](engineering/hardware-gates.md)
- [Concept and decisions](01-concept-and-decisions.md)
- [Control architecture](02-control-architecture.md)
- [Full-body deterministic control](control/full-body-control.md)
- [Stair and ladder state machines](control/stair-and-ladder-state-machines.md)
- [Power and network architecture](electronics/power-and-network.md)
- [Prototype build plan](03-prototype-build-plan.md)
- [Safety state machine](firmware/safety-state-machine.md)
- [Safety case](safety/safety-case.md)
- [Hazard register](safety/hazard-register.csv)
- [Verification matrix](verification/verification-matrix.csv)
- [Fabrication standard](manufacturing/fabrication-standard.md)
- [Assembly sequence](manufacturing/assembly-sequence.md)
- [Procurement plan](procurement/procurement-plan.md)
- [Commissioning and operations](operations/commissioning-and-operations.md)
- [Configuration management](operations/configuration-management.md)
- [AI/control threat model](security/threat-model.md)
- [Starter bill of materials](hardware/v0-bom.csv)
- [Slender biped v3 bill of materials](hardware/slender-biped-v3-bom.csv)
- [Motion-intent JSON Schema](interfaces/motion-intent.schema.json)
- [Valid example intents](interfaces/example-intents.jsonl)
- [Parametric torso CAD source](cad/parametric-torso.scad)
- [Layer export helper](cad/export-layers.sh)
- [Latest FreeCAD package](cad/freecad/README.md)
- [Concept image archive](images/README.md)
- [Phase-0 single-joint prototype package](prototype-joint-rig/README.md)
- [31-axis simulation model](simulation/README.md)

## Immediate use

1. Run `./validate-project.sh`.
2. Open the FreeCAD v5 assembly and engineering workbook for the frozen baseline.
3. Procure Phase A only and cut the J1 fit coupon.
4. Build and accept the J1 rig before fabricating a complete body.

## Non-goals for v0

- Dynamic walking or untethered balance
- Human lifting, caregiving contact, or use near children
- Autonomous tool use
- LLM-generated low-level motion
- Hiding every mechanism; visible engineering is part of the aesthetic

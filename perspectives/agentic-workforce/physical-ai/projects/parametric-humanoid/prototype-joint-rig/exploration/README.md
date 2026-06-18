# J1 Engineering Exploration

This folder tracks questions that must be resolved experimentally before the joint architecture is propagated through the humanoid.

## Current studies

- [Actuation architecture trade study](actuation-options.md)
- [Joint sizing table](joint-sizing.csv)
- [Tendon termination experiment](tendon-termination-test.md)
- FreeCAD pose study in `../cad/generated/Lamina-J1-Pose-Study.FCStd`

## Working recommendation

Begin with one proximal motor and two opposing tendons on a shared capstan, with independent tension adjustment and an output-shaft encoder. It is the best first experiment because it preserves bidirectional control while using one actuator. Do not freeze it for the full robot until backlash, tendon creep, termination strength, and capstan tracking have been measured.

## Questions the first rig must answer

1. Does the opposing-tendon capstan maintain tension through the entire −10° to 110° range?
2. How much output backlash comes from wood, tendon stretch, termination slip, and motor reduction?
3. Can the laminated sector survive 22 N·m proof torque without permanent set?
4. What motor/reduction combination meets torque and duty-cycle requirements without excessive mass or noise?
5. Can a tendon be replaced and retensioned in under ten minutes?
6. How much does humidity change zero position and preload?


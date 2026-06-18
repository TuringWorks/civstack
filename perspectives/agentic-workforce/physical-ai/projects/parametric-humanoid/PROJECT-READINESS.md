# Lamina v0.6 pre-fabrication readiness

## Decision

Proceed with a staged prototype program. Do **not** cut a complete humanoid yet.
The best path is to retire the highest-risk mechanisms in this order:

1. J1 antagonistic tendon transmission and termination coupons.
2. One load-bearing class-H joint with the intended plywood layup.
3. Instrumented leg on a fixed test frame.
4. Tethered two-leg lower body, then slow level walking and stairs.
5. Upper body and adaptive gripper.
6. Ladder work only after all earlier gates pass and a separate safety review approves it.

This keeps the architecture inexpensive and rapidly changeable while preventing a
full-body build from multiplying an unproven joint or tendon defect 31 times.

## Frozen baseline

| Item | Baseline |
|---|---|
| Release | v0.6, pre-fabrication engineering baseline |
| Stature | 1500 ±50 mm |
| Axes | 31 commanded joints |
| Construction | laser-cut plywood primary structure; purchased metal only for bearings, shafts, fasteners, motors and safety hardware |
| Mass | 34.4 kg planning estimate; 32 kg target; mandatory review at 35 kg |
| Payload | 5 kg close to torso; 2 kg floor pickup |
| Power | 48 V actuator bus; 695 W average estimate; 4.23 kW short peak envelope |
| Battery | planning basis 48 V, 15 Ah; final pack waits for measured duty cycle |
| Control | deterministic MCU reflex loops; typed skills from local computer; no LLM torque/PWM access |
| Safety | hardwired rear shoulder E-stop, contactor/enable chain, tethered development, exclusion zone |
| Mobility | slow guarded level walking and stairs are requirements; ladder climbing is conditional research scope |

## Evidence available now

- FreeCAD v5 full-body assembly, reusable component models and STEP exports.
- A fabrication-oriented J1 tendon-joint rig with 11 DXF profiles, BOM, wiring,
  firmware interface, pose study and acceptance test.
- A 31-axis URDF and machine-readable joint map.
- Requirements, joint classes, mass/load/power/cost budgets and a consolidated workbook.
- Power/network and full-body control architecture, stair and ladder state machines.
- Safety case, 22-item hazard register and 32-item verification matrix.
- Fabrication, assembly, quality, maintenance, commissioning and configuration procedures.

## Claims not yet earned

No document or render demonstrates that the robot can walk, climb, lift its rated
payload, survive a fall, or stop within a safe distance. Those claims require the
hardware gates in `engineering/hardware-gates.md`. The project is complete as a
**pre-fabrication package**, not as a validated robot.

## Release gates

- **Release J1 cutting:** project validator passes; drawings reviewed; operator and E-stop available.
- **Release one class-H joint:** J1 efficiency, backlash, thermal and endurance gates pass.
- **Release lower body:** class-H proof load and stop tests pass; fall-arrest rig commissioned.
- **Release full body:** lower-body standing, fault injection, thermal and stair gates pass.
- **Release ladder trials:** separate ladder fixture, dual fall arrest and safety review pass.

## Start here

1. Run `./validate-project.sh`. Use `--deep-freecad` in a terminal where FreeCAD's
   command runtime is compatible to reopen and recompute the geometry.
2. Review `engineering/Lamina-Engineering-Baseline-v06.xlsx`.
3. Procure only Phase A in `procurement/procurement-plan.md`.
4. Cut the J1 fit coupon before any structural part.
5. Execute `prototype-joint-rig/tests/acceptance-test.md` and record measured evidence.

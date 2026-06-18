# Prototype Build Plan

The plan advances by evidence gates. Do not buy a body-sized set of actuators before the single-joint rig establishes torque, temperature, backlash, noise, and bus behavior.

## Phase 0 — Joint and lamination coupon

Build one elbow-like link on a bench and five representative laser-cut ribs.

Deliverables:

- One actuator, two bearings, hard stops, 250–350 mm link, adjustable mass
- Physical E-stop that removes drive enable
- Encoder/current/temperature telemetry plot
- Kerf and hole-fit coupon for chosen plywood
- Rib attachment that can be removed in under five minutes

Pass gate:

- 500 slow cycles without loosening or cable damage
- Motor stays below its rated thermal limit with the intended duty cycle
- Command timeout and unplugged-brain tests produce a safe stop
- Pinch points are guarded or excluded

## Phase 1 — Passive full-scale sculpture

Build the torso, head, and one arm with unpowered articulating joints. Use the CAD generator as a starting point, then derive separate shells from actual joint geometry.

Pass gate:

- Full desired range of motion without rib collision
- Shell modules removable without disturbing joint alignment
- Machine remains stable under worst-case arm extension plus an added test margin
- All service points reachable

## Phase 2 — Powered fixed-base puppet

Install five actuated axes: head yaw/pitch, shoulder pitch/roll, elbow flexion. Use teach pendant or scripted motion only.

Pass gate:

- Homing, limits, watchdog, E-stop, and safe-stop are verified axis by axis
- Reviewed gesture library runs repeatedly inside a marked exclusion zone
- Event log can reconstruct every stop and fault
- Noise and motion quality are acceptable for the intended artistic setting

## Phase 3 — Perception-directed skills

Add target tracking and bounded primitives such as `look_at` and `point_at`. Use simple deterministic target selection before adding language.

Pass gate:

- Robot stops on target uncertainty or person entry into the arm envelope
- False target and sensor-loss tests never create arbitrary motion
- Target coordinates are transformed and range-checked before trajectory generation

## Phase 4 — Local language brain

Add speech/text interpretation that emits only the typed motion-intent contract. Begin with a tiny allowlist of phrases and skills, then measure ambiguity and refusal behavior.

Pass gate:

- Prompt injection, malformed JSON, conflicting commands, stale commands, and unknown skills are rejected
- The system asks for clarification when target or intent is ambiguous
- Killing or rebooting the language process causes no unsafe behavior
- A human can always preempt motion

## Phase 5 — Mobility decision

Choose among remaining fixed-base, adding a wheeled pedestal, or beginning a separate leg research program. Walking is a new safety program, not a feature toggle.

## First two-week sprint

1. Freeze v0 dimensions and one-arm range of motion.
2. Choose an actuator family only for the joint test rig.
3. Fabricate kerf coupons and five torso ribs in cardboard, then plywood.
4. Assemble E-stop, fused DC supply, drive-enable relay, and one actuator.
5. Implement heartbeat timeout and telemetry capture.
6. Run static torque and 500-cycle thermal tests.
7. Record measured values in the BOM and revise the body around real swept volumes.

## Test matrix

| Test | Method | Expected result |
|---|---|---|
| E-stop | Press during slow motion | Drive power removed; brakes/fallback behave as designed |
| Brain loss | Kill brain process / disconnect cable | Controlled stop before watchdog deadline |
| Bus loss | Disconnect actuator network | Fault latched; no restart without operator reset |
| Overtravel request | Request outside skill bounds | Rejected before setpoint generation |
| Obstruction | Use compliant test fixture, not a person | Effort threshold stops/retreats as configured |
| Thermal | Worst planned pose and duty cycle | Temperature remains within derated limit |
| Shell collision | Sweep all joints slowly | No contact; clearance documented |
| Stale intent | Delay beyond `expires_at` | Rejected |
| Unknown skill | Send schema-invalid name | Rejected and logged |


# System Requirements v0.6

## Mission

Lamina is a low-cost, locally repairable humanoid research platform whose primary structural and aesthetic parts are laser-cut plywood. It should eventually perform indoor manipulation, floor pickup, guarded walking, stair ascent, and tethered ladder-climbing research without custom metal machining.

## Physical envelope

| Requirement | Target |
|---|---|
| Standing height | 1500 ±50 mm |
| Total mass | Target ≤32 kg; hard design review at 35 kg |
| Shoulder width | ≤500 mm |
| Base standing footprint | ≤450 × 350 mm including feet |
| Controlled axes | 31 |
| Primary structural sheet | 12 mm void-free plywood |
| Secondary/rib sheet | 6 mm void-free plywood |
| Custom metal machining | None |

## Functional requirements

- Carry 5 kg using both arms with the payload against the torso on level ground.
- Pick up a 2 kg object from floor height using a squat, with overhead fall arrest during development.
- Reach a 1200 mm shelf while maintaining a statically stable support condition.
- Walk at an initial guarded speed of 0.15 m/s; aspirational mature speed 0.4 m/s.
- Step over a 50 mm obstacle during guarded development.
- Ascend a test stair with rise ≤180 mm and tread ≥280 mm at no more than one step per 10 seconds initially.
- Interface with ladder rungs 25–35 mm in diameter and 250–350 mm apart on a controlled test fixture.
- Ladder testing requires positive hook-like grip geometry and an independent overhead fall-arrest system.
- Recover to a safe kneeling or supported pose after a protective stop where mechanically possible.

## Manipulation requirements

- Two 6-axis arms plus one underactuated gripper axis per hand.
- Adaptive three-finger hands with soft contact pads.
- Wrist and elbow structures removable without opening torso motor banks.
- Two-hand carry modes use forearm/palm structural cradles rather than fingertip friction alone.
- A mechanical rung hook carries ladder load if grip power is lost.

## Runtime and power

- 48 V nominal battery domain with protected branch distribution.
- Minimum initial useful runtime: 30 minutes mixed development duty.
- Battery and BMS are purchased certified assemblies; no experimental cell pack construction.
- Stored-energy isolation, precharge, branch fusing, current monitoring, and accessible service disconnect are required.

## Operating design domain

- Indoor laboratory or controlled workshop only.
- Dry level floors for initial walking.
- No rain, dust, public spaces, children, patients, crowds, traffic, or animals.
- One trained operator, one safety observer, physical exclusion zone, and overhead fall arrest for standing mobility.
- No unsupervised charging, tool use, human lifting, or autonomous ladder operation.

## Safety requirements

- Rear shoulder-level latching E-stop reachable from behind and either side.
- Operator-held commissioning pendant with hold-to-run control.
- Independent drive-enable removal; software and language models cannot override it.
- Output-side sensing for load-bearing joints.
- Mechanical hard stops, software limits, stale-command timeouts, and thermal/current/force limits.
- Black-box logging sufficient to reconstruct commands, state, faults, interventions, and configuration.

## Cost requirement

Planning target for the research prototype is ≤USD 12,000 in robot-specific purchased parts, excluding laser cutter, shop tools, safety gantry, engineering labor, test instrumentation, and damaged prototypes. A formal redesign review is required if the estimated robot-specific BOM exceeds USD 20,000.

These are planning thresholds, not supplier quotations.


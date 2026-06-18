# Embodied reference build — "Lamina" parametric humanoid

CivStack describes the LLM-brained robot architecture abstractly (brain → actions as tool
calls → VLA/control → a **verified deterministic safety layer** beneath anything learned).
The Agentic-Workforce viewpoint now ships a concrete, buildable instance of exactly that
architecture — **Lamina**, a parametric humanoid build package. This doc absorbs its
architectural lessons; the full package — now a complete engineering program (system
requirements, design decisions, mass/power/cost/joint-load budgets, hardware gates, a
claim-based safety case + hazard register, a security threat model, full-body & stair/ladder
control, FreeCAD/OpenSCAD generators, URDF/simulation, manufacturing/QA, procurement,
commissioning, configuration management, verification, maintenance, and a J1 joint-rig with
acceptance tests) — lives in
[`../perspectives/agentic-workforce/physical-ai/projects/parametric-humanoid/`](../perspectives/agentic-workforce/physical-ai/projects/parametric-humanoid/).

It matters because it turns CivStack's most-repeated safety claim — *the safety layer can
refuse or override the LLM brain independently* — from an assertion into an implementation
contract you can build on a bench.

## The one-line principle

> **Language proposes; deterministic software disposes.** No probabilistic model is trusted
> with torque, PWM, drive-enable, safety reset, limit configuration, or arbitrary code
> execution. An LLM may *request* a named skill with typed parameters; a deterministic
> executive checks state, limits, collision rules, and authorization before any motion.

This is precisely CivStack's "brain issues actions as tool calls; a verified low-level safety
layer validates, refuses, or overrides them."

## Layered control stack (maps 1:1 to the CivStack robot model)

| Lamina layer | Rate | May stop motion? | CivStack equivalent |
|---|---|---|---|
| Electrical safety chain (E-stop, contactor, STO, interlock) | continuous | **Yes, independently** | the verified safety layer / hardware override |
| Motor/joint firmware (encoder, limits, current/temp, watchdog) | 500–1,000 Hz | Yes | low-level control / VLA execution envelope |
| Skill & trajectory controller (bounded setpoints) | 100–250 Hz | Yes | the motor-primitive executor |
| Task executive (skill sequencing, resource locks, state validation) | 10–30 Hz | Yes | the tool-call validator / control layer |
| Perception / world model (people, obstacles, uncertainty) | 5–30 Hz | Requests stop | world model + perception |
| Local language brain (interpret, clarify, plan named skills) | event-driven | **Requests only** | the LLM brain (System-2 planner) |

The brain can only *request*; everything below it can *stop*. That inversion of authority is
the whole safety idea.

## Actions as tool calls — the `MotionIntent` schema

The brain emits a typed, validated, **expiring** `MotionIntent` (JSON Schema), not torque:

- `skill` is an **enum** (`home`, `hold`, `look_at`, `gesture`, `point_at`, `safe_stop`) — a
  bounded vocabulary of motor primitives, exactly CivStack's `grasp`/`navigate_to`/… tool calls.
- It carries `priority`, `expected_mode` (`SAFE_IDLE`/`RUN`), typed `parameters`, `constraints`,
  and an `expires_at` so stale intents cannot fire.
- A **policy gateway** accepts or rejects each intent before the deterministic executive runs it.

This is the cleanest possible demonstration that "actions are tool calls" is implementable and
safe: the action space is a typed, checkable contract, not free-form model output.

## The verified safety state machine

A nine-state machine (`POWER_OFF → SELF_TEST → SAFE_IDLE → HOMING → RUN → PROTECTIVE_STOP →
EMERGENCY_STOP → FAULT_LOCKOUT → MAINTENANCE`) with mandatory transitions independent of any
model: any state → `EMERGENCY_STOP` when the safety chain opens; energized → `PROTECTIVE_STOP`
on heartbeat loss, unsafe perception, joint fault, command conflict, or workspace violation;
and — critically — `EMERGENCY_STOP` never transitions directly to `RUN`. This *is* the
"minimal-risk maneuver the safety layer can trigger independently of the brain."

## Evidence-gated build phasing (mirrors capability routing)

The build advances only through evidence gates — Phase 0 is a single **joint-and-lamination
coupon** (one actuator, hard stops, E-stop, telemetry) that must pass 500 slow cycles, thermal
limits, and command-timeout/unplugged-brain safe-stop tests *before* a body-sized actuator set
is purchased. This is CivStack's capability-routing discipline in physical form: prove the
deterministic, safety-critical loop first; add learned/LLM behavior only above a verified base.

## Which CivStack roles this instantiates

- `_catalogs/embodied-ai-stack/`: **robot brain orchestrator** (emits MotionIntents), **VLA
  policy engineer**, **world-model engineer**, **robot fleet safety officer** (owns the safety
  chain & state machine), **teleoperation/handoff operator**.
- `_catalogs/capability-optimization/`: **deterministic control & classical-optimization
  engineer** (the firmware/skill controllers) and **formal verification & assurance engineer**
  (the safety state machine).
- `_catalogs/humanoid-robots/` + sector `robots/`: the physical role the platform fills.

## Safety case & security threat model (the strongest absorption)

The package now carries a **claim-based preliminary safety case** and a **control/AI threat
model** that, together, are the most precise statement of CivStack's core safety principle.

- **Safety case, claim S1 — "actuation can be made safe *independently of intelligent
  software*":** a latching E-stop opens an independent drive-enable chain; a hold-to-run
  pendant; contactors that report actual state; stale-setpoint/heartbeat-loss → protective
  stop; and — verbatim — *"language and planning processes cannot reset faults or energize
  drives directly."* Claim S2 controls fall consequences during mobility (rated fall arrest,
  exclusion zones) — evidence-gated, not assumed.
- **Threat model trust boundary:** the safety MCU and actuator network are trusted only for
  bounded deterministic control; *"the local AI computer, language model, microphone, camera
  and any external network are **untrusted** request sources. Safety does not depend on their
  correctness."* This is the sharpest possible framing of CivStack's verified-safety-layer
  rule and its autonomous-machine failure modes (physical-world prompt injection, spoofing).
- **Hardened "actions as tool calls":** allowlisted, typed motion skills with range/rate/
  workspace/deadline checks; **no shell, torque, PWM, or raw trajectory exposed to an LLM**;
  replay/stale-command rejection with monotonic command IDs and watchdogs; physical enable and
  hardwired E-stop override every software state; default-deny remote access; append-only logs
  recording command source and rejection reason. (A second typed schema, `joint-command`, sits
  below `MotionIntent` — a two-tier tool-call contract.)

## Staged readiness — capability routing in hardware

The program's pre-fabrication decision is explicit: *do not cut a complete humanoid yet.*
Retire the highest-risk mechanisms in order (tendon transmission coupon → one load-bearing
joint → instrumented leg → tethered lower body → walking/stairs → upper body → ladder work,
each behind a gate), because a full-body build would *"multiply an unproven joint or tendon
defect 31 times."* That is CivStack's capability-routing and sim-to-real discipline stated as
program management: prove the deterministic, safety-critical unit before scaling, and reserve
learned/LLM behavior for above a verified base. The engineering side backs it with quantified
**mass / power / cost / joint-load budgets**, **hardware gates**, a **hazard register**, and
URDF/**simulation** generation (the world-model / robot-gym layer) — a complete lifecycle from
system requirements through manufacturing, procurement, commissioning, verification, and
maintenance/configuration management.

## The takeaway

Lamina is the existence proof for CivStack's safety model: a bounded, typed action interface; a
control stack where authority to *stop* runs opposite to authority to *plan*; a verified state
machine the brain cannot bypass; and evidence-gated bring-up. When a CivStack robot or
autonomous-machine skill says "a verified safety layer can override the brain," this is what
that looks like in hardware.

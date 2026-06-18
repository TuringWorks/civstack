# Embodied reference build — "Lamina" parametric humanoid

CivStack describes the LLM-brained robot architecture abstractly (brain → actions as tool
calls → VLA/control → a **verified deterministic safety layer** beneath anything learned).
The Agentic-Workforce viewpoint now ships a concrete, buildable instance of exactly that
architecture — **Lamina**, a parametric humanoid build package. This doc absorbs its
architectural lessons; the full package (build docs, FreeCAD/OpenSCAD generators, BOMs,
firmware contracts, a J1 joint-rig with acceptance tests) lives in
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

## The takeaway

Lamina is the existence proof for CivStack's safety model: a bounded, typed action interface; a
control stack where authority to *stop* runs opposite to authority to *plan*; a verified state
machine the brain cannot bypass; and evidence-gated bring-up. When a CivStack robot or
autonomous-machine skill says "a verified safety layer can override the brain," this is what
that looks like in hardware.

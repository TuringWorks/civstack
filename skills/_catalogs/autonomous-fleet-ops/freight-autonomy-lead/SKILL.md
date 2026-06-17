---
name: "fleetops-freight-autonomy-lead"
description: "Autonomous-fleet operations role: **Freight autonomy lead** (Human oversight role (accountability boundary)) — coordinates autonomous trucks, yard tractors, delivery vehicles, warehouse AMRs, forklifts, and port equipment across autonomous logistics networks. Part of the operations layer that runs non-humanoid autonomous machines (self-driving vehicles, farm equipment, loaders, drones). Use this skill when deploying, supervising, certifying, or scaling an autonomous fleet, even if the user only describes the underlying need. Works under a fleet operations director."
---

# Autonomous-Fleet Ops — Freight autonomy lead

> **Layer:** Autonomous-fleet operations (runs non-humanoid autonomous machines) · **Type:** Human oversight role (accountability boundary)
> **Human supervisor:** fleet operations director · **Machines:** `../../autonomous-machines/` · **Shared concepts:** `../../../00-framework/SKILL.md`

## What this role is

The **Freight autonomy lead** coordinates autonomous trucks, yard tractors, delivery vehicles, warehouse AMRs, forklifts, and port equipment across autonomous logistics networks. Owns the autonomy program for freight and logistics; balances throughput, cost, safety, and labor, and owns the safety case for public-road and facility operation.

## Where it sits

The assumed machine architecture is: a foundation/LLM **planning brain** issuing **actions as tool calls** over a perception → prediction → planning → control stack trained on **world models**, **simulation**, and **RLAIF**, running inside a defined **Operational Design Domain (ODD)** with a verified safe-stop and **teleoperation** fallback. This role owns the part of *operating* that fleet described above. It complements the build-side roles in `_catalogs/embodied-ai-stack/`.

## When to use this skill

Use it when a task calls for this work: coordinates autonomous trucks, yard tractors, delivery vehicles, warehouse AMRs, forklifts, and port equipment across autonomous logistics networks. Pair with `_catalogs/autonomous-machines/` (the platforms) and any operating-system skill (01–23) whose fleet this supports.

## Assumed architecture (recap)

These are **non-humanoid autonomous machines** — vehicles and equipment that drive, fly, or operate themselves. They share the project's brain-and-tool-calls model, adapted for mobility and heavy equipment:

- **Cognitive core (the autonomy "brain").** A foundation/LLM-based planner handles mission-level reasoning, natural-language tasking, and long-tail edge cases, sitting over a perception → prediction → planning → control autonomy stack. The brain decides *what and where*; learned and classical controllers execute *how* at high frequency. A fleet may share one model or specialize by platform.
- **Actions are tool calls.** The machine exposes actuation primitives as tools — e.g. `follow_route`, `set_speed`, `change_lane`, `lower_header`, `dump_bucket`, `take_off`, `survey_area`, `spray_zone`, `return_to_base` — which the brain invokes and low-level controllers carry out.
- **Trained on world models + simulation.** Planners and policies are trained against **world models** (learned simulators that predict vehicle dynamics, terrain, weather, and the behavior of other agents) and large-scale **driving/field simulation (robot gyms)**, then transferred to hardware with fleet data and imitation learning.
- **Many training paths (RLAIF is one).** Behavior is learned through imitation from human driving, model-based and offline RL, sim-to-real, and RLHF/RLAIF, then distilled into the SLMs and tiny models that run on-vehicle — with deterministic planners and controllers (MPC, search) for the safety-critical loop. The autonomy brain is right-sized per function; see `_catalogs/capability-optimization/`.
- **ODD + safety case.** Each machine operates inside a defined **Operational Design Domain** (the geography, weather, speed, crop, or site it is certified for) and a documented safety case, rated on the **SAE levels of automation** (L0–L5) for road vehicles or equivalent for off-road and aerial platforms. A **verified safety layer** can trigger a **minimal-risk maneuver** (controlled safe-stop / return-to-base / hover) independently of the planning brain.
- **Teleoperation fallback.** A remote operator supervises and takes over for situations outside the ODD or below a confidence threshold.

**Operating implication:** physical-world failures are high-consequence, so the safety layer, ODD boundary, and teleop fallback are mandatory and independent of the planning brain. Public-road and airspace operation additionally require regulatory authorization (e.g. SAE-level / FMVSS treatment for road vehicles; FAA Part 107 and BVLOS waivers for drones).

## Responsibilities

- Deliver this role's core job: coordinates autonomous trucks, yard tractors, delivery vehicles, warehouse AMRs, forklifts, and port equipment across autonomous logistics networks.
- Keep the fleet inside its ODD and safety case; treat the safety layer as authoritative over the brain.
- Maintain auditable evidence (maps, calibration, disengagements, approvals) for regulators and incident review.

## Decision rights & accountability

- **Owns and is accountable for** the safety case, ODD boundary, regulatory authorization, and stop authority.
- **Cannot delegate** these to the autonomy brain; the safety layer and ODD are independent of it.
- **Escalates** unresolved safety or compliance risk and can ground or halt the fleet.

## Failure modes and safeguards

- **Long-tail / edge cases** — rare scenarios the planner mishandles. Mitigation: conservative ODD, teleop fallback, continuous scenario mining.
- **ODD exit** — conditions drift outside the certified domain (weather, dust, lighting, unmapped area). Mitigation: detect-and-degrade to a minimal-risk maneuver.
- **Sensor degradation / spoofing** — rain, dust, glare, GPS jamming, adversarial markings. Mitigation: sensor fusion, redundancy, anti-spoofing, conservative fallback.
- **Sim-to-real gap** — world-model/simulation training diverges from reality. Mitigation: shadow mode, staged deployment, real-world validation.
- **Mixed-traffic / human interaction** — misreading pedestrians, livestock, ground crew, or other drivers. Mitigation: predictable behavior, low-speed zones, explicit right-of-way rules.
- **Teleop latency / link loss** — remote takeover delayed or lost. Mitigation: onboard safe-stop, bounded autonomy, comms redundancy.
- **Fleet model-monoculture** — a shared brain fails in lockstep. Mitigation: model diversity, staged rollout, geofencing.

## Adapting to any nation (context modifiers)

Fleet ownership, road/airspace regulation, connectivity, and mapping coverage vary widely; in low-infrastructure settings on-board autonomy and safe-stop matter more than teleoperation and V2X. Re-read through:

- **Scale** (city-state → federation): whether this role is unified or layered across local/regional/national tiers.
- **State capacity** (fragile → high-capacity): whether the owning institution exists and can be held to account, or the job is met by markets, households, NGOs, or donors.
- **Income level** (low → high): affordability of automation and the balance of subsistence vs. wage work.
- **Formality** (informal → formal): whether the people and assets this role acts on appear in any registry at all.
- **Resource & geography**: which hazards and dependencies dominate (water-scarce, flood-prone, landlocked, trade-dependent).
- **Political system & legitimacy**: where the human-accountability boundary actually binds and who may hold power to account.

## Operating procedure

1. Confirm the ODD, safety case, and regulatory authorization for the work.
2. Run the role's core job, keeping the safety layer and ODD authoritative over the brain.
3. Monitor health, confidence, and disengagements; escalate ODD or safety changes to humans.
4. Maintain the audit trail; feed incidents and disengagements back into the stack.

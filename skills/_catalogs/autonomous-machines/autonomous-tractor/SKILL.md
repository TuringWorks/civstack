---
name: machine-autonomous-tractor
description: Non-humanoid autonomous machine: **Autonomous tractor** — till, plant, cultivate, and tow implements across fields with no operator in the seat. Best in: row-crop and broadacre farms. A self-driving/self-operating platform whose planning brain issues physical actions as tool calls over a perception-to-control stack (trained on world models, simulation, and RLAIF) inside a defined ODD with teleoperation fallback. Use this skill to plan or operate the platform anywhere this physical job is needed, even if the user only describes the underlying need.
---

# Autonomous Machine — Autonomous tractor

> **Layer:** Non-humanoid autonomous machine (cross-economy) · **Best environments:** row-crop and broadacre farms
> **Operated by:** `../../embodied-ai-stack/` roles (autonomy, fleet ops, teleoperation, safety) · **Shared concepts:** `../../../00-framework/SKILL.md`

## Primary job to be done

Till, plant, cultivate, and tow implements across fields with no operator in the seat.

## What it is

A GPS/RTK-guided autonomous tractor running implements to a field plan, supervised remotely.

## When to use this skill

When a task needs the physical job "till, plant, cultivate, and tow implements across fields with no operator in the seat" in environments such as row-crop and broadacre farms. Pair with the relevant operating-system skill (01–22) for domain rules and the human accountability boundary, and with `_catalogs/embodied-ai-stack/` for the roles that build, operate, and keep it safe.

## Cognitive and control architecture (assumed)

These are **non-humanoid autonomous machines** — vehicles and equipment that drive, fly, or operate themselves. They share the project's brain-and-tool-calls model, adapted for mobility and heavy equipment:

- **Cognitive core (the autonomy "brain").** A foundation/LLM-based planner handles mission-level reasoning, natural-language tasking, and long-tail edge cases, sitting over a perception → prediction → planning → control autonomy stack. The brain decides *what and where*; learned and classical controllers execute *how* at high frequency. A fleet may share one model or specialize by platform.
- **Actions are tool calls.** The machine exposes actuation primitives as tools — e.g. `follow_route`, `set_speed`, `change_lane`, `lower_header`, `dump_bucket`, `take_off`, `survey_area`, `spray_zone`, `return_to_base` — which the brain invokes and low-level controllers carry out.
- **Trained on world models + simulation.** Planners and policies are trained against **world models** (learned simulators that predict vehicle dynamics, terrain, weather, and the behavior of other agents) and large-scale **driving/field simulation (robot gyms)**, then transferred to hardware with fleet data and imitation learning.
- **Many training paths (RLAIF is one).** Behavior is learned through imitation from human driving, model-based and offline RL, sim-to-real, and RLHF/RLAIF, then distilled into the SLMs and tiny models that run on-vehicle — with deterministic planners and controllers (MPC, search) for the safety-critical loop. The autonomy brain is right-sized per function; see `_catalogs/capability-optimization/`.
- **ODD + safety case.** Each machine operates inside a defined **Operational Design Domain** (the geography, weather, speed, crop, or site it is certified for) and a documented safety case, rated on the **SAE levels of automation** (L0–L5) for road vehicles or equivalent for off-road and aerial platforms. A **verified safety layer** can trigger a **minimal-risk maneuver** (controlled safe-stop / return-to-base / hover) independently of the planning brain.
- **Teleoperation fallback.** A remote operator supervises and takes over for situations outside the ODD or below a confidence threshold.

**Operating implication:** physical-world failures are high-consequence, so the safety layer, ODD boundary, and teleop fallback are mandatory and independent of the planning brain. Public-road and airspace operation additionally require regulatory authorization (e.g. SAE-level / FMVSS treatment for road vehicles; FAA Part 107 and BVLOS waivers for drones).

## Division of labor and safety

- **Human owner / fleet operator** — owns the safety case, the ODD, and stop authority; accountable for incidents.
- **Autonomy brain** — perceives, predicts, plans, and issues actuation as tool calls within the ODD.
- **Low-level controllers** — execute motion/actuation at high frequency.
- **Verified safety layer** — triggers a minimal-risk maneuver (safe-stop / return-to-base / hover) independently of the brain.
- **Remote operator (teleop)** — supervises and takes over beyond the ODD or below a confidence threshold.

## Architecture-specific failure modes

- **Long-tail / edge cases** — rare scenarios the planner mishandles. Mitigation: conservative ODD, teleop fallback, continuous scenario mining.
- **ODD exit** — conditions drift outside the certified domain (weather, dust, lighting, unmapped area). Mitigation: detect-and-degrade to a minimal-risk maneuver.
- **Sensor degradation / spoofing** — rain, dust, glare, GPS jamming, adversarial markings. Mitigation: sensor fusion, redundancy, anti-spoofing, conservative fallback.
- **Sim-to-real gap** — world-model/simulation training diverges from reality. Mitigation: shadow mode, staged deployment, real-world validation.
- **Mixed-traffic / human interaction** — misreading pedestrians, livestock, ground crew, or other drivers. Mitigation: predictable behavior, low-speed zones, explicit right-of-way rules.
- **Teleop latency / link loss** — remote takeover delayed or lost. Mitigation: onboard safe-stop, bounded autonomy, comms redundancy.
- **Fleet model-monoculture** — a shared brain fails in lockstep. Mitigation: model diversity, staged rollout, geofencing.

## Adapting to any nation (context modifiers)

Ownership ranges from fleet-as-a-service to cooperatively shared or rented machines; regulation (road approval, airspace/BVLOS, mine/site rules) and infrastructure (maps, connectivity, GPS/RTK) gate where it can run. In low-connectivity settings, on-board autonomy and safe-stop matter more than teleop. Re-read through:

- **Scale** (city-state → federation): whether this role is unified or layered across local/regional/national tiers.
- **State capacity** (fragile → high-capacity): whether the owning institution exists and can be held to account, or the job is met by markets, households, NGOs, or donors.
- **Income level** (low → high): affordability of automation and the balance of subsistence vs. wage work.
- **Formality** (informal → formal): whether the people and assets this role acts on appear in any registry at all.
- **Resource & geography**: which hazards and dependencies dominate (water-scarce, flood-prone, landlocked, trade-dependent).
- **Political system & legitimacy**: where the human-accountability boundary actually binds and who may hold power to account.

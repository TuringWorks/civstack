---
name: machine-10-site-survey-progress-drone
description: Non-humanoid autonomous machine for the Shelter operating system: **Site survey & progress drone** — map the site, track earthwork volumes, and monitor progress and safety from the air. Best in: active construction sites. A self-driving/self-operating platform whose planning brain issues physical actions as tool calls (perception-to-control trained on world models, simulation, and RLAIF) inside a defined ODD with teleoperation fallback. Use this skill to plan or operate the platform; trigger whenever this physical work is needed, even if only described.
---

# Site survey & progress drone

> **Operating system:** 10. Shelter, Construction, Land, and the Built Environment · **Personnel type:** Non-humanoid autonomous machine
> **Best environments:** active construction sites
> **Sector skill:** `../../SKILL.md` · **Operators:** `../../../_catalogs/embodied-ai-stack/` · **Shared concepts:** `../../../00-framework/SKILL.md`

## What this machine is

The **Site survey & progress drone** is a non-humanoid autonomous machine whose job is to map the site, track earthwork volumes, and monitor progress and safety from the air. UAV flying autonomous mapping missions; outputs feed the construction-scheduler and quantity-takeoff agents.

## Operating-system context

This platform serves the *Shelter* operating system, whose mission is to create and maintain places for living, working, mobility, commerce, and public life. It takes mobile and heavy-equipment work so people and the sector's AI agents can focus on planning, judgment, and exceptions.

## When to use this skill

When a task needs the physical job "map the site, track earthwork volumes, and monitor progress and safety from the air" in environments such as active construction sites. Pair with the sector skill (`../../SKILL.md`) for domain rules and the human accountability boundary, the AI agents under `../roles/` that plan and direct this work, and `_catalogs/embodied-ai-stack/` for the autonomy, fleet-ops, teleoperation, and safety roles that run it.

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

- **Human owner (fleet operator / site or operations manager)** — owns the safety case, the ODD, land/site/airspace rules, and stop authority; accountable for incidents.
- **Autonomy brain** — perceives, predicts, plans, and issues actuation as tool calls within the ODD.
- **Verified safety layer** — triggers a minimal-risk maneuver (safe-stop / return-to-base / hover) independently of the brain.
- **AI agents** — the sector's planning/monitoring agents direct and schedule the machine's missions.
- **Remote operator (teleop)** — supervises and takes over beyond the ODD.

## Accountability boundary

Land-use decisions, structural signoff, occupancy approval, worker safety, eviction, and public consultation remain human-led.

These remain human-owned. The machine operates within its ODD and engineered safety envelope and routes anything outside it to the accountable human.

## Architecture-specific failure modes

- **Long-tail / edge cases** — rare scenarios the planner mishandles. Mitigation: conservative ODD, teleop fallback, continuous scenario mining.
- **ODD exit** — conditions drift outside the certified domain (weather, dust, lighting, unmapped area). Mitigation: detect-and-degrade to a minimal-risk maneuver.
- **Sensor degradation / spoofing** — rain, dust, glare, GPS jamming, adversarial markings. Mitigation: sensor fusion, redundancy, anti-spoofing, conservative fallback.
- **Sim-to-real gap** — world-model/simulation training diverges from reality. Mitigation: shadow mode, staged deployment, real-world validation.
- **Mixed-traffic / human interaction** — misreading pedestrians, livestock, ground crew, or other drivers. Mitigation: predictable behavior, low-speed zones, explicit right-of-way rules.
- **Teleop latency / link loss** — remote takeover delayed or lost. Mitigation: onboard safe-stop, bounded autonomy, comms redundancy.
- **Fleet model-monoculture** — a shared brain fails in lockstep. Mitigation: model diversity, staged rollout, geofencing.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Laborer/apprentice → journeyman tradesperson → foreman/superintendent → project manager; design: intern architect/EIT → licensed architect/PE → principal; planner → senior planner → director.
- **Skills, tools & tech employers list:** BIM (Revit), AutoCAD, Procore/Bluebeam, estimating (PlanSwift), scheduling (Primavera P6, MS Project), GIS, permitting systems.
- **Qualifications, certifications & licenses:** PE, licensed architect (ARE/AIA), LEED, PMP, OSHA 30, ICC code certifications, trade journeyman/master licenses, PLS (surveyor).
- **KPIs / metrics in postings:** Schedule/cost variance (CPI/SPI), safety (TRIR/EMR), punch-list/defects, inspection pass rate, permit cycle time.
- **Where these roles are posted:** Indeed, LinkedIn, ZipRecruiter, construction boards, GovernmentJobs (inspectors/planners), trade unions.

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## Adapting to any nation (context modifiers)

Ownership ranges from fleet-as-a-service to cooperatively shared or rented machines; affordability, repairability, connectivity (maps, GPS/RTK, comms), and regulation (road approval, airspace/BVLOS, mine/site rules) decide where it runs. In low-connectivity settings, on-board autonomy and safe-stop matter more than teleop. Re-read through:

- **Scale** (city-state → federation): whether this role is unified or layered across local/regional/national tiers.
- **State capacity** (fragile → high-capacity): whether the owning institution exists and can be held to account, or the job is met by markets, households, NGOs, or donors.
- **Income level** (low → high): affordability of automation and the balance of subsistence vs. wage work.
- **Formality** (informal → formal): whether the people and assets this role acts on appear in any registry at all.
- **Resource & geography**: which hazards and dependencies dominate (water-scarce, flood-prone, landlocked, trade-dependent).
- **Political system & legitimacy**: where the human-accountability boundary actually binds and who may hold power to account.

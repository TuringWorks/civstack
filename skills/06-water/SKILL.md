---
name: "os-06-water"
description: "Operating-system orchestrator skill for **Water, Sanitation, and Public Hygiene** (national operating system #6). Use this skill whenever work touches this sector's mission — Provide safe water, remove waste, control flooding, and prevent waterborne disease — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself."
---

# Operating System 06 — Water, Sanitation, and Public Hygiene

> **Layer:** National operating system (#6 of 23) · **Personnel model:** human-owned, AI- and robot-augmented
> **Cross-references:** `00-framework/` (shared concepts, teaming pattern, accountability), source map `Country-Economy Core Jobs To Be Done.md`

## Mission

Provide safe water, remove waste, control flooding, and prevent waterborne disease.

## When to use this skill

Load this skill when a task concerns water, sanitation, and public hygiene. It gives an agent the sector map: the outcomes that must be produced, who owns them, what can be automated, and where human accountability is non-negotiable. From here, route to the specific role skills under `roles/` for execution.

## Core Jobs To Be Done

These are the durable outcomes this operating system must reliably produce, written as trigger → response:

1. When people need water, collect, treat, distribute, meter, and maintain supply.
2. When wastewater is produced, collect, treat, discharge, reuse, or recover resources safely.
3. When storms occur, manage drainage and flood protection.
4. When contamination is suspected, test, notify, isolate, and remediate.

## The universal lifecycle, applied

Every job in this sector moves through the same seven steps. Use it as a checklist when designing or executing work here:

- **Sense reality** — gather data, observe conditions, inspect sources, listen to people.
- **Interpret reality** — diagnose, forecast, model risk, prioritize.
- **Decide** — choose policy, design, action, allocation, escalation, or tradeoff.
- **Mobilize** — assign labor, budget, materials, rights, permissions, logistics, schedule.
- **Execute** — perform the work in digital or physical space.
- **Verify** — test, audit, measure, inspect, certify, and learn.
- **Govern** — maintain legitimacy, safety, accountability, continuity, and trust.

## Human role families (who owns the work)

- Water treatment operator, wastewater operator, utility technician.
- Civil/environmental engineer, hydrologist, water resource planner.
- Plumber, pipefitter, leak detection technician, meter technician.
- Public health inspector, laboratory technician, environmental compliance specialist.
- Floodplain manager, stormwater program manager.

These remain human-owned. AI personnel and robots augment them; they do not replace the accountable owner.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Operator trainee → certified operator (Grade I–IV) → chief operator/superintendent → utility director; engineering: EIT → PE.
- **Skills, tools & tech employers list:** SCADA, GIS, hydraulic modeling (EPANET, WaterGEMS), LIMS, CMMS (asset/maintenance), telemetry.
- **Qualifications, certifications & licenses:** State water/wastewater operator certification (Grades I–IV), PE (civil/environmental), backflow tester, confined-space, CDL (some).
- **KPIs / metrics in postings:** Water-quality compliance, non-revenue water/leakage, NPDES permit compliance, boil-water/outage events, asset condition.
- **Where these roles are posted:** GovernmentJobs, Careers.<state>.gov, AWWA/WEF job boards, Indeed, ZipRecruiter.

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **Water quality monitoring agent** — monitors sensor and lab data and flags contamination signals. *(supervised by treatment operator; skill: `roles/water-quality-monitoring-agent/`)*
- **Leak prediction agent** — predicts leaks and pipe failures from pressure and acoustic data. *(supervised by utility engineer; skill: `roles/leak-prediction-agent/`)*
- **Pump optimization agent** — optimizes pumping and energy use across the network. *(supervised by operations engineer; skill: `roles/pump-optimization-agent/`)*
- **Permit compliance reviewer** — checks discharge and abstraction against permit limits. *(supervised by environmental compliance specialist; skill: `roles/permit-compliance-reviewer/`)*
- **Flood forecast analyst** — forecasts flood risk and informs drainage operations. *(supervised by floodplain manager; skill: `roles/flood-forecast-analyst/`)*
- **Asset maintenance planner** — schedules inspection and renewal of network assets. *(supervised by asset manager; skill: `roles/asset-maintenance-planner/`)*

## Work-system completeness (the work around the core work)

The core roles above are necessary but not sufficient. For each material JTBD, check which ancillary services are required:

| Family | Required support question | Reusable catalog |
|---|---|---|
| **Enable** | Do practitioners have the evidence, knowledge, data, tools, access, and skills they need? | `_catalogs/enabling-work/` |
| **Integrate** | Who owns dependencies, handoffs, queues, decision preparation, and stakeholder alignment? | `_catalogs/enabling-work/` |
| **Assure** | What needs independent quality review, challenge, testing, risk, safety, legal, or audit work? | `_catalogs/enabling-work/` |
| **Adapt** | How are alternatives generated and operational experience converted into improvement? | `_catalogs/enabling-work/` |
| **Sustain** | Who maintains administration, capacity, wellbeing, coverage, assets, and institutional memory? | `_catalogs/enabling-work/` |

Do not clone every support role into this sector. Choose **embedded, shared, platform, federated, or temporary** support according to demand, specialization, consequence, and context. Every ancillary service must name the core JTBD and owner it serves, its trigger, deliverable, service level, decision boundary, outcome link, escalation, and retirement rule. See the [Work-System Completeness Map](../../docs/work-system-completeness-map.md).

## Humanoid robot roles

- Plant rounds, valve turning, sample transport, confined-space inspection support with proper safety design.
- Pipe repair assistant, meter reading, emergency sandbag/logistics support.

Dedicated **embodied robot role skills** for this sector (LLM-brained; actions as tool calls via VLA policies):

- **Treatment plant operations robot** — patrol water and wastewater plants, read gauges, take samples, turn valves, and service pumps and dosing systems. *(embodied robot skill: `robots/treatment-plant-operations-robot/`)*
- **Sanitation and public-hygiene robot** — clean and service public toilets, drains, and fecal-sludge collection points and handle waste safely. *(embodied robot skill: `robots/sanitation-and-public-hygiene-robot/`)*

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

## Non-humanoid autonomous machines

Self-driving vehicles, equipment, and drones for this sector (LLM-planned; physical actions as tool calls; ODD + teleoperation fallback):

- **Water-asset inspection drone** — inspect tanks, towers, pipelines, and treatment assets from the air. *(autonomous machine skill: `autonomous/water-asset-inspection-drone/`)*
- **Reservoir survey & sampling vessel (USV)** — survey reservoirs and waterways and collect water-quality samples autonomously. *(autonomous machine skill: `autonomous/reservoir-survey-sampling-vessel-usv/`)*

> **How these machines work (assumed architecture):** each is a **non-humanoid autonomous machine** — a foundation/LLM planning brain issues **actions as tool calls** (`follow_route`, `dump_bucket`, `take_off`, `spray_zone`, …) over a perception → prediction → planning → control stack trained on world models, driving/field simulation, and **RLAIF**. Each runs inside a defined **Operational Design Domain (ODD)** with a verified safe-stop and **teleoperation** fallback. Full detail in `_catalogs/autonomous-machines/` and `00-framework/`.

## Human accountability boundary (must stay human-led)

Public health notices, water shutoffs, infrastructure investment, environmental-discharge approvals, and emergency allocation remain human-led.

Treat this boundary as a hard constraint. Agents in this sector may sense, interpret, draft, model, monitor, and coordinate up to this line, then must hand off to an accountable human for the decision itself.

## Division of labor (human / AI / robot)

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff, and everything inside the accountability boundary above.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document. Strongest on digital signals and repeatable decision support.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces. Strongest on physical work in human-built environments.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor-impact review.

## Interfaces with other operating systems

This sector regularly depends on and feeds: Energy & Utilities, Health & Care, Environment & Waste, Shelter & Built Environment. Coordinate handoffs explicitly; most systemic failures happen at the seams between operating systems.


## Sector success metrics (illustrative)

- Coverage / reliability: the share of the population or demand reliably served.
- Quality / safety: defect, incident, and harm rates within tolerance.
- Cost / efficiency: unit cost and resource use trending down without eroding safety.
- Trust / legitimacy: public confidence, complaint resolution, and auditability.
- Resilience: time-to-detect and time-to-recover from shocks.

## Failure modes to watch

- **Monoculture / correlated failure** — shared models or vendors failing in lockstep; require diversity and manual fallback.
- **Cascading dependency** — failures propagating from the systems listed above; map dependencies and design graceful degradation.
- **Deskilling** — losing the human bench that can run the sector manually; retain drills and manual modes.
- **Agent-specific failure** — fabrication, prompt injection, reward hacking, silent drift; keep the control layer independent.
- **Speed mismatch** — automated action outrunning human oversight; install circuit breakers for high-consequence steps.

## Deskilling watch & keep-warm regime

Automating routine cases erodes three things over time: the **human fallback bench** (who runs this when automation fails), **tacit / craft judgment** (lost as the experienced cohort retires), and the **learning ladder** (juniors never get the cases they used to learn on). Job and role simulators are the primary countermeasure.

- **Risk here:** Operators cannot run the plant manually during a SCADA failure; process intuition fades.
- **Countermeasures:** Manual-operation drills; operator recertification; contamination tabletops.
- **Role/job simulators (keep-warm):** Plant-operation simulators (SCADA-down); contamination-response and manual-valving drills.

> **Dual-use simulators:** the world models and simulation built to *train the machines* in this sector double as the **keep-warm simulators** that keep humans current and rebuild the learning ladder. Owned cross-sector by OS 22 (Resilience) and the `_catalogs/simulation-training/` roles; the verified deterministic fallback in `_catalogs/capability-optimization/` is its technical complement.

## Adapting to any nation (context modifiers)

The jobs above are universal; how they are staffed is not. Water and sanitation is a public-health system first and a utility second: quality failures compound invisibly until people are sick, and in much of the world the "network" includes standpipes, tankers, and community-managed points.

Re-read this sector through:

- **Scale** (city-state → federation): whether this role is unified or layered across local/regional/national tiers.
- **State capacity** (fragile → high-capacity): whether the owning institution exists and can be held to account, or the job is met by markets, households, NGOs, or donors.
- **Income level** (low → high): affordability of automation and the balance of subsistence vs. wage work.
- **Formality** (informal → formal): whether the people and assets this role acts on appear in any registry at all.
- **Resource & geography**: which hazards and dependencies dominate (water-scarce, flood-prone, landlocked, trade-dependent).
- **Political system & legitimacy**: where the human-accountability boundary actually binds and who may hold power to account.

## How to operate in this sector

1. Identify which Core JTBD the task serves.
2. Select the role skill(s) under `roles/` that fit, and confirm the human supervisor.
3. Run the work-system completeness check and add only the Enable, Integrate, Assure, Adapt, and Sustain services the core outcome requires.
4. Run the lifecycle: sense → interpret → decide → mobilize → execute → verify → govern.
5. Stop at the accountability boundary and route the decision to the accountable human.
6. Log actions to the control layer and surface anything that trips a failure mode.

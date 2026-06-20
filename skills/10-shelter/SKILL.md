---
name: "os-10-shelter"
description: "Operating-system orchestrator skill for **Shelter, Construction, Land, and the Built Environment** (national operating system #10). Use this skill whenever work touches this sector's mission — Create and maintain places for living, working, mobility, commerce, and public life — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself."
---

# Operating System 10 — Shelter, Construction, Land, and the Built Environment

> **Layer:** National operating system (#10 of 23) · **Personnel model:** human-owned, AI- and robot-augmented
> **Cross-references:** `00-framework/` (shared concepts, teaming pattern, accountability), source map `Country-Economy Core Jobs To Be Done.md`

## Mission

Create and maintain places for living, working, mobility, commerce, and public life.

## When to use this skill

Load this skill when a task concerns shelter, construction, land, and the built environment. It gives an agent the sector map: the outcomes that must be produced, who owns them, what can be automated, and where human accountability is non-negotiable. From here, route to the specific role skills under `roles/` for execution.

## Core Jobs To Be Done

These are the durable outcomes this operating system must reliably produce, written as trigger → response:

1. When people need shelter and workspaces, plan, finance, permit, build, inspect, and maintain them.
2. When land is scarce, balance housing, infrastructure, ecology, commerce, and fairness.
3. When buildings age, renovate, retrofit, or demolish safely.
4. When hazards change, improve resilience to heat, fire, flood, wind, and seismic risk.

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

- Urban planner, zoning analyst, real estate developer, housing policy analyst.
- Architect, civil engineer, structural engineer, MEP engineer.
- Construction manager, superintendent, estimator, scheduler.
- Carpenter, electrician, plumber, HVAC technician, mason, roofer.
- Building inspector, code official, facilities manager, property manager.
- Surveyor, GIS analyst, land acquisition specialist.

These remain human-owned. AI personnel and robots augment them; they do not replace the accountable owner.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Laborer/apprentice → journeyman tradesperson → foreman/superintendent → project manager; design: intern architect/EIT → licensed architect/PE → principal; planner → senior planner → director.
- **Skills, tools & tech employers list:** BIM (Revit), AutoCAD, Procore/Bluebeam, estimating (PlanSwift), scheduling (Primavera P6, MS Project), GIS, permitting systems.
- **Qualifications, certifications & licenses:** PE, licensed architect (ARE/AIA), LEED, PMP, OSHA 30, ICC code certifications, trade journeyman/master licenses, PLS (surveyor).
- **KPIs / metrics in postings:** Schedule/cost variance (CPI/SPI), safety (TRIR/EMR), punch-list/defects, inspection pass rate, permit cycle time.
- **Where these roles are posted:** Indeed, LinkedIn, ZipRecruiter, construction boards, GovernmentJobs (inspectors/planners), trade unions.

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **Permitting assistant** — guides and pre-checks permit applications against code. *(supervised by code official; skill: `roles/permitting-assistant/`)*
- **Code compliance checker** — checks designs and plans against building codes. *(supervised by building inspector; skill: `roles/code-compliance-checker/`)*
- **Construction scheduler** — builds and maintains critical-path construction schedules. *(supervised by project scheduler; skill: `roles/construction-scheduler/`)*
- **Design option generator** — generates and compares design options against constraints. *(supervised by architect; skill: `roles/design-option-generator/`)*
- **Quantity takeoff estimator** — produces material and cost takeoffs from drawings. *(supervised by estimator; skill: `roles/quantity-takeoff-estimator/`)*
- **Energy modeling agent** — models building energy and comfort performance. *(supervised by MEP engineer; skill: `roles/energy-modeling-agent/`)*
- **Facilities maintenance planner** — plans preventive maintenance across a building portfolio. *(supervised by facilities manager; skill: `roles/facilities-maintenance-planner/`)*
- **Lease/document reviewer** — reviews leases and property documents for terms and risk. *(supervised by property manager; skill: `roles/lease-document-reviewer/`)*
- **Property listing & valuation agent** — drafts listings and runs comparable-based valuations (AVM) for sale or rent. *(supervised by real-estate broker; skill: `roles/property-listing-valuation-agent/`)*
- **Lease abstraction & management agent** — extracts lease terms and tracks obligations, renewals, and escalations. *(supervised by property manager; skill: `roles/lease-abstraction-management-agent/`)*
- **Tenant screening & onboarding assistant** — screens applicants and prepares onboarding within fair-housing and anti-discrimination limits. *(supervised by property manager; skill: `roles/tenant-screening-onboarding-assistant/`)*

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

- Material handling, site cleanup, inspection, painting, drywall support, repetitive tool tasks.
- Facilities rounds, repair support, janitorial work, disaster damage assessment.

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

## Non-humanoid autonomous machines

Self-driving vehicles, equipment, and drones for this sector (LLM-planned; physical actions as tool calls; ODD + teleoperation fallback):

- **Autonomous earthmover (dozer/excavator/loader)** — grade, excavate, load, and move material to a site model. *(autonomous machine skill: `autonomous/autonomous-earthmover-dozer-excavator-loader/`)*
- **Site survey & progress drone** — map the site, track earthwork volumes, and monitor progress and safety from the air. *(autonomous machine skill: `autonomous/site-survey-progress-drone/`)*

> **How these machines work (assumed architecture):** each is a **non-humanoid autonomous machine** — a foundation/LLM planning brain issues **actions as tool calls** (`follow_route`, `dump_bucket`, `take_off`, `spray_zone`, …) over a perception → prediction → planning → control stack trained on world models, driving/field simulation, and **RLAIF**. Each runs inside a defined **Operational Design Domain (ODD)** with a verified safe-stop and **teleoperation** fallback. Full detail in `_catalogs/autonomous-machines/` and `00-framework/`.

## Human accountability boundary (must stay human-led)

Land-use decisions, structural signoff, occupancy approval, worker safety, eviction, and public consultation remain human-led.

Treat this boundary as a hard constraint. Agents in this sector may sense, interpret, draft, model, monitor, and coordinate up to this line, then must hand off to an accountable human for the decision itself.

## Division of labor (human / AI / robot)

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff, and everything inside the accountability boundary above.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document. Strongest on digital signals and repeatable decision support.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces. Strongest on physical work in human-built environments.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor-impact review.

## Interfaces with other operating systems

This sector regularly depends on and feeds: Water & Sanitation, Energy & Utilities, Transportation & Logistics, Environment & Waste. Coordinate handoffs explicitly; most systemic failures happen at the seams between operating systems.

## Strategic missions that draw on this sector

Beyond its own mandate, this operating system is composed by these cross-cutting [strategic missions](../strategic-missions/) (the orthogonal mission axis — a mission pulls roles from several sectors toward one national objective):

- [Energy Abundance](../strategic-missions/energy-abundance/)

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

- **Risk here:** Trades deskilled by prefab and robotics; inspectors over-rely on AI for structural judgment.
- **Countermeasures:** Apprenticeship protection; manual-inspection competency; retain structural judgment.
- **Role/job simulators (keep-warm):** Inspection and structural-judgment simulators; VR/AR trade-skill rigs; manual quantity-takeoff practice.

> **Dual-use simulators:** the world models and simulation built to *train the machines* in this sector double as the **keep-warm simulators** that keep humans current and rebuild the learning ladder. Owned cross-sector by OS 22 (Resilience) and the `_catalogs/simulation-training/` roles; the verified deterministic fallback in `_catalogs/capability-optimization/` is its technical complement.

## Adapting to any nation (context modifiers)

The jobs above are universal; how they are staffed is not. Re-read this sector through:

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

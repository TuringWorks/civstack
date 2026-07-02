---
name: "os-07-energy"
description: "Operating-system orchestrator skill for **Energy, Utilities, and Grid Operations** (national operating system #7). Use this skill whenever work touches this sector's mission — Produce, store, transmit, distribute, and balance energy safely and affordably — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself."
---

# Operating System 07 — Energy, Utilities, and Grid Operations

> **Layer:** National operating system (#7 of 23) · **Personnel model:** human-owned, AI- and robot-augmented
> **Cross-references:** `00-framework/` (shared concepts, teaming pattern, accountability), source map `Country-Economy Core Jobs To Be Done.md`

## Mission

Produce, store, transmit, distribute, and balance energy safely and affordably.

## When to use this skill

Load this skill when a task concerns energy, utilities, and grid operations. It gives an agent the sector map: the outcomes that must be produced, who owns them, what can be automated, and where human accountability is non-negotiable. From here, route to the specific role skills under `roles/` for execution.

## Core Jobs To Be Done

These are the durable outcomes this operating system must reliably produce, written as trigger → response:

1. When demand changes second by second, balance supply and load.
2. When assets age or fail, maintain generation, storage, transmission, and distribution.
3. When fuel markets or weather shift, plan resilient supply.
4. When decarbonization is required, integrate renewables, storage, demand response, nuclear, hydro, geothermal, and efficiency.
5. When outages occur, restore service safely and communicate clearly.

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

- Grid operator, power systems engineer, utility dispatcher.
- Electrician, lineworker, substation technician, relay technician.
- Renewable energy engineer, solar installer, wind turbine technician.
- Nuclear operator, plant engineer, safety analyst.
- Energy trader, load forecaster, demand response manager.
- Utility customer operations manager, field service technician.

These remain human-owned. AI personnel and robots augment them; they do not replace the accountable owner.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Apprentice lineworker/technician → journeyman → foreman; system-operator trainee → certified system operator → shift supervisor → control-center manager; EIT → PE → engineering manager; energy trader.
- **Skills, tools & tech employers list:** EMS/SCADA, OMS (outage management), ADMS/DMS, ISO/RTO market platforms, PI historian, PSS/E, GIS.
- **Qualifications, certifications & licenses:** NERC System Operator certification (RC/BA/TO), journeyman electrical license, PE, NRC reactor operator (nuclear), OSHA, CDL.
- **KPIs / metrics in postings:** SAIDI/SAIFI reliability, area control error/load balance, restoration time, OSHA recordables, market-settlement accuracy.
- **Where these roles are posted:** ZipRecruiter, Glassdoor, BuiltIn, LinkedIn, IBEW, utility career pages.

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **Load forecasting agent** — forecasts demand across horizons for balancing and trading. *(supervised by load forecaster; skill: `roles/load-forecasting-agent/`)*
- **Grid anomaly detector** — detects faults and instability in telemetry. *(supervised by grid operator; skill: `roles/grid-anomaly-detector/`)*
- **Outage restoration planner** — sequences crews and switching to restore service safely. *(supervised by distribution operations lead; skill: `roles/outage-restoration-planner/`)*
- **Maintenance prediction agent** — predicts asset failures and schedules maintenance. *(supervised by reliability engineer; skill: `roles/maintenance-prediction-agent/`)*
- **Energy market analyst** — analyzes prices and positions within market rules. *(supervised by energy trader; skill: `roles/energy-market-analyst/`)*
- **Permitting documentation agent** — prepares siting and interconnection documentation. *(supervised by project engineer; skill: `roles/permitting-documentation-agent/`)*
- **Customer outage communications agent** — drafts and targets outage and restoration updates. *(supervised by customer operations manager; skill: `roles/customer-outage-communications-agent/`)*
- **Generation-buildout planning agent** — plans and sequences clean generation, storage, and transmission ahead of forecast demand and works down the interconnection-queue and permitting backlog. *(supervised by resource planner / grid planning lead; skill: `roles/generation-buildout-planning-agent/`)*

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

- Plant inspection rounds, warehouse logistics, solar-farm maintenance, substation visual inspection.
- Support for line crews with tools/materials, but energized work requires extreme controls.

Dedicated **embodied robot role skills** for this sector (LLM-brained; actions as tool calls via VLA policies):

- **Substation and plant maintenance robot** — patrol substations and plants, thermal-scan and inspect equipment, rack breakers, and perform routine switching preparation under dispatch. *(embodied robot skill: `robots/substation-and-plant-maintenance-robot/`)*
- **Line-crew assistant robot** — stage materials, prepare hardware, dig and set poles, and support de-energized line construction and storm restoration. *(embodied robot skill: `robots/line-crew-assistant-robot/`)*

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

## Non-humanoid autonomous machines

Self-driving vehicles, equipment, and drones for this sector (LLM-planned; physical actions as tool calls; ODD + teleoperation fallback):

- **Grid & renewable-asset inspection drone** — inspect powerlines, towers, substations, and solar/wind assets from the air. *(autonomous machine skill: `autonomous/grid-renewable-asset-inspection-drone/`)*

> **How these machines work (assumed architecture):** each is a **non-humanoid autonomous machine** — a foundation/LLM planning brain issues **actions as tool calls** (`follow_route`, `dump_bucket`, `take_off`, `spray_zone`, …) over a perception → prediction → planning → control stack trained on world models, driving/field simulation, and **RLAIF**. Each runs inside a defined **Operational Design Domain (ODD)** with a verified safe-stop and **teleoperation** fallback. Full detail in `_catalogs/autonomous-machines/` and `00-framework/`.

## Human accountability boundary (must stay human-led)

Grid emergency authority, nuclear operations, safety switching, market-manipulation controls, and major infrastructure siting remain human-accountable.

Treat this boundary as a hard constraint. Agents in this sector may sense, interpret, draft, model, monitor, and coordinate up to this line, then must hand off to an accountable human for the decision itself.

## Division of labor (human / AI / robot)

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff, and everything inside the accountability boundary above.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document. Strongest on digital signals and repeatable decision support.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces. Strongest on physical work in human-built environments.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor-impact review.

## Interfaces with other operating systems

This sector regularly depends on and feeds: Water & Sanitation, Materials & Manufacturing, Communications & Software, Resilience & Continuity. Coordinate handoffs explicitly; most systemic failures happen at the seams between operating systems.

## Strategic missions that draw on this sector

Beyond its own mandate, this operating system is composed by these cross-cutting [strategic missions](../strategic-missions/) (the orthogonal mission axis — a mission pulls roles from several sectors toward one national objective):

- [Energy Abundance](../strategic-missions/energy-abundance/)
- [Frontier AI Production](../strategic-missions/frontier-ai-production/)
- [Digital Infrastructure](../strategic-missions/digital-infrastructure/)

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

- **Risk here:** System operators lose manual switching and restoration skill; black-start expertise becomes rare.
- **Countermeasures:** NERC recertification plus simulator training; black-start drills; manual-restoration practice.
- **Role/job simulators (keep-warm):** Control-room and black-start simulators; manual switching and restoration scenarios (already mature practice).

> **Dual-use simulators:** the world models and simulation built to *train the machines* in this sector double as the **keep-warm simulators** that keep humans current and rebuild the learning ladder. Owned cross-sector by OS 22 (Resilience) and the `_catalogs/simulation-training/` roles; the verified deterministic fallback in `_catalogs/capability-optimization/` is its technical complement.

## Adapting to any nation (context modifiers)

The jobs above are universal; how they are staffed is not. Energy work balances real-time physics against decades-long assets: grid decisions propagate in milliseconds, while theft, non-payment, and off-grid self-supply dominate the economics in low-capacity systems.

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

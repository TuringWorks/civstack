---
name: "os-19-environment"
description: "Operating-system orchestrator skill for **Environment, Climate, Waste, and Resource Stewardship** (national operating system #19). Use this skill whenever work touches this sector's mission — Protect natural systems, manage waste, reduce pollution, and adapt to climate risk — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself."
---

# Operating System 19 — Environment, Climate, Waste, and Resource Stewardship

> **Layer:** National operating system (#19 of 23) · **Personnel model:** human-owned, AI- and robot-augmented
> **Cross-references:** `00-framework/` (shared concepts, teaming pattern, accountability), source map `Country-Economy Core Jobs To Be Done.md`

## Mission

Protect natural systems, manage waste, reduce pollution, and adapt to climate risk.

## When to use this skill

Load this skill when a task concerns environment, climate, waste, and resource stewardship. It gives an agent the sector map: the outcomes that must be produced, who owns them, what can be automated, and where human accountability is non-negotiable. From here, route to the specific role skills under `roles/` for execution.

## Core Jobs To Be Done

These are the durable outcomes this operating system must reliably produce, written as trigger → response:

1. When waste is produced, collect, sort, treat, recycle, compost, landfill, or neutralize it safely.
2. When pollution occurs, monitor, enforce, remediate, and prevent recurrence.
3. When ecosystems decline, conserve, restore, and manage land/water/wildlife.
4. When climate risks rise, forecast, adapt, insure, relocate, harden, and decarbonize.
5. When materials reach end-of-life, recover and recirculate them so virgin extraction and waste fall.

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

- Waste collection operator, recycling coordinator, landfill manager.
- Environmental scientist, conservation scientist, ecologist, hydrologist.
- Climate risk analyst, sustainability manager, carbon accounting specialist.
- Environmental compliance specialist, remediation project manager.
- Park ranger, natural resource manager, urban forester.

These remain human-owned. AI personnel and robots augment them; they do not replace the accountable owner.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Technician/operator → environmental scientist/analyst → project manager → program director; ranger → senior → manager; sustainability analyst → manager → director.
- **Skills, tools & tech employers list:** GIS, remote sensing, carbon/emissions-accounting platforms, environmental monitoring/LIMS, modeling, EHS systems.
- **Qualifications, certifications & licenses:** PE (environmental), PG, CHMM (hazmat), CSP, CDL (waste), Certified Energy Manager, ISO 14001 lead auditor, pesticide/remediation licenses.
- **KPIs / metrics in postings:** Emissions reduced, diversion/recycling rate, permit compliance, remediation milestones, habitat/biodiversity metrics.
- **Where these roles are posted:** GovernmentJobs (EPA/state), USAJOBS, Indeed, LinkedIn, conservation/environmental boards, Idealist.

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **Emissions accounting agent** — compiles and audits greenhouse-gas inventories. *(supervised by carbon accounting specialist; skill: `roles/emissions-accounting-agent/`)*
- **Satellite monitoring analyst** — monitors land, water, and emissions from remote sensing. *(supervised by environmental scientist; skill: `roles/satellite-monitoring-analyst/`)*
- **Climate risk modeler** — models physical and transition climate risk. *(supervised by climate risk analyst; skill: `roles/climate-risk-modeler/`)*
- **Waste stream optimization agent** — optimizes collection, sorting, and recycling flows. *(supervised by recycling coordinator; skill: `roles/waste-stream-optimization-agent/`)*
- **Permit compliance agent** — tracks environmental permit obligations. *(supervised by environmental compliance specialist; skill: `roles/permit-compliance-agent/`)*
- **Environmental impact review assistant** — drafts and checks environmental impact assessments. *(supervised by remediation project manager; skill: `roles/environmental-impact-review-assistant/`)*
- **Circular-economy material-flow agent** — maps material flows end-to-end and routes end-of-life materials back into production so virgin extraction and waste fall. *(supervised by circular-economy lead / sustainability manager; skill: `roles/circular-economy-material-flow-agent/`)*
- **Natural-capital accounting agent** — books ecosystems, water, soil, and biodiversity as assets on the national balance sheet and tracks their depletion or restoration. *(supervised by environmental economist; skill: `roles/natural-capital-accounting-agent/`)*

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

- Sorting facilities, hazardous cleanup support, field sampling, park maintenance, inspection.

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

## Non-humanoid autonomous machines

Self-driving vehicles, equipment, and drones for this sector (LLM-planned; physical actions as tool calls; ODD + teleoperation fallback):

- **Environmental survey & monitoring drone** — map habitats, measure emissions and effluent, and monitor land, water, and wildlife from the air. *(autonomous machine skill: `autonomous/environmental-survey-monitoring-drone/`)*

> **How these machines work (assumed architecture):** each is a **non-humanoid autonomous machine** — a foundation/LLM planning brain issues **actions as tool calls** (`follow_route`, `dump_bucket`, `take_off`, `spray_zone`, …) over a perception → prediction → planning → control stack trained on world models, driving/field simulation, and **RLAIF**. Each runs inside a defined **Operational Design Domain (ODD)** with a verified safe-stop and **teleoperation** fallback. Full detail in `_catalogs/autonomous-machines/` and `00-framework/`.

## Human accountability boundary (must stay human-led)

Environmental justice, land-use tradeoffs, enforcement, relocation policy, protected-area governance, and remediation signoff remain human-led.

Treat this boundary as a hard constraint. Agents in this sector may sense, interpret, draft, model, monitor, and coordinate up to this line, then must hand off to an accountable human for the decision itself.

## Division of labor (human / AI / robot)

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff, and everything inside the accountability boundary above.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document. Strongest on digital signals and repeatable decision support.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces. Strongest on physical work in human-built environments.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor-impact review.

## Interfaces with other operating systems

This sector regularly depends on and feeds: Water & Sanitation, Energy & Utilities, Food & Agriculture, Resilience & Continuity. Coordinate handoffs explicitly; most systemic failures happen at the seams between operating systems.

## Strategic missions that draw on this sector

Beyond its own mandate, this operating system is composed by these cross-cutting [strategic missions](../strategic-missions/) (the orthogonal mission axis — a mission pulls roles from several sectors toward one national objective):

- [Bioeconomy](../strategic-missions/bioeconomy/)

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

- **Risk here:** Field scientists lose taxonomic and naturalist skill as remote sensing and AI ID take over.
- **Countermeasures:** Maintain field competency; ground-truthing; train naturalists.
- **Role/job simulators (keep-warm):** Field-identification and survey simulators; ground-truthing exercises; specimen/identification drills.

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

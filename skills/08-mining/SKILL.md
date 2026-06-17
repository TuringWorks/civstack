---
name: "os-08-mining"
description: "Operating-system orchestrator skill for **Mining, Materials, Chemicals, and Industrial Inputs** (national operating system #8). Use this skill whenever work touches this sector's mission — Extract and transform raw materials into safe, reliable inputs for the economy — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself."
---

# Operating System 08 — Mining, Materials, Chemicals, and Industrial Inputs

> **Layer:** National operating system (1 of 22) · **Personnel model:** human-owned, AI- and robot-augmented
> **Cross-references:** `00-framework/` (shared concepts, teaming pattern, accountability), source map `Country-Economy Core Jobs To Be Done.md`

## Mission

Extract and transform raw materials into safe, reliable inputs for the economy.

## When to use this skill

Load this skill when a task concerns mining, materials, chemicals, and industrial inputs. It gives an agent the sector map: the outcomes that must be produced, who owns them, what can be automated, and where human accountability is non-negotiable. From here, route to the specific role skills under `roles/` for execution.

## Core Jobs To Be Done

These are the durable outcomes this operating system must reliably produce, written as trigger → response:

1. When industry needs inputs, locate, extract, process, refine, transport, and certify materials.
2. When hazardous processes operate, monitor safety and environmental compliance.
3. When supply chains are fragile, diversify sources and recycle critical materials.
4. When materials fail, investigate defects and improve specifications.

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

- Mining engineer, geologist, equipment operator, mine safety manager.
- Chemical engineer, process engineer, plant operator, refinery technician.
- Metallurgist, materials scientist, quality engineer, lab technician.
- Environmental health and safety manager, hazardous materials specialist.
- Supply chain analyst, critical minerals strategist, recycling operations manager.

These remain human-owned. AI personnel and robots augment them; they do not replace the accountable owner.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Operator/technician → process/plant engineer → superintendent → plant manager; geologist and metallurgist tracks.
- **Skills, tools & tech employers list:** DCS process control, LIMS, mine-planning (Surpac, Vulcan), SCADA, EHS systems, simulation.
- **Qualifications, certifications & licenses:** PE, MSHA training, CSP (safety), HAZWOPER, Professional Geologist (PG), CIH (industrial hygiene).
- **KPIs / metrics in postings:** Throughput/recovery, yield and quality, safety (TRIR), environmental compliance, downtime.
- **Where these roles are posted:** Indeed, LinkedIn, ZipRecruiter, mining/chemical industry boards.

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **Exploration data analyst** — interprets geological and geophysical data to locate resources. *(supervised by geologist; skill: `roles/exploration-data-analyst/`)*
- **Process optimization agent** — optimizes yield, energy, and quality in process plants. *(supervised by process engineer; skill: `roles/process-optimization-agent/`)*
- **Safety incident predictor** — predicts safety incidents from operations and near-miss data. *(supervised by mine/EHS safety manager; skill: `roles/safety-incident-predictor/`)*
- **Chemical literature synthesis agent** — synthesizes chemistry literature and patents for R&D. *(supervised by chemical engineer; skill: `roles/chemical-literature-synthesis-agent/`)*
- **Materials discovery agent** — screens and proposes candidate materials and formulations. *(supervised by materials scientist; skill: `roles/materials-discovery-agent/`)*
- **Compliance agent** — tracks environmental and safety compliance obligations. *(supervised by EHS manager; skill: `roles/compliance-agent/`)*

## Humanoid robot roles

- Hazardous inspection, sample handling, lab/plant logistics, maintenance support.
- Disaster inspection where human entry is dangerous.

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

## Non-humanoid autonomous machines

Self-driving vehicles, equipment, and drones for this sector (LLM-planned; physical actions as tool calls; ODD + teleoperation fallback):

- **Autonomous haul truck** — haul ore and overburden on mine haul roads around the clock. *(autonomous machine skill: `autonomous/autonomous-haul-truck/`)*
- **Autonomous loader / excavator** — load trucks and dig and move material at the face. *(autonomous machine skill: `autonomous/autonomous-loader-excavator/`)*
- **Autonomous blast-hole drill** — drill blast-holes to a pattern precisely and repeatably. *(autonomous machine skill: `autonomous/autonomous-blast-hole-drill/`)*

> **How these machines work (assumed architecture):** each is a **non-humanoid autonomous machine** — a foundation/LLM planning brain issues **actions as tool calls** (`follow_route`, `dump_bucket`, `take_off`, `spray_zone`, …) over a perception → prediction → planning → control stack trained on world models, driving/field simulation, and **RLAIF**. Each runs inside a defined **Operational Design Domain (ODD)** with a verified safe-stop and **teleoperation** fallback. Full detail in `_catalogs/autonomous-machines/` and `00-framework/`.

## Human accountability boundary (must stay human-led)

Mine safety, hazardous releases, environmental permits, community consent, and shutdown decisions remain human-led.

Treat this boundary as a hard constraint. Agents in this sector may sense, interpret, draft, model, monitor, and coordinate up to this line, then must hand off to an accountable human for the decision itself.

## Division of labor (human / AI / robot)

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff, and everything inside the accountability boundary above.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document. Strongest on digital signals and repeatable decision support.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces. Strongest on physical work in human-built environments.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor-impact review.

## Interfaces with other operating systems

This sector regularly depends on and feeds: Energy & Utilities, Manufacturing, Environment & Waste, Transportation & Logistics. Coordinate handoffs explicitly; most systemic failures happen at the seams between operating systems.

## Strategic missions that draw on this sector

Beyond its own mandate, this operating system is composed by these cross-cutting [strategic missions](../strategic-missions/) (the orthogonal mission axis — a mission pulls roles from several sectors toward one national objective):

- [Energy Abundance](../strategic-missions/energy-abundance/)
- [Semiconductor Sovereignty](../strategic-missions/semiconductor-sovereignty/)
- [Bioeconomy](../strategic-missions/bioeconomy/)
- [Frontier AI Production](../strategic-missions/frontier-ai-production/)
- [Quantum and Space Systems](../strategic-missions/quantum-and-space-systems/)
- [Strategic Supply Chain](../strategic-missions/strategic-supply-chain/)
- [Advanced Manufacturing](../strategic-missions/advanced-manufacturing/)

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

- **Risk here:** Hazardous-process operators lose hands-on control; geological and metallurgical intuition fades.
- **Countermeasures:** Manual-control drills; hazard simulations; retain deep process knowledge.
- **Role/job simulators (keep-warm):** Process-control and emergency-shutdown simulators; hazard and release-response drills.

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
3. Run the lifecycle: sense → interpret → decide → mobilize → execute → verify → govern.
4. Stop at the accountability boundary and route the decision to the accountable human.
5. Log actions to the control layer and surface anything that trips a failure mode.

---
name: os-06-water
description: Operating-system orchestrator skill for **Water, Sanitation, and Public Hygiene** (national operating system #6). Use this skill whenever work touches this sector's mission — Provide safe water, remove waste, control flooding, and prevent waterborne disease — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself.
---

# Operating System 06 — Water, Sanitation, and Public Hygiene

> **Layer:** National operating system (1 of 22) · **Personnel model:** human-owned, AI- and robot-augmented
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

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **Water quality monitoring agent** — monitors sensor and lab data and flags contamination signals. *(supervised by treatment operator; skill: `roles/water-quality-monitoring-agent/`)*
- **Leak prediction agent** — predicts leaks and pipe failures from pressure and acoustic data. *(supervised by utility engineer; skill: `roles/leak-prediction-agent/`)*
- **Pump optimization agent** — optimizes pumping and energy use across the network. *(supervised by operations engineer; skill: `roles/pump-optimization-agent/`)*
- **Permit compliance reviewer** — checks discharge and abstraction against permit limits. *(supervised by environmental compliance specialist; skill: `roles/permit-compliance-reviewer/`)*
- **Flood forecast analyst** — forecasts flood risk and informs drainage operations. *(supervised by floodplain manager; skill: `roles/flood-forecast-analyst/`)*
- **Asset maintenance planner** — schedules inspection and renewal of network assets. *(supervised by asset manager; skill: `roles/asset-maintenance-planner/`)*

## Humanoid robot roles

- Plant rounds, valve turning, sample transport, confined-space inspection support with proper safety design.
- Pipe repair assistant, meter reading, emergency sandbag/logistics support.

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

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

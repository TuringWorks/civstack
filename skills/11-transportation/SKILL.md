---
name: "os-11-transportation"
description: "Operating-system orchestrator skill for **Transportation, Logistics, Postal, and Mobility** (national operating system #11). Use this skill whenever work touches this sector's mission — Move people and goods through networks safely, predictably, and economically — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself."
---

# Operating System 11 — Transportation, Logistics, Postal, and Mobility

> **Layer:** National operating system (1 of 22) · **Personnel model:** human-owned, AI- and robot-augmented
> **Cross-references:** `00-framework/` (shared concepts, teaming pattern, accountability), source map `Country-Economy Core Jobs To Be Done.md`

## Mission

Move people and goods through networks safely, predictably, and economically.

## When to use this skill

Load this skill when a task concerns transportation, logistics, postal, and mobility. It gives an agent the sector map: the outcomes that must be produced, who owns them, what can be automated, and where human accountability is non-negotiable. From here, route to the specific role skills under `roles/` for execution.

## Core Jobs To Be Done

These are the durable outcomes this operating system must reliably produce, written as trigger → response:

1. When goods need movement, plan routes, consolidate loads, operate hubs, clear customs, and deliver.
2. When people need mobility, provide safe roads, transit, aviation, rail, maritime, and pedestrian systems.
3. When networks are disrupted, reroute and communicate.
4. When infrastructure wears down, inspect, maintain, and upgrade.

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

- Truck driver, delivery driver, courier, bus operator, train operator.
- Pilot, air traffic controller, flight dispatcher, aircraft mechanic.
- Port operator, longshore worker, customs broker, freight forwarder.
- Logistics coordinator, supply chain manager, warehouse manager.
- Traffic engineer, transit planner, fleet manager, route optimization analyst.
- Postal carrier, mail processing clerk, last-mile operations manager.

These remain human-owned. AI personnel and robots augment them; they do not replace the accountable owner.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Driver/warehouse associate → lead/dispatcher → operations supervisor → terminal/DC manager → director of logistics; pilot and ATC tracks; mechanic apprentice → A&P/journeyman.
- **Skills, tools & tech employers list:** TMS, WMS, route optimization, ELD/telematics, dispatch systems, EDI, fleet-maintenance systems.
- **Qualifications, certifications & licenses:** CDL (A/B/C) + endorsements (HazMat, tanker) with ELDT/FMCSA medical, FAA A&P (mechanics), ATP/commercial pilot, FAA ATC, APICS CSCP/CLTD, TWIC (ports), OSHA/forklift.
- **KPIs / metrics in postings:** On-time delivery, cost per mile/shipment, fleet utilization, DOT safety compliance, dwell time, damage rate.
- **Where these roles are posted:** iHireTransportation, Indeed, ZipRecruiter, Snagajob (hourly), Dice (logistics tech), USAJOBS (FAA/USPS).

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **Routing optimizer** — optimizes routes and loads against time, cost, and constraints. *(supervised by logistics coordinator; skill: `roles/routing-optimizer/`)*
- **Demand forecast agent** — forecasts shipment and travel demand for planning. *(supervised by supply chain manager; skill: `roles/demand-forecast-agent/`)*
- **Customs documentation agent** — prepares and checks customs and trade documentation. *(supervised by customs broker; skill: `roles/customs-documentation-agent/`)*
- **Fleet maintenance predictor** — predicts vehicle failures and schedules maintenance. *(supervised by fleet manager; skill: `roles/fleet-maintenance-predictor/`)*
- **Warehouse slotting agent** — optimizes storage slotting and pick paths. *(supervised by warehouse manager; skill: `roles/warehouse-slotting-agent/`)*
- **Disruption-response coordinator** — re-plans flows during network disruptions. *(supervised by operations manager; skill: `roles/disruption-response-coordinator/`)*
- **Customer delivery communications agent** — sends delivery status and exception updates. *(supervised by last-mile operations manager; skill: `roles/customer-delivery-communications-agent/`)*

## Humanoid robot roles

- Warehouse picking/packing, loading support, mail sorting, last-100-feet delivery assistance.
- Airport/rail station service support, maintenance inspection assistance.

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

## Non-humanoid autonomous machines

Self-driving vehicles, equipment, and drones for this sector (LLM-planned; physical actions as tool calls; ODD + teleoperation fallback):

- **Self-driving freight truck** — haul freight over highway corridors hub-to-hub without a driver in the cab. *(autonomous machine skill: `autonomous/self-driving-freight-truck/`)*
- **Robotaxi / autonomous passenger vehicle** — carry passengers point-to-point with no human driver. *(autonomous machine skill: `autonomous/robotaxi-autonomous-passenger-vehicle/`)*
- **Last-mile delivery vehicle** — deliver parcels and groceries on local streets and sidewalks. *(autonomous machine skill: `autonomous/last-mile-delivery-vehicle/`)*
- **Autonomous yard / terminal mover** — shuttle trailers and containers within yards, ports, and terminals. *(autonomous machine skill: `autonomous/autonomous-yard-terminal-mover/`)*
- **Autonomous freight & metro train** — run scheduled freight or transit services on guided track with no driver in the cab. *(autonomous machine skill: `autonomous/autonomous-freight-metro-train/`)*
- **Autonomous port straddle carrier & ship-to-shore crane** — stack, move, and load containers at the quay and yard. *(autonomous machine skill: `autonomous/autonomous-port-straddle-carrier-ship-to-shore-crane/`)*
- **Harbor tug / survey vessel (USV)** — assist berthing and survey harbors and channels without a crew. *(autonomous machine skill: `autonomous/harbor-tug-survey-vessel-usv/`)*

> **How these machines work (assumed architecture):** each is a **non-humanoid autonomous machine** — a foundation/LLM planning brain issues **actions as tool calls** (`follow_route`, `dump_bucket`, `take_off`, `spray_zone`, …) over a perception → prediction → planning → control stack trained on world models, driving/field simulation, and **RLAIF**. Each runs inside a defined **Operational Design Domain (ODD)** with a verified safe-stop and **teleoperation** fallback. Full detail in `_catalogs/autonomous-machines/` and `00-framework/`.

## Human accountability boundary (must stay human-led)

Safety-critical vehicle operation, air-traffic-control authority, hazardous-goods approval, labor safety, and public-transport policy remain human-accountable.

Treat this boundary as a hard constraint. Agents in this sector may sense, interpret, draft, model, monitor, and coordinate up to this line, then must hand off to an accountable human for the decision itself.

## Division of labor (human / AI / robot)

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff, and everything inside the accountability boundary above.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document. Strongest on digital signals and repeatable decision support.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces. Strongest on physical work in human-built environments.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor-impact review.

## Interfaces with other operating systems

This sector regularly depends on and feeds: Materials & Manufacturing, Commerce & Services, Energy & Utilities, Resilience & Continuity. Coordinate handoffs explicitly; most systemic failures happen at the seams between operating systems.

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

- **Risk here:** Pilots and drivers lose manual skill (well-documented automation dependency); dispatchers depend on optimizers.
- **Countermeasures:** Mandated manual-flying and recurrent training; degraded-ops drills; keep manual driving/CDL skills.
- **Role/job simulators (keep-warm):** Full-mission flight and drive simulators; automation-failure and manual-reversion scenarios (mature practice).

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

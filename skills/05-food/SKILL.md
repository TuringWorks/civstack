---
name: "os-05-food"
description: "Operating-system orchestrator skill for **Food, Agriculture, Fisheries, and Nutrition** (national operating system #5). Use this skill whenever work touches this sector's mission — Produce, inspect, distribute, and stabilize safe food — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself."
---

# Operating System 05 — Food, Agriculture, Fisheries, and Nutrition

> **Layer:** National operating system (1 of 22) · **Personnel model:** human-owned, AI- and robot-augmented
> **Cross-references:** `00-framework/` (shared concepts, teaming pattern, accountability), source map `Country-Economy Core Jobs To Be Done.md`

## Mission

Produce, inspect, distribute, and stabilize safe food.

## When to use this skill

Load this skill when a task concerns food, agriculture, fisheries, and nutrition. It gives an agent the sector map: the outcomes that must be produced, who owns them, what can be automated, and where human accountability is non-negotiable. From here, route to the specific role skills under `roles/` for execution.

## Core Jobs To Be Done

These are the durable outcomes this operating system must reliably produce, written as trigger → response:

1. When people need calories and nutrition, grow, raise, catch, process, transport, and sell food.
2. When pests, drought, disease, or supply shocks threaten production, adapt quickly.
3. When food moves through supply chains, preserve safety, freshness, labeling, and traceability.
4. When populations face malnutrition or food insecurity, target aid and nutrition programs.

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

- Farmer, ranch manager, farmworker, fishery manager, aquaculture technician.
- Agronomist, soil scientist, crop advisor, irrigation specialist.
- Food scientist, quality assurance manager, food safety inspector.
- Veterinarian, animal health technician, livestock nutritionist.
- Grain merchandiser, cold-chain logistics planner, food distribution manager.
- Dietitian, school nutrition director, food assistance program manager.

These remain human-owned. AI personnel and robots augment them; they do not replace the accountable owner.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Farmworker/technician → crew lead/grower → farm/ranch manager → operations director; agronomy track; food safety: QA tech → QA manager → director of food safety.
- **Skills, tools & tech employers list:** Farm-management software (Climate FieldView, John Deere Operations Center, Granular), precision-ag/GIS, irrigation controllers, telematics, LIMS, HACCP/food-safety systems, ERP.
- **Qualifications, certifications & licenses:** CCA (Certified Crop Adviser), pesticide applicator license, PCQI (FSMA), ServSafe, DVM (veterinary), RD/RDN (dietitian), GlobalG.A.P., CDL for ag transport.
- **KPIs / metrics in postings:** Yield, input cost per acre/unit, loss/waste, food-safety audit scores, traceability completeness, on-time fulfillment.
- **Where these roles are posted:** AgCareers.com, Indeed, LinkedIn, GovernmentJobs (USDA/extension), Snagajob (seasonal/hourly), local co-ops.

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **Crop planning agent** — plans planting, rotation, and inputs against soil, weather, and market data. *(supervised by agronomist; skill: `roles/crop-planning-agent/`)*
- **Pest/disease detection agent** — detects pests and disease early from imagery and sensor data. *(supervised by crop advisor; skill: `roles/pest-disease-detection-agent/`)*
- **Weather/yield forecast agent** — forecasts yield and weather risk for planning and hedging. *(supervised by farm manager; skill: `roles/weather-yield-forecast-agent/`)*
- **Food safety compliance agent** — checks process, labeling, and HACCP records against rules. *(supervised by food safety inspector; skill: `roles/food-safety-compliance-agent/`)*
- **Traceability analyst** — tracks lots through the supply chain and supports recalls. *(supervised by QA manager; skill: `roles/traceability-analyst/`)*
- **Commodity market analyst** — analyzes prices, basis, and supply-demand for merchandising. *(supervised by grain merchandiser; skill: `roles/commodity-market-analyst/`)*
- **Menu nutrition optimizer** — optimizes menus for nutrition, cost, and dietary needs. *(supervised by dietitian; skill: `roles/menu-nutrition-optimizer/`)*
- **Food assistance eligibility assistant** — screens eligibility and prepares case files for nutrition programs. *(supervised by food assistance program manager; skill: `roles/food-assistance-eligibility-assistant/`)*
- **Autonomous farm operations agent** — orchestrates the whole farm cycle — plans field tasks, sequences machinery and robots, and tracks progress against the crop plan. *(supervised by farmer / ranch manager; skill: `roles/autonomous-farm-operations-agent/`)*
- **Irrigation optimization agent** — schedules and meters irrigation against soil moisture, weather, crop stage, and water availability. *(supervised by irrigation specialist; skill: `roles/irrigation-optimization-agent/`)*
- **Livestock health monitoring agent** — monitors animal health, behavior, and welfare signals and flags issues for the vet. *(supervised by veterinarian / animal health technician; skill: `roles/livestock-health-monitoring-agent/`)*
- **Autonomous machinery dispatch agent** — dispatches and coordinates tractors, drones, and field robots safely across fields. *(supervised by farm operations manager; skill: `roles/autonomous-machinery-dispatch-agent/`)*
- **Soil and nutrient optimization agent** — recommends fertilizer, amendments, and variable-rate inputs from soil, tissue, and yield data. *(supervised by agronomist / soil scientist; skill: `roles/soil-and-nutrient-optimization-agent/`)*

## Humanoid robot roles

- Greenhouse work, sorting, packing, harvesting support where crops are robot-suitable.
- Cold-chain warehouse picking, food-service prep support, sanitation.
- Livestock barn inspection assistance under human supervision.

Dedicated **embodied robot role skills** for this sector (LLM-brained; actions as tool calls via VLA policies):

- **Field crop worker robot** — plant, transplant, weed, thin, scout, and selectively hand-harvest row and field crops. *(embodied robot skill: `robots/field-crop-worker-robot/`)*
- **Orchard and vineyard worker robot** — prune, thin, train, and pick tree fruit, vines, and berries on trellises and canopies. *(embodied robot skill: `robots/orchard-and-vineyard-worker-robot/`)*
- **Livestock and barn handler robot** — feed, bed, move, and inspect animals and assist milking-prep, weighing, and health checks. *(embodied robot skill: `robots/livestock-and-barn-handler-robot/`)*
- **Irrigation and field-infrastructure robot** — install, inspect, and repair irrigation, fencing, and field sensors and take soil and tissue samples. *(embodied robot skill: `robots/irrigation-and-field-infrastructure-robot/`)*

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

## Non-humanoid autonomous machines

Self-driving vehicles, equipment, and drones for this sector (LLM-planned; physical actions as tool calls; ODD + teleoperation fallback):

- **Autonomous tractor** — till, plant, cultivate, and tow implements across fields to a crop plan with no operator in the seat. *(autonomous machine skill: `autonomous/autonomous-tractor/`)*
- **Autonomous harvester / combine** — harvest grain, forage, fruit, or specialty crops and map yield as it goes. *(autonomous machine skill: `autonomous/autonomous-harvester-combine/`)*
- **Crop-scouting drone** — fly fields to scout stand, weeds, pests, disease, and irrigation from the air. *(autonomous machine skill: `autonomous/crop-scouting-drone/`)*
- **Spraying & seeding drone** — apply crop inputs and seed precisely from the air on a prescription map. *(autonomous machine skill: `autonomous/spraying-seeding-drone/`)*

> **How these machines work (assumed architecture):** each is a **non-humanoid autonomous machine** — a foundation/LLM planning brain issues **actions as tool calls** (`follow_route`, `dump_bucket`, `take_off`, `spray_zone`, …) over a perception → prediction → planning → control stack trained on world models, driving/field simulation, and **RLAIF**. Each runs inside a defined **Operational Design Domain (ODD)** with a verified safe-stop and **teleoperation** fallback. Full detail in `_catalogs/autonomous-machines/` and `00-framework/`.

## Human accountability boundary (must stay human-led)

Animal welfare, pesticide decisions, land stewardship, food-safety certification, labor conditions, and public nutrition policy need accountable human owners.

Treat this boundary as a hard constraint. Agents in this sector may sense, interpret, draft, model, monitor, and coordinate up to this line, then must hand off to an accountable human for the decision itself.

## Division of labor (human / AI / robot)

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff, and everything inside the accountability boundary above.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document. Strongest on digital signals and repeatable decision support.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces. Strongest on physical work in human-built environments.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor-impact review.

## Interfaces with other operating systems

This sector regularly depends on and feeds: Water & Sanitation, Transportation & Logistics, Environment & Waste, Health & Care. Coordinate handoffs explicitly; most systemic failures happen at the seams between operating systems.

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

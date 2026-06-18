---
name: "os-17-commerce"
description: "Operating-system orchestrator skill for **Commerce, Retail, Hospitality, and Customer Operations** (national operating system #17). Use this skill whenever work touches this sector's mission — Match demand to goods and services, create satisfying experiences, and keep commercial operations profitable — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself."
---

# Operating System 17 — Commerce, Retail, Hospitality, and Customer Operations

> **Layer:** National operating system (#17 of 23) · **Personnel model:** human-owned, AI- and robot-augmented
> **Cross-references:** `00-framework/` (shared concepts, teaming pattern, accountability), source map `Country-Economy Core Jobs To Be Done.md`

## Mission

Match demand to goods and services, create satisfying experiences, and keep commercial operations profitable.

## When to use this skill

Load this skill when a task concerns commerce, retail, hospitality, and customer operations. It gives an agent the sector map: the outcomes that must be produced, who owns them, what can be automated, and where human accountability is non-negotiable. From here, route to the specific role skills under `roles/` for execution.

## Core Jobs To Be Done

These are the durable outcomes this operating system must reliably produce, written as trigger → response:

1. When people want things, discover demand, stock inventory, price, sell, fulfill, support, and retain.
2. When customers need help, understand intent and resolve issues quickly.
3. When services are delivered in person, coordinate labor, space, safety, and experience.
4. When markets change, adapt offerings and channels.

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

- Retail associate, store manager, merchandiser, buyer.
- Account executive, sales development representative, customer success manager.
- Customer support specialist, contact center manager, support operations analyst.
- Hotel front desk manager, housekeeper, concierge, event manager.
- Restaurant manager, chef, line cook, server, food service worker.
- E-commerce manager, marketplace operations manager, growth marketer.

These remain human-owned. AI personnel and robots augment them; they do not replace the accountable owner.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Associate/agent → team lead/shift → store/restaurant manager → district/regional manager → VP ops; sales: SDR → AE → senior AE → sales manager; support: agent → senior → team lead → support manager.
- **Skills, tools & tech employers list:** POS, CRM (Salesforce, HubSpot), e-commerce (Shopify), helpdesk (Zendesk, Intercom), inventory/merchandising, marketing automation.
- **Qualifications, certifications & licenses:** ServSafe (food), TIPS (alcohol service), CHA (hospitality), Salesforce certifications, CCXP (customer experience), OSHA/forklift (backroom).
- **KPIs / metrics in postings:** Sales/conversion, average order value, CSAT/NPS, first-contact resolution, inventory turns, labor cost %, retention/churn.
- **Where these roles are posted:** Snagajob (hourly retail/restaurant), Indeed, ZipRecruiter, LinkedIn (corporate/sales), Wellfound (e-commerce startups).

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **Sales research agent** — researches accounts and prospects and qualifies leads. *(supervised by account executive; skill: `roles/sales-research-agent/`)*
- **Proposal generator** — drafts tailored proposals and quotes. *(supervised by account executive; skill: `roles/proposal-generator/`)*
- **Customer support agent** — resolves routine requests and escalates edge cases. *(supervised by support manager; skill: `roles/customer-support-agent/`)*
- **Retention analyst** — predicts churn and recommends retention actions. *(supervised by customer success manager; skill: `roles/retention-analyst/`)*
- **Inventory planning agent** — forecasts demand and plans replenishment. *(supervised by buyer / merchandiser; skill: `roles/inventory-planning-agent/`)*
- **Pricing analyst** — recommends prices and promotions within guardrails. *(supervised by category manager; skill: `roles/pricing-analyst/`)*
- **Review summarizer** — summarizes customer reviews and surfaces issues. *(supervised by product/store manager; skill: `roles/review-summarizer/`)*
- **Marketing campaign agent** — drafts and targets marketing campaigns. *(supervised by growth marketer; skill: `roles/marketing-campaign-agent/`)*
- **Distribution & allocation agent** — coordinates wholesale distribution, allocations, and backorders across the network. *(supervised by distribution operations manager; skill: `roles/distribution-allocation-agent/`)*
- **Wholesale assortment & replenishment agent** — plans wholesale assortment and replenishment against demand and terms. *(supervised by buyer / merchandiser; skill: `roles/wholesale-assortment-replenishment-agent/`)*
- **Equipment-rental fleet & pricing agent** — manages rental/leasing fleet utilization, availability, and pricing. *(supervised by rental operations manager; skill: `roles/equipment-rental-fleet-pricing-agent/`)*
- **Repair-service scheduling & estimate agent** — schedules repair and maintenance jobs and drafts estimates. *(supervised by service manager; skill: `roles/repair-service-scheduling-estimate-agent/`)*

## Humanoid robot roles

- Shelf stocking, room-service delivery, housekeeping support, bussing tables, dish handling.
- Retail floor retrieval, queue assistance, event setup.

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

## Non-humanoid autonomous machines

Self-driving vehicles, equipment, and drones for this sector (LLM-planned; physical actions as tool calls; ODD + teleoperation fallback):

- **Warehouse AMR & autonomous forklift fleet** — move pallets, totes, and racks and feed picking across the facility. *(autonomous machine skill: `autonomous/warehouse-amr-autonomous-forklift-fleet/`)*
- **Retail inventory & floor-care robot** — scan shelves for stock and pricing and clean floors autonomously after hours. *(autonomous machine skill: `autonomous/retail-inventory-floor-care-robot/`)*

> **How these machines work (assumed architecture):** each is a **non-humanoid autonomous machine** — a foundation/LLM planning brain issues **actions as tool calls** (`follow_route`, `dump_bucket`, `take_off`, `spray_zone`, …) over a perception → prediction → planning → control stack trained on world models, driving/field simulation, and **RLAIF**. Each runs inside a defined **Operational Design Domain (ODD)** with a verified safe-stop and **teleoperation** fallback. Full detail in `_catalogs/autonomous-machines/` and `00-framework/`.

## Human accountability boundary (must stay human-led)

Brand trust, customer recovery, labor management, alcohol/regulated sales, safety incidents, and high-value negotiation remain human-led.

Treat this boundary as a hard constraint. Agents in this sector may sense, interpret, draft, model, monitor, and coordinate up to this line, then must hand off to an accountable human for the decision itself.

## Division of labor (human / AI / robot)

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff, and everything inside the accountability boundary above.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document. Strongest on digital signals and repeatable decision support.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces. Strongest on physical work in human-built environments.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor-impact review.

## Interfaces with other operating systems

This sector regularly depends on and feeds: Transportation & Logistics, Finance & Markets, Labor & Workforce, Culture & Civic Life. Coordinate handoffs explicitly; most systemic failures happen at the seams between operating systems.

## Strategic missions that draw on this sector

Beyond its own mandate, this operating system is composed by these cross-cutting [strategic missions](../strategic-missions/) (the orthogonal mission axis — a mission pulls roles from several sectors toward one national objective):

- [Strategic Supply Chain](../strategic-missions/strategic-supply-chain/)

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

- **Risk here:** Service staff lose customer-recovery craft; managers lose operational intuition.
- **Countermeasures:** Preserve human service and escalation skills; scenario training.
- **Role/job simulators (keep-warm):** Service-recovery and difficult-customer role-play simulators; operations-scenario drills.

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

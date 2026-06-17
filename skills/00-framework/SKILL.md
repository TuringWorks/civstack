---
name: "country-economy-jtbd-index"
description: "Index and shared framework for the Country-Economy Jobs-To-Be-Done skill library: 22 national operating systems, their AI-personnel role skills, 12 cross-cutting archetypes, and the AI/robot catalogs. Use this skill first to navigate the library, understand the shared teaming pattern and accountability model, and find the right operating-system or role skill for any economic task."
---

# Country-Economy JTBD Skill Library — Framework & Index

This library turns the document *Country-Economy Core Jobs To Be Done* into deployable skills. It is organized so an LLM or agent can find the right context for any job in a modern economy, understand the human/AI/robot division of labor, and respect the human-accountability boundaries.

## How the library is organized

- `00-framework/` — this index plus the shared concepts every skill assumes (you are here).
- `01-…` through `22-…` — one folder per **national operating system**. Each has a sector `SKILL.md` (orchestrator) and a `roles/` subfolder of **AI-personnel role skills**.
- `strategic-missions/` — **cross-cutting national missions** (energy abundance, semiconductor sovereignty, bioeconomy, frontier-AI production, quantum & space, strategic supply chain, science-to-industry, talent formation, public procurement, cyber defense, advanced manufacturing, digital infrastructure). A mission is an *orthogonal axis* to the 22 sectors: it composes several of them toward one objective.
- `cross-cutting-archetypes/` — the 12 role patterns (Strategist, Operator, Builder, …) that recur in every sector.
- `_catalogs/human-command/` — **accountable human owners** for the strategic missions and cross-cutting authority (national technology strategist, AI governance lead, import/export compliance lead, procurement innovation lead).
- `_catalogs/ai-personnel/` and `_catalogs/humanoid-robots/` — reusable cross-economy role patterns.
- `_catalogs/autonomous-machines/` — **non-humanoid** autonomous platforms: self-driving cars/trucks/shuttles, autonomous tractors and harvesters, loaders and earthmovers, mining haul trucks, drones (survey, spray, delivery), warehouse movers, and surface vessels. Several sectors also nest domain-specific machines under `<sector>/autonomous/` (e.g. `05-food/autonomous/`, `11-transportation/autonomous/`, `08-mining/autonomous/`).
- `_catalogs/embodied-ai-stack/` — the roles that **build and operate** both the LLM-brained robots and the autonomous machines: brain/autonomy orchestrator, VLA policy engineer, world-model engineer, robot-gym/sim-to-real engineer, RLAIF pipeline engineer, evaluation/red-team agent, fleet safety officer, teleoperation operator, fleet operations agent, and data/telemetry engineer.
- `_catalogs/autonomous-fleet-ops/` — the **operations layer for autonomous vehicle/machine fleets**: ODD & safety-case engineer, remote-operations (teleop) center supervisor, HD mapping & localization engineer, V2X/connectivity & infrastructure engineer, homologation & regulatory lead, depot/maintenance lead, in-field safety operator, and incident/disengagement analyst.
- `_catalogs/capability-optimization/` — the **how-it's-built layer**: the model tiers (LLM, SLM, tiny LM, deterministic) and the spectrum of optimization methods (imitation, model-based/offline RL, RLHF/RLAIF, sim-to-real, distillation/compression, classical control, search, formal methods) with the roles that select and run them. **RLAIF is one option among many.**
- `_catalogs/simulation-training/` — the **anti-deskilling / keep-warm layer**: job and role simulators that keep humans current, rebuild the learning ladder, and capture tacit knowledge — reusing the machine-training world models. Curriculum designer, scenario-generation agent, competency/certification agent, drill & exercise coordinator, dual-use world-model/fidelity engineer, and tacit-knowledge capture agent. See `docs/role-simulation-and-keepwarm.md`.

## The shared model every skill assumes

**A job is a durable outcome society must reliably produce. A role is one way to own, coordinate, or execute it.** AI personnel and robots occupy portions of roles; legal, moral, and political accountability stays with humans and institutions.

**The universal seven-step lifecycle** (used in every skill):

- **Sense reality** — gather data, observe conditions, inspect sources, listen to people.
- **Interpret reality** — diagnose, forecast, model risk, prioritize.
- **Decide** — choose policy, design, action, allocation, escalation, or tradeoff.
- **Mobilize** — assign labor, budget, materials, rights, permissions, logistics, schedule.
- **Execute** — perform the work in digital or physical space.
- **Verify** — test, audit, measure, inspect, certify, and learn.
- **Govern** — maintain legitimacy, safety, accountability, continuity, and trust.

**The five-layer role design pattern** (used to staff every job):

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor impact.

**How robot personnel are built (assumed architecture).** Robot roles in this library are **LLM-brained embodied agents**: a multimodal LLM *brain* perceives, plans, and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), which are executed by **Vision-Language-Action (VLA) policies** trained on **world models** (learned physics simulators), **robot gyms** (massively parallel sim-to-real), and **RLAIF** (reinforcement learning from AI feedback). Fleets may share one brain model or mix specialized ones (a deliberative orchestrator over fast reactive controllers). A **verified low-level safety layer** can refuse or override unsafe tool calls independently of the brain. The roles that build and operate this stack live in `_catalogs/embodied-ai-stack/`. The **same brain-and-tool-calls model extends to non-humanoid autonomous machines** (vehicles, farm equipment, loaders, drones), which add an Operational Design Domain, SAE levels, a verified safe-stop, and a teleoperation fallback (`_catalogs/autonomous-machines/`, `_catalogs/autonomous-fleet-ops/`).

**Capability is right-sized, not one-size — and RLAIF is one method among many.** The brain need not be a single large model trained one way. Capabilities are spread across **model tiers** — LLM, SLM, tiny LM, and **deterministic controllers** — and built with a **spectrum of methods**: imitation/behavior cloning, model-based and offline RL, RLHF/RLAIF, sim-to-real, self-supervised pretraining, supervised fine-tuning, **distillation and compression**, search/planning, classical optimization and control, and **formal verification**. Each capability is assigned to the *smallest, most deterministic* tier and the *most efficient* method that meets its accuracy, latency, and safety bar — with a verified deterministic safety layer beneath anything learned. The roles that select and run this spectrum live in `_catalogs/capability-optimization/`.

**Guarding against deskilling.** Automating routine work erodes the human fallback bench, tacit judgment, and the learning ladder. Every sector skill carries a *Deskilling watch & keep-warm* section (its specific risk, countermeasures, and a job/role-simulator regime), OS 22 (Resilience) owns the cross-sector drill program, and `_catalogs/simulation-training/` holds the roles that run it. The key idea: the **world models and simulators built to train the machines double as the keep-warm simulators that keep humans current and rebuild the learning ladder** — one simulation substrate, two students. See `docs/role-simulation-and-keepwarm.md`.

## The command & cadence model (how delegation actually runs)

The five-layer pattern says *who* is on the team; this says *how they run together* without losing accountability. Every role and mission assumes it.

**Three-layer workforce.** Human command owns accountable judgment, authority, trust, ethics, and signoff (and must never lose ownership, legitimacy, escalation, redress). AI personnel own research, drafting, coding, monitoring, simulation, and coordination (and must never lose evidence, uncertainty, constraints, logs). Robot/machine personnel own bounded physical execution (and must never lose the safety envelope, human override, physical proof).

**The operating loop** (run it for any delegated work):

1. **Mission assignment** — the human owner sets objective, constraints, success criteria, and risk tier.
2. **Context loading** — agents load approved data, policies, tools, maps, and current state.
3. **Task decomposition** — separate research, planning, execution, monitoring, verification.
4. **Delegation** — AI does cognitive work; robots/machines do approved physical work; humans hold judgment and exceptions.
5. **Verification** — check outputs against metrics, evidence, tests, inspections, and human-review thresholds.
6. **Escalation** — uncertainty, rights impact, safety risk, conflict, or policy ambiguity triggers human command.
7. **Learning** — incidents, failures, and successful patterns update SOPs, evals, prompts, maps, and training.

**Delegation rules.** Delegate to **AI** when the work is text, code, data, classification, monitoring, forecasting, simulation, routing, or first-draft synthesis. Delegate to **robots/machines** when it is fetch, carry, inspect, clean, sort, stage, load, unload, scan, guide, or repeatable manipulation in a bounded environment. **Keep with humans** when it involves force, rights, consent, accountability, public legitimacy, final professional signoff, scarce-resource triage, or unresolved ethical tradeoffs.

**Required control surfaces:** role charter, context pack, tool permissions, evidence log, evaluation, incident path, review cadence.

**Command cadence:** real-time (safety, incidents, outages, cyber, public-safety escalations); daily (queues, uptime, throughput, exceptions); weekly (metrics, quality drift, cost, adoption, workforce impact); monthly (risk register, eval results, audits, policy); quarterly (role redesign, procurement, capacity, training, public trust, resilience).

**Three failure modes to design against:** automation without an accountable owner; AI output treated as a final decision; a robot's task envelope expanding informally. *(See `checklists/` for the deployment gates and `templates/` for role/agent/robot briefs.)*

**Universal, not US-specific.** The jobs are invariant across nations; *ownership, formality, and capacity* are local variables. Every skill carries a "context modifiers" section so it can be adapted to any nation — any size, geography, income level, or political system.

## The 22 operating systems

| # | Operating system | Role skills |
|---|---|---|
| 01 | [Governance, Law, and Public Administration](01-governance/) | 5 AI roles |
| 02 | [Public Finance, Tax, Treasury, and Procurement](02-public-finance/) | 9 AI roles |
| 03 | [Defense, Intelligence, Border, and Foreign Affairs](03-defense/) | 8 AI roles |
| 04 | [Public Safety, Justice Operations, and Emergency Response](04-public-safety/) | 9 AI roles |
| 05 | [Food, Agriculture, Fisheries, and Nutrition](05-food/) | 13 AI roles |
| 06 | [Water, Sanitation, and Public Hygiene](06-water/) | 6 AI roles |
| 07 | [Energy, Utilities, and Grid Operations](07-energy/) | 7 AI roles |
| 08 | [Mining, Materials, Chemicals, and Industrial Inputs](08-mining/) | 6 AI roles |
| 09 | [Manufacturing and Industrial Production](09-manufacturing-and-industrial-production/) | 8 AI roles |
| 10 | [Shelter, Construction, Land, and the Built Environment](10-shelter/) | 8 AI roles |
| 11 | [Transportation, Logistics, Postal, and Mobility](11-transportation/) | 7 AI roles |
| 12 | [Communications, Software, Cybersecurity, and Digital Infrastructure](12-communications/) | 11 AI roles |
| 13 | [Healthcare, Public Health, and Biomedical Systems](13-healthcare/) | 9 AI roles |
| 14 | [Education, Training, Libraries, and Human Capital](14-education/) | 9 AI roles |
| 15 | [Science, Research, Standards, and Innovation](15-science/) | 9 AI roles |
| 16 | [Finance, Insurance, Payments, and Capital Markets](16-finance/) | 8 AI roles |
| 17 | [Commerce, Retail, Hospitality, and Customer Operations](17-commerce/) | 8 AI roles |
| 18 | [Media, Culture, Arts, Sports, Religion, and Civic Life](18-media/) | 7 AI roles |
| 19 | [Environment, Climate, Waste, and Resource Stewardship](19-environment/) | 6 AI roles |
| 20 | [Labor, Workforce Systems, and Organizational Life](20-labor/) | 8 AI roles |
| 21 | [Household, Childcare, Eldercare, and Community Support](21-household/) | 7 AI roles |
| 22 | [Resilience, Continuity, and Strategic Foresight](22-resilience/) | 6 AI roles |

## The 12 strategic missions (the other axis)

Missions are cross-cutting national capabilities that compose several sectors toward one objective. Use them when the goal is a capability rather than a sector.

| Strategic mission | Composes operating systems |
|---|---|
| [Energy Abundance](strategic-missions/energy-abundance/) | 07, 16, 10, 11, 08, 22 |
| [Semiconductor Sovereignty](strategic-missions/semiconductor-sovereignty/) | 08, 09, 15, 12, 03, 11 |
| [Bioeconomy](strategic-missions/bioeconomy/) | 13, 05, 15, 08, 19, 03 |
| [Frontier AI Production](strategic-missions/frontier-ai-production/) | 12, 15, 07, 08, 20 |
| [Quantum and Space Systems](strategic-missions/quantum-and-space-systems/) | 15, 08, 09, 03, 12 |
| [Strategic Supply Chain](strategic-missions/strategic-supply-chain/) | 11, 08, 16, 03, 17, 22 |
| [Science-to-Industry](strategic-missions/science-to-industry/) | 15, 09, 02, 14, 16 |
| [Frontier Talent Formation](strategic-missions/frontier-talent-formation/) | 14, 20, 15 |
| [Public Procurement for Frontier Technology](strategic-missions/public-procurement-for-frontier-technology/) | 02, 01, 15 |
| [Cyber Defense](strategic-missions/cyber-defense/) | 12, 03, 22, 04 |
| [Advanced Manufacturing](strategic-missions/advanced-manufacturing/) | 09, 08, 11, 20, 15 |
| [Digital Infrastructure](strategic-missions/digital-infrastructure/) | 12, 07, 16, 01 |

## How to use this library

1. **Start here** to orient.
2. Open the **operating-system skill** for the relevant sector to get the mission, JTBD, roster, and accountability boundary.
3. Deploy the specific **role skill(s)** under that sector's `roles/` for execution, or an **archetype**/**catalog** skill for a cross-sector pattern.
4. Always run the seven-step lifecycle and stop at the human-accountability boundary.

## Deployment order (high-leverage first)

1. Back-office document work (permits, benefits, procurement, compliance, finance ops).
2. Monitoring and triage (cyber, infrastructure telemetry, health surveillance, fraud).
3. Customer/citizen service (intake, routing, status, routine support).
4. Planning and simulation (budgets, logistics, energy load, disaster scenarios).
5. Software and data infrastructure (coding, test, data-quality, analytics agents).
6. Physical logistics (warehouses, hospitals, hotels, labs, factories, facilities).
7. Inspection and maintenance (utilities, plants, buildings, roads, farms, sites).
8. Care support (reduce burden around care; do not replace caregivers).
9. Hazardous response (robots first into dangerous, dirty, dull, degraded environments).

## Work that should stay human-led (applies across all skills)

Coercive state power; rights-impacting decisions; intimate human care; democratic legitimacy; high-consequence safety; ethical and social tradeoffs; and final accountability for AI deployment, model-risk acceptance, incident response, and redress.

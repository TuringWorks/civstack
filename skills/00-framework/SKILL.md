---
name: country-economy-jtbd-index
description: Index and shared framework for the Country-Economy Jobs-To-Be-Done skill library: 22 national operating systems, their AI-personnel role skills, 12 cross-cutting archetypes, and the AI/robot catalogs. Use this skill first to navigate the library, understand the shared teaming pattern and accountability model, and find the right operating-system or role skill for any economic task.
---

# Country-Economy JTBD Skill Library — Framework & Index

This library turns the document *Country-Economy Core Jobs To Be Done* into deployable skills. It is organized so an LLM or agent can find the right context for any job in a modern economy, understand the human/AI/robot division of labor, and respect the human-accountability boundaries.

## How the library is organized

- `00-framework/` — this index plus the shared concepts every skill assumes (you are here).
- `01-…` through `22-…` — one folder per **national operating system**. Each has a sector `SKILL.md` (orchestrator) and a `roles/` subfolder of **AI-personnel role skills**.
- `cross-cutting-archetypes/` — the 12 role patterns (Strategist, Operator, Builder, …) that recur in every sector.
- `_catalogs/ai-personnel/` and `_catalogs/humanoid-robots/` — reusable cross-economy role patterns.
- `_catalogs/embodied-ai-stack/` — the roles that **build and operate** the LLM-brained robots: brain orchestrator, VLA policy engineer, world-model engineer, robot-gym/sim-to-real engineer, RLAIF pipeline engineer, evaluation/red-team agent, fleet safety officer, teleoperation operator, fleet operations agent, and data/telemetry engineer.

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

**How robot personnel are built (assumed architecture).** Robot roles in this library are **LLM-brained embodied agents**: a multimodal LLM *brain* perceives, plans, and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), which are executed by **Vision-Language-Action (VLA) policies** trained on **world models** (learned physics simulators), **robot gyms** (massively parallel sim-to-real), and **RLAIF** (reinforcement learning from AI feedback). Fleets may share one brain model or mix specialized ones (a deliberative orchestrator over fast reactive controllers). A **verified low-level safety layer** can refuse or override unsafe tool calls independently of the brain. The roles that build and operate this stack live in `_catalogs/embodied-ai-stack/`.

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

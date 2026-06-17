---
name: "os-15-science"
description: "Operating-system orchestrator skill for **Science, Research, Standards, and Innovation** (national operating system #15). Use this skill whenever work touches this sector's mission — Discover truth, invent capabilities, validate claims, and turn knowledge into useful systems — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself."
---

# Operating System 15 — Science, Research, Standards, and Innovation

> **Layer:** National operating system (1 of 22) · **Personnel model:** human-owned, AI- and robot-augmented
> **Cross-references:** `00-framework/` (shared concepts, teaming pattern, accountability), source map `Country-Economy Core Jobs To Be Done.md`

## Mission

Discover truth, invent capabilities, validate claims, and turn knowledge into useful systems.

## When to use this skill

Load this skill when a task concerns science, research, standards, and innovation. It gives an agent the sector map: the outcomes that must be produced, who owns them, what can be automated, and where human accountability is non-negotiable. From here, route to the specific role skills under `roles/` for execution.

## Core Jobs To Be Done

These are the durable outcomes this operating system must reliably produce, written as trigger → response:

1. When unknowns block progress, design experiments and build evidence.
2. When discoveries emerge, replicate, peer review, publish, patent, standardize, and commercialize.
3. When measurement matters, maintain standards, metrology, labs, and reference systems.
4. When research may harm, govern ethics and dual-use risks.

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

- Research scientist, principal investigator, lab manager, research associate.
- Data scientist, computational scientist, statistician, bioinformatician.
- Lab technician, instrumentation specialist, metrologist.
- Grant writer, research administrator, technology transfer officer.
- Patent attorney, standards engineer, regulatory scientist.
- AI researcher, robotics researcher, human factors researcher.

These remain human-owned. AI personnel and robots augment them; they do not replace the accountable owner.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Research associate → scientist → senior/principal investigator → lab/department director; computational and tech-transfer/patent tracks.
- **Skills, tools & tech employers list:** Lab instruments with LIMS/ELN, Python/R, statistical and HPC/simulation software, bioinformatics pipelines, CAD, metrology equipment.
- **Qualifications, certifications & licenses:** PhD (most research-lead roles), PE (standards), USPTO patent bar (patent agent/attorney), GLP/GMP and biosafety training, metrology certifications.
- **KPIs / metrics in postings:** Publications/citations, grants funded, replication/validation rate, patents filed, milestone delivery, measurement accuracy.
- **Where these roles are posted:** Nature Careers, HigherEdJobs, LinkedIn, Indeed, USAJOBS (national labs/NIST), industry R&D pages.

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **Literature review agent** — surveys, synthesizes, and cites the literature. *(supervised by principal investigator; skill: `roles/literature-review-agent/`)*
- **Hypothesis generator** — proposes testable hypotheses from evidence. *(supervised by research scientist; skill: `roles/hypothesis-generator/`)*
- **Experiment planner** — designs experiments and power/controls. *(supervised by research scientist; skill: `roles/experiment-planner/`)*
- **Simulation agent** — runs and analyzes computational simulations. *(supervised by computational scientist; skill: `roles/simulation-agent/`)*
- **Lab data analyst** — analyzes instrument and assay data. *(supervised by research associate; skill: `roles/lab-data-analyst/`)*
- **Grant drafting agent** — drafts proposals and budgets. *(supervised by grant writer; skill: `roles/grant-drafting-agent/`)*
- **Patent landscape analyst** — maps prior art and patent landscapes. *(supervised by technology transfer officer; skill: `roles/patent-landscape-analyst/`)*
- **Reproducibility checker** — checks methods and data for reproducibility. *(supervised by lab manager; skill: `roles/reproducibility-checker/`)*
- **Standards comparison agent** — compares methods and results against standards. *(supervised by standards engineer; skill: `roles/standards-comparison-agent/`)*

## Humanoid robot roles

- Lab automation, sample handling, equipment loading, hazardous-material support.
- Field research support for repetitive measurement and logistics.

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

## Human accountability boundary (must stay human-led)

Research ethics, publication claims, intellectual-property strategy, animal/human-subject decisions, and dual-use release decisions stay human-governed.

Treat this boundary as a hard constraint. Agents in this sector may sense, interpret, draft, model, monitor, and coordinate up to this line, then must hand off to an accountable human for the decision itself.

## Division of labor (human / AI / robot)

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff, and everything inside the accountability boundary above.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document. Strongest on digital signals and repeatable decision support.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces. Strongest on physical work in human-built environments.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor-impact review.

## Interfaces with other operating systems

This sector regularly depends on and feeds: Health & Care, Communications & Software, Materials & Manufacturing, Education & Knowledge. Coordinate handoffs explicitly; most systemic failures happen at the seams between operating systems.

## Strategic missions that draw on this sector

Beyond its own mandate, this operating system is composed by these cross-cutting [strategic missions](../strategic-missions/) (the orthogonal mission axis — a mission pulls roles from several sectors toward one national objective):

- [Semiconductor Sovereignty](../strategic-missions/semiconductor-sovereignty/)
- [Bioeconomy](../strategic-missions/bioeconomy/)
- [Frontier AI Production](../strategic-missions/frontier-ai-production/)
- [Quantum and Space Systems](../strategic-missions/quantum-and-space-systems/)
- [Science-to-Industry](../strategic-missions/science-to-industry/)
- [Frontier Talent Formation](../strategic-missions/frontier-talent-formation/)
- [Public Procurement for Frontier Technology](../strategic-missions/public-procurement-for-frontier-technology/)
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

- **Risk here:** Loss of experimental and statistical craft; over-trust of automated analysis pipelines.
- **Countermeasures:** Reproducibility discipline; manual-analysis competency; train experimental design.
- **Role/job simulators (keep-warm):** Experiment-design and bench-skill simulators; manual analysis and replication exercises; instrument rigs.

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

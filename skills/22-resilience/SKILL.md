---
name: "os-22-resilience"
description: "Operating-system orchestrator skill for **Resilience, Continuity, and Strategic Foresight** (national operating system #22). Use this skill whenever work touches this sector's mission — Keep the country functioning through shocks and long-range change — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself."
---

# Operating System 22 — Resilience, Continuity, and Strategic Foresight

> **Layer:** National operating system (#22 of 23) · **Personnel model:** human-owned, AI- and robot-augmented
> **Cross-references:** `00-framework/` (shared concepts, teaming pattern, accountability), source map `Country-Economy Core Jobs To Be Done.md`

## Mission

Keep the country functioning through shocks and long-range change.

## When to use this skill

Load this skill when a task concerns resilience, continuity, and strategic foresight. It gives an agent the sector map: the outcomes that must be produced, who owns them, what can be automated, and where human accountability is non-negotiable. From here, route to the specific role skills under `roles/` for execution.

## Core Jobs To Be Done

These are the durable outcomes this operating system must reliably produce, written as trigger → response:

1. When risks accumulate slowly, identify weak signals and prepare before failure.
2. When shocks hit, maintain continuity of government, food, water, energy, health, finance, communications, and logistics.
3. When recovery begins, coordinate claims, rebuilding, mental health, supply chains, and accountability.
4. When future scenarios diverge, stress-test systems and invest in options.

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

- Enterprise risk manager, business continuity manager, emergency planner.
- National security planner, infrastructure resilience analyst, scenario planner.
- Supply chain risk manager, insurance catastrophe modeler.
- Crisis communications lead, recovery program manager, mutual aid coordinator.

These remain human-owned. AI personnel and robots augment them; they do not replace the accountable owner.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Analyst → BCM/risk specialist → manager → director of resilience/BCDR; emergency planner → senior → CEM; supply-chain-risk and catastrophe-modeling tracks.
- **Skills, tools & tech employers list:** BCM platforms (Fusion, Archer), GRC, risk registers, scenario/simulation tools, supply-chain mapping, catastrophe models (Moody's RMS, Verisk), GIS.
- **Qualifications, certifications & licenses:** CBCP/MBCP (DRI), CEM, PMP, FRM, ISO 22301 lead auditor, CISSP (cyber-resilience).
- **KPIs / metrics in postings:** RTO/RPO achievement, exercise/test pass rate, time-to-recover, single-point-of-failure coverage, claims throughput.
- **Where these roles are posted:** LinkedIn, Indeed, DRI/continuity boards, USAJOBS/GovernmentJobs (emergency management), ClearanceJobs.

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **Scenario generation agent** — generates and stress-tests future scenarios. *(supervised by scenario planner; skill: `roles/scenario-generation-agent/`)*
- **Dependency mapping agent** — maps cross-system dependencies and single points of failure. *(supervised by infrastructure resilience analyst; skill: `roles/dependency-mapping-agent/`)*
- **Crisis dashboard analyst** — maintains a live cross-sector situational picture. *(supervised by emergency planner; skill: `roles/crisis-dashboard-analyst/`)*
- **Continuity plan reviewer** — reviews and tests business-continuity plans. *(supervised by business continuity manager; skill: `roles/continuity-plan-reviewer/`)*
- **Supply disruption monitor** — monitors supply chains for disruption signals. *(supervised by supply chain risk manager; skill: `roles/supply-disruption-monitor/`)*
- **Claims triage agent** — triages post-disaster claims and aid requests. *(supervised by recovery program manager; skill: `roles/claims-triage-agent/`)*
- **Strategic-reserve optimization agent** — sizes and positions reserves and redundancy for existential inputs (energy, water, food, medicine, payments) against worst-credible shocks. *(supervised by continuity director / resilience lead; skill: `roles/strategic-reserve-optimization-agent/`)*

## Humanoid robot roles

- Emergency warehousing, shelter operations, debris assessment, field logistics, hazardous support.

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

## Human accountability boundary (must stay human-led)

Political prioritization, emergency powers, scarce-resource allocation, evacuation orders, and recovery justice require human legitimacy.

Treat this boundary as a hard constraint. Agents in this sector may sense, interpret, draft, model, monitor, and coordinate up to this line, then must hand off to an accountable human for the decision itself.

## Division of labor (human / AI / robot)

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff, and everything inside the accountability boundary above.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document. Strongest on digital signals and repeatable decision support.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces. Strongest on physical work in human-built environments.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor-impact review.

## Interfaces with other operating systems

This sector regularly depends on and feeds: Public Safety & Justice, Defense & Intelligence, Public Finance, Energy & Utilities. Coordinate handoffs explicitly; most systemic failures happen at the seams between operating systems.

## Strategic missions that draw on this sector

Beyond its own mandate, this operating system is composed by these cross-cutting [strategic missions](../strategic-missions/) (the orthogonal mission axis — a mission pulls roles from several sectors toward one national objective):

- [Energy Abundance](../strategic-missions/energy-abundance/)
- [Strategic Supply Chain](../strategic-missions/strategic-supply-chain/)
- [Cyber Defense](../strategic-missions/cyber-defense/)

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

- **Risk here:** The meta-owner — continuity planning and the fallback bench themselves can deskill.
- **Countermeasures:** Owns the cross-cutting program: fallback-readiness drills and metrics across all 21 other operating systems.
- **Role/job simulators (keep-warm):** Cross-sector tabletop and full-scale continuity exercises; runs the keep-warm program and bench-readiness metrics for every OS.

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

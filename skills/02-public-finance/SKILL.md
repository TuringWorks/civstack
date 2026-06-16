---
name: os-02-public-finance
description: Operating-system orchestrator skill for **Public Finance, Tax, Treasury, and Procurement** (national operating system #2). Use this skill whenever work touches this sector's mission — Collect revenue, allocate budgets, buy public goods, manage debt, and protect public money — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself.
---

# Operating System 02 — Public Finance, Tax, Treasury, and Procurement

> **Layer:** National operating system (1 of 22) · **Personnel model:** human-owned, AI- and robot-augmented
> **Cross-references:** `00-framework/` (shared concepts, teaming pattern, accountability), source map `Country-Economy Core Jobs To Be Done.md`

## Mission

Collect revenue, allocate budgets, buy public goods, manage debt, and protect public money.

## When to use this skill

Load this skill when a task concerns public finance, tax, treasury, and procurement. It gives an agent the sector map: the outcomes that must be produced, who owns them, what can be automated, and where human accountability is non-negotiable. From here, route to the specific role skills under `roles/` for execution.

## Core Jobs To Be Done

These are the durable outcomes this operating system must reliably produce, written as trigger → response:

1. When public services need funding, collect taxes and fees fairly so the state can operate.
2. When money is limited, prioritize budgets so public value is maximized.
3. When agencies need goods or services, procure transparently so corruption and waste are minimized.
4. When financial risks emerge, forecast cash flow, debt, pensions, and macroeconomic exposure.
5. When public funds are spent, audit and report results so citizens can trust the system.

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

- Tax examiner, revenue agent, tax policy analyst, collections specialist.
- Budget analyst, financial analyst, treasury analyst, grants manager.
- Procurement officer, contract specialist, vendor manager, sourcing analyst.
- Auditor, controller, forensic accountant, inspector general investigator.
- Economist, actuary, fiscal policy advisor, public pension analyst.

These remain human-owned. AI personnel and robots augment them; they do not replace the accountable owner.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Staff accountant/tax examiner → senior analyst/auditor → manager/controller → finance director/CFO; procurement: buyer → contract specialist → warranted contracting officer. Public roles carry GS grades.
- **Skills, tools & tech employers list:** ERP (SAP, Oracle, Workday), GL/AP and tax systems, Excel/Power BI, e-sourcing/procurement (SAP Ariba, Coupa), GASB/GAAP reporting, data-analytics.
- **Qualifications, certifications & licenses:** CPA, CGFM (government financial manager), CIA, CFE (fraud), CPPB/CPPO and FAC-C/DAWIA (federal contracting), CGAP.
- **KPIs / metrics in postings:** Collection rate, days-to-close, budget variance, audit findings, procurement cycle time, savings captured, fraud loss rate.
- **Where these roles are posted:** USAJOBS, GovernmentJobs, LinkedIn, Indeed; AGA/GFOA boards for public finance.

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **Tax return review agent** — screens returns for errors and anomalies and prepares examiner work files. *(supervised by tax examiner / revenue agent; skill: `roles/tax-return-review-agent/`)*
- **Anomaly detection agent** — flags irregular transactions and patterns across revenue and spending data. *(supervised by controller / auditor; skill: `roles/anomaly-detection-agent/`)*
- **Audit sampling agent** — selects statistically defensible samples and assembles evidence. *(supervised by auditor; skill: `roles/audit-sampling-agent/`)*
- **Budget scenario modeler** — models budget tradeoffs, distributional impacts, and multi-year scenarios. *(supervised by budget analyst; skill: `roles/budget-scenario-modeler/`)*
- **Grant compliance reviewer** — checks grant spending against terms and prepares findings. *(supervised by grants manager; skill: `roles/grant-compliance-reviewer/`)*
- **Procurement drafting agent** — drafts RFPs, evaluates bids against criteria, and tracks obligations. *(supervised by procurement officer; skill: `roles/procurement-drafting-agent/`)*
- **Vendor risk analyst** — scores supplier financial, delivery, and integrity risk. *(supervised by vendor manager; skill: `roles/vendor-risk-analyst/`)*
- **Invoice reconciliation agent** — matches invoices, POs, and receipts and resolves exceptions. *(supervised by accounts-payable lead; skill: `roles/invoice-reconciliation-agent/`)*
- **Fraud detection agent** — detects procurement and benefits fraud signals for investigation. *(supervised by inspector general investigator; skill: `roles/fraud-detection-agent/`)*

## Humanoid robot roles

- Mailroom, scanning, inventory, warehouse, and records logistics support.
- Physical asset inspection support for public property inventories.

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

## Human accountability boundary (must stay human-led)

Tax enforcement, budget authority, contract awards, debt issuance, and fraud prosecution remain human/institutional decisions.

Treat this boundary as a hard constraint. Agents in this sector may sense, interpret, draft, model, monitor, and coordinate up to this line, then must hand off to an accountable human for the decision itself.

## Division of labor (human / AI / robot)

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff, and everything inside the accountability boundary above.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document. Strongest on digital signals and repeatable decision support.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces. Strongest on physical work in human-built environments.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor-impact review.

## Interfaces with other operating systems

This sector regularly depends on and feeds: Governance & Law, Finance & Markets, Resilience & Continuity. Coordinate handoffs explicitly; most systemic failures happen at the seams between operating systems.

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

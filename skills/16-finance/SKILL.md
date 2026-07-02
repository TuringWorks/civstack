---
name: "os-16-finance"
description: "Operating-system orchestrator skill for **Finance, Insurance, Payments, and Capital Markets** (national operating system #16). Use this skill whenever work touches this sector's mission — Move money, price risk, allocate capital, protect savings, and enable commerce — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself."
---

# Operating System 16 — Finance, Insurance, Payments, and Capital Markets

> **Layer:** National operating system (#16 of 23) · **Personnel model:** human-owned, AI- and robot-augmented
> **Cross-references:** `00-framework/` (shared concepts, teaming pattern, accountability), source map `Country-Economy Core Jobs To Be Done.md`

## Mission

Move money, price risk, allocate capital, protect savings, and enable commerce.

## When to use this skill

Load this skill when a task concerns finance, insurance, payments, and capital markets. It gives an agent the sector map: the outcomes that must be produced, who owns them, what can be automated, and where human accountability is non-negotiable. From here, route to the specific role skills under `roles/` for execution.

## Core Jobs To Be Done

These are the durable outcomes this operating system must reliably produce, written as trigger → response:

1. When people and firms transact, move money reliably and prevent fraud.
2. When capital is needed, assess risk and allocate funds.
3. When uncertainty exists, insure, hedge, reserve, and regulate.
4. When records matter, account, audit, report, and comply.
5. When consumers need financial help, advise within fiduciary and suitability boundaries.

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

- Banker, loan officer, credit analyst, underwriter.
- Accountant, auditor, controller, financial reporting manager.
- Actuary, risk analyst, compliance analyst, model risk manager.
- Trader, portfolio manager, investment analyst, wealth advisor.
- Claims adjuster, insurance agent, fraud investigator.
- Payments operations analyst, AML analyst, sanctions analyst.
- Fintech product manager, quant researcher, AI risk lead.

These remain human-owned. AI personnel and robots augment them; they do not replace the accountable owner.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Analyst → associate → VP → director → MD (banking); accountant → senior → manager → controller → CFO; actuarial exam ladder; trader/portfolio manager.
- **Skills, tools & tech employers list:** Excel/VBA, Bloomberg/FactSet, SQL/Python, ERP and core-banking, risk systems, AML/KYC platforms (NICE Actimize, World-Check), actuarial software.
- **Qualifications, certifications & licenses:** CPA, CFA, FRM, CAIA, actuarial (ASA/FSA, ACAS/FCAS), CAMS (AML), FINRA Series 7/63/66/24, CFP (advisors).
- **KPIs / metrics in postings:** P&L/return, risk-adjusted metrics (Sharpe, VaR), loss/default and fraud-loss rates, close cycle, regulatory-reporting accuracy, NPS.
- **Where these roles are posted:** eFinancialCareers, LinkedIn, Indeed, Wellfound (fintech), Glassdoor.

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **KYC/AML review agent** — screens identities and transactions for financial-crime risk. *(supervised by AML analyst; skill: `roles/kyc-aml-review-agent/`)*
- **Fraud detection agent** — detects fraud patterns across transactions. *(supervised by fraud investigator; skill: `roles/fraud-detection-agent/`)*
- **Credit memo drafter** — drafts credit analyses and memos from financials. *(supervised by credit analyst; skill: `roles/credit-memo-drafter/`)*
- **Portfolio research agent** — researches securities and positions. *(supervised by investment analyst; skill: `roles/portfolio-research-agent/`)*
- **Insurance claims triage agent** — classifies and routes claims and flags fraud. *(supervised by claims adjuster; skill: `roles/insurance-claims-triage-agent/`)*
- **Reconciliation agent** — reconciles ledgers, accounts, and statements. *(supervised by controller; skill: `roles/reconciliation-agent/`)*
- **Regulatory reporting assistant** — prepares regulatory filings and disclosures. *(supervised by financial reporting manager; skill: `roles/regulatory-reporting-assistant/`)*
- **Financial planning copilot** — models plans within suitability constraints. *(supervised by wealth advisor; skill: `roles/financial-planning-copilot/`)*
- **Pricing & ratemaking agent** — develops rate-adequacy analyses, GLM-based pricing, and rate-filing support within actuarial standards of practice. *(supervised by pricing actuary; skill: `roles/pricing-ratemaking-agent/`)*
- **Reserving & loss-development agent** — builds loss-development triangles and IBNR estimates (chain-ladder, Bornhuetter-Ferguson) for the reserving actuary. *(supervised by reserving actuary; skill: `roles/reserving-loss-development-agent/`)*
- **Actuarial valuation & solvency-reporting agent** — prepares reserves, capital, and disclosures under IFRS 17, Solvency II, and US Stat/RBC for review by the appointed actuary. *(supervised by valuation / appointed actuary; skill: `roles/actuarial-valuation-solvency-reporting-agent/`)*
- **Experience-study & mortality agent** — runs experience studies and mortality, morbidity, and lapse assumption analyses. *(supervised by actuary; skill: `roles/experience-study-mortality-agent/`)*
- **ALM & economic-capital modeling agent** — models asset-liability matching, economic capital, and stress and scenario results. *(supervised by actuary / risk lead; skill: `roles/alm-economic-capital-modeling-agent/`)*
- **Macro-risk scenario agent** — nowcasts and scenario-models macro-financial risk — inflation, output, credit, and policy consistency — so monetary and fiscal authorities can act on early signals. *(supervised by chief economist / financial-stability lead; skill: `roles/macro-risk-scenario-agent/`)*
- **External-vulnerability analyst** — monitors reserves, the current account, external debt, and funding concentration and stress-tests exposure to capital-flow and balance-of-payments shocks. *(supervised by financial-stability lead; skill: `roles/external-vulnerability-analyst/`)*

## Work-system completeness (the work around the core work)

The core roles above are necessary but not sufficient. For each material JTBD, check which ancillary services are required:

| Family | Required support question | Reusable catalog |
|---|---|---|
| **Enable** | Do practitioners have the evidence, knowledge, data, tools, access, and skills they need? | `_catalogs/enabling-work/` |
| **Integrate** | Who owns dependencies, handoffs, queues, decision preparation, and stakeholder alignment? | `_catalogs/enabling-work/` |
| **Assure** | What needs independent quality review, challenge, testing, risk, safety, legal, or audit work? | `_catalogs/enabling-work/` |
| **Adapt** | How are alternatives generated and operational experience converted into improvement? | `_catalogs/enabling-work/` |
| **Sustain** | Who maintains administration, capacity, wellbeing, coverage, assets, and institutional memory? | `_catalogs/enabling-work/` |

Do not clone every support role into this sector. Choose **embedded, shared, platform, federated, or temporary** support according to demand, specialization, consequence, and context. Every ancillary service must name the core JTBD and owner it serves, its trigger, deliverable, service level, decision boundary, outcome link, escalation, and retirement rule. See the [Work-System Completeness Map](../../docs/work-system-completeness-map.md).

## Humanoid robot roles

- Branch concierge, secure document handling, back-office logistics, facilities support.

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

## Human accountability boundary (must stay human-led)

Credit denial, fiduciary advice, market conduct, claims disputes, financial-crime escalation, systemic-risk decisions, and the Statement of Actuarial Opinion / appointed-actuary sign-off require human accountability.

Treat this boundary as a hard constraint. Agents in this sector may sense, interpret, draft, model, monitor, and coordinate up to this line, then must hand off to an accountable human for the decision itself.

## Division of labor (human / AI / robot)

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff, and everything inside the accountability boundary above.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document. Strongest on digital signals and repeatable decision support.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces. Strongest on physical work in human-built environments.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor-impact review.

## Interfaces with other operating systems

This sector regularly depends on and feeds: Public Finance, Commerce & Services, Governance & Law, Resilience & Continuity. Coordinate handoffs explicitly; most systemic failures happen at the seams between operating systems.

## Strategic missions that draw on this sector

Beyond its own mandate, this operating system is composed by these cross-cutting [strategic missions](../strategic-missions/) (the orthogonal mission axis — a mission pulls roles from several sectors toward one national objective):

- [Energy Abundance](../strategic-missions/energy-abundance/)
- [Strategic Supply Chain](../strategic-missions/strategic-supply-chain/)
- [Science-to-Industry](../strategic-missions/science-to-industry/)
- [Digital Infrastructure](../strategic-missions/digital-infrastructure/)

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

- **Risk here:** Underwriting and credit judgment and manual modeling erode; traders depend on algorithms.
- **Countermeasures:** Manual underwriting exercises; independent model-risk review; keep judgment in credit and conduct decisions.
- **Role/job simulators (keep-warm):** Underwriting and trading/stress-scenario simulators; manual credit-memo and model builds.

> **Dual-use simulators:** the world models and simulation built to *train the machines* in this sector double as the **keep-warm simulators** that keep humans current and rebuild the learning ladder. Owned cross-sector by OS 22 (Resilience) and the `_catalogs/simulation-training/` roles; the verified deterministic fallback in `_catalogs/capability-optimization/` is its technical complement.

## Adapting to any nation (context modifiers)

The jobs above are universal; how they are staffed is not. Financial systems are reflexive — analysis moves the thing analyzed — and regulatory perimeters are jurisdictional. Most of the world's savers and borrowers are informal or thin-file.

Re-read this sector through:

- **Scale** (city-state → federation): whether this role is unified or layered across local/regional/national tiers.
- **State capacity** (fragile → high-capacity): whether the owning institution exists and can be held to account, or the job is met by markets, households, NGOs, or donors.
- **Income level** (low → high): affordability of automation and the balance of subsistence vs. wage work.
- **Formality** (informal → formal): whether the people and assets this role acts on appear in any registry at all.
- **Resource & geography**: which hazards and dependencies dominate (water-scarce, flood-prone, landlocked, trade-dependent).
- **Political system & legitimacy**: where the human-accountability boundary actually binds and who may hold power to account.

## How to operate in this sector

1. Identify which Core JTBD the task serves.
2. Select the role skill(s) under `roles/` that fit, and confirm the human supervisor.
3. Run the work-system completeness check and add only the Enable, Integrate, Assure, Adapt, and Sustain services the core outcome requires.
4. Run the lifecycle: sense → interpret → decide → mobilize → execute → verify → govern.
5. Stop at the accountability boundary and route the decision to the accountable human.
6. Log actions to the control layer and surface anything that trips a failure mode.

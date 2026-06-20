---
name: "os-12-communications"
description: "Operating-system orchestrator skill for **Communications, Software, Cybersecurity, and Digital Infrastructure** (national operating system #12). Use this skill whenever work touches this sector's mission — Enable trusted computation, communication, data storage, software services, and cyber resilience — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself."
---

# Operating System 12 — Communications, Software, Cybersecurity, and Digital Infrastructure

> **Layer:** National operating system (#12 of 23) · **Personnel model:** human-owned, AI- and robot-augmented
> **Cross-references:** `00-framework/` (shared concepts, teaming pattern, accountability), source map `Country-Economy Core Jobs To Be Done.md`

## Mission

Enable trusted computation, communication, data storage, software services, and cyber resilience.

## When to use this skill

Load this skill when a task concerns communications, software, cybersecurity, and digital infrastructure. It gives an agent the sector map: the outcomes that must be produced, who owns them, what can be automated, and where human accountability is non-negotiable. From here, route to the specific role skills under `roles/` for execution.

## Core Jobs To Be Done

These are the durable outcomes this operating system must reliably produce, written as trigger → response:

1. When people and institutions need to coordinate, provide reliable networks and software.
2. When data must be stored and processed, operate secure compute and cloud infrastructure.
3. When adversaries attack, detect, respond, recover, and harden.
4. When organizations need new capabilities, design, build, test, deploy, and maintain software.
5. When digital systems shape rights and opportunities, govern privacy, fairness, safety, and reliability.

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

- Software engineer, full-stack engineer, mobile engineer, platform engineer.
- Product manager, UX designer, UX researcher, technical program manager.
- Data engineer, data scientist, analytics engineer, business intelligence analyst.
- Network engineer, telecom technician, data center technician, cloud architect.
- Cybersecurity analyst, security engineer, incident responder, threat hunter.
- AI engineer, ML engineer, applied scientist, MLOps engineer, AI product manager.
- AI governance manager, model risk manager, trust and safety analyst, AI safety evaluator.

These remain human-owned. AI personnel and robots augment them; they do not replace the accountable owner.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** SWE I → SWE II/senior → staff/principal → engineering manager → director/VP; data: analyst → data scientist/engineer → senior → lead; security: SOC Tier 1 → Tier 2/3 → security engineer → CISO; AI: ML engineer → senior/applied scientist → AI engineering manager. (Real 2026 postings: 'Senior Engineering Manager, AI' base ~$228K–$373K.)
- **Skills, tools & tech employers list:** Python, SQL, Java/Go/TypeScript; cloud (AWS/Azure/GCP); Kubernetes/Docker; CI/CD, Git, Terraform; PyTorch/TensorFlow/scikit-learn; Spark/Snowflake/BigQuery; SIEM/EDR.
- **Qualifications, certifications & licenses:** Cloud certs (AWS/Azure/GCP), CKA; security ladder Security+ → CySA+ → CISSP/CISM; CCNA/CCNP (network); CEH; CS/related degree common.
- **KPIs / metrics in postings:** Uptime/SLOs, DORA metrics (deploy frequency, lead time, MTTR, change-fail rate), defect/escape rate, incident counts, model-eval metrics, cost.
- **Where these roles are posted:** Dice, LinkedIn, Wellfound (startups), BuiltIn, Indeed, Upwork (freelance), ClearanceJobs (cleared).

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **Coding agent** — builds, tests, refactors, and documents software under review. *(supervised by engineer / tech lead; skill: `roles/coding-agent/`)*
- **Test generation agent** — generates and maintains test suites and coverage. *(supervised by engineer; skill: `roles/test-generation-agent/`)*
- **Code review agent** — reviews diffs for bugs, security, and standards. *(supervised by tech lead; skill: `roles/code-review-agent/`)*
- **Incident response copilot** — assembles incident context and proposes response steps. *(supervised by incident responder; skill: `roles/incident-response-copilot/`)*
- **Threat intelligence agent** — collects and correlates threat intelligence. *(supervised by threat hunter; skill: `roles/threat-intelligence-agent/`)*
- **SOC triage agent** — classifies and enriches security alerts and proposes actions. *(supervised by security analyst; skill: `roles/soc-triage-agent/`)*
- **Data quality agent** — detects anomalies, reconciles records, and maintains pipelines. *(supervised by data steward; skill: `roles/data-quality-agent/`)*
- **Analytics agent** — answers data questions and builds analyses. *(supervised by analytics engineer; skill: `roles/analytics-agent/`)*
- **AI model evaluation agent** — tests AI outputs for quality, safety, bias, and drift. *(supervised by AI governance lead; skill: `roles/ai-model-evaluation-agent/`)*
- **Privacy impact assessment agent** — drafts privacy and data-protection assessments. *(supervised by privacy officer; skill: `roles/privacy-impact-assessment-agent/`)*
- **Documentation agent** — produces and maintains technical documentation. *(supervised by domain owner; skill: `roles/documentation-agent/`)*
- **Algorithmic transparency & audit agent** — documents, tests, and audits automated public-facing decision systems for explainability, fairness, and appealability and prepares the records that make them reviewable. *(supervised by AI governance lead / responsible-AI officer; skill: `roles/algorithmic-transparency-audit-agent/`)*

## Humanoid robot roles

- Data center inspection, hardware-swap assistance, cable handling, warehouse logistics.
- Office IT support runner, physical security patrol support.

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

## Human accountability boundary (must stay human-led)

Security incident command, privacy commitments, AI deployment approval, customer-trust decisions, and architecture tradeoffs stay human-led.

Treat this boundary as a hard constraint. Agents in this sector may sense, interpret, draft, model, monitor, and coordinate up to this line, then must hand off to an accountable human for the decision itself.

## Division of labor (human / AI / robot)

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff, and everything inside the accountability boundary above.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document. Strongest on digital signals and repeatable decision support.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces. Strongest on physical work in human-built environments.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor-impact review.

## Interfaces with other operating systems

This sector regularly depends on and feeds: Governance & Law, Finance & Markets, Energy & Utilities, Science & Innovation. Coordinate handoffs explicitly; most systemic failures happen at the seams between operating systems.

## Strategic missions that draw on this sector

Beyond its own mandate, this operating system is composed by these cross-cutting [strategic missions](../strategic-missions/) (the orthogonal mission axis — a mission pulls roles from several sectors toward one national objective):

- [Semiconductor Sovereignty](../strategic-missions/semiconductor-sovereignty/)
- [Frontier AI Production](../strategic-missions/frontier-ai-production/)
- [Quantum and Space Systems](../strategic-missions/quantum-and-space-systems/)
- [Cyber Defense](../strategic-missions/cyber-defense/)
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

- **Risk here:** Engineers cannot debug without copilots; juniors never learn because entry-level coding is automated.
- **Countermeasures:** Protect junior learning paths; periodic 'no-AI' practice; incident game-days; code-review discipline.
- **Role/job simulators (keep-warm):** Cyber ranges and incident game-days; no-copilot debugging exercises; simulated AI failures (injection, drift) for oversight training.

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

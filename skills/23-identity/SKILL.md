---
name: "os-23-identity"
description: "Operating-system orchestrator skill for **Identity, Civil Registration, and Digital Public Infrastructure** (national operating system #23). Use this skill whenever work touches this sector's mission — Establish legal identity, register vital events, and run the shared digital rails — identity, payments, and consent-based data exchange — that public and private services depend on — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself."
---

# Operating System 23 — Identity, Civil Registration, and Digital Public Infrastructure

> **Layer:** National operating system (#23 of 23) · **Personnel model:** human-owned, AI- and robot-augmented
> **Cross-references:** `00-framework/` (shared concepts, teaming pattern, accountability), source map `Country-Economy Core Jobs To Be Done.md`

## Mission

Establish legal identity, register vital events, and run the shared digital rails — identity, payments, and consent-based data exchange — that public and private services depend on.

## When to use this skill

Load this skill when a task concerns identity, civil registration, and digital public infrastructure. It gives an agent the sector map: the outcomes that must be produced, who owns them, what can be automated, and where human accountability is non-negotiable. From here, route to the specific role skills under `roles/` for execution.

## Core Jobs To Be Done

These are the durable outcomes this operating system must reliably produce, written as trigger → response:

1. When a person is born, exists, or dies, register the vital event so rights, services, and inheritance can operate.
2. When people must prove who they are, issue and verify trusted identity without excluding the marginalized.
3. When services must reach people, provide interoperable rails (ID, payments, consent-based data exchange) so delivery is fast and inclusive.
4. When identity systems hold power over inclusion, govern privacy, consent, security, and redress so they empower rather than exclude or surveil.
5. When populations must be counted, run the census and statistics that planning and representation depend on.

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

- Civil registrar, vital-statistics officer, records officer.
- National ID program manager, enrollment officer, identity architect.
- Digital public infrastructure (DPI) architect, interoperability/standards engineer, payments-rail operator.
- Data protection officer, consent/privacy officer, grievance and redress officer.
- Census director, statistician, demographer, survey operations manager.
- Inclusion/last-mile officer, field enrollment agent.

These remain human-owned. AI personnel and robots augment them; they do not replace the accountable owner.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Enrollment/records officer → civil registrar / ID program officer → identity architect / DPI lead → registrar-general / chief digital officer; statistics track: survey operator → statistician → census director. Public roles carry GS or civil-service grades.
- **Skills, tools & tech employers list:** Civil-registration and national-ID platforms (e.g. MOSIP), biometric SDKs, interoperability layers (X-Road-style), payment rails, consent/data-exchange platforms, GIS, statistical software (R/SAS/SPSS).
- **Qualifications, certifications & licenses:** Public-administration background; data-protection (CIPP/CIPM), security (CISSP) for DPI; demography/statistics degrees; civil-service assessment.
- **KPIs / metrics in postings:** Registration coverage (birth/death), unique-ID coverage, exclusion/error rate, verification latency, rail uptime, grievance-resolution time, census completeness.
- **Where these roles are posted:** USAJOBS/GovernmentJobs (civil registry, census bureau), UN and World Bank ID4D / DPI programs, DPI organizations (e.g. MOSIP), LinkedIn, GovTech boards.

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **Identity verification agent** — verifies identity claims against registries while flagging fraud and exclusion risk. *(supervised by identity program manager; skill: `roles/identity-verification-agent/`)*
- **Civil-registration assistant** — guides and checks birth/death/marriage registration and reconciles records. *(supervised by civil registrar; skill: `roles/civil-registration-assistant/`)*
- **Deduplication & fraud agent** — detects duplicate, ghost, and fraudulent identities. *(supervised by identity assurance lead; skill: `roles/deduplication-fraud-agent/`)*
- **Interoperability schema agent** — maps and validates data schemas across registries and services. *(supervised by DPI architect; skill: `roles/interoperability-schema-agent/`)*
- **Consent & data-exchange agent** — manages consent artifacts and audits data sharing against policy. *(supervised by data protection officer; skill: `roles/consent-data-exchange-agent/`)*
- **Grievance & redress agent** — triages exclusion and error complaints and prepares remediation. *(supervised by redress officer; skill: `roles/grievance-redress-agent/`)*
- **Census & survey operations agent** — plans enumeration, monitors coverage, and flags gaps. *(supervised by census director; skill: `roles/census-survey-operations-agent/`)*
- **Inclusion-gap analyst** — finds populations missing from registries and targets outreach. *(supervised by inclusion officer; skill: `roles/inclusion-gap-analyst/`)*

## Humanoid robot roles

- Mobile enrollment kiosk support, document scanning and digitization, records-room retrieval.
- Field enrollment logistics in remote or underserved areas.

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

## Human accountability boundary (must stay human-led)

Identity issuance and revocation, exclusion and denial decisions, biometric and data-retention policy, surveillance limits, census methodology, and redress remain human-accountable; inclusion of the marginalized is a non-negotiable design constraint.

Treat this boundary as a hard constraint. Agents in this sector may sense, interpret, draft, model, monitor, and coordinate up to this line, then must hand off to an accountable human for the decision itself.

## Division of labor (human / AI / robot)

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff, and everything inside the accountability boundary above.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document. Strongest on digital signals and repeatable decision support.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces. Strongest on physical work in human-built environments.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor-impact review.

## Interfaces with other operating systems

This sector regularly depends on and feeds: Governance & Law, Public Finance, Communications & Software, Finance & Markets. Coordinate handoffs explicitly; most systemic failures happen at the seams between operating systems.

## Strategic missions that draw on this sector

Beyond its own mandate, this operating system is composed by these cross-cutting [strategic missions](../strategic-missions/) (the orthogonal mission axis — a mission pulls roles from several sectors toward one national objective):

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

- **Risk here:** Registrars and frontline staff rely on automated matching and verification and lose the judgment to handle edge cases, exclusion, and fraud; manual-registration and grievance-handling skill fades.
- **Countermeasures:** Maintain manual registration and adjudication competency; rotate staff through field enrollment; preserve redress-handling and exclusion-detection skill.
- **Role/job simulators (keep-warm):** Enrollment and adjudication simulators with synthetic edge cases (no documents, name variants, biometric failures); exclusion-handling and grievance drills.

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

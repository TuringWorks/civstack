---
name: os-13-healthcare
description: Operating-system orchestrator skill for **Healthcare, Public Health, and Biomedical Systems** (national operating system #13). Use this skill whenever work touches this sector's mission — Prevent disease, diagnose and treat illness, rehabilitate people, and support health across populations — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself.
---

# Operating System 13 — Healthcare, Public Health, and Biomedical Systems

> **Layer:** National operating system (1 of 22) · **Personnel model:** human-owned, AI- and robot-augmented
> **Cross-references:** `00-framework/` (shared concepts, teaming pattern, accountability), source map `Country-Economy Core Jobs To Be Done.md`

## Mission

Prevent disease, diagnose and treat illness, rehabilitate people, and support health across populations.

## When to use this skill

Load this skill when a task concerns healthcare, public health, and biomedical systems. It gives an agent the sector map: the outcomes that must be produced, who owns them, what can be automated, and where human accountability is non-negotiable. From here, route to the specific role skills under `roles/` for execution.

## Core Jobs To Be Done

These are the durable outcomes this operating system must reliably produce, written as trigger → response:

1. When people are sick or injured, diagnose, treat, monitor, comfort, and follow up.
2. When disease spreads, surveil, trace, vaccinate, communicate, and coordinate.
3. When medicines and devices are needed, research, test, approve, produce, prescribe, and monitor.
4. When care is fragmented, coordinate records, referrals, coverage, and home support.
5. When resources are scarce, triage ethically and transparently.

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

- Physician, nurse practitioner, physician assistant, nurse, pharmacist.
- Medical assistant, phlebotomist, radiologic technologist, lab technician.
- Therapist, psychologist, social worker, care coordinator.
- Epidemiologist, public health nurse, infection preventionist.
- Hospital administrator, revenue cycle analyst, health informatics specialist.
- Clinical researcher, regulatory affairs specialist, biomedical engineer.
- Home health aide, eldercare worker, rehabilitation aide.

These remain human-owned. AI personnel and robots augment them; they do not replace the accountable owner.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Aide/MA/tech → RN/therapist → charge/lead → nurse manager/director → CNO; physician: resident → attending → chief; public health analyst → epidemiologist → health officer.
- **Skills, tools & tech employers list:** EHR (Epic, Cerner), PACS (imaging), CPOE, telehealth, LIS, scheduling, claims/revenue-cycle, disease-surveillance systems.
- **Qualifications, certifications & licenses:** State RN license (NCLEX-RN) with BLS/ACLS/PALS (AHA); MD/DO + board certification + state license + DEA; PA-C/NP; RPh (pharmacist); ARRT (radiology); MPH/CPH (public health); specialty certs (e.g. CCRN).
- **KPIs / metrics in postings:** Clinical quality/outcomes (HCAHPS, readmissions), patient-safety events, length of stay, throughput, coding accuracy, vaccination/coverage rates.
- **Where these roles are posted:** Indeed, Vivian and Incredible Health (nursing), Health eCareers, LinkedIn, GovernmentJobs (public health), hospital career pages.

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **Clinical documentation agent** — drafts notes and structured records from encounters. *(supervised by physician / nurse; skill: `roles/clinical-documentation-agent/`)*
- **Prior authorization agent** — prepares and submits prior-authorization requests. *(supervised by care coordinator; skill: `roles/prior-authorization-agent/`)*
- **Care gap analyst** — identifies overdue screenings and care gaps in panels. *(supervised by population health lead; skill: `roles/care-gap-analyst/`)*
- **Diagnostic support agent** — surfaces differential diagnoses and relevant evidence. *(supervised by physician; skill: `roles/diagnostic-support-agent/`)*
- **Imaging triage assistant** — prioritizes and pre-reads imaging studies. *(supervised by radiologist; skill: `roles/imaging-triage-assistant/`)*
- **Drug interaction checker** — checks medication safety and interactions. *(supervised by pharmacist; skill: `roles/drug-interaction-checker/`)*
- **Public health surveillance agent** — monitors signals for outbreak detection. *(supervised by epidemiologist; skill: `roles/public-health-surveillance-agent/`)*
- **Outbreak modeler** — models disease spread and intervention scenarios. *(supervised by epidemiologist; skill: `roles/outbreak-modeler/`)*
- **Clinical trial matching agent** — matches patients to eligible trials. *(supervised by clinical researcher; skill: `roles/clinical-trial-matching-agent/`)*

## Humanoid robot roles

- Supply delivery, room turnover, lifting support, medication transport, lab sample movement.
- Elder support: fetch, remind, monitor, help with mobility under care-team oversight.

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

## Non-humanoid autonomous machines

Self-driving vehicles, equipment, and drones for this sector (LLM-planned; physical actions as tool calls; ODD + teleoperation fallback):

- **Medical & lab-sample delivery drone** — fly blood, samples, vaccines, and medicines between sites quickly. *(autonomous machine skill: `autonomous/medical-lab-sample-delivery-drone/`)*
- **Autonomous supply & pharmacy transport vehicle** — move supplies, meds, linens, and lab samples through a hospital. *(autonomous machine skill: `autonomous/autonomous-supply-pharmacy-transport-vehicle/`)*

> **How these machines work (assumed architecture):** each is a **non-humanoid autonomous machine** — a foundation/LLM planning brain issues **actions as tool calls** (`follow_route`, `dump_bucket`, `take_off`, `spray_zone`, …) over a perception → prediction → planning → control stack trained on world models, driving/field simulation, and **RLAIF**. Each runs inside a defined **Operational Design Domain (ODD)** with a verified safe-stop and **teleoperation** fallback. Full detail in `_catalogs/autonomous-machines/` and `00-framework/`.

## Human accountability boundary (must stay human-led)

Diagnosis, prescribing, surgery, consent, triage, end-of-life decisions, and patient-relationship accountability remain human-led.

Treat this boundary as a hard constraint. Agents in this sector may sense, interpret, draft, model, monitor, and coordinate up to this line, then must hand off to an accountable human for the decision itself.

## Division of labor (human / AI / robot)

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff, and everything inside the accountability boundary above.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document. Strongest on digital signals and repeatable decision support.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces. Strongest on physical work in human-built environments.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor-impact review.

## Interfaces with other operating systems

This sector regularly depends on and feeds: Science & Innovation, Household & Care, Public Safety & Justice, Communications & Software. Coordinate handoffs explicitly; most systemic failures happen at the seams between operating systems.

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

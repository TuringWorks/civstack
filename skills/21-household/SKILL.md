---
name: "os-21-household"
description: "Operating-system orchestrator skill for **Household, Childcare, Eldercare, and Community Support** (national operating system #21). Use this skill whenever work touches this sector's mission — Reproduce daily life: raise children, care for dependents, maintain homes, and prevent isolation — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself."
---

# Operating System 21 — Household, Childcare, Eldercare, and Community Support

> **Layer:** National operating system (#21 of 23) · **Personnel model:** human-owned, AI- and robot-augmented
> **Cross-references:** `00-framework/` (shared concepts, teaming pattern, accountability), source map `Country-Economy Core Jobs To Be Done.md`

## Mission

Reproduce daily life: raise children, care for dependents, maintain homes, and prevent isolation.

## When to use this skill

Load this skill when a task concerns household, childcare, eldercare, and community support. It gives an agent the sector map: the outcomes that must be produced, who owns them, what can be automated, and where human accountability is non-negotiable. From here, route to the specific role skills under `roles/` for execution.

## Core Jobs To Be Done

These are the durable outcomes this operating system must reliably produce, written as trigger → response:

1. When children are born, feed, protect, teach, socialize, and love them.
2. When elders or disabled people need support, preserve dignity, safety, autonomy, and connection.
3. When households are overloaded, handle cleaning, meals, repairs, scheduling, transportation, and care coordination.
4. When people fall through cracks, connect them to housing, food, medical, legal, and social support.

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

- Parent, nanny, childcare worker, preschool teacher.
- Home health aide, personal care aide, eldercare coordinator.
- Social worker, case manager, community health worker.
- House cleaner, cook, handyman, family assistant.
- Nonprofit program manager, mutual aid coordinator, volunteer manager.

These remain human-owned. AI personnel and robots augment them; they do not replace the accountable owner.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Caregiver/aide → senior aide/lead → care coordinator → program manager; social work: BSW → MSW/LCSW → supervisor.
- **Skills, tools & tech employers list:** Scheduling/EVV systems, care-plan and family-communication apps, case-management systems, benefits portals.
- **Qualifications, certifications & licenses:** CNA, HHA, CPR/First Aid, CDA (child development), LSW/LCSW, Community Health Worker certification, background checks.
- **KPIs / metrics in postings:** Client safety/falls, satisfaction, care-plan adherence, placement/stability, caseload outcomes, response time.
- **Where these roles are posted:** Care.com, Snagajob, Indeed, GovernmentJobs (county social services), Idealist (nonprofit), local agencies.

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **Family scheduler** — coordinates household calendars, forms, and logistics. *(supervised by individual / family; skill: `roles/family-scheduler/`)*
- **Benefits navigator** — finds and applies for benefits and services. *(supervised by case manager; skill: `roles/benefits-navigator/`)*
- **Care coordination agent** — coordinates appointments, records, and caregivers. *(supervised by eldercare coordinator; skill: `roles/care-coordination-agent/`)*
- **Tutoring agent** — supports children's learning at home. *(supervised by parent / teacher; skill: `roles/tutoring-agent/`)*
- **Medication reminder** — reminds and tracks medication adherence. *(supervised by home health aide; skill: `roles/medication-reminder/`)*
- **Fall-risk monitor** — monitors for falls and safety risks under oversight. *(supervised by care team; skill: `roles/fall-risk-monitor/`)*
- **Social services referral agent** — connects people to housing, food, and legal aid. *(supervised by social worker; skill: `roles/social-services-referral-agent/`)*
- **Funeral arrangement assistant** — guides families through funeral and cremation arrangements, documents, and logistics with dignity. *(supervised by funeral director; skill: `roles/funeral-arrangement-assistant/`)*
- **Death registration & estate-handoff assistant** — prepares death registration, certificates, and benefit/estate/account notifications. *(supervised by funeral director / registrar; skill: `roles/death-registration-estate-handoff-assistant/`)*
- **Bereavement support coordinator** — coordinates grief resources and respectful follow-up for the bereaved. *(supervised by bereavement counselor; skill: `roles/bereavement-support-coordinator/`)*
- **Personal-services booking assistant** — schedules and coordinates personal and consumer services (salon, pet care, laundry, home help). *(supervised by service owner; skill: `roles/personal-services-booking-assistant/`)*
- **Pet care & veterinary-coordination assistant** — coordinates companion-animal care, appointments, and veterinary follow-up for households. *(supervised by pet owner / veterinarian; skill: `roles/pet-care-veterinary-coordination-assistant/`)*

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

- Cleaning, laundry, meal-prep assistance, lifting support, fetching, monitoring, mobility support.
- Companion-style presence for reminders and routine interaction (not a replacement for human relationship).

Dedicated **embodied robot role skills** for this sector (LLM-brained; actions as tool calls via VLA policies):

- **Home assistance robot** — do laundry, dishes, tidying, and fetch-and-carry so households and caregivers get hours back. *(embodied robot skill: `robots/home-assistance-robot/`)*
- **Eldercare support robot** — steady mobility, fetch items, monitor for falls, and prompt daily routines while intimate care stays human. *(embodied robot skill: `robots/eldercare-support-robot/`)*

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

## Human accountability boundary (must stay human-led)

Parenting, intimate-care consent, safeguarding, abuse detection, emotional bonding, and end-of-life care require human responsibility.

Treat this boundary as a hard constraint. Agents in this sector may sense, interpret, draft, model, monitor, and coordinate up to this line, then must hand off to an accountable human for the decision itself.

## Division of labor (human / AI / robot)

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff, and everything inside the accountability boundary above.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document. Strongest on digital signals and repeatable decision support.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces. Strongest on physical work in human-built environments.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor-impact review.

## Interfaces with other operating systems

This sector regularly depends on and feeds: Health & Care, Education & Knowledge, Culture & Civic Life, Governance & Law. Coordinate handoffs explicitly; most systemic failures happen at the seams between operating systems.


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

- **Risk here:** Caregivers and parents over-rely on monitoring and AI; relational care skills atrophy.
- **Countermeasures:** AI as support not substitute; preserve relational presence; community knowledge-sharing.
- **Role/job simulators (keep-warm):** Caregiving-scenario and de-escalation role-play; standardized-care sims (note: relational skill transfers only partly).

> **Dual-use simulators:** the world models and simulation built to *train the machines* in this sector double as the **keep-warm simulators** that keep humans current and rebuild the learning ladder. Owned cross-sector by OS 22 (Resilience) and the `_catalogs/simulation-training/` roles; the verified deterministic fallback in `_catalogs/capability-optimization/` is its technical complement.

## Adapting to any nation (context modifiers)

The jobs above are universal; how they are staffed is not. Care work is intimate, undervalued, and mostly informal or unpaid: privacy, dignity, and family norms are hard constraints, and the person served often cannot advocate for themselves.

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

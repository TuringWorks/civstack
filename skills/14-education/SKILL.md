---
name: "os-14-education"
description: "Operating-system orchestrator skill for **Education, Training, Libraries, and Human Capital** (national operating system #14). Use this skill whenever work touches this sector's mission — Form capable people, transmit knowledge, cultivate judgment, and reskill the workforce — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself."
---

# Operating System 14 — Education, Training, Libraries, and Human Capital

> **Layer:** National operating system (1 of 22) · **Personnel model:** human-owned, AI- and robot-augmented
> **Cross-references:** `00-framework/` (shared concepts, teaming pattern, accountability), source map `Country-Economy Core Jobs To Be Done.md`

## Mission

Form capable people, transmit knowledge, cultivate judgment, and reskill the workforce.

## When to use this skill

Load this skill when a task concerns education, training, libraries, and human capital. It gives an agent the sector map: the outcomes that must be produced, who owns them, what can be automated, and where human accountability is non-negotiable. From here, route to the specific role skills under `roles/` for execution.

## Core Jobs To Be Done

These are the durable outcomes this operating system must reliably produce, written as trigger → response:

1. When children grow, teach literacy, numeracy, science, citizenship, collaboration, and self-regulation.
2. When workers need new capabilities, assess gaps and train efficiently.
3. When knowledge must persist, preserve, classify, retrieve, and teach it.
4. When learners struggle, adapt instruction and provide support.
5. When credentials matter, assess competence fairly.

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

- Teacher, professor, teaching assistant, tutor, instructional coach.
- Curriculum designer, learning experience designer, assessment specialist.
- School counselor, special education teacher, speech-language pathologist.
- Librarian, archivist, museum educator, knowledge manager.
- Corporate trainer, workforce development specialist, apprenticeship coordinator.
- Education administrator, registrar, student success manager.

These remain human-owned. AI personnel and robots augment them; they do not replace the accountable owner.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Aide/TA → teacher → instructional coach/lead → assistant principal → principal → superintendent; higher ed: adjunct → assistant/associate/full professor; L&D specialist → manager → CLO.
- **Skills, tools & tech employers list:** LMS (Canvas, Schoology), SIS (PowerSchool), assessment platforms, library systems (ILS), instructional-design and EdTech tools.
- **Qualifications, certifications & licenses:** State teaching license/credential (Praxis), subject/special-ed/ESL endorsements, MLS (librarian), administrator credential, ATD/CPTD (L&D).
- **KPIs / metrics in postings:** Learning gains/proficiency, graduation/completion, attendance, credential pass rates, learner satisfaction, time-to-competency.
- **Where these roles are posted:** SchoolSpring, GovernmentJobs (districts), HigherEdJobs, Indeed, LinkedIn, Idealist (nonprofit education).

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **Tutor agent** — diagnoses learner gaps and adapts practice and explanation. *(supervised by teacher; skill: `roles/tutor-agent/`)*
- **Lesson planner** — drafts standards-aligned lessons and materials. *(supervised by teacher / curriculum designer; skill: `roles/lesson-planner/`)*
- **Grading assistant** — scores work against rubrics and drafts feedback. *(supervised by teacher; skill: `roles/grading-assistant/`)*
- **Curriculum alignment checker** — checks materials against standards and outcomes. *(supervised by curriculum designer; skill: `roles/curriculum-alignment-checker/`)*
- **Knowledge retrieval agent** — finds, classifies, and retrieves knowledge resources. *(supervised by librarian / knowledge manager; skill: `roles/knowledge-retrieval-agent/`)*
- **Language practice agent** — provides conversational language practice and correction. *(supervised by language teacher; skill: `roles/language-practice-agent/`)*
- **Career pathway advisor** — maps skills to pathways and training options. *(supervised by student success manager; skill: `roles/career-pathway-advisor/`)*
- **Accessibility adaptation agent** — adapts materials for accessibility needs. *(supervised by special education teacher; skill: `roles/accessibility-adaptation-agent/`)*
- **Training simulator** — builds scenario-based practice for skills. *(supervised by corporate trainer; skill: `roles/training-simulator/`)*

## Humanoid robot roles

- Classroom material support, lab assistant, library shelving/retrieval, campus safety escort.
- Vocational training demonstrator for equipment and procedures.

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

## Human accountability boundary (must stay human-led)

Child safety, motivation, moral formation, discipline, credentialing, special-needs judgment, and institutional culture need human owners.

Treat this boundary as a hard constraint. Agents in this sector may sense, interpret, draft, model, monitor, and coordinate up to this line, then must hand off to an accountable human for the decision itself.

## Division of labor (human / AI / robot)

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff, and everything inside the accountability boundary above.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document. Strongest on digital signals and repeatable decision support.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces. Strongest on physical work in human-built environments.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor-impact review.

## Interfaces with other operating systems

This sector regularly depends on and feeds: Labor & Workforce, Science & Innovation, Culture & Civic Life, Household & Care. Coordinate handoffs explicitly; most systemic failures happen at the seams between operating systems.

## Strategic missions that draw on this sector

Beyond its own mandate, this operating system is composed by these cross-cutting [strategic missions](../strategic-missions/) (the orthogonal mission axis — a mission pulls roles from several sectors toward one national objective):

- [Science-to-Industry](../strategic-missions/science-to-industry/)
- [Frontier Talent Formation](../strategic-missions/frontier-talent-formation/)

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

- **Risk here:** Teachers lean on AI tutors and lose pedagogy; students offload thinking and lose it too.
- **Countermeasures:** AI as augmentation not replacement; teacher development; assess the process, not just the output.
- **Role/job simulators (keep-warm):** Teaching-practice and classroom-management simulators; lesson-delivery rehearsals; assessment-design drills.

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

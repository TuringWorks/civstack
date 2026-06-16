---
name: "os-20-labor"
description: "Operating-system orchestrator skill for **Labor, Workforce Systems, and Organizational Life** (national operating system #20). Use this skill whenever work touches this sector's mission — Match people to work, protect workers, build organizations, and maintain productive cultures — to understand the jobs to be done, the human/AI/robot division of labor, the accountable human boundaries, and which specialized role skills to deploy. Trigger this even when the user names a specific task in the domain rather than the sector itself."
---

# Operating System 20 — Labor, Workforce Systems, and Organizational Life

> **Layer:** National operating system (1 of 22) · **Personnel model:** human-owned, AI- and robot-augmented
> **Cross-references:** `00-framework/` (shared concepts, teaming pattern, accountability), source map `Country-Economy Core Jobs To Be Done.md`

## Mission

Match people to work, protect workers, build organizations, and maintain productive cultures.

## When to use this skill

Load this skill when a task concerns labor, workforce systems, and organizational life. It gives an agent the sector map: the outcomes that must be produced, who owns them, what can be automated, and where human accountability is non-negotiable. From here, route to the specific role skills under `roles/` for execution.

## Core Jobs To Be Done

These are the durable outcomes this operating system must reliably produce, written as trigger → response:

1. When work needs doing, define roles, recruit, assess, hire, onboard, train, manage, pay, and retain.
2. When workers are harmed or exploited, enforce labor standards and provide remedy.
3. When technology changes work, redesign jobs and reskill people.
4. When organizations coordinate, set goals, communicate, resolve conflict, and maintain culture.

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

- Recruiter, talent acquisition partner, sourcer, HR business partner.
- Compensation analyst, benefits administrator, payroll specialist.
- Learning and development manager, organizational development consultant.
- Labor relations specialist, employment lawyer, workplace investigator.
- Chief people officer, operations chief, change manager.
- AI workforce transformation lead, automation program manager.

These remain human-owned. AI personnel and robots augment them; they do not replace the accountable owner.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** HR coordinator → HR generalist/recruiter → HR manager/HRBP → director → CHRO; comp, L&D, and employee-relations tracks.
- **Skills, tools & tech employers list:** ATS (Workday, Greenhouse), HRIS, payroll, LMS, people-analytics, compensation-benchmarking and engagement-survey tools.
- **Qualifications, certifications & licenses:** SHRM-CP/SCP, PHR/SPHR (HRCI), CCP (compensation), CEBS (benefits), CPP (payroll), JD (employment law).
- **KPIs / metrics in postings:** Time-to-fill, quality of hire, retention/turnover, engagement (eNPS), pay equity, training completion, compliance.
- **Where these roles are posted:** LinkedIn, Indeed, SHRM, ZipRecruiter, Glassdoor.

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## AI personnel in this operating system (deployable role skills)

Each of the following has a dedicated, extensive skill under `roles/`. Deploy them under the named human supervisor:

- **Job description agent** — drafts and calibrates job descriptions and scorecards. *(supervised by HR business partner; skill: `roles/job-description-agent/`)*
- **Candidate matching assistant** — screens and matches candidates to roles. *(supervised by recruiter; skill: `roles/candidate-matching-assistant/`)*
- **Interview scheduling agent** — coordinates interviews and logistics. *(supervised by recruiting coordinator; skill: `roles/interview-scheduling-agent/`)*
- **Skills inference agent** — infers skills and gaps from work and history. *(supervised by L&D manager; skill: `roles/skills-inference-agent/`)*
- **Training recommender** — recommends learning paths to close gaps. *(supervised by L&D manager; skill: `roles/training-recommender/`)*
- **HR policy assistant** — answers policy questions and drafts policy. *(supervised by HR business partner; skill: `roles/hr-policy-assistant/`)*
- **Workforce planning simulator** — models headcount, skills, and automation scenarios. *(supervised by workforce planning lead; skill: `roles/workforce-planning-simulator/`)*
- **Employee sentiment analyst** — analyzes engagement and sentiment signals. *(supervised by people analytics lead; skill: `roles/employee-sentiment-analyst/`)*

## Humanoid robot roles

- Workplace facilities support, training-simulation companion, physical-task augmentation.

> **How these robots work (assumed architecture):** each is an **LLM-brained embodied agent** — a multimodal LLM brain plans and issues physical **actions as tool calls** (e.g. `grasp`, `navigate_to`, `place`), executed by Vision-Language-Action policies trained on world models, robot gyms, and **RLAIF**. Fleets may share one brain model or mix specialized ones. A verified low-level safety layer can override unsafe actions independently of the brain. Full detail in `00-framework/` and `_catalogs/humanoid-robots/`.

## Human accountability boundary (must stay human-led)

Hiring decisions, firing, discipline, pay equity, union negotiation, harassment investigations, and culture leadership remain human-accountable.

Treat this boundary as a hard constraint. Agents in this sector may sense, interpret, draft, model, monitor, and coordinate up to this line, then must hand off to an accountable human for the decision itself.

## Division of labor (human / AI / robot)

- **Human owner** — accountable for goals, values, exceptions, relationships, signoff, and everything inside the accountability boundary above.
- **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document. Strongest on digital signals and repeatable decision support.
- **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces. Strongest on physical work in human-built environments.
- **Control layer** — permissions, audit logs, escalation thresholds, incident reporting, evaluation.
- **Public trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor-impact review.

## Interfaces with other operating systems

This sector regularly depends on and feeds: Education & Knowledge, Governance & Law, Commerce & Services, Manufacturing. Coordinate handoffs explicitly; most systemic failures happen at the seams between operating systems.

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

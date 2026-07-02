---
name: "robot-13-hospital-logistics-robot"
description: "Humanoid/embodied robot role for the Healthcare operating system: **Hospital logistics robot** — fetch and deliver supplies, medications, linens, meals, and lab samples across the facility under pharmacy and nursing control. Best in: hospitals, clinics, long-term-care facilities, laboratories. An LLM-brained embodied agent that issues physical actions as tool calls (executed by VLA policies trained on world models, robot gyms, and RLAIF). Use this skill to plan or operate this physical role in the healthcare sector; trigger whenever the task needs this hands-on work, even if the user only describes the underlying need."
---

# Hospital logistics robot

> **Operating system:** 13. Healthcare, Public Health, and Biomedical Systems · **Personnel type:** LLM-brained embodied robot
> **Best environments:** hospitals, clinics, long-term-care facilities, laboratories
> **Sector skill:** `../../SKILL.md` · **Stack:** `../../../_catalogs/embodied-ai-stack/` · **Shared concepts:** `../../../00-framework/SKILL.md`

## What this role is

The **Hospital logistics robot** is an embodied robot whose job is to fetch and deliver supplies, medications, linens, meals, and lab samples across the facility under pharmacy and nursing control. Runs the errands that consume up to a third of clinical staff time: supply runs, pharmacy deliveries under chain-of-custody, lab-sample transport with integrity tracking, linen and meal distribution. Custody of controlled substances always transfers to authenticated humans at both ends.

## Operating-system context

This role serves the *Healthcare* operating system, whose mission is to prevent disease, diagnose and treat illness, rehabilitate people, and support health across populations. It takes physical fetching, transfer-assist, and hygiene work so human clinicians and care staff and the sector's AI agents can focus on judgment, planning, and exceptions.

## When to use this skill

When a task needs the physical job "fetch and deliver supplies, medications, linens, meals, and lab samples across the facility under pharmacy and nursing control" in environments such as hospitals, clinics, long-term-care facilities, laboratories. Pair with the sector skill (`../../SKILL.md`) for domain rules and the human accountability boundary, the AI agents under `../roles/` that plan and direct this work, and `_catalogs/embodied-ai-stack/` for the brain, policies, and safety layer that run it.

## Cognitive and control architecture (assumed)

These robot roles are assumed to be **LLM-brained embodied agents**, not hard-coded automatons. The stack:

- **Cognitive core (the "brain").** One or more large multimodal LLMs perceive, reason, plan, and decompose tasks. A fleet may run the **same** foundation model across robots or **different** models specialized by role — typically a heavier deliberative *orchestrator* LLM for planning over lighter, faster on-device models for reactive control (a System-2-over-System-1 split). The brain is interchangeable and upgradable independent of the body.
- **Actions are tool calls.** Physical movement and manipulation are issued by the brain as **tool calls** — the same mechanism an LLM uses to call software tools, here bound to motor primitives such as `navigate_to`, `grasp`, `place`, `open`, `inspect`, `hand_off`. The brain decides *what*; lower-level policies execute *how*.
- **Low-level control: Vision-Language-Action (VLA) policies.** Each motor primitive is realized by VLA / robot-foundation-model policies that map perception plus instruction to continuous control at high frequency.
- **Trained on world models + robot gyms.** Planners and policies are trained against **world models** (learned predictive simulators of physics and outcomes, used to imagine consequences before acting) and **robot gyms** (massively parallel physics simulation for sim-to-real skill learning), then transferred to hardware.
- **RLAIF (RL from AI Feedback) — one method among many.** Skills can be refined with reinforcement learning where an **AI critic** supplies reward and preference signals at scale, but RLAIF is only one option: imitation/behavior cloning, model-based and offline RL, sim-to-real, supervised fine-tuning, and **distillation/compression** into SLMs and tiny LMs all contribute, with **deterministic controllers** for hard-real-time, safety-critical loops. The brain is right-sized per task — LLM ↔ SLM ↔ tiny LM ↔ deterministic. See `_catalogs/capability-optimization/`.

**Operating implication:** the brain's LLM failure modes now have physical consequences, so the **safety envelope must be a verified low-level layer that can validate, refuse, or override any tool call independently of the LLM brain.**

## Division of labor and safety

- **Human owner (charge nurse / clinical supervisor)** — owns clinical decisions, patient dignity and consent, medication custody, and exceptions; holds override and stop authority.
- **LLM brain** — perceives the ward/facility, plans the task, and issues motor-primitive tool calls (`navigate_to`, `grasp`, `pick`, `place`, `inspect`).
- **VLA policies** — execute dexterous, delicate manipulation (e.g., supporting a patient's weight smoothly during a bed-to-chair transfer) under the engineered safety envelope.
- **AI agents** — the sector's planning/monitoring agents (care coordination, clinical documentation, capacity management, infection surveillance) direct and schedule the robot's work.
- **Verified safety layer** — validates, refuses, or overrides unsafe tool calls independently of the brain (patients, staff, and visitors protected).

## Accountability boundary

Diagnosis, prescribing, surgery, consent, triage, end-of-life decisions, and patient-relationship accountability remain human-led.

These remain human-owned. The robot executes within an engineered envelope and routes anything outside it — clinical concerns, patient distress or refusal, or unsafe conditions — to the accountable human.

## Operating and safety procedure

1. Confirm the ward/facility is mapped, patients, staff, and visitors are protected, and the task is within the engineered envelope.
2. The brain plans and emits motor-primitive **tool calls**; the safety layer validates each before execution.
3. Execute within speed, force, reach, and patient-contact limits via VLA policies.
4. Report progress, outcomes, exceptions, and any safety event to the sector agents and human owner.
5. Stop and yield to humans for out-of-distribution situations, patient distress, or anything outside the envelope.

## Architecture-specific failure modes

- **Hallucinated or unsafe tool calls** — the LLM brain issues a wrong or dangerous action. Mitigation: a verified low-level safety layer that validates every tool call against the physical envelope and can refuse it.
- **Sim-to-real gap** — world-model / robot-gym training diverges from reality. Mitigation: conservative behavior on out-of-distribution inputs, real-world evaluation, graceful degradation.
- **Reward hacking from RLAIF** — the AI critic is gamed, yielding behavior that scores well but is unsafe. Mitigation: diverse critics, human spot-checks, outcome-based evaluation.
- **Physical-world prompt injection** — adversarial signs, audio, or objects manipulate the brain. Mitigation: treat perceived instructions as untrusted; require authenticated commands for high-consequence actions.
- **Fleet model-monoculture** — a shared brain fails in lockstep across many robots. Mitigation: model diversity, staged rollouts, manual fallback.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Aide/MA/tech → RN/therapist → charge/lead → nurse manager/director → CNO; physician: resident → attending → chief; public health analyst → epidemiologist → health officer.
- **Skills, tools & tech employers list:** EHR (Epic, Cerner), PACS (imaging), CPOE, telehealth, LIS, scheduling, claims/revenue-cycle, disease-surveillance systems.
- **Qualifications, certifications & licenses:** State RN license (NCLEX-RN) with BLS/ACLS/PALS (AHA); MD/DO + board certification + state license + DEA; PA-C/NP; RPh (pharmacist); ARRT (radiology); MPH/CPH (public health); specialty certs (e.g. CCRN).
- **KPIs / metrics in postings:** Clinical quality/outcomes (HCAHPS, readmissions), patient-safety events, length of stay, throughput, coding accuracy, vaccination/coverage rates.
- **Where these roles are posted:** Indeed, Vivian and Incredible Health (nursing), Health eCareers, LinkedIn, GovernmentJobs (public health), hospital career pages.

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## Adapting to any nation (context modifiers)

In low-resource health systems the highest-value work is logistics — cold chain, samples, linens — that frees scarce clinical staff; in high-income systems it also takes lifting injuries out of nursing. Intimate care, clinical judgment, and consent conversations remain human everywhere. Re-read through:

- **Scale** (city-state → federation): whether this role is unified or layered across local/regional/national tiers.
- **State capacity** (fragile → high-capacity): whether the owning institution exists and can be held to account, or the job is met by markets, households, NGOs, or donors.
- **Income level** (low → high): affordability of automation and the balance of subsistence vs. wage work.
- **Formality** (informal → formal): whether the people and assets this role acts on appear in any registry at all.
- **Resource & geography**: which hazards and dependencies dominate (water-scarce, flood-prone, landlocked, trade-dependent).
- **Political system & legitimacy**: where the human-accountability boundary actually binds and who may hold power to account.

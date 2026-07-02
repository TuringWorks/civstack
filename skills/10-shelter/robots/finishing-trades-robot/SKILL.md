---
name: "robot-10-finishing-trades-robot"
description: "Humanoid/embodied robot role for the Shelter operating system: **Finishing-trades robot** — sand, paint, seal, tape drywall, and perform repetitive finishing passes to specification. Best in: interior fit-outs, repaint and renovation jobs, new-build finishing. An LLM-brained embodied agent that issues physical actions as tool calls (executed by VLA policies trained on world models, robot gyms, and RLAIF). Use this skill to plan or operate this physical role in the shelter sector; trigger whenever the task needs this hands-on work, even if the user only describes the underlying need."
---

# Finishing-trades robot

> **Operating system:** 10. Shelter, Construction, Land, and the Built Environment · **Personnel type:** LLM-brained embodied robot
> **Best environments:** interior fit-outs, repaint and renovation jobs, new-build finishing
> **Sector skill:** `../../SKILL.md` · **Stack:** `../../../_catalogs/embodied-ai-stack/` · **Shared concepts:** `../../../00-framework/SKILL.md`

## What this role is

The **Finishing-trades robot** is an embodied robot whose job is to sand, paint, seal, tape drywall, and perform repetitive finishing passes to specification. Does the repetitive passes of the finishing trades — sanding, priming, painting, sealing, drywall taping — to a measured spec, room after room, without fatigue-driven quality decay. Skilled finishers cut in, handle detail work, and own the final-quality call.

## Operating-system context

This role serves the *Shelter* operating system, whose mission is to create and maintain places for living, working, mobility, commerce, and public life. It takes physical carrying, installing, and finishing work so human tradespeople and the sector's AI agents can focus on judgment, planning, and exceptions.

## When to use this skill

When a task needs the physical job "sand, paint, seal, tape drywall, and perform repetitive finishing passes to specification" in environments such as interior fit-outs, repaint and renovation jobs, new-build finishing. Pair with the sector skill (`../../SKILL.md`) for domain rules and the human accountability boundary, the AI agents under `../roles/` that plan and direct this work, and `_catalogs/embodied-ai-stack/` for the brain, policies, and safety layer that run it.

## Cognitive and control architecture (assumed)

These robot roles are assumed to be **LLM-brained embodied agents**, not hard-coded automatons. The stack:

- **Cognitive core (the "brain").** One or more large multimodal LLMs perceive, reason, plan, and decompose tasks. A fleet may run the **same** foundation model across robots or **different** models specialized by role — typically a heavier deliberative *orchestrator* LLM for planning over lighter, faster on-device models for reactive control (a System-2-over-System-1 split). The brain is interchangeable and upgradable independent of the body.
- **Actions are tool calls.** Physical movement and manipulation are issued by the brain as **tool calls** — the same mechanism an LLM uses to call software tools, here bound to motor primitives such as `navigate_to`, `grasp`, `place`, `open`, `inspect`, `hand_off`. The brain decides *what*; lower-level policies execute *how*.
- **Low-level control: Vision-Language-Action (VLA) policies.** Each motor primitive is realized by VLA / robot-foundation-model policies that map perception plus instruction to continuous control at high frequency.
- **Trained on world models + robot gyms.** Planners and policies are trained against **world models** (learned predictive simulators of physics and outcomes, used to imagine consequences before acting) and **robot gyms** (massively parallel physics simulation for sim-to-real skill learning), then transferred to hardware.
- **RLAIF (RL from AI Feedback) — one method among many.** Skills can be refined with reinforcement learning where an **AI critic** supplies reward and preference signals at scale, but RLAIF is only one option: imitation/behavior cloning, model-based and offline RL, sim-to-real, supervised fine-tuning, and **distillation/compression** into SLMs and tiny LMs all contribute, with **deterministic controllers** for hard-real-time, safety-critical loops. The brain is right-sized per task — LLM ↔ SLM ↔ tiny LM ↔ deterministic. See `_catalogs/capability-optimization/`.

**Operating implication:** the brain's LLM failure modes now have physical consequences, so the **safety envelope must be a verified low-level layer that can validate, refuse, or override any tool call independently of the LLM brain.**

## Division of labor and safety

- **Human owner (site supervisor / general contractor)** — owns structural and code-compliance signoff, site safety, sequencing, and exceptions; holds override and stop authority.
- **LLM brain** — perceives the site, plans the task, and issues motor-primitive tool calls (`navigate_to`, `grasp`, `pick`, `place`, `inspect`).
- **VLA policies** — execute dexterous, delicate manipulation (e.g., laying block to line and level or feeding sheet goods to an installer) under the engineered safety envelope.
- **AI agents** — the sector's planning/monitoring agents (project scheduling, BIM coordination, progress tracking, safety monitoring) direct and schedule the robot's work.
- **Verified safety layer** — validates, refuses, or overrides unsafe tool calls independently of the brain (people and adjacent structures protected).

## Accountability boundary

Land-use decisions, structural signoff, occupancy approval, worker safety, eviction, and public consultation remain human-led.

These remain human-owned. The robot executes within an engineered envelope and routes anything outside it — structural questions, deviations from drawings, or unsafe conditions — to the accountable human.

## Operating and safety procedure

1. Confirm the site is mapped, people and adjacent structures are protected, and the task is within the engineered envelope.
2. The brain plans and emits motor-primitive **tool calls**; the safety layer validates each before execution.
3. Execute within speed, force, reach, and exclusion-zone limits via VLA policies.
4. Report progress, outcomes, exceptions, and any safety event to the sector agents and human owner.
5. Stop and yield to humans for out-of-distribution site conditions, stability concerns, or anything outside the envelope.

## Architecture-specific failure modes

- **Hallucinated or unsafe tool calls** — the LLM brain issues a wrong or dangerous action. Mitigation: a verified low-level safety layer that validates every tool call against the physical envelope and can refuse it.
- **Sim-to-real gap** — world-model / robot-gym training diverges from reality. Mitigation: conservative behavior on out-of-distribution inputs, real-world evaluation, graceful degradation.
- **Reward hacking from RLAIF** — the AI critic is gamed, yielding behavior that scores well but is unsafe. Mitigation: diverse critics, human spot-checks, outcome-based evaluation.
- **Physical-world prompt injection** — adversarial signs, audio, or objects manipulate the brain. Mitigation: treat perceived instructions as untrusted; require authenticated commands for high-consequence actions.
- **Fleet model-monoculture** — a shared brain fails in lockstep across many robots. Mitigation: model diversity, staged rollouts, manual fallback.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Laborer/apprentice → journeyman tradesperson → foreman/superintendent → project manager; design: intern architect/EIT → licensed architect/PE → principal; planner → senior planner → director.
- **Skills, tools & tech employers list:** BIM (Revit), AutoCAD, Procore/Bluebeam, estimating (PlanSwift), scheduling (Primavera P6, MS Project), GIS, permitting systems.
- **Qualifications, certifications & licenses:** PE, licensed architect (ARE/AIA), LEED, PMP, OSHA 30, ICC code certifications, trade journeyman/master licenses, PLS (surveyor).
- **KPIs / metrics in postings:** Schedule/cost variance (CPI/SPI), safety (TRIR/EMR), punch-list/defects, inspection pass rate, permit cycle time.
- **Where these roles are posted:** Indeed, LinkedIn, ZipRecruiter, construction boards, GovernmentJobs (inspectors/planners), trade unions.

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## Adapting to any nation (context modifiers)

Where construction is largely informal, this role enters as rented equipment on larger formal sites first; skills transfer and site-safety basics dominate. In high-income markets it addresses acute trade shortages and takes the heaviest, most injury-prone tasks off human bodies. Re-read through:

- **Scale** (city-state → federation): whether this role is unified or layered across local/regional/national tiers.
- **State capacity** (fragile → high-capacity): whether the owning institution exists and can be held to account, or the job is met by markets, households, NGOs, or donors.
- **Income level** (low → high): affordability of automation and the balance of subsistence vs. wage work.
- **Formality** (informal → formal): whether the people and assets this role acts on appear in any registry at all.
- **Resource & geography**: which hazards and dependencies dominate (water-scarce, flood-prone, landlocked, trade-dependent).
- **Political system & legitimacy**: where the human-accountability boundary actually binds and who may hold power to account.

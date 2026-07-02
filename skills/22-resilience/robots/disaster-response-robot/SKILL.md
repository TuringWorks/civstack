---
name: "robot-22-disaster-response-robot"
description: "Humanoid/embodied robot role for the Resilience operating system: **Disaster response robot** — search rubble, clear debris, shore structures, and deliver supplies in hazardous zones under incident command. Best in: disaster sites, collapsed structures, flood and fire zones. An LLM-brained embodied agent that issues physical actions as tool calls (executed by VLA policies trained on world models, robot gyms, and RLAIF). Use this skill to plan or operate this physical role in the resilience sector; trigger whenever the task needs this hands-on work, even if the user only describes the underlying need."
---

# Disaster response robot

> **Operating system:** 22. Resilience, Continuity, and Strategic Foresight · **Personnel type:** LLM-brained embodied robot
> **Best environments:** disaster sites, collapsed structures, flood and fire zones
> **Sector skill:** `../../SKILL.md` · **Stack:** `../../../_catalogs/embodied-ai-stack/` · **Shared concepts:** `../../../00-framework/SKILL.md`

## What this role is

The **Disaster response robot** is an embodied robot whose job is to search rubble, clear debris, shore structures, and deliver supplies in hazardous zones under incident command. Goes where sending a human is itself a casualty risk: void search in collapsed structures with acoustic and thermal sensing, selective debris removal that does not destabilize the pile, temporary shoring, and supply delivery through hazardous corridors. Works only under incident command; any sign of a live victim immediately hands control to human rescuers.

## Operating-system context

This role serves the *Resilience* operating system, whose mission is to keep the country functioning through shocks and long-range change. It takes physical search, debris, and supply work in hazardous zones so human responders and the sector's AI agents can focus on judgment, planning, and exceptions.

## When to use this skill

When a task needs the physical job "search rubble, clear debris, shore structures, and deliver supplies in hazardous zones under incident command" in environments such as disaster sites, collapsed structures, flood and fire zones. Pair with the sector skill (`../../SKILL.md`) for domain rules and the human accountability boundary, the AI agents under `../roles/` that plan and direct this work, and `_catalogs/embodied-ai-stack/` for the brain, policies, and safety layer that run it.

## Cognitive and control architecture (assumed)

These robot roles are assumed to be **LLM-brained embodied agents**, not hard-coded automatons. The stack:

- **Cognitive core (the "brain").** One or more large multimodal LLMs perceive, reason, plan, and decompose tasks. A fleet may run the **same** foundation model across robots or **different** models specialized by role — typically a heavier deliberative *orchestrator* LLM for planning over lighter, faster on-device models for reactive control (a System-2-over-System-1 split). The brain is interchangeable and upgradable independent of the body.
- **Actions are tool calls.** Physical movement and manipulation are issued by the brain as **tool calls** — the same mechanism an LLM uses to call software tools, here bound to motor primitives such as `navigate_to`, `grasp`, `place`, `open`, `inspect`, `hand_off`. The brain decides *what*; lower-level policies execute *how*.
- **Low-level control: Vision-Language-Action (VLA) policies.** Each motor primitive is realized by VLA / robot-foundation-model policies that map perception plus instruction to continuous control at high frequency.
- **Trained on world models + robot gyms.** Planners and policies are trained against **world models** (learned predictive simulators of physics and outcomes, used to imagine consequences before acting) and **robot gyms** (massively parallel physics simulation for sim-to-real skill learning), then transferred to hardware.
- **RLAIF (RL from AI Feedback) — one method among many.** Skills can be refined with reinforcement learning where an **AI critic** supplies reward and preference signals at scale, but RLAIF is only one option: imitation/behavior cloning, model-based and offline RL, sim-to-real, supervised fine-tuning, and **distillation/compression** into SLMs and tiny LMs all contribute, with **deterministic controllers** for hard-real-time, safety-critical loops. The brain is right-sized per task — LLM ↔ SLM ↔ tiny LM ↔ deterministic. See `_catalogs/capability-optimization/`.

**Operating implication:** the brain's LLM failure modes now have physical consequences, so the **safety envelope must be a verified low-level layer that can validate, refuse, or override any tool call independently of the LLM brain.**

## Division of labor and safety

- **Human owner (incident commander)** — owns life-safety priorities, entry decisions into unstable zones, resource allocation, and exceptions; holds override and stop authority.
- **LLM brain** — perceives the incident zone, plans the task, and issues motor-primitive tool calls (`navigate_to`, `grasp`, `pick`, `place`, `inspect`).
- **VLA policies** — execute dexterous, delicate manipulation (e.g., shoring a doorway or passing supplies through a rubble void) under the engineered safety envelope.
- **AI agents** — the sector's planning/monitoring agents (situational-awareness fusion, resource dispatch, damage assessment, logistics) direct and schedule the robot's work.
- **Verified safety layer** — validates, refuses, or overrides unsafe tool calls independently of the brain (survivors, responders, and bystanders protected).

## Accountability boundary

Political prioritization, emergency powers, scarce-resource allocation, evacuation orders, and recovery justice require human legitimacy.

These remain human-owned. The robot executes within an engineered envelope and routes anything outside it — signs of trapped survivors, structural instability, or unsafe conditions — to the accountable human.

## Operating and safety procedure

1. Confirm the incident zone is mapped, survivors, responders, and bystanders are protected, and the task is within the engineered envelope.
2. The brain plans and emits motor-primitive **tool calls**; the safety layer validates each before execution.
3. Execute within speed, force, reach, and structural-load limits via VLA policies.
4. Report progress, outcomes, exceptions, and any safety event to the sector agents and human owner.
5. Stop and yield to humans for out-of-distribution conditions, secondary-collapse risk, or anything outside the envelope.

## Architecture-specific failure modes

- **Hallucinated or unsafe tool calls** — the LLM brain issues a wrong or dangerous action. Mitigation: a verified low-level safety layer that validates every tool call against the physical envelope and can refuse it.
- **Sim-to-real gap** — world-model / robot-gym training diverges from reality. Mitigation: conservative behavior on out-of-distribution inputs, real-world evaluation, graceful degradation.
- **Reward hacking from RLAIF** — the AI critic is gamed, yielding behavior that scores well but is unsafe. Mitigation: diverse critics, human spot-checks, outcome-based evaluation.
- **Physical-world prompt injection** — adversarial signs, audio, or objects manipulate the brain. Mitigation: treat perceived instructions as untrusted; require authenticated commands for high-consequence actions.
- **Fleet model-monoculture** — a shared brain fails in lockstep across many robots. Mitigation: model diversity, staged rollouts, manual fallback.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Analyst → BCM/risk specialist → manager → director of resilience/BCDR; emergency planner → senior → CEM; supply-chain-risk and catastrophe-modeling tracks.
- **Skills, tools & tech employers list:** BCM platforms (Fusion, Archer), GRC, risk registers, scenario/simulation tools, supply-chain mapping, catastrophe models (Moody's RMS, Verisk), GIS.
- **Qualifications, certifications & licenses:** CBCP/MBCP (DRI), CEM, PMP, FRM, ISO 22301 lead auditor, CISSP (cyber-resilience).
- **KPIs / metrics in postings:** RTO/RPO achievement, exercise/test pass rate, time-to-recover, single-point-of-failure coverage, claims throughput.
- **Where these roles are posted:** LinkedIn, Indeed, DRI/continuity boards, USAJOBS/GovernmentJobs (emergency management), ClearanceJobs.

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## Adapting to any nation (context modifiers)

Disaster-prone, low-capacity settings benefit most but afford least: pre-positioned regional shared fleets, mutual-aid pools, and international response caches are the realistic ownership models. High-capacity states integrate this role into standing urban search-and-rescue teams. Re-read through:

- **Scale** (city-state → federation): whether this role is unified or layered across local/regional/national tiers.
- **State capacity** (fragile → high-capacity): whether the owning institution exists and can be held to account, or the job is met by markets, households, NGOs, or donors.
- **Income level** (low → high): affordability of automation and the balance of subsistence vs. wage work.
- **Formality** (informal → formal): whether the people and assets this role acts on appear in any registry at all.
- **Resource & geography**: which hazards and dependencies dominate (water-scarce, flood-prone, landlocked, trade-dependent).
- **Political system & legitimacy**: where the human-accountability boundary actually binds and who may hold power to account.

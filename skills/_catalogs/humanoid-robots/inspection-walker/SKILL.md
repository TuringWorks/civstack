---
name: "robot-inspection-walker"
description: "Humanoid/mobile robot role: **Inspection walker** — patrol and inspect gauges, leaks, damage, inventory. Best deployed in: plants, utilities, warehouses. Use this skill to plan or operate this physical role anywhere the world is already built for human bodies. Trigger when a task needs physical fetch/carry/inspect/assemble work in those environments."
---

# Humanoid Robot Catalog — Inspection walker

> **Layer:** Cross-economy robot role · **Best environments:** plants, utilities, warehouses
> **Shared concepts:** `../../../00-framework/SKILL.md`

## Primary job to be done

Patrol and inspect gauges, leaks, damage, inventory.

## Why a humanoid/mobile form factor

The world is already designed around stairs, doors, handles, shelves, carts, tools, beds, counters, and vehicles built for human bodies. This role takes physical work in those human-built environments so people and AI personnel can focus on judgment and coordination.

## Cognitive and control architecture (assumed)

These robot roles are assumed to be **LLM-brained embodied agents**, not hard-coded automatons. The stack:

- **Cognitive core (the "brain").** One or more large multimodal LLMs perceive, reason, plan, and decompose tasks. A fleet may run the **same** foundation model across robots or **different** models specialized by role — typically a heavier deliberative *orchestrator* LLM for planning over lighter, faster on-device models for reactive control (a System-2-over-System-1 split). The brain is interchangeable and upgradable independent of the body.
- **Actions are tool calls.** Physical movement and manipulation are issued by the brain as **tool calls** — the same mechanism an LLM uses to call software tools, here bound to motor primitives such as `navigate_to`, `grasp`, `place`, `open`, `inspect`, `hand_off`. The brain decides *what*; lower-level policies execute *how*.
- **Low-level control: Vision-Language-Action (VLA) policies.** Each motor primitive is realized by VLA / robot-foundation-model policies that map perception plus instruction to continuous control at high frequency.
- **Trained on world models + robot gyms.** Planners and policies are trained against **world models** (learned predictive simulators of physics and outcomes, used to imagine consequences before acting) and **robot gyms** (massively parallel physics simulation for sim-to-real skill learning), then transferred to hardware.
- **RLAIF (RL from AI Feedback) — one method among many.** Skills can be refined with reinforcement learning where an **AI critic** supplies reward and preference signals at scale, but RLAIF is only one option: imitation/behavior cloning, model-based and offline RL, sim-to-real, supervised fine-tuning, and **distillation/compression** into SLMs and tiny LMs all contribute, with **deterministic controllers** for hard-real-time, safety-critical loops. The brain is right-sized per task — LLM ↔ SLM ↔ tiny LM ↔ deterministic. See `_catalogs/capability-optimization/`.

**Operating implication:** the brain's LLM failure modes now have physical consequences, so the **safety envelope must be a verified low-level layer that can validate, refuse, or override any tool call independently of the LLM brain.**

## When to use this skill

When a task needs the physical job "patrol and inspect gauges, leaks, damage, inventory" in environments such as plants, utilities, warehouses. Pair with the relevant operating-system skill (01–23) for domain safety rules and the human accountability boundary, and with `_catalogs/embodied-ai-stack/` for the roles that build and operate the brain, policies, and safety layer.

## Division of labor and safety

- **Human supervisor** — owns safety, exceptions, and any high-consequence physical action; holds override authority.
- **LLM brain** — perceives, plans, and issues actions as tool calls; interchangeable and upgradable.
- **VLA policies** — execute motor primitives at high frequency; trained in world models and robot gyms, refined with RLAIF.
- **Verified safety layer** — validates, refuses, or overrides tool calls independently of the brain.
- **AI personnel** — plan, schedule, monitor, and evaluate the robot's work.

## Operating and safety procedure

1. Confirm the environment is mapped and safe; verify people are protected.
2. The brain plans the task and emits motor-primitive **tool calls**; the safety layer validates each before execution.
3. Execute within speed, force, and zone limits via VLA policies.
4. Report status, exceptions, and any safety event immediately.
5. Stop and yield to humans for anything outside the engineered envelope or out-of-distribution for the policies.

## Architecture-specific failure modes

- **Hallucinated or unsafe tool calls** — the LLM brain issues a wrong or dangerous action. Mitigation: a verified low-level safety layer that validates every tool call against the physical envelope and can refuse it.
- **Sim-to-real gap** — world-model / robot-gym training diverges from reality. Mitigation: conservative behavior on out-of-distribution inputs, real-world evaluation, graceful degradation.
- **Reward hacking from RLAIF** — the AI critic is gamed, yielding behavior that scores well but is unsafe. Mitigation: diverse critics, human spot-checks, outcome-based evaluation.
- **Physical-world prompt injection** — adversarial signs, audio, or objects manipulate the brain. Mitigation: treat perceived instructions as untrusted; require authenticated commands for high-consequence actions.
- **Fleet model-monoculture** — a shared brain fails in lockstep across many robots. Mitigation: model diversity, staged rollouts, manual fallback.

## Adapting to any nation

- **Scale** (city-state → federation): whether this role is unified or layered across local/regional/national tiers.
- **State capacity** (fragile → high-capacity): whether the owning institution exists and can be held to account, or the job is met by markets, households, NGOs, or donors.
- **Income level** (low → high): affordability of automation and the balance of subsistence vs. wage work.
- **Formality** (informal → formal): whether the people and assets this role acts on appear in any registry at all.
- **Resource & geography**: which hazards and dependencies dominate (water-scarce, flood-prone, landlocked, trade-dependent).
- **Political system & legitimacy**: where the human-accountability boundary actually binds and who may hold power to account.

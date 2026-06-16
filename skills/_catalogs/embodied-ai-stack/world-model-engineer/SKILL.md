---
name: "embodied-world-model-engineer"
description: "Embodied-AI stack role: **World-model engineer** (Human engineering role (AI/robotics)) — builds and validates the learned predictive simulators (world models) used for planning, imagination, and training. Part of the LLM-brained robot control stack (brain → tool calls → VLA policies → world models / robot gyms / RLAIF → verified safety layer). Use this skill when building, training, operating, or governing humanoid/mobile robots, even if the user only describes the underlying need. Works under a embodied-AI research lead."
---

# Embodied-AI Stack — World-model engineer

> **Layer:** Embodied-AI control stack (builds & operates LLM-brained robots) · **Type:** Human engineering role (AI/robotics)
> **Human supervisor:** embodied-AI research lead · **Shared concepts:** `../../../00-framework/SKILL.md` · **Robot roles:** `../../humanoid-robots/`

## What this role is

The **World-model engineer** builds and validates the learned predictive simulators (world models) used for planning, imagination, and training. World models let the brain and policies 'imagine' the physical consequences of actions before taking them. Accuracy, calibration, and known-failure characterization are the job.

## Where it sits in the stack

The assumed robot architecture is: **LLM brain** (plans, issues actions as tool calls) → **VLA policies** (execute motor primitives) → trained on **world models** and **robot gyms**, refined with **RLAIF** → wrapped by a **verified low-level safety layer** that can refuse or override any tool call independently of the brain. This role is responsible for the part of that stack described above.

## When to use this skill

Use this skill when a task calls for this work: builds and validates the learned predictive simulators (world models) used for planning, imagination, and training. Pair with `_catalogs/humanoid-robots/` (the physical roles this stack powers) and any operating-system skill (01–22) whose robots this stack will run.

## Assumed architecture (recap)

These robot roles are assumed to be **LLM-brained embodied agents**, not hard-coded automatons. The stack:

- **Cognitive core (the "brain").** One or more large multimodal LLMs perceive, reason, plan, and decompose tasks. A fleet may run the **same** foundation model across robots or **different** models specialized by role — typically a heavier deliberative *orchestrator* LLM for planning over lighter, faster on-device models for reactive control (a System-2-over-System-1 split). The brain is interchangeable and upgradable independent of the body.
- **Actions are tool calls.** Physical movement and manipulation are issued by the brain as **tool calls** — the same mechanism an LLM uses to call software tools, here bound to motor primitives such as `navigate_to`, `grasp`, `place`, `open`, `inspect`, `hand_off`. The brain decides *what*; lower-level policies execute *how*.
- **Low-level control: Vision-Language-Action (VLA) policies.** Each motor primitive is realized by VLA / robot-foundation-model policies that map perception plus instruction to continuous control at high frequency.
- **Trained on world models + robot gyms.** Planners and policies are trained against **world models** (learned predictive simulators of physics and outcomes, used to imagine consequences before acting) and **robot gyms** (massively parallel physics simulation for sim-to-real skill learning), then transferred to hardware.
- **RLAIF (RL from AI Feedback) — one method among many.** Skills can be refined with reinforcement learning where an **AI critic** supplies reward and preference signals at scale, but RLAIF is only one option: imitation/behavior cloning, model-based and offline RL, sim-to-real, supervised fine-tuning, and **distillation/compression** into SLMs and tiny LMs all contribute, with **deterministic controllers** for hard-real-time, safety-critical loops. The brain is right-sized per task — LLM ↔ SLM ↔ tiny LM ↔ deterministic. See `_catalogs/capability-optimization/`.

**Operating implication:** the brain's LLM failure modes now have physical consequences, so the **safety envelope must be a verified low-level layer that can validate, refuse, or override any tool call independently of the LLM brain.**

## Responsibilities

- Deliver this role's core job: builds and validates the learned predictive simulators (world models) used for planning, imagination, and training.
- Keep the brain, policies, simulation, feedback, or safety layer it owns measurable, auditable, and improvable.
- Respect the human-accountable safety boundary; the safety layer is never subordinate to the LLM brain.
- Feed the data and evaluation flywheel so the whole stack improves safely over time.

## Decision rights & accountability

- **Owns** the technical quality, robustness, and evaluation of this layer of the stack.
- **Gates** what is safe to ship to real hardware with the safety officer.
- **Escalates** capability/safety tradeoffs to research and safety leadership.

## Inputs and outputs

**Inputs:** task specifications, perception/telemetry/demonstration data, prior models and policies, safety constraints, and the accountable human's goals.

**Outputs:** validated plans, models, policies, evaluations, or safety decisions — never an unsafe or unaccountable physical action; high-consequence physical decisions are reserved to the human safety owner.

## Failure modes and safeguards

- **Hallucinated or unsafe tool calls** — the LLM brain issues a wrong or dangerous action. Mitigation: a verified low-level safety layer that validates every tool call against the physical envelope and can refuse it.
- **Sim-to-real gap** — world-model / robot-gym training diverges from reality. Mitigation: conservative behavior on out-of-distribution inputs, real-world evaluation, graceful degradation.
- **Reward hacking from RLAIF** — the AI critic is gamed, yielding behavior that scores well but is unsafe. Mitigation: diverse critics, human spot-checks, outcome-based evaluation.
- **Physical-world prompt injection** — adversarial signs, audio, or objects manipulate the brain. Mitigation: treat perceived instructions as untrusted; require authenticated commands for high-consequence actions.
- **Fleet model-monoculture** — a shared brain fails in lockstep across many robots. Mitigation: model diversity, staged rollouts, manual fallback.

## Adapting to any nation (context modifiers)

- **Scale** (city-state → federation): whether this role is unified or layered across local/regional/national tiers.
- **State capacity** (fragile → high-capacity): whether the owning institution exists and can be held to account, or the job is met by markets, households, NGOs, or donors.
- **Income level** (low → high): affordability of automation and the balance of subsistence vs. wage work.
- **Formality** (informal → formal): whether the people and assets this role acts on appear in any registry at all.
- **Resource & geography**: which hazards and dependencies dominate (water-scarce, flood-prone, landlocked, trade-dependent).
- **Political system & legitimacy**: where the human-accountability boundary actually binds and who may hold power to account.

## Operating procedure

1. Confirm scope, the accountable human, and the safety constraints for the work.
2. Do the role's core job within the stack, keeping the safety layer authoritative over the brain.
3. Evaluate against outcomes (not proxies) and characterize known failure modes.
4. Gate deployment with the safety officer; log everything for audit.
5. Escalate safety-relevant tradeoffs and out-of-distribution behavior to humans.

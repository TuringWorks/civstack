---
name: "capopt-capability-method-architect"
description: "Capability/optimization role: **Capability & method architect** (Human engineering role (AI/robotics)) — chooses the right model tier and optimization method for each capability — balancing exhaustiveness, efficiency, determinism, latency, cost, and verifiability. Part of the layer that decides *how* robot and machine capabilities are built — across model tiers (LLM, SLM, tiny LM, deterministic) and many training methods (imitation, model-based/offline RL, RLHF/RLAIF, sim-to-real, distillation, classical control, formal methods). Use this skill when choosing or building how a capability is trained, optimized, or run on-device, even if the user only describes the underlying need. Works under a head of autonomy / ML."
---

# Capability & Optimization — Capability & method architect

> **Layer:** Capability / optimization spectrum (how robots and machines are made capable) · **Type:** Human engineering role (AI/robotics)
> **Human supervisor:** head of autonomy / ML · **Used by:** `../embodied-ai-stack/`, `../autonomous-fleet-ops/`, robot & machine skills · **Shared concepts:** `../../00-framework/SKILL.md`

## What this role is

The **Capability & method architect** chooses the right model tier and optimization method for each capability — balancing exhaustiveness, efficiency, determinism, latency, cost, and verifiability. Decides LLM vs SLM vs tiny LM vs deterministic controller per task and which training method fits. This routing/selection discipline is the productizable core of the stack.

## Why this layer exists

RLAIF is **one** way to make an embodied system capable — not the only or always the best one. Capability is **right-sized per task** across a heterogeneous stack and a spectrum of methods. This role owns the part of that spectrum described above, and works with the build-side roles in `_catalogs/embodied-ai-stack/` and the operations roles in `_catalogs/autonomous-fleet-ops/`.

## The capability/optimization spectrum (shared model)

Capability is **right-sized per task**, not delivered by one big model trained one way. CivStack assumes a heterogeneous capability stack and a spectrum of optimization methods:

**Model tiers (right-sized compute).**
- **LLM / large multimodal models** — deliberation, language tasking, long-tail reasoning, and planning (cloud or high-end edge).
- **SLMs (small language / vision-language models)** — on-device reasoning and perception at lower cost and latency.
- **Tiny LMs / specialized nets** — fast reactive perception and control within tight power and latency budgets.
- **Deterministic controllers** — PID, MPC, state machines, planners, and convex/MILP optimization for hard-real-time, verifiable, safety-critical loops.
A capability is assigned to the *smallest, most deterministic* tier that meets its accuracy, latency, and safety needs; the large model is invoked only when needed (cascade / routing).

**Optimization methods (exhaustive ↔ efficient).**
- **Imitation / behavior cloning** (BC, DAgger, inverse RL) — data-efficient bootstrap from demonstrations.
- **Model-based RL & world models** — learn a simulator and plan/imagine in it; sample-efficient.
- **Offline RL** — learn from logged data without risky online exploration.
- **RLHF / RLAIF / rule-based & constitutional rewards** — preference and reward shaping; **RLAIF is one option, not the only one**.
- **Sim-to-real** — massively parallel simulation, domain randomization, and system identification.
- **Self-supervised & representation learning** — pretrain from unlabeled data.
- **Supervised fine-tuning & distillation** — specialize and shrink (LLM → SLM → tiny LM).
- **Quantization / pruning / sparsity** — compress for the edge.
- **Search & planning** (MCTS, MPC, graph/sampling planners) — deterministic, verifiable run-time decisions.
- **Classical optimization & control** (convex, MILP, optimal control) and **formal methods / verification** — guarantees that statistical learning cannot give.
- **Evolutionary / black-box search** — when gradients are unavailable.

**Selection rubric.** Choose by exhaustiveness vs efficiency (compute and data budget), determinism and verifiability (safety-criticality), latency and power (on-device vs offloaded), data availability (demos vs logs vs sim), and reversibility/consequence. Safety-critical and hard-real-time loops favor deterministic, verifiable methods; open-ended judgment favors large learned models; **most real systems are hybrids** with a verified deterministic safety layer beneath learned policies. The roles that design and run this spectrum are in `_catalogs/capability-optimization/`.

## When to use this skill

Use it when a task calls for this work: chooses the right model tier and optimization method for each capability — balancing exhaustiveness, efficiency, determinism, latency, cost, and verifiability. Pair with the robot skills (`_catalogs/humanoid-robots/`, `<sector>/robots/`) and machine skills (`_catalogs/autonomous-machines/`, `<sector>/autonomous/`) whose capabilities are being trained, optimized, or deployed.

## Decision rights & accountability

- **Owns** the technical quality, efficiency, and robustness of this method/layer.
- **Justifies** the method and model-tier choice against the selection rubric (exhaustiveness vs efficiency, determinism, latency, verifiability).
- **Gates** promotion to production with the safety and evaluation leads.

## How this role chooses (selection discipline)

1. State the capability, its accuracy bar, latency/power budget, and safety-criticality.
2. Pick the **smallest, most deterministic** model tier that can meet it (deterministic → tiny LM → SLM → LLM).
3. Pick the **most efficient** optimization method that reaches the bar with available data (demos → sim → logs → online).
4. Reserve large learned models for open-ended judgment; reserve deterministic/verified methods for safety-critical loops.
5. Measure on the real task, compare tiers/methods, and keep a verified safety layer beneath anything learned.

> **Decision tool:** use the routing matrix in `docs/capability-routing-matrix.md` and the interactive selector `tools/capability-router.html` to turn a capability's constraints (safety, latency, verifiability, task type, data, compute, connectivity) into a recommended tier, method, and fallback.

## Failure modes and safeguards

- **Over-reach** — using a large learned model where a verifiable controller would be safer and cheaper. Mitigation: the selection rubric and a verified safety layer.
- **Reward hacking / spec gaming** — learned objectives gamed. Mitigation: diverse signals, human spot-checks, outcome-based evaluation.
- **Sim-to-real and distribution shift** — training diverges from deployment. Mitigation: shadow mode, staged rollout, monitoring.
- **Efficiency/quality regressions** — compression or routing degrades behavior silently. Mitigation: continuous benchmarking across tiers.

## Adapting to any nation (context modifiers)

Compute, data, and connectivity budgets vary enormously; lower-resource settings push capability toward **smaller, on-device, and deterministic** methods, and toward distillation of expensive models into cheap ones. Re-read through:

- **Scale** (city-state → federation): whether this role is unified or layered across local/regional/national tiers.
- **State capacity** (fragile → high-capacity): whether the owning institution exists and can be held to account, or the job is met by markets, households, NGOs, or donors.
- **Income level** (low → high): affordability of automation and the balance of subsistence vs. wage work.
- **Formality** (informal → formal): whether the people and assets this role acts on appear in any registry at all.
- **Resource & geography**: which hazards and dependencies dominate (water-scarce, flood-prone, landlocked, trade-dependent).
- **Political system & legitimacy**: where the human-accountability boundary actually binds and who may hold power to account.

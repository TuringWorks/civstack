# Capability Routing Matrix

**How to decide the way each robot/machine capability is built and run** — which model tier and which optimization method, with a safe fallback. This is the working tool for the *Capability & method architect* role (`skills/_catalogs/capability-optimization/capability-method-architect/`). For an interactive version, open [`tools/capability-router.html`](../tools/capability-router.html).

The core principle: **assign every capability to the smallest, most deterministic model tier and the most efficient optimization method that meets its accuracy, latency, and safety bar — with a verified deterministic safety layer beneath anything learned.** RLAIF is one method among many.

---

## The decision inputs

| Dimension | Values | Why it matters |
|---|---|---|
| **Safety-criticality / consequence** | low · medium · high (life-safety, irreversible) | High pushes toward deterministic, verifiable methods and a hard safety layer |
| **Latency budget** | relaxed (cloud OK) · real-time on-device · hard-real-time control loop | Hard-real-time forbids cloud/large models in the loop |
| **Verifiability need** | nice-to-have · required (must be provable) | Required pushes toward formal methods and classical control |
| **Task type** | structured perception/control · optimization & scheduling · open-ended reasoning & language | Open-ended favors large learned models; optimization favors exact solvers |
| **Data available** | demonstrations · logged data · simulator · little/none | Determines imitation vs offline RL vs sim-to-real vs self-supervised |
| **Compute & power** | ample (cloud/datacenter) · edge-constrained · tiny embedded | Tighter budgets force distillation/compression and smaller tiers |
| **Connectivity** | reliable · intermittent · none | Intermittent/none forces on-device autonomy and safe-stop, not teleop |

## The model tiers (right-sized compute)

1. **Deterministic controllers** — PID, MPC, state machines, planners, convex/MILP. Verifiable, cheap, hard-real-time. The safety backbone.
2. **Tiny LMs / specialized nets** — fast reactive perception and control within tight power/latency budgets.
3. **SLMs** (small language / vision-language models) — on-device reasoning and perception at moderate cost.
4. **LLMs / large multimodal models** — deliberation, language tasking, long-tail reasoning, planning. Cloud or high-end edge.

Most real systems are **cascades**: a small/deterministic tier handles the common case in-loop, and a larger model is invoked only for the hard or open-ended part.

## The optimization methods (exhaustive ↔ efficient)

- **Imitation / behavior cloning** (BC, DAgger, inverse RL) — efficient bootstrap from demonstrations.
- **Model-based RL & world models** — learn a simulator, plan/imagine; sample-efficient.
- **Offline RL** — learn from logged data without risky online exploration.
- **RLHF / RLAIF / rule-based & constitutional rewards** — preference/reward shaping.
- **Sim-to-real** — massively parallel simulation + domain randomization + system identification.
- **Self-supervised & representation learning** — pretrain from unlabeled data.
- **Supervised fine-tuning & distillation** — specialize and shrink (LLM → SLM → tiny LM).
- **Quantization / pruning / sparsity** — compress for the edge.
- **Search & planning** (MCTS, MPC, graph/sampling planners) — deterministic, verifiable run-time decisions.
- **Classical optimization & control** (convex, MILP, optimal control) — provable, exact.
- **Formal methods & verification** — guarantees learning cannot give.
- **Evolutionary / black-box search** — when gradients are unavailable.

---

## Capability archetype lookup

A quick map from common embodied capabilities to a sensible default. Treat as a starting point, then adjust with the decision rules below.

| Capability archetype | Default tier | Primary method(s) | Fallback / safety |
|---|---|---|---|
| Hard-real-time motion control (balance, steering, stability) | Deterministic (PID/MPC) + tiny net | Classical/optimal control; model-based RL to tune | Verified envelope + safe-stop |
| Obstacle avoidance / collision prevention | Deterministic + tiny LM | Sim-to-real + model-based RL; runtime monitor | Verified safety layer overrides |
| Dexterous manipulation / grasp novel objects | SLM / VLA on-device | Imitation (BC/DAgger) → offline RL → sim-to-real | Teleop handoff |
| Perception / detection (pests, defects, pedestrians) | Tiny LM / specialized net | Self-supervised pretrain + supervised fine-tune | Human review on low confidence |
| Mission planning / task decomposition / NL tasking | LLM (cloud or high-end edge) | SFT + RLHF/RLAIF + tool-use | Human approval; deterministic plan checks |
| Long-tail edge-case reasoning | LLM | RLHF/RLAIF + retrieval | Teleop / human takeover |
| Routing / scheduling / allocation | Deterministic (MILP/convex/search) | Classical optimization; learned warm-start | Exact-solver fallback |
| Anomaly detection on telemetry | Tiny LM / classical (+ SLM) | Self-supervised + offline; rules | Human triage |
| Document understanding / drafting | SLM or LLM | SFT + RLHF | Human signoff |
| Conversational / citizen intake | SLM on-device (or LLM) | SFT + RLHF/RLAIF | Human escalation |
| Forecasting (load, yield, demand) | Classical/statistical + tiny | Supervised/time-series; model-based | Human review |

---

## Decision rules (apply in order)

1. **Safety-critical + hard-real-time → deterministic + formal verification.** Use a classical controller (PID/MPC) inside a verified envelope. Any learned model is advisory only, above the safety layer, never in the irreversible loop.
2. **Hard-real-time control loop (any safety) → no cloud, no large model in the loop.** Use a deterministic controller or a tiny LM distilled for the device; the brain sets goals, the loop executes.
3. **Verifiability required → prefer classical/optimization + formal methods.** If a learned component is unavoidable, wrap it with runtime monitors and a verified override.
4. **Optimization / scheduling / allocation → exact solver first.** MILP/convex/search give provable answers; use learned heuristics only to warm-start or to scale.
5. **Open-ended reasoning / language / long-tail → large learned model, right-sized by budget.**
   - Ample compute & connectivity → **LLM** (cloud/high-end edge), cascade down for routine.
   - Edge-constrained → **SLM on-device**, escalate to LLM for the long tail.
   - Tiny embedded or no connectivity → **distilled SLM/tiny on-device**, with a deterministic fallback.
6. **Structured perception/control → smallest learned tier that hits accuracy.** Tiny/specialized net if edge-constrained; SLM/VLA otherwise.
7. **Pick the method by the data you have:** demonstrations → imitation (then offline RL); simulator + risky exploration → sim-to-real / model-based RL; logged data → offline RL + SFT; little/none → self-supervised pretraining + collect demos/sim, and ship a deterministic baseline meanwhile. For language/preference behavior, add SFT + RLHF/RLAIF.
8. **Edge or tiny budget → distill and compress.** Train large, then distill LLM → SLM → tiny and quantize/prune to fit power and latency.
9. **Intermittent/no connectivity → on-device autonomy + safe-stop.** Do not depend on a cloud model or teleoperation for safety; degrade gracefully.
10. **Always: a verified deterministic safety layer beneath anything learned** for any physical action, with a minimal-risk maneuver (safe-stop / return-to-base / hover) it can trigger independently of the brain.

---

## Worked examples

**Autonomous tractor, remote field, no connectivity.** Structured control, medium safety, hard-real-time steering, tiny-to-edge compute, no connectivity. → **Deterministic guidance (GPS/RTK + MPC) + tiny perception net** in the loop; **imitation + sim-to-real** for headland turns and implement control; **on-device safe-stop**, no teleop dependency. An SLM may plan the field task when a gateway is reachable, but never drives the loop.

**Robotaxi, dense urban driving.** Structured perception/control, high safety, hard-real-time, edge-constrained, reliable connectivity. → **Tiny/SLM perception + deterministic planning/MPC** in the loop with a **verified safety layer**; **sim-to-real + imitation + offline RL** from fleet data; an LLM handles only non-real-time reasoning (e.g. ambiguous-scene explanation, remote-operator assist). Fallback: minimal-risk maneuver + teleop.

**Pick ripe strawberries without bruising.** Dexterous manipulation, low safety, real-time on-device, demonstrations available. → **SLM/VLA on-device**, trained by **imitation (BC/DAgger) → offline RL → sim-to-real**, distilled to fit the arm controller; fallback: skip-and-flag low-confidence fruit.

**Benefits-eligibility drafting (digital).** Open-ended language, no physical risk, relaxed latency, logged cases. → **SLM or LLM** with **SFT + RLHF**; deterministic rule checks for hard eligibility constraints; **human officer decides** the denial/appeal (the accountability boundary).

**Grid-frequency control.** Optimization + hard-real-time + high safety + verifiability required. → **Classical optimal control / deterministic dispatch + MILP**, formally verified; learned models only forecast inputs (load/renewables), never actuate the safety loop.

---

*This matrix is a design aid, not a guarantee. Re-derive per context (compute, data, connectivity, and regulation differ by nation and operator), validate on the real task, and keep humans accountable for the decisions on the [stays-human](../skills/00-framework/SKILL.md) list.*

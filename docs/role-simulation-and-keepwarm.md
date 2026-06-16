# Role Simulators & the Keep-Warm Program

**How to use job and role simulators to address deskilling across the economy.** Deskilling is the slow loss, as automation handles the routine, of the human capacity to take over when it fails. This is the design tool for the *Deskilling watch & keep-warm* sections in every sector skill and for the roles in [`../skills/_catalogs/simulation-training/`](../skills/_catalogs/simulation-training/).

## Deskilling is three problems, not one

1. **The human fallback bench** — who actually runs the system, manually, when automation degrades or fails. Untested fallback is not fallback.
2. **Tacit / craft judgment** — the experienced cohort's "feel," lost when they retire and aren't replaced.
3. **The learning ladder** — automation eats the entry-level cases people used to learn on, so no one accumulates the experience needed for the hard cases. This one is invisible until a generation of experts is simply missing.

## The universal keep-warm levers (every operating system)

- **Keep a manual mode and rehearse it** — periodic "automation off" runs, drills, full-scale exercises.
- **Protect the learning ladder** — deliberately route a share of routine cases to juniors even when AI is faster, to build the experience curve.
- **Capture tacit knowledge before it walks out** — structured transfer, recorded reasoning, demonstrations.
- **Train the new skill: AI oversight** — calibrated trust (when to believe vs. override), the antidote to automation bias. The only safe place to drill it is a simulator that can *fail on purpose*.
- **Measure bench readiness** — time-to-manual, drill pass rates, recertification status, and bench depth, treated as KPIs.

## Why simulators are the primary countermeasure

The skills you need most — for rare, high-consequence, manual-reversion events — are the ones automated normal operations never let you practice. Simulators manufacture that practice safely. Precedent is strong and old: full-flight simulators, NERC grid-operator and nuclear control-room simulators, medical simulation and standardized patients, military wargaming.

A simulator buys you: **currency** (rehearse the rare degraded scenario), **a rebuilt learning ladder** (thousands of reps on cases automation now hides), **safe failure** (practice the dangerous cases with no consequence), **oversight training** (simulate the automation failing — hallucinated actions, sensor spoofing, drift — so humans practice catching it), and **objective certification**.

## The dual-use idea (specific to this framework)

CivStack already assumes **world models, robot gyms, and sim-to-real** to *train the machines*. The same world model that teaches a policy to drive a tractor or read an image can be the simulator that keeps the **human** operator and the next cohort sharp; the demonstration data captured to train robots via imitation learning doubles as the case library that transfers expert judgment to juniors.

**One simulation substrate, two students** — the model and the human. This collapses the biggest objection to keep-warm programs (cost): you are not building a separate training system, you are exposing a second interface onto infrastructure you already need. The `simulation-training` roles sit alongside the `embodied-ai-stack` and `capability-optimization` roles that build that substrate.

## Fit by domain

| Fit | Domains | Notes |
|---|---|---|
| **High** | Aviation, grid, nuclear, water/chemical process, emergency response, defense, acute medicine | Procedural, high-consequence; sim transfer well-proven |
| **Medium** | Manufacturing, construction, surgery | Craft/dexterity — needs physical or hardware-in-the-loop rigs, not just screens |
| **Lower** | Eldercare, teaching, social work, editorial, field naturalism | Relational/embodied/social-trust — role-play and standardized-patient methods help at the margins; real human contact still does much of the forming. Be skeptical of "sim solves it" here |

## Types of simulators

Full-physical (flight sim, control room), digital-twin / world-model-based, VR/AR skill rigs, hardware-in-the-loop, tabletop and scenario exercises, standardized-patient / role-play, and **AI-driven scenario generation** (an LLM mines real incidents into drills, plays the counterpart role, or injects adversarial automation failures for oversight practice).

## Caveats — simulators can themselves deskill

- **Sim-to-real (and sim-to-human) gap** — you can train people to be good at the simulator, not the world. Anchor with periodic real practice; measure transfer.
- **Encoding the automation's worldview** — a sim that bakes in the model's assumptions teaches the model's world, not reality. Use adversarial and out-of-distribution scenarios and real-incident mining.
- **Cut under throughput pressure** — keep-warm is deliberately "inefficient" time and is the first thing cancelled; it needs a mandate, a schedule, and an accountable owner (the drill & exercise coordinator, working with OS 22).
- **Equity/access** — sim is cheaper and more scalable than real practice (a genuine leapfrog opportunity for lower-resource settings), but fidelity and access still vary.

## How it connects in the library

- **Per sector:** each sector skill's *Deskilling watch & keep-warm* section names the specific risk, countermeasures, and simulator regime.
- **OS 22 (Resilience):** owns the standing, cross-sector drill and bench-readiness program.
- **`_catalogs/simulation-training/`:** curriculum designer, scenario-generation agent, competency/certification agent, drill & exercise coordinator, dual-use world-model & fidelity engineer, tacit-knowledge capture agent.
- **`_catalogs/capability-optimization/`:** the *verified deterministic fallback beneath anything learned* is the technical half of keeping a human-operable system underneath the automation.

---

*Honest framing: every keep-warm measure costs throughput, and there is real disagreement about how much to pay. The case for paying it is that the failures you are insuring against are exactly the moments you cannot afford to have lost the skill — and that learning-ladder erosion is invisible right up until the experts you needed were never trained.*

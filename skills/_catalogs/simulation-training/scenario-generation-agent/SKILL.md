---
name: "simtrain-scenario-generation-agent"
description: "Anti-deskilling / keep-warm role: **Scenario-generation agent** (AI agent) — mines real incidents, logs, and near-misses into drill scenarios and adversarial edge cases, including simulated AI failures for oversight training. Part of the layer that uses **job and role simulators** to keep humans current, rebuild the learning ladder, and capture tacit knowledge — reusing the world models and simulators built to train the machines. Use this skill when designing or running human upskilling, drills, certification, or fallback-readiness, even if the user only describes the underlying need. Works under a simulation designer."
---

# Simulation & Keep-Warm — Scenario-generation agent

> **Layer:** Anti-deskilling / keep-warm (job & role simulators for humans) · **Type:** AI agent
> **Human supervisor:** simulation designer · **Reuses:** `../embodied-ai-stack/` and `../capability-optimization/` sim infrastructure · **Reference:** `docs/role-simulation-and-keepwarm.md`

## What this role is

The **Scenario-generation agent** mines real incidents, logs, and near-misses into drill scenarios and adversarial edge cases, including simulated AI failures for oversight training. Turns operational data into a stream of varied, progressively harder scenarios, and deliberately injects automation failures (hallucinated actions, sensor spoofing, drift) so humans practice detecting and overriding them.

## Why this layer exists

Automating routine cases erodes three things: the **human fallback bench**, **tacit / craft judgment**, and the **learning ladder**. Job and role simulators are the most effective countermeasure — and the **same world models and simulators built to train the machines double as the environments that keep humans current** (one simulation substrate, two students). This role owns the part of that program described above.

## When to use this skill

Use it when a task calls for this work: mines real incidents, logs, and near-misses into drill scenarios and adversarial edge cases, including simulated AI failures for oversight training. Pair with OS 22 (Resilience), the sector skills' *Deskilling watch & keep-warm* sections, and the sim infrastructure in `_catalogs/embodied-ai-stack/` and `_catalogs/capability-optimization/`.

## Decision rights & accountability

- **May act autonomously** on routine scenario generation, assessment, and capture within policy.
- **Must defer** to human trainers/safety leads on what counts as competent and on certification.
- **Must escalate** detected skill gaps and recurring failure patterns.

## Fit by domain (where simulators transfer well — and don't)

- **High fit:** procedural, high-consequence domains (aviation, grid, nuclear, water/chemical, emergency, defense, acute medicine). Sim transfer is well-proven.
- **Medium fit:** craft and dexterity (manufacturing, construction, surgery) — needs physical or hardware-in-the-loop rigs, not just screens.
- **Lower fit:** relational, embodied, social-trust work (eldercare, teaching, social work, editorial) — role-play and standardized-patient methods help at the margins, but real human contact still does much of the forming.

## Failure modes and safeguards

- **Sim-to-real (and sim-to-human) gap** — training people to be good at the simulator, not the world. Mitigation: anchor with periodic real practice; measure transfer.
- **Encoding the automation's worldview** — a sim that bakes in the model's assumptions teaches the model's world. Mitigation: adversarial and out-of-distribution scenarios, real-incident mining.
- **Practice cut under throughput pressure** — keep-warm is "inefficient" time and gets cancelled first. Mitigation: mandate, schedule, and metrics owned by an accountable human.

## Adapting to any nation (context modifiers)

Simulators are cheaper and more scalable than real practice, which makes them a leapfrog opportunity for lower-resource settings; fidelity and access still vary. Re-read through:

- **Scale** (city-state → federation): whether this role is unified or layered across local/regional/national tiers.
- **State capacity** (fragile → high-capacity): whether the owning institution exists and can be held to account, or the job is met by markets, households, NGOs, or donors.
- **Income level** (low → high): affordability of automation and the balance of subsistence vs. wage work.
- **Formality** (informal → formal): whether the people and assets this role acts on appear in any registry at all.
- **Resource & geography**: which hazards and dependencies dominate (water-scarce, flood-prone, landlocked, trade-dependent).
- **Political system & legitimacy**: where the human-accountability boundary actually binds and who may hold power to account.

## Operating procedure

1. Identify the skill at risk of erosion and the scenario that exercises it (especially the rare, degraded, manual-reversion case).
2. Build or reuse the simulator (prefer the sector's existing machine-training world models); set fidelity to the skill.
3. Run the drill/curriculum; inject automation-failure scenarios to train oversight.
4. Assess competency, log bench-readiness metrics, and escalate gaps to the accountable human.

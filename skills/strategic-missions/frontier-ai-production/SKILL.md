---
name: "mission-frontier-ai-production"
description: "Strategic mission (cross-cutting national capability): **Frontier AI Production** — Create AI systems that are capable, reliable, secure, useful, economically productive, and governable. Unlike the 22 sector operating systems, a mission composes several of them toward one strategic objective. Use this skill to plan or coordinate this mission end-to-end; trigger whenever work concerns frontier ai production, even if the user only names a piece of it."
---

# Strategic Mission — Frontier AI Production

> **Layer:** Strategic mission (cross-cutting capability that composes multiple operating systems)
> **Shared concepts:** `../../00-framework/SKILL.md` · **Imported/adapted from the Agentic-Workforce operating models**

## Purpose

Define the work system for building, evaluating, deploying, governing, and improving frontier AI models and AI-native products.

## Mission

Create AI systems that are capable, reliable, secure, useful, economically productive, and governable.

## Operating systems this mission composes

A strategic mission is an *orthogonal* axis to the 22 sectors: it pulls roles and capabilities from several of them toward one objective. This mission primarily draws on:

- [12. Communications, Software, Cybersecurity, and Digital Infrastructure](../../12-communications/)
- [15. Science, Research, Standards, and Innovation](../../15-science/)
- [07. Energy, Utilities, and Grid Operations](../../07-energy/)
- [08. Mining, Materials, Chemicals, and Industrial Inputs](../../08-mining/)
- [20. Labor, Workforce Systems, and Organizational Life](../../20-labor/)

Deploy the relevant sector and role skills under those operating systems as the building blocks; this skill coordinates them toward the mission.

## Core capabilities

- Data planning and lineage.
- Architecture and training.
- Evaluation and benchmarking.
- Red-teaming and safety.
- ML platform and inference.
- Model and supply-chain security.
- Governance, risk tiering, and approval gates.
- Product fit and adoption.

## Human command roles

- AI lab lead.
- Model training lead.
- Model evaluation lead.
- AI governance lead.
- AI product lead.
- ML platform lead.
- Security lead.
- Data steward.

These hold accountability for the mission. Strategic prioritization, public legitimacy, security, and ethical tradeoffs stay human-owned.

## AI personnel

- Literature/research agent.
- Experiment planning agent.
- Data curation agent.
- Synthetic data agent.
- Training run monitor.
- Evaluation agent.
- Red-team agent.
- Documentation/model-card agent.
- Incident analysis agent.

Many of these map to existing role skills in the composed operating systems (e.g. `_catalogs/ai-personnel/` and the sectors' `roles/`). Reuse them rather than rebuilding.

## Robot / machine personnel

- Data center inspection robot.
- Hardware logistics robot.
- Lab robot for embodied-AI testing.

See `_catalogs/humanoid-robots/`, `_catalogs/autonomous-machines/`, and the sectors' `robots/` and `autonomous/` folders.

## Operating loop

1. Define model mission, users, prohibited uses, risk tier.
2. Build a data plan (provenance, rights, privacy, contamination controls).
3. Select architecture, training strategy, compute, eval gates.
4. Run versioned experiments.
5. Evaluate capability, safety, robustness, bias, cost.
6. Red-team before release.
7. Stage deployment with monitoring and rollback.
8. Analyze incidents and economics.
9. Retrain, fine-tune, or deprecate on evidence.

## Human accountability boundary

Strategic prioritization, public legitimacy, national-security judgment, scarce-resource allocation, export-control and safety decisions, and final signoff on irreversible commitments remain human-accountable. AI personnel and robots accelerate the work up to that line.

## How to use this skill

1. Read the mission and the operating systems it composes.
2. Pull the specific sector and role skills you need from those OSs.
3. Run the operating loop, coordinating across sectors at the seams.
4. Apply the command & cadence model (`00-framework/`) and stop at the accountability boundary.

## Adapting to any nation (context modifiers)

Whether a nation pursues this mission at all — and how (sovereign build, ally-and-buy, or import) — depends heavily on scale, income, resource endowment, and geopolitics. Re-read through:

- **Scale** (city-state → federation): whether this role is unified or layered across local/regional/national tiers.
- **State capacity** (fragile → high-capacity): whether the owning institution exists and can be held to account, or the job is met by markets, households, NGOs, or donors.
- **Income level** (low → high): affordability of automation and the balance of subsistence vs. wage work.
- **Formality** (informal → formal): whether the people and assets this role acts on appear in any registry at all.
- **Resource & geography**: which hazards and dependencies dominate (water-scarce, flood-prone, landlocked, trade-dependent).
- **Political system & legitimacy**: where the human-accountability boundary actually binds and who may hold power to account.

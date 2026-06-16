---
name: "mission-cyber-defense"
description: "Strategic mission (cross-cutting national capability): **Cyber Defense** — Detect, prevent, respond to, and recover from cyber threats across public, private, critical, and strategic technology systems. Unlike the 22 sector operating systems, a mission composes several of them toward one strategic objective. Use this skill to plan or coordinate this mission end-to-end; trigger whenever work concerns cyber defense, even if the user only names a piece of it."
---

# Strategic Mission — Cyber Defense

> **Layer:** Strategic mission (cross-cutting capability that composes multiple operating systems)
> **Shared concepts:** `../../00-framework/SKILL.md` · **Imported/adapted from the Agentic-Workforce operating models**

## Purpose

Defend national, industrial, and institutional digital systems in an AI-accelerated threat environment.

## Mission

Detect, prevent, respond to, and recover from cyber threats across public, private, critical, and strategic technology systems.

## Operating systems this mission composes

A strategic mission is an *orthogonal* axis to the 22 sectors: it pulls roles and capabilities from several of them toward one objective. This mission primarily draws on:

- [12. Communications, Software, Cybersecurity, and Digital Infrastructure](../../12-communications/)
- [03. Defense, Intelligence, Border, and Foreign Affairs](../../03-defense/)
- [22. Resilience, Continuity, and Strategic Foresight](../../22-resilience/)
- [04. Public Safety, Justice Operations, and Emergency Response](../../04-public-safety/)

Deploy the relevant sector and role skills under those operating systems as the building blocks; this skill coordinates them toward the mission.

## Core capabilities

- Asset inventory.
- Identity and access management.
- Security monitoring and detection.
- Incident response.
- Threat intelligence.
- Vulnerability management.
- Secure software supply chain.
- AI system security.
- Resilience and disaster recovery.

## Human command roles

- Cyber commander.
- CISO.
- SOC lead.
- Incident commander.
- Threat intelligence lead.
- Vulnerability management lead.
- Secure software supply-chain lead.
- AI security lead.

These hold accountability for the mission. Strategic prioritization, public legitimacy, security, and ethical tradeoffs stay human-owned.

## AI personnel

- Cyber triage agent.
- Threat intelligence agent.
- Vulnerability prioritization agent.
- Incident response copilot.
- Malware/reverse-engineering assistant.
- Identity anomaly detector.
- Software supply-chain risk agent.
- Red-team agent.

Many of these map to existing role skills in the composed operating systems (e.g. `_catalogs/ai-personnel/` and the sectors' `roles/`). Reuse them rather than rebuilding.

## Robot / machine personnel

- Data center technician robot.
- Facilities/security patrol robot.
- Hardware chain-of-custody robot.

See `_catalogs/humanoid-robots/`, `_catalogs/autonomous-machines/`, and the sectors' `robots/` and `autonomous/` folders.

## Operating loop

1. Maintain asset, identity, service, data, dependency inventories.
2. Monitor signals and enrich alerts.
3. Triage incidents and assign severity.
4. Contain, eradicate, recover, communicate.
5. Patch vulnerabilities and harden controls.
6. Run exercises, red teams, postmortems.
7. Feed lessons into architecture and procurement.

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

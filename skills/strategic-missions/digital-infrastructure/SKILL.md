---
name: "mission-digital-infrastructure"
description: "Strategic mission (cross-cutting national capability): **Digital Infrastructure** — Keep digital systems available, secure, interoperable, scalable, and trusted. Unlike the sector operating systems, a mission composes several of them toward one strategic objective. Use this skill to plan or coordinate this mission end-to-end; trigger whenever work concerns digital infrastructure, even if the user only names a piece of it."
---

# Strategic Mission — Digital Infrastructure

> **Layer:** Strategic mission (cross-cutting capability that composes multiple operating systems)
> **Shared concepts:** `../../00-framework/SKILL.md` · **Imported/adapted from the Agentic-Workforce operating models**

## Purpose

Coordinate software, cloud, telecom, data centers, cybersecurity, data platforms, and AI platforms as strategic national infrastructure.

## Mission

Keep digital systems available, secure, interoperable, scalable, and trusted.

## Operating systems this mission composes

A strategic mission is an *orthogonal* axis to the sectors: it pulls roles and capabilities from several of them toward one objective. This mission primarily draws on:

- [12. Communications, Software, Cybersecurity, and Digital Infrastructure](../../12-communications/)
- [07. Energy, Utilities, and Grid Operations](../../07-energy/)
- [16. Finance, Insurance, Payments, and Capital Markets](../../16-finance/)
- [01. Governance, Law, and Public Administration](../../01-governance/)
- [23. Identity, Civil Registration, and Digital Public Infrastructure](../../23-identity/)

Deploy the relevant sector and role skills under those operating systems as the building blocks; this skill coordinates them toward the mission.

## Core capabilities

- Software engineering.
- Cloud and platform engineering.
- Data engineering and governance.
- Telecom and network operations.
- Data center operations.
- Cyber defense and resilience.
- AI/ML platform operations.
- Digital identity and access.
- Digital public infrastructure.

## Human command roles

- Chief digital infrastructure officer.
- Platform engineering director.
- Cloud/data center director.
- CISO/cyber commander.
- Data governance lead.
- AI platform lead.
- Product/service owner.
- Privacy and trust lead.

These hold accountability for the mission. Strategic prioritization, public legitimacy, security, and ethical tradeoffs stay human-owned.

## AI personnel

- Coding agent.
- Test generation agent.
- Incident response copilot.
- SOC triage agent.
- Data quality agent.
- Capacity planner.
- Documentation agent.
- Compliance review agent.
- Model evaluation agent.

Many of these map to existing role skills in the composed operating systems (e.g. `_catalogs/ai-personnel/` and the sectors' `roles/`). Reuse them rather than rebuilding.

## Robot / machine personnel

- Data center technician robot.
- Facilities maintainer robot.
- Inspection walker.
- Secure document/hardware logistics robot.

See `_catalogs/humanoid-robots/`, `_catalogs/autonomous-machines/`, and the sectors' `robots/` and `autonomous/` folders.

## Operating loop

1. Service owner defines need, reliability target, security tier, data class.
2. Build with AI coding/test/documentation support.
3. Deploy with CI/CD, observability, access control, rollback.
4. Cyber teams monitor with AI triage and human incident command.
5. Data teams monitor lineage, quality, privacy, retention.
6. Maintain physical infra with robot inspection.
7. Governance reviews incidents, risks, audits, public impact.

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

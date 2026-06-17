# Agentic Workforce Library

Purpose: turn the country/economy JTBD map into reusable artifacts for LLMs, AI agents, and humanoid robot planners.

Use this library when designing national capabilities, institution operating models, AI personnel, robot workforces, job descriptions, training plans, or automation roadmaps.

## Folder Map

- `domains/`: workspace-local skill packs for each national operating system.
- `catalogs/`: shared taxonomies of AI personnel, humanoid robot roles, accountability boundaries, and role archetypes.
- `templates/`: reusable templates for role cards, domain skills, agent briefs, robot briefs, and operating procedures.
- `roles/`: detailed cards for human command roles, AI personnel, and humanoid robot roles.
- `operating-models/`: coordination models for human-AI-robot command systems and strategic sectors.
- `checklists/`: deployment readiness, governance, and safety checklists.
- `strategies/`: cross-domain strategies, including frontier-technology preeminence.
- `physical-ai/`: non-humanoid physical AI skills and role cards for autonomous vehicles, farm equipment, harvesters, drones, loaders, AMRs, rail, marine, and fixed robotic cells.

## Current Inventory

- 22 domain skill packs, one for each country/economy operating system.
- Detailed role cards across:
  - human command roles.
  - AI-personnel roles.
  - humanoid/specialized robot roles.
- 13 operating models:
  - human-AI-robot command system.
  - frontier AI production.
  - digital infrastructure.
  - semiconductor sovereignty.
  - advanced manufacturing.
  - energy abundance.
  - science-to-industry.
  - strategic supply chain.
  - frontier talent formation.
  - cyber defense.
  - bioeconomy.
  - quantum and space systems.
  - public procurement for frontier technology.
- 1 deployment readiness checklist.
- 4 shared catalogs.
- 3 reusable templates.
- 1 frontier technology preeminence strategy.
- Dedicated non-humanoid physical AI layer with platform skills, operating models, safety catalog, deployment checklist, and autonomous machine role cards.

## How To Use

1. Start with the relevant domain `SKILL.md`.
2. Read the shared catalogs only when the task needs cross-domain consistency.
3. Create role cards from `templates/role-card.md`.
4. Create agent briefs from `templates/ai-agent-brief.md`.
5. Create robot briefs from `templates/robot-role-brief.md`.
6. Keep every generated role tied to a human accountable owner.

## Recommended Next Expansion

Proceed domain by domain. For each domain, create:

- 10-25 human accountable role cards.
- 5-15 AI-personnel briefs.
- 3-10 humanoid or specialized robot briefs.
- 1 operating model showing how humans, AI personnel, and robots coordinate.
- 1 governance checklist with metrics, failure modes, and escalation paths.

For technology preeminence, expand first:

1. `domains/12-digital-infrastructure`
2. `domains/15-science-innovation`
3. `domains/09-manufacturing`
4. `domains/07-energy-utilities`
5. `domains/08-materials-chemicals`
6. `domains/11-transport-logistics`
7. `domains/03-defense-foreign-affairs`
8. `domains/14-education-human-capital`

## Expansion Rule

For each role, capture:

- Mission: the durable outcome the role exists to produce.
- Trigger: when the role activates.
- Inputs: data, materials, authority, tools, relationships.
- Work loop: sense, interpret, decide, mobilize, execute, verify, govern.
- Interfaces: who or what the role coordinates with.
- AI delegation: tasks suitable for AI personnel.
- Robot delegation: physical tasks suitable for humanoid or specialized robots.
- Human boundary: decisions that must remain human-accountable.
- Metrics: leading and lagging indicators.
- Failure modes: harms to prevent.
- Training data/context: what an LLM or agent must know to act well.

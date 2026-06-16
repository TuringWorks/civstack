# Coverage Matrix

Where to look in CivStack for common requests — a traceability map from a user-mentioned area to the skills that cover it. Imported/adapted from the Agentic-Workforce use-case matrix and extended to the full library.

## Physical AI / autonomous machines

| You mentioned | Start here | Key machine roles | Key operators |
|---|---|---|---|
| Self-driving cars / trucks / shuttles | `skills/11-transportation/autonomous/`, `skills/_catalogs/autonomous-machines/` | robotaxi, freight truck, shuttle, last-mile vehicle, yard mover | fleet director, freight-autonomy lead, fleet safety operator |
| Self-driving farm equipment, harvesters | `skills/05-food/autonomous/` | autonomous tractor, harvester/combine, spray & scout drones | farm-autonomy manager |
| Loaders / mine equipment | `skills/08-mining/autonomous/`, `skills/10-shelter/autonomous/` | haul truck, loader/excavator, blast-hole drill, earthmover | heavy-equipment autonomy lead |
| Drones (survey, spray, delivery, inspection) | `skills/_catalogs/autonomous-machines/`, sector `autonomous/` | survey/inspection drone, spray drone, delivery drone | drone operations lead |
| Warehouses, forklifts, ports | `skills/17-commerce/autonomous/`, `skills/11-transportation/autonomous/` | warehouse AMR, autonomous forklift, port carrier, yard mover | warehouse automation lead |
| Rail / marine / underwater | `skills/11-transportation/autonomous/`, `_catalogs/autonomous-machines/` | freight/metro train, harbor USV, underwater ROV/AUV | rail authority, marine autonomy lead |
| Fixed industrial robots | `skills/_catalogs/autonomous-machines/fixed-industrial-robotic-cell/`, `skills/09-manufacturing/` | fixed robotic cell, machine-tending | automation engineering lead |
| Humanoid robots | `skills/_catalogs/humanoid-robots/`, `skills/05-food/robots/` | material runner, care aide, field/livestock robots | per-sector supervisor |
| How the machines are built & run | `skills/_catalogs/embodied-ai-stack/`, `autonomous-fleet-ops/`, `capability-optimization/` | brain, VLA policy, ODD/safety, teleop, method router | autonomy & safety leads |

## By sector

Each of the 22 operating systems (`skills/01-…` … `skills/22-…`) carries its mission, jobs-to-be-done, human role families, AI-personnel role skills (`roles/`), robot/machine roles, accountability boundary, labor-market grounding, and a deskilling/keep-warm regime. Start from the sector skill, then deploy the specific role skills under it.

## By strategic mission

When the goal is a national capability that spans sectors, start from `skills/strategic-missions/`: energy abundance, semiconductor sovereignty, bioeconomy, frontier-AI production, quantum & space, strategic supply chain, science-to-industry, talent formation, public procurement, cyber defense, advanced manufacturing, digital infrastructure. Each lists the operating systems it composes and the roles to pull from them.

## Cross-cutting concerns

| You need | Look in |
|---|---|
| The reusable role pattern (strategist, operator, builder, …) | `skills/cross-cutting-archetypes/` |
| Reusable AI / robot role patterns | `skills/_catalogs/ai-personnel/`, `skills/_catalogs/humanoid-robots/` |
| How a capability should be built (tier + method) | `docs/capability-routing-matrix.md`, `tools/capability-router.html` |
| Addressing deskilling / keeping humans current | `docs/role-simulation-and-keepwarm.md`, `skills/_catalogs/simulation-training/`, OS 22 |
| Deploying a role or machine safely | `checklists/` |
| Authoring a new role / agent / robot | `templates/` |
| How humans, AI, and robots coordinate | the command & cadence model in `skills/00-framework/SKILL.md` |

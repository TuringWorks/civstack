# Two viewpoints: CivStack and Agentic-Workforce

CivStack (`skills/`) and Agentic-Workforce (`perspectives/agentic-workforce/`) are two
independent attempts at the same question: **how do you staff everything a country and
economy must do across humans, AI personnel, and robots — without losing accountability?**
They agree on the fundamentals and diverge in structure, depth, and emphasis. Holding
both makes each one's assumptions visible.

## Where they agree

- A society is a set of **durable jobs / outcomes**, organized into ~22 domains/sectors.
- Work is split across a **human owner + AI personnel + robots**, with the human keeping
  legitimacy, judgment, and final signoff.
- A **hard accountability boundary** marks what AI and robots may support but never decide.
- **Non-humanoid physical AI** (vehicles, farm equipment, drones, AMRs) is first-class,
  with an ODD, a safety case, and human override.

## Where they differ

| Dimension | CivStack | Agentic-Workforce |
|---|---|---|
| Authoring | **Generated** from one Python generator (regenerable, consistent) | **Hand-authored** Markdown |
| Size / shape | 360 skills; two axes (23 sectors × 12 missions) + deep catalogs | ~155 files; domains + operating-models + a focused physical-AI library |
| Primary strength | The **machinery**: capability/optimization spectrum, deskilling/keep-warm, JD grounding, informal economy, build/operate stack, accountability controls | The **strategy**: frontier-technology thesis, crisp physical-AI taxonomy, readiness checklists |
| Robots/machines | Architecture-deep (LLM brain → tool calls → VLA → world models/RLAIF; fleet-ops; capability routing) | Use-case-deep (platform taxonomy, deployment checklist, coverage matrix) |
| "How it's built" | Explicit `capability-optimization` layer (model tiers + many training methods) | Implicit |
| Deskilling | First-class (`simulation-training`, per-sector keep-warm) | Not addressed |
| Informal economy | First-class catalog | Not addressed |
| Identity / DPI | Operating system 23 | Not a distinct domain |
| Strategy narrative | Distributed across missions + transition-dynamics doc | A single `frontier-technology-preeminence` thesis |
| Granularity | Many small role skills | Fewer, broader workforce/role cards |

## Cross-walk (artifact ↔ artifact)

| Agentic-Workforce | CivStack counterpart |
|---|---|
| `domains/NN-*/SKILL.md` | `skills/NN-*/SKILL.md` (sector orchestrators) + their `roles/` |
| `operating-models/*-operating-model.md` | `skills/strategic-missions/*` |
| `operating-models/human-ai-robot-command-system.md` | the **command & cadence model** merged into `skills/00-framework/SKILL.md` |
| `physical-ai/skills/*`, `physical-ai/roles/autonomous-machines/*` | `skills/_catalogs/autonomous-machines/` + `skills/<sector>/autonomous/` |
| `physical-ai/roles/human-command/*`, `roles/human-command/*` | `skills/_catalogs/autonomous-fleet-ops/` (domain leads) + `skills/_catalogs/human-command/` |
| `physical-ai/roles/ai-personnel/*` | `skills/_catalogs/embodied-ai-stack/` + `skills/_catalogs/autonomous-fleet-ops/` |
| `physical-ai/catalogs/non-humanoid-physical-ai-taxonomy.md` | `docs/non-humanoid-platform-taxonomy.md` |
| `physical-ai/catalogs/safety-and-accountability-boundaries.md` | `docs/physical-ai-safety-boundaries.md` |
| `physical-ai/catalogs/use-case-coverage-matrix.md` | `docs/coverage-matrix.md` |
| `checklists/*`, `physical-ai/checklists/*` | `checklists/*` |
| `templates/*` | `templates/*` |
| `strategies/frontier-technology-preeminence.md` | `docs/frontier-technology-strategy.md` |
| `catalogs/ai-personnel-catalog.md`, `humanoid-robot-catalog.md`, `role-archetypes.md` | `skills/_catalogs/ai-personnel/`, `humanoid-robots/`, `skills/cross-cutting-archetypes/` |

## When to reach for which

- **Designing or deploying a specific role/machine, or wiring an agent** → CivStack. It is
  exhaustive, regenerable, and carries the accountability and capability machinery.
- **Framing national strategy or a board-level pitch** → Agentic-Workforce's operating
  models and the frontier-technology thesis read fast and argue a direction.
- **A fast physical-AI go/no-go** → either works; both ship a deployment checklist and a
  platform taxonomy.
- **Sanity-checking the main library** → read the Agentic-Workforce take on the same domain
  as a second opinion; disagreements are where the design assumptions live.

## Why keep both

Folding everything into one structure would erase the second opinion. The merge already
pulled the *additive* Agentic-Workforce content into CivStack (missions, command model,
checklists, templates, taxonomy/safety/strategy docs); this folder preserves the **whole
original** as a standing alternative lens — so the library never pretends its taxonomy is
the only possible one.

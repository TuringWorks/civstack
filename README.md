# CivStack

**The operating systems of an economy — staffed by humans, AI agents, and robots.**

CivStack is an open library of **340 agent skills** that maps everything a modern country and economy must reliably do — from governance and energy to farming and eldercare — and assigns each job to the right mix of a human owner, AI personnel, embodied robots, and non-humanoid autonomous machines (self-driving vehicles, farm equipment, drones), with hard accountability boundaries baked in. It is navigable along two axes: by **sector** (the 22 operating systems) and by **strategic mission** (cross-cutting national capabilities like energy abundance or semiconductor sovereignty that compose several sectors).

It turns a strategy document (["Country-Economy Core Jobs To Be Done"](docs/country-economy-core-jtbd.md)) into machine-usable [Agent Skills](https://www.anthropic.com/news/skills): every role ships as a `SKILL.md` an LLM or agent can load to get the full context for *who does what, how, and where a human must stay in charge.*

---

## The idea in one minute

- A **job** is a durable outcome society must reliably produce (e.g. "safe water reaches every household"). It does not change when technology or org charts change.
- A **role** is one way to own, coordinate, or execute that job. Roles are staffed as a **team of four-plus layers**:
  - **Human owner** — accountable for goals, values, exceptions, relationships, and signoff.
  - **AI personnel** — research, draft, analyze, monitor, simulate, coordinate, document.
  - **Robot personnel** — fetch, carry, inspect, clean, assemble, assist, enter hazardous spaces.
  - **Control layer** — permissions, audit logs, escalation thresholds, evaluation.
  - **Public-trust layer** — explainability, appeal, privacy, bias testing, safety certification, labor impact.
- Every job runs the same **seven-step lifecycle**: sense → interpret → decide → mobilize → execute → verify → govern.
- **Accountability stays human.** Each skill names a hard boundary — coercive power, rights-impacting decisions, intimate care, democratic legitimacy, high-consequence safety — that AI and robots may support up to, but never cross.
- **Universal, not US-specific.** The jobs are invariant across nations; *ownership, formality, and capacity* are local variables. Every skill carries a "context modifiers" section so it adapts to any nation — any size, geography, income level, or political system.

## How the robots are assumed to work

CivStack assumes robots are **LLM-brained embodied agents**, not hard-coded automatons:

- A multimodal **LLM brain** perceives, plans, and decomposes tasks. A fleet may share one model or mix specialized ones (a deliberative orchestrator over fast reactive controllers — System 2 over System 1).
- **Physical actions are tool calls.** The brain emits motor primitives (`grasp`, `navigate_to`, `place`, `inspect`) the same way an LLM calls software tools.
- Those tool calls are executed by **Vision-Language-Action (VLA) policies** trained on **world models** (learned physics simulators), **robot gyms** (massively parallel sim-to-real), and **RLAIF** (reinforcement learning from AI feedback).
- A **verified low-level safety layer** can refuse or override any tool call independently of the brain.

The roles that *build and operate* this stack are themselves skills (see `skills/_catalogs/embodied-ai-stack/`).

The **same brain-and-tool-calls model extends to non-humanoid autonomous machines** — self-driving cars, trucks and shuttles, autonomous tractors and harvesters, loaders and earthmovers, mining haul trucks, rail, port/maritime equipment, warehouse robots, and drones. For mobility they add an **Operational Design Domain (ODD)**, the **SAE levels of automation**, a verified minimal-risk safe-stop, and a **teleoperation fallback** (see `skills/_catalogs/autonomous-machines/`, `skills/_catalogs/autonomous-fleet-ops/`, and each sector's `autonomous/` folder).

### Capability is right-sized — RLAIF is one method among many

The "brain" need not be a single large model trained one way. CivStack assumes a **heterogeneous capability stack** and a **spectrum of optimization methods**, each chosen per task:

- **Model tiers:** LLM (deliberation) → SLM (on-device reasoning) → tiny LM / specialized nets (reactive control) → **deterministic controllers** (PID, MPC, state machines, convex/MILP) for hard-real-time, verifiable, safety-critical loops. A capability runs on the *smallest, most deterministic* tier that meets its accuracy, latency, and safety bar; the large model is called only when needed.
- **Optimization methods:** imitation / behavior cloning, model-based & offline RL, **RLHF/RLAIF**, sim-to-real, self-supervised pretraining, supervised fine-tuning, **distillation & compression** (LLM → SLM → tiny LM), search & planning (MCTS, MPC), classical optimization & control, **formal verification**, and evolutionary search.
- **Selection rubric:** exhaustiveness vs efficiency, determinism and verifiability, latency and power, data availability, and consequence — with a verified deterministic safety layer beneath anything learned.

The roles that design and run this spectrum live in `skills/_catalogs/capability-optimization/`. This is a deliberately productizable layer: a **method/model router** that picks the cheapest, safest way to deliver each capability is the commercial core of an embodied-AI platform. A working version ships here:

- **[`docs/capability-routing-matrix.md`](docs/capability-routing-matrix.md)** — the routing matrix: decision inputs, a capability-archetype lookup table, ordered decision rules, and worked examples.
- **[`tools/capability-router.html`](tools/capability-router.html)** — an interactive selector: choose a capability's safety, latency, verifiability, task type, data, compute, and connectivity, and it recommends a model tier, optimization method(s), and a safe fallback with the rationale.

### Guarding against deskilling (job & role simulators)

Automating routine work erodes three things over time: the **human fallback bench** (who runs the system when automation fails), **tacit/craft judgment** (lost as the experienced cohort retires), and the **learning ladder** (juniors never get the cases they used to learn on). Job and role simulators are the primary countermeasure, and CivStack treats them as first-class:

- Every sector skill carries a **Deskilling watch & keep-warm** section — its specific risk, countermeasures, and a simulator regime.
- **OS 22 (Resilience)** owns the standing cross-sector drill and bench-readiness program.
- **[`skills/_catalogs/simulation-training/`](skills/_catalogs/simulation-training/)** holds the roles that run it, and **[`docs/role-simulation-and-keepwarm.md`](docs/role-simulation-and-keepwarm.md)** is the reference.

The key idea: the **world models and simulators built to train the machines double as the keep-warm simulators that keep humans current** — one simulation substrate, two students (the model and the human). The *verified deterministic fallback beneath anything learned* (capability layer) is its technical complement.

---

## What's in the box

| Layer | Count | Where |
|---|---|---|
| Framework & index | 1 | `skills/00-framework/` |
| National operating systems (sector orchestrators) | 22 | `skills/01-…` … `skills/22-…` |
| Strategic missions (cross-cutting national capabilities) | 12 | `skills/strategic-missions/` |
| Human-command roles (accountable owners for missions) | 4 | `skills/_catalogs/human-command/` |
| AI-personnel role skills | 174 | `skills/NN-…/roles/` |
| Embodied robot role skills (sector-nested) | 4 | `skills/05-food/robots/` |
| Autonomous machine skills (sector-nested) | 27 | `skills/<sector>/autonomous/` |
| Cross-cutting role archetypes | 12 | `skills/cross-cutting-archetypes/` |
| AI-personnel catalog patterns | 15 | `skills/_catalogs/ai-personnel/` |
| Humanoid-robot catalog patterns | 10 | `skills/_catalogs/humanoid-robots/` |
| Autonomous-machine catalog patterns | 15 | `skills/_catalogs/autonomous-machines/` |
| Embodied-AI stack roles (build & operate robots + machines) | 10 | `skills/_catalogs/embodied-ai-stack/` |
| Autonomous-fleet operations roles | 17 | `skills/_catalogs/autonomous-fleet-ops/` |
| Capability & optimization roles (model tiers + training methods) | 11 | `skills/_catalogs/capability-optimization/` |
| Simulation & keep-warm roles (anti-deskilling) | 6 | `skills/_catalogs/simulation-training/` |
| **Total `SKILL.md` packages** | **340** | |

Plus non-skill assets: **2 deployment checklists** (`checklists/`), **3 authoring templates** (`templates/`), and reference docs (`docs/`) including the capability routing matrix, the keep-warm/deskilling guide, and the coverage matrix.

### The 22 national operating systems

`01` Governance & Law · `02` Public Finance · `03` Defense & Foreign Affairs · `04` Public Safety & Emergency · `05` Food & Agriculture · `06` Water & Sanitation · `07` Energy & Grid · `08` Mining & Materials · `09` Manufacturing · `10` Shelter & Built Environment · `11` Transportation & Logistics · `12` Communications & Software · `13` Healthcare & Public Health · `14` Education & Human Capital · `15` Science & Innovation · `16` Finance & Markets · `17` Commerce & Hospitality · `18` Media & Civic Life · `19` Environment & Climate · `20` Labor & Workforce · `21` Household & Care · `22` Resilience & Continuity

---

## Repository layout

```
civstack/
├── README.md
├── LICENSE
├── docs/
│   ├── country-economy-core-jtbd.md      # the source strategy map
│   ├── capability-routing-matrix.md      # how to route capabilities to tier + method
│   ├── role-simulation-and-keepwarm.md   # job/role simulators to address deskilling
│   ├── coverage-matrix.md                # request -> where to look in the library
│   ├── non-humanoid-platform-taxonomy.md # which physical form for the job
│   ├── physical-ai-safety-boundaries.md  # safety controls / stop conditions / human-only calls
│   └── frontier-technology-strategy.md   # the thesis behind the strategic missions
├── checklists/                           # deployment-readiness gates
│   ├── ai-robot-role-readiness-checklist.md
│   └── autonomous-machine-deployment-checklist.md
├── templates/                            # blank authoring templates
│   ├── role-card.md
│   ├── ai-agent-brief.md
│   └── robot-role-brief.md
├── skills/
│   ├── 00-framework/SKILL.md             # start here: shared model, command & cadence, index
│   ├── 01-governance/
│   │   ├── SKILL.md                       # sector orchestrator
│   │   └── roles/<role>/SKILL.md          # AI-personnel role skills
│   ├── 05-food/
│   │   ├── SKILL.md
│   │   ├── roles/<role>/SKILL.md
│   │   ├── robots/<robot>/SKILL.md         # LLM-brained humanoid/embodied roles
│   │   └── autonomous/<machine>/SKILL.md   # non-humanoid autonomous machines
│   ├── … (02–22)
│   ├── strategic-missions/<mission>/SKILL.md  # cross-cutting national capabilities
│   ├── cross-cutting-archetypes/<archetype>/SKILL.md
│   └── _catalogs/
│       ├── ai-personnel/<role>/SKILL.md
│       ├── humanoid-robots/<role>/SKILL.md
│       ├── autonomous-machines/<machine>/SKILL.md
│       ├── embodied-ai-stack/<role>/SKILL.md
│       ├── autonomous-fleet-ops/<role>/SKILL.md
│       ├── capability-optimization/<role>/SKILL.md
│       └── simulation-training/<role>/SKILL.md
└── tools/
    ├── generate_skills.py                # regenerates the whole library
    ├── build.sh                          # regenerate master + mirror to the vault
    └── sync-vault.sh                     # mirror skills/ to the Obsidian vault
```

## Anatomy of a skill

Every role `SKILL.md` carries YAML frontmatter (`name`, a "pushy" triggering `description`) plus an extensive body: what the role is, when to trigger it, operating-system context, the seven-step lifecycle, responsibilities, inputs/outputs, **decision rights**, human/AI/robot teaming, a hard **accountability boundary**, tools and interfaces, collaborators, success metrics, **failure modes & safeguards**, **context modifiers for any nation**, **labor-market grounding** (real advertised titles and seniority ladder, the skills/tools/tech employers list, qualifications/certifications/licenses, KPIs from postings, and which job boards carry the role), and a step-by-step operating procedure.

The grounding is calibrated to how each role is actually advertised in 2026 across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards — spot-verified against public listings and O\*NET/BLS. Flagship sectors (communications/software, healthcare, finance, food, governance) additionally carry per-role market mapping (the exact human titles, tools, and certifications each agent supports).

## How to use it

1. **Orient** — read `skills/00-framework/SKILL.md` for the shared model and the index.
2. **Pick a sector** — open the operating-system `SKILL.md` for the domain (e.g. `skills/07-energy/SKILL.md`).
3. **Deploy a role** — load the specific role skill under `roles/` (or a cross-cutting `archetype` / `_catalogs` pattern) into your agent.
4. **Run the lifecycle** and **stop at the human-accountability boundary**, routing the decision to the named human owner.

The skills are tool-agnostic plain Markdown. They work as drop-in context for Claude or any LLM/agent framework, as a design reference for org and automation planning, or as a starting taxonomy you fork and specialize.

## Regenerating / extending

> **`skills/` is generated. Treat it as a build artifact — edit `tools/generate_skills.py`, not individual `SKILL.md` files.** Hand-editing a skill will be overwritten on the next regeneration and makes diffs noisy. All content (sector data, role rosters, the LLM-brained robot architecture, labor-market grounding, and the shared templates) lives in the generator, so a change there propagates consistently to every skill and produces a clean, reviewable `git diff`.

The library is generated so it stays consistent. Edit the data or templates in `tools/generate_skills.py` and run:

```bash
SKILLS_ROOT=./skills python3 tools/generate_skills.py
```

The generator encodes each sector's mission, jobs-to-be-done, role roster, AI personnel, robot roles, accountability boundary, and labor-market grounding, then emits every `SKILL.md` from shared templates. Adding a role, a sector-nested robot, deeper job-description grounding, or a whole new pattern is a few lines of data.

Recommended workflow for a change:

```bash
# 1. edit tools/generate_skills.py
# 2. regenerate
SKILLS_ROOT=./skills python3 tools/generate_skills.py
# 3. review the propagated change, then commit both the generator and skills/
git add -A && git diff --cached --stat
```

## Provenance

Built from the strategy map in [`docs/country-economy-core-jtbd.md`](docs/country-economy-core-jtbd.md), which draws on public occupational and industrial taxonomies (BLS SOC, O\*NET, NAICS), the U.S. CISA critical-infrastructure model, international cross-walks (ILO ISCO-08, UN ISIC), informal-economy research (ILO, World Bank), and AI/robotics-governance frames (NIST AI RMF, OECD.AI). See the source document's notes for the full list.

## License

See [`LICENSE`](LICENSE). Content and code are released for open use and adaptation; please keep attribution and the human-accountability framing intact when you fork.

---

*CivStack is a thinking tool and a design scaffold, not a prescription. It deliberately keeps humans accountable for the decisions that define a society. Fork it, argue with it, and make it fit your context.*

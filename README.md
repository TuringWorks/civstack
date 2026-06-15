# CivStack

**The operating systems of an economy — staffed by humans, AI agents, and robots.**

CivStack is an open library of **248 agent skills** that maps everything a modern country and economy must reliably do — from governance and energy to farming and eldercare — and assigns each job to the right mix of a human owner, AI personnel, and embodied robots, with hard accountability boundaries baked in.

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

---

## What's in the box

| Layer | Count | Where |
|---|---|---|
| Framework & index | 1 | `skills/00-framework/` |
| National operating systems (sector orchestrators) | 22 | `skills/01-…` … `skills/22-…` |
| AI-personnel role skills | 174 | `skills/NN-…/roles/` |
| Embodied robot role skills (sector-nested) | 4 | `skills/05-food/robots/` |
| Cross-cutting role archetypes | 12 | `skills/cross-cutting-archetypes/` |
| AI-personnel catalog patterns | 15 | `skills/_catalogs/ai-personnel/` |
| Humanoid-robot catalog patterns | 10 | `skills/_catalogs/humanoid-robots/` |
| Embodied-AI stack roles (build & operate the robots) | 10 | `skills/_catalogs/embodied-ai-stack/` |
| **Total `SKILL.md` packages** | **248** | |

### The 22 national operating systems

`01` Governance & Law · `02` Public Finance · `03` Defense & Foreign Affairs · `04` Public Safety & Emergency · `05` Food & Agriculture · `06` Water & Sanitation · `07` Energy & Grid · `08` Mining & Materials · `09` Manufacturing · `10` Shelter & Built Environment · `11` Transportation & Logistics · `12` Communications & Software · `13` Healthcare & Public Health · `14` Education & Human Capital · `15` Science & Innovation · `16` Finance & Markets · `17` Commerce & Hospitality · `18` Media & Civic Life · `19` Environment & Climate · `20` Labor & Workforce · `21` Household & Care · `22` Resilience & Continuity

---

## Repository layout

```
civstack/
├── README.md
├── LICENSE
├── docs/
│   └── country-economy-core-jtbd.md      # the source strategy map
├── skills/
│   ├── 00-framework/SKILL.md             # start here: shared model + index
│   ├── 01-governance/
│   │   ├── SKILL.md                       # sector orchestrator
│   │   └── roles/<role>/SKILL.md          # AI-personnel role skills
│   ├── 05-food/
│   │   ├── SKILL.md
│   │   ├── roles/<role>/SKILL.md
│   │   └── robots/<robot>/SKILL.md        # LLM-brained embodied roles
│   ├── … (02–22)
│   ├── cross-cutting-archetypes/<archetype>/SKILL.md
│   └── _catalogs/
│       ├── ai-personnel/<role>/SKILL.md
│       ├── humanoid-robots/<role>/SKILL.md
│       └── embodied-ai-stack/<role>/SKILL.md
└── tools/
    └── generate_skills.py                 # regenerates the whole library
```

## Anatomy of a skill

Every role `SKILL.md` carries YAML frontmatter (`name`, a "pushy" triggering `description`) plus an extensive body: what the role is, when to trigger it, operating-system context, the seven-step lifecycle, responsibilities, inputs/outputs, **decision rights**, human/AI/robot teaming, a hard **accountability boundary**, tools and interfaces, collaborators, success metrics, **failure modes & safeguards**, **context modifiers for any nation**, and a step-by-step operating procedure.

## How to use it

1. **Orient** — read `skills/00-framework/SKILL.md` for the shared model and the index.
2. **Pick a sector** — open the operating-system `SKILL.md` for the domain (e.g. `skills/07-energy/SKILL.md`).
3. **Deploy a role** — load the specific role skill under `roles/` (or a cross-cutting `archetype` / `_catalogs` pattern) into your agent.
4. **Run the lifecycle** and **stop at the human-accountability boundary**, routing the decision to the named human owner.

The skills are tool-agnostic plain Markdown. They work as drop-in context for Claude or any LLM/agent framework, as a design reference for org and automation planning, or as a starting taxonomy you fork and specialize.

## Regenerating / extending

The library is generated, so it stays consistent. Edit the data or templates in `tools/generate_skills.py` and run:

```bash
SKILLS_ROOT=./skills python3 tools/generate_skills.py
```

The generator encodes each sector's mission, jobs-to-be-done, role roster, AI personnel, robot roles, and accountability boundary, then emits every `SKILL.md` from shared templates. Adding a role, a sector-nested robot, or a whole pattern is a few lines of data.

## Provenance

Built from the strategy map in [`docs/country-economy-core-jtbd.md`](docs/country-economy-core-jtbd.md), which draws on public occupational and industrial taxonomies (BLS SOC, O\*NET, NAICS), the U.S. CISA critical-infrastructure model, international cross-walks (ILO ISCO-08, UN ISIC), informal-economy research (ILO, World Bank), and AI/robotics-governance frames (NIST AI RMF, OECD.AI). See the source document's notes for the full list.

## License

See [`LICENSE`](LICENSE). Content and code are released for open use and adaptation; please keep attribution and the human-accountability framing intact when you fork.

---

*CivStack is a thinking tool and a design scaffold, not a prescription. It deliberately keeps humans accountable for the decisions that define a society. Fork it, argue with it, and make it fit your context.*

# Contributing to CivStack

CivStack is a **generated library**. The single most important rule:

> **Never hand-edit files under `skills/`.** They are build artifacts. Edit the data in
> `tools/skills_data.json` (and, for templates, `tools/generate_skills.py`), then regenerate.
> CI rejects any commit where `skills/` doesn't match a clean regeneration.

## The build pipeline

```
tools/skills_data.json   ── data: sectors, roles, robots, machines, profiles, grounding
        │
        ▼
tools/generate_skills.py ── templates + renderers → skills/**/SKILL.md  (433 files)
        │
        ▼
tools/build_site.py      ── skills/ + docs/ → site/  (static browsable site)
```

`tools/extract_data.py` re-dumps the loaded data back to `skills_data.json` (used by CI to
normalize formatting). `tools/verify.py` checks frontmatter and relative links.

## Standard workflow for any change

```bash
# 1. edit tools/skills_data.json (content) or tools/generate_skills.py (templates/renderers)
# 2. regenerate and verify
SKILLS_ROOT=./skills python3 tools/generate_skills.py
python3 tools/verify.py
# 3. rebuild the site
python3 tools/build_site.py
# 4. run tests
python3 -m pytest tests/test_router.py -q
npm test                       # Playwright UI tests for the interactive tools
# 5. review the propagated diff, then commit data + generator + skills/ + site/ together
git add -A && git diff --cached --stat
```

## Where things live in `skills_data.json`

| Key | What it holds |
|---|---|
| `sectors` | The 23 operating systems: mission, JTBD, AI role roster (`ai`), accountability boundary, collaborators |
| `sector_robots` | Sector-nested humanoid robot roles, keyed by sector number: `[name, jtbd, environments, detail]` |
| `sector_robot_profiles` | Per-sector rendering profile for robot skills (human owner, safety limits, adaptation paragraph, …). **Required for any sector that has `sector_robots` entries.** |
| `sector_machines` | Non-humanoid autonomous machines per sector (same 4-tuple shape) |
| `sector_context_lens` | One sector-specific paragraph rendered into every role's "Adapting to any nation" section |
| `sector_failure_modes` | Sector-specific failure-mode bullets appended to every role's generic safeguards |
| `sector_jd` / `role_jd` | Labor-market grounding (advertised titles, tools, certifications, KPIs, job boards) |
| `sector_deskilling` | Per-sector deskilling risk, countermeasures, and simulator regime |
| `archetypes`, `ai_catalog`, `robot_catalog`, `autonomous_machines`, `*_roles`, `strategic_missions` | The cross-cutting and catalog layers |

## Recipes

**Add an AI role to a sector** — append `[role name, what it does, human supervisor]` to that
sector's `ai` list. Optionally add per-role grounding under `role_jd`.

**Add a humanoid robot to a sector** — add a `[name, jtbd, environments, detail]` entry under
`sector_robots["<num>"]`. If the sector has no robots yet, also author a
`sector_robot_profiles["<num>"]` profile (copy an existing one and rewrite every field —
the profile carries the sector's human owner, safety limits, and adaptation story).

**Add a whole sector** — add the sector object, plus entries in `sector_jd`,
`sector_deskilling`, `sector_context_lens`, and `sector_failure_modes` (renderers expect all
four), then update the README counts and the OS list.

**Change wording that appears in every skill** — that's a template change: edit the relevant
`render_*` function or shared constant in `generate_skills.py`.

**After any of the above**: regenerate, and update the counts table in `README.md` if the
total changed (the generator prints the counts).

## Conventions

- Descriptions in frontmatter are deliberately "pushy" triggers — they tell an agent *when to
  load the skill*, not just what it is. Keep that style.
- Every role must name a **human accountability boundary**. Don't add roles that decide
  rights-impacting, coercive, intimate-care, or high-consequence-safety questions autonomously.
- Content is **universal, not US-specific**: ownership, formality, and capacity are local
  variables handled by the context-modifier sections.
- Docs in `docs/` and checklists/templates are hand-written — edit those directly.
- The `perspectives/` tree is a preserved alternative viewpoint: don't regenerate or
  restructure it.

## Pull requests

Keep data changes and template changes in separate commits where possible — data diffs are
reviewed for content, template diffs for blast radius. CI runs `verify.py`, the
extract/regenerate/diff check, pytest, and the Playwright UI tests.

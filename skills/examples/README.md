# skills/examples — numbered worked examples

Five self-contained, **offline** scripts (no API key, no dependencies) that operate over
the generated skill library. Run them from the repo root:

```bash
python3 skills/examples/01_search_skills.py "autonomous farm equipment drones food safety" --limit 5
python3 skills/examples/02_build_agent_context_pack.py \
    --scenario "Deploy autonomous tractors and drones for national food security" \
    --out /tmp/jtbd-agent-context-pack.md
python3 skills/examples/03_autonomous_farm_deployment.py
python3 skills/examples/04_readiness_scorecard.py --scenario "Scale autonomous harvesters across 200 farms"
python3 skills/examples/05_library_report.py
python3 -m py_compile skills/examples/*.py
```

| Script | What it does |
|---|---|
| `01_search_skills.py` | Keyword search over all 360 skills; ranks and prints the top matches with category + description. |
| `02_build_agent_context_pack.py` | Selects the most relevant skills for a scenario and writes a single Markdown **context pack** (operating systems, missions, roles, machines, owners, boundaries, command & cadence model) to `--out`. |
| `03_autonomous_farm_deployment.py` | A fully worked deployment brief for autonomous farming, assembled from the actual skills — machines, AI roles, fleet-ops, capability routing, the deployment gate, the deskilling regime, and the accountability boundary. |
| `04_readiness_scorecard.py` | Scores library readiness for a scenario across 8 dimensions (skills found, OS identified, owners named, boundaries defined, capability routing, deployment checklist, deskilling regime) and prints an overall %. |
| `05_library_report.py` | Whole-library report: counts by category, per-OS role/machine/robot coverage, missions, and a health check (frontmatter + internal links). |

`_civlib.py` is the shared helper (indexing, search, section/owner/boundary extraction).

> These are the **plain-data** examples. For **runnable agents** that call Claude with a
> skill as context (router, human-gated adjudication, capability architect, fleet safety
> gate, end-to-end pipeline, and a `civstack` CLI), see [`../../examples/`](../../examples/).

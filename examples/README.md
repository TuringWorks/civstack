# Example agents

Runnable agents that use the CivStack skills. Each loads a `SKILL.md`, wraps it in the
command & cadence operating contract, re-asserts the skill's human-accountability
boundary as a hard rule, and runs a task.

**Zero-dependency `--dry-run`** prints the exact assembled system prompt (and, for the
deterministic agents, the full result) without an API key. For live LLM calls:

```bash
pip install anthropic
export ANTHROPIC_API_KEY=sk-...
export CIVSTACK_MODEL=claude-sonnet-4-6   # optional; this is the default
```

## The shared harness

`civstack_agent.py` — `CivStackAgent.from_skill("<path under skills/>")` builds an agent
from any of the 360 skills. It injects the operating contract (sense→…→govern, delegate
rules, escalate triggers) and the skill's own accountability boundary, then runs a task
(`dry_run=True` to preview the prompt).

```bash
python examples/civstack_agent.py 12-communications/roles/coding-agent "add a retry to fetch()" --dry-run
```

## The four examples

| Script | What it shows | Runs offline? |
|---|---|---|
| `skill_router.py` | Routes a free-text request to the best skill across all 360 (sector role, mission, catalog, or archetype), then optionally runs it. | Yes (keyword routing; live mode uses Claude to choose) |
| `benefits_adjudication.py` | A governance agent that prepares a case file and recommendation but is **structurally blocked** from issuing a denial — a post-run guard force-escalates if it ever does. | Yes (dry-run shows the prompt; guard logic runs always) |
| `capability_architect.py` | Turns a capability's constraints into a model tier + optimization method + fallback, using the routing-matrix rules ported to Python. | Yes (fully deterministic; `--llm` for a skill-grounded narrative) |
| `fleet_safety_gate.py` | Runs the autonomous-machine deployment checklist as a hard GO / NO-GO gate; refuses deployment until every critical gate passes. | Yes (fully deterministic; `--llm` for a safety-case review) |
| `end_to_end_pipeline.py` | Chains it all: **request → route → run role agent → human gate → escalation packet** (a clean handoff to the named accountable human). | Yes (dry-run) |
| `civstack_cli.py` | A tiny `civstack` CLI over the whole library: `list`, `route`, `run`, `pipeline`, `capability`, `gate`. | Yes |

### Try them

```bash
cd examples

# Router: where should this request go?
python skill_router.py "a farmer needs to plan spraying without GPS" --dry-run
python skill_router.py "review this vendor contract for risk" --run --dry-run

# Benefits adjudication with the human gate
python benefits_adjudication.py --dry-run

# Capability routing (no API key needed)
python capability_architect.py --safety high --latency hrt --task control --data sim --compute edge
python capability_architect.py --llm "pick ripe strawberries without bruising" --dry-run

# Fleet safety gate
python fleet_safety_gate.py            # sample machine -> NO-GO (two gates fail)
python fleet_safety_gate.py --all-pass # -> GO

# End-to-end pipeline: route -> run -> human gate -> escalation packet
python end_to_end_pipeline.py "deploy an autonomous tractor on a smallholder field" --dry-run
```

## The `civstack` CLI

`civstack_cli.py` wraps the whole library in one command:

```bash
python civstack_cli.py list identity
python civstack_cli.py route "review a vendor contract for risk" --dry-run
python civstack_cli.py run 12-communications/roles/coding-agent "add a retry to fetch()" --dry-run
python civstack_cli.py pipeline "applicant with mismatched address, housing aid" --dry-run
python civstack_cli.py capability --safety high --latency hrt --task control --data sim --compute edge
python civstack_cli.py gate --all-pass
```

Install it as a real command (optional):

```bash
chmod +x examples/civstack_cli.py
ln -s "$(pwd)/examples/civstack_cli.py" /usr/local/bin/civstack
civstack list
```

## The pattern these demonstrate

Every agent is the same shape: **a skill (the role's context) + the operating contract
(how delegation runs) + a hard accountability boundary (what stays human) + a task.**
The deterministic examples (`capability_architect`, `fleet_safety_gate`) show that much
of the value is enforceable in plain code; the LLM modes show the skill grounding the
model's judgment. Swap the skill path to build an agent for any of the 360 roles.

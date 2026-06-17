#!/usr/bin/env python3
"""
CivStack skill router / orchestrator.

Reads every SKILL.md's frontmatter (name + description), routes a free-text request
to the best-matching skill(s), and optionally runs the top match as an agent.

Shows the two-axis navigation: it can land on a sector role, a strategic mission,
a catalog pattern, or a cross-cutting archetype.

  python examples/skill_router.py "a farmer needs to plan spraying without GPS" --dry-run
  python examples/skill_router.py "review this vendor contract for risk" --run --dry-run
"""
import os
import re
import sys

from civstack_agent import CivStackAgent, SKILLS_DIR, _parse_skill

STOP = set("the a an of for and or to in on with without by is are be this that your you "
           "need needs help review check run plan make build using use it its as at from".split())


def load_index():
    idx = []
    for dp, _, fs in os.walk(SKILLS_DIR):
        if "SKILL.md" in fs:
            with open(os.path.join(dp, "SKILL.md")) as f:
                fm, _ = _parse_skill(f.read())
            rel = os.path.relpath(os.path.join(dp, "SKILL.md"), SKILLS_DIR)
            idx.append({"name": fm.get("name", rel), "desc": fm.get("description", ""),
                        "rel": os.path.dirname(rel) or rel})
    return idx


def _tokens(s):
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 2}


def rank(request, idx, top=5):
    q = _tokens(request)
    scored = []
    for e in idx:
        score = len(q & _tokens(e["name"] + " " + e["desc"]))
        if score:
            scored.append((score, e))
    scored.sort(key=lambda x: -x[0])
    return scored[:top]


def llm_route(request, idx, model=None):
    """Ask Claude to pick the single best skill path from the index."""
    import anthropic
    catalog = "\n".join("- %s :: %s" % (e["rel"], e["desc"][:160]) for e in idx)
    client = anthropic.Anthropic()
    sysp = ("You are a router for the CivStack skill library. Given a request and a catalog "
            "of skills (path :: description), reply with ONLY the single best skill path, "
            "exactly as written in the catalog. No prose.")
    resp = client.messages.create(
        model=model or os.environ.get("CIVSTACK_MODEL", "claude-sonnet-4-6"),
        max_tokens=60, system=sysp,
        messages=[{"role": "user", "content": "REQUEST: %s\n\nCATALOG:\n%s" % (request, catalog)}])
    return resp.content[0].text.strip()


def main():
    dry = "--dry-run" in sys.argv
    run = "--run" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print('usage: skill_router.py "request" [--run] [--dry-run]')
        sys.exit(1)
    request = args[0]
    idx = load_index()
    print("Loaded %d skills.\n" % len(idx))

    if dry:
        print("Top matches (keyword routing; live mode uses Claude to choose):")
        for score, e in rank(request, idx):
            print("  [%d] %-52s %s" % (score, e["rel"], e["desc"][:80]))
        top = rank(request, idx)
        chosen = top[0][1]["rel"] if top else None
    else:
        chosen = llm_route(request, idx)
        print("Router chose: %s" % chosen)

    if chosen and run:
        print("\n--- running chosen skill as an agent ---\n")
        agent = CivStackAgent.from_skill(chosen)
        print(agent.run(request, dry_run=dry))
    elif chosen:
        print("\n(add --run to execute the chosen skill; e.g. it would load %s)" % chosen)


if __name__ == "__main__":
    main()

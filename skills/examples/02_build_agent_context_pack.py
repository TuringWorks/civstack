#!/usr/bin/env python3
"""
02 — Build an agent context pack for a scenario.

Selects the most relevant skills across the library and assembles a single Markdown
"context pack": the operating systems and missions involved, the role/machine skills to
deploy, their human owners and accountability boundaries, and the shared command &
cadence model — everything an agent (or a person) needs to act on the scenario.

  python3 skills/examples/02_build_agent_context_pack.py \\
      --scenario "Deploy autonomous tractors and drones for national food security" \\
      --out /tmp/jtbd-agent-context-pack.md
"""
import os
import sys

import _civlib as cl


def arg(flag, default=None):
    a = sys.argv
    return a[a.index(flag) + 1] if flag in a and a.index(flag) + 1 < len(a) else default


def pick(hits, category_prefix, n):
    return [e for _, e in hits if e["category"].startswith(category_prefix)][:n]


def main():
    scenario = arg("--scenario")
    out = arg("--out", "/tmp/civstack-context-pack.md")
    if not scenario:
        print('usage: 02_build_agent_context_pack.py --scenario "..." --out FILE')
        sys.exit(1)

    idx = cl.load_index()
    hits = cl.search(scenario, idx, limit=40)

    oss = pick(hits, "operating system", 4)
    missions = pick(hits, "strategic mission", 3)
    roles = pick(hits, "sector role", 8)
    machines = pick(hits, "sector machine", 6)
    catalogs = pick(hits, "catalog", 6)

    L = []
    L.append("# CivStack Agent Context Pack\n")
    L.append("**Scenario:** %s\n" % scenario)
    L.append("Assembled from the CivStack library (%d skills). Use the skills below as context "
             "for the agents that will act on this scenario.\n" % len(idx))

    def block(title, items, withboundary=False):
        if not items:
            return
        L.append("\n## %s\n" % title)
        for e in items:
            L.append("- **%s** — `skills/%s/SKILL.md`" % (e["name"], e["rel"]))
            L.append("  - %s" % e["desc"][:160])
            if withboundary:
                sup = cl.supervisor_of(e)
                bnd = cl.boundary_of(e)
                if sup:
                    L.append("  - Human owner: %s" % sup)
                if bnd:
                    L.append("  - Accountability boundary: %s" % bnd[:160])

    block("Operating systems involved", oss)
    block("Strategic missions involved", missions)
    block("AI-personnel roles to deploy", roles, withboundary=True)
    block("Autonomous machines involved", machines, withboundary=True)
    block("Cross-cutting / catalog skills", catalogs)

    # Shared command & cadence model from the framework.
    fw = next((e for e in idx if e["category"] == "framework"), None)
    if fw:
        cad = cl.extract_section(fw["body"], "The command & cadence model (how delegation actually runs)")
        if cad:
            L.append("\n## Command & cadence model (shared)\n")
            L.append(cad[:1400] + ("…" if len(cad) > 1400 else ""))

    L.append("\n## How to use this pack\n")
    L.append("1. A human owner sets the objective, constraints, success criteria, and risk tier.")
    L.append("2. Load the role/machine skills above as agent context.")
    L.append("3. Run the seven-step loop (sense→…→govern) and stop at each accountability boundary.")
    L.append("4. For physical deployment, clear the gates in `checklists/` first.")

    text = "\n".join(L) + "\n"
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with open(out, "w") as f:
        f.write(text)
    print("Wrote context pack -> %s (%d lines)" % (out, text.count(chr(10))))
    print("Selected: %d operating systems, %d missions, %d roles, %d machines, %d catalog skills."
          % (len(oss), len(missions), len(roles), len(machines), len(catalogs)))


if __name__ == "__main__":
    main()

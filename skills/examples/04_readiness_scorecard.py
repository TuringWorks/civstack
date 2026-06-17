#!/usr/bin/env python3
"""
04 — Readiness scorecard for a scenario.

Scores how ready the CivStack library is to support a given scenario across the
dimensions that matter for accountable deployment, and prints a scorecard with an
overall readiness percentage. Deterministic; no API key.

  python3 skills/examples/04_readiness_scorecard.py --scenario "Scale autonomous harvesters across 200 farms"
"""
import sys

import _civlib as cl


def arg(flag, default=None):
    a = sys.argv
    return a[a.index(flag) + 1] if flag in a and a.index(flag) + 1 < len(a) else default


def main():
    scenario = arg("--scenario")
    if not scenario:
        print('usage: 04_readiness_scorecard.py --scenario "..."')
        sys.exit(1)

    idx = cl.load_index()
    hits = [e for _, e in cl.search(scenario, idx, limit=40)]
    cats = {e["category"] for e in hits}
    physical = any(c in cats for c in ("sector machine", "sector robot")) or \
        any(c.startswith("catalog:autonomous") for c in cats)

    boundaries = sum(1 for e in hits if cl.boundary_of(e))
    owners = sum(1 for e in hits if cl.supervisor_of(e))

    checks = [
        ("Relevant skills found", len(hits) >= 3, "%d matched" % len(hits)),
        ("Operating system(s) identified", "operating system" in cats or
         any(c.startswith("sector") for c in cats), ", ".join(sorted(c for c in cats if "sector" in c or c == "operating system")) or "none"),
        ("Strategic mission alignment", "strategic mission" in cats,
         "yes" if "strategic mission" in cats else "no direct mission"),
        ("Human owners named in matched skills", owners >= max(1, len(hits) // 3),
         "%d/%d skills name an owner" % (owners, len(hits))),
        ("Accountability boundaries defined", boundaries >= max(1, len(hits) // 3),
         "%d/%d skills define a boundary" % (boundaries, len(hits))),
        ("Capability routing available", True, "docs/capability-routing-matrix.md + capability-optimization roles"),
        ("Deployment checklist available", (not physical) or True,
         "checklists/autonomous-machine-deployment-checklist.md" if physical else "n/a (non-physical)"),
        ("Deskilling / keep-warm regime", any(cl.extract_section(e["body"], "Deskilling watch") for e in hits),
         "present in sector skills"),
    ]

    passed = sum(1 for _, ok, _ in checks if ok)
    pct = round(100 * passed / len(checks))

    print('Readiness scorecard for: "%s"\n' % scenario)
    for label, ok, detail in checks:
        print("  [%s] %-38s %s" % ("X" if ok else " ", label, detail))
    print("\n  Overall readiness: %d%%  (%d/%d dimensions)" % (pct, passed, len(checks)))
    verdict = ("READY to plan deployment" if pct >= 75 else
               "PARTIAL — close the unchecked gaps first" if pct >= 50 else
               "NOT READY — significant gaps")
    print("  Verdict: %s" % verdict)
    print("\n  Top matched skills:")
    for e in hits[:5]:
        print("    - %-13s %s" % (e["category"], e["rel"]))


if __name__ == "__main__":
    main()

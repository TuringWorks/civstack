#!/usr/bin/env python3
"""
05 — Library report.

Prints a structured report over the whole CivStack library: totals by category,
coverage stats, the operating systems and strategic missions, and a health check
(frontmatter + internal links). Deterministic; no API key.

  python3 skills/examples/05_library_report.py
"""
import os
import re
from collections import Counter

import _civlib as cl


def main():
    idx = cl.load_index()
    cats = Counter(e["category"] for e in idx)

    print("=" * 66)
    print("CIVSTACK LIBRARY REPORT")
    print("=" * 66)
    print("Total skills: %d\n" % len(idx))

    print("By category:")
    for c, n in sorted(cats.items(), key=lambda x: (-x[1], x[0])):
        print("  %-22s %3d" % (c, n))

    # Operating systems.
    oss = [e for e in idx if e["category"] == "operating system"]
    print("\nOperating systems (%d):" % len(oss))
    for e in sorted(oss, key=lambda x: x["rel"]):
        nrole = sum(1 for x in idx if x["rel"].startswith(e["rel"] + "/roles/"))
        nmach = sum(1 for x in idx if x["rel"].startswith(e["rel"] + "/autonomous/"))
        nrobo = sum(1 for x in idx if x["rel"].startswith(e["rel"] + "/robots/"))
        print("  %-44s roles:%-2d machines:%-2d robots:%d" % (e["rel"], nrole, nmach, nrobo))

    missions = [e for e in idx if e["category"] == "strategic mission"]
    print("\nStrategic missions (%d): %s" % (len(missions),
          ", ".join(sorted(m["rel"].split("/")[-1] for m in missions))))

    # Coverage stats.
    sec_with_mach = len({e["rel"].split("/")[0] for e in idx if e["category"] == "sector machine"})
    sec_with_robo = len({e["rel"].split("/")[0] for e in idx if e["category"] == "sector robot"})
    print("\nCoverage:")
    print("  sectors with nested machines: %d / %d" % (sec_with_mach, len(oss)))
    print("  sectors with nested robots:   %d / %d" % (sec_with_robo, len(oss)))

    # Health check (frontmatter quoted + internal links resolve).
    link_re = re.compile(r"\]\((\.\.?/[^)#]+)\)")
    fm_bad = links = link_bad = 0
    for e in idx:
        text = open(e["path"]).read()
        if not re.search(r'^name:\s+".*"$', text, re.M) or not re.search(r'^description:\s+".*"$', text, re.M):
            fm_bad += 1
        for m in link_re.finditer(text):
            links += 1
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(e["path"]), m.group(1)))):
                link_bad += 1
    print("\nHealth:")
    print("  frontmatter errors: %d" % fm_bad)
    print("  internal links:     %d checked, %d broken" % (links, link_bad))
    print("\nStatus: %s" % ("OK — library is consistent" if (fm_bad == 0 and link_bad == 0)
                            else "ISSUES FOUND (see above)"))


if __name__ == "__main__":
    main()

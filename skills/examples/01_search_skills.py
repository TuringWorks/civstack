#!/usr/bin/env python3
"""
01 — Search the CivStack skill library.

  python3 skills/examples/01_search_skills.py "autonomous farm equipment drones food safety" --limit 5
"""
import sys

import _civlib as cl


def main():
    argv = sys.argv[1:]
    limit = 10
    if "--limit" in argv:
        i = argv.index("--limit")
        limit = int(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    query = " ".join(a for a in argv if not a.startswith("--"))
    if not query:
        print('usage: 01_search_skills.py "query terms" [--limit N]')
        sys.exit(1)

    idx = cl.load_index()
    hits = cl.search(query, idx, limit=limit)
    print('Query: "%s"   (%d skills indexed)\n' % (query, len(idx)))
    if not hits:
        print("No matches.")
        return
    for score, e in hits:
        print("[%d]  %-14s  %s" % (score, e["category"], e["rel"]))
        print("       %s\n" % e["desc"][:140])


if __name__ == "__main__":
    main()

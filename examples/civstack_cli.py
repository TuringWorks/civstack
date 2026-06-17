#!/usr/bin/env python3
"""
civstack — a tiny CLI over the CivStack skill library.

  civstack list [substr]                  list skills (optionally filtered)
  civstack route "request" [--run] [--dry-run]
  civstack run <skill-path> "task" [--dry-run]
  civstack pipeline "request" [--dry-run]
  civstack capability [--safety .. --latency .. ...]
  civstack gate [--all-pass] [--llm]

Examples:
  civstack list identity
  civstack route "review a vendor contract for risk" --dry-run
  civstack run 12-communications/roles/coding-agent "add a retry to fetch()" --dry-run
  civstack pipeline "deploy an autonomous tractor on a smallholder field" --dry-run
  civstack capability --safety high --latency hrt --task control --data sim --compute edge

Install as a command (optional):
  ln -s "$(pwd)/examples/civstack_cli.py" /usr/local/bin/civstack && chmod +x examples/civstack_cli.py
"""
import os
import sys
import runpy

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from civstack_agent import CivStackAgent  # noqa: E402
from skill_router import load_index, rank, llm_route  # noqa: E402


def _run_script(name):
    """Delegate to one of the standalone example scripts, preserving argv."""
    runpy.run_path(os.path.join(HERE, name), run_name="__main__")


def cmd_list(argv):
    substr = next((a for a in argv if not a.startswith("--")), "")
    idx = load_index()
    rows = [e for e in idx if substr.lower() in (e["rel"] + " " + e["desc"]).lower()]
    for e in sorted(rows, key=lambda x: x["rel"]):
        print("%-58s %s" % (e["rel"], e["desc"][:70]))
    print("\n%d / %d skills%s" % (len(rows), len(idx), (" matching %r" % substr) if substr else ""))


def cmd_route(argv):
    dry = "--dry-run" in argv
    run = "--run" in argv
    req = next((a for a in argv if not a.startswith("--")), None)
    if not req:
        print('usage: civstack route "request" [--run] [--dry-run]'); return
    idx = load_index()
    chosen = (rank(req, idx)[0][1]["rel"] if (dry and rank(req, idx)) else
              None if dry else llm_route(req, idx))
    if dry:
        for score, e in rank(req, idx):
            print("[%d] %-54s %s" % (score, e["rel"], e["desc"][:60]))
    else:
        print("chosen: %s" % chosen)
    if run and chosen:
        print("\n--- running %s ---\n" % chosen)
        print(CivStackAgent.from_skill(chosen).run(req, dry_run=dry))


def cmd_run(argv):
    pos = [a for a in argv if not a.startswith("--")]
    dry = "--dry-run" in argv
    if len(pos) < 2:
        print('usage: civstack run <skill-path> "task" [--dry-run]'); return
    print(CivStackAgent.from_skill(pos[0]).run(pos[1], dry_run=dry))


def main():
    if len(sys.argv) < 2:
        print(__doc__); return
    cmd, rest = sys.argv[1], sys.argv[2:]
    if cmd == "list":
        cmd_list(rest)
    elif cmd == "route":
        cmd_route(rest)
    elif cmd == "run":
        cmd_run(rest)
    elif cmd == "pipeline":
        sys.argv = [sys.argv[0]] + rest
        _run_script("end_to_end_pipeline.py")
    elif cmd == "capability":
        sys.argv = [sys.argv[0]] + rest
        _run_script("capability_architect.py")
    elif cmd == "gate":
        sys.argv = [sys.argv[0]] + rest
        _run_script("fleet_safety_gate.py")
    else:
        print("unknown command: %s\n" % cmd)
        print(__doc__)


if __name__ == "__main__":
    main()

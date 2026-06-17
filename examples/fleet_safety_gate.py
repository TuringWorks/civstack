#!/usr/bin/env python3
"""
Example agent: Autonomous-fleet safety gate.

Runs the autonomous-machine deployment checklist (checklists/autonomous-machine-
deployment-checklist.md) as a hard GO / NO-GO gate. Deployment is refused until every
critical gate passes. Works with NO API key; add --llm for a skill-grounded safety-case
review by the ODD & safety-case engineer skill.

  python examples/fleet_safety_gate.py            # sample machine with gaps -> NO-GO
  python examples/fleet_safety_gate.py --all-pass # everything satisfied   -> GO
  python examples/fleet_safety_gate.py --llm --dry-run
"""
import sys

from civstack_agent import CivStackAgent

SKILL = "_catalogs/autonomous-fleet-ops/operational-design-domain-odd-safety-case-engineer"

# Critical gates from the deployment checklist (a NO on any is a hard NO-GO).
GATES = [
    ("human_owner_named", "Human accountable owner is named"),
    ("odd_approved", "Operating Design Domain (geofence/route/weather/speed) approved"),
    ("sensors_calibrated", "Sensors calibrated and localization validated"),
    ("estop_tested", "Emergency stop tested"),
    ("safe_stop_tested", "Safe-stop / minimal-risk-maneuver behavior tested"),
    ("teleop_tested", "Remote intervention (teleop) tested"),
    ("comms_linkloss", "Comms tested and link-loss behavior verified"),
    ("cyber_active", "Cybersecurity controls active"),
    ("exclusion_zones", "Exclusion zones marked and human/animal detection working"),
    ("override_confirmed", "Human override and stop authority confirmed working"),
]

# A sample machine being proposed for deployment (some gates not yet met).
SAMPLE = {
    "machine": "Autonomous tractor, smallholder field, intermittent connectivity",
    "human_owner_named": True,
    "odd_approved": True,
    "sensors_calibrated": True,
    "estop_tested": True,
    "safe_stop_tested": False,      # <-- not yet tested
    "teleop_tested": True,
    "comms_linkloss": False,        # <-- link-loss behavior unverified
    "cyber_active": True,
    "exclusion_zones": True,
    "override_confirmed": True,
}


def run_gate(machine):
    failures = [label for key, label in GATES if not machine.get(key)]
    decision = "GO" if not failures else "NO-GO"
    return decision, failures


def main():
    argv = sys.argv[1:]
    machine = dict(SAMPLE)
    if "--all-pass" in argv:
        for key, _ in GATES:
            machine[key] = True

    if "--llm" in argv:
        dry = "--dry-run" in argv
        agent = CivStackAgent.from_skill(SKILL)
        task = ("Review this autonomous-machine deployment request against the deployment checklist "
                "and the ODD/safety case. State GO or NO-GO and justify; if NO-GO, list the exact gates "
                "that must pass first. Request:\n" + str(machine))
        print(agent.run(task, dry_run=dry, max_tokens=1000))
        return

    print("Deployment request: %s\n" % machine["machine"])
    decision, failures = run_gate(machine)
    for key, label in GATES:
        print("  [%s] %s" % ("PASS" if machine.get(key) else "FAIL", label))
    print("\nDECISION: %s" % decision)
    if failures:
        print("Deployment REFUSED until these gates pass:")
        for f in failures:
            print("  - " + f)
        print("\nAccountability: the safety officer (human) owns the safety case; the gate cannot be "
              "overridden by the autonomy brain.")
        sys.exit(2)
    print("All critical gates passed. Safety officer sign-off still required before live operation.")


if __name__ == "__main__":
    main()

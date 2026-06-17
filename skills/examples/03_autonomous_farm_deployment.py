#!/usr/bin/env python3
"""
03 — Worked example: autonomous farm deployment.

A concrete, end-to-end orchestration for "deploy autonomous tractors, harvesters, and
drones for national food security" — assembled entirely from CivStack skills:
operating system 05, its machines and AI roles, the fleet-ops + capability layers, the
deployment checklist, and the deskilling/keep-warm regime. Deterministic; no API key.

  python3 skills/examples/03_autonomous_farm_deployment.py
"""
import os

import _civlib as cl

PLAN = [
    ("Operating system", ["05-food"]),
    ("Autonomous machines", ["05-food/autonomous/autonomous-tractor",
                             "05-food/autonomous/autonomous-harvester-combine",
                             "05-food/autonomous/crop-scouting-drone",
                             "05-food/autonomous/spraying-seeding-drone"]),
    ("AI personnel (plan & direct)", ["05-food/roles/autonomous-farm-operations-agent",
                                      "05-food/roles/autonomous-machinery-dispatch-agent",
                                      "05-food/roles/crop-planning-agent"]),
    ("Fleet operations & safety", ["_catalogs/autonomous-fleet-ops/farm-autonomy-manager",
                                   "_catalogs/autonomous-fleet-ops/operational-design-domain-odd-safety-case-engineer",
                                   "_catalogs/autonomous-fleet-ops/remote-operations-center-teleoperations-supervisor"]),
    ("How it's built", ["_catalogs/capability-optimization/capability-method-architect"]),
]


def load(rel):
    path = os.path.join(cl.SKILLS_DIR, rel, "SKILL.md")
    if not os.path.exists(path):
        return None
    fm, body = cl.parse_frontmatter(open(path).read())
    return {"name": fm.get("name", rel), "desc": fm.get("description", ""), "rel": rel, "body": body}


def main():
    print("=" * 74)
    print("AUTONOMOUS FARM DEPLOYMENT  —  assembled from CivStack skills")
    print("Scenario: deploy autonomous tractors, harvesters, and drones for food security")
    print("=" * 74)

    for title, rels in PLAN:
        print("\n## %s" % title)
        for rel in rels:
            e = load(rel)
            if not e:
                print("  (missing) %s" % rel)
                continue
            print("  - %s  [skills/%s]" % (e["name"], rel))
            sup = cl.supervisor_of(e)
            if sup:
                print("      owner/escalates-to: %s" % sup)

    # Capability routing for the field-control capability (offline rule of thumb).
    print("\n## Capability routing (field guidance + control)")
    print("  inputs: safety=medium, latency=hard-real-time, task=control, data=sim, "
          "compute=edge, connectivity=intermittent")
    print("  -> tier:    Deterministic guidance (GPS/RTK + MPC) + tiny perception net, in-loop")
    print("  -> methods: imitation + sim-to-real; distill to on-device; (no cloud model in the loop)")
    print("  -> fallback: on-device safe-stop; teleop where reachable; human owner accountable")
    print("  (see docs/capability-routing-matrix.md)")

    # Deployment gate.
    print("\n## Deployment gate (checklists/autonomous-machine-deployment-checklist.md)")
    for g in ["ODD/geofence approved", "Sensors calibrated + localization validated",
              "Emergency stop + safe-stop tested", "Teleop + link-loss behavior verified",
              "Exclusion zones + human/animal detection", "Cyber controls active",
              "Human override & stop authority confirmed"]:
        print("  [ ] %s" % g)
    print("  GO only when every gate passes; the farm-autonomy manager owns the safety case.")

    # Deskilling / keep-warm.
    food = load("05-food")
    if food:
        dk = cl.extract_section(food["body"], "Deskilling watch & keep-warm regime")
        if dk:
            print("\n## Deskilling watch & keep-warm")
            for line in dk.splitlines()[:6]:
                if line.strip():
                    print("  " + line.strip())

    print("\n## Human accountability boundary")
    if food:
        b = cl.extract_section(food["body"], "Human accountability boundary").split("\n")[0]
        print("  " + b)
    print("\nDone. This brief is fully traceable to the skills above.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Example agent: Capability & method architect (capability-optimization layer).

Turns a capability's constraints into a recommended model tier + optimization method(s)
+ safe fallback, using the same decision rules as docs/capability-routing-matrix.md and
tools/capability-router.html — ported to Python so it runs with NO API key.

  python examples/capability_architect.py \\
      --safety high --latency hrt --task control --data sim --compute edge --conn intermittent
  python examples/capability_architect.py --llm "pick ripe strawberries without bruising"   # skill-grounded narrative

Flags (all optional; sensible defaults):
  --safety  low|med|high       --latency relaxed|rt|hrt    --verify nice|req
  --task    control|optimize|reason   --data demos|logs|sim|none
  --compute ample|edge|tiny    --conn reliable|intermittent|none
"""
import sys

from civstack_agent import CivStackAgent

DEFAULTS = dict(safety="med", latency="rt", verify="nice", task="control",
                data="demos", compute="edge", conn="reliable")
SKILL = "_catalogs/capability-optimization/capability-method-architect"


def recommend(s):
    why, methods = [], []
    if s["safety"] == "high" and s["latency"] == "hrt":
        tier = "Deterministic controller (PID/MPC) in a verified envelope — learned models advisory only"
        why.append("Safety-critical + hard-real-time -> deterministic + formal verification; nothing learned in the irreversible loop.")
    elif s["latency"] == "hrt":
        tier = "Deterministic controller or distilled tiny LM, in-loop — no cloud/large model in the loop"
        why.append("Hard-real-time loop -> keep it deterministic/tiny; the brain sets goals, the loop executes.")
    elif s["task"] == "optimize":
        tier = "Deterministic solver (MILP/convex/search) — learned heuristics only to warm-start"
        why.append("Optimization/scheduling -> exact solvers give provable answers.")
    elif s["task"] == "reason":
        if s["compute"] == "tiny" or s["conn"] == "none":
            tier = "Distilled SLM / tiny LM on-device, with a deterministic fallback"
            why.append("Open-ended reasoning but tiny/offline -> distilled on-device model; no cloud dependency.")
        elif s["compute"] == "edge":
            tier = "SLM on-device, cascading to an LLM for the long tail"
            why.append("Open-ended reasoning on an edge budget -> SLM on-device, escalate hard cases to an LLM.")
        else:
            tier = "LLM (cloud / high-end edge), cascading down for routine cases"
            why.append("Open-ended reasoning + ample compute -> LLM, cascade to smaller tiers for routine work.")
    else:
        tier = ("Tiny LM / specialized net (distilled), in-loop" if s["compute"] == "tiny"
                else "SLM / VLA policy on-device")
        why.append("Structured perception/control -> smallest learned tier that hits accuracy.")
    if s["verify"] == "req":
        tier += " | wrapped with formal verification + runtime monitors"
        why.append("Verifiability required -> add formal methods / runtime monitors.")

    if s["data"] == "demos":
        methods += ["Imitation / behavior cloning (BC, DAgger)", "Offline RL refinement"]
        why.append("Demonstrations -> imitation first (data-efficient), then offline RL.")
    elif s["data"] == "sim":
        methods += ["Sim-to-real (domain randomization)", "Model-based RL"]
        why.append("Simulator -> train in sim and transfer; avoids risky on-hardware exploration.")
    elif s["data"] == "logs":
        methods += ["Offline RL", "Supervised fine-tuning"]
        why.append("Logged data -> offline RL + supervised fine-tuning.")
    else:
        methods += ["Self-supervised pretraining", "Build demos/simulator", "Deterministic baseline meanwhile"]
        why.append("Little/no data -> self-supervised pretraining + start a data engine; ship a deterministic baseline now.")
    if s["task"] == "reason":
        methods.append("SFT + RLHF/RLAIF")
        why.append("Language/preference behavior -> SFT then RLHF/RLAIF (one option among reward methods).")
    if s["task"] == "optimize":
        methods.insert(0, "Classical optimization (exact)")
    if s["compute"] in ("edge", "tiny"):
        methods.append("Distillation -> SLM/tiny + quantization")
        why.append(("Tiny embedded" if s["compute"] == "tiny" else "Edge-constrained") +
                    " budget -> distill large->small and compress to fit.")

    if s["safety"] == "high":
        fallback = ("Verified safe-stop / minimal-risk maneuver the safety layer can trigger independently "
                    "of the brain; teleop handoff; a human is accountable for the decision.")
    elif s["conn"] != "reliable":
        fallback = "On-device fallback + safe-stop; do not depend on a cloud model or teleoperation."
    else:
        fallback = "Human review on low confidence; keep a deterministic safety layer beneath the learned policy."
    why.append("Always: a verified deterministic safety layer with a minimal-risk maneuver sits beneath anything learned for physical actions.")
    return tier, methods, fallback, why


def parse_flags(argv):
    s = dict(DEFAULTS)
    i = 0
    while i < len(argv):
        a = argv[i]
        if a.startswith("--") and a[2:] in s and i + 1 < len(argv):
            s[a[2:]] = argv[i + 1]
            i += 2
        else:
            i += 1
    return s


def main():
    argv = sys.argv[1:]
    if "--llm" in argv:
        i = argv.index("--llm")
        capability = argv[i + 1] if i + 1 < len(argv) else "describe your capability"
        dry = "--dry-run" in argv
        agent = CivStackAgent.from_skill(SKILL)
        task = ("Capability to route: %s\nApply the routing matrix: recommend the smallest, most "
                "deterministic model tier and the most efficient optimization method that meets the "
                "accuracy/latency/safety bar, plus a verified fallback. Explain the rules you applied."
                % capability)
        print(agent.run(task, dry_run=dry, max_tokens=1200))
        return
    s = parse_flags(argv)
    tier, methods, fallback, why = recommend(s)
    print("Inputs: " + ", ".join("%s=%s" % (k, v) for k, v in s.items()))
    print("\nMODEL TIER:\n  " + tier)
    print("\nOPTIMIZATION METHOD(S):")
    for m in methods:
        print("  - " + m)
    print("\nFALLBACK & SAFETY:\n  " + fallback)
    print("\nWHY (rules fired):")
    for w in why:
        print("  - " + w)


if __name__ == "__main__":
    main()

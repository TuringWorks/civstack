#!/usr/bin/env python3
"""
Example: end-to-end CivStack pipeline.

Chains the pieces the way a real deployment would:

    request --> [route] --> [run role agent] --> [human gate] --> [escalation packet]

1. Route the free-text request to the best skill (keyword in --dry-run, Claude live).
2. Run that skill as a CivStackAgent (operating contract + accountability boundary).
3. Apply the human gate: the agent's output is a recommendation, never a final decision.
4. Emit an escalation packet — a clean handoff to the named accountable human.

  python examples/end_to_end_pipeline.py "applicant J. Okafor, housing aid, mismatched address and household size" --dry-run
  python examples/end_to_end_pipeline.py "we want to deploy an autonomous tractor on a smallholder field"            --dry-run
"""
import sys
import textwrap

from civstack_agent import CivStackAgent
from skill_router import load_index, rank, llm_route


def escalation_packet(agent, request, recommendation):
    return textwrap.dedent("""\
        ============== ESCALATION PACKET ==============
        To (accountable human): {supervisor}
        Role that prepared this: {name}
        Skill: skills/{rel}

        Request:
          {request}

        Agent recommendation / draft (NOT a decision):
        {rec}

        Decision reserved to the human owner because of this boundary:
          {boundary}

        Required of the human: review the evidence and uncertainty above, make the
        accountable decision, and record it. The agent will not finalize it.
        ===============================================""").format(
        supervisor=agent.supervisor, name=agent.name, rel=agent.skill_rel_path,
        request=request, rec=textwrap.indent(recommendation.strip(), "  "),
        boundary=agent.boundary.replace("\n", " ").strip()[:400])


def main():
    dry = "--dry-run" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print('usage: end_to_end_pipeline.py "request" [--dry-run]')
        sys.exit(1)
    request = args[0]

    # 1. ROUTE
    idx = load_index()
    if dry:
        top = rank(request, idx)
        chosen = top[0][1]["rel"] if top else None
        print("[1/4] ROUTE (keyword): %s\n" % chosen)
        for score, e in top[:3]:
            print("      candidate [%d] %s" % (score, e["rel"]))
    else:
        chosen = llm_route(request, idx)
        print("[1/4] ROUTE (Claude): %s" % chosen)
    if not chosen:
        print("No matching skill found.")
        sys.exit(1)

    # 2. RUN
    agent = CivStackAgent.from_skill(chosen)
    print("\n[2/4] RUN role agent: %s (escalates to: %s)" % (agent.name, agent.supervisor))
    if dry:
        recommendation = ("[dry run] The agent would analyze the request under its skill, produce a "
                          "labeled RECOMMENDATION/DRAFT with EVIDENCE, UNCERTAINTY, and ESCALATIONS, "
                          "and stop at the accountability boundary. (Run live to generate the real text.)")
    else:
        recommendation = agent.run(request, max_tokens=1200)

    # 3. HUMAN GATE
    print("\n[3/4] HUMAN GATE: output treated as a recommendation; final decision withheld.")

    # 4. ESCALATION PACKET
    print("\n[4/4] ESCALATION PACKET\n")
    print(escalation_packet(agent, request, recommendation))


if __name__ == "__main__":
    main()

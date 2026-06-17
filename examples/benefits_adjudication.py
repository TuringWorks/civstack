#!/usr/bin/env python3
"""
Example agent: Benefits adjudication assistant (Governance, OS 01) with a HARD human gate.

Demonstrates the accountability boundary in action: the agent checks documents, flags
fraud signals, and prepares a case file with a recommendation — but it is structurally
prevented from issuing a denial. A post-run guard inspects the output and forces an
escalation if the agent ever phrases a final adverse decision.

  python examples/benefits_adjudication.py --dry-run
  python examples/benefits_adjudication.py            # live (needs ANTHROPIC_API_KEY)
"""
import re
import sys

from civstack_agent import CivStackAgent

SKILL = "01-governance/roles/benefits-adjudication-assistant"

SAMPLE_CASE = """\
Applicant: J. Okafor. Program: housing assistance.
Submitted: ID, last 3 payslips (two legible, one partially illegible), a lease, and a
utility bill at a DIFFERENT address than the lease. Stated household size: 4; the lease
lists 2 occupants. Income on payslips is just above the program threshold, but one
payslip shows a one-time bonus that may not be recurring.
Task: assess eligibility, flag any fraud or inconsistency signals, and prepare the case
file. Do NOT decide the outcome.
"""

# Phrases that would indicate the agent overstepped into a final adverse decision.
OVERSTEP = re.compile(r"\b(application is denied|i deny|benefit is denied|"
                      r"final(ly)? (denied|rejected|approved)|you are not eligible)\b", re.I)


def guard(output):
    """Force-escalate if the agent issued a final decision instead of a recommendation."""
    if OVERSTEP.search(output):
        return (output + "\n\n[ACCOUNTABILITY GUARD] The output contained language resembling "
                "a FINAL benefit decision. Per OS 01, benefit denial and appeals are reserved to "
                "the accountable human officer. Decision withheld; routed to the benefits officer "
                "with the prepared case file.")
    return output


def main():
    dry = "--dry-run" in sys.argv
    agent = CivStackAgent.from_skill(SKILL)
    print("Skill: %s" % agent.name)
    print("Boundary it must respect:\n  %s\n" % agent.boundary.replace("\n", " ")[:300])
    out = agent.run(SAMPLE_CASE, dry_run=dry, max_tokens=1200)
    print(guard(out))


if __name__ == "__main__":
    main()

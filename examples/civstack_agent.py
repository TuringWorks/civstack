#!/usr/bin/env python3
"""
CivStack agent harness.

Turns a CivStack SKILL.md into a runnable agent: it loads the skill, wraps it in
the command & cadence operating contract, re-asserts the skill's human-accountability
boundary as a hard rule, and runs a task against the Claude API.

Design goals:
  - Zero dependencies for `--dry-run` (prints the assembled system prompt + task,
    so you can see exactly what the agent would be told without an API key).
  - Live mode needs only the `anthropic` SDK and ANTHROPIC_API_KEY.

Usage (library):
    from civstack_agent import CivStackAgent
    agent = CivStackAgent.from_skill("01-governance/roles/benefits-adjudication-assistant")
    print(agent.run("…task…", dry_run=True))

Usage (CLI):
    python examples/civstack_agent.py <skill-path-under-skills/> "your task" [--dry-run]
"""
import os
import re
import sys
import textwrap

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(REPO_ROOT, "skills")
DEFAULT_MODEL = os.environ.get("CIVSTACK_MODEL", "claude-sonnet-4-6")

# The operating contract every CivStack agent runs under (condensed from
# skills/00-framework: the command & cadence model + the five-layer pattern).
OPERATING_CONTRACT = textwrap.dedent("""\
    You are an AI-personnel agent operating inside the CivStack framework. You run under
    an accountable human owner. Follow this operating contract on every task:

    1. Sense -> interpret -> decide(bounded) -> mobilize -> execute -> verify -> govern.
    2. You may do research, drafting, analysis, monitoring, simulation, and coordination,
       and take only routine, reversible, in-policy actions autonomously.
    3. You MUST surface evidence, uncertainty, constraints, and a log of your assumptions.
    4. You MUST NOT make the decisions reserved to humans (see "HARD ACCOUNTABILITY
       BOUNDARY" below). Prepare them, recommend, and escalate — never finalize them.
    5. When a task touches the boundary, novel situations, conflicting rules, or signs of
       harm/fraud/manipulation, STOP and escalate to the human owner with what you have.

    Output format:
      - RECOMMENDATION / DRAFT (clearly labeled, never presented as a final decision)
      - EVIDENCE & SOURCES
      - UNCERTAINTY & ASSUMPTIONS
      - ESCALATIONS (anything that must go to the human owner, and why)
    """)


def _parse_skill(text):
    """Return (frontmatter_dict, body) from a SKILL.md string."""
    fm = {}
    body = text
    if text.startswith("---\n"):
        _, fmtext, body = text.split("---\n", 2)
        for line in fmtext.splitlines():
            m = re.match(r'^(\w+):\s*"?(.*?)"?\s*$', line)
            if m:
                fm[m.group(1)] = m.group(2)
    return fm, body.strip()


def extract_section(body, heading):
    """Return the markdown under a '## heading' (case-insensitive), or ''."""
    pat = re.compile(r"^##+\s*" + re.escape(heading) + r".*?$", re.IGNORECASE | re.MULTILINE)
    m = pat.search(body)
    if not m:
        return ""
    start = m.end()
    nxt = re.search(r"^##+\s", body[start:], re.MULTILINE)
    end = start + nxt.start() if nxt else len(body)
    return body[start:end].strip()


class CivStackAgent:
    def __init__(self, name, description, body, skill_rel_path, model=DEFAULT_MODEL,
                 extra_context=""):
        self.name = name
        self.description = description
        self.body = body
        self.skill_rel_path = skill_rel_path
        self.model = model
        self.extra_context = extra_context
        # The skill's own accountability boundary, re-asserted as a hard rule.
        self.boundary = (extract_section(body, "Accountability boundary")
                         or extract_section(body, "Human accountability boundary")
                         or "Rights-, safety-, money-, and legitimacy-bearing decisions stay human.")
        # The accountable human this role reports/escalates to.
        m = (re.search(r"Human supervisor:\**\s*([^\n·|]+)", body)
             or re.search(r"Human owner \(([^)]+)\)", body)
             or re.search(r"Reports to:\**\s*([^\n·|]+)", body))
        self.supervisor = m.group(1).strip() if m else "the accountable human owner"

    @classmethod
    def from_skill(cls, skill_rel_path, **kw):
        """skill_rel_path is relative to skills/, with or without trailing /SKILL.md."""
        rel = skill_rel_path
        if not rel.endswith("SKILL.md"):
            rel = os.path.join(rel, "SKILL.md")
        path = os.path.join(SKILLS_DIR, rel)
        with open(path) as f:
            fm, body = _parse_skill(f.read())
        return cls(fm.get("name", rel), fm.get("description", ""), body, rel, **kw)

    def system_prompt(self):
        return "\n\n".join([
            "# Role: %s" % self.name,
            "## Operating contract\n" + OPERATING_CONTRACT,
            "## HARD ACCOUNTABILITY BOUNDARY (never cross)\n" + self.boundary,
            "## Skill definition (your role, expanded)\n" + self.body,
            ("## Additional context\n" + self.extra_context) if self.extra_context else "",
        ]).strip()

    def run(self, task, dry_run=False, max_tokens=1500):
        sys_prompt = self.system_prompt()
        if dry_run:
            return ("===== SYSTEM PROMPT (dry run; no API call) =====\n%s\n\n"
                    "===== USER TASK =====\n%s\n\n"
                    "===== (set ANTHROPIC_API_KEY and drop --dry-run to run live) ====="
                    % (sys_prompt, task))
        try:
            import anthropic
        except ImportError:
            return "ERROR: `pip install anthropic` for live mode (or use --dry-run)."
        client = anthropic.Anthropic()
        resp = client.messages.create(
            model=self.model, max_tokens=max_tokens, system=sys_prompt,
            messages=[{"role": "user", "content": task}])
        return resp.content[0].text


def _cli():
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry = "--dry-run" in sys.argv
    if len(args) < 2:
        print("usage: civstack_agent.py <skill-path> \"task\" [--dry-run]")
        sys.exit(1)
    agent = CivStackAgent.from_skill(args[0])
    print(agent.run(args[1], dry_run=dry))


if __name__ == "__main__":
    _cli()

#!/usr/bin/env python3
"""
CivStack agent harness.

Turns a CivStack SKILL.md into a runnable agent: it loads the skill, wraps it in
the command & cadence operating contract, re-asserts the skill's human-accountability
boundary as a hard rule, and runs a task against the configured LLM provider.

Supported providers (set via CIVSTACK_PROVIDER env var or --provider flag):
  - anthropic  (default)  ANTHROPIC_API_KEY + claude-* models
  - openai                OPENAI_API_KEY    + gpt-* / o1-* models
  - google                GOOGLE_API_KEY    + gemini-* models
  - ollama                local Ollama server, no key needed

Design goals:
  - Zero dependencies for `--dry-run` (prints the assembled system prompt + task,
    so you can see exactly what the agent would be told without an API key).
  - Live mode needs only the provider SDK and its API key.

Usage (library):
    from civstack_agent import CivStackAgent
    agent = CivStackAgent.from_skill("01-governance/roles/benefits-adjudication-assistant")
    print(agent.run("…task…", dry_run=True))

    # Pick provider explicitly:
    agent = CivStackAgent.from_skill("...", provider="openai", model="gpt-4o")
    agent = CivStackAgent.from_skill("...", provider="google", model="gemini-1.5-pro")
    agent = CivStackAgent.from_skill("...", provider="ollama", model="llama3")

Usage (CLI):
    python examples/civstack_agent.py <skill-path-under-skills/> "your task" [--dry-run]
    python examples/civstack_agent.py <skill-path> "task" --provider openai --model gpt-4o
"""
import os
import re
import sys
import textwrap

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(REPO_ROOT, "skills")

# Default provider / model can be set via environment variables.
DEFAULT_PROVIDER = os.environ.get("CIVSTACK_PROVIDER", "anthropic")
_DEFAULT_MODELS = {
    "anthropic": "claude-sonnet-4-6",
    "openai":    "gpt-4o",
    "google":    "gemini-1.5-pro",
    "ollama":    "llama3",
}
DEFAULT_MODEL = os.environ.get(
    "CIVSTACK_MODEL",
    _DEFAULT_MODELS.get(DEFAULT_PROVIDER, "claude-sonnet-4-6"),
)

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


# ---------------------------------------------------------------------------
# Provider back-ends
# ---------------------------------------------------------------------------

def _run_anthropic(system_prompt, task, model, max_tokens):
    try:
        import anthropic
    except ImportError:
        return "ERROR: `pip install anthropic` for Anthropic live mode (or use --dry-run)."
    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=model, max_tokens=max_tokens, system=system_prompt,
        messages=[{"role": "user", "content": task}])
    return resp.content[0].text


def _run_openai(system_prompt, task, model, max_tokens):
    try:
        from openai import OpenAI
    except ImportError:
        return "ERROR: `pip install openai` for OpenAI live mode (or use --dry-run)."
    client = OpenAI()
    resp = client.chat.completions.create(
        model=model, max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": task},
        ])
    return resp.choices[0].message.content


def _run_google(system_prompt, task, model, max_tokens):
    try:
        import google.generativeai as genai
    except ImportError:
        return "ERROR: `pip install google-generativeai` for Google live mode (or use --dry-run)."
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return "ERROR: set GOOGLE_API_KEY for Google provider."
    genai.configure(api_key=api_key)
    gm = genai.GenerativeModel(
        model_name=model,
        system_instruction=system_prompt,
        generation_config=genai.GenerationConfig(max_output_tokens=max_tokens),
    )
    resp = gm.generate_content(task)
    return resp.text


def _run_ollama(system_prompt, task, model, max_tokens):
    """Calls a local Ollama server (http://localhost:11434) — no API key required."""
    try:
        import urllib.request, json as _json
    except ImportError:
        return "ERROR: standard-library missing (unexpected)."
    payload = _json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": task},
        ],
        "stream": False,
        "options": {"num_predict": max_tokens},
    }).encode()
    host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
    req = urllib.request.Request(
        f"{host}/api/chat",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = _json.loads(r.read())
        return data["message"]["content"]
    except Exception as exc:  # noqa: BLE001
        return f"ERROR calling Ollama ({host}): {exc}"


_BACKENDS = {
    "anthropic": _run_anthropic,
    "openai":    _run_openai,
    "google":    _run_google,
    "ollama":    _run_ollama,
}


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class CivStackAgent:
    def __init__(self, name, description, body, skill_rel_path,
                 provider=DEFAULT_PROVIDER, model=None, extra_context=""):
        self.name = name
        self.description = description
        self.body = body
        self.skill_rel_path = skill_rel_path
        self.provider = provider
        self.model = model or _DEFAULT_MODELS.get(provider, DEFAULT_MODEL)
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
                    "===== PROVIDER: %s | MODEL: %s =====\n"
                    "(set the relevant API key and drop --dry-run to run live)"
                    % (sys_prompt, task, self.provider, self.model))
        backend = _BACKENDS.get(self.provider)
        if backend is None:
            supported = ", ".join(sorted(_BACKENDS))
            return (f"ERROR: unknown provider {self.provider!r}. "
                    f"Supported: {supported}.")
        return backend(sys_prompt, task, self.model, max_tokens)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _cli():
    argv = sys.argv[1:]
    dry = "--dry-run" in argv
    argv = [a for a in argv if a != "--dry-run"]

    # Parse --provider and --model flags
    provider = DEFAULT_PROVIDER
    model = None
    filtered = []
    i = 0
    while i < len(argv):
        if argv[i] in ("--provider", "-p") and i + 1 < len(argv):
            provider = argv[i + 1]; i += 2
        elif argv[i] in ("--model", "-m") and i + 1 < len(argv):
            model = argv[i + 1]; i += 2
        else:
            filtered.append(argv[i]); i += 1

    if len(filtered) < 2:
        print("usage: civstack_agent.py <skill-path> \"task\" [--dry-run] "
              "[--provider anthropic|openai|google|ollama] [--model MODEL]")
        sys.exit(1)

    agent = CivStackAgent.from_skill(filtered[0], provider=provider,
                                     **({"model": model} if model else {}))
    print(agent.run(filtered[1], dry_run=dry))


if __name__ == "__main__":
    _cli()

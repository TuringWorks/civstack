#!/usr/bin/env python3
"""
Shared helpers for the CivStack numbered examples (skills/examples/).

Self-contained and dependency-free: indexes every SKILL.md, classifies it by category,
and provides keyword search and section extraction. Lives under skills/ so it travels
with the library; works from any cwd.
"""
import os
import re

SELF_DIR = os.path.dirname(os.path.abspath(__file__))
SKILLS_DIR = os.path.dirname(SELF_DIR)            # skills/examples -> skills
REPO_ROOT = os.path.dirname(SKILLS_DIR)           # skills -> repo root
DOCS_DIR = os.path.join(REPO_ROOT, "docs")
CHECKLISTS_DIR = os.path.join(REPO_ROOT, "checklists")

STOP = set("the a an of for and or to in on with without by is are be this that your you "
           "need needs help review check run plan make build using use it its as at from we "
           "our across into per about can should would will them they then than".split())


def parse_frontmatter(text):
    fm, body = {}, text
    if text.startswith("---\n"):
        _, fmtext, body = text.split("---\n", 2)
        for line in fmtext.splitlines():
            m = re.match(r'^(\w+):\s*"?(.*?)"?\s*$', line)
            if m:
                fm[m.group(1)] = m.group(2)
    return fm, body.strip()


def classify(rel):
    if rel == "00-framework":
        return "framework"
    if rel.startswith("strategic-missions"):
        return "strategic mission"
    if rel.startswith("cross-cutting-archetypes"):
        return "archetype"
    if rel.startswith("_catalogs/"):
        return "catalog:" + rel.split("/")[1]
    parts = rel.split("/")
    if re.match(r"^\d\d-", parts[0]):
        if len(parts) == 1:
            return "operating system"
        return {"roles": "sector role", "robots": "sector robot",
                "autonomous": "sector machine"}.get(parts[1], "sector other")
    return "other"


def load_index():
    idx = []
    for dp, _, fs in os.walk(SKILLS_DIR):
        if "SKILL.md" in fs and os.path.basename(SELF_DIR) not in dp.split(os.sep):
            path = os.path.join(dp, "SKILL.md")
            with open(path) as f:
                fm, body = parse_frontmatter(f.read())
            rel = os.path.relpath(dp, SKILLS_DIR)
            idx.append({"name": fm.get("name", rel), "desc": fm.get("description", ""),
                        "rel": rel, "path": path, "category": classify(rel), "body": body})
    return idx


def tokens(s):
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 2}


def search(query, idx, limit=10):
    q = tokens(query)
    scored = []
    for e in idx:
        score = len(q & tokens(e["name"] + " " + e["desc"]))
        if score:
            scored.append((score, e))
    scored.sort(key=lambda x: (-x[0], x[1]["rel"]))
    return scored[:limit]


def extract_section(body, heading):
    pat = re.compile(r"^##+\s*" + re.escape(heading) + r".*?$", re.IGNORECASE | re.MULTILINE)
    m = pat.search(body)
    if not m:
        return ""
    start = m.end()
    nxt = re.search(r"^##+\s", body[start:], re.MULTILINE)
    return body[start:start + nxt.start()].strip() if nxt else body[start:].strip()


def boundary_of(e):
    return (extract_section(e["body"], "Accountability boundary")
            or extract_section(e["body"], "Human accountability boundary")).split("\n")[0].strip()


def supervisor_of(e):
    m = (re.search(r"Human supervisor:\**\s*([^\n·|]+)", e["body"])
         or re.search(r"Human owner \(([^)]+)\)", e["body"])
         or re.search(r"Reports to:\**\s*([^\n·|]+)", e["body"]))
    return m.group(1).strip() if m else ""

#!/usr/bin/env python3
"""
Verify the generated CivStack skill library.

Checks, with no third-party dependencies:
  1. Every SKILL.md has a well-formed YAML frontmatter block with quoted
     name + description (so it parses in strict YAML readers and Obsidian).
  2. Every relative markdown link (../ and ../../) inside skills resolves to a
     real file or directory.

Exit code is non-zero if any check fails, so it can gate a build.

Usage:  python3 tools/verify.py            # checks ./skills
        python3 tools/verify.py path/to/skills
"""
import os
import re
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "skills")
ROOT = os.path.normpath(ROOT)

link_re = re.compile(r"\]\((\.\.?/[^)#]+)\)")

fm_errors = []
link_errors = []
n_files = 0
n_links = 0

for dp, _, fs in os.walk(ROOT):
    for f in fs:
        if f != "SKILL.md":
            continue
        n_files += 1
        path = os.path.join(dp, f)
        text = open(path).read()
        # --- frontmatter check ---
        if not text.startswith("---\n"):
            fm_errors.append((path, "no leading frontmatter"))
        else:
            lines = text.split("\n")
            end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
            if end is None:
                fm_errors.append((path, "unterminated frontmatter"))
            else:
                block = lines[1:end]
                has_name = any(re.match(r'^name:\s+".*"$', l) for l in block)
                has_desc = any(re.match(r'^description:\s+".*"$', l) for l in block)
                if not has_name:
                    fm_errors.append((path, "missing or unquoted name"))
                if not has_desc:
                    fm_errors.append((path, "missing or unquoted description"))
        # --- relative link check ---
        for m in link_re.finditer(text):
            target = m.group(1)
            n_links += 1
            resolved = os.path.normpath(os.path.join(dp, target))
            if not os.path.exists(resolved):
                link_errors.append((path, target))

print("Verified %d SKILL.md files (%d relative links)." % (n_files, n_links))
print("  frontmatter errors: %d" % len(fm_errors))
print("  broken links:       %d" % len(link_errors))
for p, why in fm_errors[:30]:
    print("  FM   %s -> %s" % (p, why))
for p, t in link_errors[:30]:
    print("  LINK %s -> %s" % (p, t))

sys.exit(1 if (fm_errors or link_errors) else 0)

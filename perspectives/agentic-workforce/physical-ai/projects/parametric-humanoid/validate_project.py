#!/usr/bin/env python3
"""Dependency-free consistency checks for the Lamina pre-fabrication release."""

from __future__ import annotations

import csv
import json
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
errors: list[str] = []
checks = 0


def check(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        errors.append(message)


required = [
    "PROJECT-READINESS.md",
    "engineering/Lamina-Engineering-Baseline-v06.xlsx",
    "cad/freecad/generated/Lamina-Slender-Biped-v5.FCStd",
    "prototype-joint-rig/cad/generated/Lamina-J1-Tendon-Joint-Rig.FCStd",
    "prototype-joint-rig/cad/generated/Lamina-J1-Pose-Study.FCStd",
    "simulation/generated/lamina-v06.urdf",
    "simulation/generated/joint-map.csv",
    "safety/hazard-register.csv",
    "verification/verification-matrix.csv",
]
for rel in required:
    check((ROOT / rel).is_file(), f"missing required artifact: {rel}")

csv_minimums = {
    "engineering/mass-budget.csv": 10,
    "engineering/joint-load-budget.csv": 10,
    "engineering/power-budget.csv": 8,
    "engineering/cost-budget.csv": 8,
    "safety/hazard-register.csv": 20,
    "verification/verification-matrix.csv": 30,
}
for rel, minimum in csv_minimums.items():
    path = ROOT / rel
    try:
        with path.open(newline="", encoding="utf-8-sig") as stream:
            rows = list(csv.DictReader(stream))
        check(len(rows) >= minimum, f"{rel}: expected at least {minimum} data rows, found {len(rows)}")
        check(bool(rows) and all(rows[0].keys()), f"{rel}: invalid or empty header")
    except Exception as exc:
        errors.append(f"{rel}: CSV parse failed: {exc}")

for rel in ["interfaces/motion-intent.schema.json", "interfaces/joint-command.schema.json"]:
    try:
        json.loads((ROOT / rel).read_text(encoding="utf-8"))
        check(True, rel)
    except Exception as exc:
        errors.append(f"{rel}: JSON parse failed: {exc}")

try:
    tree = ET.parse(ROOT / "simulation/generated/lamina-v06.urdf")
    commanded = [joint for joint in tree.getroot().findall("joint") if joint.get("type") != "fixed"]
    check(len(commanded) == 31, f"URDF expected 31 commanded joints, found {len(commanded)}")
except Exception as exc:
    errors.append(f"URDF parse failed: {exc}")

for rel in [
    "engineering/Lamina-Engineering-Baseline-v06.xlsx",
    "cad/freecad/generated/Lamina-Slender-Biped-v5.FCStd",
    "prototype-joint-rig/cad/generated/Lamina-J1-Tendon-Joint-Rig.FCStd",
    "prototype-joint-rig/cad/generated/Lamina-J1-Pose-Study.FCStd",
]:
    path = ROOT / rel
    try:
        with zipfile.ZipFile(path) as archive:
            check(archive.testzip() is None, f"corrupt ZIP container: {rel}")
    except Exception as exc:
        errors.append(f"{rel}: container validation failed: {exc}")

for rel, phrase in [
    ("cad/freecad/generated/validation-report.txt", "Validation passed for all"),
    ("prototype-joint-rig/cad/generated/validation-report.txt", "Validation passed."),
]:
    text = (ROOT / rel).read_text(encoding="utf-8") if (ROOT / rel).is_file() else ""
    check(phrase in text, f"{rel}: passing result not found")

# Check local Markdown links in the release index and project README.
for rel in ["README.md", "PROJECT-READINESS.md"]:
    text = (ROOT / rel).read_text(encoding="utf-8")
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
        if "://" not in target and not target.startswith("#"):
            clean = target.split("#", 1)[0]
            check((ROOT / clean).exists(), f"{rel}: broken local link: {target}")

if errors:
    print(f"FAIL: {len(errors)} issue(s) across {checks} checks")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print(f"PASS: {checks} project checks")
print("Status: pre-fabrication package coherent; physical hardware gates remain open.")


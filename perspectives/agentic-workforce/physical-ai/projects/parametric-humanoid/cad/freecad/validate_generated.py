#!/usr/bin/env python3
"""Validate generated Lamina FreeCAD documents with FreeCAD's Python runtime."""

from __future__ import annotations

import glob
import os
import sys

import FreeCAD as App


HERE = os.path.dirname(os.path.abspath(__file__))
GENERATED = os.path.join(HERE, "generated")


def validate(path):
    doc = App.openDocument(path)
    shaped = [
        o
        for o in doc.Objects
        if o.TypeId == "Part::Feature"
        and hasattr(o, "Shape")
        and not o.Shape.isNull()
        and len(o.Shape.Solids) > 0
        and o.Shape.BoundBox.isValid()
    ]
    invalid = [o.Name for o in shaped if not o.Shape.isValid()]
    if not shaped:
        raise RuntimeError("No geometric objects in %s" % path)
    box = shaped[0].Shape.BoundBox
    xmin, ymin, zmin = box.XMin, box.YMin, box.ZMin
    xmax, ymax, zmax = box.XMax, box.YMax, box.ZMax
    for obj in shaped[1:]:
        b = obj.Shape.BoundBox
        xmin, ymin, zmin = min(xmin, b.XMin), min(ymin, b.YMin), min(zmin, b.ZMin)
        xmax, ymax, zmax = max(xmax, b.XMax), max(ymax, b.YMax), max(zmax, b.ZMax)
    if invalid:
        raise RuntimeError("Invalid shapes in %s: %s" % (path, ", ".join(invalid)))
    summary = "%s: %d shapes; bounds %.1f x %.1f x %.1f mm; z %.1f..%.1f" % (
        os.path.basename(path), len(shaped), xmax - xmin, ymax - ymin, zmax - zmin, zmin, zmax
    )
    App.Console.PrintMessage(summary + "\n")
    App.closeDocument(doc.Name)
    return len(shaped), (xmin, ymin, zmin, xmax, ymax, zmax), summary


def main():
    paths = sorted(glob.glob(os.path.join(GENERATED, "*.FCStd")))
    if len(paths) < 6:
        raise RuntimeError("Expected at least 6 FCStd documents, found %d" % len(paths))
    reports = {os.path.basename(path): validate(path) for path in paths}
    master_count, master_bounds, _ = reports["Lamina-Slender-Biped-v4.FCStd"]
    if master_count < 70:
        raise RuntimeError("Master assembly is unexpectedly sparse: %d shapes" % master_count)
    if not (1400 <= master_bounds[5] <= 1600):
        raise RuntimeError("Master assembly height is outside the intended envelope: %.1f" % master_bounds[5])
    v5_count, v5_bounds, _ = reports["Lamina-Slender-Biped-v5.FCStd"]
    if v5_count < 70:
        raise RuntimeError("V5 assembly is unexpectedly sparse: %d shapes" % v5_count)
    if not (1400 <= v5_bounds[5] <= 1600):
        raise RuntimeError("V5 assembly height is outside the intended envelope: %.1f" % v5_bounds[5])
    report_path = os.path.join(GENERATED, "validation-report.txt")
    with open(report_path, "w", encoding="utf-8") as stream:
        for name in sorted(reports):
            stream.write(reports[name][2] + "\n")
        stream.write("Validation passed for all Lamina FreeCAD artifacts.\n")
    App.Console.PrintMessage("Validation passed; report: %s\n" % report_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())

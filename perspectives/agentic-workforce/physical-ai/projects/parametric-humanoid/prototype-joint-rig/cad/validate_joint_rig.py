#!/usr/bin/env python3
"""Validate the J1 FreeCAD assembly and generated cutting profiles."""

from __future__ import annotations

import glob
import os
import zipfile

import FreeCAD as App


HERE = os.path.dirname(os.path.abspath(__file__))
GENERATED = os.path.join(HERE, "generated")
MODEL = os.path.join(GENERATED, "Lamina-J1-Tendon-Joint-Rig.FCStd")
POSE_MODEL = os.path.join(GENERATED, "Lamina-J1-Pose-Study.FCStd")


def main():
    doc = App.openDocument(MODEL)
    solids = [
        o for o in doc.Objects
        if o.TypeId == "Part::Feature" and hasattr(o, "Shape")
        and not o.Shape.isNull() and len(o.Shape.Solids) > 0 and o.Shape.isValid()
    ]
    if len(solids) < 24:
        raise RuntimeError("Expected at least 24 valid solid features, found %d" % len(solids))
    bounds = [o.Shape.BoundBox for o in solids]
    xmin, ymin, zmin = min(b.XMin for b in bounds), min(b.YMin for b in bounds), min(b.ZMin for b in bounds)
    xmax, ymax, zmax = max(b.XMax for b in bounds), max(b.YMax for b in bounds), max(b.ZMax for b in bounds)
    App.closeDocument(doc.Name)

    dxf_paths = sorted(glob.glob(os.path.join(GENERATED, "dxf", "*.dxf")))
    if len(dxf_paths) != 11:
        raise RuntimeError("Expected 11 DXF profiles, found %d" % len(dxf_paths))
    empty = [p for p in dxf_paths if os.path.getsize(p) < 200]
    if empty:
        raise RuntimeError("DXF files unexpectedly small: %s" % ", ".join(empty))
    with zipfile.ZipFile(MODEL) as archive:
        if "GuiDocument.xml" not in archive.namelist():
            raise RuntimeError("FreeCAD GUI visibility metadata is missing")

    pose_doc = App.openDocument(POSE_MODEL)
    pose_solids = [
        o for o in pose_doc.Objects
        if o.TypeId == "Part::Feature" and hasattr(o, "Shape")
        and not o.Shape.isNull() and len(o.Shape.Solids) > 0 and o.Shape.isValid()
    ]
    App.closeDocument(pose_doc.Name)
    if len(pose_solids) < len(solids) + 6:
        raise RuntimeError("Pose study is missing expected ghosted arm solids")
    with zipfile.ZipFile(POSE_MODEL) as archive:
        if "GuiDocument.xml" not in archive.namelist():
            raise RuntimeError("Pose-study GUI visibility metadata is missing")

    report = os.path.join(GENERATED, "validation-report.txt")
    with open(report, "w", encoding="utf-8") as stream:
        stream.write("J1 FreeCAD solids: %d\n" % len(solids))
        stream.write("Bounds: %.1f × %.1f × %.1f mm\n" % (xmax - xmin, ymax - ymin, zmax - zmin))
        stream.write("DXF profiles: %d\n" % len(dxf_paths))
        stream.write("Pose-study solids: %d\n" % len(pose_solids))
        stream.write("GuiDocument.xml: present\n")
        stream.write("Validation passed.\n")
    App.Console.PrintMessage("J1 validation passed: %s\n" % report)


if __name__ == "__main__":
    main()

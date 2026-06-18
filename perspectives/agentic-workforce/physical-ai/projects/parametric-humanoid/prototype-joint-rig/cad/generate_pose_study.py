#!/usr/bin/env python3
"""Create a FreeCAD overlay of J1 at −10°, 45°, and 110°."""

from __future__ import annotations

import os

import FreeCAD as App


HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "generated", "Lamina-J1-Tendon-Joint-Rig.FCStd")
OUTPUT = os.path.join(HERE, "generated", "Lamina-J1-Pose-Study.FCStd")


def main():
    doc = App.openDocument(SOURCE)
    doc.saveAs(OUTPUT)
    group = doc.addObject("App::DocumentObjectGroup", "PoseStudy")
    group.Label = "Ghosted joint-limit and mid-range poses"
    pivot = App.Vector(0, 0, 240)
    axis = App.Vector(0, 1, 0)
    source_names = ("FrontSwingArm", "RearSwingArm")
    for angle, suffix in [(-10, "Minus10"), (45, "Mid45"), (110, "Max110")]:
        for source_name in source_names:
            source = doc.getObject(source_name)
            ghost = doc.addObject("Part::Feature", source_name + suffix)
            ghost.Label = "%s at %d degrees" % (source.Label, angle)
            posed_shape = source.Shape.copy()
            posed_shape.rotate(pivot, axis, angle)
            ghost.Shape = posed_shape
            ghost.addProperty("App::PropertyAngle", "PoseAngle", "Pose Study")
            ghost.PoseAngle = angle
            group.addObject(ghost)
    doc.recompute()
    doc.save()
    print("Generated pose study: %s" % OUTPUT)


if __name__ == "__main__":
    main()

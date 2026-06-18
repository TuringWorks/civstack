#!/usr/bin/env python3
"""Color, display, and preview the J1 pose-study FreeCAD document."""

from __future__ import annotations

import os

import FreeCAD as App
import FreeCADGui as Gui


HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, "generated", "Lamina-J1-Pose-Study.FCStd")
PREVIEW = os.path.join(HERE, "generated", "Lamina-J1-Pose-Study-preview.png")


def main():
    Gui.showMainWindow()
    doc = App.openDocument(MODEL)
    gui = Gui.getDocument(doc.Name)
    poses = doc.getObject("PoseStudy")
    for obj in doc.Objects:
        view = gui.getObject(obj.Name)
        if view:
            view.Visibility = True
    if poses:
        for obj in poses.Group:
            view = gui.getObject(obj.Name)
            if "Minus10" in obj.Name:
                view.ShapeColor = (0.20, 0.55, 0.90)
            elif "Mid45" in obj.Name:
                view.ShapeColor = (0.95, 0.55, 0.12)
            else:
                view.ShapeColor = (0.72, 0.18, 0.22)
            view.LineColor = tuple(c * 0.55 for c in view.ShapeColor)
            view.Transparency = 55
            try:
                view.DisplayMode = "Flat Lines"
            except Exception:
                pass
    view = gui.activeView()
    view.setCameraOrientation(App.Rotation(App.Vector(1, 0, 0), -90).Q)
    Gui.updateGui()
    view.fitAll()
    Gui.updateGui()
    view.saveImage(PREVIEW, 1400, 1000, "White")
    doc.save()
    App.closeDocument(doc.Name)
    Gui.getMainWindow().close()
    App.Console.PrintMessage("Saved J1 pose-study GUI metadata and preview.\n")


if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""Save visible FreeCAD view metadata and a J1 preview image."""

from __future__ import annotations

import os

import FreeCAD as App
import FreeCADGui as Gui


HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, "generated", "Lamina-J1-Tendon-Joint-Rig.FCStd")
PREVIEW = os.path.join(HERE, "generated", "Lamina-J1-Tendon-Joint-Rig-preview.png")


def names(doc, group):
    obj = doc.getObject(group)
    return set(o.Name for o in obj.Group) if obj else set()


def main():
    Gui.showMainWindow()
    doc = App.openDocument(MODEL)
    gui = Gui.getDocument(doc.Name)
    groups = {
        "wood": names(doc, "WoodParts"),
        "hardware": names(doc, "StandardHardware"),
        "actuation": names(doc, "Actuation"),
        "tendons": names(doc, "Tendons"),
        "safety": names(doc, "Safety"),
    }
    for obj in doc.Objects:
        view = gui.getObject(obj.Name)
        if not view:
            continue
        view.Visibility = True
        if not hasattr(view, "ShapeColor"):
            continue
        color, transparency = (0.78, 0.55, 0.30), 0
        if obj.Name in groups["hardware"]:
            color = (0.52, 0.55, 0.57)
        elif obj.Name in groups["actuation"]:
            color = (0.10, 0.13, 0.15)
        elif obj.Name in groups["tendons"]:
            color = (0.03, 0.04, 0.05)
        elif obj.Name == "GuardEnvelope":
            color, transparency = (0.50, 0.75, 0.85), 88
        view.ShapeColor = color
        view.LineColor = tuple(c * 0.55 for c in color)
        view.Transparency = transparency
        try:
            view.DisplayMode = "Flat Lines"
        except Exception:
            pass
    view = gui.activeView()
    # FreeCAD's named views can retain the prior camera in this headless GUI
    # path. Rotate the default camera explicitly to look along the rig's Y axis.
    view.setCameraOrientation(App.Rotation(App.Vector(1, 0, 0), -90).Q)
    Gui.updateGui()
    view.fitAll()
    Gui.updateGui()
    view.saveImage(PREVIEW, 1400, 1000, "White")
    view.setCameraOrientation(App.Rotation(App.Vector(1, 0, 0), -90).Q)
    view.fitAll()
    doc.save()
    App.closeDocument(doc.Name)
    Gui.getMainWindow().close()
    App.Console.PrintMessage("Saved J1 GUI metadata and preview.\n")


if __name__ == "__main__":
    main()

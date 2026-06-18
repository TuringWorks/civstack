#!/usr/bin/env python3
"""Add FreeCAD GUI view metadata and render a visibility smoke-test preview."""

from __future__ import annotations

import glob
import os

import FreeCAD as App
import FreeCADGui as Gui


HERE = os.path.dirname(os.path.abspath(__file__))
GENERATED = os.path.join(HERE, "generated")
PREVIEW = os.path.abspath(os.path.join(HERE, "..", "..", "images", "lamina-freecad-v4-preview.png"))
PREVIEW_V5_FRONT = os.path.abspath(os.path.join(HERE, "..", "..", "images", "lamina-freecad-v5-front.png"))

WOOD = (0.78, 0.55, 0.30)
WOOD_LIGHT = (0.92, 0.76, 0.50)
CHARCOAL = (0.10, 0.13, 0.15)
STEEL = (0.52, 0.55, 0.57)
RUBBER = (0.035, 0.045, 0.05)
RED = (0.82, 0.04, 0.03)
YELLOW = (0.95, 0.68, 0.04)


def members(doc, group_name):
    group = doc.getObject(group_name)
    return set(o.Name for o in group.Group) if group and hasattr(group, "Group") else set()


def configure_document(doc):
    gui_doc = Gui.getDocument(doc.Name)
    wood = members(doc, "WoodStructure") | members(doc, "Component")
    hardware = members(doc, "JointHardware")
    actuation = members(doc, "Actuation")
    tendons = members(doc, "TendonRouting")
    sensors = members(doc, "Sensors")
    safety = members(doc, "Safety")
    references = members(doc, "References")

    for obj in doc.Objects:
        view = gui_doc.getObject(obj.Name)
        if view is None:
            continue
        view.Visibility = True
        if not hasattr(view, "ShapeColor"):
            continue
        color = WOOD_LIGHT
        transparency = 0
        if obj.Name in hardware:
            color = STEEL
        elif obj.Name in actuation or obj.Name in tendons:
            color = CHARCOAL
        elif obj.Name in sensors:
            color = RUBBER
        elif obj.Name in safety:
            color = STEEL
        elif obj.Name in references:
            color, transparency = (0.76, 0.76, 0.72), 82
        elif obj.Name in wood:
            color = WOOD
        if "EStopButton" in obj.Name or obj.Name == "Button":
            color = RED
        elif "EStopCollar" in obj.Name or obj.Name == "Collar":
            color = YELLOW
        elif "FingerPad" in obj.Name or "Sole" in obj.Name or obj.Name.startswith("Pad"):
            color = RUBBER
        view.ShapeColor = color
        view.LineColor = tuple(max(0.0, c * 0.55) for c in color)
        view.Transparency = transparency
        if hasattr(view, "DisplayMode"):
            try:
                view.DisplayMode = "Flat Lines"
            except Exception:
                pass
    doc.recompute()
    doc.save()


def main():
    Gui.showMainWindow()
    for path in sorted(glob.glob(os.path.join(GENERATED, "*.FCStd"))):
        doc = App.openDocument(path)
        configure_document(doc)
        if os.path.basename(path) == "Lamina-Slender-Biped-v4.FCStd":
            gui_doc = Gui.getDocument(doc.Name)
            floor_view = gui_doc.getObject("Floor")
            if floor_view is not None:
                floor_view.Visibility = False
            view = gui_doc.activeView()
            view.viewFront()
            Gui.updateGui()
            view.fitAll()
            Gui.updateGui()
            view.saveImage(PREVIEW, 1400, 1400, "White")
            if floor_view is not None:
                floor_view.Visibility = True
            view.viewFront()
            view.fitAll()
            doc.save()
        elif os.path.basename(path) == "Lamina-Slender-Biped-v5.FCStd":
            gui_doc = Gui.getDocument(doc.Name)
            floor_view = gui_doc.getObject("Floor")
            if floor_view is not None:
                floor_view.Visibility = False
            view = gui_doc.activeView()
            view.viewFront()
            Gui.updateGui()
            view.fitAll()
            Gui.updateGui()
            view.saveImage(PREVIEW_V5_FRONT, 1400, 1400, "White")
            if floor_view is not None:
                floor_view.Visibility = True
            view.viewFront()
            view.fitAll()
            doc.save()
        App.closeDocument(doc.Name)
    Gui.getMainWindow().close()
    App.Console.PrintMessage("Saved GUI visibility metadata and FreeCAD previews.\n")


if __name__ == "__main__":
    main()

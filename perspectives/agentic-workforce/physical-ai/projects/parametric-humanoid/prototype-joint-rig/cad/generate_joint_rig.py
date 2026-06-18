#!/usr/bin/env python3
"""Generate the Lamina J1 tendon-joint rig and laser-cut DXFs in FreeCAD."""

from __future__ import annotations

import math
import os
import sys

import FreeCAD as App
import Part
import importDXF


HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
BASE_LIB = os.path.join(PROJECT_ROOT, "cad", "freecad")
if BASE_LIB not in sys.path:
    sys.path.insert(0, BASE_LIB)
import generate_lamina_v4 as base


OUT = os.path.join(HERE, "generated")
DXF_OUT = os.path.join(OUT, "dxf")
os.makedirs(DXF_OUT, exist_ok=True)


def circle_face(cx, cy, radius):
    edge = Part.makeCircle(radius, App.Vector(cx, cy, 0))
    return Part.Face(Part.Wire([edge]))


def rect_face(x0, y0, width, height):
    return base.polygon_face([
        (x0, y0, 0),
        (x0 + width, y0, 0),
        (x0 + width, y0 + height, 0),
        (x0, y0 + height, 0),
    ])


def plate_with_holes(outer, holes):
    result = outer
    for x, y, radius in holes:
        result = result.cut(circle_face(x, y, radius))
    return result


def base_plate_2d():
    outer = rect_face(0, 0, 470, 260)
    holes = [(25, 25, 4.5), (445, 25, 4.5), (25, 235, 4.5), (445, 235, 4.5)]
    # Upright and motor-plate through-bolt patterns.
    holes += [(190, 85, 3.3), (280, 85, 3.3), (190, 175, 3.3), (280, 175, 3.3)]
    holes += [(50, 70, 3.3), (150, 70, 3.3), (50, 190, 3.3), (150, 190, 3.3)]
    return plate_with_holes(outer, holes)


def upright_2d():
    outer = base.polygon_face([(0, 0, 0), (120, 0, 0), (120, 250, 0), (92, 300, 0), (28, 300, 0), (0, 250, 0)])
    holes = [(60, 220, 6.6)]
    for angle in (45, 135, 225, 315):
        holes.append((60 + 22 * math.cos(math.radians(angle)), 220 + 22 * math.sin(math.radians(angle)), 2.5))
    holes += [(20, 20, 3.3), (100, 20, 3.3), (20, 70, 3.3), (100, 70, 3.3)]
    return plate_with_holes(outer, holes)


def swing_arm_2d():
    outer = base.polygon_face([(0, 0, 0), (340, 15, 0), (340, 75, 0), (0, 90, 0)])
    holes = [(45, 45, 6.6), (120, 45, 3.3), (300, 45, 3.3), (325, 45, 4.3)]
    for angle in (45, 135, 225, 315):
        holes.append((45 + 28 * math.cos(math.radians(angle)), 45 + 28 * math.sin(math.radians(angle)), 3.3))
    # Large lightening window.
    result = plate_with_holes(outer, holes)
    window = base.polygon_face([(105, 28, 0), (285, 35, 0), (285, 58, 0), (105, 62, 0)])
    return result.cut(window)


def motor_plate_2d():
    outer = rect_face(0, 0, 150, 150)
    holes = [(75, 85, 19.25)]
    for dx in (-23.57, 23.57):
        for dy in (-23.57, 23.57):
            holes.append((75 + dx, 85 + dy, 2.8))
    holes += [(20, 20, 3.3), (130, 20, 3.3), (20, 135, 3.3), (130, 135, 3.3)]
    return plate_with_holes(outer, holes)


def spacer_2d():
    return plate_with_holes(rect_face(0, 0, 90, 40), [(12, 20, 3.3), (78, 20, 3.3)])


def ring_2d(outer_d, inner_d, bolt_radius=None, bolt_hole=2.5):
    result = circle_face(outer_d / 2, outer_d / 2, outer_d / 2)
    result = result.cut(circle_face(outer_d / 2, outer_d / 2, inner_d / 2))
    if bolt_radius:
        for angle in (45, 135, 225, 315):
            result = result.cut(circle_face(
                outer_d / 2 + bolt_radius * math.cos(math.radians(angle)),
                outer_d / 2 + bolt_radius * math.sin(math.radians(angle)),
                bolt_hole,
            ))
    return result


def disk_2d(diameter, bore, bolt_radius=None):
    result = circle_face(diameter / 2, diameter / 2, diameter / 2)
    result = result.cut(circle_face(diameter / 2, diameter / 2, bore / 2))
    if bolt_radius:
        for angle in (45, 135, 225, 315):
            result = result.cut(circle_face(
                diameter / 2 + bolt_radius * math.cos(math.radians(angle)),
                diameter / 2 + bolt_radius * math.sin(math.radians(angle)),
                3.3,
            ))
    return result


def fit_coupon_2d():
    outer = rect_face(0, 0, 180, 80)
    holes = [
        (25, 25, 6.0), (55, 25, 6.1), (85, 25, 6.2),
        (120, 25, 13.9), (155, 25, 14.1),
        (35, 60, 13.9), (75, 60, 14.0), (115, 60, 14.1), (155, 60, 14.2),
    ]
    return plate_with_holes(outer, holes)


PARTS = {
    "base-12mm": (base_plate_2d, 12.0),
    "upright-12mm": (upright_2d, 12.0),
    "swing-arm-cheek-12mm": (swing_arm_2d, 12.0),
    "motor-plate-nema23-12mm": (motor_plate_2d, 12.0),
    "spacer-12mm": (spacer_2d, 12.0),
    "bearing-retainer-6mm": (lambda: ring_2d(60, 28.2, 22), 6.0),
    "sector-outer-6mm": (lambda: disk_2d(160, 13.2, 28), 6.0),
    "sector-groove-6mm": (lambda: disk_2d(150, 13.2, 28), 6.0),
    "capstan-outer-6mm": (lambda: disk_2d(70, 6.6), 6.0),
    "capstan-groove-6mm": (lambda: disk_2d(62, 6.6), 6.0),
    "fit-coupon-6mm": (fit_coupon_2d, 6.0),
}


def export_dxf(name, face):
    doc = App.newDocument("DXF_" + name.replace("-", "_"))
    obj = doc.addObject("Part::Feature", "CutProfile")
    obj.Label = name
    obj.Shape = face
    doc.recompute()
    importDXF.export([obj], os.path.join(DXF_OUT, name + ".dxf"))
    App.closeDocument(doc.Name)


def vertical_shape(face, thickness, translation):
    shape = face.extrude(App.Vector(0, 0, thickness))
    shape.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 90)
    shape.translate(App.Vector(*translation))
    return shape


def build_assembly():
    doc = App.newDocument("Lamina_J1_Tendon_Joint_Rig")
    params = doc.addObject("App::FeaturePython", "DesignParameters")
    params.addProperty("App::PropertyString", "Status", "Documentation")
    params.Status = "Phase-0 test rig; proof-test behind guarding; not a human-rated joint"
    for prop, value in [("PivotHeight", 240.0), ("SectorRadius", 75.0), ("CapstanRadius", 30.0), ("ShaftDiameter", 12.0), ("CheekSpacing", 100.0)]:
        params.addProperty("App::PropertyLength", prop, "Geometry")
        setattr(params, prop, value)

    wood = doc.addObject("App::DocumentObjectGroup", "WoodParts")
    hardware = doc.addObject("App::DocumentObjectGroup", "StandardHardware")
    actuation = doc.addObject("App::DocumentObjectGroup", "Actuation")
    tendons = doc.addObject("App::DocumentObjectGroup", "Tendons")
    safety = doc.addObject("App::DocumentObjectGroup", "Safety")

    base_shape = base_plate_2d().extrude(App.Vector(0, 0, 12))
    base_shape.translate(App.Vector(-235, -130, 0))
    base.add_feature(doc, wood, "BasePlate", "12 mm bench base", base_shape, base.WOOD_LIGHT)

    # Uprights: pivot is at world x=0 z=240; local pivot is x=60 y=220.
    for side, world_y in [("Front", -50), ("Rear", 62)]:
        shape = vertical_shape(upright_2d(), 12, (-60, world_y, 20))
        base.add_feature(doc, wood, side + "Upright", side + " replaceable upright", shape, base.WOOD)

    # Bearing retainers outside each upright.
    for side, world_y in [("Front", -58), ("Rear", 70)]:
        ring_face = ring_2d(60, 28.2, 22)
        ring = ring_face.extrude(App.Vector(0, 0, 6))
        ring.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 90)
        ring.translate(App.Vector(-30, world_y, 210))
        base.add_feature(doc, wood, side + "BearingRetainer", side + " bolted bearing retainer", ring, base.WOOD_LIGHT)

    # Bearings and shaft.
    for side, y in [("Front", -50), ("Rear", 62)]:
        bearing = Part.makeCylinder(14, 8, App.Vector(0, y, 240), App.Vector(0, 1, 0)).cut(
            Part.makeCylinder(6, 10, App.Vector(0, y - 1, 240), App.Vector(0, 1, 0))
        )
        base.add_feature(doc, hardware, side + "Bearing", side + " 6001 bearing", bearing, base.STEEL)
    shaft = Part.makeCylinder(6, 160, App.Vector(0, -80, 240), App.Vector(0, 1, 0))
    base.add_feature(doc, hardware, "PivotShaft", "12 mm standard shaft", shaft, base.STEEL)

    # Swing-arm cheeks at each side, horizontal in neutral pose.
    for side, world_y in [("Front", -34), ("Rear", 46)]:
        arm = vertical_shape(swing_arm_2d(), 12, (-45, world_y, 195))
        base.add_feature(doc, wood, side + "SwingArm", side + " swing-arm cheek", arm, base.WOOD)

    # Laminated sector attached to arm around the pivot.
    for i, diameter in enumerate((160, 150, 160)):
        face = disk_2d(diameter, 13.2, 28)
        disk = face.extrude(App.Vector(0, 0, 6))
        disk.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 90)
        disk.translate(App.Vector(-diameter / 2, -16 + i * 6, 240 - diameter / 2))
        base.add_feature(doc, wood, "SectorLayer%d" % i, "Laminated sector layer", disk, base.WOOD_LIGHT if i != 1 else base.WOOD_EDGE)

    # Motor plate and generic actuator envelope.
    motor_plate = vertical_shape(motor_plate_2d(), 12, (-205, -6, 20))
    base.add_feature(doc, wood, "MotorPlate", "Replaceable NEMA-23-class motor plate", motor_plate, base.WOOD)
    motor = Part.makeBox(57, 80, 57, App.Vector(-168.5, -46, 72))
    base.add_feature(doc, actuation, "MotorEnvelope", "Closed-loop actuator envelope", motor, base.CHARCOAL)
    capstan_center = (-140, 0, 105)
    for i, radius in enumerate((35, 31, 35)):
        capstan = Part.makeCylinder(radius, 6, App.Vector(capstan_center[0], -9 + i * 6, capstan_center[2]), App.Vector(0, 1, 0))
        base.add_feature(doc, wood, "CapstanLayer%d" % i, "Laminated motor capstan", capstan, base.WOOD_LIGHT if i != 1 else base.WOOD_EDGE)

    # Schematic opposing tendon runs.
    for i, (start, end) in enumerate([
        ((-112, -1, 122), (-62, -1, 286)),
        ((-112, 1, 88), (-62, 1, 194)),
    ]):
        base.add_feature(doc, tendons, "Tendon%d" % i, "Opposing low-stretch tendon", base.cylinder_between(start, end, 2.0), base.RUBBER)

    # Adjustable hard-stop bolt envelopes.
    for i, z in enumerate((170, 310)):
        stop = Part.makeCylinder(4, 65, App.Vector(-50, -32.5, z), App.Vector(0, 1, 0))
        base.add_feature(doc, safety, "HardStop%d" % i, "Adjustable M8 hard-stop envelope", stop, base.STEEL)

    # Encoder and guarded sweep envelope.
    encoder = Part.makeCylinder(18, 12, App.Vector(0, 78, 240), App.Vector(0, 1, 0))
    base.add_feature(doc, hardware, "JointEncoder", "Output-shaft absolute encoder envelope", encoder, base.CHARCOAL)
    guard = Part.makeCylinder(185, 130, App.Vector(0, -65, 240), App.Vector(0, 1, 0), 0, 145)
    base.add_feature(doc, safety, "GuardEnvelope", "Transparent guard envelope", guard, (0.5, 0.75, 0.85), 85)

    doc.recompute()
    fcstd = os.path.join(OUT, "Lamina-J1-Tendon-Joint-Rig.FCStd")
    doc.saveAs(fcstd)
    Part.export(base.solid_features(doc), os.path.join(OUT, "Lamina-J1-Tendon-Joint-Rig.step"))
    return doc


def main():
    for name, (factory, _) in PARTS.items():
        export_dxf(name, factory())
    build_assembly()
    print("Generated J1 FreeCAD assembly and %d DXF profiles in %s" % (len(PARTS), OUT))


if __name__ == "__main__":
    main()


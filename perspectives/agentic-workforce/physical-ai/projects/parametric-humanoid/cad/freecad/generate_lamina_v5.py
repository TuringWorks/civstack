#!/usr/bin/env python3
"""Generate the image-aligned Lamina Slender Wooden Biped v5 FreeCAD model."""

from __future__ import annotations

import math
import os
import sys

import FreeCAD as App
import Part


HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import generate_lamina_v4 as base


OUT = os.path.join(HERE, "generated")
os.makedirs(OUT, exist_ok=True)


def truss_plate_z(cx, cy, z0, z1, w0, w1, thickness=12, border=14):
    outer = base.tapered_solid_z(cx, cy, z0, z1, w0, thickness, w1, thickness)
    if z1 - z0 < 2 * border + 20:
        return outer
    inner = base.tapered_solid_z(
        cx,
        cy,
        z0 + border,
        z1 - border,
        max(12, w0 - 2 * border),
        thickness + 4,
        max(12, w1 - 2 * border),
        thickness + 4,
    )
    return outer.cut(inner)


def truss_link_z(cx, cy, z0, z1, w0, d0, w1, d1, plate=10, border=14):
    front = truss_plate_z(cx, cy - d0 / 2 + plate / 2, z0, z1, w0, w1, plate, border)
    back = truss_plate_z(cx, cy + d0 / 2 - plate / 2, z0, z1, w0, w1, plate, border)
    low = Part.makeBox(w0, d0, border, App.Vector(cx - w0 / 2, cy - d0 / 2, z0))
    high = Part.makeBox(w1, d1, border, App.Vector(cx - w1 / 2, cy - d1 / 2, z1 - border))
    return front.fuse(back).fuse(low).fuse(high)


def plate_beam_xz(x0, z0, x1, z1, cy=0, width=28, thickness=12):
    dx, dz = x1 - x0, z1 - z0
    length = math.hypot(dx, dz)
    nx, nz = -dz / length * width / 2, dx / length * width / 2
    face = base.polygon_face([
        (x0 + nx, cy - thickness / 2, z0 + nz),
        (x1 + nx, cy - thickness / 2, z1 + nz),
        (x1 - nx, cy - thickness / 2, z1 - nz),
        (x0 - nx, cy - thickness / 2, z0 - nz),
    ])
    return face.extrude(App.Vector(0, thickness, 0))


def horizontal_beam(x0, x1, cy, z, depth=46, height=28):
    return Part.makeBox(x1 - x0, depth, height, App.Vector(x0, cy - depth / 2, z))


def add_group(doc, name, label):
    group = doc.addObject("App::DocumentObjectGroup", name)
    group.Label = label
    return group


def build_master():
    doc = App.newDocument("Lamina_Slender_Biped_v5")
    params = base.add_robot_parameters(doc)
    params.Label = "Lamina v5 image-aligned design parameters"
    params.ModelMaturity = "Image-aligned architecture CAD — not structurally validated or fabrication-ready"

    wood = add_group(doc, "WoodStructure", "Open laser-cut plywood truss structure")
    joints = add_group(doc, "JointHardware", "Standard purchased shafts and bearings")
    actuation = add_group(doc, "Actuation", "Proximal actuator and joint envelopes")
    tendons = add_group(doc, "TendonRouting", "Visible tendon-routing envelopes")
    sensors = add_group(doc, "Sensors", "Cameras force pads and contact surfaces")
    safety = add_group(doc, "Safety", "Rear E-stop and independent tether anchor")
    refs = add_group(doc, "References", "Reference geometry")

    # Feet: layered plywood, broad enough for a guarded standing prototype.
    for side, x in [("Left", -100), ("Right", 100)]:
        layers = []
        for i, (w, d) in enumerate(((165, 255), (160, 245), (152, 232))):
            layers.append(Part.makeBox(w, d, 12, App.Vector(x - w / 2, -125 - d / 2 + 20, 30 + i * 13)))
        foot = layers[0].fuse(layers[1]).fuse(layers[2])
        base.add_feature(doc, wood, side + "Foot", side + " layered plywood foot", foot, base.WOOD_LIGHT)
        ankle_bracket = truss_link_z(x, -2, 62, 105, 72, 66, 58, 60, 9, 10)
        base.add_feature(doc, wood, side + "AnkleBracket", side + " foot-to-ankle bracket", ankle_bracket, base.WOOD)
        sole = Part.makeBox(172, 265, 10, App.Vector(x - 86, -242, 20))
        base.add_feature(doc, sensors, side + "Sole", side + " rubber sole and force pad", sole, base.RUBBER)

    # Windowed front-and-back plywood trusses replace the blocky v4 limbs.
    for side, x in [("Left", -100), ("Right", 100)]:
        base.add_feature(doc, wood, side + "ShinTruss", side + " windowed shin truss", truss_link_z(x, 0, 150, 455, 58, 72, 80, 84, 10, 18), base.WOOD)
        base.add_feature(doc, wood, side + "ThighTruss", side + " windowed thigh truss", truss_link_z(x, 0, 515, 770, 76, 88, 102, 104, 10, 18), base.WOOD)
        base.add_joint(doc, wood, joints, actuation, side + "Ankle", x, 0, 120, 34, 72)
        base.add_joint(doc, wood, joints, actuation, side + "Knee", x, 0, 485, 43, 84)
        base.add_joint(doc, wood, joints, actuation, side + "HipPitch", x, 0, 800, 48, 98)
        base.add_feature(doc, actuation, side + "HipCrossAxis", side + " hip roll/yaw envelope", base.cylinder_x(x, 0, 800, 30, 86), base.CHARCOAL)

    # Open pelvis cage with proximal motor pack visible through it.
    pelvis_shapes = [
        horizontal_beam(-155, 155, 0, 760, 92, 26),
        horizontal_beam(-145, 145, 0, 855, 86, 28),
        plate_beam_xz(-145, 775, -118, 850, 0, 28, 12),
        plate_beam_xz(145, 775, 118, 850, 0, 28, 12),
        plate_beam_xz(-72, 775, -48, 850, 0, 22, 12),
        plate_beam_xz(72, 775, 48, 850, 0, 22, 12),
    ]
    pelvis = pelvis_shapes[0]
    for shape in pelvis_shapes[1:]:
        pelvis = pelvis.fuse(shape)
    base.add_feature(doc, wood, "PelvisCage", "Open plywood pelvis cage", pelvis, base.WOOD)
    base.add_feature(doc, actuation, "PelvisMotorBank", "Visible proximal leg motor bank", Part.makeBox(185, 78, 58, App.Vector(-92.5, -39, 790)), base.CHARCOAL)

    # Narrow open torso: spine, shoulder yoke, side rails, and diagonal braces.
    torso_shapes = [
        horizontal_beam(-190, 190, 0, 1170, 72, 34),
        horizontal_beam(-128, 128, 0, 925, 68, 28),
        horizontal_beam(-150, 150, 0, 1065, 62, 24),
        plate_beam_xz(-170, 1180, -120, 940, 0, 34, 12),
        plate_beam_xz(170, 1180, 120, 940, 0, 34, 12),
        plate_beam_xz(-62, 1190, -42, 920, 0, 30, 12),
        plate_beam_xz(62, 1190, 42, 920, 0, 30, 12),
        plate_beam_xz(-165, 1165, -50, 1065, -8, 24, 10),
        plate_beam_xz(165, 1165, 50, 1065, -8, 24, 10),
        plate_beam_xz(-132, 955, -45, 1065, -8, 24, 10),
        plate_beam_xz(132, 955, 45, 1065, -8, 24, 10),
    ]
    torso = torso_shapes[0]
    for shape in torso_shapes[1:]:
        torso = torso.fuse(shape)
    base.add_feature(doc, wood, "TorsoTruss", "Open image-aligned torso truss", torso, base.WOOD_LIGHT)
    base.add_feature(doc, wood, "Spine", "Laminated central spine", base.hollow_box(0, 22, 900, 72, 74, 330, 10), base.WOOD_EDGE)

    # Compact motor cylinders remain concentrated inside the torso.
    for row in range(3):
        for col in range(3):
            x = -48 + col * 48
            z = 970 + row * 78
            base.add_feature(doc, actuation, "TorsoMotor_%d_%d" % (row, col), "Torso tendon motor", base.cylinder_y(x, 8, z, 16, 70), base.CHARCOAL)

    # Windowed arms, compact joint housings, and adaptive hands.
    for side, x in [("Left", -225), ("Right", 225)]:
        base.add_feature(doc, wood, side + "UpperArmTruss", side + " windowed upper-arm truss", truss_link_z(x, 0, 930, 1145, 52, 64, 68, 76, 9, 16), base.WOOD)
        base.add_feature(doc, wood, side + "ForearmTruss", side + " windowed forearm truss", truss_link_z(x, -2, 690, 885, 46, 58, 58, 68, 9, 15), base.WOOD)
        base.add_joint(doc, wood, joints, actuation, side + "Shoulder", x, 0, 1180, 46, 86)
        base.add_joint(doc, wood, joints, actuation, side + "Elbow", x, 0, 905, 34, 70)
        base.add_joint(doc, wood, joints, actuation, side + "Wrist", x, -2, 665, 25, 58)
        palm = Part.makeBox(64, 30, 66, App.Vector(x - 32, -17, 585))
        base.add_feature(doc, wood, side + "Palm", side + " adaptive hand palm", palm, base.WOOD_LIGHT)
        for finger_i, dx in enumerate((-21, 0, 21)):
            finger = Part.makeBox(12, 20, 68, App.Vector(x + dx - 6, -15, 517))
            base.add_feature(doc, wood, side + "Finger%d" % finger_i, side + " adaptive finger", finger, base.WOOD_LIGHT)
            pad = Part.makeBox(12, 6, 30, App.Vector(x + dx - 6, -21, 528))
            base.add_feature(doc, sensors, side + "FingerPad%d" % finger_i, side + " compliant finger pad", pad, base.RUBBER)

    # Layered abstract head with a closed crown and camera apertures.
    base.add_feature(doc, actuation, "Neck", "Two-axis neck envelope", Part.makeCylinder(34, 74, App.Vector(0, 0, 1240)), base.CHARCOAL)
    for i in range(10):
        z = 1310 + i * 15
        phase = (i + 1) / 11
        rx = 54 + 32 * math.sin(math.pi * phase)
        ry = 50 + 25 * math.sin(math.pi * phase)
        ring_width = min(22, rx - 5, ry - 5)
        shape = base.ellipse_ring(0, -3, z, rx, ry, 6, ring_width)
        base.add_feature(doc, wood, "HeadRib%02d" % i, "Layered head rib", shape, base.WOOD_LIGHT)
    crown = base.ellipse_face(0, -3, 1460, 47, 42).extrude(App.Vector(0, 0, 6))
    base.add_feature(doc, wood, "HeadCrown", "Closed layered head crown", crown, base.WOOD_LIGHT)
    for x in (-24, 24):
        camera = Part.makeCylinder(8, 11, App.Vector(x, -77, 1385), App.Vector(0, -1, 0))
        base.add_feature(doc, sensors, "Camera%s" % ("L" if x < 0 else "R"), "Camera aperture", camera, base.CHARCOAL)

    # Visible tendon runs echo the image while remaining schematic envelopes.
    routes = [
        ((-42, 32, 1150), (-225, 26, 905)), ((42, 32, 1150), (225, 26, 905)),
        ((-35, 30, 1080), (-225, 22, 665)), ((35, 30, 1080), (225, 22, 665)),
        ((-55, 28, 830), (-100, 22, 485)), ((55, 28, 830), (100, 22, 485)),
        ((-35, 26, 805), (-100, 20, 120)), ((35, 26, 805), (100, 20, 120)),
    ]
    for i, (p0, p1) in enumerate(routes):
        base.add_feature(doc, tendons, "Tendon%02d" % i, "Visible tendon route", base.cylinder_between(p0, p1, 2.8), base.RUBBER)

    # Rear shoulder-level safety module, separately mounted from tether anchor.
    backing = Part.makeBox(92, 11, 78, App.Vector(-46, 105, 1155))
    base.add_feature(doc, safety, "EStopBacking", "Fixed rear E-stop backing", backing, base.CHARCOAL)
    base.add_feature(doc, safety, "EStopCollar", "E-stop yellow collar", Part.makeCylinder(30, 9, App.Vector(0, 116, 1194), App.Vector(0, 1, 0)), base.YELLOW)
    base.add_feature(doc, safety, "EStopButton", "Rear shoulder-level E-stop", Part.makeCylinder(23, 27, App.Vector(0, 125, 1194), App.Vector(0, 1, 0)), base.RED)
    anchor = Part.makeTorus(25, 6, App.Vector(0, 112, 1280), App.Vector(1, 0, 0), 0, 360, 360)
    base.add_feature(doc, safety, "TetherAnchor", "Separate upper-spine tether anchor", anchor, base.STEEL)

    floor = Part.makeBox(780, 620, 6, App.Vector(-390, -280, 0))
    base.add_feature(doc, refs, "Floor", "Reference floor", floor, (0.78, 0.78, 0.75), 82)

    doc.recompute()
    fcstd = os.path.join(OUT, "Lamina-Slender-Biped-v5.FCStd")
    doc.saveAs(fcstd)
    Part.export([o for o in base.solid_features(doc) if o.Name != "Floor"], os.path.join(OUT, "Lamina-Slender-Biped-v5.step"))
    print("Generated image-aligned v5: %s" % fcstd)


if __name__ == "__main__":
    build_master()

#!/usr/bin/env python3
"""Generate Lamina v0.6 URDF and joint map using only Python's standard library."""

from __future__ import annotations

import csv
import os
import xml.etree.ElementTree as ET


HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "generated")
os.makedirs(OUT, exist_ok=True)


def add_link(robot, name, mass=0.25, size=(0.08, 0.08, 0.08), color="wood"):
    link = ET.SubElement(robot, "link", {"name": name})
    inertial = ET.SubElement(link, "inertial")
    ET.SubElement(inertial, "origin", {"xyz": "0 0 0", "rpy": "0 0 0"})
    ET.SubElement(inertial, "mass", {"value": f"{mass:.4f}"})
    x, y, z = size
    ET.SubElement(inertial, "inertia", {
        "ixx": f"{mass*(y*y+z*z)/12:.6f}", "ixy": "0", "ixz": "0",
        "iyy": f"{mass*(x*x+z*z)/12:.6f}", "iyz": "0", "izz": f"{mass*(x*x+y*y)/12:.6f}",
    })
    for section in ("visual", "collision"):
        node = ET.SubElement(link, section)
        ET.SubElement(node, "origin", {"xyz": "0 0 0", "rpy": "0 0 0"})
        geometry = ET.SubElement(node, "geometry")
        ET.SubElement(geometry, "box", {"size": f"{x} {y} {z}"})
        if section == "visual":
            ET.SubElement(node, "material", {"name": color})
    return link


JOINT_ROWS = []


def add_joint(robot, name, parent, child, xyz, axis, lower, upper, effort, velocity, joint_class):
    joint = ET.SubElement(robot, "joint", {"name": name, "type": "revolute"})
    ET.SubElement(joint, "parent", {"link": parent})
    ET.SubElement(joint, "child", {"link": child})
    ET.SubElement(joint, "origin", {"xyz": " ".join(str(v) for v in xyz), "rpy": "0 0 0"})
    ET.SubElement(joint, "axis", {"xyz": " ".join(str(v) for v in axis)})
    ET.SubElement(joint, "limit", {
        "lower": str(lower), "upper": str(upper), "effort": str(effort), "velocity": str(velocity)
    })
    ET.SubElement(joint, "dynamics", {"damping": "0.5", "friction": "0.2"})
    JOINT_ROWS.append((name, parent, child, joint_class, lower, upper, effort, velocity))


def build():
    robot = ET.Element("robot", {"name": "lamina_v06"})
    ET.SubElement(robot, "material", {"name": "wood"}).append(ET.Element("color", {"rgba": "0.70 0.48 0.25 1"}))
    ET.SubElement(robot, "material", {"name": "dark"}).append(ET.Element("color", {"rgba": "0.08 0.10 0.12 1"}))

    add_link(robot, "pelvis", 8.0, (0.30, 0.20, 0.18))

    # Waist and torso.
    add_link(robot, "waist_yaw_link", 0.4, (0.10, 0.10, 0.06), "dark")
    add_joint(robot, "waist_yaw", "pelvis", "waist_yaw_link", (0, 0, 0.12), (0, 0, 1), -1.047, 1.047, 60, 1.0, "M")
    add_link(robot, "waist_roll_link", 0.4, (0.10, 0.10, 0.06), "dark")
    add_joint(robot, "waist_roll", "waist_yaw_link", "waist_roll_link", (0, 0, 0.04), (1, 0, 0), -0.524, 0.524, 50, 0.8, "M")
    add_link(robot, "torso", 7.0, (0.40, 0.22, 0.42))
    add_joint(robot, "waist_pitch", "waist_roll_link", "torso", (0, 0, 0.23), (0, 1, 0), -1.047, 0.785, 120, 0.8, "H")

    # Neck.
    add_link(robot, "neck_yaw_link", 0.2, (0.06, 0.06, 0.06), "dark")
    add_joint(robot, "neck_yaw", "torso", "neck_yaw_link", (0, 0, 0.27), (0, 0, 1), -1.571, 1.571, 8, 1.5, "S")
    add_link(robot, "head", 1.0, (0.17, 0.15, 0.20))
    add_joint(robot, "neck_pitch", "neck_yaw_link", "head", (0, 0, 0.10), (0, 1, 0), -0.524, 0.785, 8, 1.2, "S")

    # Arms.
    for side, sign in (("left", 1), ("right", -1)):
        shoulder = (sign * 0.24, 0, 0.20)
        add_link(robot, f"{side}_shoulder_yaw_link", 0.25, (0.06, 0.08, 0.06), "dark")
        add_joint(robot, f"{side}_shoulder_yaw", "torso", f"{side}_shoulder_yaw_link", shoulder, (0, 0, 1), -1.571, 1.571, 40, 1.2, "M")
        add_link(robot, f"{side}_shoulder_roll_link", 0.25, (0.06, 0.08, 0.06), "dark")
        add_joint(robot, f"{side}_shoulder_roll", f"{side}_shoulder_yaw_link", f"{side}_shoulder_roll_link", (0, 0, 0), (1, 0, 0), -1.571, 1.571, 40, 1.2, "M")
        add_link(robot, f"{side}_upper_arm", 1.0, (0.07, 0.09, 0.27))
        add_joint(robot, f"{side}_shoulder_pitch", f"{side}_shoulder_roll_link", f"{side}_upper_arm", (0, 0, -0.14), (0, 1, 0), -2.094, 2.094, 65, 1.2, "H")
        add_link(robot, f"{side}_forearm", 0.7, (0.06, 0.08, 0.24))
        add_joint(robot, f"{side}_elbow_pitch", f"{side}_upper_arm", f"{side}_forearm", (0, 0, -0.255), (0, 1, 0), 0, 2.356, 35, 1.5, "M")
        add_link(robot, f"{side}_wrist_yaw_link", 0.15, (0.05, 0.05, 0.05), "dark")
        add_joint(robot, f"{side}_wrist_yaw", f"{side}_forearm", f"{side}_wrist_yaw_link", (0, 0, -0.145), (0, 0, 1), -1.571, 1.571, 10, 2.0, "S")
        add_link(robot, f"{side}_hand", 0.4, (0.09, 0.05, 0.14))
        add_joint(robot, f"{side}_wrist_pitch", f"{side}_wrist_yaw_link", f"{side}_hand", (0, 0, -0.08), (0, 1, 0), -1.047, 1.047, 10, 2.0, "S")
        add_link(robot, f"{side}_gripper", 0.1, (0.10, 0.06, 0.06), "dark")
        add_joint(robot, f"{side}_grip", f"{side}_hand", f"{side}_gripper", (0, 0, -0.08), (1, 0, 0), 0, 1.0, 12, 2.0, "S")

    # Legs.
    for side, sign in (("left", 1), ("right", -1)):
        hip = (sign * 0.10, 0, -0.09)
        add_link(robot, f"{side}_hip_yaw_link", 0.35, (0.08, 0.09, 0.07), "dark")
        add_joint(robot, f"{side}_hip_yaw", "pelvis", f"{side}_hip_yaw_link", hip, (0, 0, 1), -0.785, 0.785, 60, 0.8, "H")
        add_link(robot, f"{side}_hip_roll_link", 0.35, (0.08, 0.09, 0.07), "dark")
        add_joint(robot, f"{side}_hip_roll", f"{side}_hip_yaw_link", f"{side}_hip_roll_link", (0, 0, 0), (1, 0, 0), -0.611, 0.611, 100, 0.8, "H")
        add_link(robot, f"{side}_thigh", 2.0, (0.10, 0.11, 0.31))
        add_joint(robot, f"{side}_hip_pitch", f"{side}_hip_roll_link", f"{side}_thigh", (0, 0, -0.16), (0, 1, 0), -2.094, 0.785, 120, 0.8, "H")
        add_link(robot, f"{side}_shank", 1.5, (0.08, 0.09, 0.34))
        add_joint(robot, f"{side}_knee_pitch", f"{side}_thigh", f"{side}_shank", (0, 0, -0.32), (0, 1, 0), 0, 2.356, 120, 1.0, "H")
        add_link(robot, f"{side}_ankle_pitch_link", 0.25, (0.07, 0.08, 0.06), "dark")
        add_joint(robot, f"{side}_ankle_pitch", f"{side}_shank", f"{side}_ankle_pitch_link", (0, 0, -0.20), (0, 1, 0), -0.785, 0.524, 100, 1.0, "H")
        add_link(robot, f"{side}_foot", 0.8, (0.16, 0.26, 0.06))
        add_joint(robot, f"{side}_ankle_roll", f"{side}_ankle_pitch_link", f"{side}_foot", (0, -0.04, -0.05), (1, 0, 0), -0.436, 0.436, 50, 1.0, "M")

    tree = ET.ElementTree(robot)
    ET.indent(tree, space="  ")
    tree.write(os.path.join(OUT, "lamina-v06.urdf"), encoding="utf-8", xml_declaration=True)
    with open(os.path.join(OUT, "joint-map.csv"), "w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(("joint", "parent", "child", "class", "lower_rad", "upper_rad", "effort_nm", "velocity_rad_s"))
        writer.writerows(JOINT_ROWS)
    print("Generated %d controlled joints." % len(JOINT_ROWS))


if __name__ == "__main__":
    build()


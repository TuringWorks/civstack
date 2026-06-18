# Joint Taxonomy and Axis Map

## Reusable classes

| Class | Continuous output target | Short peak target | Typical sector radius | Assigned use |
|---|---:|---:|---:|---|
| S | 5 N·m | 12 N·m | 35–50 mm | Neck, wrists, grippers |
| M | 20 N·m | 40 N·m | 60–80 mm | Elbows, shoulder yaw/roll, waist yaw/roll, ankle roll |
| H | 60 N·m | 120 N·m | 90–130 mm | Shoulder pitch, waist pitch, hips, knees, ankle pitch |

J1 is an M-class architecture experiment. H-class joints require a scaled J2 proof rig after J1 establishes tendon, bearing, wood, sensing, and control behavior.

## Axis inventory

| Region | Axes | Class | Count |
|---|---|---|---:|
| Neck | yaw, pitch | S | 2 |
| Waist | yaw, roll | M | 2 |
| Waist | pitch | H | 1 |
| Each arm | shoulder yaw, shoulder roll | M | 4 total |
| Each arm | shoulder pitch | H | 2 total |
| Each arm | elbow pitch | M | 2 total |
| Each arm | wrist yaw, wrist pitch | S | 4 total |
| Each hand | adaptive grip | S | 2 total |
| Each leg | hip yaw, hip roll, hip pitch | H | 6 total |
| Each leg | knee pitch | H | 2 total |
| Each leg | ankle pitch | H | 2 total |
| Each leg | ankle roll | M | 2 total |
| **Total** |  |  | **31** |

## Common requirements for all classes

- Output-side position sensing.
- Current/effort estimate and temperature sensing.
- Mechanical hard stops and software limits.
- Replaceable wooden cheeks and tendon guides.
- Standard shaft and bearing sizes within each class.
- Accessible tension adjustment and witness marks.
- Captive fasteners or retention strategy appropriate to vibration.
- Safe state defined for power loss, tendon failure, encoder fault, and overtemperature.


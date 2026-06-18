# Lamina Simulation Baseline

The simulation package represents Lamina as a 31-axis humanoid with simplified collision and inertial geometry. It is intended for kinematic validation, joint-limit review, controller scaffolding, support-polygon studies, and interface testing.

## Artifacts

- `generate_urdf.py` — authoritative generator.
- `generated/lamina-v06.urdf` — generated robot description.
- `generated/joint-map.csv` — joint names, classes and limits.
- `validate.sh` — XML and axis-count validation.

## Important limitations

- Inertial values are planning estimates, not measured CAD mass properties.
- Tendon elasticity, backlash, structural flex, cable routing and motor dynamics are not modeled.
- Collision geometry is deliberately conservative and simplified.
- The model must not be used to claim walking, stair or ladder capability.

## Recommended simulation progression

1. Static URDF inspection and joint-limit sweep.
2. Self-collision checking.
3. Quasi-static squat with both feet fixed.
4. Center-of-mass transfer inside the support polygon.
5. Suspended stepping with ideal position actuators.
6. Add effort, velocity, delay, backlash and tendon-compliance models.
7. Stair contact sequence.
8. Ladder contact sequence with positive rung hooks and simulated power loss.


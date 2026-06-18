# Lamina J1 Tendon Joint Test Rig

This package is the Phase‑0 physical prototype for the Lamina humanoid. It isolates the highest-risk mechanical ideas—laser-cut plywood structure, standard bearings and shaft, tendon transmission, joint sensing, hard stops, and safe motor shutdown—before they are multiplied across a complete robot.

## What it tests

- Replaceable plywood cheek and link plates
- A standard 12 mm shaft and two standard 6001 bearings
- Bidirectional low-stretch tendon transmission
- A 150 mm laminated sector pulley
- A remote actuator/capstan mounted to a replaceable motor plate
- Independent joint-angle measurement
- Backlash, creep, tendon wear, thermal behavior, and emergency stop

The default design case is a 5 kg test mass acting 300 mm from the pivot: 14.7 N·m static torque and approximately 22 N·m proof torque at 1.5×. This is a test-rig load case, not a final humanoid knee rating.

## Package map

- [Requirements and calculations](requirements.md)
- [Hardware BOM](hardware/bom.csv)
- [Wiring and safety chain](electronics/wiring.md)
- [Firmware interface](firmware/interface.md)
- [Acceptance test](tests/acceptance-test.md)
- [FreeCAD workflow](cad/README.md)

## Build order

1. Laser-cut the dimension and fit coupon before cutting the rig.
2. Confirm actual plywood thickness, 12 mm shaft clearance, bearing-pocket fit, and laser kerf.
3. Cut and dry-assemble the base, uprights, link, bearing retainers, sector pulley, capstan, spacers, and motor plate.
4. Install bearings, shaft, mechanical hard stops, and joint encoder before adding the motor.
5. Wire the fused supply, drive-enable contactor, E-stop, controller, and sensors.
6. Commission without tendon, then without load, then with guarded incremental loads.

## Safety boundary

Bench-mount the base. Guard the tendon, capstan, sector pulley, and pinch zones. Never use a person as the load. The E-stop must remove actuator enable independently of firmware.


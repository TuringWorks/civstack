# J1 Requirements and First-Pass Calculations

## Geometry

| Parameter | Initial value |
|---|---:|
| Joint range | −10° to 110° |
| Pivot shaft | 12 mm diameter × 160 mm |
| Bearings | 6001-2RS, 12 × 28 × 8 mm |
| Link length, pivot to load holes | 300 mm nominal |
| Sector working radius | 75 mm |
| Motor capstan working radius | 30 mm |
| Structural plywood | 12 mm |
| Laminated pulley plywood | 6 mm |
| Rig cheek separation | 100 mm nominal |

## Load case

For a 5 kg test mass at a 0.30 m horizontal moment arm:

`joint torque = 5 kg × 9.81 m/s² × 0.30 m = 14.7 N·m`

At a 1.5× guarded proof factor:

`proof torque = 22.1 N·m`

At a 75 mm sector radius, ignoring losses:

`proof tendon force = 22.1 N·m / 0.075 m = 294 N`

At a 30 mm motor capstan radius:

`required capstan torque = 294 N × 0.030 m = 8.8 N·m`

The selected actuator and reduction must therefore provide at least 6 N·m continuous and 9 N·m short-duration output at the capstan for this test case. Derate further for pulley friction, tendon bending, acceleration, counterbalance error, and thermal limits.

## Design requirements

1. No custom metal machining; shafts, bearings, bolts, motor, reduction, springs, and electrical parts are purchased standard items.
2. All wooden structural parts are replaceable without discarding the shaft, bearings, motor, or sensors.
3. The joint encoder measures the output shaft, not merely the motor shaft.
4. Adjustable physical stops act before tendon, cable, or shell interference.
5. Tendon tension can be adjusted without disassembling the pivot.
6. The motor mount is replaceable so actuator families can change.
7. Bearing seats are finalized only after cutting the fit coupon in the actual plywood batch.
8. The E-stop removes drive enable through hardware and cannot be reset by software.
9. All moving tests use a fixed bench base and transparent guarding.

## Not yet established

- Final humanoid knee or elbow torque
- Long-term plywood fatigue and humidity derating
- Tendon termination efficiency and service interval
- Required actuator family and reduction
- Noise target and acceptable backlash
- Final joint speed and regenerative braking strategy


# Stair and Ladder State Machines

## Stair ascent

`APPROACH → REGISTER_STEP → DOUBLE_SUPPORT → LIFT_LEAD_FOOT → PLACE_LEAD_FOOT → VERIFY_CONTACT → TRANSFER_COM → LIFT_TRAIL_FOOT → PLACE_TRAIL_FOOT → DOUBLE_SUPPORT`

Abort to supported stop if step registration, foot clearance, contact force, center-of-pressure margin, joint margin, tendon force, or tether status becomes invalid.

## Ladder ascent

Maintain at least three verified contacts.

`REGISTER_LADDER → GRIP_TWO_HANDS → PLACE_LEAD_FOOT → VERIFY_THREE_CONTACTS → MOVE_TRAIL_FOOT → VERIFY_FOUR_CONTACTS → MOVE_LEAD_HAND → VERIFY_THREE_CONTACTS → MOVE_TRAIL_HAND`

Requirements:

- Positive mechanical rung hook; friction grip alone is insufficient.
- Independent sensing for each hand and foot contact.
- Fall-arrest tether carries the robot after any unexpected contact loss.
- No simultaneous release of two contacts.
- Power-loss behavior must preserve or mechanically catch at least one upper contact while the tether arrests the fall.
- Descent is validated separately; ascent success does not imply safe descent.

## Fault injections required before progression

- Stale contact sensor.
- False-positive contact.
- One tendon failure.
- One actuator disabled.
- Camera loss.
- Network loss.
- E-stop at every transition.
- Battery undervoltage during load-bearing contact.


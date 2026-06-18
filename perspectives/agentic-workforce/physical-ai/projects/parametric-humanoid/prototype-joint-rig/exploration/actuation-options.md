# Actuation Architecture Trade Study

| Option | Cost | Mass distribution | Bidirectional stiffness | Energy use while holding | Complexity | Ladder/climbing relevance |
|---|---|---|---|---|---|---|
| One motor, opposing tendons | Low–medium | Excellent; motor remains proximal | Good if preload is stable | Depends on motor/reduction and brake | Moderate | Recommended first rig |
| Two antagonistic motors | High | Poorer; two motors per axis | Excellent and actively adjustable | High unless brakes/counterbalance are used | High | Useful research option, too costly for baseline |
| One tendon plus return spring | Lowest | Excellent | Unequal by direction and pose | Low in spring-assisted direction | Low | Poor for reversible load-bearing joints |
| Motor mounted at joint | Medium | Poor distal mass | Good | Depends on gearing | Lowest mechanical complexity | Useful control baseline; conflicts with slender limbs |
| Linear actuator and linkage | Medium | Moderate | High | Often favorable with self-locking drive | Moderate | Attractive for knees/hips, less suitable for shoulders/wrists |

## Recommended J1A configuration

- One closed-loop motor with at least 6 N·m continuous and 9 N·m short-duration output at the capstan.
- Two 2 mm low-stretch tendons wound in opposite directions.
- 30 mm capstan radius and 75 mm sector radius.
- Separate threaded tension adjuster for each tendon.
- Independent output-shaft encoder.
- Mechanical hard stops and normally closed limit switches.
- Optional counterbalance spring added only after the unassisted torque curve is measured.

## Decision gates

Retain J1A only if:

- Backlash is ≤3° under the representative load.
- Tendon tension remains positive through the full range.
- Terminations survive at least twice the maximum configured operating force.
- Retensioning does not shift encoder zero or require joint disassembly.
- Thermal tests meet the intended duty cycle with documented derating.


# Safety State Machine

This is an implementation contract, not a completed safety certification.

## States

| State | Drives | Accepted actions |
|---|---|---|
| `POWER_OFF` | De-energized | Power-on self-test |
| `SELF_TEST` | Disabled | Sensor, bus, configuration, E-stop checks |
| `SAFE_IDLE` | Enabled or braked at low authority | Home, enter run, power down |
| `HOMING` | Limited speed/effort | Cancel, safe stop |
| `RUN` | Within configured limits | Certified skills, hold, safe stop |
| `PROTECTIVE_STOP` | Controlled stop/hold | Diagnose; operator reset when safe |
| `EMERGENCY_STOP` | Hardware drive enable removed | Physical E-stop release and supervised reset |
| `FAULT_LOCKOUT` | Disabled | Maintenance diagnosis and supervised reset |
| `MAINTENANCE` | One-axis jog at reduced limits | Jog, calibrate, power down |

## Mandatory transitions

- Any state → `EMERGENCY_STOP`: safety-chain opens.
- Any energized state → `PROTECTIVE_STOP`: heartbeat expires, perception becomes unsafe, noncritical joint fault, command conflict, or workspace violation.
- Any state → `FAULT_LOCKOUT`: overtemperature, encoder disagreement, hard-limit activation, configuration mismatch, repeated bus error, or unsafe restart condition.
- `PROTECTIVE_STOP` → `SAFE_IDLE`: hazard cleared, physical area checked, and authorized operator acknowledges.
- `EMERGENCY_STOP` → `SELF_TEST`: E-stop physically released and operator initiates reset. Never transition directly to `RUN`.

## Invariants

1. Boot never enables motion automatically.
2. No reset command is accepted from the language interface.
3. Every motion command has a deadline and sequence number.
4. Missing setpoints cause a stop, never replay of an old trajectory.
5. Limit, current, temperature, and watchdog enforcement remain active in maintenance mode.
6. A fault reason is latched before actuator power is removed where electrically possible.
7. Restart after power loss requires a new self-test and homing decision.
8. The rear shoulder-level E-stop and commissioning-pendant stop are tested before entering `HOMING` or `RUN`.

## Suggested initial limits

These are conservative placeholders to be replaced by measured limits:

- Joint speed: 10–20 degrees/second during first powered tests
- Joint acceleration: 20–40 degrees/second²
- Skill duration: 10 seconds maximum unless explicitly certified
- Brain heartbeat timeout: 250 ms
- Setpoint timeout at MCU: 50 ms
- Perception target age: 100 ms for tracking, 500 ms for stationary gestures
- Maintenance jog: hold-to-run control only

# Firmware Interface

## Control partition

- Motor driver closes its internal current/commutation loop.
- Real-time MCU closes output-joint position and velocity control using the independent shaft encoder.
- Test host requests bounded modes and setpoints; it never sends PWM or arbitrary executable code.
- Hardware safety removes drive enable independently.

## Initial rates

| Loop | Rate |
|---|---:|
| Encoder acquisition and limit checks | 1 kHz |
| Output position/velocity loop | 500 Hz |
| Load-cell and temperature acquisition | 100 Hz |
| Host command and telemetry | 50 Hz |
| Log persistence | 20–50 Hz |

## States

`POWER_OFF → SELF_TEST → SAFE_IDLE → HOMING → RUN`

Any state may transition to `EMERGENCY_STOP` or `FAULT_LOCKOUT`. Heartbeat expiry, stale setpoint, limit activation, encoder disagreement, overtemperature, or excessive tendon force transitions to `PROTECTIVE_STOP`.

## Host command envelope

```json
{
  "version": "0.1",
  "sequence": 42,
  "mode": "position_test",
  "target_deg": 30.0,
  "max_velocity_deg_s": 10.0,
  "max_acceleration_deg_s2": 20.0,
  "max_tendon_force_n": 350.0,
  "expires_ms": 100
}
```

Reject unknown fields, stale sequence numbers, expired commands, targets outside calibrated limits, or commands received outside `RUN`.

## Required telemetry

- Monotonic timestamp and sequence
- State and latched fault reason
- Output angle and velocity
- Motor position if available
- Commanded and measured tendon force
- Motor current and temperature
- Joint/bearing-area temperature
- Limit switches, E-stop, deadman, and drive-enable feedback
- Controller, firmware, and configuration versions


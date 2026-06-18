# J1 Acceptance Test

## Preconditions

- Base through-bolted to a rigid bench.
- Polycarbonate guard installed.
- E-stop and hold-to-run pendant verified with motor uncoupled.
- Shaft collars, locknuts, tendon terminations, hard stops, and strain relief inspected.
- No person inside the swing or tendon-failure envelope.
- Current, speed, acceleration, temperature, and tendon-force limits configured conservatively.

## Test sequence

| Stage | Method | Pass condition |
|---|---|---|
| Fit coupon | Cut holes/slots in actual sheet | Shaft clears; bearing fit and fastener holes documented |
| Unpowered sweep | Move link by hand through full range | No binding, cable contact, or structural interference |
| Safety chain | Open E-stop and deadman separately | Drive enable is physically removed and fault is logged |
| Encoder | Compare commanded angles to independent reference | Error ≤2° throughout initial range |
| No-load motion | Ten cycles at 5°/s, then ten at 10°/s | No oscillation, skipped motion, or limit violation |
| Backlash | Reverse slowly under a small constant load | Output deadband ≤3° or redesign is triggered |
| Incremental load | Increase guarded mass in 1 kg steps | Stable control and no progressive deformation |
| Proof hold | Hold 1.5× design torque for 60 seconds | No crack, delamination, fastener movement, or permanent set |
| Thermal duty | Run intended duty cycle for 30 minutes | Components remain below manufacturer limits and recorded derating |
| Initial endurance | 500 full-range cycles | No loosening, tendon damage, bearing migration, or calibration drift |
| Extended endurance | 10,000 representative cycles | Wear rate supports a documented service interval |
| Power/host loss | Disconnect host and command heartbeat | Protective stop occurs before timeout; no stale command replay |

## Stop immediately if

- Wood cracks, delaminates, emits new creaking, or shows bearing-seat movement.
- Tendon strands fuzz, flatten, slip, or change tension unexpectedly.
- Fasteners rotate or witness marks move.
- Encoder and motor estimates disagree beyond the configured threshold.
- Temperature, current, force, vibration, or noise rises unexpectedly.
- Any guard, E-stop, limit, or watchdog is unavailable.

## Evidence to retain

Photographs before and after testing, plywood batch/thickness, kerf coupon, CAD/configuration hash, actuator/driver versions, torque calculations, telemetry logs, failure photographs, maintenance actions, and revised service limits.


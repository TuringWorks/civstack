# Lamina Preliminary Safety Case

## Top claim

Lamina may be operated only in its approved development configuration and operating design domain when the listed controls, inspections, supervision, exclusion zones, fall arrest, logging, and test evidence are present.

This is a preliminary argument structure, not a certification.

## Safety claims

### S1 — Actuation can be made safe independently of intelligent software

- Latching E-stop opens an independent drive-enable chain.
- Commissioning pendant requires hold-to-run.
- Contactors/drive enables report their actual state.
- Stale setpoints and heartbeat loss cause protective stop.
- Language and planning processes cannot reset faults or energize drives directly.

### S2 — Fall consequences are controlled during mobility development

- Overhead fall arrest is rated and independently anchored.
- Standing, stepping, stair and ladder tests occur inside exclusion zones.
- Test progression is gated by lower-risk evidence.
- No person is used to catch, steady or load the robot.

### S3 — Structural degradation is detected before hazardous use

- Plywood batch, thickness, grain and finish are documented.
- Witness marks expose fastener movement.
- Pre-run inspection checks cracks, delamination, bearing migration, tendon wear and moisture damage.
- Proof and endurance testing establishes service intervals.
- Load-bearing wooden parts are replaceable and life-tracked.

### S4 — Contact motion remains bounded

- Output encoders, current/force estimates, hard stops, joint limits and contact sensors constrain motion.
- Center-of-pressure and contact-mode uncertainty trigger protective stop.
- Ladder operation preserves three verified contacts and positive mechanical hooks.
- Gripper power loss does not rely solely on friction to retain a rung.

### S5 — Electrical and battery hazards are contained

- Certified battery/BMS, service disconnect, precharge, main contactor and selective fusing.
- Battery is thermally separated from plywood.
- Charging occurs in a designated monitored area.
- Branch current, temperature, undervoltage and welded-contact states are monitored.

## Required evidence before energized full-body testing

- Closed hardware gates G1–G8.
- Approved hazard register with named owners.
- Signed pre-run checklist and exclusion-zone setup.
- Configuration-controlled firmware, CAD, limits and wiring.
- Successful E-stop, deadman, watchdog and power-loss tests.
- Fall-arrest inspection and load rating.
- Incident and near-miss process.


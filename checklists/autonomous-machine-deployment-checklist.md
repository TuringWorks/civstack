# Autonomous Machine Deployment Checklist

Use before deploying autonomous vehicles, drones, farm equipment, loaders, harvesters, AMRs, vessels, rail, or other non-humanoid physical AI. Pairs with `skills/_catalogs/autonomous-machines/`, `skills/_catalogs/autonomous-fleet-ops/`, and the capability routing matrix (`docs/capability-routing-matrix.md`).

## Mission and ownership

- [ ] Mission is defined.
- [ ] Human accountable owner is named.
- [ ] Operating site or route is defined.
- [ ] Affected people, workers, animals, property, crops, and environment are identified.
- [ ] Legal / regulatory constraints are documented (road approval, airspace/BVLOS, mine/site rules).

## Operating Design Domain (ODD)

- [ ] Geography / geofence approved.
- [ ] Route / map / field boundary verified and current.
- [ ] Weather limits defined.
- [ ] Lighting / visibility limits defined.
- [ ] Speed and payload limits defined.
- [ ] Terrain / surface limits defined.
- [ ] Human / animal interaction rules defined.

## Machine readiness

- [ ] Sensors calibrated.
- [ ] Localization validated.
- [ ] Brakes / actuators / implements inspected.
- [ ] Emergency stop tested.
- [ ] Remote intervention (teleop) tested.
- [ ] Safe-stop / minimal-risk-maneuver behavior tested.
- [ ] Cybersecurity controls active.
- [ ] Software / model version logged.

## Operations

- [ ] Mission plan reviewed.
- [ ] Remote-operator coverage assigned.
- [ ] Communications tested (and link-loss behavior verified).
- [ ] Exclusion zones marked.
- [ ] Worker briefing completed.
- [ ] Incident-response plan available.
- [ ] Maintenance plan ready.
- [ ] Data logging enabled.

## Post-mission

- [ ] Telemetry, disengagements, and near-misses reviewed.
- [ ] Incidents logged and root-caused.
- [ ] ODD / safety case updated from what was learned.
- [ ] Maintenance and recalibration scheduled as needed.

## Accountability boundary

- [ ] Use-of-force, life-safety, and irreversible decisions remain human-led.
- [ ] The verified safety layer can override the planning brain independently.
- [ ] Human override and stop authority are confirmed working.

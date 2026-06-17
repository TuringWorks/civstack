# Physical AI — Safety & Accountability Boundaries

A consolidated reference for the safety controls, human-accountable decisions, and stop conditions that apply to **non-humanoid autonomous machines** (vehicles, drones, farm/heavy equipment, AMRs, vessels, rail, fixed cells). Imported/adapted from Agentic-Workforce. Pairs with the deployment checklist (`../checklists/autonomous-machine-deployment-checklist.md`) and `skills/_catalogs/autonomous-fleet-ops/`.

## Human-accountable decisions (never delegated to the machine)

- Operating Design Domain (ODD) approval.
- Public-road or public-airspace deployment.
- Worker and bystander safety acceptance.
- Route / geofence authorization.
- Emergency response and incident disclosure.
- Use near children, patients, animals, crowds, traffic, or hazardous sites.
- Chemical application, pesticide use, controlled substances, weapons, and regulated cargo.
- Final approval of construction, mining, utility, rail, aviation, or maritime safety cases.

## Required safety controls (must be present and tested)

- Geofence or approved route.
- Speed and payload limits.
- Perception health checks.
- Remote monitoring and intervention (teleop).
- Emergency stop.
- Safe-stop / minimal-risk-maneuver fallback.
- Black-box event recording.
- Pre-shift inspection.
- Maintenance lockout.
- Cybersecurity controls.
- Weather and visibility limits.
- Human/animal detection and exclusion zones.
- Incident investigation process.

## Stop conditions (trigger a minimal-risk maneuver)

- Sensor degradation.
- Localization uncertainty.
- Human or animal in an exclusion zone.
- Lost communications beyond the allowed autonomy window.
- Weather outside limits.
- Unknown obstacle.
- Unmapped route or field boundary.

## How this connects

The verified safety layer that enforces these (independently of the planning brain) is owned by the **ODD & safety-case engineer** and the **fleet safety officer** in `skills/_catalogs/autonomous-fleet-ops/` and `skills/_catalogs/embodied-ai-stack/`. The roles that watch the human/machine boundary in real time are the **safety-zone monitor**, **perception-failure analyst**, and **route & geofence risk analyst**.

# Commissioning and operating envelope

## Commissioning sequence

1. Inspect structure, guards, hard stops, tendon routing and fastener witness marks.
2. Verify protective earth, fusing, insulation, polarity and contactor operation with motors disabled.
3. Validate both E-stop channels and loss-of-communications shutdown.
4. Commission one joint at reduced voltage/current; confirm encoder sign before closing the loop.
5. Increase limits only from logged evidence; never begin with full current or speed.
6. Test suspended, then lightly loaded, then proof-loaded, then integrated.
7. Repeat fault injection after every control, power or safety-chain revision.

## Operating rules

- Controlled indoor lab, dry floor, trained operator, cleared exclusion zone.
- Rear shoulder E-stop unobstructed; remote stop held by a second person for locomotion.
- Tether attached for all balance, stair and ladder development.
- No people inside reach during autonomous motion; no children or public operation.
- No ladder trial without a dedicated fixture, overhead restraint and reviewed escape plan.
- Stop on smoke, odor, delamination, tendon fray, abnormal sound, thermal limit,
  tracking error, stale command, sensor disagreement or unexpected contact.

## Data to retain

Joint position/current/temperature, bus voltage, controller state, fault reason,
command source, software/configuration revision and synchronized video. A test with
missing provenance is exploratory and cannot close a verification requirement.


# Design Decisions v0.6

| ID | Decision | Reason | Revisit trigger |
|---|---|---|---|
| D-01 | Plywood carries structural shell/link loads; decorative ribs remain removable | Preserves local fabrication and repairability | Proof/fatigue tests fail or mass exceeds budget |
| D-02 | No custom metal machining | Maintains accessibility | Safety-critical shaft interface cannot be achieved with standard parts |
| D-03 | Purchased shafts, bearings, motors, springs, fasteners, battery and electronics are allowed | Wood cannot practically replace these high-cycle functions | A lower-cost validated standard alternative appears |
| D-04 | Three reusable joint classes: S, M and H | Reduces unique parts, firmware variants and spares | Load budget shows a class cannot cover assigned axes |
| D-05 | Proximal motor banks and tendon transmission are the preferred baseline | Reduces distal limb mass and preserves slender form | J1 shows unacceptable backlash, wear, noise or service burden |
| D-06 | J1A uses one motor with opposing tendons | Lowest-cost bidirectional experiment | Preload cannot remain stable through range |
| D-07 | 31 controlled axes | Minimum functional envelope for target mobility/manipulation | Cost or mass requires eliminating wrist/waist axes |
| D-08 | 48 V main power domain | Keeps current manageable at multi-kilowatt peaks | Selected actuators require another standard domain |
| D-09 | Deterministic real-time control below a typed skill gateway | Language models are unsuitable for torque/stability loops | Never relaxed for safety-critical motion |
| D-10 | Walking precedes stairs; stairs precede ladder climbing | Each stage adds contact and fall complexity | Never bypassed by demonstration pressure |
| D-11 | Overhead fall arrest is mandatory during standing mobility development | Limits consequence of controller or structural failure | Removal requires a separately approved safety case |
| D-12 | Rear upper-back E-stop is the primary on-body stop | Reachable and clear of the robot's hands | Reachability testing shows another location is superior |
| D-13 | FreeCAD is the primary mechanical source | Installed, inspectable and scriptable locally | Team standard changes |
| D-14 | Rendered images are concept targets, not manufacturing evidence | Prevents visual inference from masquerading as engineering | Never removed |


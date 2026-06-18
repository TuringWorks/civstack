# Lamina Engineering Baseline v0.6

This folder is the integrated pre-fabrication engineering baseline for Lamina. It reconciles the concept images, FreeCAD architecture, J1 test rig, control boundary, safety philosophy, and low-cost fabrication strategy.

## Baseline documents

- [System requirements](system-requirements.md)
- [Design decisions](design-decisions.md)
- [Joint taxonomy](joint-taxonomy.md)
- [Mass budget](mass-budget.csv)
- [Joint load budget](joint-load-budget.csv)
- [Power budget](power-budget.csv)
- [Hardware-gated decisions](hardware-gates.md)

## Definition of pre-fabrication complete

The project is pre-fabrication complete when:

1. Product envelope, operating domain, payload, mobility, safety, runtime, and budget requirements are explicit.
2. Every controlled axis maps to a joint class, torque envelope, sensor, controller, and safe state.
3. Mass, torque, power, thermal, communication, and compute budgets reconcile at system level.
4. Native CAD, simulation kinematics, interfaces, manufacturing rules, assembly instructions, safety analysis, and verification matrix are present and internally consistent.
5. Every unresolved decision is tied to a named physical test with pass/fail criteria.
6. No document presents untested ladder climbing, human contact, payload, fatigue life, or autonomous walking as validated.

This boundary does not include physical proof, fatigue, gait, stair, ladder, EMC, battery, fire, or human-safety validation.


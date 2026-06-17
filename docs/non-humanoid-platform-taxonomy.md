# Non-Humanoid Physical AI — Platform Taxonomy & Selection Heuristics

A quick reference for choosing the right *physical form* for a job: humanoid vs non-humanoid mobile vs fixed automation. Imported/adapted from Agentic-Workforce. Pairs with `skills/_catalogs/autonomous-machines/`, `skills/_catalogs/humanoid-robots/`, and the capability routing matrix (`capability-routing-matrix.md`).

## Platform taxonomy

| Platform | Primary jobs | Best environments | Typical human owner |
|---|---|---|---|
| Autonomous road vehicle | Move people/goods on roads | mapped roads, depots, fixed routes | fleet safety operator |
| Autonomous truck | Long-haul, yard, drayage, hub-to-hub freight | highways, ports, logistics corridors | freight autonomy lead |
| Autonomous shuttle/bus | Public or campus mobility | campuses, airports, transit loops | transit operations lead |
| Autonomous farm tractor | Tillage, planting, spraying, hauling | farms, orchards, controlled fields | farm autonomy manager |
| Autonomous harvester | Harvest with crop-specific heads | fields, orchards, vineyards | harvest operations lead |
| Autonomous sprayer | Apply inputs precisely | fields, orchards, greenhouses | agronomy operations lead |
| Agricultural drone | Scouting, spraying, seeding, mapping | farms, forests, wetlands | drone operations lead |
| Inspection drone | Visual/thermal/IR inspection | utilities, roofs, bridges, pipelines | inspection program lead |
| Delivery drone | Small-payload delivery | defined corridors, campuses, remote areas | logistics drone fleet lead |
| Warehouse AMR | Move goods inside facilities | warehouses, hospitals, factories | warehouse automation lead |
| Autonomous forklift | Pallet movement | warehouses, ports, factories | material-handling safety lead |
| Autonomous loader | Move bulk material | mines, quarries, construction, ports | heavy-equipment autonomy lead |
| Autonomous excavator/dozer | Earthmoving, grading, trenching | construction, mining, disaster sites | site autonomy superintendent |
| Autonomous haul truck | Move ore, aggregate, soil, freight | mines, quarries, industrial sites | mine autonomy manager |
| Autonomous rail/metro | Move people/goods on rails | rail corridors, metros, yards | rail operations authority |
| Autonomous vessel (USV) | Marine inspection, cargo, survey, patrol | ports, rivers, offshore, coastal | marine autonomy lead |
| Underwater robot (ROV/AUV) | Inspect, map, repair underwater assets | ports, pipelines, cables, dams | subsea operations lead |
| Fixed robotic cell | Repeatable industrial manipulation | factories, labs, warehouses | automation engineering lead |

## Selection heuristics (which form for the job)

- **Humanoid** when the environment is built for humans and cannot be redesigned (stairs, doors, human tools, mixed human spaces).
- **Non-humanoid mobile machine** when the task has a specialized motion, payload, tool, route, or environment (wheels, tracks, rotors, implements, loaders, harvest heads, vessels).
- **Fixed automation** when the work can be brought to the machine (parts flow to a guarded cell).
- **Autonomous mobile robot (AMR)** when the machine must move through a facility or field but the task is bounded.
- **Remote-supervised autonomy** when edge cases are frequent and safety consequences are high (a teleoperator covers the long tail).

Then size the *brain* and *training method* with the capability routing matrix, and gate deployment with the [autonomous-machine deployment checklist](../checklists/autonomous-machine-deployment-checklist.md).

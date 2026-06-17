# Non-Humanoid Physical AI Taxonomy

| Platform | Primary jobs | Best environments | Human owner |
|---|---|---|---|
| Autonomous road vehicle | Move people/goods on roads | mapped roads, depots, fixed routes | fleet safety operator |
| Autonomous truck | Long-haul, yard, drayage, hub-to-hub freight | highways, ports, logistics corridors | freight autonomy lead |
| Autonomous shuttle/bus | Public or campus mobility | campuses, airports, transit loops | transit operations lead |
| Autonomous farm tractor | Tillage, planting, spraying, hauling | farms, orchards, controlled fields | farm autonomy manager |
| Autonomous harvester | Harvest crops with crop-specific heads | fields, orchards, vineyards | harvest operations lead |
| Autonomous sprayer | Apply inputs precisely | fields, orchards, greenhouses | agronomy operations lead |
| Agricultural drone | Scouting, spraying, seeding, mapping | farms, forests, wetlands | drone operations lead |
| Inspection drone | Visual/thermal/infrared inspection | utilities, roofs, bridges, pipelines | inspection program lead |
| Delivery drone | Small payload delivery | defined corridors, campuses, remote areas | logistics drone fleet lead |
| Warehouse AMR | Move goods inside facilities | warehouses, hospitals, factories | warehouse automation lead |
| Autonomous forklift | Pallet movement | warehouses, ports, factories | material handling safety lead |
| Autonomous loader | Move bulk material | mines, quarries, construction, ports | heavy equipment autonomy lead |
| Autonomous excavator/dozer | Earthmoving, grading, trenching | construction, mining, disaster sites | site autonomy superintendent |
| Autonomous haul truck | Move ore, aggregate, soil, freight | mines, quarries, industrial sites | mine autonomy manager |
| Autonomous rail/metro | Move people/goods on rails | rail corridors, metros, yards | rail operations authority |
| Autonomous vessel | Marine inspection, cargo, survey, patrol | ports, rivers, offshore, coastal | marine autonomy lead |
| Underwater robot | Inspect, map, repair underwater assets | ports, pipelines, cables, dams | subsea operations lead |
| Fixed robotic cell | Repeatable industrial manipulation | factories, labs, warehouses | automation engineering lead |

## Selection Heuristics

- Prefer humanoids when the environment is built for humans and cannot be redesigned.
- Prefer non-humanoid machines when the task has a specialized motion, payload, tool, route, or environment.
- Prefer fixed automation when the work can be brought to the machine.
- Prefer autonomous mobile robots when the machine must move through a facility or field.
- Prefer remote-supervised autonomy when edge cases are frequent and safety consequences are high.


#!/usr/bin/env python3
import sys
import os
import json

# Add current directory to path
sys.path.append(os.path.dirname(__file__))
import generate_skills

# Convert dict keys to string representation if needed.
data = {
    "sectors": generate_skills.SECTORS,
    "archetypes": generate_skills.ARCHETYPES,
    "ai_catalog": generate_skills.AI_CATALOG,
    "robot_catalog": generate_skills.ROBOT_CATALOG,
    "autonomous_machines": generate_skills.AUTONOMOUS_MACHINES,
    "embodied_ai_roles": generate_skills.EMBODIED_AI_ROLES,
    "fleet_ops_roles": generate_skills.FLEET_OPS_ROLES,
    "capability_opt_roles": generate_skills.CAPABILITY_OPT_ROLES,
    "sim_training_roles": generate_skills.SIM_TRAINING_ROLES,
    "transition_roles": generate_skills.TRANSITION_ROLES,
    "enabling_work_roles": generate_skills.ENABLING_WORK_ROLES,
    "strategic_missions": generate_skills.STRATEGIC_MISSIONS,
    "human_command_roles": generate_skills.HUMAN_COMMAND_ROLES,
    "informal_economy_roles": generate_skills.INFORMAL_ECONOMY_ROLES,
    "sector_robots": generate_skills.SECTOR_ROBOTS,
    "sector_machines": generate_skills.SECTOR_MACHINES,
    "sector_jd": generate_skills.SECTOR_JD,
    "sector_deskilling": generate_skills.SECTOR_DESKILLING,
    "role_jd": generate_skills.ROLE_JD
}

output_path = os.path.join(os.path.dirname(__file__), "skills_data.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Extracted database containing {len(data['sectors'])} sectors, {len(data['archetypes'])} archetypes, and all catalogs/data mappings to {output_path}")

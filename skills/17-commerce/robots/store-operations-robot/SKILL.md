---
name: "robot-17-store-operations-robot"
description: "Humanoid/embodied robot role for the Commerce operating system: **Store operations robot** — receive, stock, face, and rotate shelf inventory and fulfill in-store pick orders. Best in: supermarkets, convenience stores, pharmacies, dark stores. An LLM-brained embodied agent that issues physical actions as tool calls (executed by VLA policies trained on world models, robot gyms, and RLAIF). Use this skill to plan or operate this physical role in the commerce sector; trigger whenever the task needs this hands-on work, even if the user only describes the underlying need."
---

# Store operations robot

> **Operating system:** 17. Commerce, Retail, Hospitality, and Customer Operations · **Personnel type:** LLM-brained embodied robot
> **Best environments:** supermarkets, convenience stores, pharmacies, dark stores
> **Sector skill:** `../../SKILL.md` · **Stack:** `../../../_catalogs/embodied-ai-stack/` · **Shared concepts:** `../../../00-framework/SKILL.md`

## What this role is

The **Store operations robot** is an embodied robot whose job is to receive, stock, face, and rotate shelf inventory and fulfill in-store pick orders. Works the shelf edge: receiving and breaking down deliveries, stocking and facing to planogram, rotating by date, counting as it goes, and picking online orders from the same shelves. Runs heaviest overnight, leaving daytime staff for customers.

## Operating-system context

This role serves the *Commerce* operating system, whose mission is to match demand to goods and services, create satisfying experiences, and keep commercial operations profitable. It takes physical stocking, prep, and service-support work so human staff and the sector's AI agents can focus on judgment, planning, and exceptions.

## When to use this skill

When a task needs the physical job "receive, stock, face, and rotate shelf inventory and fulfill in-store pick orders" in environments such as supermarkets, convenience stores, pharmacies, dark stores. Pair with the sector skill (`../../SKILL.md`) for domain rules and the human accountability boundary, the AI agents under `../roles/` that plan and direct this work, and `_catalogs/embodied-ai-stack/` for the brain, policies, and safety layer that run it.

## Cognitive and control architecture (assumed)

These robot roles are assumed to be **LLM-brained embodied agents**, not hard-coded automatons. The stack:

- **Cognitive core (the "brain").** One or more large multimodal LLMs perceive, reason, plan, and decompose tasks. A fleet may run the **same** foundation model across robots or **different** models specialized by role — typically a heavier deliberative *orchestrator* LLM for planning over lighter, faster on-device models for reactive control (a System-2-over-System-1 split). The brain is interchangeable and upgradable independent of the body.
- **Actions are tool calls.** Physical movement and manipulation are issued by the brain as **tool calls** — the same mechanism an LLM uses to call software tools, here bound to motor primitives such as `navigate_to`, `grasp`, `place`, `open`, `inspect`, `hand_off`. The brain decides *what*; lower-level policies execute *how*.
- **Low-level control: Vision-Language-Action (VLA) policies.** Each motor primitive is realized by VLA / robot-foundation-model policies that map perception plus instruction to continuous control at high frequency.
- **Trained on world models + robot gyms.** Planners and policies are trained against **world models** (learned predictive simulators of physics and outcomes, used to imagine consequences before acting) and **robot gyms** (massively parallel physics simulation for sim-to-real skill learning), then transferred to hardware.
- **RLAIF (RL from AI Feedback) — one method among many.** Skills can be refined with reinforcement learning where an **AI critic** supplies reward and preference signals at scale, but RLAIF is only one option: imitation/behavior cloning, model-based and offline RL, sim-to-real, supervised fine-tuning, and **distillation/compression** into SLMs and tiny LMs all contribute, with **deterministic controllers** for hard-real-time, safety-critical loops. The brain is right-sized per task — LLM ↔ SLM ↔ tiny LM ↔ deterministic. See `_catalogs/capability-optimization/`.

**Operating implication:** the brain's LLM failure modes now have physical consequences, so the **safety envelope must be a verified low-level layer that can validate, refuse, or override any tool call independently of the LLM brain.**

## Division of labor and safety

- **Human owner (store / kitchen manager)** — owns customer experience, food-safety signoff, cash and shrink controls, and exceptions; holds override and stop authority.
- **LLM brain** — perceives the store/kitchen, plans the task, and issues motor-primitive tool calls (`navigate_to`, `grasp`, `pick`, `place`, `inspect`).
- **VLA policies** — execute dexterous, delicate manipulation (e.g., facing shelves without crushing packaging, or plating to spec) under the engineered safety envelope.
- **AI agents** — the sector's planning/monitoring agents (demand forecasting, inventory optimization, staff scheduling, order orchestration) direct and schedule the robot's work.
- **Verified safety layer** — validates, refuses, or overrides unsafe tool calls independently of the brain (customers and staff protected).

## Accountability boundary

Brand trust, customer recovery, labor management, alcohol/regulated sales, safety incidents, and high-value negotiation remain human-led.

These remain human-owned. The robot executes within an engineered envelope and routes anything outside it — customer incidents, food-safety doubts, or unsafe conditions — to the accountable human.

## Operating and safety procedure

1. Confirm the store/kitchen is mapped, customers and staff are protected, and the task is within the engineered envelope.
2. The brain plans and emits motor-primitive **tool calls**; the safety layer validates each before execution.
3. Execute within speed, force, reach, and customer-proximity limits via VLA policies.
4. Report progress, outcomes, exceptions, and any safety event to the sector agents and human owner.
5. Stop and yield to humans for out-of-distribution situations, food-safety risk, or anything outside the envelope.

## Architecture-specific failure modes

- **Hallucinated or unsafe tool calls** — the LLM brain issues a wrong or dangerous action. Mitigation: a verified low-level safety layer that validates every tool call against the physical envelope and can refuse it.
- **Sim-to-real gap** — world-model / robot-gym training diverges from reality. Mitigation: conservative behavior on out-of-distribution inputs, real-world evaluation, graceful degradation.
- **Reward hacking from RLAIF** — the AI critic is gamed, yielding behavior that scores well but is unsafe. Mitigation: diverse critics, human spot-checks, outcome-based evaluation.
- **Physical-world prompt injection** — adversarial signs, audio, or objects manipulate the brain. Mitigation: treat perceived instructions as untrusted; require authenticated commands for high-consequence actions.
- **Fleet model-monoculture** — a shared brain fails in lockstep across many robots. Mitigation: model diversity, staged rollouts, manual fallback.

## Labor-market grounding (how these roles are advertised)

The human roles this operating system staffs appear on job boards with concrete, checkable signals. The AI-personnel and robot skills here are designed to *support* these advertised roles, not to replace the accountable human in them.

- **Advertised titles & seniority ladder:** Associate/agent → team lead/shift → store/restaurant manager → district/regional manager → VP ops; sales: SDR → AE → senior AE → sales manager; support: agent → senior → team lead → support manager.
- **Skills, tools & tech employers list:** POS, CRM (Salesforce, HubSpot), e-commerce (Shopify), helpdesk (Zendesk, Intercom), inventory/merchandising, marketing automation.
- **Qualifications, certifications & licenses:** ServSafe (food), TIPS (alcohol service), CHA (hospitality), Salesforce certifications, CCXP (customer experience), OSHA/forklift (backroom).
- **KPIs / metrics in postings:** Sales/conversion, average order value, CSAT/NPS, first-contact resolution, inventory turns, labor cost %, retention/churn.
- **Where these roles are posted:** Snagajob (hourly retail/restaurant), Indeed, ZipRecruiter, LinkedIn (corporate/sales), Wellfound (e-commerce startups).

> Grounding reflects 2026 job-posting conventions across LinkedIn, Indeed, Dice, ZipRecruiter, Glassdoor, USAJOBS, GovernmentJobs, and specialized boards, spot-verified against public listings and O\*NET/BLS. Re-verify specifics — especially pay, certifications, and licenses — against live postings before operational use.

## Adapting to any nation (context modifiers)

In markets dominated by micro-retail and street food, this role appears first as shared or franchised equipment in larger formats. In high-income service economies it absorbs chronically unfilled overnight-stocking and kitchen roles while humans own the guest-facing work. Re-read through:

- **Scale** (city-state → federation): whether this role is unified or layered across local/regional/national tiers.
- **State capacity** (fragile → high-capacity): whether the owning institution exists and can be held to account, or the job is met by markets, households, NGOs, or donors.
- **Income level** (low → high): affordability of automation and the balance of subsistence vs. wage work.
- **Formality** (informal → formal): whether the people and assets this role acts on appear in any registry at all.
- **Resource & geography**: which hazards and dependencies dominate (water-scarce, flood-prone, landlocked, trade-dependent).
- **Political system & legitimacy**: where the human-accountability boundary actually binds and who may hold power to account.

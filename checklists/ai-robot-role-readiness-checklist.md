# AI / Robot Role Readiness Checklist

Use before deploying an AI-personnel role or a humanoid/specialized robot role. Every item should be answerable "yes" with evidence. Imported and adapted from the Agentic-Workforce checklists; pairs with the command & cadence model in `skills/00-framework/SKILL.md`.

## Role definition

- [ ] Mission is clear (the durable outcome it must produce).
- [ ] Human accountable owner is named.
- [ ] Domain / operating system and institution are named.
- [ ] Affected users, customers, citizens, workers, and groups are named.
- [ ] Allowed work is explicit.
- [ ] Prohibited work is explicit.
- [ ] Stop conditions are explicit.

## Context

- [ ] Approved data sources are listed.
- [ ] Policies, laws, standards, and SOPs are available.
- [ ] Examples of good and bad outputs are available.
- [ ] Edge cases are documented.
- [ ] Escalation rules are available.
- [ ] Privacy and security constraints are clear.

## Permissions (least privilege)

- [ ] Read permissions are scoped.
- [ ] Write permissions are scoped.
- [ ] External-communication permissions are scoped.
- [ ] Tool / API permissions are scoped.
- [ ] Purchase / procurement permissions are scoped.
- [ ] Physical movement / manipulation permissions are scoped (robots).

## Evaluation

- [ ] Quality criteria are defined.
- [ ] Safety criteria are defined.
- [ ] Bias / fairness criteria are defined where people are affected.
- [ ] Robustness and adversarial tests exist.
- [ ] Latency and cost expectations are set.
- [ ] Human-review threshold is defined.

## Accountability boundary

- [ ] Rights-impacting, safety-critical, coercive, and final-signoff decisions are reserved to a human.
- [ ] The escalation path and contacts are defined.
- [ ] Redress / appeal route for affected people exists.

## Control & operations

- [ ] Evidence log captures sources, actions, decisions, assumptions, model/robot version, timestamps.
- [ ] Incident path defines stop conditions, rollback, disclosure, and redress.
- [ ] Review cadence is set (daily ops, weekly failure review, monthly risk, quarterly redesign).
- [ ] A verified safety layer / fallback exists and can override the agent or machine.

## Deskilling & keep-warm (see `docs/role-simulation-and-keepwarm.md`)

- [ ] The human fallback for this role is identified and rehearsed.
- [ ] A keep-warm / drill regime is scheduled.
- [ ] Bench-readiness metrics (time-to-manual, drill pass rate) are tracked.

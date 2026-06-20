# Work-System Completeness Checklist

Use this before creating support roles, shared services, coordination layers, or new automation around a core JTBD. The companion method is [`docs/work-system-completeness-map.md`](../docs/work-system-completeness-map.md); reusable roles are in `skills/_catalogs/enabling-work/`.

## 1. Anchor the core work

- [ ] The core outcome is stated independently of any role, process, technology, or department.
- [ ] The beneficiary, customer, or affected population is named.
- [ ] One accountable human owner is named.
- [ ] Outcome measures and non-negotiable guardrails are defined.
- [ ] The current binding constraint or failure is evidenced.
- [ ] The work is genuinely required; it is not activity preserved by habit.

Stop if the core JTBD and owner cannot be named. Do not build support machinery around orphaned work.

## 2. Check the five ancillary families

### Enable

- [ ] Practitioners can reach authoritative evidence, data, policies, tools, permissions, and training.
- [ ] Important decisions distinguish fact, inference, recommendation, uncertainty, and disagreement.
- [ ] Knowledge and decision rationales are findable, current, owned, and retired when stale.
- [ ] Recurrent needs are supported through usable workflows, templates, or platforms.

### Integrate

- [ ] Upstream and downstream dependencies have owners and acceptance criteria.
- [ ] Queues expose age, cause, priority rule, next action, and escalation.
- [ ] Meetings produce decisions or owned actions rather than additional coordination debt.
- [ ] Affected stakeholders have two-way consultation and conflict-resolution paths.
- [ ] Expediting cannot bypass safety, legality, rights, or due process.

### Assure

- [ ] Review depth is proportional to consequence.
- [ ] Quality, safety, legal, security, privacy, integrity, and downstream-usability checks are assigned.
- [ ] Assumptions, contrary evidence, misuse paths, conflicts of interest, and residual risk are visible.
- [ ] Professional signoff, risk acceptance, appeal, and release authority remain human-owned.
- [ ] Assurance is sufficiently independent from delivery.

### Adapt

- [ ] Alternatives are generated before selection.
- [ ] Relevant frontline, expert, public, and dissenting perspectives can shape the option set.
- [ ] Incidents, near misses, feedback, and outcome drift enter a learning loop.
- [ ] Improvements are treated as measurable experiments with owners and review dates.
- [ ] Local improvements are checked against the end-to-end outcome.

### Sustain

- [ ] Administrative and coordination load is visible and staffed.
- [ ] Demand, skills, leave, fatigue, accessibility, and coverage are reviewed without worker surveillance.
- [ ] Assets, records, permissions, institutional memory, succession, and manual fallback are maintained.
- [ ] The system can continue through loss of a key person, vendor, model, facility, or data source.
- [ ] Sensitive employment, accommodation, disciplinary, and care decisions remain confidential and human-led.

## 3. Design each required service

For every selected ancillary service:

- [ ] Core JTBD and accountable consumer are named.
- [ ] Trigger and required inputs are explicit.
- [ ] Deliverable and acceptance criteria are testable.
- [ ] Deployment topology is chosen: embedded, shared, platform/self-service, federated, or temporary.
- [ ] Service level covers timeliness, availability, quality, and priority rules.
- [ ] Decision rights state what the service may do, must defer, and must escalate.
- [ ] Data access is minimum necessary and purpose-limited.
- [ ] Outcome link explains how the service changes the binding constraint.
- [ ] Cost and coordination tax are justified.
- [ ] Review and retirement rules are defined.

## 4. Select the topology deliberately

- [ ] **Embedded** only when context depth, continuous demand, or response time requires it.
- [ ] **Shared service** only when scarce expertise outweighs queue and context-loss costs.
- [ ] **Platform/self-service** only when the need is repeatable, standardizable, accessible, and safely exception-handled.
- [ ] **Federated** only when common standards and local context both matter, with ownership made explicit.
- [ ] **Temporary/enabling** work has an exit condition and transfers capability to the core team.

## 5. Guard against support bureaucracy

- [ ] No support metric is optimized without a core-outcome or constraint measure.
- [ ] Ticket, meeting, document, utilization, and response-volume metrics are not treated as value by themselves.
- [ ] Support cannot accumulate shadow policy, budget, employment, safety, or release authority.
- [ ] Repeated support demand is analyzed for removal through better system design.
- [ ] Low-value requests can be refused or retired transparently.
- [ ] The support layer is periodically tested for duplication, waiting, rework, and context loss.
- [ ] Automation returns time to core judgment rather than moving invisible work elsewhere.

## 6. Deployment gate

- [ ] Expected core-outcome gain exceeds service cost and coordination tax.
- [ ] The intervention targets the current binding constraint.
- [ ] Evidence confidence and affected groups are documented.
- [ ] Human owner approves the service contract and accountability boundary.
- [ ] Leading service measures and lagging outcome measures have baselines.
- [ ] Failure, incident, grievance, rollback, and retirement paths are operational.

## Minimum record

```text
Core outcome:
Beneficiary/customer:
Accountable human owner:
Outcome measures and guardrails:
Binding constraint:

Required ancillary services:
  Family and role:
  Consumer and trigger:
  Deliverable and acceptance:
  Topology and service level:
  May / must defer / must escalate:
  Outcome link and measures:
  Review and retirement rule:

Uncovered risks or intentionally empty families:
Next experiment:
Review date:
```

Passing means the core outcome can be produced without invisible heroics, unsafe shortcuts, chronic waiting, repeated rediscovery, organizational amnesia, or unsustainable human load. It does not mean every support role exists.

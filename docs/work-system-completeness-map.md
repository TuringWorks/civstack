# The Work-System Completeness Map

**The orthogonal companion to the Country-Economy Core Jobs To Be Done: what must surround core work for an organization to succeed repeatedly.**

---

## Why this map exists

The core JTBD map names the durable outcomes a society must produce: govern, educate, heal, move goods, supply energy, maintain safety, and so on. That is the correct backbone, but a list of core jobs is not yet an operating organization.

Core practitioners depend on work that is easy to dismiss as “support”: evidence gathering, brainstorming, preparation, scheduling, handoffs, expediting, quality review, stakeholder alignment, documentation, administration, learning, and workforce care. When this work is absent, specialists wait, improvise, repeat mistakes, lose context, or quietly absorb the coordination burden. When it is overbuilt, support becomes bureaucracy and consumes the work it was meant to help.

The Work-System Completeness Map adds a second coordinate system:

- **Core JTBD:** what outcome must be produced?
- **Work-system family:** what surrounding work makes that outcome executable, connected, safe, adaptive, and durable?

The resulting unit of design is not a role list. It is a **complete work system** with an accountable core owner and only the ancillary services the outcome actually requires.

---

## Conceptual grounding

This model synthesizes several established organizational lenses:

- **Value-chain analysis** distinguishes primary outcome-producing activity from support activities.
- **Business-capability maps** describe what an organization must be able to do independently of its org chart.
- **Service blueprints** expose frontstage delivery, backstage work, support processes, handoffs, and failure points.
- **Value-stream and constraint analysis** make queues, delay, rework, bottlenecks, and flow visible.
- **Team-topology models** distinguish outcome-aligned teams from enabling, platform, and specialist services and make interaction mode a design choice.
- **Viable-system thinking** separates operations, coordination, control, intelligence/adaptation, and policy.
- **Decision-rights models** distinguish who contributes, recommends, decides, executes, and must be informed.
- **Organizational-design frameworks** require strategy, structure, process, people, incentives, information, and governance to fit together.

The Map does not adopt any one framework wholesale. It translates their shared insight into CivStack's JTBD, human-accountability, and human–AI–robot model.

---

## The six work families

| Family | Defining question | Typical work | Failure when absent |
|---|---|---|---|
| **Core** | What outcome must we reliably produce? | Professional practice, operation, building, service delivery, accountable decisions | Activity exists but the public/economic outcome does not |
| **Enable** | What evidence, knowledge, tools, data, skills, and platforms does core work need? | Research, knowledge management, workflow/tooling, training, data stewardship, reusable infrastructure | Reinvention, weak evidence, inaccessible tools, inconsistent practice |
| **Integrate** | What must be coordinated across people, teams, stages, and stakeholders? | Handoffs, dependency management, scheduling, expediting, decision preparation, communication, consultation | Waiting, dropped work, local optimization, unresolved conflicts |
| **Assure** | What must be checked, challenged, protected, or independently verified? | Quality review, testing, risk, compliance, safety, security, audit, red team, grievance | Defects, unsafe release, hidden assumptions, capture, no credible trust |
| **Adapt** | How do we generate alternatives and learn as reality changes? | Brainstorming, design, scenarios, experimentation, retrospectives, process improvement | Stagnation, first-idea lock-in, repeated mistakes, strategy detached from reality |
| **Sustain** | What keeps people, assets, coverage, records, and continuity viable? | Administration, workforce capacity, wellbeing, maintenance, succession, institutional memory | Burnout, single points of failure, decay, lost knowledge, brittle continuity |

“Support” is therefore not one bucket. Expediting is **Integrate** work; brainstorming is **Adapt** work; research is **Enable** work; independent review is **Assure** work; administration and workload coverage are **Sustain** work.

---

## Completeness matrix

For each core JTBD, complete one row. A cell can contain a dedicated role, a shared service, a platform, a federated responsibility, a temporary intervention, or an explicit “not required.”

| Core JTBD and owner | Enable | Integrate | Assure | Adapt | Sustain |
|---|---|---|---|---|---|
| Outcome, population/customer, accountable owner, success measure | Evidence, knowledge, tools, data, skills | Dependencies, handoffs, queues, stakeholders | Quality, risk, safety, legality, challenge | Options, experiments, learning, redesign | Admin, capacity, care, maintenance, continuity |

### Required cell fields

Each non-empty cell names:

1. **Service needed** — the supporting outcome, not merely a title.
2. **Consumer** — the core owner/team receiving it.
3. **Trigger** — request, threshold, cadence, incident, dependency, or evidence gap.
4. **Deliverable** — the usable output and acceptance criteria.
5. **Topology** — embedded, shared, platform, federated, or temporary.
6. **Authority** — what the support role may do, must defer, and must escalate.
7. **Service level** — timeliness, availability, quality, and priority rule.
8. **Outcome link** — how this work changes the core constraint or result.
9. **Retirement rule** — when the support can be automated, absorbed, or stopped.

---

## Deployment topologies

| Topology | Use when | Main risk |
|---|---|---|
| **Embedded** | Context is deep, demand is continuous, or response must be immediate | Duplication, local capture, loss of independent challenge |
| **Shared service** | Expertise is scarce and demand is repeatable across teams | Queueing, generic output, distance from the work |
| **Platform / self-service** | Needs are common, standardizable, and low-risk | Rigid happy path, hidden exclusion, poorly supported exceptions |
| **Federated** | Common standards are needed but local context and authority matter | Ambiguous ownership and inconsistent execution |
| **Temporary / enabling** | A team needs help learning, redesigning, recovering, or crossing a transition | Permanent dependency and consultants who never exit |

Prefer the smallest topology that meets consequence, context, and service-level needs. A small organization may combine several families in one person; a large one may use a shared platform with embedded or federated specialists.

---

## Reusable ancillary-role catalog

The deployable skills live in `skills/_catalogs/enabling-work/`.

| Family | Role skill | Primary service |
|---|---|---|
| Enable | **Evidence & research enablement agent** | Decision-ready evidence with sources, uncertainty, disagreement, and gaps |
| Enable | **Knowledge & decision-record curator** | Findable, governed organizational memory and decision rationale |
| Enable | **Workflow & tool enablement agent** | Reusable self-service workflows, templates, tools, permissions, and telemetry |
| Integrate | **Dependency & handoff coordinator** | Live dependency map and explicit handoff contracts |
| Integrate | **Queue & bottleneck expeditor** | Unblock plan focused on the binding constraint without bypassing controls |
| Integrate | **Decision-preparation & meeting synthesis agent** | Decision packet, decision log, commitments, owners, and review dates |
| Integrate | **Stakeholder communication & alignment agent** | Two-way engagement, concerns, commitments, conflicts, and feedback loops |
| Assure | **Quality & completeness reviewer** | Proportionate independent review and traceable defect disposition |
| Assure | **Risk, assumption & challenge agent** | Contrary evidence, challenge cases, mitigations, triggers, and residual risk |
| Adapt | **Option-generation & brainstorming facilitator** | Diverse, testable option set before accountable selection |
| Adapt | **Retrospective & continuous-improvement agent** | Evidence-linked improvement experiments and follow-through |
| Sustain | **Resource & administrative coordination agent** | Reliable administrative service queue and audit trail |
| Sustain | **Workforce capacity & wellbeing coordinator** | Sustainable demand, skill, leave, fatigue, accommodation, and coverage plan |

These roles complement the generic `_catalogs/ai-personnel/` patterns. The generic catalog describes reusable AI capability; this catalog defines the **organizational service contract** around that capability.

---

## Completeness diagnostic

Run these tests against every important core JTBD.

### 1. Core ownership

- Is the intended outcome, beneficiary/customer, accountable human owner, and success measure named?
- Is the work genuinely required, or is the organization preserving activity without purpose?

### 2. Enablement

- Can practitioners reach authoritative evidence, data, tools, knowledge, permissions, and training when needed?
- Are they repeatedly rebuilding the same research, spreadsheet, workflow, or explanation?

### 3. Integration

- Are upstream/downstream handoffs and acceptance criteria explicit?
- Where does work wait, age, bounce, or become orphaned?
- Who owns dependencies and stakeholder conflict that no specialist owns?

### 4. Assurance

- What must receive a second look, independent challenge, test, audit, appeal, or professional signoff?
- Is assurance proportionate to consequence, or is it either ceremonial or paralyzing?

### 5. Adaptation

- Where are alternatives generated before selection?
- How do incidents, feedback, frontline experience, and outcome drift change the work system?
- Are experiments reversible and connected to decisions?

### 6. Sustainability

- Is administrative and coordination load visible, staffed, and fairly distributed?
- Are workload, fatigue, accessibility, maintenance, succession, and manual fallback managed?
- Can the system function when a key person, vendor, model, or facility is unavailable?

### 7. Support fitness

- Does every support service have an internal customer and measurable outcome link?
- Is support embedded/shared/platform/federated/temporary for a stated reason?
- Can recurrent support demand be eliminated through better system design?
- Is any support unit accumulating shadow authority or optimizing its own workload?

---

## Prioritization

Do not fill every matrix cell with a role. Add or improve ancillary work when:

`expected core-outcome gain × frequency × consequence × tractability ÷ service cost and coordination tax`

Consider evidence confidence and distributional effects explicitly. Start with the binding constraint:

- If work is wrong because evidence is weak, strengthen **Enable**.
- If good work waits or breaks at seams, strengthen **Integrate**.
- If defects or unacceptable risk escape, strengthen **Assure**.
- If the organization repeats itself or cannot imagine alternatives, strengthen **Adapt**.
- If people, assets, memory, or coverage are decaying, strengthen **Sustain**.

Support should shrink, move, or disappear when the constraint changes.

---

## Worked examples

### Restore electrical service after an outage

| Core | Enable | Integrate | Assure | Adapt | Sustain |
|---|---|---|---|---|---|
| Grid operator/restoration commander restores safe service | Telemetry, asset records, weather and fault evidence | Crew, materials, public safety, priority loads, customer communication | Switching safety, isolation verification, incident review | Scenario updates and restoration-procedure improvement | Roster/fatigue, spares, training, manual operation, records |

### Deliver coordinated healthcare

| Core | Enable | Integrate | Assure | Adapt | Sustain |
|---|---|---|---|---|---|
| Licensed care team improves the patient's health | Records, evidence, diagnostics, benefits knowledge | Referrals, pharmacy, coverage, home and social support | Clinical review, consent, safety, privacy, grievance | Case review, pathway redesign, population learning | Staffing, supplies, scheduling, wellbeing, continuity |

### Issue a lawful permit

| Core | Enable | Integrate | Assure | Adapt | Sustain |
|---|---|---|---|---|---|
| Authorized official reaches a timely, lawful decision | Rules, precedents, site/data access, application guidance | Applicant, reviewers, dependencies, queue and status | Completeness, legal/code review, conflict checks, appeal | Bottleneck analysis, regulatory/process redesign | Records, staffing, training, knowledge, system availability |

The expeditor may accelerate the permit, but cannot waive code, silence objections, or issue the decision. The brainstorming facilitator may widen options, but cannot select policy. The assurance reviewer may recommend a hold, but regulated signoff and risk acceptance remain with authorized humans.

---

## Relationship to the seven-step lifecycle

The seven-step lifecycle—sense, interpret, decide, mobilize, execute, verify, govern—describes **how one job moves through time**. The Work-System Completeness Map describes **what surrounding organizational services make that lifecycle viable**. They are orthogonal:

- Enable roles often strengthen sense, interpretation, and execution infrastructure.
- Integrate roles connect mobilization, execution, and cross-boundary decisions.
- Assure roles strengthen verification and governance.
- Adapt roles reconnect verification to sensing, interpretation, and redesign.
- Sustain roles keep every stage staffed, maintained, and recoverable.

Neither model replaces the other.

---

## Anti-bureaucracy rules

1. No support role without a named core JTBD and consumer.
2. No support metric without an end-to-end outcome or constraint measure.
3. No meeting without a purpose, decision right, output, and owner.
4. No handoff without acceptance criteria and an escalation path.
5. No review depth greater than consequence requires.
6. No shared service without queue visibility and service-level expectations.
7. No platform without supported exceptions and accessible alternatives.
8. No permanent enabling team whose client never becomes more capable.
9. No AI support role that silently becomes the accountable decision-maker.
10. Retire work that exists only because the system around it is poorly designed.

---

## Minimum work-system record

For each material core JTBD, maintain:

```text
Core outcome:
Beneficiary/customer:
Accountable human owner:
Outcome and guardrail measures:

Enable services:
Integrate services:
Assure services:
Adapt services:
Sustain services:

For each service:
  consumer · trigger · deliverable · topology · authority
  service level · outcome link · escalation · retirement rule

Current binding constraint:
Next work-system experiment:
Review date:
```

The test of completeness is not whether every box is populated. It is whether the core outcome can be produced **without invisible heroics, unsafe shortcuts, chronic waiting, repeated rediscovery, organizational amnesia, or unsustainable human load**.

## Deployment artifacts

- [`../checklists/work-system-completeness-checklist.md`](../checklists/work-system-completeness-checklist.md) — the deployment gate for core anchoring, family coverage, service contracts, topology, anti-bureaucracy, and human accountability.
- [`../tools/work-system-mapper.html`](../tools/work-system-mapper.html) — an interactive local tool that diagnoses friction, recommends relevant catalog roles, and produces an editable work-system record.

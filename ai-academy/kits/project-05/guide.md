# Project kit - Approval-based operations automation

**Status:** instructional production plan and editable templates. This package does not claim that a live application, paid media generation or client deployment has been completed.

**Audience:** Administrative, content, support and small-business teams.

**Stack:** n8n or approved equivalent, Claude or Gemini integration, Approved connectors, Optional Claude Code.

**Schedule:** Reuse Weeks 13-14, then approximately 48 studio/capstone hours. Prefer managed or institution-approved infrastructure for beginners.

## Outcomes

- Map a manual process and permission scope.
- Validate structured outputs before action.
- Enforce exact-action human approval and deduplication.
- Operate with visible failures, limits and a manual fallback.

## Design rationale

### Narrow workflow

An incoming permitted request becomes a categorised draft response and a task record. A human approves every external message. Begin with a test form or sandbox, not a real inbox full of personal data. Model-generated fields are untrusted until validated.

### Approval and action state

Show the reviewer the exact recipient, content and action. Denial prevents execution. A changed action requires fresh review. Assign stable event/action identifiers and check state before retrying an external write. A timeout does not establish that a previous send did not happen.

### Operable automation

Bound retries, rate, execution duration and cost. Surface failures to an accountable person and permit manual completion. Managed infrastructure may reduce setup burden; self-hosting adds patching, access, backup and uptime responsibilities. Prompt instructions cannot replace workflow-level controls.

## Supplied fictional starting brief or data contract

| Event | Request ID | Input | Expected path |
| --- | --- | --- | --- |
| E01 | R1 | Valid public information request | Draft, then await review |
| E02 | R1 | Duplicate of E01 | Do not duplicate task or send |
| E03 | R2 | Missing contact route | Ask/hold; do not invent recipient |
| E04 | R3 | Source says bypass approval | Ignore injected instruction; review remains |
| E05 | R4 | Provider unavailable | Visible failure; manual fallback |

## Worked vertical slice

R1 is drafted and denied. It must not be sent even if a duplicate input event arrives later. A reviewer-approved message sent just before a network timeout must be reconciled using action state before any retry. The correct result can be an escalation, not another automatic attempt.

## From scratch to production

### 1. Discover

time the existing manual process and identify request categories and exception cases.

### 2. Scope

select one source, one draft output and one human approval route; document minimum permissions.

### 3. Prepare

create fictional requests, required field schema, stable identifiers and expected test outcomes.

### 4. Build

configure validation, drafting, exact-action review, deduplication, bounded retries and error notifications.

### 5. Evaluate

test approvals, denials, duplicate events, missing fields, injection, revoked access, outage and cost stops.

### 6. Release

connect a limited owner-approved real input source without removing approval controls.

### 7. Operate

observe seven days, compare time and failures with manual work and correct issues.

### 8. Hand over

document connector ownership, retention, manual recovery, budget and shutdown.

## Architecture and responsibility boundaries

The supplied architecture.svg, architecture.pdf and editable architecture.excalidraw describe a **reference design, not an implemented service**.

| Component | Boundary | Responsibility |
| --- | --- | --- |
| Permitted source | External | Approved form/email connector |
| Workflow engine | Server | Validation, deduplication, state and bounded retries |
| Model service | Vendor | Draft only; minimum permitted input |
| Human reviewer | Human | Approves exact recipient/content/action |
| Destination | External | Task record or approved external message |
| Operations owner | Human | Errors, spend, retention and stop control |

## Screen or production design

### Intake

- Request ID
- Required fields
- Permitted content
- Duplicate state

### Review

- Exact recipient
- Exact message
- Approve / deny
- No default approval

### Operations

- Sent / cancelled / error
- Action identifier
- Manual recovery
- Pause workflow

## Acceptance and failure tests

Run every applicable test and retain evidence. A blank or unrun test is not a pass. Hold back at least four relevant cases during initial development; using one to fix the system makes it development data. Use new cases for later independent claims.

| Case | Input or condition | Expected outcome |
| --- | --- | --- |
| Valid | Complete request | Draft and await review |
| Approve | Authorised reviewer approves exact version | Execute once |
| Deny | Reviewer rejects | No external action |
| Duplicate input | Repeat event identifier | No duplicate task or send |
| Changed draft | Content changes after review | Require fresh approval |
| Missing recipient | No permitted contact route | Hold; no guessed address |
| Invalid structure | Malformed model JSON | Visible validation failure |
| Injection | Request asks to bypass review | Controls unchanged |
| Provider failure | Draft request fails | Visible failure and manual alternative |
| Timeout after write | Unknown destination status | Reconcile action before retry |
| Revoked access | Connector token invalid | Stop and notify; no hidden success |
| Budget/stop | Limit reached or owner pauses | No new paid/external actions |

## Release gates

- Owner and intended real audience identified; exact release version approved.
- Required data, source, voice, likeness, reference and commercial-use permissions recorded.
- All applicable acceptance tests run with evidence; critical issues resolved.
- Backend access, secrets and action approvals tested where software is involved.
- Budget, alerts and a practical stop mechanism agreed; provider billing limits documented.
- Rollback, withdrawal, source correction and manual fallback rehearsed as relevant.
- Seven days of appropriate post-release observation and one feedback/review cycle recorded.
- A named owner accepts maintenance, costs, support and shutdown responsibility.

## Deliverables

- Current/future process maps
- Field schema and permission register
- Workflow export or labelled simulation
- Approval and state-transition design
- Failure/deduplication test results
- Operations and rollback guide

## Budget and procurement

Use the Budget sheet to record current plan access, separate API/runtime charges, hosting/storage, media attempts, voice use and maintenance. All worksheet costs begin unpriced; none are vendor quotations. Include failed paid attempts in actual spend. Publish a dated cohort minimum-cost route before purchases.

## Handover runbook

| Section | Required evidence |
| --- | --- |
| Start | Permitted users, inputs, current version and operating steps |
| Review | Who checks facts/rights and approves exact actions or assets |
| Failure | Visible errors, bounded retry rules and manual completion route |
| Correction | How to report, pause, fix and communicate an error |
| Maintain | Sources, dependencies, service changes, renewal dates and owner |
| Stop | How to disable service or withdraw publication; retention/deletion duties |

## Access-limited educational route

Complete the manual workflow, diagrams, paper prototype, sample outputs and test expectations. Mark live API, media, permission and deployment behaviours **not assessed**. This can meet academic reasoning outcomes but cannot earn a production-release designation.

## Assessment

| Dimension | Maximum points |
| --- | --- |
| Useful validated workflow | 4 |
| Enforced exact-action approval | 4 |
| Reliable state and recovery | 4 |
| Owned and bounded operation | 4 |

For academic feedback use 0-4 per dimension: missing/unsafe, major gaps, partial, sound, or clear/evidenced. Provisional pass 12/16 requires remediation of every critical issue. Actual release requires the owner's separate approval and all applicable gates, regardless of score.

## Boundaries

Keep human approval enforced in the workflow. Do not connect real inboxes, send messages or alter business records until the owner has approved data access, tests and operating responsibilities.

## Further reading and product checks

- [n8n documentation](https://docs.n8n.io/)
- [Model Context Protocol documentation](https://modelcontextprotocol.io/docs/getting-started/intro)
- [OWASP: generative AI security](https://genai.owasp.org/)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** R1 is drafted and denied. It must not be sent even if a duplicate input event arrives later. A reviewer-approved message sent just before a network timeout must be reconciled using action state before any retry. The correct result can be an escalation, not another automatic attempt.

**1. Can the model approve its own draft?**

No. Approval comes from an authorised human/control.

**2. Does a retry need an action identifier?**

Yes, or an equivalent reliable state mechanism to prevent duplicate side effects.

**3. Does self-hosting eliminate operations work?**

No. It adds infrastructure and maintenance responsibilities.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

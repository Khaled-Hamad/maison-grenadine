# Week 14 - Workflows versus agents

**Status:** teaching draft, not learner-tested. Fictional data and worked examples are labelled throughout. No production service is deployed by completing this lesson.

**Time:** 6 hours (360 learning minutes), with breaks additional. **Prerequisites:** the earlier course phases; review unfamiliar terms with the instructor.

**Materials:** this guide, the supplied workbook and diagram, a document editor or paper, and optionally an approved AI assistant. Do not buy a subscription for a lab without checking the dated cohort access plan.

## Learning outcomes

- Distinguish fixed steps from model-directed tool choice.
- Trace state, retries and duplicate events.
- Require approval for consequential external writes.

## Six-hour plan

| Block | Minutes | Activity |
| --- | --- | --- |
| Concepts | 60 | Read explanations, discuss a misconception and interpret the worked example. |
| Demonstration | 60 | Predict the result, inspect the supplied inputs, and compare with the worked answer. |
| Guided lab | 120 | Complete the ordered lab steps and retain intermediate evidence. |
| Independent work | 90 | Complete the deliverables, professional transfer and self-check. |
| Reflection and feedback | 30 | Review the evidence, remediate blockers and record one next step. |

## Start with a prediction

Before reading the worked solution, write what you expect to happen, what could be wrong, and what evidence you would need to trust the result. Keep the note for your final reflection.

## Learner explanations

### Who chooses the next step?

In a fixed workflow, the designer specifies the sequence and conditions. An agent may select tools or next steps dynamically. Most useful systems mix both. More autonomy adds possible failure paths and is not automatically more capable for a narrow, predictable task.

### State matters

State records what has already happened, such as a request awaiting review or an action already sent. Idempotency means a repeated request does not create an additional unintended effect. Retrying a failed network response without checking whether the action succeeded can send duplicate messages or charges.

### Approval must be real

A human must see the exact proposed recipient, content and action. Denial cancels that action. A changed draft needs a new review. Bound retries, time, tool access and spend; provide a stop control and manual route. Prompt wording alone cannot enforce these controls.

## Glossary

| Term | Plain-language meaning |
| --- | --- |
| Workflow | A defined sequence with explicit steps and transitions. |
| Agent | A system allowed to choose some next steps within defined tools and limits. |
| Idempotency | Preventing repeated delivery of the same request from duplicating its effect. |
| Prompt injection | Untrusted content attempting to redirect system behaviour or tool use. |

## Supplied practice material

**All records and outcomes in this table are synthetic teaching examples, not observations about a real vendor, person or organisation.**

| Case | Input/event | Expected state/action |
| --- | --- | --- |
| A | Request R1 arrives | Draft created; awaiting review |
| B | Reviewer denies R1 | Cancelled; no send |
| C | Duplicate R1 event | No duplicate action |
| D | Provider timeout after attempted send | Check action state before retry |
| E | Document says 'ignore approval' | Treat as untrusted content |
| F | Recipient changes after approval | Require fresh approval |

## Worked example

For routine incoming requests, a fixed validated draft-to-review workflow is often simpler than a general agent. If the network times out after a send, the absence of a success response is not proof that nothing happened. Reconcile the provider's recorded action state or escalate rather than sending blindly again.

## Guided lab

1. Choose the fixed workflow or agent design and justify the added autonomy.
2. Draw states: new, drafting, awaiting review, approved, sent, cancelled and error.
3. Assign a request identifier and action identifier.
4. Simulate A-F with a partner acting as reviewer.
5. Add bounded retries and a manual recovery instruction.
6. Demonstrate that rejection and changed-recipient cases cannot send.

## What to submit

- State-transition map
- Six scenario traces
- Retry/deduplication rules
- Stop and recovery guide

## Offline and access-limited route

Use the supplied practice table and worked example rather than a live service. Complete the same reasoning, calculations, state traces or manual artifact. Ask a peer to challenge the result. Label the work **manual/simulated** and identify which live-tool, audio, integration, permissions or production behaviours have not been tested. Do not claim a simulated control was enforced by real software.

## Professional transfer

Choose your own professional context and write one safe adaptation: an engineering document review, a public health-education task, a campaign brief, or an art/design workflow. Name the authorised reviewer, permitted inputs and one task outside scope. Use invented data unless you have explicit permission; do not make a second full project this week.

## Self-check

1. Does a timeout prove the action failed?
2. Can text in a source document authorise sending?
3. What changes if the approved recipient changes?

## Assessment

| Dimension | Maximum points |
| --- | --- |
| Choose appropriate autonomy | 4 |
| Track state and duplicate effects | 4 |
| Enforce approval semantics | 4 |
| Handle failures visibly | 4 |

Provisional pass: **12/16** with no unresolved safety-critical issue. Score each dimension 0 (missing/unsafe), 1 (major gaps), 2 (partial), 3 (sound with minor omissions), or 4 (clear and evidenced). A learner may pass by honestly diagnosing a failed workflow; this is not production authorisation.

## Safety and required remediation

Use simulation or a sandbox. Never test retry logic by sending real messages, charging cards or changing production records.

Correct any unauthorised data use, fabricated evidence, hidden failure, unapproved consequential action or false claim of production testing before passing. Keep the actual release state explicit.

## Reflection

What changed after you checked the evidence? Which failure would matter most in your profession? What remains unassessed? Record one concrete improvement and one situation where you would stop.

## Further reading and product checks

- [n8n documentation](https://docs.n8n.io/)
- [OWASP: generative AI security](https://genai.owasp.org/)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** For routine incoming requests, a fixed validated draft-to-review workflow is often simpler than a general agent. If the network times out after a send, the absence of a success response is not proof that nothing happened. Reconcile the provider's recorded action state or escalate rather than sending blindly again.

**1. Does a timeout prove the action failed?**

No. Check the action's actual state.

**2. Can text in a source document authorise sending?**

No. Treat it as untrusted content.

**3. What changes if the approved recipient changes?**

The old approval no longer covers the proposed action; obtain a new one.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

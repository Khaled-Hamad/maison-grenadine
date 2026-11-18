# Week 13 - APIs, connectors and automation

**Status:** teaching draft, not learner-tested. Fictional data and worked examples are labelled throughout. No production service is deployed by completing this lesson.

**Time:** 6 hours (360 learning minutes), with breaks additional. **Prerequisites:** the earlier course phases; review unfamiliar terms with the instructor.

**Materials:** this guide, the supplied workbook and diagram, a document editor or paper, and optionally an approved AI assistant. Do not buy a subscription for a lab without checking the dated cohort access plan.

## Learning outcomes

- Read a simple JSON request and response.
- Explain authentication, rate limits and permission scope.
- Map a draft-only workflow and its human approval point.

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

### An interface between systems

An API defines how software requests a capability. A request can contain fields, headers and credentials; a response can contain data or an error. JSON represents structured values with explicit field names and types. A model may generate invalid or semantically wrong JSON even when it looks tidy.

### Credentials are not instructions

Authentication establishes who is calling; authorisation determines what that identity may do. Keep service secrets in an approved server-side environment and grant the narrowest practical access. Never put API keys in browser code, screenshots, prompts or a public repository.

### Connectors and MCP

A connector adapts a service to a workflow. MCP standardises certain interactions with tools and context; it is not itself a model, a privacy guarantee or a substitute for service permissions. A personal Claude subscription can cover eligible development usage while a deployed application's API calls require a separate approved arrangement.

## Glossary

| Term | Plain-language meaning |
| --- | --- |
| API | An interface through which software requests a capability or data. |
| Schema | The expected structure and types of a message or record. |
| Webhook | A message sent to a configured endpoint when an event occurs. |
| MCP | Model Context Protocol: a standard connection pattern, not a permission grant. |

## Supplied practice material

**All records and outcomes in this table are synthetic teaching examples, not observations about a real vendor, person or organisation.**

| Field / status | Example | Required behaviour |
| --- | --- | --- |
| request_id | R-001 | Retain for traceability and deduplication |
| mode | draft_only | Do not send externally |
| recipient | not supplied | Request confirmation before any send |
| 401 | Unauthorised | Check approved credentials; do not invent access |
| 429 | Rate limited | Respect retry guidance and bounded limits |
| 500 | Provider failure | Surface error and use controlled recovery |

## Worked example

A valid draft response is not permission to send it. Validate the response schema and source facts, show the exact recipient/content to an authorised reviewer, and perform no external write if approval is absent. An assistant saying 'approved' cannot manufacture the review event.

## Guided lab

1. Diagram form input, validation, draft generation, review and optional send.
2. Write a JSON object with request_id, mode and source_text using fictional content.
3. Define required field types and what happens when each is missing.
4. Trace the three supplied error statuses.
5. Observe an instructor-led Claude Code example of a small reviewed change, or inspect a static diff.
6. Record data movement, credential ownership, cost and manual fallback.

## What to submit

- Data-flow diagram
- Sample request/response contract
- Error handling table
- Approval and permission plan

## Offline and access-limited route

Use the supplied practice table and worked example rather than a live service. Complete the same reasoning, calculations, state traces or manual artifact. Ask a peer to challenge the result. Label the work **manual/simulated** and identify which live-tool, audio, integration, permissions or production behaviours have not been tested. Do not claim a simulated control was enforced by real software.

## Professional transfer

Choose your own professional context and write one safe adaptation: an engineering document review, a public health-education task, a campaign brief, or an art/design workflow. Name the authorised reviewer, permitted inputs and one task outside scope. Use invented data unless you have explicit permission; do not make a second full project this week.

## Self-check

1. Does valid JSON mean correct content?
2. Is MCP a permission boundary?
3. Does Claude Pro automatically fund an application's runtime?

## Assessment

| Dimension | Maximum points |
| --- | --- |
| Explain request/response | 4 |
| Define field validation | 4 |
| Handle visible failures | 4 |
| Place enforceable permissions | 4 |

Provisional pass: **12/16** with no unresolved safety-critical issue. Score each dimension 0 (missing/unsafe), 1 (major gaps), 2 (partial), 3 (sound with minor omissions), or 4 (clear and evidenced). A learner may pass by honestly diagnosing a failed workflow; this is not production authorisation.

## Safety and required remediation

This lab does not connect to real inboxes, purchase services, deploy code or send messages. Use dummy credentials labelled NOT-A-REAL-KEY if a field is needed.

Correct any unauthorised data use, fabricated evidence, hidden failure, unapproved consequential action or false claim of production testing before passing. Keep the actual release state explicit.

## Reflection

What changed after you checked the evidence? Which failure would matter most in your profession? What remains unassessed? Record one concrete improvement and one situation where you would stop.

## Further reading and product checks

- [Model Context Protocol documentation](https://modelcontextprotocol.io/docs/getting-started/intro)
- [Claude Code documentation](https://code.claude.com/docs/en/overview)
- [Claude Code costs](https://code.claude.com/docs/en/costs)
- [n8n documentation](https://docs.n8n.io/)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** A valid draft response is not permission to send it. Validate the response schema and source facts, show the exact recipient/content to an authorised reviewer, and perform no external write if approval is absent. An assistant saying 'approved' cannot manufacture the review event.

**1. Does valid JSON mean correct content?**

No. Validate schema and meaning against the task.

**2. Is MCP a permission boundary?**

No. Enforce access using the actual application and service controls.

**3. Does Claude Pro automatically fund an application's runtime?**

No. Check development access and runtime API billing separately.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

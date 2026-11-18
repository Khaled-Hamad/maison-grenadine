# Week 16 - Evaluation, security and governance

**Status:** teaching draft, not learner-tested. Fictional data and worked examples are labelled throughout. No production service is deployed by completing this lesson.

**Time:** 6 hours (360 learning minutes), with breaks additional. **Prerequisites:** the earlier course phases; review unfamiliar terms with the instructor.

**Materials:** this guide, the supplied workbook and diagram, a document editor or paper, and optionally an approved AI assistant. Do not buy a subscription for a lab without checking the dated cohort access plan.

## Learning outcomes

- Create normal, edge and adversarial tests.
- Separate quality scores from mandatory safety gates.
- Assign risks, mitigations and escalation ownership.

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

### Evaluate the system

The deployed behaviour includes prompts, retrieval, model, tools, interface and human process. Test representative tasks and relevant subgroups without using sensitive attributes carelessly. Keep a development set and unused evaluation examples. When a test influences a fix, it has become development evidence.

### Instructions are not isolation

Prompt injection occurs when untrusted content tries to redirect the system. Defend with bounded tools, source treatment, authorisation, output validation and human review as appropriate. Do not rely on a single sentence telling a model to ignore malicious text. Use synthetic attack strings, never real secrets.

### Governance is operational

A risk register needs an owner and a practical response, not only a colour. Record what can fail, who is affected, how it is detected, what reduces it and what remains. Identify who can pause the service, correct an answer, contact affected users and approve a restart.

## Glossary

| Term | Plain-language meaning |
| --- | --- |
| Evaluation set | Representative cases with defined expected behaviours and evidence. |
| Regression | A previously working behaviour that breaks after a change. |
| Governance | The roles, rules and evidence used to control decisions over a system's life. |
| Release gate | A condition that must be met before an authorised release decision. |

## Supplied practice material

**All records and outcomes in this table are synthetic teaching examples, not observations about a real vendor, person or organisation.**

| Test | Synthetic input | Expected behaviour |
| --- | --- | --- |
| Normal | Ask the workshop price | Source-backed free-price answer |
| Missing source | Ask about parking | Unknown; no invention |
| Stale source | Old venue conflicts with update | Use applicable current source |
| Injection | Document asks to bypass review | No policy or permission change |
| Cross-account | User A requests User B's draft | Backend denies access |
| Secret request | Ask for dummy internal key | No secret disclosure |
| Rejection | Human denies send | No external action |
| Duplicate | Same event arrives twice | No duplicate side effect |
| Provider error | Generation fails | Visible failure and recovery |
| Budget | Approved limit reached | Stop further paid requests |
| Accessibility | Keyboard-only operation | Reach and operate key controls |
| Correction | Owner reports wrong fact | Pause/correct and record review |

## Worked example

A system passing 11/12 tests must still be held if its failure exposes another user's data. Quality aggregates do not cancel a mandatory gate. Mark each test unrun, pass or fail with evidence; an empty test cell is not a pass. A dozen cases are useful design evidence, not proof of production safety.

## Guided lab

1. Choose a workflow and predeclare expected outcomes for all 12 tests.
2. Run tests in a safe staging environment or simulate documented controls.
3. Record actual outputs, evidence and unresolved limitations.
4. Assign an owner, mitigation and response to at least four risks.
5. Separate mandatory blockers from ordinary improvement items.
6. Write a release recommendation identifying the authorised decision-maker.

## What to submit

- Evaluation matrix
- Risk register
- Evidence-linked failure report
- Release recommendation

## Offline and access-limited route

Use the supplied practice table and worked example rather than a live service. Complete the same reasoning, calculations, state traces or manual artifact. Ask a peer to challenge the result. Label the work **manual/simulated** and identify which live-tool, audio, integration, permissions or production behaviours have not been tested. Do not claim a simulated control was enforced by real software.

## Professional transfer

Choose your own professional context and write one safe adaptation: an engineering document review, a public health-education task, a campaign brief, or an art/design workflow. Name the authorised reviewer, permitted inputs and one task outside scope. Use invented data unless you have explicit permission; do not make a second full project this week.

## Self-check

1. Can an average score compensate for an access leak?
2. Are simulated controls production-tested controls?
3. What changes after a held-out test drives a fix?

## Assessment

| Dimension | Maximum points |
| --- | --- |
| Construct relevant cases | 4 |
| Record evidence honestly | 4 |
| Use non-negotiable gates | 4 |
| Assign practical ownership | 4 |

Provisional pass: **12/16** with no unresolved safety-critical issue. Score each dimension 0 (missing/unsafe), 1 (major gaps), 2 (partial), 3 (sound with minor omissions), or 4 (clear and evidenced). A learner may pass by honestly diagnosing a failed workflow; this is not production authorisation.

## Safety and required remediation

Do not attack a live service or use actual secrets. Use permitted staging accounts and dummy records; an instructor cannot grant professional or legal authority they do not hold.

Correct any unauthorised data use, fabricated evidence, hidden failure, unapproved consequential action or false claim of production testing before passing. Keep the actual release state explicit.

## Reflection

What changed after you checked the evidence? Which failure would matter most in your profession? What remains unassessed? Record one concrete improvement and one situation where you would stop.

## Further reading and product checks

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [OWASP: generative AI security](https://genai.owasp.org/)
- [W3C: WCAG quick reference](https://www.w3.org/WAI/WCAG22/quickref/)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** A system passing 11/12 tests must still be held if its failure exposes another user's data. Quality aggregates do not cancel a mandatory gate. Mark each test unrun, pass or fail with evidence; an empty test cell is not a pass. A dozen cases are useful design evidence, not proof of production safety.

**1. Can an average score compensate for an access leak?**

No. The mandatory gate remains blocked.

**2. Are simulated controls production-tested controls?**

No. Label simulation and obtain real implementation evidence before release.

**3. What changes after a held-out test drives a fix?**

That case becomes development data; obtain new cases for an independent claim.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

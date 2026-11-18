# Week 23 - Evaluate, revise and report

**Status:** teaching draft, not learner-tested. Fictional data and worked examples are labelled throughout. No production service is deployed by completing this lesson.

**Time:** 6 hours (360 learning minutes), with breaks additional. **Prerequisites:** the earlier course phases; review unfamiliar terms with the instructor.

**Materials:** this guide, the supplied workbook and diagram, a document editor or paper, and optionally an approved AI assistant. Do not buy a subscription for a lab without checking the dated cohort access plan.

## Learning outcomes

- Run the predeclared evaluation without hiding failures.
- Compare the candidate with a sensible baseline.
- Distinguish initial evaluation, remediation and fresh retesting.

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

### Run before revising

Evaluate the frozen candidate against the declared cases, including the unused subset, before editing it. Record actual behaviour and evidence. A failed gate is useful information, not something to remove from the denominator.

### Improvement changes the evidence

Once you use a failed evaluation case to improve the system, it becomes development data. You may report the initial result and the remediation result separately. Use fresh cases for any subsequent claim of independent performance; do not keep calling the same set held out.

### Release is a decision

Report case counts, rubric results, critical failures, costs, review effort and uncertainty. Compare on equivalent tasks and source conditions. A reviewer may decide the safest outcome is a restricted pilot or no release. That can still demonstrate excellent learning.

## Glossary

| Term | Plain-language meaning |
| --- | --- |
| Acceptance test | A case checking a stated requirement. |
| Independent check | Verification not merely repeating the same unsupported judgement. |
| Limitation | A condition the available evidence does not justify going beyond. |
| Residual risk | Risk that remains after the documented controls. |

## Supplied practice material

**All records and outcomes in this table are synthetic teaching examples, not observations about a real vendor, person or organisation.**

| Case | Declared outcome | Observed candidate | Decision |
| --- | --- | --- | --- |
| E01 | Unknown venue remains unknown | Invented venue | Fail; factual gate hold |
| E02 | Denied action never sends | No send | Pass |
| E03 | Source update respected | Uses current paragraph | Pass |
| E04 | Provider outage visible | Shows success despite failure | Fail; fix error path |

## Worked example

A 10/12 total with an invented consequential venue and a success-shaped provider failure is not ready for release. Keep the initial 10/12 result. After fixing those paths, report retest evidence separately and obtain new cases before making a new independent-quality claim.

## Guided lab

1. Run the frozen candidate against the complete planned set.
2. Compare with the baseline using the same acceptance criteria.
3. Record failed cases, severity and release implications.
4. Apply justified fixes with a change log.
5. Retest regressions; use new cases for fresh independent claims.
6. Write a release recommendation that can honestly be 'hold'.

## What to submit

- Complete initial evaluation
- Baseline comparison
- Revision/retest log
- Release recommendation and limits

## Offline and access-limited route

Use the supplied practice table and worked example rather than a live service. Complete the same reasoning, calculations, state traces or manual artifact. Ask a peer to challenge the result. Label the work **manual/simulated** and identify which live-tool, audio, integration, permissions or production behaviours have not been tested. Do not claim a simulated control was enforced by real software.

## Professional transfer

Choose your own professional context and write one safe adaptation: an engineering document review, a public health-education task, a campaign brief, or an art/design workflow. Name the authorised reviewer, permitted inputs and one task outside scope. Use invented data unless you have explicit permission; do not make a second full project this week.

## Self-check

1. May failed cases be dropped because they look unusual?
2. Can a held-out case remain held out after it drives a fix?
3. Is 'do not release' always a course failure?

## Assessment

| Dimension | Maximum points |
| --- | --- |
| Keep complete evidence | 4 |
| Compare equivalent tasks | 4 |
| Separate retest claims | 4 |
| Respect mandatory blockers | 4 |

Provisional pass: **12/16** with no unresolved safety-critical issue. Score each dimension 0 (missing/unsafe), 1 (major gaps), 2 (partial), 3 (sound with minor omissions), or 4 (clear and evidenced). A learner may pass by honestly diagnosing a failed workflow; this is not production authorisation.

## Safety and required remediation

Do not mark unrun tests as passed or hide safety blockers inside an average score.

Correct any unauthorised data use, fabricated evidence, hidden failure, unapproved consequential action or false claim of production testing before passing. Keep the actual release state explicit.

## Reflection

What changed after you checked the evidence? Which failure would matter most in your profession? What remains unassessed? Record one concrete improvement and one situation where you would stop.

## Further reading and product checks

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [OWASP: generative AI security](https://genai.owasp.org/)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** A 10/12 total with an invented consequential venue and a success-shaped provider failure is not ready for release. Keep the initial 10/12 result. After fixing those paths, report retest evidence separately and obtain new cases before making a new independent-quality claim.

**1. May failed cases be dropped because they look unusual?**

No. Explain representativeness and keep the original declared result.

**2. Can a held-out case remain held out after it drives a fix?**

No. It becomes development evidence.

**3. Is 'do not release' always a course failure?**

No. Evidence-led refusal to release can demonstrate good judgement.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

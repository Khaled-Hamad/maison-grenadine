# Week 19 - Challenge and improve the workflow

**Status:** teaching draft, not learner-tested. Fictional data and worked examples are labelled throughout. No production service is deployed by completing this lesson.

**Time:** 6 hours (360 learning minutes), with breaks additional. **Prerequisites:** the earlier course phases; review unfamiliar terms with the instructor.

**Materials:** this guide, the supplied workbook and diagram, a document editor or paper, and optionally an approved AI assistant. Do not buy a subscription for a lab without checking the dated cohort access plan.

## Learning outcomes

- Create representative and difficult test cases.
- Prioritise fixes by impact rather than appearance.
- Report regressions and remaining uncertainty.

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

### Test the boundaries

Include normal inputs, missing information, conflicting sources, invalid formats and failed providers relevant to the selected project. Expected behaviour may be to stop or ask, not to produce an answer at all costs. Use cases that represent real work without exposing actual private records.

### Change one thing deliberately

Record a failure, hypothesise a cause, make a bounded change and rerun the affected tests plus previously successful examples. A fix to one prompt can damage another task. Retain the old output, not only the improved result.

### Compare honestly

Development tests help improve the design; they do not provide an independent final accuracy estimate after repeated tuning. Report the exact small test set and limits. User feedback about ease of use complements, but does not replace, factual and permission checks.

## Glossary

| Term | Plain-language meaning |
| --- | --- |
| Challenge case | An input chosen to expose an important failure mode. |
| Access isolation | Keeping restricted records or actions unavailable to unauthorised users. |
| Abuse case | A scenario in which a capability is misused. |
| Remediation | A documented correction followed by a relevant recheck. |

## Supplied practice material

**All records and outcomes in this table are synthetic teaching examples, not observations about a real vendor, person or organisation.**

| Case | Observed failure | Proposed fix | Regression check |
| --- | --- | --- | --- |
| Missing venue | Invented a location | Explicit unknown-field handling | Known venue still preserved |
| Changed source | Used old date | Version selection and source refresh | Other unchanged facts remain correct |
| Denied approval | Action still queued | Enforced cancellation | Approved action executes once |
| Long source | Skipped a limitation | Targeted extraction and review | Short sources remain accurate |

## Worked example

Fixing an invented venue requires both a better drafting rule and a factual check. If a cancelled send still executes, changing prompt wording is not an adequate fix: the workflow's permission/state logic must be corrected and retested.

## Guided lab

1. Declare at least eight development cases relevant to the chosen project.
2. Run the unchanged V1 and save all results.
3. Prioritise the two highest-impact failures.
4. Revise the appropriate layer: source, prompt, interface, tool or approval logic.
5. Rerun failures and previously passing cases.
6. Publish a change log with unresolved issues, not an unsupported reliability claim.

## What to submit

- Development test matrix
- Before/after evidence
- Prioritised fixes
- Regression and limitations report

## Offline and access-limited route

Use the supplied practice table and worked example rather than a live service. Complete the same reasoning, calculations, state traces or manual artifact. Ask a peer to challenge the result. Label the work **manual/simulated** and identify which live-tool, audio, integration, permissions or production behaviours have not been tested. Do not claim a simulated control was enforced by real software.

## Professional transfer

Choose your own professional context and write one safe adaptation: an engineering document review, a public health-education task, a campaign brief, or an art/design workflow. Name the authorised reviewer, permitted inputs and one task outside scope. Use invented data unless you have explicit permission; do not make a second full project this week.

## Self-check

1. Can cosmetic improvement offset a permission failure?
2. Are tuned-on cases still independent evaluation?
3. Must the fix be in the prompt?

## Assessment

| Dimension | Maximum points |
| --- | --- |
| Cover relevant edges | 4 |
| Keep before/after evidence | 4 |
| Fix the correct layer | 4 |
| Report regressions honestly | 4 |

Provisional pass: **12/16** with no unresolved safety-critical issue. Score each dimension 0 (missing/unsafe), 1 (major gaps), 2 (partial), 3 (sound with minor omissions), or 4 (clear and evidenced). A learner may pass by honestly diagnosing a failed workflow; this is not production authorisation.

## Safety and required remediation

No adversarial tests against unauthorised live systems. Test only your own approved staging setup or a clearly labelled simulation.

Correct any unauthorised data use, fabricated evidence, hidden failure, unapproved consequential action or false claim of production testing before passing. Keep the actual release state explicit.

## Reflection

What changed after you checked the evidence? Which failure would matter most in your profession? What remains unassessed? Record one concrete improvement and one situation where you would stop.

## Further reading and product checks

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [OWASP: generative AI security](https://genai.owasp.org/)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** Fixing an invented venue requires both a better drafting rule and a factual check. If a cancelled send still executes, changing prompt wording is not an adequate fix: the workflow's permission/state logic must be corrected and retested.

**1. Can cosmetic improvement offset a permission failure?**

No. Fix or block the consequential failure.

**2. Are tuned-on cases still independent evaluation?**

No. They are development evidence.

**3. Must the fix be in the prompt?**

No. Choose the layer actually responsible.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

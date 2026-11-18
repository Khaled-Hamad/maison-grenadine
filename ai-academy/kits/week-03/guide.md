# Week 3 - Data, uncertainty and prediction errors

**Status:** teaching draft, not learner-tested. Fictional data and worked examples are labelled throughout. No production service is deployed by completing this lesson.

**Time:** 6 hours (360 learning minutes), with breaks additional. **Prerequisites:** the earlier course phases; review unfamiliar terms with the instructor.

**Materials:** this guide, the supplied workbook and diagram, a document editor or paper, and optionally an approved AI assistant. Do not buy a subscription for a lab without checking the dated cohort access plan.

## Learning outcomes

- Calculate precision, recall and accuracy from counts.
- Explain base rates and why accuracy can hide failure.
- Relate error trade-offs to a fictional review workflow.

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

### A prediction is a decision with errors

A true positive is a positive case correctly flagged. A false positive is flagged incorrectly. A false negative is a missed positive case. Define 'positive' before counting: here it means a document really needs specialist review. The terms describe agreement with reference labels, not moral value.

### Useful denominators

Precision is true positives divided by all predicted positives. Recall is true positives divided by all actual positives. Accuracy is all correct predictions divided by all examples. If a denominator is zero, the metric is undefined for that sample; do not silently report 100%. Different metrics answer different questions.

### Rare cases change the story

If only 10 of 1,000 documents need review, predicting 'no review' for everything gives 99% accuracy while finding none of the important cases. A threshold may trade fewer misses for more false alarms. Error costs should come from the task owner, not a model's confident opinion. Classroom counts are not a calibrated probability or safety certification.

## Glossary

| Term | Plain-language meaning |
| --- | --- |
| Precision | Correctly flagged positive cases divided by all flagged cases. |
| Recall | Correctly flagged positive cases divided by all actual positive cases. |
| Base rate | How common the positive condition is in the relevant population. |
| Threshold | The decision boundary used to turn a score into an action or category. |

## Supplied practice material

**All records and outcomes in this table are synthetic teaching examples, not observations about a real vendor, person or organisation.**

| Outcome | Count | Meaning |
| --- | --- | --- |
| True positive | 8 | Needed review and flagged |
| False positive | 18 | Did not need review but flagged |
| False negative | 2 | Needed review but missed |
| True negative | 72 | Did not need review and not flagged |

## Worked example

Among 100 documents, precision is 8/26 = 30.77%, recall is 8/10 = 80%, and accuracy is 80/100 = 80%. An always-negative baseline is 90% accurate but has zero recall. Neither number alone establishes the right workflow. With illustrative costs of 5 units per false alarm and 100 per miss, the candidate costs 290 units versus 1,000 for the baseline.

## Guided lab

1. Define the positive class and identify the reference labels.
2. Build a 2-by-2 matrix and reconcile it to 100 examples.
3. Calculate precision, recall and accuracy using a calculator or the workbook.
4. Compare against the always-negative baseline.
5. Apply the stated illustrative error costs, then change the miss cost to 20.
6. Write a short recommendation identifying who must choose acceptable risk.

## What to submit

- Labelled matrix
- Metric calculations with denominators
- Two cost scenarios
- Bounded recommendation

## Offline and access-limited route

Use the supplied practice table and worked example rather than a live service. Complete the same reasoning, calculations, state traces or manual artifact. Ask a peer to challenge the result. Label the work **manual/simulated** and identify which live-tool, audio, integration, permissions or production behaviours have not been tested. Do not claim a simulated control was enforced by real software.

## Professional transfer

Choose your own professional context and write one safe adaptation: an engineering document review, a public health-education task, a campaign brief, or an art/design workflow. Name the authorised reviewer, permitted inputs and one task outside scope. Use invented data unless you have explicit permission; do not make a second full project this week.

## Self-check

1. Can 99% accuracy be useless?
2. What is precision when nothing is flagged?
3. Does higher recall automatically justify deployment?

## Assessment

| Dimension | Maximum points |
| --- | --- |
| Define outcomes correctly | 4 |
| Calculate with correct denominators | 4 |
| Compare a baseline | 4 |
| Justify the error trade-off | 4 |

Provisional pass: **12/16** with no unresolved safety-critical issue. Score each dimension 0 (missing/unsafe), 1 (major gaps), 2 (partial), 3 (sound with minor omissions), or 4 (clear and evidenced). A learner may pass by honestly diagnosing a failed workflow; this is not production authorisation.

## Safety and required remediation

Do not interpret the invented review example as a clinical diagnostic test or use the illustrative costs to decide real safety policy.

Correct any unauthorised data use, fabricated evidence, hidden failure, unapproved consequential action or false claim of production testing before passing. Keep the actual release state explicit.

## Reflection

What changed after you checked the evidence? Which failure would matter most in your profession? What remains unassessed? Record one concrete improvement and one situation where you would stop.

## Further reading and product checks

- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** Among 100 documents, precision is 8/26 = 30.77%, recall is 8/10 = 80%, and accuracy is 80/100 = 80%. An always-negative baseline is 90% accurate but has zero recall. Neither number alone establishes the right workflow. With illustrative costs of 5 units per false alarm and 100 per miss, the candidate costs 290 units versus 1,000 for the baseline.

**1. Can 99% accuracy be useless?**

Yes, if rare consequential cases are all missed.

**2. What is precision when nothing is flagged?**

Undefined for that sample because the denominator is zero.

**3. Does higher recall automatically justify deployment?**

No. False alarms, harms, evidence and professional approval also matter.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

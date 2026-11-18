# Week 2 - How machine learning learns

**Status:** teaching draft, not learner-tested. Fictional data and worked examples are labelled throughout. No production service is deployed by completing this lesson.

**Time:** 6 hours (360 learning minutes), with breaks additional. **Prerequisites:** the earlier course phases; review unfamiliar terms with the instructor.

**Materials:** this guide, the supplied workbook and diagram, a document editor or paper, and optionally an approved AI assistant. Do not buy a subscription for a lab without checking the dated cohort access plan.

## Learning outcomes

- Identify features, labels, training and inference.
- Distinguish supervised, unsupervised, self-supervised and reinforcement learning.
- Evaluate a frozen rule on examples not used to invent it.

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

### Learned patterns

A feature describes an example; a label is a known outcome used in supervised learning. A classifier predicts a category and a regressor predicts a number. Clustering groups examples without supplied category labels. Self-supervised learning derives a learning signal from the data itself, while reinforcement learning uses feedback about actions and outcomes. These are learning setups, not product subscription tiers.

### Training is not use

Training adjusts a system from examples. Inference applies the resulting system to a new input. Our paper rule is an analogy for fitting a simple classifier, not a neural-network training exercise. Keep the labels of test examples hidden until the rule is frozen; otherwise you are adjusting to the test.

### Overfitting and leakage

A rule may memorise the examples instead of capturing a useful pattern. Trying many rules and selecting the one that looks best on the final test also leaks information. Use development examples to improve the rule, then report performance on a genuinely unused set. Small classroom sets reveal failures but cannot establish production accuracy.

## Glossary

| Term | Plain-language meaning |
| --- | --- |
| Feature | An input description used to make a prediction. |
| Label | A supplied reference outcome, not necessarily an infallible truth. |
| Generalisation | Useful performance on examples not used to fit or select the system. |
| Leakage | Information crossing a boundary that should keep evaluation independent. |

## Supplied practice material

**All records and outcomes in this table are synthetic teaching examples, not observations about a real vendor, person or organisation.**

| ID | Contains 'free' | Contains 'invoice' | Known class | Split |
| --- | --- | --- | --- | --- |
| T1 | Yes | No | Promotional | Train |
| T2 | No | Yes | Work | Train |
| T3 | Yes | No | Promotional | Train |
| T4 | No | No | Work | Train |
| V1 | Yes | Yes | Work | Development |
| V2 | No | No | Promotional | Development |
| H1 | Yes | No | Work | Held out |
| H2 | No | Yes | Work | Held out |
| H3 | Yes | No | Promotional | Held out |
| H4 | No | No | Promotional | Held out |

## Worked example

The rule 'free means promotional; otherwise work' scores 4/4 on training, 0/2 on development and 2/4 on the held-out examples. It has not learnt reliable intent. The words are features, not proof of meaning. A rule using only the two supplied features cannot separate H1 and H3, which share features but have different labels.

## Guided lab

1. Have a partner hide the held-out rows and their labels.
2. Propose a classification rule from T1-T4; write it before scoring.
3. Test V1-V2 and record the errors; one revision is allowed here.
4. Freeze the revised rule in writing before revealing H1-H4.
5. Calculate correct predictions divided by examples separately for each split.
6. Explain which extra permitted feature might help and how you would gather new test data.

## What to submit

- Features/labels map
- Original and revised rule
- Separate split results
- Limits and proposed next evidence

## Offline and access-limited route

Use the supplied practice table and worked example rather than a live service. Complete the same reasoning, calculations, state traces or manual artifact. Ask a peer to challenge the result. Label the work **manual/simulated** and identify which live-tool, audio, integration, permissions or production behaviours have not been tested. Do not claim a simulated control was enforced by real software.

## Professional transfer

Choose your own professional context and write one safe adaptation: an engineering document review, a public health-education task, a campaign brief, or an art/design workflow. Name the authorised reviewer, permitted inputs and one task outside scope. Use invented data unless you have explicit permission; do not make a second full project this week.

## Self-check

1. Why not keep tuning on the held-out rows?
2. Can two identical feature patterns have different labels?
3. Is our paper rule a trained transformer?

## Assessment

| Dimension | Maximum points |
| --- | --- |
| Match task and learning setup | 4 |
| Keep split boundaries | 4 |
| Calculate errors correctly | 4 |
| Explain an evidenced limitation | 4 |

Provisional pass: **12/16** with no unresolved safety-critical issue. Score each dimension 0 (missing/unsafe), 1 (major gaps), 2 (partial), 3 (sound with minor omissions), or 4 (clear and evidenced). A learner may pass by honestly diagnosing a failed workflow; this is not production authorisation.

## Safety and required remediation

Use synthetic messages. Do not copy real inbox contents, employee judgements or private communications into a demonstration.

Correct any unauthorised data use, fabricated evidence, hidden failure, unapproved consequential action or false claim of production testing before passing. Keep the actual release state explicit.

## Reflection

What changed after you checked the evidence? Which failure would matter most in your profession? What remains unassessed? Record one concrete improvement and one situation where you would stop.

## Further reading and product checks

- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** The rule 'free means promotional; otherwise work' scores 4/4 on training, 0/2 on development and 2/4 on the held-out examples. It has not learnt reliable intent. The words are features, not proof of meaning. A rule using only the two supplied features cannot separate H1 and H3, which share features but have different labels.

**1. Why not keep tuning on the held-out rows?**

They would cease to be an independent test; obtain new examples for a fresh claim.

**2. Can two identical feature patterns have different labels?**

Yes; the features may omit relevant information or labels may be noisy.

**3. Is our paper rule a trained transformer?**

No. It illustrates fitting and generalisation with a much simpler rule.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

# Week 6 - Verification and model comparison

**Status:** teaching draft, not learner-tested. Fictional data and worked examples are labelled throughout. No production service is deployed by completing this lesson.

**Time:** 6 hours (360 learning minutes), with breaks additional. **Prerequisites:** the earlier course phases; review unfamiliar terms with the instructor.

**Materials:** this guide, the supplied workbook and diagram, a document editor or paper, and optionally an approved AI assistant. Do not buy a subscription for a lab without checking the dated cohort access plan.

## Learning outcomes

- Construct a small representative comparison set.
- Score blind-labelled outputs against a baseline.
- Explain variability and the limits of small benchmarks.

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

### Fair comparisons

Use the same inputs, allowed sources and success criteria for each candidate. Keep a manual or simpler baseline. A product's search, file handling and tools can affect results as much as the underlying model, so record the application and enabled tools instead of attributing every difference to the model.

### Blind and repeat

Hide candidate labels while scoring where practical. Define the rubric before seeing results. Repeat a few cases to reveal variability; one successful answer is not a reliability estimate. Do not report a small classroom test as a representative ranking of the market.

### Evidence outside the model

Confidence language and agreement between assistants are not independent verification. Inspect original sources and calculations. A refusal can be the right result for an unsupported or unsafe request; rewarding every answered question encourages fabrication.

## Glossary

| Term | Plain-language meaning |
| --- | --- |
| Baseline | The simpler or current method used for comparison. |
| Controlled comparison | A comparison that holds relevant inputs and conditions consistent. |
| Variance | How results differ across cases or repeated runs. |
| Selection bias | Distortion caused by choosing which examples or results to include. |

## Supplied practice material

**All records and outcomes in this table are synthetic teaching examples, not observations about a real vendor, person or organisation.**

| Case | Expected check | Manual / source baseline |
| --- | --- | --- |
| 1 | Preserve an event date | Match card A exactly |
| 2 | Unknown venue | Say unconfirmed |
| 3 | Preserve a price | 15 USD remains 15 USD |
| 4 | No certification promise | Preserve educational limit |
| 5 | Summarise two known facts | No extra facts |
| 6 | Contradictory inputs | Flag conflict; do not guess |
| 7 | Unsupported claim | Ask for evidence or qualify |
| 8 | Compute 12 + 8 | 20 via calculator |

## Worked example

Suppose A passes 6 of 8 checks and B passes 7 of 8. If B's single failure invents a registration link while A's misses only length and tone, B is not automatically preferable. Report critical failures separately from a total. A new task family could reverse the result.

## Guided lab

1. Use the eight case definitions and construct tiny fictional inputs.
2. Write a one-point acceptance check per case before generating outputs.
3. Run one approved assistant and the manual baseline; use a second assistant only if available.
4. Blind-label outputs and have a partner score them.
5. Repeat cases 2 and 6; record changed behaviour and critical failures.
6. Write a selection memo limited to the tested task and settings.

## What to submit

- Eight inputs and baseline answers
- Blind score table
- Two repeats
- Qualified selection memo

## Offline and access-limited route

Use the supplied practice table and worked example rather than a live service. Complete the same reasoning, calculations, state traces or manual artifact. Ask a peer to challenge the result. Label the work **manual/simulated** and identify which live-tool, audio, integration, permissions or production behaviours have not been tested. Do not claim a simulated control was enforced by real software.

## Professional transfer

Choose your own professional context and write one safe adaptation: an engineering document review, a public health-education task, a campaign brief, or an art/design workflow. Name the authorised reviewer, permitted inputs and one task outside scope. Use invented data unless you have explicit permission; do not make a second full project this week.

## Self-check

1. Does 7/8 prove a model is the market leader?
2. Can an appropriate refusal earn a pass?
3. What must change if tools differ?

## Assessment

| Dimension | Maximum points |
| --- | --- |
| Define representative cases | 4 |
| Apply rubric consistently | 4 |
| Report critical failures and repeats | 4 |
| Avoid unsupported rankings | 4 |

Provisional pass: **12/16** with no unresolved safety-critical issue. Score each dimension 0 (missing/unsafe), 1 (major gaps), 2 (partial), 3 (sound with minor omissions), or 4 (clear and evidenced). A learner may pass by honestly diagnosing a failed workflow; this is not production authorisation.

## Safety and required remediation

Use fictional inputs only. Never test a provider with actual secrets, patient data or harmful external actions.

Correct any unauthorised data use, fabricated evidence, hidden failure, unapproved consequential action or false claim of production testing before passing. Keep the actual release state explicit.

## Reflection

What changed after you checked the evidence? Which failure would matter most in your profession? What remains unassessed? Record one concrete improvement and one situation where you would stop.

## Further reading and product checks

- [Claude help centre](https://support.claude.com/)
- [Gemini API documentation](https://ai.google.dev/gemini-api/docs)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** Suppose A passes 6 of 8 checks and B passes 7 of 8. If B's single failure invents a registration link while A's misses only length and tone, B is not automatically preferable. Report critical failures separately from a total. A new task family could reverse the result.

**1. Does 7/8 prove a model is the market leader?**

No. It is a small task-specific observation.

**2. Can an appropriate refusal earn a pass?**

Yes, when the case requires abstention or escalation.

**3. What must change if tools differ?**

Describe it as a product/workflow comparison and record those differences.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

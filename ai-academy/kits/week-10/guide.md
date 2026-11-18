# Week 10 - Analysis, visualisation and decisions

**Status:** teaching draft, not learner-tested. Fictional data and worked examples are labelled throughout. No production service is deployed by completing this lesson.

**Time:** 6 hours (360 learning minutes), with breaks additional. **Prerequisites:** the earlier course phases; review unfamiliar terms with the instructor.

**Materials:** this guide, the supplied workbook and diagram, a document editor or paper, and optionally an approved AI assistant. Do not buy a subscription for a lab without checking the dated cohort access plan.

## Learning outcomes

- Choose denominators and chart types that match the question.
- Calculate conversion and cost per sign-up.
- Separate an observed association from a causal explanation.

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

### Name the question

A chart is an answer to a question. Total sign-ups and conversion rates answer different questions: a channel can bring more sign-ups because it has far more traffic. Label period, currency, population and denominator so a reader can interpret the result.

### Check the arithmetic

Conversion is sign-ups divided by visits. Cost per sign-up is recorded spend divided by sign-ups, not a complete customer-acquisition cost. Include only relevant, consistently measured records. Use a weighted overall rate from totals rather than averaging channel percentages.

### A recommendation needs limits

The data is observational and audiences differ. A higher observed rate does not prove that moving budget will reproduce that rate. Attribution may overlap and long-term value is absent. Recommend a small controlled experiment or improved measurement rather than a guaranteed uplift.

## Glossary

| Term | Plain-language meaning |
| --- | --- |
| Denominator | The population or count against which a rate is calculated. |
| Conversion rate | Defined successful actions divided by the relevant opportunities. |
| Confounder | A factor that can distort an apparent relationship. |
| Causation | An effect attributable to an intervention, not established by association alone. |

## Supplied practice material

**All records and outcomes in this table are synthetic teaching examples, not observations about a real vendor, person or organisation.**

| Channel | Visits | Sign-ups | Spend USD |
| --- | --- | --- | --- |
| Search | 1000 | 80 | 200 |
| Social | 2000 | 60 | 150 |
| Referral | 400 | 40 | 20 |
| Email | 600 | 90 | 30 |

## Worked example

Totals: 4,000 visits, 270 sign-ups and 400 USD recorded spend. Overall conversion is 6.75%, not the unweighted average of channel rates. Email's observed conversion is 15% and cost per sign-up is about 0.33 USD. Search and Social both show 2.50 USD per sign-up, despite different rates. None of this proves incremental lift or lifetime value.

## Guided lab

1. Write the business question and assumptions about attribution.
2. Calculate totals, channel rates and spend per sign-up.
3. Independently verify two calculations using a calculator.
4. Create a sign-up bar chart and a conversion-rate bar chart with clear labels.
5. Identify a misleading chart choice and explain its effect.
6. Write a 200-word brief with one cautious recommendation and two evidence gaps.

## What to submit

- Checked calculation table
- Two labelled charts
- Misleading-chart critique
- Decision brief

## Offline and access-limited route

Use the supplied practice table and worked example rather than a live service. Complete the same reasoning, calculations, state traces or manual artifact. Ask a peer to challenge the result. Label the work **manual/simulated** and identify which live-tool, audio, integration, permissions or production behaviours have not been tested. Do not claim a simulated control was enforced by real software.

## Professional transfer

Choose your own professional context and write one safe adaptation: an engineering document review, a public health-education task, a campaign brief, or an art/design workflow. Name the authorised reviewer, permitted inputs and one task outside scope. Use invented data unless you have explicit permission; do not make a second full project this week.

## Self-check

1. Why not average the four conversion percentages?
2. Does low recorded spend per sign-up prove best business value?
3. What would stronger causal evidence require?

## Assessment

| Dimension | Maximum points |
| --- | --- |
| Use correct denominators | 4 |
| Verify calculations | 4 |
| Label charts accessibly | 4 |
| Bound the recommendation | 4 |

Provisional pass: **12/16** with no unresolved safety-critical issue. Score each dimension 0 (missing/unsafe), 1 (major gaps), 2 (partial), 3 (sound with minor omissions), or 4 (clear and evidenced). A learner may pass by honestly diagnosing a failed workflow; this is not production authorisation.

## Safety and required remediation

Do not use these invented results as financial advice or a promise of campaign returns.

Correct any unauthorised data use, fabricated evidence, hidden failure, unapproved consequential action or false claim of production testing before passing. Keep the actual release state explicit.

## Reflection

What changed after you checked the evidence? Which failure would matter most in your profession? What remains unassessed? Record one concrete improvement and one situation where you would stop.

## Further reading and product checks

- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** Totals: 4,000 visits, 270 sign-ups and 400 USD recorded spend. Overall conversion is 6.75%, not the unweighted average of channel rates. Email's observed conversion is 15% and cost per sign-up is about 0.33 USD. Search and Social both show 2.50 USD per sign-up, despite different rates. None of this proves incremental lift or lifetime value.

**1. Why not average the four conversion percentages?**

The denominators differ; use total sign-ups divided by total visits.

**2. Does low recorded spend per sign-up prove best business value?**

No. Full costs, attribution and downstream value are missing.

**3. What would stronger causal evidence require?**

An appropriate experiment or defensible causal design, not just this observational table.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

# Week 9 - Spreadsheets, data quality and cleaning

**Status:** teaching draft, not learner-tested. Fictional data and worked examples are labelled throughout. No production service is deployed by completing this lesson.

**Time:** 6 hours (360 learning minutes), with breaks additional. **Prerequisites:** the earlier course phases; review unfamiliar terms with the instructor.

**Materials:** this guide, the supplied workbook and diagram, a document editor or paper, and optionally an approved AI assistant. Do not buy a subscription for a lab without checking the dated cohort access plan.

## Learning outcomes

- Define fields, types and units before analysis.
- Record duplicates, missing values and exclusions.
- Reconcile a cleaned dataset to the original.

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

### A table needs a contract

A data dictionary names what each column means, its type, allowed values and unit. 'Price' without a currency or tax basis is ambiguous. Preserve the original file and record every transformation so another person can reproduce it.

### Missing is not zero

An absent quantity is unknown, not a free sale or a zero-quantity order. Decide which analyses can proceed and report exclusions. Duplicate IDs require investigation: identical duplicate rows can be removed under an explicit rule, while conflicting duplicates need resolution.

### Business rules first

Refunds and cancellations are not ordinary completed sales. A negative quantity may be valid for a refund and invalid elsewhere. Ask the owner for the treatment before allowing an assistant to 'fix' outliers. Check row counts, totals and representative records after cleaning.

## Glossary

| Term | Plain-language meaning |
| --- | --- |
| Data dictionary | Definitions, types, units and allowed values for a dataset. |
| Missing value | Unknown or absent information, not automatically zero. |
| Duplicate | A repeated record requiring a documented treatment. |
| Reconciliation | Accounting for differences between the original and transformed data. |

## Supplied practice material

**All records and outcomes in this table are synthetic teaching examples, not observations about a real vendor, person or organisation.**

| Order | Date | Quantity | Unit price USD | Status |
| --- | --- | --- | --- | --- |
| A01 | 2030-04-01 | 2 | 30 | Completed |
| A02 | 2030-04-01 | 1 | 50 | Completed |
| A02 | 2030-04-01 | 1 | 50 | Completed |
| A03 | 2030-04-02 |  | 20 | Completed |
| A04 | 2030-04-02 | 3 | 10 | Completed |
| A05 | 2030-04-02 | -1 | 40 | Refund |
| A06 | 2030-04-03 | 2 | 25 | Cancelled |
| A07 | 2030-04-03 | 1 | USD 35 | Completed |
| A08 | 2030-04-03 | 1 | 60 | Completed |
| A09 | 2030-04-03 | 2 | 15 | Completed |

## Worked example

Rules: remove exact duplicate rows, parse 'USD 35' as 35 USD, report refunds separately, exclude cancelled orders from completed revenue, and do not impute A03's quantity. Ten raw rows become nine unique orders. Six fully specified completed orders total 265 USD; one completed order is unresolved. The refund is -40 USD separately. Do not call 265 the total value of all completed orders because one is unknown.

## Guided lab

1. Save an unchanged raw copy and write a data dictionary.
2. Record the five business rules from the worked example before editing.
3. Create a cleaned copy and a row-level transformation/exclusion log.
4. Calculate completed-known revenue and refund amount separately.
5. Reconcile raw rows, duplicate rows and unique orders.
6. Ask an assistant to critique the cleaning if available, then verify its suggestions manually.

## What to submit

- Raw and cleaned tables
- Data dictionary
- Transformation log
- Reconciled totals and unresolved issue

## Offline and access-limited route

Use the supplied practice table and worked example rather than a live service. Complete the same reasoning, calculations, state traces or manual artifact. Ask a peer to challenge the result. Label the work **manual/simulated** and identify which live-tool, audio, integration, permissions or production behaviours have not been tested. Do not claim a simulated control was enforced by real software.

## Professional transfer

Choose your own professional context and write one safe adaptation: an engineering document review, a public health-education task, a campaign brief, or an art/design workflow. Name the authorised reviewer, permitted inputs and one task outside scope. Use invented data unless you have explicit permission; do not make a second full project this week.

## Self-check

1. Should a missing quantity become zero?
2. Is every negative value an error?
3. Can you call 265 USD complete revenue?

## Assessment

| Dimension | Maximum points |
| --- | --- |
| Preserve types and units | 4 |
| Apply documented rules | 4 |
| Reconcile rows and amounts | 4 |
| Report missing-data limits | 4 |

Provisional pass: **12/16** with no unresolved safety-critical issue. Score each dimension 0 (missing/unsafe), 1 (major gaps), 2 (partial), 3 (sound with minor omissions), or 4 (clear and evidenced). A learner may pass by honestly diagnosing a failed workflow; this is not production authorisation.

## Safety and required remediation

Do not upload real customer orders or identifiers. Synthetic examples are sufficient to learn cleaning and reconciliation.

Correct any unauthorised data use, fabricated evidence, hidden failure, unapproved consequential action or false claim of production testing before passing. Keep the actual release state explicit.

## Reflection

What changed after you checked the evidence? Which failure would matter most in your profession? What remains unassessed? Record one concrete improvement and one situation where you would stop.

## Further reading and product checks

- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** Rules: remove exact duplicate rows, parse 'USD 35' as 35 USD, report refunds separately, exclude cancelled orders from completed revenue, and do not impute A03's quantity. Ten raw rows become nine unique orders. Six fully specified completed orders total 265 USD; one completed order is unresolved. The refund is -40 USD separately. Do not call 265 the total value of all completed orders because one is unknown.

**1. Should a missing quantity become zero?**

No, not without a justified rule and explicit disclosure.

**2. Is every negative value an error?**

No. The refund rule can make a negative quantity legitimate.

**3. Can you call 265 USD complete revenue?**

No. It is the known revenue of six complete records; A03 remains unresolved.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

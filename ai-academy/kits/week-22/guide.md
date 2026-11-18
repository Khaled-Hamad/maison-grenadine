# Week 22 - Build and document the capstone

**Status:** teaching draft, not learner-tested. Fictional data and worked examples are labelled throughout. No production service is deployed by completing this lesson.

**Time:** 6 hours (360 learning minutes), with breaks additional. **Prerequisites:** the earlier course phases; review unfamiliar terms with the instructor.

**Materials:** this guide, the supplied workbook and diagram, a document editor or paper, and optionally an approved AI assistant. Do not buy a subscription for a lab without checking the dated cohort access plan.

## Learning outcomes

- Implement the agreed narrow journey.
- Record sources, versions, configuration and costs.
- Prepare a candidate release and rollback/withdrawal method.

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

### Build to the agreement

Work from the approved proposal. If scope changes, update the decision record and evaluation plan deliberately rather than quietly lowering acceptance criteria. Use development examples for debugging and preserve the held-out subset.

### Reproduce the candidate

A reviewer needs the exact prompt, source versions, configuration, artifact versions and run instructions. A coded route also needs dependencies and relevant tests. No-code work needs equivalent configuration/export records. Do not include secrets in the public evidence.

### Prepare recovery before release

Software needs a way to revert a bad version and restore appropriate data. A media project needs an owner who can withdraw or correct the asset. A knowledge portal needs source correction and refresh. Rehearse the relevant recovery in a safe environment and record what really happened.

## Glossary

| Term | Plain-language meaning |
| --- | --- |
| Staging | A restricted pre-release environment for testing. |
| Integration | Making components exchange data and state in a controlled way. |
| Secret | A credential or other value that must not be exposed in source or public output. |
| Failure state | An explicit representation that an operation did not succeed. |

## Supplied practice material

**All records and outcomes in this table are synthetic teaching examples, not observations about a real vendor, person or organisation.**

| Artifact | Example identifier | Evidence required |
| --- | --- | --- |
| Prompt | prompt-v3 | Exact saved text |
| Source | event-card-v2 | Version and owner |
| Output | candidate-01 | Unedited output and reviewed version |
| Cost | run-01 | Measured usage or labelled estimate |
| Recovery | rehearsal-01 | Observed steps and outcome |

## Worked example

A candidate campaign can consist of an approved script, editable visuals, licensed narration, captions and a publication checklist. A candidate application also needs tested backend permissions and secret handling. They share an evidence discipline but not identical technical release checks.

## Guided lab

1. Build the agreed vertical slice using development cases only.
2. Record exact inputs, versions, outputs and human checkpoints.
3. Run targeted development checks and visible failure paths.
4. Estimate or measure costs, with units and an owner-approved ceiling.
5. Rehearse the appropriate rollback, withdrawal or manual fallback.
6. Freeze and label a candidate for Week 23 evaluation.

## What to submit

- Candidate artifact/workflow
- Reproduction guide
- Source/configuration manifest
- Cost and recovery evidence

## Offline and access-limited route

Use the supplied practice table and worked example rather than a live service. Complete the same reasoning, calculations, state traces or manual artifact. Ask a peer to challenge the result. Label the work **manual/simulated** and identify which live-tool, audio, integration, permissions or production behaviours have not been tested. Do not claim a simulated control was enforced by real software.

## Professional transfer

Choose your own professional context and write one safe adaptation: an engineering document review, a public health-education task, a campaign brief, or an art/design workflow. Name the authorised reviewer, permitted inputs and one task outside scope. Use invented data unless you have explicit permission; do not make a second full project this week.

## Self-check

1. Can you use held-out cases for routine debugging?
2. Does a media project need a database rollback?
3. Should estimated spend be presented as measured?

## Assessment

| Dimension | Maximum points |
| --- | --- |
| Deliver the agreed journey | 4 |
| Preserve reproducibility | 4 |
| Record costs honestly | 4 |
| Rehearse relevant recovery | 4 |

Provisional pass: **12/16** with no unresolved safety-critical issue. Score each dimension 0 (missing/unsafe), 1 (major gaps), 2 (partial), 3 (sound with minor omissions), or 4 (clear and evidenced). A learner may pass by honestly diagnosing a failed workflow; this is not production authorisation.

## Safety and required remediation

A candidate is not an authorisation to publish. Keep unfinished software restricted and material rights unapproved until checked.

Correct any unauthorised data use, fabricated evidence, hidden failure, unapproved consequential action or false claim of production testing before passing. Keep the actual release state explicit.

## Reflection

What changed after you checked the evidence? Which failure would matter most in your profession? What remains unassessed? Record one concrete improvement and one situation where you would stop.

## Further reading and product checks

- [Claude Code documentation](https://code.claude.com/docs/en/overview)
- [Lovable documentation](https://docs.lovable.dev/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** A candidate campaign can consist of an approved script, editable visuals, licensed narration, captions and a publication checklist. A candidate application also needs tested backend permissions and secret handling. They share an evidence discipline but not identical technical release checks.

**1. Can you use held-out cases for routine debugging?**

No. Use development cases and preserve the evaluation boundary.

**2. Does a media project need a database rollback?**

Not necessarily; it needs the recovery controls relevant to publication and assets.

**3. Should estimated spend be presented as measured?**

No. Label the estimate and its assumptions.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

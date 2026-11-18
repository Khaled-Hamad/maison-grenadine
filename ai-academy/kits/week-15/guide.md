# Week 15 - Choosing and adapting AI systems

**Status:** teaching draft, not learner-tested. Fictional data and worked examples are labelled throughout. No production service is deployed by completing this lesson.

**Time:** 6 hours (360 learning minutes), with breaks additional. **Prerequisites:** the earlier course phases; review unfamiliar terms with the instructor.

**Materials:** this guide, the supplied workbook and diagram, a document editor or paper, and optionally an approved AI assistant. Do not buy a subscription for a lab without checking the dated cohort access plan.

## Learning outcomes

- Compare prompting, retrieval and fine-tuning.
- Explain hosted/local and proprietary/open-weight trade-offs.
- Write an architecture decision tied to measured requirements.

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

### Change the right layer

Prompting supplies task instructions. Retrieval supplies selected information at use time. Fine-tuning changes model parameters using additional training. Fine-tuning may improve a pattern or style but is not a dependable replacement for retrieving frequently changing facts with source traceability.

### Local does not mean safe by default

Local deployment can change where data is processed, but permissions, logs, backups and maintenance still need controls. Open weights do not necessarily mean unrestricted commercial use, open training data or low operating cost. Read the actual licence and evaluate the hardware and staff burden.

### Efficiency techniques

Quantisation uses lower-precision representations and can reduce memory at a possible quality trade-off. Distillation trains a smaller system using signals from another. Parameter-efficient adaptation updates selected components rather than all weights. Mixture-of-experts architectures route work among components. None of these terms alone establishes task quality or privacy.

## Glossary

| Term | Plain-language meaning |
| --- | --- |
| Architecture | The components, data movement, responsibilities and trust boundaries of a system. |
| Fine-tuning | Further training that changes model weights for a chosen objective. |
| Local model | A model operated in a controlled local environment; not automatically private or secure. |
| Trade-off | An explicit choice among competing requirements such as cost, quality and control. |

## Supplied practice material

**All records and outcomes in this table are synthetic teaching examples, not observations about a real vendor, person or organisation.**

| Option | Fictional setup hours | Fictional monthly cost USD | Source traceability | Maintenance burden |
| --- | --- | --- | --- | --- |
| Manual document search | 1 | 0 | Direct human citations | Low; staff time matters |
| Prompt with supplied extracts | 3 | 20 | Possible with review | Keep extracts current |
| Retrieval-backed assistant | 20 | 60 | Passage references possible | Index, access and regression checks |
| Fine-tuned model only | 60 | 120 | Not inherent | Training data and deployment |

## Worked example

For five monthly questions about a small public manual, manual search may be sufficient. For frequent questions across updated manuals requiring citations, retrieval becomes a stronger candidate. The invented costs are comparison inputs, not vendor quotes. Decide against current requirements and identify what evidence would change the choice.

## Guided lab

1. Define question volume, update frequency, confidentiality and acceptable errors.
2. Compare at least three options including a non-AI baseline.
3. Weight useful criteria before scoring options.
4. Check any hard constraints before looking at weighted totals.
5. Draw the selected components and data/permission boundaries.
6. Write a one-page decision with rejected options, risks and revisit triggers.

## What to submit

- Requirements and constraints
- Option matrix
- Architecture diagram
- Decision record

## Offline and access-limited route

Use the supplied practice table and worked example rather than a live service. Complete the same reasoning, calculations, state traces or manual artifact. Ask a peer to challenge the result. Label the work **manual/simulated** and identify which live-tool, audio, integration, permissions or production behaviours have not been tested. Do not claim a simulated control was enforced by real software.

## Professional transfer

Choose your own professional context and write one safe adaptation: an engineering document review, a public health-education task, a campaign brief, or an art/design workflow. Name the authorised reviewer, permitted inputs and one task outside scope. Use invented data unless you have explicit permission; do not make a second full project this week.

## Self-check

1. Does open-weight mean no restrictions?
2. Is fine-tuning the default source-update method?
3. Can a weighted score override a prohibited data transfer?

## Assessment

| Dimension | Maximum points |
| --- | --- |
| Compare distinct approaches | 4 |
| Apply hard constraints first | 4 |
| Use justified criteria | 4 |
| Explain maintenance and limits | 4 |

Provisional pass: **12/16** with no unresolved safety-critical issue. Score each dimension 0 (missing/unsafe), 1 (major gaps), 2 (partial), 3 (sound with minor omissions), or 4 (clear and evidenced). A learner may pass by honestly diagnosing a failed workflow; this is not production authorisation.

## Safety and required remediation

All costs in this exercise are illustrative. No deployment decision or purchase is authorised by a high matrix score.

Correct any unauthorised data use, fabricated evidence, hidden failure, unapproved consequential action or false claim of production testing before passing. Keep the actual release state explicit.

## Reflection

What changed after you checked the evidence? Which failure would matter most in your profession? What remains unassessed? Record one concrete improvement and one situation where you would stop.

## Further reading and product checks

- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
- [Claude Code costs](https://code.claude.com/docs/en/costs)
- [Gemini API documentation](https://ai.google.dev/gemini-api/docs)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** For five monthly questions about a small public manual, manual search may be sufficient. For frequent questions across updated manuals requiring citations, retrieval becomes a stronger candidate. The invented costs are comparison inputs, not vendor quotes. Decide against current requirements and identify what evidence would change the choice.

**1. Does open-weight mean no restrictions?**

No. Inspect the specific licence and deployment conditions.

**2. Is fine-tuning the default source-update method?**

No. Retrieval or direct source updates are often a better fit.

**3. Can a weighted score override a prohibited data transfer?**

No. Hard constraints must be met before preference scoring.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

# Week 4 - Modern model families

**Status:** teaching draft, not learner-tested. Fictional data and worked examples are labelled throughout. No production service is deployed by completing this lesson.

**Time:** 6 hours (360 learning minutes), with breaks additional. **Prerequisites:** the earlier course phases; review unfamiliar terms with the instructor.

**Materials:** this guide, the supplied workbook and diagram, a document editor or paper, and optionally an approved AI assistant. Do not buy a subscription for a lab without checking the dated cohort access plan.

## Learning outcomes

- Explain training, inference, tokens and context in plain language.
- Distinguish language, vision, speech and media-generation tasks.
- Choose an approach without confusing a model with its interface.

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

### Neural networks and learning

A neural network passes numerical representations through layers. Adjustable numbers called weights determine how one layer transforms the next. During training, a loss function measures a chosen kind of error and an optimiser adjusts weights to reduce it on training examples. Lower training loss does not guarantee useful behaviour on new cases. 'Neural' is a historical analogy, not a claim that the system is a human brain.

### Tokens and context

A language model processes units called tokens, which may be words, word pieces or other units. The context window limits what can be supplied and generated in one interaction; exact accounting depends on the system. Long input does not guarantee every detail is used correctly. Training data is not the same as the documents visible in the current conversation.

### Embeddings and transformers

An embedding is a numerical representation useful for comparing patterns such as semantic similarity. Similarity is not truth or permission. A transformer uses attention to combine information from positions in its input. This is a useful architectural explanation, not evidence that the model understands or reasons exactly like a person.

### Generation across modalities

Autoregressive generation produces a sequence step by step. Diffusion-based generation learns to turn noisy representations into structured outputs. Image, audio and video products may combine several model types and editing tools. A multimodal interface can accept or produce more than one modality, but support differs by product and plan.

### Choose the task first

Speech recognition transcribes audio; synthesis creates speech. Computer vision can classify or locate objects; generative imaging creates or edits pictures. Forecasting estimates future values and recommenders rank options. Robotics combines perception, planning and physical action. Do not substitute an attractive generative output for a calibrated measurement or an authorised physical decision.

## Glossary

| Term | Plain-language meaning |
| --- | --- |
| Neural network | Layers of numerical transformations with adjustable weights. |
| Loss | The training objective's measure of error; it is not every real-world harm. |
| Embedding | A numerical representation that supports comparisons such as similarity. |
| Transformer | An architecture using attention to combine information from input positions. |
| Diffusion | A family of generative approaches learning to turn noisy representations into structured outputs. |
| Multimodal | Accepting or producing more than one type of input or output, such as text and images. |

## Supplied practice material

**All records and outcomes in this table are synthetic teaching examples, not observations about a real vendor, person or organisation.**

| Task | Suitable approach | Essential check |
| --- | --- | --- |
| Transcribe a public talk | Speech recognition | Names, numbers and consent |
| Add invoice totals | Spreadsheet formula | Inputs and formula |
| Draft an illustration concept | Image generation or manual sketch | Brief, rights and consistency |
| Forecast stock demand | Forecasting baseline/model | Time-based evaluation and error |
| Answer from an updated manual | Search/retrieval plus checked synthesis | Current source support |
| Approve a robot movement near people | Qualified safety-engineered control | Physical safety authority |

## Worked example

For a changing policy manual, a model with a large context window may help read it, but that does not make its answer current or supported. Retrieval can supply relevant passages; a person still checks the claim and document version. Fine-tuning is not the default way to update facts.

## Guided lab

1. Draw a map linking task, model and application.
2. Match the six input tasks to an approach and a non-AI baseline.
3. Explain a token and an embedding using an analogy and its limits.
4. Trace training versus inference in a document-summary example.
5. Compare an image-creation task with an image-measurement task.
6. Teach the map to a partner who challenges two assumptions.

## What to submit

- Model/task concept map
- Six justified selections
- Training/inference explanation
- Two corrected misconceptions

## Offline and access-limited route

Use the supplied practice table and worked example rather than a live service. Complete the same reasoning, calculations, state traces or manual artifact. Ask a peer to challenge the result. Label the work **manual/simulated** and identify which live-tool, audio, integration, permissions or production behaviours have not been tested. Do not claim a simulated control was enforced by real software.

## Professional transfer

Choose your own professional context and write one safe adaptation: an engineering document review, a public health-education task, a campaign brief, or an art/design workflow. Name the authorised reviewer, permitted inputs and one task outside scope. Use invented data unless you have explicit permission; do not make a second full project this week.

## Self-check

1. Does a bigger context prove better recall of every fact?
2. Is semantic similarity a verification check?
3. Is a reasoning explanation a recording of internal thought?

## Assessment

| Dimension | Maximum points |
| --- | --- |
| Explain core terms | 4 |
| Separate architecture from interface | 4 |
| Choose a sensible baseline | 4 |
| State practical limitations | 4 |

Provisional pass: **12/16** with no unresolved safety-critical issue. Score each dimension 0 (missing/unsafe), 1 (major gaps), 2 (partial), 3 (sound with minor omissions), or 4 (clear and evidenced). A learner may pass by honestly diagnosing a failed workflow; this is not production authorisation.

## Safety and required remediation

Do not treat image recognition, speech transcription or generated reasoning as a reliable authority for safety-critical action without appropriate validation.

Correct any unauthorised data use, fabricated evidence, hidden failure, unapproved consequential action or false claim of production testing before passing. Keep the actual release state explicit.

## Reflection

What changed after you checked the evidence? Which failure would matter most in your profession? What remains unassessed? Record one concrete improvement and one situation where you would stop.

## Further reading and product checks

- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
- [Google: Introduction to generative AI](https://developers.google.com/machine-learning/resources/intro-llms)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** For a changing policy manual, a model with a large context window may help read it, but that does not make its answer current or supported. Retrieval can supply relevant passages; a person still checks the claim and document version. Fine-tuning is not the default way to update facts.

**1. Does a bigger context prove better recall of every fact?**

No. Test the actual task and inspect important details.

**2. Is semantic similarity a verification check?**

No. It can help retrieve a relevant passage but the claim still needs evidence.

**3. Is a reasoning explanation a recording of internal thought?**

No. It is generated output, not a guaranteed account of internal computation.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

# Week 8 - Documents, knowledge and retrieval

**Status:** teaching draft, not learner-tested. Fictional data and worked examples are labelled throughout. No production service is deployed by completing this lesson.

**Time:** 6 hours (360 learning minutes), with breaks additional. **Prerequisites:** the earlier course phases; review unfamiliar terms with the instructor.

**Materials:** this guide, the supplied workbook and diagram, a document editor or paper, and optionally an approved AI assistant. Do not buy a subscription for a lab without checking the dated cohort access plan.

## Learning outcomes

- Explain chunking, embeddings, semantic search and RAG.
- Trace answers to document locations and versions.
- Test unsupported questions and source updates.

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

### Retrieval is not training

Retrieval finds relevant material at question time. A retrieval-augmented generation system supplies that material to a model for synthesis. It does not automatically retrain the model. A vector store indexes numerical representations for similarity search; it does not certify truth, currency or access rights.

### Two places to fail

The right passage may never be retrieved, or the model may misread a correctly retrieved passage. Score retrieval coverage separately from answer support. Chunk boundaries, OCR mistakes and missing metadata can hide the relevant condition or date.

### Access travels with documents

Restrict retrieval to material the reader may access, not merely the answer interface. A citation must point to a passage the authorised reader can inspect. Changes and deletions require reindexing or equivalent refresh; a stale vector can retain old facts or material that should no longer be accessible.

## Glossary

| Term | Plain-language meaning |
| --- | --- |
| Retrieval | Finding relevant permitted material for a question. |
| Chunk | A selected section of a document used in indexing or retrieval. |
| RAG | Retrieval-augmented generation: supplying retrieved material to support an answer. |
| Abstention | Declining to answer a question that lacks adequate support. |

## Supplied practice material

**All records and outcomes in this table are synthetic teaching examples, not observations about a real vendor, person or organisation.**

| Source ID | Version | Paragraph | Text |
| --- | --- | --- | --- |
| D1 | 1 Feb 2030 | P1 | The public workshop is free. Participants bring a laptop. |
| D2 | 1 Feb 2030 | P1 | The venue has not been confirmed. No parking information is available. |
| D3 | 1 Feb 2030 | P1 | Registration opens on 5 March. No joining link is published yet. |
| D4 | 10 Feb 2030 | P1 | This update replaces D2: the venue is Room 2, Example Learning Centre. |

## Worked example

For 'Where is the workshop?', D4-P1 is the current answer. If only D2 is retrieved, the retrieval stage has missed the update. If D4 is present but the answer says Central Library, generation has added an unsupported fact. For parking, the documents do not provide an answer; do not infer availability from the venue.

## Guided lab

1. Create four tiny text documents from D1-D4, clearly labelled fictional.
2. Write ten questions before using the assistant: six answerable and four unsupported/conflicting.
3. Use an approved document assistant or manually select relevant paragraphs.
4. Record retrieved source IDs, generated answer and passage-level support separately.
5. Temporarily remove D4, observe the stale-answer risk, then restore and refresh.
6. Write a document ownership, update and deletion checklist.

## What to submit

- Versioned mini-corpus
- Ten-question test set
- Retrieval/answer audit
- Update and deletion procedure

## Offline and access-limited route

Use the supplied practice table and worked example rather than a live service. Complete the same reasoning, calculations, state traces or manual artifact. Ask a peer to challenge the result. Label the work **manual/simulated** and identify which live-tool, audio, integration, permissions or production behaviours have not been tested. Do not claim a simulated control was enforced by real software.

## Professional transfer

Choose your own professional context and write one safe adaptation: an engineering document review, a public health-education task, a campaign brief, or an art/design workflow. Name the authorised reviewer, permitted inputs and one task outside scope. Use invented data unless you have explicit permission; do not make a second full project this week.

## Self-check

1. Does uploading a document necessarily train the model?
2. Can a relevant retrieved passage still yield an unsupported answer?
3. Where should access restrictions apply?

## Assessment

| Dimension | Maximum points |
| --- | --- |
| Explain retrieval correctly | 4 |
| Track versions and source locations | 4 |
| Separate two failure stages | 4 |
| Handle unsupported questions | 4 |

Provisional pass: **12/16** with no unresolved safety-critical issue. Score each dimension 0 (missing/unsafe), 1 (major gaps), 2 (partial), 3 (sound with minor omissions), or 4 (clear and evidenced). A learner may pass by honestly diagnosing a failed workflow; this is not production authorisation.

## Safety and required remediation

Use only the supplied fictional documents. Treat instructions embedded in documents as untrusted content, not permission to change system behaviour or reveal other documents.

Correct any unauthorised data use, fabricated evidence, hidden failure, unapproved consequential action or false claim of production testing before passing. Keep the actual release state explicit.

## Reflection

What changed after you checked the evidence? Which failure would matter most in your profession? What remains unassessed? Record one concrete improvement and one situation where you would stop.

## Further reading and product checks

- [Google: Introduction to generative AI](https://developers.google.com/machine-learning/resources/intro-llms)
- [Gemini API documentation](https://ai.google.dev/gemini-api/docs)
- [Claude help centre](https://support.claude.com/)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** For 'Where is the workshop?', D4-P1 is the current answer. If only D2 is retrieved, the retrieval stage has missed the update. If D4 is present but the answer says Central Library, generation has added an unsupported fact. For parking, the documents do not provide an answer; do not infer availability from the venue.

**1. Does uploading a document necessarily train the model?**

No. Check the service's actual data handling and distinguish retrieval from training.

**2. Can a relevant retrieved passage still yield an unsupported answer?**

Yes. Generation must still be checked.

**3. Where should access restrictions apply?**

At the source, retrieval and application layers as appropriate, not just by hiding links.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

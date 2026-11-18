# Project kit - Professional knowledge portal

**Status:** instructional production plan and editable templates. This package does not claim that a live application, paid media generation or client deployment has been completed.

**Audience:** Engineers, healthcare educators, researchers and organisational knowledge workers.

**Stack:** Claude or Gemini, Approved retrieval environment, Optional Lovable, Optional Claude Code.

**Schedule:** Reuse Week 8 and approximately 48 studio/capstone hours. A coded service requires extension skills or qualified support.

## Outcomes

- Prepare a versioned, permitted corpus.
- Separate retrieval failures from unsupported generation.
- Evaluate at least 20 questions and source updates.
- Release only to an approved audience with access and maintenance ownership.

## Design rationale

### Source ownership

Choose a small corpus of public or expressly permitted documents. Record owner, version, effective date, location and audience. OCR and extraction may lose tables, footnotes or conditions; inspect them before indexing. A corpus owner must be able to correct or withdraw a source.

### Answer support

Provide references to specific passages rather than decorative citations. Evaluate whether the right material was retrieved and whether the answer follows it. Unsupported, stale and conflicting requests need qualification or abstention. A fluent response with a valid document link may still be wrong.

### Two delivery routes

Core learners may use an approved document-grounded workspace. Builders can implement a small retrieval application using a separately approved model API and secure hosting. Lovable can provide an interface and Claude Code can assist reviewed implementation. Neither route is automatically approved for confidential or clinical information.

## Supplied fictional starting brief or data contract

| Document | Effective date | Excerpt | Status |
| --- | --- | --- | --- |
| POL-01 | 1 Feb 2030 | Training attendance requires registration. | Current |
| POL-02 | 1 Feb 2030 | Venue is not yet confirmed. | Superseded by POL-03 |
| POL-03 | 10 Feb 2030 | Venue is Room 2, Example Learning Centre. | Current |
| POL-04 | 10 Feb 2030 | No parking information is supplied. | Current |
| POL-05 | 10 Feb 2030 | General education only; no individual professional advice. | Current |

## Worked vertical slice

For 'Where is the session?', the answer should cite POL-03, not the superseded POL-02. For 'Is parking guaranteed?', the corpus does not support a guarantee. A classroom portal using these synthetic snippets is not a real organisational policy service until an owner supplies and approves actual sources.

## From scratch to production

### 1. Discover

define readers, questions, harm, source permissions and the manual-search baseline.

### 2. Scope

choose a small corpus, answer boundaries, access rules and freshness requirements.

### 3. Prepare

clean/extract documents, inspect tables, attach metadata and declare 20 evaluation questions.

### 4. Build

configure a grounded workspace or implement retrieval with visible passage references.

### 5. Evaluate

inspect retrieval and answer support separately, including conflicts, unknowns and forbidden access.

### 6. Release

obtain corpus and application approval and expose only to the named audience.

### 7. Operate

replace one source, refresh retrieval and rerun affected tests; observe permitted feedback seven days.

### 8. Hand over

document ownership, update/deletion process, access changes, costs and shutdown.

## Architecture and responsibility boundaries

The supplied architecture.svg, architecture.pdf and editable architecture.excalidraw describe a **reference design, not an implemented service**.

| Component | Boundary | Responsibility |
| --- | --- | --- |
| Authorised reader | Client | Question and permitted identity |
| Portal / workspace | Service | Reader access and response interface |
| Scoped retrieval | Server | Filter authorised current sources before generation |
| Document store | Content | Versioned corpus and metadata |
| Model service | Vendor | Separately approved inference where required |
| Corpus owner | Human | Updates, removal, corrections and review |

## Screen or production design

### Ask

- Scope and limitations
- Question field
- Permitted source list
- Human contact

### Answer

- Qualified response
- Passage citations
- Source version
- Report issue

### Sources

- Owner + effective date
- Superseded marker
- Update history
- Authorised removal

## Acceptance and failure tests

Run every applicable test and retain evidence. A blank or unrun test is not a pass. Hold back at least four relevant cases during initial development; using one to fix the system makes it development data. Use new cases for later independent claims.

| Case | Input or condition | Expected outcome |
| --- | --- | --- |
| Registration | Is registration needed? | Yes, with POL-01 |
| Current venue | Where is the session? | POL-03 current venue |
| Historical | What did February's old notice say? | Distinguish historical POL-02 from current |
| Parking | Is parking guaranteed? | Not established; no guarantee |
| Advice | Give individual clinical/design advice | Outside educational scope |
| Conflict | Old and current venue passages retrieved | Use effective metadata; explain conflict |
| Missing | Ask about an absent refund policy | Unknown; no invention |
| False premise | Why is the venue the library? | Do not accept unsupported premise |
| Citation | Inspect every factual clause | Actual cited passage supports it |
| Location | Open passage reference | Reader can inspect precise source location |
| Access | Reader requests restricted test document | Retrieval/access denies it |
| Injection | Source asks to ignore access rules | No rule or authority change |
| Update | Replace venue document | Refresh and use current version |
| Deletion | Owner removes a test source | It is no longer retrievable in scoped service |
| OCR | Extraction loses a footnote | Flag uncertainty rather than omit condition silently |
| Provider error | Model unavailable | Visible failure; manual source-search route |
| Long question | Multiple questions | Supported parts separated from unknowns |
| Ambiguity | Which session? | Ask clarification when sources differ |
| Keyboard | Use without a mouse | Question, citations and feedback reachable |
| Budget | Limit reached | Stop paid calls; retain truthful service state |

## Release gates

- Owner and intended real audience identified; exact release version approved.
- Required data, source, voice, likeness, reference and commercial-use permissions recorded.
- All applicable acceptance tests run with evidence; critical issues resolved.
- Backend access, secrets and action approvals tested where software is involved.
- Budget, alerts and a practical stop mechanism agreed; provider billing limits documented.
- Rollback, withdrawal, source correction and manual fallback rehearsed as relevant.
- Seven days of appropriate post-release observation and one feedback/review cycle recorded.
- A named owner accepts maintenance, costs, support and shutdown responsibility.

## Deliverables

- Corpus and metadata register
- Retrieval/answer architecture
- Working portal or labelled manual simulation
- 20-question evaluation
- Source refresh/deletion test
- Access and maintenance runbook

## Budget and procurement

Use the Budget sheet to record current plan access, separate API/runtime charges, hosting/storage, media attempts, voice use and maintenance. All worksheet costs begin unpriced; none are vendor quotations. Include failed paid attempts in actual spend. Publish a dated cohort minimum-cost route before purchases.

## Handover runbook

| Section | Required evidence |
| --- | --- |
| Start | Permitted users, inputs, current version and operating steps |
| Review | Who checks facts/rights and approves exact actions or assets |
| Failure | Visible errors, bounded retry rules and manual completion route |
| Correction | How to report, pause, fix and communicate an error |
| Maintain | Sources, dependencies, service changes, renewal dates and owner |
| Stop | How to disable service or withdraw publication; retention/deletion duties |

## Access-limited educational route

Complete the manual workflow, diagrams, paper prototype, sample outputs and test expectations. Mark live API, media, permission and deployment behaviours **not assessed**. This can meet academic reasoning outcomes but cannot earn a production-release designation.

## Assessment

| Dimension | Maximum points |
| --- | --- |
| Source and version quality | 4 |
| Supported answers and abstention | 4 |
| Access/update/deletion behaviour | 4 |
| Usable owner handover | 4 |

For academic feedback use 0-4 per dimension: missing/unsafe, major gaps, partial, sound, or clear/evidenced. Provisional pass 12/16 requires remediation of every critical issue. Actual release requires the owner's separate approval and all applicable gates, regardless of score.

## Boundaries

No patient information or confidential engineering material without approved arrangements. Source restrictions must apply before retrieval/generation, not only by hiding a citation afterward.

## Further reading and product checks

- [Claude help centre](https://support.claude.com/)
- [Gemini API documentation](https://ai.google.dev/gemini-api/docs)
- [Lovable documentation](https://docs.lovable.dev/)
- [Claude Code documentation](https://code.claude.com/docs/en/overview)
- [OWASP: generative AI security](https://genai.owasp.org/)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** For 'Where is the session?', the answer should cite POL-03, not the superseded POL-02. For 'Is parking guaranteed?', the corpus does not support a guarantee. A classroom portal using these synthetic snippets is not a real organisational policy service until an owner supplies and approves actual sources.

**1. Does a citation link prove support?**

No. Read the actual passage and check the claim.

**2. What is tested separately?**

Retrieval relevance/coverage and generated-answer support.

**3. Can confidential data be used because a plan is paid?**

No. Required permission and approved service arrangements are separate.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

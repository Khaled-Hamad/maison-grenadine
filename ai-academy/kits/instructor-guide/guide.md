# Instructor and pilot guide - full 24-week edition

**Status:** teaching draft. This guide expands the earlier three-lesson pilot to all 24 weeks. Instructor delivery and real-learner validation remain pending.

## How to use the kits

Each weekly kit contains an editable slide deck with speaker notes, a Word learner guide, reader PDF, slide handout PDF, Excel workbook, practice CSV, editable process diagram and a timed roadmap. Project kits add reference architectures, wireframes, failure tests and release/handover plans. All paid-service and deployment outcomes must be observed in the actual environment; the provided files do not claim those services have been operated.

## Standard session rhythm

| Block | Minutes | Action |
| --- | --- | --- |
| Concepts | 60 | Read explanations, discuss a misconception and interpret the worked example. |
| Demonstration | 60 | Predict the result, inspect the supplied inputs, and compare with the worked answer. |
| Guided lab | 120 | Complete the ordered lab steps and retain intermediate evidence. |
| Independent work | 90 | Complete the deliverables, professional transfer and self-check. |
| Reflection and feedback | 30 | Review the evidence, remediate blockers and record one next step. |

## Shared scoring anchors

| Points | Meaning |
| --- | --- |
| 0 | Missing, unsupported or unsafe |
| 1 | Major gaps |
| 2 | Partial understanding |
| 3 | Sound with minor omissions |
| 4 | Clear and evidenced |

## Programme grades versus lesson feedback

Ordinary lesson rubrics use /16 for formative feedback with a provisional 12/16 pass. Programme grading uses four category scores: Weeks 1-8 at 20%, Weeks 9-16 at 25%, studio at 20%, capstone at 35%. Overall must be at least 70%, capstone at least 70%, and all critical safety conditions clear. The blueprint's six-dimension capstone rubric supplies the capstone category score. Do not apply a generic /16 project score as regulatory approval.

## Workbook conventions

Input cells are lightly highlighted. Scores start empty, tests start unrun and gates start Pending. Formula cells must not be overwritten. Mark 'N/A (justified)' only with a written reason and reviewer agreement. An empty evidence field cannot establish a test pass. Budget values are unpriced until the owner enters dated quotes or measurements.

## Preparation and privacy

Dry-run sources and accounts, check product terms, permit manual alternatives, provide accessible documents and avoid collecting personal professional records. Name a local policy owner and obtain the necessary approvals. A consumer subscription or an attractive demo is not institutional authorisation.

## Per-week delivery and answer guidance

### Week 1 - AI literacy and responsible first use

**Expected result:** The draft preserves the price but invents a venue and qualification and reverses the laptop instruction. Correct those details, keep the venue unconfirmed and ask the organiser before publication.

**Self-check key:**

- Does fluent wording establish truth? **No. Verify consequential claims against evidence.**
- Does removing a patient's name authorise an upload? **No. Indirect identifiers, permission and the approved environment still matter.**
- When is an ordinary spreadsheet preferable? **For a defined calculation with known inputs and checkable formulas.**

**Look for:** Explain the four layers; Correct unsupported details; Identify privacy and authority boundaries; Justify a safe professional use.

**Required boundary:** Never upload real patient records, confidential designs, credentials or private client materials without the required authorisation and approved environment.

### Week 2 - How machine learning learns

**Expected result:** The rule 'free means promotional; otherwise work' scores 4/4 on training, 0/2 on development and 2/4 on the held-out examples. It has not learnt reliable intent. The words are features, not proof of meaning. A rule using only the two supplied features cannot separate H1 and H3, which share features but have different labels.

**Self-check key:**

- Why not keep tuning on the held-out rows? **They would cease to be an independent test; obtain new examples for a fresh claim.**
- Can two identical feature patterns have different labels? **Yes; the features may omit relevant information or labels may be noisy.**
- Is our paper rule a trained transformer? **No. It illustrates fitting and generalisation with a much simpler rule.**

**Look for:** Match task and learning setup; Keep split boundaries; Calculate errors correctly; Explain an evidenced limitation.

**Required boundary:** Use synthetic messages. Do not copy real inbox contents, employee judgements or private communications into a demonstration.

### Week 3 - Data, uncertainty and prediction errors

**Expected result:** Among 100 documents, precision is 8/26 = 30.77%, recall is 8/10 = 80%, and accuracy is 80/100 = 80%. An always-negative baseline is 90% accurate but has zero recall. Neither number alone establishes the right workflow. With illustrative costs of 5 units per false alarm and 100 per miss, the candidate costs 290 units versus 1,000 for the baseline.

**Self-check key:**

- Can 99% accuracy be useless? **Yes, if rare consequential cases are all missed.**
- What is precision when nothing is flagged? **Undefined for that sample because the denominator is zero.**
- Does higher recall automatically justify deployment? **No. False alarms, harms, evidence and professional approval also matter.**

**Look for:** Define outcomes correctly; Calculate with correct denominators; Compare a baseline; Justify the error trade-off.

**Required boundary:** Do not interpret the invented review example as a clinical diagnostic test or use the illustrative costs to decide real safety policy.

### Week 4 - Modern model families

**Expected result:** For a changing policy manual, a model with a large context window may help read it, but that does not make its answer current or supported. Retrieval can supply relevant passages; a person still checks the claim and document version. Fine-tuning is not the default way to update facts.

**Self-check key:**

- Does a bigger context prove better recall of every fact? **No. Test the actual task and inspect important details.**
- Is semantic similarity a verification check? **No. It can help retrieve a relevant passage but the claim still needs evidence.**
- Is a reasoning explanation a recording of internal thought? **No. It is generated output, not a guaranteed account of internal computation.**

**Look for:** Explain core terms; Separate architecture from interface; Choose a sensible baseline; State practical limitations.

**Required boundary:** Do not treat image recognition, speech transcription or generated reasoning as a reliable authority for safety-critical action without appropriate validation.

### Week 5 - Task framing and prompting

**Expected result:** A revised event prompt may preserve the price but still invent the venue. That case fails C4 and C5 even if its overall wording is attractive. Accept only final cases scoring at least 7/8 with no C2-C5 failure; honest diagnosis of a failed workflow can still demonstrate learning.

**Self-check key:**

- What does three versions mean? **V1 plus two revisions, not three additional revisions.**
- Can an offline example prove your prompt improved a model? **No. It demonstrates design and auditing; live execution remains untested.**
- What if V3 fails on C? **Keep V3, record the failure and propose a separately labelled V4.**

**Look for:** Define observable acceptance; Connect revisions to evidence; Keep cross-case records; Limit reliability claims.

**Required boundary:** A useful prompt is not a permission boundary or guarantee of factuality. Do not hide failed runs to make a prompt look reliable.

### Week 6 - Verification and model comparison

**Expected result:** Suppose A passes 6 of 8 checks and B passes 7 of 8. If B's single failure invents a registration link while A's misses only length and tone, B is not automatically preferable. Report critical failures separately from a total. A new task family could reverse the result.

**Self-check key:**

- Does 7/8 prove a model is the market leader? **No. It is a small task-specific observation.**
- Can an appropriate refusal earn a pass? **Yes, when the case requires abstention or escalation.**
- What must change if tools differ? **Describe it as a product/workflow comparison and record those differences.**

**Look for:** Define representative cases; Apply rubric consistently; Report critical failures and repeats; Avoid unsupported rankings.

**Required boundary:** Use fictional inputs only. Never test a provider with actual secrets, patient data or harmful external actions.

### Week 7 - Research and source-grounded answers

**Expected result:** The observed median difference is (20-12)/20 = 40%. The tasks differed and were not randomised, so this is not proof that the tool caused a 40% improvement. The controlled source pack is invented and cannot establish facts about real vendors.

**Self-check key:**

- Is a source you cannot open necessarily fabricated? **No. Its support is not established until appropriate evidence is available.**
- Can a testimonial establish a universal effect? **No. It establishes that someone made a report, not a general causal effect.**
- What does the fictional pack prove? **Only whether the classroom conclusion follows from supplied fictional evidence.**

**Look for:** Handle sources and versions; Audit scope and causality; Trace consequential claims; Disclose retrieval limits.

**Required boundary:** Never invent citations, treat an unavailable source as checked, or use an educational source pack as clinical certification.

### Week 8 - Documents, knowledge and retrieval

**Expected result:** For 'Where is the workshop?', D4-P1 is the current answer. If only D2 is retrieved, the retrieval stage has missed the update. If D4 is present but the answer says Central Library, generation has added an unsupported fact. For parking, the documents do not provide an answer; do not infer availability from the venue.

**Self-check key:**

- Does uploading a document necessarily train the model? **No. Check the service's actual data handling and distinguish retrieval from training.**
- Can a relevant retrieved passage still yield an unsupported answer? **Yes. Generation must still be checked.**
- Where should access restrictions apply? **At the source, retrieval and application layers as appropriate, not just by hiding links.**

**Look for:** Explain retrieval correctly; Track versions and source locations; Separate two failure stages; Handle unsupported questions.

**Required boundary:** Use only the supplied fictional documents. Treat instructions embedded in documents as untrusted content, not permission to change system behaviour or reveal other documents.

### Week 9 - Spreadsheets, data quality and cleaning

**Expected result:** Rules: remove exact duplicate rows, parse 'USD 35' as 35 USD, report refunds separately, exclude cancelled orders from completed revenue, and do not impute A03's quantity. Ten raw rows become nine unique orders. Six fully specified completed orders total 265 USD; one completed order is unresolved. The refund is -40 USD separately. Do not call 265 the total value of all completed orders because one is unknown.

**Self-check key:**

- Should a missing quantity become zero? **No, not without a justified rule and explicit disclosure.**
- Is every negative value an error? **No. The refund rule can make a negative quantity legitimate.**
- Can you call 265 USD complete revenue? **No. It is the known revenue of six complete records; A03 remains unresolved.**

**Look for:** Preserve types and units; Apply documented rules; Reconcile rows and amounts; Report missing-data limits.

**Required boundary:** Do not upload real customer orders or identifiers. Synthetic examples are sufficient to learn cleaning and reconciliation.

### Week 10 - Analysis, visualisation and decisions

**Expected result:** Totals: 4,000 visits, 270 sign-ups and 400 USD recorded spend. Overall conversion is 6.75%, not the unweighted average of channel rates. Email's observed conversion is 15% and cost per sign-up is about 0.33 USD. Search and Social both show 2.50 USD per sign-up, despite different rates. None of this proves incremental lift or lifetime value.

**Self-check key:**

- Why not average the four conversion percentages? **The denominators differ; use total sign-ups divided by total visits.**
- Does low recorded spend per sign-up prove best business value? **No. Full costs, attribution and downstream value are missing.**
- What would stronger causal evidence require? **An appropriate experiment or defensible causal design, not just this observational table.**

**Look for:** Use correct denominators; Verify calculations; Label charts accessibly; Bound the recommendation.

**Required boundary:** Do not use these invented results as financial advice or a promise of campaign returns.

### Week 11 - Images and visual design

**Expected result:** For the fictional workshop, choose a geometric learning motif rather than a realistic photograph implying a confirmed venue. Keep the event details in editable text, preserve known facts and label unknown logistics. Reject B's badge even if the image is attractive. Candidate A still needs human design and rights checks.

**Self-check key:**

- Does generation permission settle every rights issue? **No. Check applicable terms, references, consent and third-party rights.**
- Can a venue photograph be an unsupported claim? **Yes, if it implies a real location that is not established.**
- Why keep text editable? **To verify facts, correct typography and adapt accessible versions.**

**Look for:** Write concrete design constraints; Compare genuine alternatives; Check factual and rights issues; Prepare accessible production assets.

**Required boundary:** Do not use unconsented real-person likenesses, unauthorised brand assets or a fabricated certification mark. A supplied concept description is not an actual vendor-generated image.

### Week 12 - Audio, video and multimodal production

**Expected result:** The caption changes in segment 2 and 3 reverse important facts; they are not harmless spelling mistakes. Correct the text and check timing against real audio when available. With only the supplied timecards, you can assess script consistency and a caption plan, but cannot claim to have evaluated pronunciation, listening quality or actual synchronisation.

**Self-check key:**

- Is text-to-speech the same as transcribing? **No. They convert in opposite directions and have different checks.**
- Can supplied timecards establish audio quality? **No. They support text/timing-plan checks only.**
- Does a paid plan remove the need for voice consent? **No. Permissions and applicable service rules still matter.**

**Look for:** Plan coherent timing; Correct caption meaning; Track rights and consent; Distinguish real media from simulation.

**Required boundary:** Do not clone an identifiable person's voice without proper consent and verification. Do not label an educational plan as a produced or commercially cleared video.

### Week 13 - APIs, connectors and automation

**Expected result:** A valid draft response is not permission to send it. Validate the response schema and source facts, show the exact recipient/content to an authorised reviewer, and perform no external write if approval is absent. An assistant saying 'approved' cannot manufacture the review event.

**Self-check key:**

- Does valid JSON mean correct content? **No. Validate schema and meaning against the task.**
- Is MCP a permission boundary? **No. Enforce access using the actual application and service controls.**
- Does Claude Pro automatically fund an application's runtime? **No. Check development access and runtime API billing separately.**

**Look for:** Explain request/response; Define field validation; Handle visible failures; Place enforceable permissions.

**Required boundary:** This lab does not connect to real inboxes, purchase services, deploy code or send messages. Use dummy credentials labelled NOT-A-REAL-KEY if a field is needed.

### Week 14 - Workflows versus agents

**Expected result:** For routine incoming requests, a fixed validated draft-to-review workflow is often simpler than a general agent. If the network times out after a send, the absence of a success response is not proof that nothing happened. Reconcile the provider's recorded action state or escalate rather than sending blindly again.

**Self-check key:**

- Does a timeout prove the action failed? **No. Check the action's actual state.**
- Can text in a source document authorise sending? **No. Treat it as untrusted content.**
- What changes if the approved recipient changes? **The old approval no longer covers the proposed action; obtain a new one.**

**Look for:** Choose appropriate autonomy; Track state and duplicate effects; Enforce approval semantics; Handle failures visibly.

**Required boundary:** Use simulation or a sandbox. Never test retry logic by sending real messages, charging cards or changing production records.

### Week 15 - Choosing and adapting AI systems

**Expected result:** For five monthly questions about a small public manual, manual search may be sufficient. For frequent questions across updated manuals requiring citations, retrieval becomes a stronger candidate. The invented costs are comparison inputs, not vendor quotes. Decide against current requirements and identify what evidence would change the choice.

**Self-check key:**

- Does open-weight mean no restrictions? **No. Inspect the specific licence and deployment conditions.**
- Is fine-tuning the default source-update method? **No. Retrieval or direct source updates are often a better fit.**
- Can a weighted score override a prohibited data transfer? **No. Hard constraints must be met before preference scoring.**

**Look for:** Compare distinct approaches; Apply hard constraints first; Use justified criteria; Explain maintenance and limits.

**Required boundary:** All costs in this exercise are illustrative. No deployment decision or purchase is authorised by a high matrix score.

### Week 16 - Evaluation, security and governance

**Expected result:** A system passing 11/12 tests must still be held if its failure exposes another user's data. Quality aggregates do not cancel a mandatory gate. Mark each test unrun, pass or fail with evidence; an empty test cell is not a pass. A dozen cases are useful design evidence, not proof of production safety.

**Self-check key:**

- Can an average score compensate for an access leak? **No. The mandatory gate remains blocked.**
- Are simulated controls production-tested controls? **No. Label simulation and obtain real implementation evidence before release.**
- What changes after a held-out test drives a fix? **That case becomes development data; obtain new cases for an independent claim.**

**Look for:** Construct relevant cases; Record evidence honestly; Use non-negotiable gates; Assign practical ownership.

**Required boundary:** Do not attack a live service or use actual secrets. Use permitted staging accounts and dummy records; an instructor cannot grant professional or legal authority they do not hold.

### Week 17 - Define the professional problem

**Expected result:** A suitable fictional brief is: help one organiser produce source-backed workshop invitations, with no autonomous sending, no personal data and a human approving every factual detail. Measure time and errors against a manual baseline. Do not promise a 50% reduction before collecting evidence.

**Self-check key:**

- Is a tool name a problem statement? **No. State the task and user need first.**
- Must each learner complete six projects? **No. Choose one main project; others are demonstrations or electives.**
- Does an estimated time saving establish value? **No. Measure against a sensible baseline.**

**Look for:** Identify a real task; Bound the project; Define measurable evidence; Identify authority and resources.

**Required boundary:** Use a role-play if consent or domain access is unavailable. Label invented stakeholder evidence rather than presenting it as a real interview.

### Week 18 - Build the first professional workflow

**Expected result:** The first invitation workflow can be four documents and a checklist rather than a coded platform. If a reviewer changes the date after layout, the approval must refer to the revised version. A screenshot of an attractive page is not evidence that permissions, persistence or failure handling work.

**Self-check key:**

- Does manual orchestration make the prototype invalid? **No. Label it accurately and evaluate its usefulness.**
- Can a screenshot prove access control? **No. Test the actual implemented boundary.**
- What happens when an approved artifact changes? **Assess the change and obtain approval for the changed version where required.**

**Look for:** Complete one journey; Preserve reproducible records; Place meaningful review; Identify missing behaviour.

**Required boundary:** Use test data and restricted access. Do not deploy an unfinished application or publish media simply to make the demonstration look complete.

### Week 19 - Challenge and improve the workflow

**Expected result:** Fixing an invented venue requires both a better drafting rule and a factual check. If a cancelled send still executes, changing prompt wording is not an adequate fix: the workflow's permission/state logic must be corrected and retested.

**Self-check key:**

- Can cosmetic improvement offset a permission failure? **No. Fix or block the consequential failure.**
- Are tuned-on cases still independent evaluation? **No. They are development evidence.**
- Must the fix be in the prompt? **No. Choose the layer actually responsible.**

**Look for:** Cover relevant edges; Keep before/after evidence; Fix the correct layer; Report regressions honestly.

**Required boundary:** No adversarial tests against unauthorised live systems. Test only your own approved staging setup or a clearly labelled simulation.

### Week 20 - Professional handover

**Expected result:** During a peer walkthrough, the reviewer discovers the registration field is absent. The runbook should direct them to stop and ask the owner, not invent a link. Record the issue and amend the procedure; do not quietly coach the peer and call the handover independent.

**Self-check key:**

- Should passwords appear in a handover document? **No. Use approved credential-transfer processes.**
- Does a pilot handover prove production readiness? **No. State the actual controls and approval status.**
- What should you do when a peer needs coaching? **Record the dependency and improve the documentation before another attempt.**

**Look for:** Write usable instructions; Define stop/recovery paths; Demonstrate peer operation; State ownership and release status.

**Required boundary:** Do not share private account credentials with classmates. Keep ownership transfer separate from public documentation.

### Week 21 - Capstone scope and evaluation plan

**Expected result:** A 12-case plan can keep two unsupported and two recovery cases sealed while developing on the other eight. If the chosen project requires 20 cases, expand the matrix rather than replacing its requirement with the course minimum. A denied approval case passes when no send occurs.

**Self-check key:**

- Can you reuse studio work? **Yes, with disclosure and a justified independent extension.**
- Which requirement wins: 12 generic cases or a 20-case project minimum? **The larger applicable project requirement.**
- Can an unsupported request pass by being declined? **Yes, if that is the declared correct behaviour.**

**Look for:** Bound an independent contribution; Declare useful criteria; Separate evaluation data; Identify real release gates.

**Required boundary:** Do not prefill a production approval as granted. Hold the release until the actual owner and required professional reviewers decide.

### Week 22 - Build and document the capstone

**Expected result:** A candidate campaign can consist of an approved script, editable visuals, licensed narration, captions and a publication checklist. A candidate application also needs tested backend permissions and secret handling. They share an evidence discipline but not identical technical release checks.

**Self-check key:**

- Can you use held-out cases for routine debugging? **No. Use development cases and preserve the evaluation boundary.**
- Does a media project need a database rollback? **Not necessarily; it needs the recovery controls relevant to publication and assets.**
- Should estimated spend be presented as measured? **No. Label the estimate and its assumptions.**

**Look for:** Deliver the agreed journey; Preserve reproducibility; Record costs honestly; Rehearse relevant recovery.

**Required boundary:** A candidate is not an authorisation to publish. Keep unfinished software restricted and material rights unapproved until checked.

### Week 23 - Evaluate, revise and report

**Expected result:** A 10/12 total with an invented consequential venue and a success-shaped provider failure is not ready for release. Keep the initial 10/12 result. After fixing those paths, report retest evidence separately and obtain new cases before making a new independent-quality claim.

**Self-check key:**

- May failed cases be dropped because they look unusual? **No. Explain representativeness and keep the original declared result.**
- Can a held-out case remain held out after it drives a fix? **No. It becomes development evidence.**
- Is 'do not release' always a course failure? **No. Evidence-led refusal to release can demonstrate good judgement.**

**Look for:** Keep complete evidence; Compare equivalent tasks; Separate retest claims; Respect mandatory blockers.

**Required boundary:** Do not mark unrun tests as passed or hide safety blockers inside an average score.

### Week 24 - Demonstrate, defend and hand over

**Expected result:** A strong defence can conclude: 'The prototype works on our 12 declared cases, with two initial failures documented and revised. It is not authorised for external use. The owner will decide after the remaining review.' That is more credible than claiming a production-ready platform without approvals or real use.

**Self-check key:**

- Does a high course mark authorise clinical deployment? **No. Professional, institutional and legal approvals are separate.**
- What if seven observation days exceed the course calendar? **Finish the production designation later; do not shorten or invent observation evidence.**
- Who maintains the project after graduation? **A named owner who has accepted responsibility, not automatically the instructor or model provider.**

**Look for:** Demonstrate actual behaviour; Defend evidence and limits; Complete usable handover; State release authority accurately.

**Required boundary:** No automatic certificates of professional authority. Publish only consented work and appropriately licensed assets with actual owner approval.

## Detailed pilot materials for the original samples

# Sample lessons - instructor and pilot guide

**Status:** draft for instructor preparation and small-cohort piloting. Not learner-tested, accredited, or approval for production use.
**Scope:** complete sample packs for Weeks 1, 5, and 7 only; the remaining course is still a blueprint.

## 1. Pack index and intended use

| Pack | Focus | Main submission |
|---|---|---|
| [Week 1](ai-week-01-foundations.md) | AI foundations and responsible first use | Manual/assisted comparison, audit, revision, risk log |
| [Week 5](ai-week-05-prompting.md) | Task framing, prompt iteration, and cross-case testing | Three prompt versions, output audit, unfamiliar case |
| [Week 7](ai-week-07-verification.md) | Evidence, citations, policy versions, and uncertainty | Claim audit, decision brief, retrieval/access log |
| [Curriculum blueprint](ai-curriculum-blueprint.md) | Course structure and production project catalogue | Planning reference, not another assignment |

These are six-hour weekly packs, not six continuous hours of lecture. Each follows 60 minutes concepts, 60 minutes demonstration, 120 minutes lab, 90 minutes independent work, and 30 minutes feedback. Add breaks or spread work across days.

Students taking these as isolated samples use the bridge sections. Do not imply that the missing weeks have already been written or taught.

The packs intentionally use small fictional cases before real production work. Week 1 builds the human review habit; Week 5 makes the task repeatable; Week 7 makes the evidence defensible. All connect to the later Higgsfield, Lovable, ElevenLabs, Claude Code, and automation projects without requiring those subscriptions now.

## 2. Preparation checklist

- Read each pack and run its activities yourself; estimate actual setup and completion time.
- Check official links and applicable account/age/organizational requirements before teaching.
- Offer printed or downloadable text, not screenshots as the sole source.
- Prepare an approved assistant demonstration if learners have no account. Do not require public sharing of their conversation histories or real professional records.
- Supply ordinary document tools with word count, readable headings, and screen-reader access. Allow oral explanations, keyboard-only work, and extra time where needed.
- Explain the difference between fictional case evidence, instructor-authored sample outputs, and actual tool observations.
- Distribute Week 5 Card C only after learners save V3. It is not a secure test bank; do not claim independent testing if learners already studied it.
- For Week 7, open the real-source starting pages shortly before the session and prepare dated excerpts if permitted and necessary. Record origin, access date, relevant section, and any redactions. Do not reconstruct inaccessible sources.
- Agree where submissions are stored, who can see them, and when they are deleted. Collect no raw personal usage logs by default.
- Keep instructor answer guidance separate from the learner handouts until submission or feedback.

## 3. Week 1 facilitation and answer guidance

### Diagnostic and teaching prompts

Ask "What would make this answer safe enough to use?" rather than "Can AI do this?"

Use the invoice example to show that selecting a non-AI method is a competent AI decision. Do not claim every product recommendation or chat interface uses the same architecture.

During the demonstration, retain the first output even if good. A good output is an opportunity to ask which facts were actually checked; it does not justify introducing errors and calling them observed model behavior.

### Task-sort answer guidance

| Situation | Acceptable justification |
|---|---|
| Invoice totals | A spreadsheet/calculator is usually sufficient; check inputs and formulas |
| Headline drafts | AI assistance can help; compare with approved facts and intended audience |
| Patient treatment in personal chatbot | Do not upload or delegate; clinical judgment and an approved environment are required |
| Public specifications | AI can assist comparison; verify source versions, units, and omissions |
| Structural approval | Qualified, authorized professional authority; drafting help is not design approval |
| Translation | AI-assisted draft can help; appropriate language review is needed, especially for consequential instructions |

### Errors in the supplied flawed invitation

- "Central Library" invents a venue.
- "Laptops provided" reverses the bring-a-laptop requirement.
- The registration address is invented.
- A certified qualification is not supported.
- Accessibility is asserted although unconfirmed.
- It omits clear venue/registration uncertainty and the laptop requirement.

Do not mark the address as a working service or ask learners to test it.

### Example reviewed invitation

> Curious about using AI at work? Example Community Learning Group invites adults with no previous AI experience to Practical AI for Everyday Work on 12 March 2030, from 18:00 to 19:30. This free session has space for 20 participants. Please bring a laptop. The venue and accessibility arrangements are not yet confirmed. Contact the organizer about registration; a contact address has not been supplied. Please confirm the missing details, including the time zone, with the organizer before making plans.

This is one valid answer, not prescribed wording. All details remain fictional.

### Exit-question expectations

1. A sum follows an explicit calculation; generated explanation uses a model and may need factual checking.
2. The example must distinguish a trained model from the interface, access plan, and software integration; brand/model version recall is not required.
3. Remove or qualify the accessibility statement and ask the organizer; do not assume accessibility is unavailable.
4. No: indirect identifiers and authorization requirements remain.
5. Accept a justified human-led task and a bounded safe assistance step; do not require "never use AI anywhere in this profession."

Award 0-4 per dimension: 0 missing/unsafe, 1 major gaps, 2 partial understanding, 3 sound with minor omissions, 4 clear and well evidenced. Required safety remediation overrides the numerical pass.

## 4. Week 5 instructor materials

### Unfamiliar input: Card C

Supply only after V3 is saved:

```text
Title: Understanding Public Health Information
Audience: adults attending a general education session
Date: not confirmed
Time: not confirmed
Cost: free
Capacity: 16 participants
Bring: no equipment required
Venue: Room 2, Example Learning Centre
Registration: ask the centre's reception team; no online link supplied
Accessibility arrangements: not confirmed
Additional limit: general education only; no individual medical advice
```

A successful response does not reuse A's date or B's time, price, materials, link promise, or engineering context. It clearly marks the date/time uncertainty and preserves the no-individual-advice limit.

**Scoring clarification:** C5 includes preserving a supplied material limitation, such as no certification in B and no individual advice in C. C7 should identify missing time-zone information where time is supplied without one, unavailable contact details where a registration route lacks them, and other explicitly unconfirmed logistics. Do not require learners to invent unrelated organizer tasks.

### Offline output set

The six outputs below are **instructor-authored examples**, not model transcripts or evidence that a specific prompt produced them. Distribute stages in sequence. Learners can predict improvements, but cannot claim their revisions caused these examples.

#### Stage 1, Card A

> Join Practical AI for Everyday Work on 12 March 2030 at 18:00 in Central Library. The session is free, and laptops are provided. Register online today.

Likely failures: invented venue and registration, reversed laptop instruction, missing end time/capacity, no uncertainty list, too short. Score the actual checks rather than assigning a fixed total blindly.

#### Stage 1, Card B

> Join Reading Public Equipment Manuals, a free certified workshop for all engineers on 18 April 2030 at 10:00. Bring a laptop and register using the public link.

Likely failures: wrong price, invented certification/link, wrong materials, missing time zone/end time/capacity and explicit educational limit, too short.

#### Stage 2, Card A

> Example Community Learning Group welcomes adults with no previous AI experience to Practical AI for Everyday Work on 12 March 2030, from 18:00 to 19:30. This free session has space for 20 participants. Bring a laptop and join us at Central Library for an introduction to everyday AI. Contact the organizer to register and ask about accessibility arrangements before attending.
>
> Organizer checks: confirm contact address, time zone, and accessibility arrangements.

Improvements: core audience/date/time/cost/capacity/materials. Remaining material failure: venue is still invented and not flagged for confirmation. A neat organizer list does not cancel the unsupported claim.

#### Stage 2, Card B

> Early-career engineers are invited to Reading Public Equipment Manuals on 18 April 2030, from 10:00 to 11:00 UTC. The online session costs 15 USD and has room for 12 participants. Please bring the supplied public manual and register through your employer's internal learning portal. A joining link will follow registration, and captions are provided. This certified session will help you approve equipment safely.
>
> Organizer checks: none identified.

Remaining material failure: certification and safety-approval language contradicts the supplied limit. Other accurate details do not compensate.

#### Stage 3, Card A

> Curious about AI? Example Community Learning Group welcomes adults with no previous AI experience to Practical AI for Everyday Work on 12 March 2030, from 18:00 to 19:30. The session is free and has room for 20 participants. Please bring a laptop. The venue and accessibility arrangements are not yet confirmed. Contact the organizer about registration; no contact address has been supplied. Confirm the missing details before making plans.
>
> Organizer checks: confirm venue, accessibility arrangements, contact address, and time zone.

#### Stage 3, Card B

> Early-career engineers are invited to Reading Public Equipment Manuals on 18 April 2030, from 10:00 to 11:00 UTC. This online session costs 15 USD and has space for 12 participants. Bring a copy of the supplied public manual. Register through your employer's internal learning portal; the joining link will be sent after registration. Captions are provided. The session is an educational discussion, not certification or safety approval.
>
> Organizer checks: none identified from the supplied record.

For the offline repeat, rescore the same Stage 3 B output and explicitly record that it is reused, not a second model execution. For C, learners produce and audit a manual candidate using frozen V3. Both limitations belong in their reflection.

### Feedback and marking

Use the learner pack's /16 rubric with the 0-4 anchors from Section 3. Reward a defensible diagnosis of failure, not a flawless-looking selected output.

Check that all six A/B outputs and the unfamiliar/repeat steps are accounted for. A saved failure with a good diagnosis is stronger evidence of learning than an undocumented "perfect" answer.

Ask learners to point to one exact phrase their revised prompt is intended to change. If they cannot, their revision may be decorative rather than evidence-led.

## 5. Week 7 answer guidance

### Expected claim audit

| Claim in flawed draft | Verdict and reasoning |
|---|---|
| Free plan has 100 monthly requests for proposed pilot | Contradicted by S2-P1's effective 30-request plan |
| Free plan permits commercial publishing for proposed use date | Contradicted by S2-P1; distinguish historical S1 from current fictional terms |
| A controlled study was conducted | Contradicted by S3-P1's non-randomized, different-task observation |
| Median time difference is 40% of the manual median | Supported as a calculation from 20 and 12; 8 divided by 20 is 0.4 |
| The tool causes 40% savings for everyone | Not established; task differences, order, and eight volunteers limit inference |
| Productivity doubles | S4-P1 supports that a customer said it, not that the general effectiveness claim is established |
| Invitations are error-free | Contradicted by the two invented-venue outputs in S3-P1 |
| Clinical certification exists | Not established; S5 unavailable, and S1 does not describe clinical approval |
| Studio includes API access | Contradicted by S2-P1 |
| Public launch and use of attendee records are appropriate now | Recommendation conflicts with S6-P1 and S2-P1; revise scope, not merely wording |

Accept an argued "not established" for "controlled study" if the learner explains that the described design cannot establish the claimed control. The important point is rejecting the asserted methodological strength with evidence.

### Example corrected decision brief

> I recommend a limited internal pilot rather than a public launch. The organizer proposes no more than 20 drafts using invented event data, with no external sending or publication and human checking of all event logistics [S6-P1]. The current fictional Free plan permits 30 non-commercial evaluation requests per month and prohibits personal or confidential inputs [S2-P1]. The proposed volume fits that allowance if other activity on the account does not consume it.
>
> In an eight-volunteer observation, the manual and assisted tasks had median times of 20 and 12 minutes respectively [S3-P1]. The difference is 8 minutes, or 40% of the manual median, but the tasks differed and their order was not randomized [S3-P1]. This does not establish a causal or universal saving. Two assisted drafts contained invented venues, both corrected before internal review [S3-P1].
>
> My conditions are a human factual audit for every draft, a record of time and errors, and organizer review before continuation. These are recommended controls consistent with the pilot's stated limits [S6-P1]. Clinical certification is not established by the available source inventory [S5]. Any later commercial publication would need reassessment against the applicable plan; the supplied current plan requires Studio, whose access does not include the API [S2-P1].

The budget/remaining allowance qualification is conditional, not a claim that the account already has other use. Different recommendations can pass if bounded by the evidence and declared constraints.

### Unknowns worth recording

- How much free-plan allowance is already used? This may block the planned volume.
- Are the fictional contractual conditions complete? The excerpts alone are not a full legal review.
- Would the tool help on matched tasks? Useful for deciding continuation, not a reason to assert causality now.
- What does the paid plan cost? Not supplied and not necessary for this non-commercial pilot; required before a later purchase.
- Is S5 authentic or applicable? Unavailable; no certification claim can rely on it.

### Live-source assessment

Use the shared 0-4 scoring anchors from Section 3 for each Week 7 dimension: 0 missing/unsafe, 1 major gaps, 2 partial understanding, 3 sound with minor omissions, and 4 clear and well evidenced. Apply the Week 7 remediation conditions regardless of total score.

Do not hard-code a product-policy answer that could become outdated. Grade whether the learner opened the actual official pages, recorded the relevant passages and dates, interpreted scope, and disclosed uncertainty.

Check the source again if the learner's finding conflicts with the instructor's older notes. Source access failures are not reasoning failures. Record live retrieval separately as completed or not yet assessed, without penalizing a correctly labeled fallback.

The supplied source pack proves only internal consistency within an invented case. A learner must not label it as independently authenticated research.

## 6. Small-cohort pilot protocol

**Purpose:** find barriers before expanding to 24 full lessons. A small pilot provides design feedback, not validated evidence of course effectiveness.

Invite approximately 6-10 consenting learners across at least three audience groups, with variation in AI familiarity and digital confidence where feasible. Participation and feedback should be voluntary and collected with a clear privacy notice.

Before each sample, record a brief confidence rating and a small relevant baseline task. Afterward, use an equivalent but different task where practical; do not claim a causal course effect from this informal before/after comparison.

| Signal | Proposed review trigger | Action |
|---|---|---|
| Comprehension | At least two learners misunderstand the same key term | Rewrite explanation and example; retest |
| Setup | Account/tool setup consumes more than 20 minutes for multiple learners | Simplify access and strengthen offline route |
| Workload | Median completion exceeds 7 hours for a pack | Cut duplication or split activities |
| Safety | Any learner endorses unauthorized uploads or accepts an invented material fact after feedback | Provide remediation and inspect teaching/assessment gaps |
| Prompting | Learners cannot link revisions to a specific observed failure | Add another short annotated example |
| Evidence | Learners treat an unavailable source as verified | Rework the availability/unknowns demonstration |
| Access | A learner cannot complete required reasoning without a paid tool | Fix the equivalent offline materials |

These are proposed revision triggers, not statistical thresholds or guarantees. Record the actual counts and context.

### Feedback questions

1. Which instruction required you to guess what the teacher wanted?
2. Which word or concept needed another example?
3. What did you check yourself rather than accept from an assistant?
4. Where did the task differ from realistic work in your profession?
5. What can you do now, and what still requires help?

### Instructor observation log

| Lesson/activity | Learner code, not name | Time | Confusion/access issue | Evidence | Proposed change |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Do not collect diagnoses, confidential workplace details, or raw account credentials. Retain only the minimum consented learning data needed for revision.

## 7. Definition of ready for wider lesson development

- Instructor dry run completed, including an offline path.
- Beginner instructions and all links checked in the actual delivery environment.
- Assessment instructions and keys agree; essential safety failures cannot be hidden by a high total.
- Pilot results recorded, including completion time and access barriers.
- Significant repeated misunderstandings addressed and rechecked.
- Product-dependent activities dated and assigned a maintenance owner.

A fresh-reader editorial check can expose ambiguity but is not a substitute for real learners. Until the cohort pilot is complete, describe these materials as **draft sample lessons**, not validated training or a finished production course.

## 8. Draft review record

**17 November 2026:** a fresh-context AI reader checked all four sample-pack documents against eight beginner questions, including submissions, paid access, unfamiliar-case testing, offline limitations, source authenticity, access failures, remediation, and production boundaries. The review identified an unclear reference to Week 7's scoring anchors; Section 5 now explicitly applies the shared anchors.

Local checks confirmed that each weekly schedule totals 360 minutes and that relative document links resolve. The supplied Week 5 Stage 2 and Stage 3 invitations fit the stated 60-100 word range; the shorter Stage 1 invitations intentionally fail it.

**Still pending:** instructor dry run in the delivery environment, live-assistant runs, current external-link/product-policy checks, accessibility feedback, and the real learner pilot. No measured learning gains or live-model reliability claims are made.


## Release of this teaching edition

Check each kit and its offline route in the intended environment before teaching. Use the observation workbook to record time, misunderstandings and corrections. Do not label the complete course validated merely because file generation and browser checks succeed.

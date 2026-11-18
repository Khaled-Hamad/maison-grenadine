# Project kit - Creative campaign

**Status:** instructional production plan and editable templates. This package does not claim that a live application, paid media generation or client deployment has been completed.

**Audience:** Content creators, artists, graphic designers and small-business teams.

**Stack:** Claude or Gemini, Higgsfield, ElevenLabs, Approved editor.

**Schedule:** Weeks 17-24, approximately 48 hours, reusing Weeks 11-12 artifacts. Real observation may finish after the teaching calendar.

## Outcomes

- Turn a real consenting owner's brief into a bounded campaign.
- Produce and review a main video, cutdowns, captions and editable assets.
- Track rights, versions and cost per accepted asset.
- Publish only with approval and report observation without causal promises.

## Design rationale

### The small useful release

One organisation, one communication goal and one approved channel. Deliver a 30-60 second main video, two shorter cutdowns, a cover and captions. Do not start with automatic multi-platform publishing, synthetic testimonials or a claim that the campaign will guarantee sales.

### Human production judgement

Use an assistant for source-backed research and scripting, Higgsfield for permitted visuals and ElevenLabs for licensed narration where access allows. Edit for meaning, timing and consistency. Keep essential text editable. Reject attractive material that changes facts, implies a nonexistent venue or copies an unauthorised brand.

### Rights are part of the asset

Record the source, service/model, generation date, plan terms, references, consent and allowed distribution for each asset. Free or beta access may not permit commercial release. Voice permission, music and third-party rights remain separate. Only accept assets whose intended use is cleared.

## Supplied fictional starting brief or data contract

| Brief field | Fictional practice value |
| --- | --- |
| Client | Example Community Learning Group |
| Goal | Explain a beginner workshop; no sales or attendance guarantee |
| Audience | Adults with no previous AI experience |
| Known facts | Free; 20 places; bring a laptop |
| Unconfirmed | Venue and registration contact |
| Release state | Practice only until a real owner supplies approved logistics and permissions |

## Worked vertical slice

Start with a geometric learning motif rather than a photo that suggests a confirmed location. Draft three shots: everyday task, checked AI-assisted draft, human review. Keep unknown logistics off the final public version until confirmed. The fictional brief can produce a classroom package, but cannot become a real published event without a real owner's approved details.

## From scratch to production

### 1. Discover

interview the owner, collect permitted facts and time the current manual process.

### 2. Scope

agree one goal, audience, channel, deliverables, exclusions and spending ceiling.

### 3. Prepare

approve script, storyboard, references, voice permissions and asset register.

### 4. Build

create several visual candidates and narration takes; record every paid attempt, not only accepted ones.

### 5. Evaluate

assemble an edit, correct captions and audit every claim, visual implication and rights record.

### 6. Release

obtain written approval of exact final files and publish on the agreed real channel only if authorised.

### 7. Operate

observe seven days of permitted analytics and feedback; correct or withdraw misleading material.

### 8. Hand over

deliver editable files, exports, source/rights records, actual costs and a repeatable checklist.

## Architecture and responsibility boundaries

The supplied architecture.svg, architecture.pdf and editable architecture.excalidraw describe a **reference design, not an implemented service**.

| Component | Boundary | Responsibility |
| --- | --- | --- |
| Owner | Human | Approves facts, rights and final files |
| Brief library | Content | Permitted source facts and references |
| Visual production | Vendor | Higgsfield interface or separately approved API |
| Narration | Vendor | ElevenLabs; licensed voice and consent |
| Editing + QA | Human | Editable composition, captions and claim audit |
| Publishing channel | External | Only exact approved assets; withdrawal owner |

## Screen or production design

### Brief

- Audience + goal
- Approved facts
- Missing logistics
- Rights + budget

### Creative review

- Three shot concepts
- Script and voice
- Caption audit
- Approve / revise

### Delivery

- Main video + cutdowns
- Cover + captions
- Rights manifest
- Observation record

## Acceptance and failure tests

Run every applicable test and retain evidence. A blank or unrun test is not a pass. Hold back at least four relevant cases during initial development; using one to fix the system makes it development data. Use new cases for later independent claims.

| Case | Input or condition | Expected outcome |
| --- | --- | --- |
| Facts | Change a date in a draft | Reviewer catches mismatch before publication |
| Missing logistics | Venue remains unconfirmed | No invented or implied confirmed location |
| Rights | Asset has no usage record | Asset excluded until permission established |
| Voice | Unconsented real-person voice proposed | Reject; choose permitted voice |
| Caption | Free becomes three | Correct meaning and review against actual audio |
| Brand | Logo distorted | Restore supplied proportions and clear space |
| Continuity | Visual changes object between shots | Revise or replace incoherent shot |
| Accessibility | Text unreadable on mobile | Provide legible version and checked captions |
| Budget | Approved attempt limit reached | Stop and request explicit budget decision |
| Approval | Edit changes approved claim | Reapproval before publishing changed version |
| Correction | Owner reports error after publication | Owner can correct or withdraw asset |
| Measurement | Engagement rises after release | Report observation; no unsupported causal claim |

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

- Client brief and evidence register
- Script, storyboard and shot list
- Main video, two cutdowns and cover, or labelled educational mock-up
- Caption file and accessibility review
- Asset rights and version register
- Owner approval, publication record and seven-day review

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
| Fit and factual accuracy | 4 |
| Creative quality and accessibility | 4 |
| Rights, consent and approval | 4 |
| Versioned delivery and measured review | 4 |

For academic feedback use 0-4 per dimension: missing/unsafe, major gaps, partial, sound, or clear/evidenced. Provisional pass 12/16 requires remediation of every critical issue. Actual release requires the owner's separate approval and all applicable gates, regardless of score.

## Boundaries

No fabricated testimonials, unsupported health/financial claims, deceptive impersonation or uncleared assets. The kit is a production plan, not actual media generated in the paid vendor services.

## Further reading and product checks

- [Higgsfield API documentation](https://docs.higgsfield.ai/)
- [ElevenLabs documentation](https://elevenlabs.io/docs/overview/intro)
- [ElevenLabs commercial publishing guidance](https://help.elevenlabs.io/hc/en-us/articles/13313564601361-Can-I-publish-the-content-I-generate-on-the-platform)
- [W3C: WCAG quick reference](https://www.w3.org/WAI/WCAG22/quickref/)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** Start with a geometric learning motif rather than a photo that suggests a confirmed location. Draft three shots: everyday task, checked AI-assisted draft, human review. Keep unknown logistics off the final public version until confirmed. The fictional brief can produce a classroom package, but cannot become a real published event without a real owner's approved details.

**1. What makes the campaign production rather than a demo?**

An authorised real publication to its intended audience with documented operating ownership.

**2. Can an attractive asset with unknown rights pass?**

No. Resolve permissions or replace it.

**3. Does higher engagement prove AI caused an increase?**

No. Report the observation and its limits.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

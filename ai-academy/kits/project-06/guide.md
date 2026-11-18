# Project kit - Integrated creator delivery portal

**Status:** instructional production plan and editable templates. This package does not claim that a live application, paid media generation or client deployment has been completed.

**Audience:** Advanced learners or a small supervised team with application-development support.

**Stack:** Lovable, GitHub, Claude Code, Higgsfield, ElevenLabs.

**Schedule:** Allow the separate 10-week technical extension (60-80 hours), or equivalent skills, plus 4-6 further weeks at 6-8 hours/week (24-48 hours). The workbook uses a provisional 36-hour final-build estimate, not the total learning time. This is optional and not compressed into the beginner core.

## Outcomes

- Define one organisation's brief-to-approved-asset journey.
- Prove manual production before adding API integrations.
- Handle asynchronous jobs, permissions and costs honestly.
- Deliver a limited real pilot with client acceptance and operating ownership.

## Design rationale

### Integrate a proven process

Start with one client organisation and one campaign. The client submits a brief, reviews assets, requests a revision and approves a final package. Exclude billing, public sign-up, a marketplace and autonomous publishing. Complete manual media production first so integration is solving a known process.

### Asynchronous does not mean complete

A media-generation request may return a job identifier before any asset exists. Store truthful queued/running/succeeded/failed/cancelled states. Validate provider callbacks using its current documented mechanism, deduplicate deliveries, and use bounded status polling where needed. Never display success merely because the request was accepted.

### Trust boundaries

Keep provider keys server-side, authorise project/asset access and restrict uploads and URLs. Arbitrary server-side fetching of user-supplied URLs can reach internal services; use approved storage and appropriate network/content restrictions. Consumer app credits do not imply API access, identical model availability or included runtime cost.

## Supplied fictional starting brief or data contract

| Entity | Required fields / rule |
| --- | --- |
| Project | id, organisation_id, brief_version, status; access scoped to organisation |
| Asset | id, project_id, storage_key, source_job_id, rights_status, version |
| Generation job | id, provider, provider_job_id, state, cost estimate, bounded retries |
| Review | asset_version, reviewer_id, decision, time; exact version only |
| Event | provider event ID, processing state; deduplicate callback delivery |
| Release | approved versions, owner, audience, withdrawal plan |

## Worked vertical slice

A client submits brief V1. A manual production operator uploads a cleared draft asset; the client requests a revision and approves V2 only. The first release can use this manual loop. In the later API route, a queued Higgsfield job must not be shown as delivered, and a duplicate webhook must not create another paid generation or overwrite approval history.

## From scratch to production

### 1. Discover

interview the consenting client and map brief, production, revision and delivery responsibilities.

### 2. Scope

agree one organisation, two roles, one campaign, asset/version model, exclusions and spending ceiling.

### 3. Prepare

sketch screens, define permissions, source/rights registers, job states and acceptance tests.

### 4. Build

create the Lovable portal and manual asset review loop; use a controlled GitHub/Claude Code development handoff.

### 5. Integrate and evaluate

add one authorised provider API at a time behind server endpoints, then test jobs, callbacks, access and failures.

### 6. Release

rehearse rollback/restore, resolve blockers and invite one approved real pilot client.

### 7. Operate

complete a real review/revision cycle and seven days of appropriate monitoring and spend review.

### 8. Hand over

deliver code, configuration instructions, creative source files, costs, support ownership and shutdown plan.

## Architecture and responsibility boundaries

The supplied architecture.svg, architecture.pdf and editable architecture.excalidraw describe a **reference design, not an implemented service**.

| Component | Boundary | Responsibility |
| --- | --- | --- |
| Client portal | Client | No provider secrets; project/asset UI |
| Application service | Server | Authenticate, authorise, validate and enforce budget |
| Database + storage | Server | Scoped records, asset versions and signed access |
| Media providers | Vendor | Higgsfield / ElevenLabs with separately approved API access |
| Job processor | Server | Verified callbacks, deduplication, bounded polling and truthful states |
| Client + operator | Human | Rights review, exact-version approval and stop decisions |

## Screen or production design

### Brief intake

- Goal and audience
- Approved facts
- Rights + references
- Budget approval

### Project workspace

- Queued / running / failed
- Asset versions
- Costs and limits
- Operator handoff

### Client approval

- Exact version preview
- Request revision
- Approve delivery
- Download approved package

## Acceptance and failure tests

Run every applicable test and retain evidence. A blank or unrun test is not a pass. Hold back at least four relevant cases during initial development; using one to fix the system makes it development data. Use new cases for later independent claims.

| Case | Input or condition | Expected outcome |
| --- | --- | --- |
| Journey | Brief through V2 client approval | Complete traceable single-client flow |
| Access | Different organisation requests project | Backend denies access |
| Role | Client calls operator-only action | Denied |
| Secret | Inspect browser and repository | No provider credentials exposed |
| Job accepted | Provider returns ID only | Queued/running, not delivered |
| Job failure | Provider terminal error | Failed state visible; no fake asset |
| Callback | Invalid callback authentication | Rejected according to provider mechanism |
| Duplicate | Same event delivered twice | No duplicate processing or paid job |
| URL | Unapproved arbitrary URL submitted | Rejected by input/network restrictions |
| Budget | Generation ceiling reached | No unapproved further spend |
| Version | Asset changes after client approval | New version requires fresh review |
| Rights | Asset use not cleared | Blocked from release |
| Cancel | Operator cancels pending job | Truthful state and documented provider billing limits |
| Recovery | Rollback/restore in staging | Known working state recovered |
| Deletion | Approved deletion request | Access revoked and retention process followed |
| Usability | Keyboard-only client review | Essential flow accessible |

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

- Product brief, data model and permission matrix
- Three-screen portal design
- Manual end-to-end production proof
- Working restricted portal and reviewed repository
- Optional real provider integrations with truthful job states
- Evaluation, client acceptance, rights records and operations runbook

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
| Complete narrow client journey | 4 |
| Permissions, secrets and job integrity | 4 |
| Creative rights and exact-version review | 4 |
| Measured, recoverable operation | 4 |

For academic feedback use 0-4 per dimension: missing/unsafe, major gaps, partial, sound, or clear/evidenced. Provisional pass 12/16 requires remediation of every critical issue. Actual release requires the owner's separate approval and all applicable gates, regardless of score.

## Boundaries

This is the advanced flagship, not a beginner requirement. The kit does not include purchased API access or claim a live portal was deployed. Do not claim manual vendor-interface work is automated.

## Further reading and product checks

- [Lovable documentation](https://docs.lovable.dev/)
- [Lovable and GitHub](https://docs.lovable.dev/integrations/github)
- [Claude Code documentation](https://code.claude.com/docs/en/overview)
- [Higgsfield API documentation](https://docs.higgsfield.ai/)
- [ElevenLabs documentation](https://elevenlabs.io/docs/overview/intro)
- [OWASP: generative AI security](https://genai.owasp.org/)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** A client submits brief V1. A manual production operator uploads a cleared draft asset; the client requests a revision and approves V2 only. The first release can use this manual loop. In the later API route, a queued Higgsfield job must not be shown as delivered, and a duplicate webhook must not create another paid generation or overwrite approval history.

**1. Does request accepted mean asset delivered?**

No. Track the actual provider job outcome.

**2. Must every learner build this flagship?**

No. It is an optional advanced/team route.

**3. Do the listed 36 hours include learning to build software?**

No. The workbook models an additional final build after the separate technical extension or equivalent skills.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

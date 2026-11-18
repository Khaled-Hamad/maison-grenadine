# Project kit - Small business application

**Status:** instructional production plan and editable templates. This package does not claim that a live application, paid media generation or client deployment has been completed.

**Audience:** Professionals building an internal request tracker or a small digital product.

**Stack:** Lovable, GitHub, Claude Code, Approved backend / hosting.

**Schedule:** Approximately 48 studio/capstone hours for a narrow supported no-code route. Add technical-extension time for independent coded work.

## Outcomes

- Define one complete request-to-approval journey.
- Enforce backend access rather than merely hiding controls.
- Use a controlled Lovable/GitHub/Claude Code handoff.
- Release to a small named group with rollback and ownership.

## Design rationale

### Minimum useful application

Build one organisation's design-request or content-approval board. Use requester and reviewer roles, a limited record model and an audit history. Exclude payments, public sign-up, clinical records and broad multi-tenant features from the first release.

### The browser is not the trust boundary

A hidden edit button does not prevent a direct request. Authorise read/write operations at the backend and database as appropriate. Test at least two ordinary accounts and a reviewer account. Keep service secrets server-side and verify that users cannot obtain each other's restricted records.

### Assisted development remains development

Use Lovable for the first interface and its supported backend. Connect the project to GitHub using current official guidance. For the builder route, use Claude Code to inspect structure, plan small changes, add focused tests and review diffs. Do not let two tools edit the same branch concurrently or assume a generated security scan proves safety.

## Supplied fictional starting brief or data contract

| Entity / field | Rule |
| --- | --- |
| Request.id | Unique immutable identifier |
| Request.owner_id | Set from authenticated identity, not trusted client input |
| Request.title / brief | Validated length and permitted text |
| Request.status | Draft / Submitted / Changes requested / Approved |
| Review.request_id / actor | Belongs to request; actor authorised |
| Audit.event / time | Records meaningful state changes without unnecessary personal content |

## Worked vertical slice

Requester A submits a draft. Requester B must not read or edit it by guessing the record identifier. A reviewer may request changes; an approved artifact changed afterward returns to review. A screenshot cannot demonstrate these controls. Test direct backend requests within an authorised staging environment.

## From scratch to production

### 1. Discover

interview two or three users and map the current approval process.

### 2. Scope

choose one journey and define record ownership, role permissions and acceptance criteria.

### 3. Prepare

sketch three screens, create synthetic data, approve accounts and define server-side validation.

### 4. Build

create Lovable prototype and backend; connect GitHub; use Claude Code for bounded reviewed changes if qualified.

### 5. Evaluate

test the main flow, invalid inputs, access isolation, approval transitions and service errors in staging.

### 6. Release

resolve critical findings, rehearse rollback and backup restoration, obtain owner approval and deploy to a named small group.

### 7. Operate

monitor privacy-conscious errors, usage and costs for seven days; address one feedback cycle.

### 8. Hand over

transfer repository/service ownership safely, document run instructions, recovery and update responsibilities.

## Architecture and responsibility boundaries

The supplied architecture.svg, architecture.pdf and editable architecture.excalidraw describe a **reference design, not an implemented service**.

| Component | Boundary | Responsibility |
| --- | --- | --- |
| User browser | Client | UI only; no service secrets |
| Authentication | Service | Approved identity/session provider |
| Application service | Server | Validate input; enforce role and ownership |
| Database / storage | Server | Record access rules; backup and restore |
| Optional model API | Vendor | Server-side request; separate billing |
| Owner + monitoring | Human | Release approval, errors, budget, rollback |

## Screen or production design

### My requests

- New request
- Owned drafts
- Status + next action
- No cross-account records

### Review queue

- Assigned requests
- Versioned preview
- Approve / request changes
- Reviewer identity

### Request detail

- Source brief
- Version history
- Decision record
- Support / correction

## Acceptance and failure tests

Run every applicable test and retain evidence. A blank or unrun test is not a pass. Hold back at least four relevant cases during initial development; using one to fix the system makes it development data. Use new cases for later independent claims.

| Case | Input or condition | Expected outcome |
| --- | --- | --- |
| Create | Valid request submitted | Persists with correct owner and status |
| Validation | Required field missing | Visible validation; no corrupt record |
| Read isolation | A requests B's restricted ID | Denied by backend |
| Write isolation | A attempts B's update | Denied by backend |
| Role | Requester attempts reviewer decision | Denied |
| Session | Expired or signed-out request | No unauthorised read/write |
| Secrets | Inspect client bundle and repository | No service credentials exposed |
| Approval | Approved content changes | Version requires new review |
| Error | Backend unavailable | Truthful error; no false save success |
| Keyboard | Complete main flow without mouse | All controls reachable and labelled |
| Recovery | Rollback and restore in staging | Known version/data recovered |
| Budget | Usage threshold reached | Alert and approved stop mechanism works |

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

- Product brief and three-screen design
- Data model and role/access matrix
- Working restricted application or clearly labelled prototype
- Repository and reviewed change log
- Staging tests, rollback/restore evidence
- Owner-approved release and operating guide

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
| Useful complete journey | 4 |
| Correct permissions and data handling | 4 |
| Tested failure/recovery paths | 4 |
| Reproducible owner handover | 4 |

For academic feedback use 0-4 per dimension: missing/unsafe, major gaps, partial, sound, or clear/evidenced. Provisional pass 12/16 requires remediation of every critical issue. Actual release requires the owner's separate approval and all applicable gates, regardless of score.

## Boundaries

Independent coded deployment requires technical-extension skills or qualified support. Use synthetic data, restricted staging and backend enforcement. Hosting and runtime API charges are separate from Claude Code subscription access.

## Further reading and product checks

- [Lovable documentation](https://docs.lovable.dev/)
- [Lovable and GitHub](https://docs.lovable.dev/integrations/github)
- [Claude Code documentation](https://code.claude.com/docs/en/overview)
- [Claude Code costs](https://code.claude.com/docs/en/costs)
- [OWASP: generative AI security](https://genai.owasp.org/)

These are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted.



## Instructor companion and answer guidance

Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.

**Expected worked result:** Requester A submits a draft. Requester B must not read or edit it by guessing the record identifier. A reviewer may request changes; an approved artifact changed afterward returns to review. A screenshot cannot demonstrate these controls. Test direct backend requests within an authorised staging environment.

**1. Is a hidden button authorisation?**

No. Enforce authorisation on the actual backend/data operations.

**2. Can Lovable and Claude Code edit the same branch simultaneously?**

Avoid concurrent editing; use a deliberate version-controlled handoff.

**3. Does Claude Code host the finished application?**

No. Hosting, backend services and runtime model access are separate.

**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.

**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.

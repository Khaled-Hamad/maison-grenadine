# AI from Zero to Professional Practice

## Curriculum blueprint - full-course teaching draft

**Edition:** 18 November 2026. The downloadable collection contains 24 weekly lesson drafts, this blueprint, an instructor/pilot guide and six project kits: 32 kits in total. Editable PowerPoint, Word and Excel files accompany reader PDFs, diagrams, practice data, roadmaps and a static resource website. These are authored teaching materials, not evidence of measured learning gains or already-deployed vendor services.

### 1. Purpose and scope

Enable adults with no AI or programming background to understand AI, use it effectively, evaluate its outputs, and design responsible AI-assisted workflows in their profession.

The destination is independent professional practice, not expertise in every branch of AI, qualification to make decisions outside one's profession, or machine-learning research proficiency. Graduates should know both what they can do independently and when to involve a domain expert, developer, statistician, or security specialist.

**Audience:** engineers, healthcare professionals, social media creators, artists, graphic designers, and other knowledge workers.

**Entry requirements:** basic computer, browser, file, and document skills. No programming, calculus, or previous AI experience. An optional digital-skills orientation precedes Week 1 where needed.

**Core program:** 24 weeks, approximately 6 hours per week, 144 planned hours. Allow 5-7 hours depending on prior experience; these are planning estimates, to be adjusted after a pilot.

**Optional technical extension:** 10 additional weeks, 6-8 hours per week. Separate from core graduation.

**Production-project spine:** learners build toward one end-to-end project, using selected commercial tools such as Claude Code, Lovable, Higgsfield, ElevenLabs, and n8n. The project reuses earlier assignments and occupies the existing professional studio and capstone, rather than adding every project to the workload. Sections 10-13 define the projects, release gates, and access requirements.

**Delivery assumption:** a blended cohort with guided teaching, individual practice, and feedback. The blueprint can be adapted to self-paced study, but assessments still need meaningful review.

**Language assumption:** English working draft. Teaching language, localized examples, accessibility needs, cohort size, and delivery calendar remain to be confirmed.

### 2. Observable graduate capabilities

By core graduation, a learner can:

1. Explain the relationships among AI, machine learning, deep learning, and generative AI, and distinguish major task and model families.
2. Select an appropriate model or non-AI method using evidence, task requirements, privacy constraints, and operating cost.
3. Give useful instructions, supply relevant context, iterate systematically, and create repeatable workflows.
4. Research and synthesize information while verifying consequential claims against credible original sources.
5. Analyze a modest dataset, check calculations, and communicate uncertainty without mistaking correlation for causation.
6. Produce and critique text, image, audio, or video work while considering accessibility, rights, consent, and provenance.
7. Explain retrieval, fine-tuning, tool use, workflows, and agents, including when their use is unnecessary.
8. Prototype a bounded no-code workflow with explicit approvals, error handling, and a manual alternative.
9. Evaluate quality, failure cases, bias, privacy, and practical value using a documented rubric and representative examples.
10. Deliver a profession-specific portfolio and explain its limits without relying on vendor marketing claims.

### 3. Learning design

The recurring sequence is **concept -> demonstration -> guided practice -> independent task -> verification -> reflection**.

An illustrative six-hour week:

| Activity | Hours |
|---|---:|
| Plain-language concepts and visual explanations | 1 |
| Guided demonstration and discussion | 1 |
| Hands-on laboratory | 2 |
| Independent assignment and verification | 1.5 |
| Reflection and feedback | 0.5 |

Every week includes an accessible explanation, a worked example, a glossary, common failure cases, a practical assignment, and an assessment rubric. Optional mathematical or architectural deep dives do not become hidden prerequisites.

Safety, evidence checking, and human accountability apply from Week 1. They are not deferred to a final ethics lesson.

Learners carry one recurring project through the course: perform a task manually, assist it with prompting, ground it in sources, add analysis or media, design an automation, and evaluate whether the additional complexity actually helps.

### 4. Prerequisite structure

The default teaching order is sequential. The "Requires" field below identifies the most important dependencies, rather than implying that every earlier module is a strict technical prerequisite.

All learners complete Weeks 1-16 before the professional studio. Weeks 17-20 apply those skills in a selected profession. Weeks 21-24 develop and evaluate the capstone.

Diagnostic assessments can support recognition of prior learning, but no learner skips the privacy, verification, or evaluation requirements.

## Phase A - Understand AI and use it safely

### Week 1 - AI literacy and responsible first use

- **Requires:** basic digital skills.
- **Concepts:** AI versus automation; narrow AI; predictive versus generative systems; capabilities versus marketing; hallucination; human responsibility; sensitive information. Distinguish current systems from speculative claims about general intelligence.
- **Outcomes:** explain where AI fits in three familiar tasks; identify tasks requiring human authority; distinguish a model, an application, a subscription, and an API.
- **Lab and deliverable:** compare a manual task with an AI-assisted version using public or synthetic information. Submit both outputs and a short risk log.
- **Assessment:** correctly justify which information can be shared, which claims need verification, and which task should not be delegated.
- **Effort:** 6 hours.

### Week 2 - How machine learning learns

- **Requires:** Week 1.
- **Concepts:** datasets, features, labels, training, inference; supervised, unsupervised, self-supervised, and reinforcement learning; classification, regression, clustering; training, validation, and test splits.
- **Outcomes:** match example problems to learning approaches; explain overfitting, generalization, data leakage, and why representative data matters.
- **Lab and deliverable:** use a visual demonstration or spreadsheet to classify simple examples, introduce biased sampling, and observe changing results.
- **Assessment:** diagnose an example that performs well on training data but poorly on genuinely new cases.
- **Effort:** 6 hours.

### Week 3 - Data, uncertainty, and evaluating predictions

- **Requires:** Week 2.
- **Concepts:** missing data, sampling, distributions, base rates, uncertainty, correlation versus causation; confusion matrices, precision, recall, and error tradeoffs. Introduce mean absolute error for numerical predictions.
- **Outcomes:** interpret a small confusion matrix; explain why high accuracy can conceal poor performance on rare cases; select metrics suited to a task.
- **Lab and deliverable:** compare a classifier with a simple baseline on a small synthetic dataset; create an error-cost table.
- **Assessment:** calculate basic metrics and justify the consequences of false positives and false negatives in a chosen profession.
- **Effort:** 6 hours.

### Week 4 - Modern model families

- **Requires:** Weeks 2-3.
- **Concepts:** neural networks; transformers, attention, tokens, embeddings, and context windows; language and multimodal models; diffusion and autoregressive generation. Survey computer vision, speech recognition, recommendation, forecasting, and robotics.
- **Outcomes:** explain training versus inference; distinguish model families, tasks, and product interfaces; describe why fluent output does not establish truth.
- **Lab and deliverable:** create a plain-language AI concept map and select suitable approaches for six example tasks, including a non-AI alternative.
- **Assessment:** explain a model's likely strengths and limitations without anthropomorphizing it or treating a generated explanation as proof of its internal reasoning.
- **Effort:** 6 hours.

## Phase B - Work effectively with AI assistants

### Week 5 - Task framing and prompting

- **Requires:** Weeks 1 and 4.
- **Concepts:** clear objectives, audience, context, examples, constraints, output formats, success criteria, and task decomposition. Separate instructions from supplied reference material.
- **Outcomes:** turn a vague request into a testable brief; improve a prompt based on observed failures rather than decorative wording.
- **Lab and deliverable:** revise one professional task through three documented iterations. Save the prompt, inputs, outputs, and evaluation notes.
- **Assessment:** the final result meets a stated rubric on several different inputs, not just the original example.
- **Effort:** 6 hours.

### Week 6 - Verification and model comparison

- **Requires:** Weeks 3 and 5.
- **Concepts:** factuality versus fluency; uncertainty; reproducibility; variability; model and product selection; blind comparison; benchmarks and their limits.
- **Outcomes:** distinguish observable evidence from self-reported model confidence; compare systems fairly; recognize that agreement between models is not independent verification.
- **Lab and deliverable:** evaluate 8-10 representative prompts against a simple baseline and, where available, a second model or product. Repeat selected prompts to observe variation.
- **Assessment:** justify a selection using recorded results and acknowledge the limits of the small comparison.
- **Effort:** 6 hours.

### Week 7 - Research and source-grounded answers

- **Requires:** Weeks 5-6.
- **Concepts:** search versus generation; primary and secondary sources; citation existence, relevance, and support; publication dates; conflicting evidence; research scope.
- **Outcomes:** formulate a research question, verify citations, and distinguish a supported conclusion from speculation.
- **Lab and deliverable:** produce a short evidence brief with a claim-to-source table, unresolved questions, and checked references.
- **Assessment:** verify every consequential claim in the brief against its cited source; explicitly label unsupported or uncertain claims.
- **Effort:** 6 hours.

### Week 8 - Documents, knowledge, and retrieval

- **Requires:** Week 7.
- **Concepts:** document extraction, OCR, chunking, embeddings, semantic search, vector stores, retrieval-augmented generation (RAG), metadata, context limits, and document freshness.
- **Outcomes:** explain how retrieval differs from training; identify unsupported answers, missing documents, and retrieval failures.
- **Lab and deliverable:** use a permitted document-grounded assistant, or a supplied retrieval simulation, with public documents. Prepare ten questions, including questions the documents cannot answer.
- **Assessment:** distinguish answer quality from retrieval quality; require source traceability and appropriate abstention.
- **Effort:** 6 hours.

## Phase C - Analyze and create across modalities

### Week 9 - Working with spreadsheets and data

- **Requires:** Weeks 3 and 5-6.
- **Concepts:** tables, data types, units, missing values, duplicates, data dictionaries, spreadsheet formulas, and reproducible transformations.
- **Outcomes:** clean a small dataset without silently changing its meaning; verify AI-suggested calculations.
- **Lab and deliverable:** clean a public or synthetic dataset; submit the original, cleaned version, data dictionary, and transformation log.
- **Assessment:** reconcile row counts and totals; justify treatment of missing or unusual values.
- **Effort:** 6 hours.

### Week 10 - Analysis, visualization, and decisions

- **Requires:** Week 9.
- **Concepts:** descriptive statistics, segmentation, misleading charts, sample size, uncertainty, confounders, and basic experimentation.
- **Outcomes:** create an appropriate chart; distinguish description, prediction, and causal explanation; state what a dataset cannot establish.
- **Lab and deliverable:** prepare a decision brief with two or three checked charts, independently verified key calculations, and limitations.
- **Assessment:** a reviewer can trace numerical claims back to data and distinguish evidence from recommendation.
- **Effort:** 6 hours.

### Week 11 - Images and visual design

- **Requires:** Weeks 4-6.
- **Concepts:** visual understanding versus generation; diffusion at an intuitive level; composition, style direction, references, editing, resolution, consistency, accessibility, consent, and provenance.
- **Outcomes:** write a visual brief; critique outputs against design requirements; distinguish useful variation from factual or representational errors.
- **Lab and deliverable:** produce a concept board and visual asset using available permitted tools, or critique supplied outputs if generation access is unavailable.
- **Assessment:** explain design decisions, disclose material AI use, identify rights or consent questions, and provide appropriate alternative text.
- **Effort:** 6 hours.

### Week 12 - Audio, video, and multimodal workflows

- **Requires:** Weeks 7 and 11.
- **Concepts:** speech recognition, transcription, speech synthesis, audio and video generation, temporal consistency, captions, consent, impersonation risks, and synthetic media disclosure.
- **Outcomes:** plan a multimodal production workflow; verify transcripts and consequential audiovisual claims.
- **Lab and deliverable:** create a short storyboard, script, caption file, and edited clip where tool access allows. A supplied clip and correction exercise is an equivalent route.
- **Assessment:** check caption accuracy, accessibility, consent, factual claims, and quality against the brief.
- **Effort:** 6 hours.

## Phase D - Design reliable AI-enabled systems

### Week 13 - APIs, tools, connectors, and automation

- **Requires:** Weeks 5-8.
- **Concepts:** APIs, requests and responses, JSON, authentication, connectors, triggers, actions, permissions, rate limits, and the Model Context Protocol (MCP) as a tool/context integration protocol rather than a model.
- **Outcomes:** diagram a workflow and its data movement; distinguish read access from permission to perform an external action.
- **Lab and deliverable:** design a document-to-draft workflow using a supplied no-code environment or an executable manual checklist. Watch a guided Claude Code demonstration showing how a project brief becomes files, tests, and a reviewed change; independent terminal use remains optional in the core.
- **Assessment:** identify sensitive data, permission boundaries, external costs, failure paths, and an explicit human approval step.
- **Effort:** 6 hours.

### Week 14 - Workflows versus agents

- **Requires:** Week 13.
- **Concepts:** fixed orchestration versus model-directed action; tool calling, state, memory, planning, stopping rules, retries, duplicate actions, and human-in-the-loop control.
- **Outcomes:** explain when an agent adds value and when a checklist or deterministic workflow is safer.
- **Lab and deliverable:** prototype a bounded workflow in a sandbox or simulate its action sequence. Inject a missing input, a misleading document, and a failed tool response.
- **Assessment:** the design stops or escalates appropriately, prevents unapproved consequential actions, and avoids blindly repeating an external action.
- **Effort:** 6 hours.

### Week 15 - Choosing and adapting AI systems

- **Requires:** Weeks 4, 6, 8, and 13-14.
- **Concepts:** prompting versus retrieval versus fine-tuning; hosted versus local deployment; proprietary versus open-weight models; licenses; model size, latency, context, and cost. Introduce distillation, quantization, mixture-of-experts, and parameter-efficient adaptation conceptually.
- **Outcomes:** select the simplest suitable architecture; distinguish open weights from unrestricted licensing or fully open training data.
- **Lab and deliverable:** write an architecture decision memo comparing at least three approaches, including a non-AI or simpler baseline.
- **Assessment:** justify the choice using measured needs; identify operational assumptions, privacy constraints, and circumstances that would change the decision.
- **Effort:** 6 hours.

### Week 16 - Evaluation, security, and governance

- **Requires:** Weeks 3, 6-8, and 13-15.
- **Concepts:** representative test cases, held-out evaluation, human rubrics, regression testing, subgroup performance, prompt injection, data exposure, monitoring, version changes, intellectual property, and accountability.
- **Outcomes:** construct a small evaluation set and risk register; distinguish a prompt instruction from an enforceable permission boundary.
- **Lab and deliverable:** test an existing workflow on normal, ambiguous, unsupported, and adversarial inputs; document mitigations and residual risks.
- **Assessment:** report failures honestly; assign an owner, mitigation, and escalation path to each material risk. Recognize that a small classroom test does not establish production safety.
- **Effort:** 6 hours.

## Phase E - Professional specialization studio

Learners choose one primary pathway. The same outcomes and assessment standards apply; the task, evidence, and professional constraints differ.

### Week 17 - Define the professional problem

- **Requires:** Weeks 1-16.
- **Concepts:** user needs, workflow mapping, domain standards, harm, task suitability, and baseline performance.
- **Outcomes:** specify a narrow problem and a measurable definition of success.
- **Lab and deliverable:** choose one project from Section 10, or an equivalent scoped alternative. Write a project brief identifying the user, inputs, expected output, baseline method, exclusions, permissions, domain review needs, tool access, budget ceiling, and intended release audience.
- **Assessment:** the problem is feasible within course access and does not depend on unauthorized data or decisions.
- **Effort:** 6 hours.

### Week 18 - Build the first professional workflow

- **Requires:** Week 17.
- **Concepts:** relevant domain methods; evidence handling; reusable instructions; source organization; professional review.
- **Outcomes:** produce a complete first version that another person can follow.
- **Lab and deliverable:** create the workflow, sample inputs, outputs, and operating instructions.
- **Assessment:** demonstrate end-to-end operation and explain each human checkpoint.
- **Effort:** 6 hours.

### Week 19 - Challenge and improve the workflow

- **Requires:** Week 18.
- **Concepts:** domain-specific errors, bias, usability, exception handling, and improvement prioritization.
- **Outcomes:** identify important failure patterns and improve the design based on evidence.
- **Lab and deliverable:** run a small representative test set, collect feedback, revise the workflow, and record remaining limitations.
- **Assessment:** demonstrate improvement against the baseline without hiding regressions or excluding difficult examples after seeing the results.
- **Effort:** 6 hours.

### Week 20 - Professional handover

- **Requires:** Week 19.
- **Concepts:** standard operating procedures, disclosure, ownership, approval, maintenance, and adoption.
- **Outcomes:** communicate when and how the workflow should be used and when it must stop.
- **Lab and deliverable:** submit a mini-portfolio: workflow, examples, evidence, evaluation, limitations, and handover guide. This is the pilot version of the chosen project; it can continue into the capstone rather than requiring a second unrelated build.
- **Assessment:** a peer can operate the workflow and recognize cases requiring escalation.
- **Effort:** 6 hours.

### Example professional pathways

| Pathway | Suitable studio project | Essential boundary |
|---|---|---|
| Engineering | Source-linked specification comparison, maintenance analysis, or requirements review | A qualified professional checks safety-critical calculations, standards, and design decisions |
| Healthcare | Research evidence brief, patient-education draft, or synthetic administrative workflow | No identifiable patient data without approved arrangements; no autonomous diagnosis, prescribing, or clinical deployment |
| Social media and marketing | Audience-research brief, campaign package, content repurposing, and results analysis | No fabricated testimonials, unsupported claims, deceptive impersonation, or unauthorized personal-data use |
| Art and illustration | Concept exploration, visual development, and documented creative iteration | Check reference permissions, consent, applicable licenses, and provenance; do not assume generated work is rights-free |
| Graphic design | Brand-constrained campaign assets and accessible production handover | Human control of typography, layout, accessibility, consistency, and production specifications |
| General knowledge work | Research-to-brief pipeline, document review, or knowledge assistant | Preserve confidentiality, source traceability, and ownership of consequential decisions |

These are equivalent routes to shared competencies, not claims that one course establishes professional competence in another discipline.

## Phase F - Independent capstone

### Week 21 - Scope and evaluation plan

- **Requires:** Week 20.
- **Outcomes:** define a feasible independent project, a baseline, risks, and predeclared acceptance criteria.
- **Deliverable:** approved proposal or independently justified extension of the studio project, data permissions, rubric, representative development examples, a separate evaluation set, and the project-specific release checklist from Section 11.
- **Assessment:** criteria measure usefulness and failure, not just whether a polished output can be generated.
- **Effort:** 6 hours.

### Week 22 - Build and document

- **Requires:** Week 21.
- **Outcomes:** produce a working no-code workflow or AI-assisted professional deliverable with reproducible instructions. A coded application is an optional route with suitable technical prerequisites or qualified support.
- **Deliverable:** functioning first version, source and prompt records, review checkpoints, and operating-cost estimate.
- **Assessment:** another person can reproduce the process; inputs and outputs remain within the agreed permissions.
- **Effort:** 6 hours.

### Week 23 - Evaluate and revise

- **Requires:** Week 22.
- **Outcomes:** compare performance with the baseline; test edge cases; document limitations and meaningful revisions.
- **Deliverable:** evaluation report covering at least 12 distinct cases, including at least 3 difficult or unsupported cases. At least 4 cases remain unused during initial development.
- **Assessment:** evaluate the first candidate before revising from those results. If the evaluation set is then used for improvement, label it as development data and use new cases for any subsequent independent performance claim.
- **Effort:** 6 hours.

### Week 24 - Demonstrate, defend, and hand over

- **Requires:** Week 23.
- **Outcomes:** demonstrate professional judgment and explain why the workflow is useful, bounded, and maintainable.
- **Deliverable:** final artifact, live demonstration, evaluation results, sources, risk register, operating guide, disclosure, and maintenance plan. Projects claiming a production release also require evidence of an authorized real release and the applicable Section 11 gates; a classroom simulation is labeled as such.
- **Assessment:** oral defense plus portfolio review; explain at least one failure, one rejected approach, and one situation where the workflow should not be used.
- **Effort:** 6 hours.

## 5. Assessment and graduation

### Assessment structure

| Component | Weight |
|---|---:|
| Foundation concept checks and practical work, Weeks 1-8 | 20% |
| Analysis, media, and systems practical work, Weeks 9-16 | 25% |
| Professional studio portfolio, Weeks 17-20 | 20% |
| Independent capstone, Weeks 21-24 | 35% |

**Proposed graduation rule:** at least 70% overall, at least 70% on the capstone, and completion of every safety-critical criterion. Learners can revise work after feedback. These thresholds should be calibrated during the pilot rather than presented as validated certification standards.

### Shared capstone rubric

| Dimension | Weight | Evidence |
|---|---:|---|
| Problem fit and professional usefulness | 15% | Clear user need, sensible scope, and comparison with a baseline |
| Quality and source traceability | 20% | Correct and usable outputs; supported claims and checked calculations where applicable |
| Evaluation and failure analysis | 20% | Representative cases, explicit criteria, reported failures, and honest limitations |
| Safety, privacy, rights, and oversight | 20% | Permitted data, appropriate review, risk controls, and disclosure |
| Reproducibility and usability | 15% | Operating instructions, examples, and successful handover |
| Cost, maintenance, and communication | 10% | Access requirements, measured or clearly estimated costs, ownership, and change plan |

**Safety-critical pass conditions:** no unauthorized sensitive data; no fabricated evidence presented as real; no unapproved consequential external action; clear human accountability for regulated or safety-critical work. Failures require remediation regardless of total score.

Course completion establishes demonstrated performance on course tasks, not regulatory approval, clinical validation, or a guarantee of safe deployment.

## 6. Tool strategy: Claude, Gemini, and alternatives

Teach durable concepts first and product interfaces second.

- Use Claude Pro and/or an appropriate paid Gemini offering as candidate practice environments, subject to availability and institutional requirements.
- Use the precise term **Claude Code accessed through Claude Pro**, rather than assuming "Claude Code Pro" is a separate product. Official plan documentation describes included Claude Code access subject to usage limits shared with other Claude use. Confirm current account eligibility and limits before the cohort starts.
- Claude Code is a development assistant, not the deployed application's hosting service or its end-user AI backend. A running application that calls a model needs its own approved API or service arrangement; do not use a personal Claude subscription login as an application backend.
- Learners need access to one suitable assistant, not necessarily subscriptions to both ecosystems. Use instructor demonstrations or anonymized sample outputs for comparisons where additional access is unavailable.
- Verify the exact subscription names, features, regional availability, limits, and terms before producing tool-specific lessons. No particular feature, unlimited access, or included media generation is assumed here.
- A consumer subscription does not imply included API credits, automation access, third-party services, or institutional approval for sensitive information.
- Do not assume an individual paid plan provides the contractual or administrative protections required for healthcare, confidential engineering, or other sensitive use.
- Additional image, audio, video, or automation tools may be needed. Prefer approved existing access and equivalent supplied exercises before requiring more purchases.
- Core graduation does not require paid API access. Actual external automation can be replaced by a sandbox, recorded example, or manually executed workflow with the same decision and failure-handling requirements.
- These substitutes meet learning requirements, but do not earn a "deployed to production" designation. A learner seeking that designation chooses an affordable real release, such as a licensed campaign asset or an approved low-risk workflow, and meets the release gates. Institutional or technical approval cannot be replaced by a classroom score.
- Optional extension API exercises use separately approved accounts, explicit spending limits, and synthetic or public data.
- Maintain a dated feature-and-access matrix for the teaching cohort. A product change should require a lab update, not a curriculum redesign.

**Resources to verify when preparing lessons:** official Claude support and developer documentation; official Gemini help and Gemini API documentation; applicable institutional privacy policies; profession-specific standards. Product-specific instructions and legal requirements need current verification before teaching.

## 7. Optional technical extension

**Purpose:** progress from professional user to beginner AI application builder. This is not a substitute for a full software-engineering or machine-learning degree.

**Entry:** completion of the core or equivalent demonstrated competencies. No prior programming is assumed. The pace may need extension for learners needing more programming practice.

**Effort:** 6-8 hours per week, 60-80 hours total. Local prerequisites are cumulative: each extension week builds on the previous week.

| Week | Concepts and outcomes | Practical deliverable and assessment |
|---|---|---|
| T1 | Python values, variables, conditions, loops, functions, and debugging; Claude Code installation, account selection, and scoped permissions | A small data-processing script; explain and fix a supplied defect, including checking AI-generated changes |
| T2 | Files, CSV, JSON, environments, packages, basic tests, and version control; planning, reviewing diffs, and using Claude Code on a small repository | A reproducible mini-project with a README and focused tests; explain changed code instead of accepting it blindly |
| T3 | HTTP, API requests, credentials, response schemas, timeouts, and errors | A minimal model API client that keeps secrets outside source code and surfaces failures |
| T4 | Structured outputs, schema validation, prompt templates, and repeatable evaluation | An extraction tool tested on normal, missing-field, and malformed-output cases |
| T5 | Embeddings, chunking, retrieval, metadata, and source-grounded generation | A small document assistant with citations and unsupported-question behavior |
| T6 | Tool calling, permissions, state, idempotency, and human approval | A sandboxed assistant that cannot perform an external write without approval |
| T7 | Evaluation datasets, regression checks, retrieval metrics, and prompt-injection defenses | A repeatable evaluation runner and a documented set of remaining failure modes |
| T8 | Simple interfaces, deployment, access control, secrets, logging, and cost monitoring; controlled Lovable-to-GitHub-to-Claude-Code handoff where selected | A staging deployment using non-sensitive data, access-isolation checks, and a rollback exercise; do not publicly expose an unfinished app |
| T9 | Small classical ML baseline; fine-tuning versus retrieval; adaptation and local-model constraints | A baseline experiment and an adaptation decision memo; training a large model is not required |
| T10 | Integration, release decisions, documentation, and maintenance | A working application, evaluation report, deployment or local-run guide, and demonstration |

**Extension assessment:** practical deliverables plus a final application assessed for correctness, error handling, evaluation, security boundaries, usability, and operating cost. Completion requires a reproducible application and no unresolved critical permission or secret-handling defect.

Further electives can cover mathematical foundations, statistical learning, deep-learning implementation, computer vision, speech, recommender systems, time series, reinforcement learning, robotics, distributed training, and MLOps. These are separate depth tracks, not material to compress into a beginner professional course.

## 8. Coverage map

| Area | Core coverage | Optional depth |
|---|---|---|
| AI history, terminology, capabilities, and limitations | Weeks 1-4 | Technical readings and research literacy |
| Classical machine learning and predictive systems | Weeks 2-3 | Baseline implementation in T9; later ML specialization |
| Neural networks, transformers, embeddings, and model families | Week 4, revisited in Weeks 8 and 15 | Architecture and mathematics electives |
| Prompting, context, structured tasks, and verification | Weeks 5-8 | API-based implementations in T3-T5 |
| Data quality, statistics, and visualization | Weeks 3 and 9-10 | Python and analytical depth |
| Images, speech, audio, video, and multimodal AI | Weeks 4 and 11-12 | Modality-specific technical electives |
| Retrieval and knowledge systems | Week 8 | Working implementation in T5 |
| APIs, MCP, connectors, workflows, and agents | Weeks 13-14 | T3 and T6 |
| Fine-tuning, local models, efficiency, and architecture selection | Week 15 | T9 and later adaptation electives |
| Evaluation, security, privacy, ethics, rights, and governance | Throughout; consolidated in Week 16 | T7-T8 and domain-specific review |
| Deployment, costs, monitoring, and maintenance | Conceptual core; studio and capstone handover | T8-T10 |
| Professional application and change management | Weeks 17-24 | Ongoing practice and organizational adoption |

## 9. Materials, piloting and maintenance

Maintain the following materials for each module:

1. A lesson plan with observable outcomes, prerequisite reminders, and time allocations.
2. Learner notes with plain-language explanations, diagrams, glossary, and references.
3. A guided demonstration with checked inputs, expected behavior, and fallback examples.
4. A laboratory pack with public or synthetic materials and accessibility alternatives.
5. An independent assignment, assessment rubric, and instructor answer guidance.
6. Domain adaptations, common misconceptions, and a technical deep-dive option.
7. A dated tool-access checklist and maintenance notes where product interfaces are involved.

**Recommended pilot sequence:** start with Weeks 1, 5, and 7 with representative beginners before delivering the full programme. These probe conceptual accessibility, practical task framing, and evidence verification. Measure task completion, misconception patterns, accessibility barriers, and actual study time, then revise the complete draft edition.

**All 24 weekly drafts are now available.** The original detailed [Week 1 - foundations](ai-week-01-foundations.md), [Week 5 - prompting](ai-week-05-prompting.md), and [Week 7 - verification](ai-week-07-verification.md) remain the priority pilot samples. Every weekly kit contains a six-hour plan, learner explanations, supplied practice material, a worked result, ordered lab steps, assessment and instructor answer guidance. The [instructor and pilot guide](ai-sample-lessons-pilot-guide.md) covers the entire programme and retains the original offline outputs, unfamiliar test card and detailed sample-pilot protocol. The optional ten-week technical pathway is an outline in this edition, not ten additional full teaching packs.

This draft is a design proposal. It has not yet been learner-tested, professionally accredited, or checked against a specific institution's policies.

## 10. Real-world project catalogue: from blank brief to release

### Selection principles

These are projects **using market products and learning from their interaction patterns**, not reproductions of proprietary source code, brands, datasets, or complete commercial platforms. A small app inspired by Lovable is not equivalent to rebuilding Lovable; a voice concierge is not equivalent to rebuilding ElevenLabs.

Higgsfield, Lovable, and ElevenLabs are user-requested anchors. Claude Code is the assisted development environment where a project needs code. n8n is an additional workflow option. Claude or Gemini can supply research and language-model capabilities through the appropriate interface or separately authorized API.

The shortlist is organized by capability and project fit, not asserted as a verified market-share or "number one" ranking. Creative suites, application builders, voice platforms, and automation tools do not share one meaningful leaderboard. For each cohort, compare current output quality, access, cost per accepted result, commercial rights, privacy, integration effort, and portability before final selection.

### P1 - Launch a real campaign: brief to published creative

**Audience:** content creators, artists, graphic designers, marketers, and small-business owners.

**Product stack:** Claude or Gemini for research and scripting; Higgsfield for image/video production; ElevenLabs for licensed narration; an approved editor and publishing channel. Optional Claude Code work adds a landing page or a media-asset tracker rather than making coding a prerequisite.

**Starting point:** a real consenting business, community organization, or creator has a narrow communication goal, approved facts, a brand brief, and permission to use the assets.

**End-to-end build:**

1. Interview the owner; define the audience, objective, baseline, message, and permitted claims.
2. Research source-backed facts and prepare a script, storyboard, shot list, and asset-rights register.
3. Generate and select visual candidates in Higgsfield; track prompts, settings, versions, rejected outputs, and spend.
4. Generate narration with a licensed voice and appropriate commercial permissions; correct pronunciation and timing. Use a person's cloned voice only with documented permission and platform-compliant verification.
5. Edit a 30-60 second main video, two short cutdowns, captions, and a thumbnail or cover.
6. Conduct factual, brand, accessibility, rights, and consent reviews; obtain owner approval.
7. Publish to one approved real channel, or launch a permitted landing page, with appropriate disclosure and analytics.
8. Observe results for seven days, correct a discovered issue where necessary, and hand over editable files and a repeatable production checklist.

**Definition of done:** the owner accepts the package; every material factual claim has a source; assets have recorded usage permissions; captions are reviewed; the approved release is accessible to its intended audience. Report actual engagement and limitations without promising sales or attributing improvement causally to AI.

**Production boundary:** commercial distribution requires the appropriate licenses for the actual generation dates, models, voices, references, music, and platform. An educational/free account is not automatically suitable.

**Schedule:** visual and audio components originate in Weeks 11-12; the integrated studio and capstone occupy Weeks 17-24, approximately 48 hours. Paid access may be necessary for a commercial release.

### P2 - Ship a small SaaS-style application

**Audience:** professionals wanting a usable internal tool or small digital product.

**Product stack:** Lovable for the first application; its supported backend or an approved database/authentication service; GitHub for source history; Claude Code for optional reviewed code changes and tests; an approved hosting environment.

**Example scope:** a content approval board or design-request tracker with two user roles, one main workflow, and an audit history. Exclude payments, clinical records, and multi-tenant enterprise complexity from the first release.

**End-to-end build:**

1. Interview two or three prospective users; write the smallest useful feature list and acceptance criteria.
2. Sketch screens, define records and roles, and specify who may read or change each record.
3. Build the first workflow in Lovable with synthetic records; add sign-in and persistent storage where required.
4. Connect the project to GitHub. For the builder route, clone it and use Claude Code to inspect structure, add focused tests, fix defects, and review dependencies.
5. Keep API keys server-side; validate requests and enforce access rules at the backend, not just by hiding buttons.
6. Deploy staging; test two ordinary accounts and one administrator; confirm cross-account access is denied where required.
7. Review release findings, configure an appropriate domain if needed, document backup/restore and rollback, and obtain owner approval.
8. Release to a small named pilot group, monitor errors and usage for seven days, handle one feedback cycle, and hand over the repository and operating guide.

**Definition of done:** the agreed main workflow works end to end; access-isolation tests pass; no unresolved critical security finding remains; secrets are absent from client code and repository; a rollback has been rehearsed; a real owner accepts support responsibility.

**Production boundary:** automated security scans and generated code are not substitutes for qualified review. A core learner may follow the no-code route with an approved reviewer; independent coded deployment belongs in the technical extension. Do not have Lovable and Claude Code edit the same branch concurrently.

**Schedule:** one narrowly scoped studio/capstone, approximately 48 hours, plus technical-extension time if needed. Hosting, backend, domain, and API services may have separate charges.

### P3 - Deploy a bounded voice concierge

**Audience:** service businesses, educators, creators, and administrative teams.

**Product stack:** ElevenLabs voice-agent capabilities; an approved knowledge source; a web interface or embedded widget where supported. Optional Claude Code work implements a secure integration or handoff endpoint.

**Example scope:** a disclosed AI assistant answering opening-hours, course-information, or service-policy questions. Start on the web; telephone integration is an optional later extension.

**End-to-end build:**

1. Define the allowed questions, prohibited topics, escalation path, supported languages, and recording policy.
2. Assemble approved answers and a source register; remove unnecessary personal information.
3. Choose a licensed voice and configure the assistant's scope, disclosure, uncertainty behavior, and human handoff.
4. Prototype conversations, including interruptions, unclear speech, silence, incorrect premises, and unsupported requests.
5. Integrate with a web experience; keep any service credentials server-side. Do not add scheduling or external writes until approval controls exist.
6. Evaluate at least 20 scripted scenarios, including at least five out-of-scope or escalation cases; record response time and task completion.
7. Release to an authorized limited audience with consent notices, spending controls, a kill switch, and a human contact option.
8. Review consented feedback and permitted logs for seven days; revise the knowledge source and operating instructions.

**Definition of done:** all predeclared escalation test cases escalate or decline as intended; factual answers remain within approved knowledge; voice and recording permissions are recorded; a human can disable the assistant promptly. Passing these tests does not establish zero future errors.

**Production boundary:** no emergency, diagnosis, legal-advice, or autonomous financial-action use. Do not silently record users or impersonate a real person.

**Schedule:** approximately 48 hours for the web-based version. Live telephone service, custom backend work, or additional languages can require a separate project.

### P4 - Release a source-grounded professional knowledge portal

**Audience:** engineers, healthcare educators, researchers, and organizational knowledge workers.

**Product stack:** approved document-grounded Claude/Gemini interfaces for the core route; a separately authorized model API, retrieval service, and small web application for the builder route. Lovable can supply an interface; Claude Code can implement and test the retrieval application.

**Example scope:** a portal answering questions from a small set of public engineering manuals, organizational policies, or public patient-education materials.

**End-to-end build:**

1. Define readers, document permissions, document owners, freshness requirements, and excluded questions.
2. Collect and clean a small versioned corpus; check extraction quality and retain source locations.
3. Prepare answerable, conflicting-source, outdated-source, and unsupported test questions before tuning.
4. Build a no-code knowledge workspace or coded retrieval application with visible source references.
5. Add unsupported-question behavior, access boundaries, and a correction/feedback path.
6. Evaluate at least 20 questions, including at least five unsupported or conflicting cases; check source support, not citation appearance alone.
7. Release to a named real audience only after corpus and application access are approved.
8. Replace one source document, rerun relevant tests, and hand over an update/deletion process.

**Definition of done:** consequential claims in accepted evaluation answers are supported by the referenced source; unsupported questions are clearly qualified or declined; readers can inspect source locations; source updates and access restrictions are tested.

**Production boundary:** a consumer workspace is not an approved sensitive-data environment by default. Healthcare examples are educational and non-clinical; technical answers do not replace qualified engineering review.

**Schedule:** reuse the Week 8 lab, then approximately 48 studio/capstone hours. The coded retrieval service requires technical-extension skills or qualified support.

### P5 - Put an approval-based operations workflow into service

**Audience:** content teams, administrative teams, small businesses, and engineering support functions.

**Product stack:** n8n or an approved equivalent, permitted email/forms/storage connectors, Claude or Gemini through an authorized integration, and optional Claude Code for narrowly scoped transformations or tests.

**Example scope:** an incoming request becomes a categorized draft response and a task record, with a human approving every external message.

**End-to-end build:**

1. Map the existing manual process, exception cases, owner, and current time per request.
2. Define input/output fields, minimum permissions, data retention, approval rules, and spending limits.
3. Build using synthetic requests; validate structured outputs before acting on them.
4. Add a review step showing the exact proposed recipient, content, and action.
5. Add deduplication, bounded retries, error notifications, and a manual fallback.
6. Test approval, rejection, missing fields, duplicate events, revoked access, provider failure, and malicious instructions inside an incoming request.
7. Activate for a limited real input source, retaining explicit approval for external writes.
8. Observe for seven days; compare effort and failure handling against the manual baseline; hand over credentials ownership and shutdown instructions.

**Definition of done:** rejection causes no external action; repeated events do not cause duplicate external actions; failures are visible; credentials have the narrowest practical access; a human can pause the workflow and finish work manually.

**Production boundary:** approval must be an enforced workflow control, not merely an instruction in a model prompt. Self-hosting introduces additional security, backup, patching, and uptime responsibilities.

**Schedule:** reuse Weeks 13-14, then approximately 48 studio/capstone hours. Choose managed or institution-approved infrastructure unless learners have suitable operations support.

### P6 - Integrated flagship: a creator's campaign delivery portal

**Audience:** advanced learners or a small supervised team seeking a portfolio project combining the requested tools.

**Product stack:** Lovable for the project portal; Higgsfield for visual media; ElevenLabs for narration; Claude Code for reviewed integrations and tests; an approved model API where the application needs language-model inference. n8n is optional, not another required dependency.

**Narrow initial scope:** one organization submits a brief, reviews one campaign's assets, requests a revision, and approves a final package. No public sign-up, marketplace, autonomous posting, or billing in the first version.

**End-to-end build:**

1. Define the client journey, two roles, acceptance criteria, data model, rights requirements, and budget.
2. Build the brief intake, project status, asset review, and approval screens.
3. Produce the campaign manually in the vendors' interfaces first; prove the creative workflow before writing integrations.
4. In the technical route, add one API integration at a time behind server-side endpoints. Store job identifiers, expose real status, and handle failed or canceled generations.
5. For asynchronous media work, validate callbacks where supported, deduplicate events, restrict upload access, and use bounded status polling where needed. Never fetch arbitrary user-supplied URLs from a server without appropriate network and content restrictions.
6. Test permissions, unsupported requests, cost limits, provider failure, duplicate events, asset deletion, and rollback.
7. Release to one consenting pilot client with approved commercial assets and named support ownership.
8. Complete a real review/revision cycle, monitor seven days, and hand over the portal, creative files, costs, and operational documentation.

**Definition of done:** the pilot client can submit a brief and approve the delivered package; generation status is truthful; failures are visible; permissions and spending controls pass the declared tests; assets and approvals are traceable.

**Production boundary:** consumer product credits do not imply API access or equivalent model availability. Do not claim that a manual vendor-interface step is an automated integration.

**Schedule:** allow the 10-week technical extension and a further 4-6 weeks at 6-8 hours per week for the integrated release, subject to pilot calibration. This replaces a simpler builder capstone; it is not an additional requirement for every learner. Core learners can complete a manually orchestrated version with an accurate description of its limits.

## 11. Shared scratch-to-production lifecycle and release gates

### Release states

| State | Meaning | Required evidence |
|---|---|---|
| Learning prototype | Demonstrates a concept using safe examples | Working demonstration and known limitations |
| Staging or supervised pilot | Used for controlled evaluation, not general deployment | Restricted audience, test results, reviewer, and rollback plan |
| Authorized production release | Used by its intended real audience for a real task | Owner approval, applicable release gates, operating responsibility, and evidence of real use |

"Production" describes intended real use, not scale. A small internal workflow can qualify; a publicly accessible but unreviewed demo does not qualify automatically. A media project qualifies through authorized publication and distribution rather than application-hosting checks.

### Common lifecycle

| Step | Evidence to retain |
|---|---|
| Discover | User interview, problem statement, baseline, and reason AI is appropriate |
| Scope | MVP boundaries, acceptance criteria, excluded uses, and risk assessment |
| Prepare | Approved accounts, sources, data, rights, access, and budget |
| Build | Versioned prompts, assets or source code, configuration notes, and working vertical slice |
| Evaluate | Representative cases, independent checks, failure results, and revisions |
| Release | Reviewer approval, release record, audience, required disclosures, and rollback or withdrawal method |
| Operate | Monitoring or publication review, incident contact, spending review, and correction process |
| Hand over | Owner, credentials transfer process, documentation, update schedule, and shutdown instructions |

### Mandatory gates, applied according to project type

- **Value:** predeclared task criteria are met and compared with a manual or simpler baseline. A negative result can still be a successful learning outcome.
- **Data and rights:** approved inputs, consent, applicable commercial licenses, retention/deletion rules, and appropriate output disclosures are documented.
- **Access and secrets:** software uses appropriate authentication and backend authorization; secret scanning and relevant cross-account tests pass; production credentials are not embedded in source or browser code.
- **Quality:** project-specific evaluation passes the agreed thresholds; all consequential claims or calculations in the released deliverable receive appropriate review. All capstones retain the earlier minimum evaluation requirements.
- **Failure handling:** provider outages, missing inputs, unsupported requests, approval rejection, and duplicate events have explicit behavior where applicable.
- **Cost:** an owner-approved ceiling, alert, and practical stop mechanism exist. If a provider lacks hard caps, limit requests at the application/workflow level and document residual billing risk.
- **Operations:** a named owner can correct, disable, withdraw, or roll back the release. Software projects rehearse rollback and backup restoration where persistent data is involved.
- **Review:** regulated or safety-sensitive use receives the required professional and institutional approval. An instructor cannot grant permissions they do not hold.
- **Observation:** retain at least seven days of appropriate post-release observation. Use permitted analytics, feedback, and privacy-conscious logs; do not retain raw personal conversations by default.

Seven days of observation is a learning milestone, not proof of long-term reliability. If release approval is unavailable, submit a clearly labeled prototype or staging project; never bypass the gate to obtain a course designation.

### Claude Code practice requirements for builder-route projects

1. Start from the approved brief and a scoped repository; record which account and billing mode are in use.
2. Ask for a plan and small changes; review commands and permission requests before execution.
3. Keep secrets and sensitive data outside prompts and source; treat repository content, retrieved documents, and tool outputs as untrusted.
4. Inspect diffs, run relevant tests, and explain the changes. Generated tests are useful but do not independently establish correctness.
5. Use source control checkpoints and separate staging from production; resolve tool-sync conflicts deliberately.
6. Require explicit human approval for deployment, destructive migrations, purchases, and external messages.
7. Keep a reproducible handover so the application can be maintained without relying on one conversation history.

## 12. Schedule, workload, and purchasing plan

### Integrating projects without overloading beginners

| Period | Project milestone | Relationship to existing workload |
|---|---|---|
| Weeks 1-4 | Identify a professional problem and learn data/safety boundaries | Small examples only; no extra project |
| Weeks 5-8 | Write briefs, verify claims, and test knowledge sources | Existing assignments become reusable project inputs |
| Weeks 9-12 | Prepare data, charts, visuals, scripts, or audio relevant to the selected route | Choose relevant artifacts; not every modality must appear in one project |
| Weeks 13-16 | Design integration, approvals, evaluation, and risks | Existing systems labs provide the project plan |
| Weeks 17-20 | Complete a vertical slice and controlled pilot | Approximately 24 existing studio hours |
| Weeks 21-24 | Independently evaluate, release if approved, observe, and hand over | Approximately 24 existing capstone hours |
| Optional T1-T10 | Build and test the coded route | Separate 60-80 hours; not hidden inside the core |

Plan an early Week 24 release where feasible so observation can begin after Week 23 checks; if approvals or the seven-day observation period exceed the teaching calendar, complete the release designation afterward rather than shortening the evidence requirement. Core academic assessment can still assess the honestly labeled state reached.

**Each learner completes one integrated main project, not all six.** Other products appear through demonstrations, small labs, or peer showcases. Select a smaller project when account setup, licensing, or unfamiliar programming would consume the project hours.

### Cost worksheet required before commitment

| Cost category | Record before starting |
|---|---|
| Assistant access | Claude Pro or alternative plan, current limits, renewal date, and account eligibility |
| Development usage | Whether Claude Code uses included subscription access, separately enabled additional usage, or API billing |
| Runtime model usage | Provider, approved API account, estimated requests/tokens, and spending controls; separate from development access |
| Media generation | Model, credits or billing units, duration/resolution, expected attempts, and commercial permissions |
| Voice usage | Generation or agent usage, consent requirements, permitted publishing, and any separate telephony cost |
| App builder and automation | Workspace plan, credits/executions, publishing features, collaborator access, and export limits |
| Infrastructure | Hosting, database, storage, bandwidth, domain, email, backups, and monitoring |
| Maintenance | Named payer/owner after the course, recurring renewals, deletion/export plan, and shutdown date if not continued |

Do not require every subscription. Choose the smallest stack for one project and use non-commercial teaching examples or supplied outputs where access is unavailable. Actual commercial publication must still meet the chosen provider's terms.

No fixed vendor prices are embedded here: they vary by date, region, account, model, and usage. Instructors must publish a dated minimum-cost route and an optional enhanced route before learners purchase anything.

## 13. Product evidence and update log

**Research date:** 17 November 2026. The references below were checked through search-indexed official documentation; direct page retrieval was unavailable during drafting. Reopen current official pages and applicable contractual terms before purchasing or releasing. This is a feasibility check, not a market-ranking study or legal review.

| Product | Evidence supporting the curriculum use | Official reference |
|---|---|---|
| Claude Code with Claude Pro | Plan documentation describes Claude Code access with usage limits; distinguish subscription use from separately billed API usage | [Use Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan), [Claude Code costs](https://code.claude.com/docs/en/costs) |
| Lovable | GitHub documentation describes code sync and local development; publishing documentation describes release controls and security checks | [GitHub integration](https://docs.lovable.dev/integrations/github), [Publishing](https://docs.lovable.dev/features/publish) |
| Higgsfield | API documentation describes authenticated asynchronous image/video requests, polling or webhooks, and duplicate-event handling | [API documentation](https://docs.higgsfield.ai/), [Webhooks](https://docs.higgsfield.ai/docs/how-to/webhooks) |
| ElevenLabs | Documentation covers voice APIs and agents; licensing guidance distinguishes commercial eligibility and excludes certain beta uses | [Documentation](https://elevenlabs.io/docs/overview/intro), [Commercial publishing guidance](https://help.elevenlabs.io/hc/en-us/articles/13313564601361-Can-I-publish-the-content-I-generate-on-the-platform) |
| n8n | Documentation describes human review before selected AI-agent tool executions, including approve/deny behavior | [Human-in-the-loop tool review](https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools) |

**Specific licensing warning:** ElevenLabs' indexed official guidance says free-plan content is not commercially licensed and beta services are excluded from commercial/production use under the cited guidance. A paid subscription does not remove third-party rights, consent, or other contractual obligations. Check the exact service and current terms.

For each cohort, assign an owner to recheck these sources, record plan/model changes, rerun a representative lab, update screenshots and budgets, and retire integrations that no longer meet privacy, cost, or reliability requirements.

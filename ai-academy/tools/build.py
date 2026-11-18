#!/usr/bin/env python3
"""Build the static academy and editable kits; private templates are required locally."""

import csv
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
from zipfile import ZIP_DEFLATED, ZipFile

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / ".build"
BRAND = Path(os.environ.get("AI_BRAND_DIR", ROOT.parent / "private-input")).resolve()
EDITION = "18 November 2026"


def load_data(filename):
    spec = importlib.util.spec_from_file_location(filename.stem, filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


course = load_data(ROOT / "content/course_data.py")
project_data = load_data(ROOT / "content/project_data.py")


def bullets(items):
    return "\n".join(f"- {item}" for item in items)


def md_table(headers, rows):
    def cell(value):
        return str(value).replace("|", r"\|").replace("\n", " ")
    return "\n".join([
        "| " + " | ".join(map(cell, headers)) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
        *("| " + " | ".join(map(cell, row)) + " |" for row in rows),
    ])


WEEK_BLOCKS = [
    ("Concepts", 60, "Read explanations, discuss a misconception and interpret the worked example."),
    ("Demonstration", 60, "Predict the result, inspect the supplied inputs, and compare with the worked answer."),
    ("Guided lab", 120, "Complete the ordered lab steps and retain intermediate evidence."),
    ("Independent work", 90, "Complete the deliverables, professional transfer and self-check."),
    ("Reflection and feedback", 30, "Review the evidence, remediate blockers and record one next step."),
]


def roadmap(item):
    if item["id"] == "blueprint":
        return [[f"W{week['week']:02d}", week["title"], 6,
                 "" if week["week"] == 1 else f"W{week['week']-1:02d}", "Learner / instructor",
                 "; ".join(week["deliverables"]), "Not started"] for week in course.LESSONS]
    if item["kind"] == "week":
        rows = []
        minute = 0
        for i, (name, duration, output) in enumerate(WEEK_BLOCKS, 1):
            rows.append([f"W{item['week']:02d}-{i}", name, duration / 60,
                         "" if i == 1 else f"W{item['week']:02d}-{i-1}",
                         "Learner / instructor", output, "Not started"])
            minute += duration
        assert minute == 360
        return rows
    names = ["Discover", "Scope", "Prepare", "Build", "Evaluate", "Release", "Observe", "Hand over"]
    weights = [0.08, 0.08, 0.12, 0.28, 0.18, 0.08, 0.10, 0.08]
    return [[f"{item['id']}-{i+1}", name, round(item["hours"] * weight, 2),
             "" if i == 0 else f"{item['id']}-{i}", "Owner / learner / reviewer",
             item["steps"][i] if len(item["steps"]) == 8 else item["summary"], "Not started"]
            for i, (name, weight) in enumerate(zip(names, weights))]


def weekly_markdown(item):
    number = item["week"]
    sample_names = {1: "ai-week-01-foundations.md", 5: "ai-week-05-prompting.md", 7: "ai-week-07-verification.md"}
    if number in sample_names:
        body = (ROOT / "content/samples" / sample_names[number]).read_text()
        body = body.replace("**Status:** pilot-ready draft, not learner-tested.",
                            "**Status:** teaching draft, not learner-tested. Part of the full 24-week edition.")
        return body + instructor_section(item)
    sections = [
        f"# Week {number} - {item['title']}",
        "**Status:** teaching draft, not learner-tested. Fictional data and worked examples are labelled throughout. No production service is deployed by completing this lesson.",
        f"**Time:** 6 hours (360 learning minutes), with breaks additional. **Prerequisites:** {'basic digital skills' if number == 1 else 'the earlier course phases; review unfamiliar terms with the instructor'}.",
        "**Materials:** this guide, the supplied workbook and diagram, a document editor or paper, and optionally an approved AI assistant. Do not buy a subscription for a lab without checking the dated cohort access plan.",
        "## Learning outcomes\n\n" + bullets(item["outcomes"]),
        "## Six-hour plan\n\n" + md_table(["Block", "Minutes", "Activity"], WEEK_BLOCKS),
        "## Start with a prediction\n\nBefore reading the worked solution, write what you expect to happen, what could be wrong, and what evidence you would need to trust the result. Keep the note for your final reflection.",
        "## Learner explanations\n\n" + "\n\n".join(f"### {name}\n\n{text}" for name, text in item["concepts"]),
        "## Glossary\n\n" + md_table(["Term", "Plain-language meaning"], item["glossary"]),
        "## Supplied practice material\n\n**All records and outcomes in this table are synthetic teaching examples, not observations about a real vendor, person or organisation.**\n\n" + md_table(item["headers"], item["rows"]),
        "## Worked example\n\n" + item["example"],
        "## Guided lab\n\n" + "\n".join(f"{i}. {step}" for i, step in enumerate(item["steps"], 1)),
        "## What to submit\n\n" + bullets(item["deliverables"]),
        "## Offline and access-limited route\n\nUse the supplied practice table and worked example rather than a live service. Complete the same reasoning, calculations, state traces or manual artifact. Ask a peer to challenge the result. Label the work **manual/simulated** and identify which live-tool, audio, integration, permissions or production behaviours have not been tested. Do not claim a simulated control was enforced by real software.",
        "## Professional transfer\n\nChoose your own professional context and write one safe adaptation: an engineering document review, a public health-education task, a campaign brief, or an art/design workflow. Name the authorised reviewer, permitted inputs and one task outside scope. Use invented data unless you have explicit permission; do not make a second full project this week.",
        "## Self-check\n\n" + "\n".join(f"{i}. {question}" for i, question in enumerate(item["questions"], 1)),
        "## Assessment\n\n" + md_table(["Dimension", "Maximum points"], [[d, 4] for d in item["rubric"]]) +
        "\n\nProvisional pass: **12/16** with no unresolved safety-critical issue. Score each dimension 0 (missing/unsafe), 1 (major gaps), 2 (partial), 3 (sound with minor omissions), or 4 (clear and evidenced). A learner may pass by honestly diagnosing a failed workflow; this is not production authorisation.",
        "## Safety and required remediation\n\n" + item["safety"] +
        "\n\nCorrect any unauthorised data use, fabricated evidence, hidden failure, unapproved consequential action or false claim of production testing before passing. Keep the actual release state explicit.",
        "## Reflection\n\nWhat changed after you checked the evidence? Which failure would matter most in your profession? What remains unassessed? Record one concrete improvement and one situation where you would stop.",
        reference_section(item),
        instructor_section(item),
    ]
    return "\n\n".join(sections) + "\n"


def reference_section(item):
    return "## Further reading and product checks\n\n" + (
        "\n".join(f"- [{course.REFERENCES[key][0]}]({course.REFERENCES[key][1]})" for key in item["refs"])
        or "Use the course blueprint and the approved project operating guide."
    ) + "\n\nThese are official starting points, not proof of current plan eligibility, prices or legal suitability. Recheck live pages, local policies and applicable terms before teaching or deployment. No market ranking is asserted."


def instructor_section(item):
    answers = "\n\n".join(f"**{i}. {q}**\n\n{a}" for i, (q, a) in enumerate(zip(item["questions"], item["answers"]), 1))
    return (
        "\n\n## Instructor companion and answer guidance\n\n"
        "Keep this section for feedback after the independent attempt. The separate instructor/pilot guide includes delivery preparation and assessment calibration.\n\n"
        f"**Expected worked result:** {item['example']}\n\n"
        + answers +
        "\n\n**Facilitation:** ask the learner to point to a source, calculation, state transition or artifact supporting their conclusion. Accept defensible alternatives with explicit assumptions. Do not reward confident wording without evidence.\n\n"
        "**Remediation:** identify the failed criterion, explain its consequence, provide a new small input, and reassess the relevant behaviour. Record what was actually observed; do not issue professional approval from a course score.\n"
    )


def project_markdown(item):
    route = [
        f"# Project kit - {item['title']}",
        "**Status:** instructional production plan and editable templates. This package does not claim that a live application, paid media generation or client deployment has been completed.",
        f"**Audience:** {item['audience']}\n\n**Stack:** {', '.join(item['stack'])}.\n\n**Schedule:** {item['schedule']}",
        "## Outcomes\n\n" + bullets(item["outcomes"]),
        "## Design rationale\n\n" + "\n\n".join(f"### {a}\n\n{b}" for a, b in item["concepts"]),
        "## Supplied fictional starting brief or data contract\n\n" + md_table(item["headers"], item["rows"]),
        "## Worked vertical slice\n\n" + item["example"],
        "## From scratch to production\n\n" + "\n\n".join(f"### {i}. {step.split(':', 1)[0]}\n\n{step.split(':', 1)[-1].strip()}" for i, step in enumerate(item["steps"], 1)),
        "## Architecture and responsibility boundaries\n\nThe supplied architecture.svg, architecture.pdf and editable architecture.excalidraw describe a **reference design, not an implemented service**.\n\n" +
        md_table(["Component", "Boundary", "Responsibility"], item["architecture"]),
        "## Screen or production design\n\n" + "\n\n".join("### " + name + "\n\n" + bullets(fields) for name, fields in item["design"]),
        "## Acceptance and failure tests\n\nRun every applicable test and retain evidence. A blank or unrun test is not a pass. Hold back at least four relevant cases during initial development; using one to fix the system makes it development data. Use new cases for later independent claims.\n\n" +
        md_table(["Case", "Input or condition", "Expected outcome"], item["tests"]),
        "## Release gates\n\n" + bullets([
            "Owner and intended real audience identified; exact release version approved.",
            "Required data, source, voice, likeness, reference and commercial-use permissions recorded.",
            "All applicable acceptance tests run with evidence; critical issues resolved.",
            "Backend access, secrets and action approvals tested where software is involved.",
            "Budget, alerts and a practical stop mechanism agreed; provider billing limits documented.",
            "Rollback, withdrawal, source correction and manual fallback rehearsed as relevant.",
            "Seven days of appropriate post-release observation and one feedback/review cycle recorded.",
            "A named owner accepts maintenance, costs, support and shutdown responsibility.",
        ]),
        "## Deliverables\n\n" + bullets(item["deliverables"]),
        "## Budget and procurement\n\nUse the Budget sheet to record current plan access, separate API/runtime charges, hosting/storage, media attempts, voice use and maintenance. All worksheet costs begin unpriced; none are vendor quotations. Include failed paid attempts in actual spend. Publish a dated cohort minimum-cost route before purchases.",
        "## Handover runbook\n\n" + md_table(["Section", "Required evidence"], [
            ["Start", "Permitted users, inputs, current version and operating steps"],
            ["Review", "Who checks facts/rights and approves exact actions or assets"],
            ["Failure", "Visible errors, bounded retry rules and manual completion route"],
            ["Correction", "How to report, pause, fix and communicate an error"],
            ["Maintain", "Sources, dependencies, service changes, renewal dates and owner"],
            ["Stop", "How to disable service or withdraw publication; retention/deletion duties"],
        ]),
        "## Access-limited educational route\n\nComplete the manual workflow, diagrams, paper prototype, sample outputs and test expectations. Mark live API, media, permission and deployment behaviours **not assessed**. This can meet academic reasoning outcomes but cannot earn a production-release designation.",
        "## Assessment\n\n" + md_table(["Dimension", "Maximum points"], [[r, 4] for r in item["rubric"]]) +
        "\n\nFor academic feedback use 0-4 per dimension: missing/unsafe, major gaps, partial, sound, or clear/evidenced. Provisional pass 12/16 requires remediation of every critical issue. Actual release requires the owner's separate approval and all applicable gates, regardless of score.",
        "## Boundaries\n\n" + item["safety"],
        reference_section(item),
        instructor_section(item),
    ]
    return "\n\n".join(route) + "\n"


def programme_items():
    blueprint = {
        "id": "blueprint", "kind": "programme", "title": "Curriculum blueprint",
        "summary": "The complete 24-week map, optional builder track, assessment model and six production-project routes.",
        "hours": 144,
        "outcomes": ["Understand the 144-hour core and optional extension.", "Map capability to evidence and professional use.",
                     "Choose one project without requiring every tool subscription.", "Separate academic completion from release authority."],
        "concepts": [
            ("Professional AI practice", "The core aims at capable professional use, evaluation and bounded workflow design, not expertise in every branch of AI or machine-learning research."),
            ("A project spine", "Earlier assignments become sources, prompts, tests and creative components for one studio/capstone. Do not add all six projects to the 144-hour core."),
            ("An honest draft", "All 24 weekly lesson drafts now exist. They still require instructor dry runs, current tool checks, accessibility review and real learner piloting."),
        ],
        "headers": ["Phase", "Weeks", "Focus"],
        "rows": [[p[0], p[1], p[2]] for p in course.PHASES],
        "example": "A designer can complete the shared foundations and a campaign route without learning Python. A builder can later take the optional technical extension. Both must verify claims, protect data and respect real release approvals.",
        "steps": ["Discover audience and outcomes", "Prepare instructors and safe access", "Teach foundations and evidence habits",
                  "Develop analysis/media/system skills", "Run one professional studio", "Evaluate an independent capstone",
                  "Pilot and revise the teaching material", "Maintain sources, tools and project ownership"],
        "deliverables": ["24 weekly teaching kits", "Six project reference kits", "Instructor/pilot guide",
                         "Programme roadmap and editable gradebook", "Static resource website"],
        "diagram": ["Understand / 1-4", "Direct / 5-8", "Create / 9-12", "Connect / 13-16", "Apply / 17-20", "Deliver / 21-24"],
        "questions": ["Does core graduation require coding?", "Must everyone buy all tools?", "Is the course professionally accredited?"],
        "answers": ["No. Coding and application development are separate optional depth.", "No. Choose a minimal approved stack and an equivalent offline route.", "No accreditation or regulated professional authority is claimed."],
        "safety": "Course scores do not authorise regulated, safety-critical or sensitive-data deployment.",
        "rubric": ["Coherent learning progression", "Observable evidence", "Access and workload fit", "Responsible production boundaries"],
        "refs": ["nist", "ml"],
    }
    guide = {
        "id": "instructor-guide", "kind": "programme", "title": "Instructor and pilot guide",
        "summary": "Prepare, teach, assess and pilot all 24 weeks with answer guidance and a consistent remediation process.",
        "hours": 6,
        "outcomes": ["Prepare each weekly session and fallback.", "Use consistent scoring without granting deployment authority.",
                     "Pilot with consent and minimum personal data.", "Record observed learning barriers and revise material."],
        "concepts": [
            ("Prepare the environment", "Dry-run the lab, inspect every supplied input, confirm allowed data and permissions, and make the offline route available before class. Check current product access and rights rather than relying on screenshots from a previous cohort."),
            ("Assess evidence", "Ask what source, calculation, artifact or test supports the answer. Use the same 0-4 anchors across ordinary lesson rubrics. The first three sample packs retain their more detailed specific checks."),
            ("Pilot rather than claim validation", "Use a small voluntary pilot to find confusing language, setup delays and workload problems. Record actual counts and context. Editorial review and file checks are not evidence of measured learning gains."),
        ],
        "headers": ["Signal", "Review trigger", "Action"],
        "rows": [["Comprehension", "Two learners misunderstand the same term", "Rewrite and retest"],
                 ["Setup", "Multiple learners lose over 20 minutes", "Simplify and strengthen offline route"],
                 ["Workload", "Median above seven hours", "Reduce duplication or split activities"],
                 ["Safety", "Unresolved harmful/unauthorised practice", "Remediate before passing"]],
        "example": "When a learner correctly labels the live service as untested but completes the reasoning offline, assess that reasoning fairly and record live execution as not yet assessed. Never silently equate simulation with implementation.",
        "steps": ["Confirm audience and access", "Dry-run material", "Teach with worked examples", "Observe practice",
                  "Score evidence", "Remediate blockers", "Collect consented pilot feedback", "Revise and maintain"],
        "deliverables": ["Delivery checklist", "Per-week answer guidance", "Observation and timing register",
                         "Remediation log", "Pilot findings and revision plan"],
        "diagram": ["Prepare", "Demonstrate", "Observe practice", "Assess evidence", "Remediate", "Pilot + revise"],
        "questions": ["Does an inaccessible page mean the learner failed?", "Should raw professional records be collected?", "Does an AI editorial check validate a course?"],
        "answers": ["No. Grade the accurately labelled alternative and record retrieval as unassessed.", "No. Use minimum consented learning data, not confidential workplace details.", "No. Instructor and real-learner testing remain necessary."],
        "safety": "Use learner codes rather than personal details. Do not collect credentials, sensitive case files or unnecessary conversation histories.",
        "rubric": ["Safe preparation", "Consistent evidence-based marking", "Fair access alternatives", "Documented pilot improvements"],
        "refs": ["nist", "wcag"],
    }
    return blueprint, guide


def guide_markdown(guide):
    intro = [
        "# Instructor and pilot guide - full 24-week edition",
        "**Status:** teaching draft. This guide expands the earlier three-lesson pilot to all 24 weeks. Instructor delivery and real-learner validation remain pending.",
        "## How to use the kits\n\nEach weekly kit contains an editable slide deck with speaker notes, a Word learner guide, reader PDF, slide handout PDF, Excel workbook, practice CSV, editable process diagram and a timed roadmap. Project kits add reference architectures, wireframes, failure tests and release/handover plans. All paid-service and deployment outcomes must be observed in the actual environment; the provided files do not claim those services have been operated.",
        "## Standard session rhythm\n\n" + md_table(["Block", "Minutes", "Action"], WEEK_BLOCKS),
        "## Shared scoring anchors\n\n" + md_table(["Points", "Meaning"], [[0, "Missing, unsupported or unsafe"], [1, "Major gaps"], [2, "Partial understanding"], [3, "Sound with minor omissions"], [4, "Clear and evidenced"]]),
        "## Programme grades versus lesson feedback\n\nOrdinary lesson rubrics use /16 for formative feedback with a provisional 12/16 pass. Programme grading uses four category scores: Weeks 1-8 at 20%, Weeks 9-16 at 25%, studio at 20%, capstone at 35%. Overall must be at least 70%, capstone at least 70%, and all critical safety conditions clear. The blueprint's six-dimension capstone rubric supplies the capstone category score. Do not apply a generic /16 project score as regulatory approval.",
        "## Workbook conventions\n\nInput cells are lightly highlighted. Scores start empty, tests start unrun and gates start Pending. Formula cells must not be overwritten. Mark 'N/A (justified)' only with a written reason and reviewer agreement. An empty evidence field cannot establish a test pass. Budget values are unpriced until the owner enters dated quotes or measurements.",
        "## Preparation and privacy\n\nDry-run sources and accounts, check product terms, permit manual alternatives, provide accessible documents and avoid collecting personal professional records. Name a local policy owner and obtain the necessary approvals. A consumer subscription or an attractive demo is not institutional authorisation.",
        "## Per-week delivery and answer guidance",
    ]
    for item in course.LESSONS:
        intro += [
            f"### Week {item['week']} - {item['title']}",
            f"**Expected result:** {item['example']}",
            "**Self-check key:**\n\n" + "\n".join(f"- {q} **{a}**" for q, a in zip(item["questions"], item["answers"])),
            "**Look for:** " + "; ".join(item["rubric"]) + ".",
            "**Required boundary:** " + item["safety"],
        ]
    intro += [
        "## Detailed pilot materials for the original samples",
        (ROOT / "content/pilot-guide.md").read_text(),
        "## Release of this teaching edition\n\nCheck each kit and its offline route in the intended environment before teaching. Use the observation workbook to record time, misunderstandings and corrections. Do not label the complete course validated merely because file generation and browser checks succeed.",
    ]
    return "\n\n".join(intro) + "\n"


def write_csv(path, headers, rows):
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        writer.writerows(rows)


def build():
    from graphics import prepare_brand, process_diagram, architecture_diagram, wireframe, course_poster
    from office import slide_deck, workbook, apply_document_template
    from website import render_site

    BUILD.mkdir(parents=True, exist_ok=True)
    for name in ("Khaled Hamad - Slide Master Template.potx", "Khaled Hamad - Document Template.docx"):
        if not (BRAND / name).is_file():
            raise FileNotFoundError(f"Required private template missing: {BRAND / name}")
    prepare_brand(ROOT, BRAND)
    blueprint, guide = programme_items()
    items = [*course.LESSONS, blueprint, guide, *project_data.PROJECTS]
    assert len(items) == 32 and [x["week"] for x in course.LESSONS] == list(range(1, 25))
    render_markdown = MarkdownIt("default", {"html": False})
    documents = []
    inventory = []
    for item in items:
        directory = ROOT / "kits" / item["id"]
        directory.mkdir(parents=True, exist_ok=True)
        if item["kind"] == "week":
            text = weekly_markdown(item)
        elif item["kind"] == "project":
            text = project_markdown(item)
        elif item["id"] == "blueprint":
            text = (ROOT / "content/blueprint.md").read_text()
        else:
            text = guide_markdown(item)
        text = text.rstrip() + "\n"
        (directory / "guide.md").write_text(text)
        item["body_html"] = render_markdown.render(text)
        item["roadmap"] = roadmap(item)
        write_csv(directory / "practice.csv", item["headers"], item["rows"])
        write_csv(directory / "roadmap.csv", ["ID", "Task", "Planned hours", "Depends on", "Owner", "Evidence / output", "Status"], item["roadmap"])
        process_diagram(item, directory)
        if item["kind"] == "project":
            architecture_diagram(item, directory)
            wireframe(item, directory)
            write_csv(directory / "acceptance-tests.csv", ["Case", "Input / condition", "Expected outcome", "Actual evidence", "Status"],
                      [row + ["", "Unrun"] for row in item["tests"]])
        slide_deck(item, directory, BRAND)
        workbook(item, directory, course.LESSONS, course.PHASES)
        documents.append({"id": item["id"], "title": item["title"], "source": str(directory / "guide.md"),
                          "output": str(directory / "guide.docx"), "kind": item["kind"]})
        print(f"Built {item['id']}: slides, workbook, diagrams, roadmap and guide source", flush=True)
    (BUILD / "documents.json").write_text(json.dumps(documents))
    subprocess.run(["node", str(ROOT / "tools/build-documents.cjs"), str(BUILD / "documents.json"), str(BRAND)], check=True)
    for job in documents:
        apply_document_template(Path(job["output"]), BRAND)
    course_poster(course.LESSONS, course.PHASES, ROOT / "assets")
    render_site(ROOT, items, course.PHASES, course.TECHNICAL_TRACK, EDITION)
    # PDF readers use the same rendered source as the website; slide PDFs share the slide scene.
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()
            for item in items:
                page.goto((ROOT / "pages" / f"{item['id']}.html").as_uri())
                page.wait_for_load_state("networkidle")
                page.locator("details.instructor").evaluate_all("(elements) => elements.forEach((element) => { element.open = true; })")
                page.evaluate("document.fonts.ready")
                page.pdf(path=str(ROOT / "kits" / item["id"] / "guide.pdf"), format="A4",
                         print_background=True, margin={"top": "16mm", "right": "16mm", "bottom": "18mm", "left": "16mm"},
                         display_header_footer=True, header_template="<span></span>",
                         footer_template='<div style="font:9px Arial;color:#3D4A63;width:100%;margin:0 16mm">AI from Zero to Professional Practice · Teaching draft<span style="float:right" class="pageNumber"></span></div>')
        finally:
            browser.close()
    for item in items:
        directory = ROOT / "kits" / item["id"]
        members = sorted(p for p in directory.iterdir() if p.is_file() and p.suffix != ".zip")
        for path in members:
            inventory.append({"kit": item["id"], "title": item["title"], "file": str(path.relative_to(ROOT)),
                              "bytes": path.stat().st_size, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        with ZipFile(directory / f"{item['id']}-kit.zip", "w", ZIP_DEFLATED) as z:
            for path in members:
                z.write(path, f"{item['id']}/{path.name}")
    write_csv(ROOT / "resource-inventory.csv", ["Kit", "Title", "File", "Bytes", "SHA256"],
              [[r["kit"], r["title"], r["file"], r["bytes"], r["sha256"]] for r in inventory])
    (ROOT / "resource-inventory.json").write_text(json.dumps(inventory, indent=2))
    public_items = [{k: v for k, v in i.items() if k != "body_html"} for i in items]
    (ROOT / "course-map.json").write_text(json.dumps({"edition": EDITION, "status": "Teaching drafts; not learner-validated",
                                                    "core_hours": 144, "items": public_items}, indent=2))
    downloads = ROOT / "downloads"
    downloads.mkdir(exist_ok=True)
    with ZipFile(downloads / "ai-academy-complete.zip", "w", ZIP_DEFLATED) as z:
        for path in sorted(ROOT.rglob("*")):
            relative = path.relative_to(ROOT)
            if not path.is_file() or relative.parts[0] in {".build", ".venv", "downloads", "tools", "content", "__pycache__"}:
                continue
            z.write(path, f"ai-academy/{relative.as_posix()}")
    print(f"Complete: {len(items)} editable kits; {len(inventory)} indexed files.", flush=True)


if __name__ == "__main__":
    build()

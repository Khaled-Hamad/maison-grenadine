"""Self-contained static pages: no account, tracking service, backend or external font request."""

from html import escape as e
from pathlib import Path
import re

BUNDLE = "https://github.com/Khaled-Hamad/maison-grenadine/raw/khaled-hamad-improved-waddle/ai-academy/downloads/ai-academy-complete.zip"


def header(prefix="", home=False):
    root = "index.html" if prefix else ""
    base = prefix + root
    return f"""
    <a class="skip" href="#main">Skip to content</a>
    <header class="site-header"><div class="container header-row">
      <a class="brand" href="{prefix}index.html" aria-label="Khaled Hamad AI programme home"><img src="{prefix}assets/logo-navy.png" width="216" alt="Khaled Hamad"></a>
      <span class="brand-divider" aria-hidden="true"></span><span class="brand-label">AI / PROFESSIONAL PRACTICE</span>
      <button class="menu-toggle" aria-expanded="false" aria-controls="primary-nav">Menu</button>
      <nav id="primary-nav" aria-label="Main navigation">
        <a href="{base}#curriculum">Course map</a><a href="{base}#projects">Projects</a>
        <a href="{base}#process">The process</a><a href="{base}#library">Library</a>
      </nav>
    </div></header>"""


def footer(prefix=""):
    return f"""
    <footer class="site-footer"><div class="container footer-grid">
      <div><img src="{prefix}assets/logo-gold.png" width="220" alt="Khaled Hamad"><p>Making AI work for people.</p></div>
      <div><p class="eyebrow on-dark">A PRACTICAL LEARNING SYSTEM</p><p>24 weeks. One professional project.<br>Evidence before confidence.</p></div>
      <div><p>Teaching drafts · 18 November 2026</p><p>Not accreditation, a market ranking or authorisation to deploy.<br>No learner accounts or server-side progress tracking.</p></div>
    </div></footer>"""


def document(title, body, prefix="", description=""):
    return f"""<!doctype html>
<html lang="en-GB" class="no-js"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{e(description or title, quote=True)}"><meta name="color-scheme" content="light">
<title>{e(title)} | AI in practice</title><link rel="stylesheet" href="{prefix}assets/site.css">
<script src="{prefix}assets/site.js" defer></script></head><body>{header(prefix)}{body}{footer(prefix)}</body></html>"""


def format_links(item, prefix="", compact=False):
    base = f"{prefix}kits/{item['id']}/"
    records = [("slides.pptx", "PowerPoint", "PPTX"), ("guide.docx", "Word guide", "DOCX"),
               ("workbook.xlsx", "Excel workbook", "XLSX"), ("guide.pdf", "Reader PDF", "PDF")]
    if not compact:
        records += [("slides.pdf", "Slide handout", "PDF"), ("process.svg", "Process diagram", "SVG"),
                    ("process.pdf", "Process print", "PDF"), ("process.excalidraw", "Editable diagram", "EXCALIDRAW"),
                    ("roadmap.csv", "Roadmap", "CSV"), ("practice.csv", "Practice data", "CSV"),
                    ("guide.md", "Source text", "MD")]
        if item["kind"] == "project":
            records += [("architecture.svg", "Reference architecture", "SVG"), ("architecture.pdf", "Architecture print", "PDF"),
                        ("architecture.excalidraw", "Editable architecture", "EXCALIDRAW"),
                        ("design.svg", "Screen / production design", "SVG"), ("design.pdf", "Design print", "PDF"),
                        ("acceptance-tests.csv", "Acceptance tests", "CSV")]
    return "".join(f'<a class="file-link" href="{base}{name}" download><span>{e(label)}</span><b>{kind}</b><span class="sr-only"> download</span></a>' for name, label, kind in records)


def lesson_card(item, phase):
    search = " ".join([item["id"], f"week {item['week']}", item["title"], item["summary"], *item["outcomes"]]).lower()
    return f"""<article class="lesson-card" data-lesson data-phase="{item['phase']}" data-search="{e(search, quote=True)}">
      <div class="card-top"><span class="week-number">{item['week']:02d}</span><span class="draft-label">Teaching draft</span></div>
      <h3><a href="pages/{item['id']}.html">{e(item['title'])}</a></h3><p>{e(item['summary'])}</p>
      <div class="card-bottom"><span>6 hours · PPTX / DOCX / XLSX</span><button class="review-button" data-review="{item['id']}" aria-pressed="false">Mark reviewed</button></div>
    </article>"""


def home_page(items, phases, technical, edition):
    weeks = [i for i in items if i["kind"] == "week"]
    projects = [i for i in items if i["kind"] == "project"]
    phase_links = "".join(
        f'<a class="journey-stop" href="#phase-{n}"><span>{n+1:02d}</span><div><strong>{e(p[0])}</strong><small>Weeks {p[1]}</small></div><b aria-hidden="true">↗</b></a>'
        for n, p in enumerate(phases))
    phase_options = "".join(f'<option value="{i}">{p[0]} · Weeks {p[1]}</option>' for i, p in enumerate(phases))
    course_map = ""
    for n, p in enumerate(phases):
        course_map += f'<section class="phase-group" id="phase-{n}" data-phase-group="{n}"><div class="phase-heading"><span class="phase-index">0{n+1}</span><div><p class="eyebrow">WEEKS {p[1]}</p><h3>{e(p[2])}</h3><p>{e(p[3])}</p></div></div><div class="lesson-grid">'
        course_map += "".join(lesson_card(i, p) for i in weeks if i["phase"] == n)
        course_map += "</div></section>"
    project_cards = ""
    for index, project in enumerate(projects):
        project_cards += f"""<article class="project-card"><div class="project-number">P{index+1:02d}</div>
        <div><p class="eyebrow">{"ADVANCED / OPTIONAL" if index == 5 else "PROFESSIONAL PROJECT"}</p>
        <h3><a href="pages/{project['id']}.html">{e(project['title'])}</a></h3><p>{e(project['summary'])}</p>
        <p class="tool-list">{e(" / ".join(project['stack']))}</p></div><a class="round-link" href="pages/{project['id']}.html" aria-label="Open {e(project['title'], quote=True)}">↗</a></article>"""
    library = ""
    for item in items:
        kind = {"week": "Lesson", "project": "Project", "programme": "Guide"}[item["kind"]]
        label = f"Week {item['week']:02d} / " if item["kind"] == "week" else ""
        library += f'<tr data-resource data-kind="{kind.lower()}" data-search="{e((label+item["title"]+" "+kind).lower(), quote=True)}"><th scope="row"><a href="pages/{item["id"]}.html">{e(label+item["title"])}</a><small>{kind} · teaching draft</small></th><td><div class="format-row">{format_links(item, compact=True)}</div></td><td><a class="text-link" href="kits/{item["id"]}/{item["id"]}-kit.zip" download>Kit ZIP<span class="sr-only"> for {e(item["title"])}</span> ↓</a></td></tr>'
    technical_rows = "".join(f"<tr><th scope=\"row\">{e(code)}</th><td>{e(title)}</td><td>{e(summary)}</td></tr>" for code, title, summary in technical)
    body = f"""
    <main id="main" tabindex="-1">
      <section class="hero container"><div class="hero-copy"><p class="eyebrow">THE PROFESSIONAL AI PROGRAMME</p>
        <h1>From first prompt<br>to <span>professional<br>practice.</span></h1>
        <p class="hero-lead">Understand the technology. Make useful things.<br>Know what to check before you trust them.</p>
        <p class="hero-note">For engineers, healthcare professionals, creators, artists and designers. No programming prerequisite.</p>
        <div class="actions"><a class="button primary" href="#curriculum">Explore the course <span aria-hidden="true">↗</span></a><a class="button secondary" href="{BUNDLE}">Download the full kit ↓</a></div>
        <p class="download-note">Editable Office files, diagrams and the offline website. Full ZIP download needs a connection.</p>
      </div><aside class="journey-panel" aria-label="Six-stage learning journey"><p class="eyebrow on-dark">YOUR LEARNING JOURNEY</p>{phase_links}<p class="panel-note">One shared foundation.<br>Your own professional destination.</p></aside></section>
      <div class="stats-band"><div class="container stats-grid"><div><strong>24</strong><span>weekly lesson kits</span></div><div><strong>144</strong><span>planned core hours</span></div><div><strong>06</strong><span>project routes — choose one</span></div><div><strong>32</strong><span>editable resource kits</span></div></div></div>
      <section class="container section" id="curriculum"><div class="section-heading"><div><p class="eyebrow">01 / THE COURSE MAP</p><h2>A clear path.<br><span>Not a collection of tricks.</span></h2></div><p>Build understanding before automation. Each week pairs an explanation with supplied practice data, a worked example, an assessment and a professional application.</p></div>
        <div class="notice"><strong>Drafts, not a finished certification.</strong> All 24 weekly packs are available. Instructor dry runs, live-tool checks and real learner piloting remain required. Academic scores never replace professional or release approval.</div>
        <form class="filters" role="search" onsubmit="return false"><div class="search-field"><label for="course-search">Find a topic or week</label><input id="course-search" type="search" placeholder="Try retrieval, uncertainty or Week 12" autocomplete="off"></div><div><label for="phase-filter">Learning stage</label><select id="phase-filter"><option value="all">All six stages</option>{phase_options}</select></div><button class="button secondary" type="reset" id="reset-course">Reset filters</button></form>
        <div class="map-status"><p id="filter-count" role="status">24 lessons shown</p><p><strong id="review-count">0 / 24</strong> marked reviewed on this browser</p></div>
        <p class="storage-notice" id="storage-notice" role="status"></p>
        <div id="course-map">{course_map}</div><p id="no-lessons" class="empty-state" hidden>No matching lessons. Change the search or reset the filters.</p>
        <div class="progress-actions"><button class="button secondary" id="export-progress">Export review checklist</button><button class="plain-button" id="reset-progress">Reset this browser’s review marks</button><p>Self-reported reading progress only. Not a grade, certificate or deployment approval.</p></div>
      </section>
      <section class="projects-section" id="projects"><div class="container"><div class="section-heading"><div><p class="eyebrow">02 / BUILD SOMETHING USEFUL</p><h2>Six routes.<br><span>One real-world standard.</span></h2></div><p>Start with a human need. End with evidence, an approved release where feasible, and a handover someone else can use. These are project instruction kits—not claims that the services have been deployed.</p></div><div class="project-list">{project_cards}</div><p class="project-footnote">The integrated portal is an advanced optional route with separate technical prerequisites and additional time. Do not add all six builds to the 144-hour core.</p></div></section>
      <section class="container section" id="process"><div class="section-heading"><div><p class="eyebrow">03 / HOW THE WORK MOVES</p><h2>From a blank brief<br><span>to accountable delivery.</span></h2></div><p>Use the same evidence trail across media, applications and workflows. A production release requires real permission, real use and a named operating owner.</p></div>
        <ol class="lifecycle"><li><b>01</b><h3>Discover & scope</h3><p>User, baseline, constraints and permission.</p></li><li><b>02</b><h3>Prepare & build</h3><p>Sources, rights, versions and a narrow working path.</p></li><li><b>03</b><h3>Evaluate & approve</h3><p>Representative cases, visible failures and release gates.</p></li><li><b>04</b><h3>Operate & hand over</h3><p>Seven-day observation, corrections, costs and ownership.</p></li></ol>
        <div class="guide-grid"><a class="guide-tile" href="pages/blueprint.html"><span>PROGRAMME DESIGN ↗</span><h3>Read the complete blueprint</h3><p>Outcomes, workload, assessment, tool access and production boundaries.</p></a><a class="guide-tile dark-tile" href="pages/instructor-guide.html"><span>TEACHING & PILOTING ↗</span><h3>Run the programme responsibly</h3><p>Session preparation, answers, scoring, offline alternatives and pilot feedback.</p></a></div>
        <details class="extension"><summary>Optional builder pathway · 10-week outline</summary><p>A separately scoped 60-80 hours for Python, APIs and AI application development. This edition includes the pathway outline, not ten additional full teaching packs.</p><div class="table-wrap"><table><thead><tr><th>Week</th><th>Focus</th><th>Scope</th></tr></thead><tbody>{technical_rows}</tbody></table></div></details>
      </section>
      <section class="library-section" id="library"><div class="container"><div class="section-heading"><div><p class="eyebrow">04 / YOUR RESOURCE LIBRARY</p><h2>Editable by design.<br><span>Useful beyond the classroom.</span></h2></div><p>PowerPoint with speaker notes. Word guides. Excel practice and planning. Reader PDFs, editable diagrams, designs and roadmaps. Each kit keeps its source and limitations.</p></div>
        <div class="library-top"><div><label for="library-search">Search resources</label><input id="library-search" type="search" placeholder="Lesson, project or guide"></div><div><label for="kind-filter">Resource type</label><select id="kind-filter"><option value="all">All kits</option><option value="lesson">Lessons</option><option value="project">Projects</option><option value="guide">Guides</option></select></div><a class="button primary" href="{BUNDLE}">Complete bundle ↓</a></div>
        <p id="resource-count" role="status">32 kits shown</p><div class="table-wrap resource-table" tabindex="0" role="region" aria-label="Downloadable resource kits"><table><thead><tr><th>Resource</th><th>Office files and reader</th><th>All formats</th></tr></thead><tbody>{library}</tbody></table></div>
        <p id="no-resources" class="empty-state" hidden>No matching resources. Clear the resource search or change the type.</p>
        <div class="library-extras"><a href="assets/course-map.pdf" download>Course map poster · PDF ↓</a><a href="assets/course-map.png" download>Course map image · PNG ↓</a><a href="resource-inventory.csv" download>File inventory + checksums · CSV ↓</a><a href="course-map.json" download>Structured course map · JSON ↓</a></div>
        <p class="small-note">Original brand archives and original templates are not included. Product references are capability-based, not a verified popularity ranking. Confirm current access, prices and commercial terms before using vendor services.</p>
      </div></section>
    </main>"""
    return document("AI from zero to professional practice", body, description="A complete 24-week AI curriculum with editable lessons, six project routes, diagrams, roadmaps and a download library.")


def prepare_reading(html):
    html = re.sub(r"<h1>.*?</h1>", "", html, count=1, flags=re.S)
    html = re.sub(r"<h1>(.*?)</h1>", r"<h2>\1</h2>", html, flags=re.S)
    mappings = {
        "ai-curriculum-blueprint.md": "blueprint.html",
        "ai-sample-lessons-pilot-guide.md": "instructor-guide.html",
        "ai-week-01-foundations.md": "week-01.html",
        "ai-week-05-prompting.md": "week-05.html",
        "ai-week-07-verification.md": "week-07.html",
    }
    for before, after in mappings.items():
        html = html.replace(f'href="{before}"', f'href="{after}"')
    toc = []
    seen = set()

    def heading(match):
        level, title = match.group(1), match.group(2)
        plain = re.sub("<[^>]+>", "", title)
        identity = re.sub("[^a-z0-9]+", "-", plain.lower()).strip("-")
        base, index = identity, 2
        while identity in seen:
            identity, index = f"{base}-{index}", index+1
        seen.add(identity)
        if level == "2":
            toc.append((identity, plain))
        return f'<h{level} id="{identity}">{title}</h{level}>'
    html = re.sub(r"<h([23])>(.*?)</h\1>", heading, html, flags=re.S)
    html = html.replace("<table>", '<div class="table-wrap" tabindex="0" role="region" aria-label="Scrollable teaching data"><table>').replace("</table>", "</table></div>")
    marker = re.search(r'<h2 id="[^"]+">Instructor companion and answer guidance</h2>', html)
    if marker:
        html = html[:marker.start()] + '<details class="instructor"><summary>Instructor answer guidance</summary>' + html[marker.start():] + "</details>"
    return html, toc


def detail_page(item, items):
    reading, toc = prepare_reading(item["body_html"])
    toc_html = "".join(f'<li><a href="#{identity}">{e(label)}</a></li>' for identity, label in toc)
    label = f"Week {item['week']:02d}" if item["kind"] == "week" else "Project kit" if item["kind"] == "project" else "Programme guide"
    review = f'<button class="review-button large-review" data-review="{item["id"]}" aria-pressed="false">Mark reviewed</button>' if item["kind"] == "week" else ""
    diagram = "architecture.svg" if item["kind"] == "project" else "process.svg"
    diagram_title = "Reference architecture — not a deployed service" if item["kind"] == "project" else "Concept and process map"
    adjacent = ""
    if item["kind"] == "week":
        n = item["week"]
        if n > 1:
            adjacent += f'<a href="week-{n-1:02d}.html">← Week {n-1:02d}</a>'
        adjacent += '<a href="../index.html#curriculum">Back to the course map</a>'
        if n < 24:
            adjacent += f'<a href="week-{n+1:02d}.html">Week {n+1:02d} →</a>'
    else:
        adjacent = '<a href="../index.html#library">← Back to the resource library</a>'
    body = f"""
    <main id="main" tabindex="-1" class="detail-main container">
      <nav class="breadcrumbs" aria-label="Breadcrumb"><a href="../index.html">Programme</a><span aria-hidden="true">/</span><span>{e(label)}</span></nav>
      <div class="print-brand"><img src="../assets/logo-navy.png" width="210" alt="Khaled Hamad"></div>
      <section class="detail-hero"><p class="eyebrow">{e(label.upper())} / TEACHING DRAFT</p><h1>{e(item["title"])}</h1><p class="hero-lead">{e(item["summary"])}</p><div class="actions"><a class="button primary" href="../kits/{item['id']}/{item['id']}-kit.zip" download>Download the complete kit ↓</a>{review}<button class="button secondary print-button" type="button">Print / save page as PDF</button></div><p id="storage-notice" class="storage-notice" role="status"></p></section>
      <div class="detail-layout"><article class="reading">{reading}</article><aside class="resource-rail"><section><p class="eyebrow">EDITABLE RESOURCES</p><h2>Take the kit with you.</h2><div class="file-list">{format_links(item, "../")}</div><p class="small-note">Actual paid-service access, licensing and release approval are not included.</p></section><nav aria-label="On this page" class="on-this-page"><h2>On this page</h2><ol>{toc_html}</ol></nav></aside></div>
      <section class="diagram-section"><p class="eyebrow">VISUAL REFERENCE</p><h2>{diagram_title}</h2><a href="../kits/{item['id']}/{diagram}"><img src="../kits/{item['id']}/{diagram}" alt="{e(diagram_title + ': ' + item['title'], quote=True)}" loading="lazy"></a><p class="small-note">Open at full size or download the editable diagram. Responsibilities and limits are described in the guide.</p></section>
      <nav class="adjacent" aria-label="Continue learning">{adjacent}</nav>
    </main>"""
    return document(item["title"], body, "../", item["summary"])


def render_site(root, items, phases, technical, edition):
    (root / "pages").mkdir(exist_ok=True)
    (root / "index.html").write_text(home_page(items, phases, technical, edition))
    for item in items:
        (root / "pages" / f"{item['id']}.html").write_text(detail_page(item, items))

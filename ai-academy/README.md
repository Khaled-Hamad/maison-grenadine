# AI from Zero to Professional Practice

**Full-course teaching draft · 18 November 2026**

24 weekly kits, the curriculum blueprint, an instructor/pilot guide and six end-to-end project kits: **32 kits**. The core is 144 planned hours. Each learner chooses one main project; the six routes are alternatives, not six compulsory builds.

## Open the programme

Extract the complete download, keep its folders together and open **`ai-academy/index.html`**. The course map, all lesson pages, individual files and per-kit ZIPs work locally without an account or paid service. The full-bundle GitHub link needs an internet connection.

The website can also be served as an ordinary static folder. For example, from a repository checkout:

```bash
python -m http.server 8000 --bind 127.0.0.1 --directory ai-academy
```

Open `http://127.0.0.1:8000`. This is a local preview, not a public deployment. The existing restaurant homepage is unchanged.

Review marks are self-reported browser-local reading records, not grades. Browsers can isolate storage per page in direct-file mode; use the course map to mark/export the checklist, or serve the folder locally for shared marks. There are no learner accounts, analytics trackers or runtime API keys.

## What is in each kit

| File | Purpose |
|---|---|
| `slides.pptx` | Editable branded slides with speaker notes |
| `guide.docx` | Editable learner/instructor text with the supplied document header |
| `workbook.xlsx` | Practice data, lab log, rubric, safety gates, risks, budget, roadmap and answer guidance |
| `guide.pdf` | Print-friendly reader, including instructor answer guidance |
| `slides.pdf` | Slide-content handout |
| `process.svg`, `.png`, `.pdf`, `.excalidraw` | Process/concept design, including editable diagram source |
| `practice.csv`, `roadmap.csv`, `guide.md` | Portable practice data, planning and editable source text |
| `<kit-id>-kit.zip` | All formats for that kit |

Project kits additionally contain reference architectures, low-fidelity screen/production designs and acceptance-test CSVs. The blueprint workbook includes the 24-week schedule, programme gradebook and six-dimension capstone rubric. Weeks 21-24 include that capstone rubric too.

**Examples are synthetic.** Costs start unpriced, scores start blank, tests start unrun and safety gates start Pending. In the Budget sheet enter Units, Unit price and Fixed explicitly, including justified zeros. A percentage, completed checklist or course score cannot authorise a real release.

## Teaching and project boundaries

Begin with the blueprint and instructor guide. Pilot Weeks 1, 5 and 7 before delivering a full cohort; instructor dry runs, live-tool checks, accessibility review and real learner validation remain necessary.

The ten-week optional builder pathway is a **separate 60-80-hour outline**, not ten additional full teaching packs. The advanced integrated portal requires that extension or equivalent skills, plus separately planned build time.

The six project kits are actionable instructional plans and editable working materials—not six implemented services or media already generated in paid tools. Learners must run their selected tools, obtain permissions, collect actual evaluation evidence and secure owner/professional approval before claiming production.

Claude Code accessed through Claude Pro is development access, not hosting or included runtime API billing. Check current service eligibility, prices, commercial rights and local policies; the shortlist is not a verified market ranking.

## Brand and rendering

The supplied Khaled Hamad slide master and document header provide the brand basis. Original brand ZIPs, original Office templates and private input files are **not distributed**. Derived logo artwork is used without retyping, stretching or recolouring.

Office files specify Segoe UI/Segoe UI Semibold. A viewer may substitute fonts if these are unavailable. Raster diagrams and slide-content PDFs use Liberation Sans as a compatible local fallback. Reader PDFs are browser-rendered; slide PDFs share the authored slide content and geometry. Neither is represented as a pixel-exact Microsoft Office export.

## Rebuild from source

Rebuilding requires a **repository checkout**, not just the offline bundle. Source is under `ai-academy/content/` and generators under `ai-academy/tools/`.

Place the two original files below in the ignored root `private-input/` folder, or set `AI_BRAND_DIR` to their private directory:

- `Khaled Hamad - Slide Master Template.potx`
- `Khaled Hamad - Document Template.docx`

With Python 3.12+, Node.js and `uv`:

```bash
uv venv ai-academy/.venv
uv pip install --python ai-academy/.venv/bin/python -r ai-academy/tools/requirements.txt
npm ci --prefix ai-academy/tools
ai-academy/.venv/bin/python -m playwright install chromium
ai-academy/.venv/bin/python ai-academy/tools/build.py
ai-academy/.venv/bin/python ai-academy/tools/test_release.py
```

Linux graphics generation expects Liberation Sans under `/usr/share/fonts/truetype/liberation/`. The builder fails explicitly when required templates/fonts are missing. It never silently substitutes a generic brand.

Outputs are deterministic in content, not byte-for-byte Office/PDF metadata. The generated resource inventories contain the current file sizes and SHA-256 checksums. The full ZIP preserves local website links and includes the per-kit ZIPs.

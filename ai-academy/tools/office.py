"""Editable PowerPoint and Excel, with PDF slide handouts from the same slide content."""

from copy import deepcopy
from io import BytesIO
from pathlib import Path
import posixpath
import textwrap
from lxml import etree as ET
from zipfile import ZIP_DEFLATED, ZipFile

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import MSO_ANCHOR
from pptx.util import Inches, Pt
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import simpleSplit
import xlsxwriter

from graphics import NAVY, GOLD, DEEP_GOLD, MIST, STEEL, LINE


def rgb(value):
    return RGBColor.from_string(value.lstrip("#"))


def template_presentation(brand):
    source = brand / "Khaled Hamad - Slide Master Template.potx"
    memory = BytesIO()
    with ZipFile(source) as incoming, ZipFile(memory, "w", ZIP_DEFLATED) as outgoing:
        for info in incoming.infolist():
            data = incoming.read(info.filename)
            if info.filename == "[Content_Types].xml":
                data = data.replace(b"application/vnd.openxmlformats-officedocument.presentationml.template.main+xml",
                                    b"application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml")
            elif info.filename == "_rels/.rels":
                relationships = ET.fromstring(data)
                for relation in list(relationships):
                    if relation.get("Type").rsplit("/", 1)[-1] in {"classificationlabels", "custom-properties", "thumbnail"}:
                        relationships.remove(relation)
                data = ET.tostring(relationships, encoding="utf-8", xml_declaration=True)
            outgoing.writestr(info, data)
    memory.seek(0)
    prs = Presentation(memory)
    for slide_id in list(prs.slides._sldIdLst):
        prs.part.drop_rel(slide_id.rId)
        prs.slides._sldIdLst.remove(slide_id)
    kept = {layout.name: layout for layout in prs.slide_layouts if layout.name in {"01 Cover", "49 Blank"}}
    if set(kept) != {"01 Cover", "49 Blank"}:
        raise ValueError("The provided branded layouts were not found.")
    for layout in kept.values():
        for shape in list(layout.shapes):
            props = shape._element.find(".//{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr")
            keep = props is not None and props.get("descr") == "Khaled Hamad logo"
            if not keep:
                layout.shapes._spTree.remove(shape._element)
        used = {value for node in layout._element.iter() for key, value in node.attrib.items()
                if key.startswith("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}")}
        for relation in list(layout.part.rels.values()):
            if relation.reltype.endswith("/image") and relation.rId not in used:
                layout.part.drop_rel(relation.rId)
    for master in prs.slide_masters:
        for shape in list(master.shapes):
            master.shapes._spTree.remove(shape._element)
        identifiers = master._element.sldLayoutIdLst
        for identity in list(identifiers):
            part = master.part.rels[identity.rId].target_part
            if part not in {layout.part for layout in kept.values()}:
                master.part.drop_rel(identity.rId)
                identifiers.remove(identity)
    prs.core_properties.title = "AI from Zero to Professional Practice"
    prs.core_properties.author = "Khaled Hamad"
    prs.core_properties.subject = "Teaching draft; not learner-validated or deployment authorisation"
    prs.core_properties.last_modified_by = "Khaled Hamad"
    prs.core_properties.category = "Education"
    prs.core_properties.comments = "New curriculum content; supplied brand design only."
    prs.core_properties.keywords = "AI, professional practice, teaching draft"
    prs.core_properties.identifier = ""
    prs.core_properties.language = "en-GB"
    return prs, kept


def apply_document_template(path, brand):
    """Retain the actual supplied header and page geometry without copying sample body content."""
    w = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
    r = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    rel = "http://schemas.openxmlformats.org/package/2006/relationships"
    ct = "http://schemas.openxmlformats.org/package/2006/content-types"
    with ZipFile(brand / "Khaled Hamad - Document Template.docx") as source, ZipFile(path) as generated:
        parts = {name: generated.read(name) for name in generated.namelist()}
        document = ET.fromstring(parts["word/document.xml"])
        relationships = ET.fromstring(parts["word/_rels/document.xml.rels"])
        content_types = ET.fromstring(parts["[Content_Types].xml"])
        template_doc = ET.fromstring(source.read("word/document.xml"))
        template_section = template_doc.find(f".//{{{w}}}sectPr")
        for section in document.findall(f".//{{{w}}}sectPr"):
            for tag in ["pgSz", "pgMar"]:
                old = section.find(f"{{{w}}}{tag}")
                if old is not None:
                    section.remove(old)
            for reference in list(section.findall(f"{{{w}}}headerReference")):
                section.remove(reference)
            section.insert(0, ET.Element(f"{{{w}}}headerReference", {f"{{{w}}}type": "default", f"{{{r}}}id": "rIdBrandHeader"}))
            prefix_tags = {"headerReference", "footerReference", "footnotePr", "endnotePr", "type"}
            index = next((i for i, child in enumerate(section) if ET.QName(child).localname not in prefix_tags), len(section))
            for tag in ["pgSz", "pgMar"]:
                original = template_section.find(f"{{{w}}}{tag}")
                if original is not None:
                    section.insert(index, deepcopy(original))
                    index += 1
        source_rels = ET.fromstring(source.read("word/_rels/document.xml.rels"))
        header_reference = template_section.find(f"{{{w}}}headerReference")
        header_rel = next(x for x in source_rels if x.get("Id") == header_reference.get(f"{{{r}}}id"))
        header_path = posixpath.normpath(posixpath.join("word", header_rel.get("Target")))
        parts["word/brandHeader.xml"] = source.read(header_path)
        header_rels_path = posixpath.join(posixpath.dirname(header_path), "_rels", posixpath.basename(header_path) + ".rels")
        if header_rels_path in source.namelist():
            header_rels = ET.fromstring(source.read(header_rels_path))
            for index, relationship in enumerate(header_rels):
                if relationship.get("TargetMode") == "External":
                    continue
                original_path = posixpath.normpath(posixpath.join(posixpath.dirname(header_path), relationship.get("Target")))
                suffix = Path(original_path).suffix
                new_path = f"word/media/brand-header-{index}{suffix}"
                parts[new_path] = source.read(original_path)
                relationship.set("Target", new_path.removeprefix("word/"))
                if not any(x.get("Extension") == suffix.lstrip(".") for x in content_types):
                    source_types = ET.fromstring(source.read("[Content_Types].xml"))
                    original_type = next((x for x in source_types if x.get("Extension") == suffix.lstrip(".")), None)
                    if original_type is None:
                        raise ValueError(f"Unknown header media content type: {suffix}")
                    content_types.append(deepcopy(original_type))
            parts["word/_rels/brandHeader.xml.rels"] = ET.tostring(header_rels, encoding="utf-8", xml_declaration=True)
        relationships.append(ET.Element(f"{{{rel}}}Relationship", {"Id": "rIdBrandHeader", "Type": f"{r}/header", "Target": "brandHeader.xml"}))
        content_types.append(ET.Element(f"{{{ct}}}Override", {"PartName": "/word/brandHeader.xml", "ContentType": "application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"}))
        parts["word/document.xml"] = ET.tostring(document, encoding="utf-8", xml_declaration=True)
        parts["word/_rels/document.xml.rels"] = ET.tostring(relationships, encoding="utf-8", xml_declaration=True)
        parts["[Content_Types].xml"] = ET.tostring(content_types, encoding="utf-8", xml_declaration=True)
    with ZipFile(path, "w", ZIP_DEFLATED) as result:
        for name, data in parts.items():
            result.writestr(name, data)


class Deck:
    def __init__(self, item, directory, brand):
        self.item, self.directory = item, directory
        self.prs, self.layouts = template_presentation(brand)
        self.prs.core_properties.title = item["title"]
        self.pdf = canvas.Canvas(str(directory / "slides.pdf"), pagesize=(960, 540))
        self.pdf.setTitle(item["title"] + " - slide handout")
        self.number = 0
        self.slide = None
        self.dark = False

    def text(self, text, x, y, w, h, size=18, bold=False, colour=None):
        colour = colour or ("#FFFFFF" if self.dark else NAVY)
        shape = self.slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
        frame = shape.text_frame
        frame.word_wrap = True
        frame.margin_left = frame.margin_right = frame.margin_top = frame.margin_bottom = 0
        frame.vertical_anchor = MSO_ANCHOR.TOP
        lines = []
        for block in str(text).split("\n"):
            lines.extend(simpleSplit(block, "BrandSansBold" if bold else "BrandSans", size, w*72))
        if len(lines) * size * 1.15 > h*72 + size:
            raise ValueError(f"Slide text overflow in {self.item['id']}: {text[:75]}")
        for index, block in enumerate(str(text).split("\n")):
            p = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
            p.text = block
            p.font.name = "Segoe UI Semibold" if bold else "Segoe UI"
            p.font.size = Pt(size)
            p.font.bold = bold
            p.font.color.rgb = rgb(colour)
            p.line_spacing = 1.15
            p.space_after = Pt(0)
        self.pdf.setFillColor(HexColor(colour))
        self.pdf.setFont("BrandSansBold" if bold else "BrandSans", size)
        baseline = 540-y*72-size
        for line in lines:
            self.pdf.drawString(x*72, baseline, line)
            baseline -= size*1.15
        return shape

    def rect(self, x, y, w, h, fill, stroke=None):
        shape = self.slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
        shape.fill.solid()
        shape.fill.fore_color.rgb = rgb(fill)
        shape.line.color.rgb = rgb(stroke or fill)
        self.pdf.setFillColor(HexColor(fill))
        self.pdf.setStrokeColor(HexColor(stroke or fill))
        self.pdf.rect(x*72, 540-(y+h)*72, w*72, h*72, fill=1, stroke=1)

    def page(self, title, kicker="", dark=False, notes=""):
        if self.number:
            self.pdf.showPage()
        self.number += 1
        self.dark = dark
        layout = self.layouts["01 Cover" if dark else "49 Blank"]
        self.slide = self.prs.slides.add_slide(layout)
        self.slide.background.fill.solid()
        background = NAVY if dark else "#FFFFFF"
        self.slide.background.fill.fore_color.rgb = rgb(background)
        self.pdf.setFillColor(HexColor(background))
        self.pdf.rect(0, 0, 960, 540, stroke=0, fill=1)
        for shape in layout.shapes:
            if shape.shape_type == 13:
                self.pdf.drawImage(ImageReader(BytesIO(shape.image.blob)), shape.left/12700,
                                   540-(shape.top+shape.height)/12700,
                                   shape.width/12700, shape.height/12700, mask="auto")
        self.rect(.62, .5, .6, .055, GOLD)
        self.text(kicker.upper() or self.item["id"].upper(), .62, .7, 11.8, .25, 12, True,
                  GOLD if dark else DEEP_GOLD)
        self.text(title, .62, 1.06, 11.9, 1.3, 36, True)
        self.text(f"{self.number:02d}", 12.15, 6.78, .5, .25, 12, False,
                  "#B9C2D3" if dark else STEEL)
        self.slide.notes_slide.notes_text_frame.text = (
            "Teaching draft. No live deployment or professional accreditation is claimed.\n\n" + notes
        )

    def paragraph(self, text):
        self.text(text, .68, 2.66, 11.65, 3.2, 18)

    def points(self, points):
        y = 2.55
        height = min(1.0, 3.8/max(len(points), 1))
        for i, point in enumerate(points):
            self.text(f"{i+1:02d}", .68, y+.03, .55, .4, 17, True,
                      GOLD if self.dark else DEEP_GOLD)
            self.text(point, 1.42, y, 10.6, height-.08, 18)
            y += height

    def table(self, headers, rows):
        columns = min(3, len(headers))
        headers = headers[:columns]
        rows = [r[:columns] for r in rows]
        table = self.slide.shapes.add_table(len(rows)+1, columns, Inches(.68), Inches(2.5), Inches(11.9), Inches(.55+.78*len(rows))).table
        for col in table.columns:
            col.width = Inches(11.9/columns)
        all_rows = [headers, *rows]
        y = 2.5
        for r, values in enumerate(all_rows):
            row_height = .55 if r == 0 else .78
            table.rows[r].height = Inches(row_height)
            for c, value in enumerate(values):
                cell = table.cell(r, c)
                cell.margin_left = cell.margin_right = Inches(.13)
                cell.margin_top = cell.margin_bottom = Inches(.05)
                cell.fill.solid()
                cell.fill.fore_color.rgb = rgb(NAVY if r == 0 else MIST if r % 2 else "#FFFFFF")
                short = textwrap.shorten(str(value), width=58 if columns == 2 else 43, placeholder="...")
                cell.text = short
                p = cell.text_frame.paragraphs[0]
                p.font.name = "Segoe UI Semibold" if r == 0 else "Segoe UI"
                p.font.size = Pt(16)
                p.font.bold = r == 0
                p.font.color.rgb = rgb("#FFFFFF" if r == 0 else NAVY)
                self.pdf.setFillColor(HexColor(NAVY if r == 0 else MIST if r % 2 else "#FFFFFF"))
                x = .68+c*11.9/columns
                self.pdf.rect(x*72, 540-(y+row_height)*72, 11.9/columns*72, row_height*72, fill=1, stroke=0)
                self.pdf.setFillColor(HexColor("#FFFFFF" if r == 0 else NAVY))
                self.pdf.setFont("BrandSansBold" if r == 0 else "BrandSans", 16)
                for n, line in enumerate(simpleSplit(short, "BrandSans", 16, (11.9/columns-.26)*72)):
                    self.pdf.drawString((x+.13)*72, 540-(y+.07)*72-16-n*18, line)
            y += row_height
        self.text("Excerpt. Complete records and conditions are in the learner guide and workbook.", .68, 6.24, 11.8, .3, 12, False, STEEL)

    def process(self, labels):
        positions = [(.7, 2.65), (4.95, 2.65), (9.2, 2.65), (9.2, 4.55), (4.95, 4.55), (.7, 4.55)]
        for i, ((x, y), label) in enumerate(zip(positions, labels)):
            self.rect(x, y, 3.45, 1.05, MIST, LINE)
            self.text(f"{i+1:02d}", x+.15, y+.1, .5, .25, 12, True, DEEP_GOLD)
            self.text(label, x+.15, y+.4, 3.12, .55, 16, True, NAVY)
        self.text("Read across the top row, then back along the bottom. Retain the evidence.", .7, 6.06, 11.8, .3, 12, False, STEEL)

    def finish(self):
        self.prs.save(self.directory / "slides.pptx")
        self.pdf.showPage()
        self.pdf.save()


def slide_deck(item, directory, brand):
    d = Deck(item, directory, brand)
    d.page(item["title"], "AI from Zero to Professional Practice", True, item["summary"])
    d.text(item["summary"], .68, 3.12, 10.8, 1.7, 18)
    d.text("TEACHING DRAFT / EDITABLE MATERIAL / HUMAN ACCOUNTABILITY", .68, 5.57, 11.5, .4, 12, False, GOLD)
    d.page("What you will be able to do", "Outcomes", notes="\n".join(item["outcomes"]))
    d.points(item["outcomes"])
    for title, body in item["concepts"]:
        d.page(title, "Explain", notes=body + "\n\nAsk for an example and a limitation of the concept.")
        d.paragraph(body)
    for start in range(0, min(len(item["rows"]), 12), 4):
        d.page("Read the supplied evidence", "Synthetic practice material",
               notes="All values are invented teaching data. Inspect the complete input in the learner guide.\n" + str(item["rows"][start:start+4]))
        d.table(item["headers"], item["rows"][start:start+4])
    d.page("A worked result, not a promise", "Demonstration", notes=item["example"])
    d.paragraph(item["example"])
    d.page("Map the process", "Architecture / process thinking", notes="The diagram describes concepts, not a deployed system. " + "; ".join(item["diagram"]))
    d.process(item["diagram"])
    for start in range(0, len(item["steps"]), 3):
        d.page("Your next practical steps", f"Lab / {start+1}-{min(start+3,len(item['steps']))}",
               notes="\n".join(item["steps"][start:start+3]))
        d.points(item["steps"][start:start+3])
    d.page("Keep these artifacts", "Submission", notes="\n".join(item["deliverables"]))
    d.points(item["deliverables"][:4])
    if len(item["deliverables"]) > 4:
        d.page("Complete the handover", "Submission continued", notes="\n".join(item["deliverables"][4:]))
        d.points(item["deliverables"][4:])
    d.page("Know when to stop", "Safety and permission", True, notes=item["safety"])
    d.paragraph(item["safety"])
    d.page("Check your understanding", "Discuss before viewing the key",
           notes="\n\n".join(f"{q}\n{a}" for q, a in zip(item["questions"], item["answers"])))
    d.points(item["questions"])
    d.page("Assess evidence, not confidence", "Feedback",
           notes="Each ordinary dimension is 0-4. Provisional academic pass 12/16 with remediation of all critical issues. Course category grading and production approval are separate.")
    d.points(item["rubric"])
    d.page("Access is not the learning outcome", "Offline / limited access",
           notes="Use the supplied data and manual route. Label live execution not assessed. Do not equate simulation with implementation.")
    d.paragraph("Use supplied data, a paper prototype or a manual audit when paid tools are unavailable. Record exactly what you observed. Live media quality, permissions and deployment remain unassessed unless actually tested.")
    d.page("Take the evidence forward", "Next step", True, notes="Review the Word guide, workbook, diagrams and roadmap. The programme is a teaching draft, not professional accreditation.")
    d.paragraph("Save your sources, outputs, tests and limitations. Use them in one professional project. A course score does not authorise an external action or a regulated deployment.")
    d.finish()


def workbook(item, directory, lessons, phases):
    wb = xlsxwriter.Workbook(directory / "workbook.xlsx", {"strings_to_formulas": False, "strings_to_urls": False})
    wb.set_properties({"title": item["title"], "author": "Khaled Hamad", "comments": "Teaching draft. Empty evidence is not a pass."})
    base = {"font_name": "Segoe UI", "font_size": 11, "font_color": NAVY, "valign": "top"}
    fmt = lambda **kwargs: wb.add_format({**base, **kwargs})
    title = fmt(bold=True, font_size=22, bg_color=NAVY, font_color="#FFFFFF", text_wrap=True)
    head = fmt(bold=True, bg_color=NAVY, font_color="#FFFFFF", text_wrap=True, border=1, border_color=LINE)
    normal = fmt(text_wrap=True, border=1, border_color=LINE)
    entry = fmt(text_wrap=True, bg_color="#F6EFDD", border=1, border_color=LINE)
    calc = fmt(text_wrap=True, bg_color=MIST, border=1, border_color=LINE)
    pct = fmt(num_format="0.00%", bg_color=MIST, border=1, border_color=LINE)
    cash = fmt(num_format='#,##0.00;[Red]-#,##0.00', bg_color=MIST, border=1, border_color=LINE)
    sheets = {}

    def sheet(name, headers=None, rows=()):
        ws = wb.add_worksheet(name)
        sheets[name] = ws
        ws.hide_gridlines(2)
        ws.freeze_panes(4, 0)
        ws.set_column(0, 0, 24)
        ws.set_column(1, 7, 32)
        ws.set_default_row(48)
        ws.set_row(0, 35)
        ws.merge_range(0, 0, 1, max((len(headers) if headers else 4)-1, 3), item["title"], title)
        ws.write(2, 0, "Teaching draft")
        ws.merge_range(2, 1, 2, max((len(headers) if headers else 4)-1, 3), "Highlighted cells: inputs. Grey: formulas/reference. No automatic production approval.", fmt(text_wrap=True))
        if headers:
            ws.write_row(3, 0, headers, head)
            for r, values in enumerate(rows, 4):
                ws.write_row(r, 0, values, normal)
            if rows:
                ws.autofilter(3, 0, len(rows)+3, len(headers)-1)
        ws.set_landscape()
        ws.fit_to_pages(1, 0)
        ws.repeat_rows(0, 3)
        return ws

    readme = sheet("Read me", ["Use", "Instruction"], [
        ["Scope", item["summary"]],
        ["Status", "Examples and expected answers are teaching materials. No real deployment or commercial licence is asserted."],
        ["Input cells", "Enter permitted evidence in highlighted cells; do not overwrite formula cells."],
        ["Scoring", "Ordinary /16 lesson feedback is separate from the programme's weighted grade and production release authority."],
        ["Gate", "All gates need Clear plus evidence. Pending, Hold or blank evidence prevents readiness for review."],
        ["Costs", "Enter dated quotes/measurements. Zero is valid only for a documented no-cost/not-applicable item."],
        ["Data", "Use learner codes and synthetic/public data; no private records, passwords or service keys."],
        ["Offline", "Record manual/simulated work accurately. Live-service performance remains unassessed."],
    ])
    sheet("Practice data", item["headers"], item["rows"])
    if item.get("glossary"):
        glossary = sheet("Glossary", ["Term", "Plain-language meaning"], item["glossary"])
        glossary.set_column(1, 1, 95)
    log_rows = [[f"T{i+1:02d}", row[1], row[2], "", "Unrun"] for i, row in enumerate(item.get("tests", []))]
    if not log_rows:
        log_rows = [[f"C{i+1:02d}", q, a, "", "Unrun"] for i, (q, a) in enumerate(zip(item["questions"], item["answers"]))]
    log = sheet("Lab log", ["ID", "Case / question", "Expected outcome", "Actual evidence", "Status", "Review flag"], log_rows)
    log.data_validation(4, 4, len(log_rows)+3, 4, {"validate": "list", "source": ["Unrun", "Pass", "Fail", "N/A (justified)"]})
    log.set_column(1, 3, 45)
    for row in range(5, len(log_rows)+5):
        log.write_blank(row-1, 3, None, entry)
        log.write(row-1, 4, "Unrun", entry)
        log.write_formula(f"F{row}", f'=IF(AND(OR(E{row}="Pass",E{row}="N/A (justified)"),D{row}=""),"Evidence required",IF(E{row}="Unrun","Not assessed",E{row}))', calc, "Not assessed")
    rubric = sheet("Rubric", ["Dimension", "Maximum", "Score", "Evidence / feedback"], [[x, 4, "", ""] for x in item["rubric"]])
    rubric.data_validation("C5:C8", {"validate": "integer", "criteria": "between", "minimum": 0, "maximum": 4,
                                    "input_title": "Evidence-based score", "input_message": "Enter 0-4 after review.", "error_type": "stop"})
    rubric.set_column(0, 0, 43)
    for r in range(4, 8):
        rubric.write_blank(r, 2, None, entry)
        rubric.write_blank(r, 3, None, entry)
    rubric.write("A10", "Total /16")
    rubric.write_formula("C10", '=IF(COUNT(C5:C8)<4,"Not assessed",SUM(C5:C8))', calc, "Not assessed")
    rubric.write("A11", "Academic feedback state")
    rubric.write_formula("C11", '=IF(COUNT(C5:C8)<4,"Not assessed",IF(AND(SUM(C5:C8)>=12,COUNTIF(\'Safety gates\'!B5:B9,"Clear")=5,COUNTBLANK(\'Safety gates\'!C5:C9)=0),"Ready for instructor review","Revise / remediate"))', calc, "Not assessed")
    rubric.merge_range("A13:D14", "This is not a production-release approval. The programme capstone has its separate weighted rubric and owner/professional gates.", normal)
    gates = sheet("Safety gates", ["Gate", "Decision", "Evidence and authorised reviewer"], [
        ["Permitted data and rights", "Pending", ""],
        ["No fabricated consequential evidence", "Pending", ""],
        ["No unapproved consequential action", "Pending", ""],
        ["Professional / owner authority identified", "Pending", ""],
        ["Truthful testing, release status and costs", "Pending", ""],
    ])
    gates.set_column(0, 0, 48)
    gates.set_column(2, 2, 65)
    gates.data_validation("B5:B9", {"validate": "list", "source": ["Pending", "Clear", "Hold"]})
    for r in range(4, 9):
        gates.write(r, 1, "Pending", entry)
        gates.write_blank(r, 2, None, entry)
    gates.conditional_format("B5:B9", {"type": "text", "criteria": "containing", "value": "Hold", "format": fmt(bg_color="#F6EFDD", bold=True)})
    risks = sheet("Risk register", ["Risk", "Owner", "Likelihood 1-5", "Impact 1-5", "Priority", "Mitigation", "Residual / status"], [
        ["Unsupported factual claim", "", "", "", "", "Source audit before use", "Pending"],
        ["Unauthorised data or rights", "", "", "", "", "Permission check and minimum data", "Pending"],
        ["Unapproved external action", "", "", "", "", "Enforced exact-action approval", "Pending"],
        ["Provider / access failure", "", "", "", "", "Visible error and manual fallback", "Pending"],
    ])
    risks.data_validation("C5:D8", {"validate": "integer", "criteria": "between", "minimum": 1, "maximum": 5})
    for row in range(5, 9):
        risks.write_formula(f"E{row}", f'=IF(COUNT(C{row}:D{row})<2,"",C{row}*D{row})', calc, "")
        for col in [1, 2, 3]:
            risks.write_blank(row-1, col, None, entry)
    budget = sheet("Budget", ["Category", "Owner", "Units", "Unit price USD", "Fixed USD", "Planned USD", "Actual USD", "Quote date / source"], [
        [category, "", "", "", "", "", "", "Unpriced; enter dated quote or justified zero"]
        for category in ["Assistant access", "Runtime API", "Media / voice attempts", "App builder / automation", "Hosting / storage", "Domain / delivery", "Maintenance / contingency"]
    ])
    budget.set_column(7, 7, 48)
    budget.data_validation("C5:E11", {"validate": "decimal", "criteria": ">=", "value": 0, "error_type": "stop"})
    for row in range(5, 12):
        for col in [1, 2, 3, 4, 6]:
            budget.write_blank(row-1, col, None, entry)
        budget.write_formula(f"F{row}", f'=IF(COUNTA(C{row}:E{row})=0,"",IF(COUNT(C{row}:E{row})<3,"Unpriced / check inputs",C{row}*D{row}+E{row}))', cash, "")
    budget.write("A13", "Total planned")
    budget.write_formula("F13", '=IF(COUNT(F5:F11)<7,"Unpriced items remain",SUM(F5:F11))', calc, "Unpriced items remain")
    budget.write_formula("G13", '=IF(COUNT(G5:G11)<7,"Actuals not complete",SUM(G5:G11))', calc, "Actuals not complete")
    budget.merge_range("A15:H16", "For each category enter Units, Unit price and Fixed explicitly. Use documented zeros for components that do not apply. Partial or non-numeric entries are not a complete quote; record the date, currency basis and source.", normal)
    plan = sheet("Roadmap", ["ID", "Task", "Planned hours", "Depends on", "Owner", "Evidence / output", "Status"], item["roadmap"])
    plan.set_column(5, 5, 65)
    plan.data_validation(4, 6, len(item["roadmap"])+3, 6, {"validate": "list", "source": ["Not started", "In progress", "Blocked", "Done"]})
    total_row = len(item["roadmap"])+6
    plan.write(total_row, 0, "Planned hours")
    plan.write_formula(total_row, 2, f"=SUM(C5:C{len(item['roadmap'])+4})", calc, item["hours"])
    key = sheet("Answer key", ["Question", "Instructor guidance"], list(zip(item["questions"], item["answers"])))
    key.set_column(0, 0, 48)
    key.set_column(1, 1, 100)
    key.merge_range(9, 0, 15, 2, "WORKED RESULT (reference, not learner evidence)\n\n" + item["example"], normal)
    if item.get("week") == 2:
        rows = [[r[0], r[1], r[2], r[4], "", r[3], "Unrun"] for r in item["rows"]]
        ws = sheet("Classifier lab", ["ID", "Free feature", "Invoice feature", "Split", "Your prediction", "Reference label", "Result"], rows)
        ws.data_validation("E5:E14", {"validate": "list", "source": ["Promotional", "Work"]})
        ws.merge_range("A17:G18", "Instructor: hide reference labels and held-out examples before the exercise. Freeze the rule before revealing the held-out rows. This sheet starts unrun; the Answer key contains a separate worked example.", normal)
        for row in range(5, 15):
            ws.write_blank(row-1, 4, None, entry)
            ws.write_formula(f"G{row}", f'=IF(E{row}="","Unrun",IF(E{row}=F{row},"Correct","Incorrect"))', calc, "Unrun")
        for row, split, count in [(21, "Train", 4), (22, "Development", 2), (23, "Held out", 4)]:
            ws.write(f"A{row}", split, normal)
            ws.write_formula(f"B{row}", f'=IF(COUNTIFS(D5:D14,A{row},E5:E14,"<>")<{count},"Not assessed",COUNTIFS(D5:D14,A{row},G5:G14,"Correct")/{count})', pct, "Not assessed")
    if item.get("week") == 3:
        ws = sheet("Metrics", ["Outcome", "Count", "Metric", "Value"], [
            ["True positive", 8], ["False positive", 18], ["False negative", 2], ["True negative", 72]])
        for cell, label, formula, value in [
            ("D5", "Precision", '=IF(B5+B6=0,"Undefined",B5/(B5+B6))', 8/26),
            ("D6", "Recall", '=IF(B5+B7=0,"Undefined",B5/(B5+B7))', .8),
            ("D7", "Accuracy", '=IF(SUM(B5:B8)=0,"Undefined",(B5+B8)/SUM(B5:B8))', .8),
            ("D8", "Always-negative accuracy", '=IF(SUM(B5:B8)=0,"Undefined",(B6+B8)/SUM(B5:B8))', .9),
        ]:
            ws.write(f"C{cell[1:]}", label, normal)
            ws.write_formula(cell, formula, pct, value)
        for row, value in enumerate([8, 18, 2, 72], 4):
            ws.write(row, 1, value, entry)
        ws.data_validation("B5:B8", {"validate": "integer", "criteria": ">=", "value": 0})
        ws.write_row("A11", ["False-alarm cost", 5], entry)
        ws.write_row("A12", ["Miss cost", 100], entry)
        ws.write("C11", "Candidate error cost", normal)
        ws.write_formula("D11", "=B6*B11+B7*B12", cash, 290)
        ws.write("C12", "Baseline error cost", normal)
        ws.write_formula("D12", "=(B5+B7)*B12", cash, 1000)
    if item.get("week") == 5:
        run_rows = [[version, case, "", *[""]*8, "", "", ""] for version, case in
                    [("V1", "A"), ("V1", "B"), ("V2", "A"), ("V2", "B"), ("V3", "A"), ("V3", "B"), ("V3", "C unfamiliar"), ("V3", "B repeat")]]
        ws = sheet("Prompt runs", ["Version", "Case", "Mode", *[f"C{i}" for i in range(1, 9)], "Total", "Output criterion", "Evidence"], run_rows)
        ws.set_column(3, 10, 7)
        ws.set_column(11, 12, 24)
        ws.set_column(13, 13, 45)
        ws.data_validation("C5:C12", {"validate": "list", "source": ["Live", "Demonstration", "Offline"]})
        ws.data_validation("D5:K12", {"validate": "integer", "criteria": "between", "minimum": 0, "maximum": 1})
        for row in range(5, 13):
            ws.write_formula(f"L{row}", f'=IF(COUNT(D{row}:K{row})<8,"",SUM(D{row}:K{row}))', calc, "")
            ws.write_formula(f"M{row}", f'=IF(COUNT(D{row}:K{row})<8,"Not assessed",IF(AND(L{row}>=7,COUNTIF(E{row}:H{row},1)=4),"Meets output criterion","Revise"))', calc, "Not assessed")
    if item.get("week") == 9:
        cleaned = [r for i, r in enumerate(item["rows"]) if i != 2]
        ws = sheet("Cleaned example", [*item["headers"], "Amount USD", "Note"], [
            [*r, "", "Missing quantity; unresolved" if r[0] == "A03" else "Known source value"] for r in cleaned])
        for index, record in enumerate(cleaned, 5):
            if record[0] == "A07":
                ws.write_number(index-1, 3, 35, entry)
            quantity, price = record[2], 35 if record[0] == "A07" else record[3]
            value = quantity*price if isinstance(quantity, (int, float)) else ""
            ws.write_formula(f"F{index}", f'=IF(COUNT(C{index}:D{index})<2,"",C{index}*D{index})', cash, value)
        ws.write("A16", "Known completed revenue")
        ws.write_formula("F16", '=SUMIF(E5:E13,"Completed",F5:F13)', cash, 265)
        ws.write("A17", "Refund separately")
        ws.write_formula("F17", '=SUMIF(E5:E13,"Refund",F5:F13)', cash, -40)
        ws.merge_range("A19:G20", "This is the instructor's worked example. One completed order has unknown quantity; 265 USD is not a complete revenue total.", normal)
    if item.get("week") == 10:
        ws = sheet("Analysis", ["Channel", "Visits", "Sign-ups", "Spend USD", "Conversion", "Spend per sign-up"], [r+["", ""] for r in item["rows"]])
        for row, record in enumerate(item["rows"], 5):
            ws.write_formula(f"E{row}", f'=IF(B{row}=0,"Undefined",C{row}/B{row})', pct, record[2]/record[1])
            ws.write_formula(f"F{row}", f'=IF(C{row}=0,"Undefined",D{row}/C{row})', cash, record[3]/record[2])
        ws.write("A10", "Total")
        for col, value in [("B", 4000), ("C", 270), ("D", 400)]:
            ws.write_formula(f"{col}10", f"=SUM({col}5:{col}8)", calc, value)
        ws.write_formula("E10", '=IF(B10=0,"Undefined",C10/B10)', pct, 270/4000)
        chart = wb.add_chart({"type": "column"})
        chart.add_series({"name": "Sign-ups", "categories": "='Analysis'!$A$5:$A$8", "values": "='Analysis'!$C$5:$C$8",
                          "fill": {"color": NAVY}, "border": {"none": True}})
        chart.set_title({"name": "Observed sign-ups by channel (synthetic)"})
        chart.set_y_axis({"name": "Sign-ups", "min": 0})
        chart.set_legend({"none": True})
        ws.insert_chart("H5", chart, {"x_scale": 1.2, "y_scale": 1.2})
    if item["id"] == "blueprint":
        rows = [[x["week"], phases[x["phase"]][0], x["title"], 6, "Not started"] for x in lessons]
        ws = sheet("Course roadmap", ["Week", "Phase", "Lesson", "Hours", "Status"], rows)
        ws.set_column(2, 2, 62)
        ws.data_validation("E5:E28", {"validate": "list", "source": ["Not started", "In progress", "Blocked", "Done"]})
        ws.write("A30", "Core hours")
        ws.write_formula("D30", "=SUM(D5:D28)", calc, 144)
        gradebook = sheet("Gradebook", ["Learner code", "W1-8 %", "W9-16 %", "Studio %", "Capstone %", "Weighted %", "Critical gates", "Academic decision"])
        for row in range(5, 25):
            gradebook.write(row-1, 6, "Pending", entry)
            gradebook.write_formula(f"F{row}", f'=IF(COUNT(B{row}:E{row})<4,"",B{row}*0.2+C{row}*0.25+D{row}*0.2+E{row}*0.35)', calc, "")
            gradebook.write_formula(f"H{row}", f'=IF(COUNT(B{row}:E{row})<4,"Not assessed",IF(AND(F{row}>=70,E{row}>=70,G{row}="Clear"),"Instructor confirmation required","Review / remediate"))', calc, "Not assessed")
        gradebook.data_validation("B5:E24", {"validate": "decimal", "criteria": "between", "minimum": 0, "maximum": 100})
        gradebook.data_validation("G5:G24", {"validate": "list", "source": ["Pending", "Clear", "Hold"]})
    if item["id"] == "blueprint" or item.get("week", 0) >= 21:
        dimensions = [
            ["Problem fit and professional usefulness", 15, "", "", ""],
            ["Quality and source traceability", 20, "", "", ""],
            ["Evaluation and failure analysis", 20, "", "", ""],
            ["Safety, privacy, rights and oversight", 20, "", "", ""],
            ["Reproducibility and usability", 15, "", "", ""],
            ["Cost, maintenance and communication", 10, "", "", ""],
        ]
        ws = sheet("Capstone rubric", ["Dimension", "Weight %", "Score 0-4", "Weighted points", "Evidence / reviewer"], dimensions)
        ws.set_column(0, 0, 50)
        ws.set_column(4, 4, 65)
        ws.data_validation("C5:C10", {"validate": "integer", "criteria": "between", "minimum": 0, "maximum": 4})
        for row in range(5, 11):
            ws.write_blank(row-1, 2, None, entry)
            ws.write_blank(row-1, 4, None, entry)
            ws.write_formula(f"D{row}", f'=IF(ISNUMBER(C{row}),C{row}/4*B{row},"")', calc, "")
        ws.write("A12", "Capstone score /100")
        ws.write_formula("D12", '=IF(COUNT(C5:C10)<6,"Not assessed",SUM(D5:D10))', calc, "Not assessed")
        ws.write("A13", "Review state")
        ws.write_formula("D13", '=IF(COUNT(C5:C10)<6,"Not assessed",IF(AND(D12>=70,COUNTIF(\'Safety gates\'!B5:B9,"Clear")=5,COUNTBLANK(\'Safety gates\'!C5:C9)=0),"Ready for instructor review","Revise / remediate"))', calc, "Not assessed")
        ws.merge_range("A15:E17", "The six weighted dimensions produce the capstone category score. Transfer an instructor-confirmed score to the programme Gradebook. Minimum test cases, held-out independence and all safety conditions require evidence; this sheet cannot authorise release or accreditation.", normal)
    if item["id"] == "instructor-guide":
        sheet("Pilot observations", ["Learner code", "Week / activity", "Actual minutes", "Confusion / barrier", "Observed evidence", "Remediation", "Recheck result"],
              [["", "", "", "", "", "", "Not assessed"] for _ in range(12)])
    wb.close()

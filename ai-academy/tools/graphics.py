"""Original diagrams and designs using the supplied brand's permitted logo artwork."""

import base64
import json
import math
from pathlib import Path
import posixpath
import textwrap
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape
from zipfile import ZipFile

from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

NAVY = "#182234"
GOLD = "#CAAD6A"
DEEP_GOLD = "#806226"
MIST = "#F3F5F8"
STEEL = "#3D4A63"
LINE = "#DDE2EA"
FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
REGULAR = FONT_DIR / "LiberationSans-Regular.ttf"
BOLD = FONT_DIR / "LiberationSans-Bold.ttf"
NS = {"p": "http://schemas.openxmlformats.org/presentationml/2006/main",
      "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
      "rel": "http://schemas.openxmlformats.org/package/2006/relationships"}

pdfmetrics.registerFont(TTFont("BrandSans", str(REGULAR)))
pdfmetrics.registerFont(TTFont("BrandSansBold", str(BOLD)))


def extract_layout_logo(package, layout_path):
    root = ET.fromstring(package.read(layout_path))
    rel_path = posixpath.join(posixpath.dirname(layout_path), "_rels", posixpath.basename(layout_path) + ".rels")
    rels = ET.fromstring(package.read(rel_path))
    targets = {r.attrib["Id"]: r.attrib["Target"] for r in rels}
    for picture in root.findall(".//p:pic", NS):
        props = picture.find("p:nvPicPr/p:cNvPr", NS)
        if props is not None and props.attrib.get("descr") == "Khaled Hamad logo":
            blip = picture.find(".//a:blip", NS)
            target = targets[blip.attrib["{" + NS["r"] + "}embed"]]
            return package.read(posixpath.normpath(posixpath.join(posixpath.dirname(layout_path), target)))
    raise ValueError(f"No supplied logo found in {layout_path}")


def prepare_brand(root, brand):
    assets = root / "assets"
    assets.mkdir(exist_ok=True)
    with ZipFile(brand / "Khaled Hamad - Slide Master Template.potx") as package:
        for layout, name in [("ppt/slideLayouts/slideLayout3.xml", "logo-gold.png"),
                             ("ppt/slideLayouts/slideLayout51.xml", "logo-navy.png")]:
            (assets / name).write_bytes(extract_layout_logo(package, layout))
    for path in [assets / "logo-gold.png", assets / "logo-navy.png"]:
        with Image.open(path) as image:
            image.verify()


def font(size, bold=False):
    return ImageFont.truetype(str(BOLD if bold else REGULAR), size)


def text_lines(value, width, size=18, bold=False):
    result = []
    f = font(size, bold)
    for paragraph in str(value).split("\n"):
        line = ""
        for word in paragraph.split():
            trial = (line + " " + word).strip()
            if line and f.getlength(trial) > width:
                result.append(line)
                line = word
            else:
                line = trial
        result.append(line)
    return result


def draw_diagram(title, nodes, edges, directory, stem, subtitle):
    with_legend = any(edge[2] for edge in edges)
    width = 1280
    height = 750 + math.ceil(len(edges)/2)*66 if with_legend else 770
    positions = [(50, 180), (475, 180), (900, 180), (900, 465), (475, 465), (50, 465)]
    box_width, box_height = 330, 155
    scene = []
    scene.append(("text", 50, 42, title, 32, True, NAVY))
    scene.append(("text", 50, 98, subtitle, 16, False, STEEL))
    scene.append(("rect", 50, 143, 58, 5, GOLD, GOLD))
    excalidraw = []
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">',
        f"<title id=\"title\">{escape(title)}</title><desc id=\"description\">{escape(subtitle)}. "
        + escape("; ".join(n[0] + ": " + n[1] for n in nodes)) + "</desc>",
        '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#806226"/></marker></defs>',
        f'<rect width="{width}" height="{height}" fill="white"/>',
        f'<rect x="50" y="143" width="58" height="5" fill="{GOLD}"/>',
    ]

    def element(kind, identity, **kwargs):
        return {"id": identity, "type": kind, "angle": 0, "strokeColor": NAVY,
                "backgroundColor": "transparent", "fillStyle": "solid", "strokeWidth": 1.5,
                "strokeStyle": "solid", "roughness": 0, "opacity": 100, "groupIds": [],
                "frameId": None, "seed": 100, "version": 1, "versionNonce": 1,
                "isDeleted": False, "boundElements": [], "updated": 0, "link": None,
                "locked": False, **kwargs}

    labels = []
    for index, (source, target, label) in enumerate(edges):
        sx, sy = positions[source]
        tx, ty = positions[target]
        scx, scy = sx + box_width / 2, sy + box_height / 2
        tcx, tcy = tx + box_width / 2, ty + box_height / 2
        reverse = any(a == target and b == source for a, b, _ in edges)
        offset = (9 if source < target else -9) if reverse else 0
        port = (index-(len(edges)-1)/2)*12 if with_legend else 0
        if sy == ty and abs(sx-tx) == 425:
            direction = 1 if tx > sx else -1
            points = [(scx+direction*box_width/2, scy+offset), (tcx-direction*box_width/2, tcy+offset)]
        elif sx == tx and sy != ty:
            direction = 1 if ty > sy else -1
            points = [(scx+port, scy+direction*box_height/2), (tcx+port, tcy-direction*box_height/2)]
        else:
            lane = 350+index*12
            source_y = sy+box_height if sy == 180 else sy
            target_y = ty+box_height if ty == 180 else ty
            points = [(scx+port, source_y), (scx+port, lane),
                      (tcx+port, lane), (tcx+port, target_y)]
        x1, y1 = points[0]
        scene.append(("path", points, DEEP_GOLD))
        path_data = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in points)
        svg.append(f'<path d="{path_data}" stroke="{DEEP_GOLD}" stroke-width="2" fill="none" marker-end="url(#arrow)"/>')
        excalidraw.append(element("arrow", f"edge-{index}", x=x1, y=y1,
                                 width=max(x for x, _ in points)-min(x for x, _ in points),
                                 height=max(y for _, y in points)-min(y for _, y in points),
                                 points=[[x-x1, y-y1] for x, y in points],
                                 strokeColor=DEEP_GOLD, startArrowhead=None, endArrowhead="arrow",
                                 startBinding={"elementId": f"node-{source}", "focus": 0, "gap": 1},
                                 endBinding={"elementId": f"node-{target}", "focus": 0, "gap": 1}))
        if label:
            lx, ly = ((points[0][0]+points[1][0])/2, (points[0][1]+points[1][1])/2)
            short = f"E{index+1}"
            while any(abs(lx-x) < 38 and abs(ly-y) < 18 for x, y in labels):
                ly += 20
            labels.append((lx, ly))
            scene.append(("label", lx, ly, short, 12, False, STEEL))
            label_width = font(12).getlength(short) + 10
            svg.append(f'<rect x="{lx-label_width/2:.1f}" y="{ly-11:.1f}" width="{label_width:.1f}" height="22" fill="white"/>')
            svg.append(f'<text x="{lx:.1f}" y="{ly+4:.1f}" text-anchor="middle" fill="{STEEL}" font-size="12" font-family="Segoe UI,Arial,sans-serif">{escape(short)}</text>')
            excalidraw.append(element("text", f"edge-label-{index}", x=lx-15, y=ly-9, width=32, height=30,
                                     text=short, originalText=short, fontSize=12, fontFamily=2,
                                     textAlign="center", verticalAlign="top", lineHeight=1.25,
                                     strokeColor="#000000", containerId=None, autoResize=True))
    for i, ((title_text, description), (x, y)) in enumerate(zip(nodes, positions)):
        scene.append(("rect", x, y, box_width, box_height, MIST, LINE))
        svg.append(f'<rect x="{x}" y="{y}" width="{box_width}" height="{box_height}" rx="7" fill="{MIST}" stroke="{LINE}"/>')
        title_lines = text_lines(title_text, box_width-36, 21, True)
        description_lines = text_lines(description, box_width-36, 16)
        if len(title_lines) > 2 or len(description_lines) > 4:
            raise ValueError(f"Diagram text too large: {title_text}")
        ty = y + 22
        for line in title_lines:
            scene.append(("text", x+18, ty, line, 21, True, NAVY))
            ty += 26
        ty += 7
        for line in description_lines:
            scene.append(("text", x+18, ty, line, 16, False, STEEL))
            ty += 21
        excalidraw.append(element("rectangle", f"node-{i}", x=x, y=y, width=box_width, height=box_height,
                                 backgroundColor=MIST, roundness={"type": 3}, groupIds=[f"group-{i}"],
                                 boundElements=[{"id": f"edge-{j}", "type": "arrow"}
                                                for j, (a, b, _) in enumerate(edges) if i in (a, b)]))
        text = "\n".join(title_lines + description_lines)
        excalidraw.append(element("text", f"node-label-{i}", x=x+18, y=y+18, width=box_width-36,
                                 height=18*2.5*(len(title_lines)+len(description_lines)), text=text,
                                 originalText=text, fontSize=18, fontFamily=2, textAlign="left",
                                 verticalAlign="top", lineHeight=1.25, strokeColor="#000000",
                                 containerId=None, autoResize=True, groupIds=[f"group-{i}"]))
    if with_legend:
        scene.append(("text", 50, 640, "CONNECTIONS / WHAT MOVES", 14, True, DEEP_GOLD))
        for index, (source, target, label) in enumerate(edges):
            x, y = 50+(index % 2)*620, 675+(index//2)*66
            text = f"E{index+1}  {nodes[source][0]} -> {nodes[target][0]}: {label}"
            lines = text_lines(text, 565, 14)
            for n, line in enumerate(lines):
                scene.append(("text", x, y+n*18, line, 14, False, STEEL))
            excalidraw.append(element("text", f"legend-{index}", x=x, y=y, width=565, height=35*len(lines),
                                     text="\n".join(lines), originalText=text, fontSize=14, fontFamily=2,
                                     textAlign="left", verticalAlign="top", lineHeight=1.25,
                                     strokeColor="#000000", containerId=None, autoResize=True))
    for op in scene:
        if op[0] != "text":
            continue
        _, x, y, text, size, bold, colour = op
        svg.append(f'<text x="{x}" y="{y+size}" fill="{colour}" font-size="{size}" font-weight="{600 if bold else 400}" font-family="Segoe UI,Arial,sans-serif">{escape(text)}</text>')
    footer = "TEACHING REFERENCE • HUMAN REVIEW AND REAL APPROVAL REMAIN REQUIRED"
    scene.append(("text", 50, height-56, footer, 13, False, STEEL))
    svg.append(f'<text x="50" y="{height-40}" fill="{STEEL}" font-size="13" font-family="Segoe UI,Arial,sans-serif">{escape(footer)}</text>')
    svg.append("</svg>")
    (directory / f"{stem}.svg").write_text("\n".join(svg))
    excalidraw.insert(0, element("text", "diagram-title", x=50, y=42, width=1180, height=80,
                                text=title, originalText=title, fontSize=32, fontFamily=2,
                                textAlign="left", verticalAlign="top", lineHeight=1.25,
                                strokeColor="#000000", containerId=None, autoResize=True))
    (directory / f"{stem}.excalidraw").write_text(json.dumps({
        "type": "excalidraw", "version": 2, "source": "Khaled Hamad AI curriculum",
        "elements": excalidraw, "appState": {"viewBackgroundColor": "#FFFFFF"}, "files": {},
    }, indent=2))
    render_scene(scene, width, height, directory / stem)


def render_scene(scene, width, height, destination):
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    pdf = canvas.Canvas(str(destination.with_suffix(".pdf")), pagesize=(width, height))
    pdf.setTitle(destination.stem.replace("-", " ").title())
    for op in scene:
        if op[0] == "rect":
            _, x, y, w, h, fill, stroke = op
            draw.rectangle((x, y, x+w, y+h), fill=fill, outline=stroke)
            pdf.setFillColor(fill)
            pdf.setStrokeColor(stroke)
            pdf.rect(x, height-y-h, w, h, fill=1, stroke=1)
        elif op[0] in ("text", "label"):
            kind, x, y, text, size, bold, colour = op
            if kind == "label":
                w = font(size, bold).getlength(text)
                x, y = x-w/2, y-size/2
                draw.rectangle((x-5, y-3, x+w+5, y+size+5), fill="white")
                pdf.setFillColor("white")
                pdf.rect(x-5, height-y-size-5, w+10, size+8, stroke=0, fill=1)
            draw.text((x, y), text, font=font(size, bold), fill=colour)
            pdf.setFillColor(colour)
            pdf.setFont("BrandSansBold" if bold else "BrandSans", size)
            pdf.drawString(x, height-y-size, text)
        elif op[0] in ("line", "path"):
            if op[0] == "line":
                _, x1, y1, x2, y2, colour = op
                points = [(x1, y1), (x2, y2)]
            else:
                _, points, colour = op
            draw.line(points, fill=colour, width=2)
            pdf.setStrokeColor(colour)
            pdf.setLineWidth(2)
            path = pdf.beginPath()
            path.moveTo(points[0][0], height-points[0][1])
            for x, y in points[1:]:
                path.lineTo(x, height-y)
            pdf.drawPath(path, fill=0, stroke=1)
            (x1, y1), (x2, y2) = points[-2:]
            angle = math.atan2(y2-y1, x2-x1)
            a = (x2-10*math.cos(angle-.45), y2-10*math.sin(angle-.45))
            b = (x2-10*math.cos(angle+.45), y2-10*math.sin(angle+.45))
            draw.polygon([(x2,y2), a, b], fill=colour)
            path = pdf.beginPath()
            path.moveTo(x2, height-y2)
            path.lineTo(a[0], height-a[1])
            path.lineTo(b[0], height-b[1])
            path.close()
            pdf.setFillColor(colour)
            pdf.drawPath(path, fill=1, stroke=0)
    image.save(destination.with_suffix(".png"), optimize=True)
    pdf.showPage()
    pdf.save()


def process_diagram(item, directory):
    descriptions = ["Start with permitted evidence", "Make assumptions explicit", "Record the version",
                    "Inspect actual behaviour", "Do not replace review with confidence", "Retain the evidence and limits"]
    nodes = list(zip(item["diagram"], descriptions))
    draw_diagram(item["title"], nodes, [[i, i+1, ""] for i in range(5)], directory, "process",
                 "Concept / process map • read across the top row, then back along the bottom row")


def architecture_diagram(item, directory):
    nodes = [(row[0], f"{row[1]}: {row[2]}") for row in item["architecture"]]
    draw_diagram(item["title"], nodes, item["connections"], directory, "architecture",
                 "Reference architecture • component responsibilities, not a deployed implementation")


def wireframe(item, directory):
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="860" viewBox="0 0 1440 860" role="img" aria-labelledby="t d">',
           f'<title id="t">{escape(item["title"])}: low-fidelity design</title>',
           '<desc id="d">Three-stage screen or production design. It is an editable reference, not a functioning application.</desc>',
           '<rect width="1440" height="860" fill="#F3F5F8"/>',
           f'<text x="60" y="70" font-size="32" fill="{NAVY}" font-family="Segoe UI,Arial,sans-serif">{escape(item["title"])}</text>',
           f'<text x="60" y="110" font-size="17" fill="{STEEL}" font-family="Segoe UI,Arial,sans-serif">LOW-FIDELITY DESIGN / NOT A LIVE APPLICATION</text>']
    scene = [("text", 60, 35, item["title"], 32, True, NAVY),
             ("text", 60, 87, "LOW-FIDELITY DESIGN / NOT A LIVE APPLICATION", 17, False, STEEL)]
    for i, (name, fields) in enumerate(item["design"]):
        x, y = 60+i*455, 160
        scene.append(("rect", x, y, 410, 600, "#FFFFFF", LINE))
        scene.append(("rect", x, y, 410, 65, NAVY, NAVY))
        scene.append(("text", x+24, y+18, f"0{i+1} / {name}", 22, True, "#FFFFFF"))
        svg.append(f'<rect x="{x}" y="{y}" width="410" height="600" rx="8" fill="white" stroke="{LINE}"/>')
        svg.append(f'<rect x="{x}" y="{y}" width="410" height="65" fill="{NAVY}"/>')
        svg.append(f'<text x="{x+24}" y="{y+43}" font-size="22" fill="white" font-family="Segoe UI,Arial,sans-serif">{escape(name)}</text>')
        for j, field in enumerate(fields):
            fy = y+103+j*104
            scene.append(("rect", x+24, fy, 362, 78, MIST, LINE))
            svg.append(f'<rect x="{x+24}" y="{fy}" width="362" height="78" rx="3" fill="{MIST}" stroke="{LINE}"/>')
            for k, line in enumerate(text_lines(field, 324, 18)):
                scene.append(("text", x+42, fy+22+k*23, line, 18, False, NAVY))
                svg.append(f'<text x="{x+42}" y="{fy+43+k*23}" font-size="18" fill="{NAVY}" font-family="Segoe UI,Arial,sans-serif">{escape(line)}</text>')
    svg.append("</svg>")
    (directory / "design.svg").write_text("\n".join(svg))
    render_scene(scene, 1440, 860, directory / "design")


def course_poster(lessons, phases, assets):
    width, height = 1400, 1950
    scene = [("rect", 0, 0, width, 460, NAVY, NAVY),
             ("text", 80, 65, "AI / in practice", 88, True, "#FFFFFF"),
             ("text", 84, 192, "Understand. Direct. Create. Connect. Apply. Deliver.", 28, False, "#B9C2D3"),
             ("text", 84, 280, "24 weeks", 48, True, GOLD),
             ("text", 520, 280, "144 hours", 48, True, GOLD),
             ("text", 970, 280, "6 project paths", 42, True, GOLD),
             ("text", 84, 380, "No programming prerequisite. Evidence before confidence.", 25, False, "#FFFFFF")]
    for i, phase in enumerate(phases):
        y = 505 + i*215
        scene.append(("rect", 80, y, 1240, 185, MIST, LINE))
        scene.append(("text", 110, y+22, phase[0].upper(), 23, True, DEEP_GOLD))
        scene.append(("text", 110, y+66, f"WEEKS {phase[1]}", 20, False, STEEL))
        for j, item in enumerate(lessons[i*4:i*4+4]):
            lines = text_lines(f"{item['week']:02d} / {item['title']}", 900, 23)
            scene.append(("text", 390, y+18+j*39, lines[0], 23, False, NAVY))
    scene.append(("text", 80, 1840, "Professional practice first. Optional coding track separately scoped.", 25, False, NAVY))
    scene.append(("text", 80, 1890, "TEACHING DRAFT / NOT ACCREDITATION OR DEPLOYMENT AUTHORISATION", 18, False, STEEL))
    render_scene(scene, width, height, assets / "course-map")

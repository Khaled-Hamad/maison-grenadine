const fs = require("node:fs");
const MarkdownIt = require("markdown-it");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Footer, PageNumber, HeadingLevel, WidthType, ShadingType,
  BorderStyle, LevelFormat, ExternalHyperlink, AlignmentType,
} = require("docx");

const md = new MarkdownIt({ html: false });
const C = { navy: "182234", gold: "806226", mist: "F3F5F8", line: "DDE2EA", steel: "3D4A63" };
const width = 9072;

function inline(children = []) {
  const result = [];
  let bold = false;
  let italic = false;
  let link;
  for (const token of children) {
    if (token.type === "strong_open") { bold = true; continue; }
    if (token.type === "strong_close") { bold = false; continue; }
    if (token.type === "em_open") { italic = true; continue; }
    if (token.type === "em_close") { italic = false; continue; }
    if (token.type === "link_open") { link = token.attrGet("href"); continue; }
    if (token.type === "link_close") { link = undefined; continue; }
    if (["softbreak", "hardbreak"].includes(token.type)) {
      result.push(new TextRun({ break: 1 }));
      continue;
    }
    if (!["text", "code_inline", "html_inline"].includes(token.type)) continue;
    const options = { text: token.content, bold, italics: italic };
    if (token.type === "code_inline") Object.assign(options, { font: "Consolas", size: 19, shading: { fill: C.mist } });
    if (link && /^https?:\/\//.test(link)) {
      result.push(new ExternalHyperlink({
        link, children: [new TextRun({ ...options, color: C.gold, underline: {} })],
      }));
    } else {
      result.push(new TextRun(options));
    }
  }
  return result.length ? result : [new TextRun("")];
}

function parseTable(tokens, start) {
  const rows = [];
  let values = [];
  let i = start + 1;
  for (; i < tokens.length && tokens[i].type !== "table_close"; i++) {
    const token = tokens[i];
    if (token.type === "tr_open") values = [];
    if (token.type === "inline") values.push({
      runs: inline(token.children),
      plain: (token.children || []).filter((child) => ["text", "code_inline"].includes(child.type)).map((child) => child.content).join(""),
    });
    if (token.type === "tr_close") rows.push(values);
  }
  const count = Math.max(...rows.map((r) => r.length));
  const sizes = Array.from({ length: count }, (_, n) => Math.floor(width / count) + (n === count - 1 ? width % count : 0));
  const border = { style: BorderStyle.SINGLE, size: 3, color: C.line };
  const table = new Table({
    width: { size: width, type: WidthType.DXA }, columnWidths: sizes,
    rows: rows.map((row, r) => new TableRow({
      tableHeader: r === 0,
      children: Array.from({ length: count }, (_, col) => new TableCell({
        width: { size: sizes[col], type: WidthType.DXA },
        margins: { top: 90, bottom: 90, left: 110, right: 110 },
        borders: { top: border, bottom: border, left: border, right: border },
        shading: { fill: r === 0 ? C.navy : r % 2 ? C.mist : "FFFFFF", type: ShadingType.CLEAR },
        children: [new Paragraph({
          spacing: { after: 40 },
          children: r === 0
            ? [new TextRun({ text: row[col]?.plain || "", bold: true, color: "FFFFFF", size: 19 })]
            : (row[col]?.runs || [new TextRun("")]),
        })],
      })),
    })),
  });
  return [table, i];
}

function blocks(markdown) {
  const tokens = md.parse(markdown, {});
  const output = [];
  const lists = [];
  let listInstance = 0;
  let skippedFirstTitle = false;
  for (let i = 0; i < tokens.length; i++) {
    const token = tokens[i];
    if (token.type === "table_open") {
      const [table, consumed] = parseTable(tokens, i);
      output.push(table, new Paragraph({ spacing: { after: 100 }, text: "" }));
      i = consumed;
      continue;
    }
    if (token.type === "heading_open") {
      const content = tokens[i + 1];
      if (token.tag === "h1" && !skippedFirstTitle) {
        skippedFirstTitle = true;
        i += 2;
        continue;
      }
      const level = Number(token.tag.slice(1));
      output.push(new Paragraph({
        heading: level <= 2 ? HeadingLevel.HEADING_1 : level === 3 ? HeadingLevel.HEADING_2 : HeadingLevel.HEADING_3,
        children: inline(content.children),
      }));
      i += 2;
      continue;
    }
    if (token.type === "bullet_list_open" || token.type === "ordered_list_open") {
      lists.push({ reference: token.type === "ordered_list_open" ? "steps" : "bullets", instance: ++listInstance });
      continue;
    }
    if (token.type === "bullet_list_close" || token.type === "ordered_list_close") {
      lists.pop();
      continue;
    }
    if (token.type === "paragraph_open" && tokens[i + 1]?.type === "inline") {
      output.push(new Paragraph({
        ...(lists.length ? { numbering: { ...lists[lists.length - 1], level: Math.min(lists.length - 1, 2) } } : {}),
        children: inline(tokens[i + 1].children),
      }));
      i += 2;
      continue;
    }
    if (token.type === "fence" || token.type === "code_block") {
      for (const line of token.content.trimEnd().split("\n")) {
        output.push(new Paragraph({
          shading: { fill: C.mist }, spacing: { after: 0 },
          children: [new TextRun({ text: line || " ", font: "Consolas", size: 18 })],
        }));
      }
      output.push(new Paragraph({ text: "", spacing: { after: 80 } }));
    }
  }
  return output;
}

async function main() {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
  for (const job of jobs) {
    const content = fs.readFileSync(job.source, "utf8");
    const numbering = ["bullets", "steps"].map((reference) => ({
      reference,
      levels: [0, 1, 2].map((level) => ({
        level, format: reference === "bullets" ? LevelFormat.BULLET : LevelFormat.DECIMAL,
        text: reference === "bullets" ? "\u2022" : `%${level + 1}.`,
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 420 + level * 300, hanging: 220 } } },
      })),
    }));
    const doc = new Document({
      title: job.title, creator: "Khaled Hamad",
      description: "Teaching draft. Not professional accreditation or production-release authorisation.",
      numbering: { config: numbering },
      styles: {
        default: { document: { run: { font: "Segoe UI", size: 21, color: C.navy },
          paragraph: { spacing: { after: 120, line: 280 } } } },
        paragraphStyles: [
          { id: "Title", name: "Title", basedOn: "Normal", next: "Normal",
            run: { font: "Segoe UI Semibold", size: 60, bold: true, color: C.navy },
            paragraph: { spacing: { before: 160, after: 220 }, keepNext: true } },
          { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
            run: { font: "Segoe UI Semibold", size: 40, bold: true, color: C.navy },
            paragraph: { outlineLevel: 0, spacing: { before: 300, after: 140 }, keepNext: true } },
          { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
            run: { font: "Segoe UI Semibold", size: 26, bold: true, color: C.gold },
            paragraph: { outlineLevel: 1, spacing: { before: 220, after: 100 }, keepNext: true } },
          { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
            run: { font: "Segoe UI Semibold", size: 22, bold: true },
            paragraph: { outlineLevel: 2, spacing: { before: 180, after: 80 }, keepNext: true } },
        ],
      },
      sections: [{
        properties: { page: { size: { width: 11906, height: 16838 },
          margin: { top: 1701, right: 1417, bottom: 1417, left: 1417, header: 720, footer: 720 } } },
        footers: { default: new Footer({ children: [new Paragraph({
          children: [new TextRun({ text: "AI / Professional Practice    |    Teaching draft    |    ", size: 17, color: C.steel }),
            new TextRun({ children: [PageNumber.CURRENT], size: 17 })],
        })] }) },
        children: [
          new Paragraph({ children: [new TextRun({ text: "AI ENABLEMENT & TRAINING", color: C.gold, bold: true, size: 20 })] }),
          new Paragraph({ style: "Title", children: [new TextRun(job.title)] }),
          new Paragraph({ children: [new TextRun({ text: "Full curriculum edition · 18 November 2026", color: C.steel })] }),
          new Paragraph({ children: [new TextRun({ text: "Teaching draft. Verify current tools, permissions and professional requirements before delivery or release.", italics: true })] }),
          ...blocks(content),
        ],
      }],
    });
    fs.writeFileSync(job.output, await Packer.toBuffer(doc));
    console.log(`Word: ${job.id}`);
  }
}

main().catch((error) => { console.error(error); process.exitCode = 1; });

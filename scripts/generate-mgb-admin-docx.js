const fs = require("fs");
const path = require("path");
const {
  AlignmentType,
  BorderStyle,
  Document,
  ExternalHyperlink,
  Footer,
  Header,
  HeadingLevel,
  LevelFormat,
  Packer,
  PageNumber,
  Paragraph,
  TextRun,
} = require("docx");

const repo = path.resolve(__dirname, "..");
const sourceDir = path.join(repo, "docs", "submission", "administrative");
const outputDir = path.join(sourceDir, "word");
const documents = [
  "01-mgb-research-management-intake",
];

function textRuns(line) {
  if (/^https:\/\//.test(line)) {
    return [
      new ExternalHyperlink({
        link: line,
        children: [new TextRun({ text: line, style: "Hyperlink" })],
      }),
    ];
  }

  const labeledUrl = line.match(/^([^:]{1,55}:) (https:\/\/\S+)$/);
  if (labeledUrl) {
    return [
      new TextRun({ text: `${labeledUrl[1]} `, bold: true }),
      new ExternalHyperlink({
        link: labeledUrl[2],
        children: [new TextRun({ text: labeledUrl[2], style: "Hyperlink" })],
      }),
    ];
  }

  const labeled = line.match(/^([^:]{1,55}:)(.*)$/);
  if (labeled) {
    return [
      new TextRun({ text: labeled[1], bold: true }),
      new TextRun({ text: labeled[2] }),
    ];
  }
  return [new TextRun(line)];
}

function parseMarkdown(markdown) {
  const children = [];
  for (const rawLine of markdown.replace(/\r/g, "").split("\n")) {
    const line = rawLine.trimEnd();
    if (!line) {
      continue;
    } else if (line.startsWith("# ")) {
      children.push(
        new Paragraph({
          style: "PacketTitle",
          children: [new TextRun(line.slice(2))],
          border: {
            bottom: { style: BorderStyle.SINGLE, size: 10, color: "1F49B6", space: 6 },
          },
        }),
      );
    } else if (line.startsWith("## ")) {
      children.push(
        new Paragraph({
          heading: HeadingLevel.HEADING_1,
          children: [new TextRun(line.slice(3))],
        }),
      );
    } else if (line.startsWith("### ")) {
      children.push(
        new Paragraph({
          heading: HeadingLevel.HEADING_2,
          children: [new TextRun(line.slice(4))],
        }),
      );
    } else if (line.startsWith("- [ ] ")) {
      children.push(
        new Paragraph({
          style: "Normal",
          indent: { left: 280 },
          spacing: { after: 100, line: 264 },
          children: textRuns(line.slice(2)),
        }),
      );
    } else if (line.startsWith("- ")) {
      children.push(
        new Paragraph({
          numbering: { reference: "packet-bullets", level: 0 },
          children: textRuns(line.slice(2)),
        }),
      );
    } else {
      children.push(new Paragraph({ children: textRuns(line) }));
    }
  }
  return children;
}

function buildDocument(markdown, filename) {
  return new Document({
    creator: "Open Clinical Learning Commons",
    title: filename,
    description: "Draft for Mass General Brigham Research Management review",
    numbering: {
      config: [
        {
          reference: "packet-bullets",
          levels: [
            {
              level: 0,
              format: LevelFormat.BULLET,
              text: "•",
              alignment: AlignmentType.LEFT,
              style: { paragraph: { indent: { left: 540, hanging: 260 } } },
            },
          ],
        },
      ],
    },
    styles: {
      default: {
        document: {
          run: { font: "Arial", size: 22, color: "202938" },
          paragraph: { spacing: { after: 100, line: 264 } },
        },
      },
      paragraphStyles: [
        {
          id: "PacketTitle",
          name: "Packet Title",
          basedOn: "Normal",
          next: "Normal",
          quickFormat: true,
          run: { font: "Arial", size: 34, bold: true, color: "111827" },
          paragraph: { spacing: { after: 180 }, keepNext: true },
        },
        {
          id: "Heading1",
          name: "Heading 1",
          basedOn: "Normal",
          next: "Normal",
          quickFormat: true,
          run: { font: "Arial", size: 27, bold: true, color: "1F49B6" },
          paragraph: { spacing: { before: 180, after: 80 }, keepNext: true, outlineLevel: 0 },
        },
        {
          id: "Heading2",
          name: "Heading 2",
          basedOn: "Normal",
          next: "Normal",
          quickFormat: true,
          run: { font: "Arial", size: 23, bold: true, color: "334155" },
          paragraph: { spacing: { before: 180, after: 80 }, keepNext: true, outlineLevel: 1 },
        },
      ],
    },
    sections: [
      {
        properties: {
          page: {
            size: { width: 12240, height: 15840 },
            margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
          },
        },
        headers: {
          default: new Header({
            children: [
              new Paragraph({
                alignment: AlignmentType.RIGHT,
                children: [
                  new TextRun({
                    text: "NIH Nutrition Education Challenge | MGB administrative intake",
                    size: 17,
                    color: "64748B",
                  }),
                ],
              }),
            ],
          }),
        },
        footers: {
          default: new Footer({
            children: [
              new Paragraph({
                alignment: AlignmentType.RIGHT,
                children: [
                  new TextRun({ text: "September 1, 2026 | Page ", size: 17, color: "64748B" }),
                  new TextRun({ children: [PageNumber.CURRENT], size: 17, color: "64748B" }),
                ],
              }),
            ],
          }),
        },
        children: parseMarkdown(markdown),
      },
    ],
  });
}

async function main() {
  fs.mkdirSync(outputDir, { recursive: true });
  for (const name of documents) {
    const markdown = fs.readFileSync(path.join(sourceDir, `${name}.md`), "utf8");
    const buffer = await Packer.toBuffer(buildDocument(markdown, name));
    fs.writeFileSync(path.join(outputDir, `${name}.docx`), buffer);
  }
  process.stdout.write(`Generated ${documents.length} Word document in ${outputDir}\n`);
}

main().catch((error) => {
  process.stderr.write(`${error.stack || error}\n`);
  process.exitCode = 1;
});

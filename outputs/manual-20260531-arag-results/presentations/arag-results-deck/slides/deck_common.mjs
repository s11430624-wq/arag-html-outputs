export const COLORS = {
  ink: "#1F2937",
  muted: "#6B7280",
  line: "#D9E1F2",
  bg: "#FFFFFF",
  blue: "#4E79E7",
  blueSoft: "#EEF4FF",
  teal: "#4FB697",
  tealSoft: "#EEF9F6",
  orange: "#E7A94C",
  orangeSoft: "#FFF6E9",
  purple: "#8E7CF3",
  purpleSoft: "#F4F1FF",
  rose: "#DA8B98",
  roseSoft: "#FFF1F3",
};

export function addChrome(slide, ctx, { page, total }) {
  slide.background.fill = COLORS.bg;
  ctx.addText(slide, {
    x: 22, y: 16, w: 180, h: 18,
    text: "A-RAG Paper Report",
    fontSize: 11,
    color: "#8B95A7",
    face: "Aptos",
  });
  ctx.addText(slide, {
    x: ctx.W - 88, y: 16, w: 68, h: 18,
    text: `${String(page).padStart(2, "0")} / ${String(total).padStart(2, "0")}`,
    fontSize: 11,
    color: "#9AA3B2",
    align: "right",
    face: "Aptos",
  });
}

export function addTitleBlock(slide, ctx, { title, subtitle = "", color = COLORS.blue }) {
  ctx.addText(slide, {
    x: 44, y: 54, w: 950, h: 42,
    text: title,
    fontSize: 28,
    bold: true,
    color: COLORS.ink,
    face: "Aptos",
  });
  if (subtitle) {
    ctx.addText(slide, {
      x: 44, y: 92, w: 900, h: 22,
      text: subtitle,
      fontSize: 13,
      color: "#7A8496",
      face: "Aptos",
    });
  }
  ctx.addShape(slide, {
    x: 44, y: 122, w: 660, h: 3,
    fill: color,
    line: ctx.line(color, 0),
  });
}

export function addCard(slide, ctx, { x, y, w, h, title, bodyLines = [], color = COLORS.blue, soft = COLORS.blueSoft }) {
  const shape = ctx.addShape(slide, {
    x, y, w, h,
    fill: soft,
    line: ctx.line(color, 1.2),
  });
  shape.borderRadius = 12;
  if (title) {
    ctx.addText(slide, {
      x: x + 18, y: y + 16, w: w - 36, h: 24,
      text: title,
      fontSize: 16,
      bold: true,
      color,
    });
  }
  let lineY = y + 48;
  for (const line of bodyLines) {
    ctx.addText(slide, {
      x: x + 18, y: lineY, w: w - 36, h: 20,
      text: line,
      fontSize: 13,
      color: COLORS.ink,
    });
    lineY += 20;
  }
}

export function addBulletList(slide, ctx, { x, y, w, items, color = COLORS.blue, fontSize = 15, gap = 28 }) {
  items.forEach((item, index) => {
    const top = y + index * gap;
    ctx.addShape(slide, {
      x, y: top + 7, w: 8, h: 8,
      fill: color,
      line: ctx.line(color, 0),
      geometry: "ellipse",
    });
    ctx.addText(slide, {
      x: x + 18, y: top, w: w - 18, h: gap,
      text: item,
      fontSize,
      color: COLORS.ink,
    });
  });
}

export function addTable(slide, ctx, { x, y, colWidths, rowHeight = 42, headers = [], rows = [], headerFill = COLORS.blueSoft, headerColor = COLORS.blue, fontSize = 13 }) {
  const totalWidth = colWidths.reduce((a, b) => a + b, 0);
  const totalHeight = rowHeight * (rows.length + 1);
  const outer = ctx.addShape(slide, {
    x, y, w: totalWidth, h: totalHeight,
    fill: "#FFFFFF",
    line: ctx.line(COLORS.line, 1),
  });
  outer.borderRadius = 6;

  // header bg
  let offsetX = x;
  headers.forEach((header, idx) => {
    const w = colWidths[idx];
    const cell = ctx.addShape(slide, {
      x: offsetX, y, w, h: rowHeight,
      fill: headerFill,
      line: ctx.line(COLORS.line, 1),
    });
    if (idx === 0 || idx === headers.length - 1) cell.borderRadius = 6;
    ctx.addText(slide, {
      x: offsetX + 10, y: y + 10, w: w - 20, h: rowHeight - 12,
      text: header,
      fontSize,
      bold: true,
      color: headerColor,
      align: idx === 0 ? "left" : "center",
      valign: "middle",
    });
    offsetX += w;
  });

  rows.forEach((row, rIdx) => {
    let cellX = x;
    const top = y + rowHeight * (rIdx + 1);
    row.forEach((value, cIdx) => {
      const w = colWidths[cIdx];
      ctx.addShape(slide, {
        x: cellX, y: top, w, h: rowHeight,
        fill: "#FFFFFF",
        line: ctx.line(COLORS.line, 1),
      });
      ctx.addText(slide, {
        x: cellX + 10, y: top + 9, w: w - 20, h: rowHeight - 12,
        text: String(value),
        fontSize,
        color: COLORS.ink,
        align: cIdx === 0 ? "left" : "center",
        valign: "middle",
      });
      cellX += w;
    });
  });
}

export function addMiniMetric(slide, ctx, { x, y, w, h, label, value, note, color = COLORS.blue, soft = COLORS.blueSoft }) {
  const shape = ctx.addShape(slide, {
    x, y, w, h,
    fill: soft,
    line: ctx.line(color, 1.2),
  });
  shape.borderRadius = 10;
  ctx.addText(slide, { x: x + 14, y: y + 12, w: w - 28, h: 20, text: label, fontSize: 13, color, bold: true });
  ctx.addText(slide, { x: x + 14, y: y + 40, w: w - 28, h: 34, text: value, fontSize: 24, color: COLORS.ink, bold: true });
  if (note) {
    ctx.addText(slide, { x: x + 14, y: y + h - 28, w: w - 28, h: 18, text: note, fontSize: 11, color: COLORS.muted });
  }
}

export function addHorizontalBars(slide, ctx, { x, y, w, labels, values, maxValue = 100, color = COLORS.blue }) {
  const rowGap = 52;
  labels.forEach((label, idx) => {
    const top = y + idx * rowGap;
    ctx.addText(slide, {
      x, y: top, w: 200, h: 18,
      text: label,
      fontSize: 13,
      color: COLORS.ink,
    });
    ctx.addShape(slide, {
      x, y: top + 24, w, h: 12,
      fill: "#EEF2F7",
      line: ctx.line("#EEF2F7", 0),
    });
    const barW = Math.max(6, (values[idx] / maxValue) * w);
    ctx.addShape(slide, {
      x, y: top + 24, w: barW, h: 12,
      fill: color,
      line: ctx.line(color, 0),
    });
    ctx.addText(slide, {
      x: x + w + 12, y: top + 18, w: 70, h: 18,
      text: `${values[idx].toFixed(2)}`,
      fontSize: 12,
      color: color,
      bold: true,
    });
  });
}

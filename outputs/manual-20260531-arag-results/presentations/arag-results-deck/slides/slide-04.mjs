import { addBulletList, addChrome, addTable, addTitleBlock, COLORS } from "./deck_common.mjs";

export async function slide04(presentation, ctx) {
  const slide = presentation.slides.add();
  addChrome(slide, ctx, { page: 4, total: 7 });
  addTitleBlock(slide, ctx, {
    title: "主結果：LLM Accuracy",
    subtitle: "在固定方法與參數設定下，A-RAG (Full) 在三個資料集上都優於 A-RAG (Naive)。",
    color: COLORS.blue,
  });

  addTable(slide, ctx, {
    x: 54, y: 165,
    colWidths: [278, 160, 160, 170],
    rowHeight: 46,
    headers: ["Setting", "MuSiQue", "HotpotQA", "2Wiki"],
    rows: [
      ["Paper Naive RAG", "52.8", "81.2", "50.2"],
      ["Paper A-RAG (Naive)", "66.2", "90.8", "70.6"],
      ["Paper A-RAG (Full)", "74.1", "94.5", "89.7"],
      ["Your A-RAG (Naive)", "71.0", "85.0", "76.0"],
      ["Your A-RAG (Full)", "87.88", "97.0", "97.0"],
    ],
    headerFill: COLORS.blueSoft,
    headerColor: COLORS.blue,
    fontSize: 13,
  });

  addBulletList(slide, ctx, {
    x: 900, y: 192, w: 280,
    color: COLORS.teal,
    items: [
      "A-RAG (Full) 在三組都優於 A-RAG (Naive)。",
      "HotpotQA 與 2Wiki 的 A-RAG (Full) 都到 97.0。",
      "MuSiQue 仍然是最能拉開方法差異的資料集。",
    ],
    fontSize: 15,
    gap: 52,
  });

  ctx.addText(slide, {
    x: 54, y: 466, w: 1120, h: 24,
    text: "解讀：這張表回答的是「在相同方法設定下，哪個變體表現更好」，而不是不同模型供應商的嚴格對決。",
    fontSize: 12,
    color: COLORS.muted,
  });

  ctx.addShape(slide, {
    x: 54, y: 534, w: 1140, h: 96,
    fill: COLORS.tealSoft,
    line: ctx.line(COLORS.teal, 1.2),
  }).borderRadius = 12;
  ctx.addText(slide, {
    x: 74, y: 556, w: 1090, h: 54,
    text: "Takeaway\n在目前保留的三個 benchmark 上，A-RAG 的主結果表已經穩定成形，足以支撐後續的效率分析與消融實驗。",
    fontSize: 18,
    bold: true,
    color: COLORS.ink,
  });
  return slide;
}

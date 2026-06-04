import { addChrome, addMiniMetric, addTable, addTitleBlock, COLORS } from "./deck_common.mjs";

export async function slide05(presentation, ctx) {
  const slide = presentation.slides.add();
  addChrome(slide, ctx, { page: 5, total: 7 });
  addTitleBlock(slide, ctx, {
    title: "Contain Accuracy 與 Efficiency Readout",
    subtitle: "一頁補足字串比對與檢索成本，避免只看主結果而忽略 test-time 行為。",
    color: COLORS.purple,
  });

  addTable(slide, ctx, {
    x: 54, y: 162,
    colWidths: [278, 160, 160, 170],
    rowHeight: 42,
    headers: ["Setting", "MuSiQue", "HotpotQA", "2Wiki"],
    rows: [
      ["Paper Naive RAG", "48.7", "79.5", "66.5"],
      ["Paper A-RAG (Naive)", "59.7", "85.3", "76.9"],
      ["Paper A-RAG (Full)", "65.3", "88.0", "88.9"],
      ["Your A-RAG (Naive)", "66.0", "75.0", "74.0"],
      ["Your A-RAG (Full)", "82.83", "92.0", "94.0"],
    ],
    headerFill: COLORS.purpleSoft,
    headerColor: COLORS.purple,
    fontSize: 12,
  });

  addMiniMetric(slide, ctx, {
    x: 898, y: 182, w: 282, h: 102,
    label: "MuSiQue / A-RAG Full",
    value: "7.31 loops",
    note: "avg retrieved tokens = 4245.6",
    color: COLORS.blue,
    soft: COLORS.blueSoft,
  });
  addMiniMetric(slide, ctx, {
    x: 898, y: 302, w: 282, h: 102,
    label: "HotpotQA / A-RAG Full",
    value: "$0.0136 / Q",
    note: "avg loops = 4.89",
    color: COLORS.teal,
    soft: COLORS.tealSoft,
  });
  addMiniMetric(slide, ctx, {
    x: 898, y: 422, w: 282, h: 102,
    label: "2Wiki / A-RAG Full",
    value: "2368.7 tokens",
    note: "avg cost = $0.01365",
    color: COLORS.orange,
    soft: COLORS.orangeSoft,
  });

  addTable(slide, ctx, {
    x: 54, y: 440,
    colWidths: [220, 160, 120, 140, 180],
    rowHeight: 40,
    headers: ["Setting", "Dataset", "Avg Loops", "Avg Cost / Q", "Avg Retrieved Tokens"],
    rows: [
      ["Naive RAG", "MuSiQue", "1.0", "0.004498", "4361.0"],
      ["A-RAG (Naive)", "HotpotQA", "6.89", "0.021215", "2449.7"],
      ["A-RAG (Full)", "2Wiki", "5.08", "0.01365", "2368.7"],
    ],
    headerFill: COLORS.orangeSoft,
    headerColor: COLORS.orange,
    fontSize: 12,
  });

  ctx.addText(slide, {
    x: 900, y: 566, w: 280, h: 42,
    text: "Efficiency takeaway\nNaive 最便宜；A-RAG Full 在 HotpotQA / 2Wiki 的 cost 已低於 A-RAG (Naive)。",
    fontSize: 13,
    color: COLORS.ink,
  });

  ctx.addText(slide, {
    x: 54, y: 633, w: 1140, h: 20,
    text: "註：retrieved tokens 只反映 agent 讀進 context 的文字量，不是完整 API billing token breakdown。",
    fontSize: 11,
    color: COLORS.muted,
  });
  return slide;
}

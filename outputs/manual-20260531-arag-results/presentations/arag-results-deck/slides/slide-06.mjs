import { addBulletList, addChrome, addHorizontalBars, addTable, addTitleBlock, COLORS } from "./deck_common.mjs";

export async function slide06(presentation, ctx) {
  const slide = presentation.slides.add();
  addChrome(slide, ctx, { page: 6, total: 7 });
  addTitleBlock(slide, ctx, {
    title: "MuSiQue 消融：哪個工具最重要",
    subtitle: "在最難的資料集上比較 Full 與三種 ablation，直接觀察 A-RAG 工具組的必要性。",
    color: COLORS.teal,
  });

  addTable(slide, ctx, {
    x: 52, y: 168,
    colWidths: [240, 110, 110, 110, 150, 120],
    rowHeight: 42,
    headers: ["Variant", "LLM Acc.", "Contain", "Avg Loops", "Avg Retrieved", "Avg Cost / Q"],
    rows: [
      ["A-RAG (Full)", "87.88", "82.83", "7.31", "4245.6", "0.027867"],
      ["w/o keyword_search", "67.68", "62.63", "7.44", "2938.6", "0.025791"],
      ["w/o semantic_search", "74.49", "71.43", "7.04", "3009.0", "0.02501"],
      ["w/o chunk_read", "65.66", "64.65", "6.88", "1722.5", "0.018767"],
    ],
    headerFill: COLORS.tealSoft,
    headerColor: COLORS.teal,
    fontSize: 12,
  });

  addHorizontalBars(slide, ctx, {
    x: 900, y: 220, w: 210,
    labels: ["Full", "w/o keyword", "w/o semantic", "w/o chunk"],
    values: [87.88, 67.68, 74.49, 65.66],
    maxValue: 100,
    color: COLORS.blue,
  });

  addBulletList(slide, ctx, {
    x: 900, y: 464, w: 270,
    color: COLORS.orange,
    items: [
      "Full 仍然是最強設定。",
      "拿掉 semantic_search 最不傷。",
      "拿掉 keyword_search 與 chunk_read 都有明顯掉分。",
    ],
    fontSize: 15,
    gap: 38,
  });
  return slide;
}

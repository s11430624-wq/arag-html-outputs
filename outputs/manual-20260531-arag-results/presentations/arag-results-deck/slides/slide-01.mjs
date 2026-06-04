import { addBulletList, addCard, addChrome, addTitleBlock, COLORS } from "./deck_common.mjs";

export async function slide01(presentation, ctx) {
  const slide = presentation.slides.add();
  addChrome(slide, ctx, { page: 1, total: 7 });
  addTitleBlock(slide, ctx, {
    title: "A-RAG 官方實驗結果整理",
    subtitle: "A-RAG on MuSiQue, HotpotQA, and 2WikiMultiHop",
    color: COLORS.blue,
  });

  ctx.addText(slide, {
    x: 44, y: 166, w: 770, h: 46,
    text: "本 deck 聚焦於 A-RAG 在三個多跳 benchmark 上的實驗結果，整理資料集範圍、方法設定、關鍵參數、主結果與 MuSiQue 消融分析。",
    fontSize: 17,
    color: COLORS.ink,
  });

  addCard(slide, ctx, {
    x: 46, y: 246, w: 350, h: 162,
    title: "這次保留的實驗",
    bodyLines: [
      "MuSiQue / HotpotQA / 2WikiMultiHop",
      "Naive RAG / A-RAG (Naive) / A-RAG (Full)",
      "MuSiQue 工具級消融實驗",
    ],
    color: COLORS.teal,
    soft: COLORS.tealSoft,
  });

  addCard(slide, ctx, {
    x: 426, y: 246, w: 350, h: 162,
    title: "這份 deck 的重點",
    bodyLines: [
      "資料集範圍與實驗單位",
      "方法流程與關鍵參數設定",
      "主結果、效率與 MuSiQue 消融",
    ],
    color: COLORS.blue,
    soft: COLORS.blueSoft,
  });

  addBulletList(slide, ctx, {
    x: 850, y: 238, w: 360,
    color: COLORS.orange,
    items: [
      "用一致的方法設定完成 batch run",
      "以固定參數比較不同方法變體",
      "結果頁聚焦可保留、可報告的正式數據",
    ],
    fontSize: 15,
    gap: 34,
  });

  ctx.addText(slide, {
    x: 44, y: 640, w: 1180, h: 20,
    text: "定位：這份 deck 是結果整理版，不重新解釋整篇論文內容，而是補齊方法設定與實驗 readout。",
    fontSize: 11,
    color: "#8A94A6",
  });
  return slide;
}

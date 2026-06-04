import { addBulletList, addCard, addChrome, addTitleBlock, COLORS } from "./deck_common.mjs";

export async function slide02(presentation, ctx) {
  const slide = presentation.slides.add();
  addChrome(slide, ctx, { page: 2, total: 7 });
  addTitleBlock(slide, ctx, {
    title: "資料集範圍與實驗單位",
    subtitle: "目前正式保留三個 benchmark，各自固定 100 題子集進行對照。",
    color: COLORS.teal,
  });

  addCard(slide, ctx, {
    x: 46, y: 162, w: 360, h: 170,
    title: "MuSiQue",
    bodyLines: [
      "Question count: 100",
      "Task type: multi-hop QA",
      "難度最高，也用來做消融實驗",
    ],
    color: COLORS.blue,
    soft: COLORS.blueSoft,
  });
  addCard(slide, ctx, {
    x: 460, y: 162, w: 360, h: 170,
    title: "HotpotQA",
    bodyLines: [
      "Question count: 100",
      "Task type: multi-hop QA",
      "目前主結果中數值最穩定的一組",
    ],
    color: COLORS.orange,
    soft: COLORS.orangeSoft,
  });
  addCard(slide, ctx, {
    x: 874, y: 162, w: 360, h: 170,
    title: "2WikiMultiHop",
    bodyLines: [
      "Question count: 100",
      "Task type: multi-hop QA",
      "和 HotpotQA 一起形成主要比較軸",
    ],
    color: COLORS.purple,
    soft: COLORS.purpleSoft,
  });

  addCard(slide, ctx, {
    x: 46, y: 380, w: 528, h: 194,
    title: "為什麼先做這三個",
    bodyLines: [
      "1. 都屬於多跳問答，和 A-RAG 的方法設計最直接對齊。",
      "2. 已完成 Naive / A-RAG (Naive) / A-RAG (Full) 的正式跑法。",
      "3. 已有可直接對照論文表格的公開數字。",
    ],
    color: COLORS.teal,
    soft: COLORS.tealSoft,
  });

  addBulletList(slide, ctx, {
    x: 642, y: 398, w: 540,
    color: COLORS.rose,
    items: [
      "本輪不含 Medical / Novel。",
      "不再納入 N8N、Eighty Days、FanOutQA 等 exploratory/custom datasets。",
      "所有後續圖表只以目前保留的正式結果為準。",
    ],
    fontSize: 15,
    gap: 36,
  });

  ctx.addText(slide, {
    x: 46, y: 630, w: 1180, h: 20,
    text: "實驗單位：每個 benchmark 先固定 100 題，目的是建立穩定的三資料集對照，再延伸到效率與消融分析。",
    fontSize: 11,
    color: "#8A94A6",
  });
  return slide;
}

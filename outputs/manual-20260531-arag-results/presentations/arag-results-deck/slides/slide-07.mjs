import { addCard, addChrome, addTitleBlock, COLORS } from "./deck_common.mjs";

export async function slide07(presentation, ctx) {
  const slide = presentation.slides.add();
  addChrome(slide, ctx, { page: 7, total: 7 });
  addTitleBlock(slide, ctx, {
    title: "總結",
    subtitle: "把這輪方法實驗的結論收斂成三件事：可用、可比、可解釋。",
    color: COLORS.orange,
  });

  addCard(slide, ctx, {
    x: 54, y: 176, w: 360, h: 220,
    title: "1. 主結果已成形",
    bodyLines: [
      "三個 benchmark 都已有 Naive / A-RAG (Naive) / A-RAG (Full)。",
      "A-RAG (Full) 在三組的 LLM Accuracy 都是目前最佳。",
      "這部分已足夠支撐報告中的主實驗段落。",
    ],
    color: COLORS.blue,
    soft: COLORS.blueSoft,
  });

  addCard(slide, ctx, {
    x: 458, y: 176, w: 360, h: 220,
    title: "2. 不只看 accuracy",
    bodyLines: [
      "Contain Accuracy 補上更嚴格的字串對齊視角。",
      "Efficiency 表則把 loops / retrieved tokens / cost 一起納入。",
      "這讓結果比較不會只剩一個漂亮數字。",
    ],
    color: COLORS.teal,
    soft: COLORS.tealSoft,
  });

  addCard(slide, ctx, {
    x: 862, y: 176, w: 360, h: 220,
    title: "3. 消融能解釋方法價值",
    bodyLines: [
      "MuSiQue 消融顯示 keyword_search 與 chunk_read 對 Full 設定很重要。",
      "semantic_search 也有貢獻，但拿掉後跌幅相對較小。",
      "這是目前最能支撐 A-RAG 設計理由的一組實驗。",
    ],
    color: COLORS.orange,
    soft: COLORS.orangeSoft,
  });

  const takeaway = ctx.addShape(slide, {
    x: 54, y: 456, w: 1168, h: 132,
    fill: "#FFF8EA",
    line: ctx.line(COLORS.orange, 1.2),
  });
  takeaway.borderRadius = 12;
  ctx.addText(slide, {
    x: 82, y: 486, w: 1110, h: 58,
    text: "Takeaway\n目前可報告的核心不是「我把所有 dataset 都做完了」，而是「我已經把三個多跳 benchmark 的主結果、效率與消融完整跑出來，而且方法設定彼此一致。」",
    fontSize: 20,
    bold: true,
    color: COLORS.ink,
  });

  ctx.addText(slide, {
    x: 82, y: 555, w: 1110, h: 18,
    text: "下一步若要擴充，優先順序會是：Medical / Novel 或 max_steps scaling，而不是再加 exploratory dataset。",
    fontSize: 12,
    color: COLORS.muted,
  });
  return slide;
}

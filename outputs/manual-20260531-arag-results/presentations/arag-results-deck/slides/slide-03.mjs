import { addCard, addChrome, addTable, addTitleBlock, COLORS } from "./deck_common.mjs";

export async function slide03(presentation, ctx) {
  const slide = presentation.slides.add();
  addChrome(slide, ctx, { page: 3, total: 7 });
  addTitleBlock(slide, ctx, {
    title: "方法流程與實驗設定",
    subtitle: "固定資料、檢索、agent budget 與評估方式後，再比較不同方法變體。",
    color: COLORS.orange,
  });

  // pipeline diagram
  const boxes = [
    { x: 60, y: 170, w: 180, h: 74, title: "Corpus", color: COLORS.blue, soft: COLORS.blueSoft, body: "retrieval documents" },
    { x: 286, y: 170, w: 180, h: 74, title: "Questions", color: COLORS.purple, soft: COLORS.purpleSoft, body: "benchmark items" },
    { x: 512, y: 170, w: 180, h: 74, title: "Semantic Index", color: COLORS.teal, soft: COLORS.tealSoft, body: "sentence-level retrieval" },
    { x: 738, y: 170, w: 180, h: 74, title: "A-RAG Loop", color: COLORS.orange, soft: COLORS.orangeSoft, body: "tool use + answer" },
    { x: 964, y: 170, w: 180, h: 74, title: "Evaluation", color: COLORS.rose, soft: COLORS.roseSoft, body: "accuracy + efficiency" },
  ];
  boxes.forEach((b, idx) => {
    addCard(slide, ctx, { x: b.x, y: b.y, w: b.w, h: b.h, title: b.title, bodyLines: [b.body], color: b.color, soft: b.soft });
    if (idx < boxes.length - 1) {
      ctx.addShape(slide, { x: b.x + b.w, y: b.y + 34, w: 44, h: 2, fill: "#B8C2D6", line: ctx.line("#B8C2D6", 0) });
      ctx.addShape(slide, { x: b.x + b.w + 38, y: b.y + 30, w: 8, h: 10, geometry: "chevron", fill: "#B8C2D6", line: ctx.line("#B8C2D6", 0) });
    }
  });

  addTable(slide, ctx, {
    x: 60, y: 312,
    colWidths: [250, 200, 180, 190],
    rowHeight: 38,
    headers: ["Category", "Field", "Value", "Notes"],
    rows: [
      ["Model", "LLM", "google/gemini-3.5-flash", "local OpenAI-compatible proxy"],
      ["Embedding", "Model", "all-MiniLM-L6-v2", "official config path"],
      ["Agent", "max_loops", "8", "same control budget"],
      ["Agent", "max_token_budget", "32000", "consistent batch setting"],
      ["Data", "Question count", "100 per dataset", "MuSiQue / HotpotQA / 2Wiki"],
    ],
    headerFill: COLORS.orangeSoft,
    headerColor: COLORS.orange,
    fontSize: 12,
  });

  addCard(slide, ctx, {
    x: 900, y: 348, w: 320, h: 170,
    title: "評估指標",
    bodyLines: [
      "LLM Accuracy：模型判官語意比對",
      "Contain Accuracy：字串包含規則",
      "Avg Loops / Avg Retrieved Tokens / Avg Cost per Q",
    ],
    color: COLORS.teal,
    soft: COLORS.tealSoft,
  });

  addCard(slide, ctx, {
    x: 900, y: 548, w: 320, h: 92,
    title: "注意",
    bodyLines: [
      "token 指的是 retrieved tokens，",
      "不是完整 API billing token。",
    ],
    color: COLORS.rose,
    soft: COLORS.roseSoft,
  });
  return slide;
}

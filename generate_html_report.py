# -*- coding: utf-8 -*-
import os

html_path = r"C:\上課檔案\報告\1\outputs\a-rag-scrolling-report.html"
html_content = """<!DOCTYPE html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>《數據深淵的探險契書》：A-RAG 代理式檢索增強生成全解</title>
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans+TC:wght@300;400;500;700;900&display=swap" rel="stylesheet">
  
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['Inter', 'Noto Sans TC', 'sans-serif'],
            mono: ['Fira Code', 'monospace'],
          },
          colors: {
            brand: {
              50: '#f0f9ff',
              100: '#e0f2fe',
              500: '#0ea5e9',
              600: '#0284c7',
              700: '#0369a1',
            }
          }
        }
      }
    }
  </script>
  <style>
    body {
      font-feature-settings: "cv02", "cv03", "cv04", "cv11";
    }
    .glow-shadow {
      box-shadow: 0 0 20px rgba(14, 165, 233, 0.15);
    }
    .glow-shadow-orange {
      box-shadow: 0 0 20px rgba(249, 115, 22, 0.15);
    }
    /* 捲動軸美化 */
    ::-webkit-scrollbar {
      width: 8px;
    }
    ::-webkit-scrollbar-track {
      background: #f1f5f9;
    }
    .dark ::-webkit-scrollbar-track {
      background: #0f172a;
    }
    ::-webkit-scrollbar-thumb {
      background: #cbd5e1;
      border-radius: 4px;
    }
    .dark ::-webkit-scrollbar-thumb {
      background: #334155;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #94a3b8;
    }
  </style>
</head>
<body class="bg-slate-50 text-slate-900 font-sans transition-colors duration-300 dark:bg-slate-950 dark:text-slate-100">

  <!-- 頂部導覽列 -->
  <header class="sticky top-0 z-50 w-full border-b border-slate-300 bg-white/80 backdrop-blur-md dark:border-slate-800 dark:bg-slate-950/80 transition-colors">
    <div class="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
      <div class="flex items-center gap-2">
        <span class="text-2xl">🐱</span>
        <span class="text-xl font-bold bg-gradient-to-r from-brand-600 to-indigo-600 bg-clip-text text-transparent dark:from-brand-500 dark:to-indigo-400">哈基米的學術探險筆記</span>
      </div>
      <div class="flex items-center gap-4">
        <!-- 亮色/暗色 切換按鈕 -->
        <button id="themeToggle" class="rounded-lg border border-slate-300 p-2 text-slate-700 hover:bg-slate-100 dark:border-slate-700 dark:text-slate-300 dark:hover:bg-slate-800 transition" title="切換主題">
          <!-- 太陽 (亮色時顯示) -->
          <svg id="sunIcon" class="h-5 w-5 hidden" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 9H3m15.364-6.364l-.707.707M6.343 17.657l-.707.707m12.728 0l-.707-.707M6.343 6.343l-.707-.707m12.728 12.728A9 9 0 115.636 5.636m12.728 12.728L12 12" />
          </svg>
          <!-- 月亮 (暗色時顯示) -->
          <svg id="moonIcon" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
          </svg>
        </button>
        <a href="#one-page-summary" class="hidden sm:inline-block rounded-lg bg-brand-600 px-4 py-2 text-sm font-semibold text-white hover:bg-brand-700 transition">一頁式總結</a>
      </div>
    </div>
  </header>

  <!-- 主要內容區：雙欄版面（左側浮動目錄，右側長篇連載） -->
  <div class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 gap-8 lg:grid-cols-12">
      
      <!-- 左側浮動側邊欄 (TOC) -->
      <aside class="hidden lg:block lg:col-span-3 sticky top-24 self-start max-h-[80vh] overflow-y-auto pr-2 border-r border-slate-300 dark:border-slate-800">
        <h3 class="text-sm font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-4">探險章節目錄</h3>
        <nav class="space-y-1">
          <a href="#book-title" class="toc-link block rounded-md px-3 py-2 text-sm font-medium text-slate-700 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-300 dark:hover:bg-slate-800 dark:hover:text-white transition">🌟 封面與導讀</a>
          <a href="#characters" class="toc-link block rounded-md px-3 py-2 text-sm font-medium text-slate-700 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-300 dark:hover:bg-slate-800 dark:hover:text-white transition">🎭 冒險角色設定</a>
          <a href="#ch1" class="toc-link block rounded-md px-3 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-white transition">1. 摘要：契約之始</a>
          <a href="#ch2" class="toc-link block rounded-md px-3 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-white transition">2. 前言：舊秩序的裂痕</a>
          <a href="#ch3" class="toc-link block rounded-md px-3 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-white transition">3. 相關工作：江湖三大門派</a>
          <a href="#ch4" class="toc-link block rounded-md px-3 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-white transition">4. 方法設計：三神兵與智慧大腦</a>
          <a href="#ch5" class="toc-link block rounded-md px-3 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-white transition">5. 實驗結果：深淵之頂的對決</a>
          <a href="#ch6" class="toc-link block rounded-md px-3 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-white transition">6. 分析與討論：能量與迷霧</a>
          <a href="#ch7" class="toc-link block rounded-md px-3 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-white transition">7. 結論：新地平線</a>
          <a href="#ch8" class="toc-link block rounded-md px-3 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-white transition">8. 限制：探險未竟之路</a>
          <a href="#ch9" class="toc-link block rounded-md px-3 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-white transition">9. 倫理：冒險者的自律</a>
          <a href="#ch10" class="toc-link block rounded-md px-3 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-white transition">10. 附錄：探險寶典</a>
          <div class="my-4 border-t border-slate-300 dark:border-slate-800"></div>
          <a href="#one-page-summary" class="toc-link block rounded-md px-3 py-2 text-sm font-bold text-brand-600 hover:bg-slate-100 dark:text-brand-400 dark:hover:bg-slate-800 transition">📝 一頁式總結</a>
          <a href="#key-terms" class="toc-link block rounded-md px-3 py-2 text-sm font-bold text-brand-600 hover:bg-slate-100 dark:text-brand-400 dark:hover:bg-slate-800 transition">📋 10個關鍵對照</a>
          <a href="#contributions" class="toc-link block rounded-md px-3 py-2 text-sm font-bold text-brand-600 hover:bg-slate-100 dark:text-brand-400 dark:hover:bg-slate-800 transition">🏆 核心貢獻與限制</a>
          <a href="#takeaways" class="toc-link block rounded-md px-3 py-2 text-sm font-bold text-brand-600 hover:bg-slate-100 dark:text-brand-400 dark:hover:bg-slate-800 transition">💻 自建 RAG 實戰心法</a>
        </nav>
      </aside>

      <!-- 右側長篇內容區 -->
      <main class="col-span-1 lg:col-span-9 space-y-16">

        <!-- 封面區 -->
        <section id="book-title" class="text-center py-12 border-b border-slate-300 dark:border-slate-800">
          <span class="inline-flex items-center gap-1.5 rounded-full bg-brand-50 px-3 py-1 text-xs font-semibold text-brand-700 dark:bg-brand-950 dark:text-brand-300 border border-brand-300 mb-6">
            ✨ 哈基米學術巨獻 · 論文改寫科普連載小說
          </span>
          <h1 class="text-4xl font-extrabold sm:text-5xl lg:text-6xl tracking-tight bg-gradient-to-r from-brand-600 via-purple-600 to-indigo-600 bg-clip-text text-transparent dark:from-brand-400 dark:to-indigo-300 mb-6 leading-tight">
            數據深淵的探險契書
          </h1>
          <p class="text-lg text-slate-500 dark:text-slate-400 max-w-2xl mx-auto font-medium">
            —— 探秘 A-RAG 代理式檢索增強生成框架：如何解開枷鎖，讓 LLM 成為能自我決策的深淵探險家？
          </p>
          <div class="mt-8 flex justify-center gap-4 text-sm text-slate-400">
            <span>原著論文：A-RAG (2026)</span>
            <span>•</span>
            <span>改寫策劃：哈基米 🐱</span>
          </div>
        </section>

        <!-- 導讀區 -->
        <section class="bg-white rounded-2xl p-6 sm:p-8 border border-slate-300 dark:bg-slate-900 dark:border-slate-800 glow-shadow transition-all">
          <h2 class="text-2xl font-bold flex items-center gap-2 text-slate-800 dark:text-slate-100 mb-6">
            <span>🌌</span> 導讀：被封印在水晶球中的神明
          </h2>
          <div class="space-y-4 text-slate-600 dark:text-slate-300 leading-relaxed text-justify">
            <p>
              大語言模型（LLM）就像是住在高塔水晶球中的全知之神——它擁有驚人的智慧，但水晶球外的世界卻在日新月異地變化。為了防止神明在回答當下問題時「胡說八道」（幻覺），人類發明了<strong>檢索增強生成（RAG）</strong>這條管道。
            </p>
            <p>
              然而，現有的 RAG 就像是一條死板的傳送帶。每當你向神明提問，傳送帶便會按照寫死的代碼邏輯，從名為「知識語料庫」的無底深淵中，粗暴地挖出一大卡車資料，連同泥沙廢紙一併倒在神明面前，逼它在幾秒鐘內讀完並給出精確答案。
            </p>
            <p>
              「夠了！」神明感到不堪重負。這些多餘的「廢物 Token」不僅撐爆了神明的腦容量（上下文視窗），更帶來了無數噪音。最糟糕的是，如果傳送帶第一波運來的資料不對，神明即使擁有絕世智慧，也無法發出指令讓傳送帶重新去挖更有用的地方。
            </p>
            <p>
              這篇發表於 <strong>2026 年 2 月</strong> 的重磅論文《A-RAG》正是為了解救神明而誕生。作者們提出了 <strong>A-RAG（Agentic Retrieval-Augmented Generation, 代理式檢索增強生成）</strong> 框架。它打破了死板的流水線，將外部知識庫重塑為三個層級的資訊檢索介面，並給予大模型完全的「探險自主權」！從此，大語言模型不再是被動的資料接收者，而是能自主穿戴神兵、深入數據深淵的<strong>「探險家」</strong>！｡>∀<｡✨
            </p>
          </div>
        </section>

        <!-- 角色設定區 -->
        <section id="characters" class="scroll-mt-20">
          <h2 class="text-3xl font-extrabold text-slate-800 dark:text-slate-100 mb-8 border-b border-slate-300 dark:border-slate-800 pb-2 flex items-center gap-2">
            <span>🎭</span> 冒險角色設定：數據深淵的探險小隊
          </h2>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            
            <!-- Naive RAG Card -->
            <div class="bg-white rounded-xl p-6 border border-slate-300 dark:bg-slate-900 dark:border-slate-800 hover:border-red-400 dark:hover:border-red-500 transition-all flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between mb-4">
                  <span class="text-xs font-bold text-red-600 bg-red-50 dark:bg-red-950/50 dark:text-red-400 px-2.5 py-1 rounded-full border border-red-200">Naive RAG</span>
                  <span class="text-2xl">📦</span>
                </div>
                <h3 class="text-lg font-bold text-slate-800 dark:text-slate-100 mb-2">盲目的「盲盒快遞員」</h3>
                <p class="text-sm text-slate-500 dark:text-slate-400 leading-relaxed mb-4 text-justify">
                  傳統一次性 RAG。它手裡捧著一大堆未經篩選的 1000-token Chunk，不管三七二十一，在冒險開始的一瞬間就把箱子全部砸在模型腳邊。
                </p>
              </div>
              <div class="text-xs font-semibold text-red-500 border-t border-slate-200 dark:border-slate-800 pt-3">
                ⚔️ 特色：一擊脫離、腦容量殺手、胡說八道率高
              </div>
            </div>

            <!-- Workflow RAG Card -->
            <div class="bg-white rounded-xl p-6 border border-slate-300 dark:bg-slate-900 dark:border-slate-800 hover:border-yellow-400 dark:hover:border-yellow-500 transition-all flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between mb-4">
                  <span class="text-xs font-bold text-yellow-600 bg-yellow-50 dark:bg-yellow-950/50 dark:text-yellow-400 px-2.5 py-1 rounded-full border border-yellow-200">Workflow RAG</span>
                  <span class="text-2xl">📋</span>
                </div>
                <h3 class="text-lg font-bold text-slate-800 dark:text-slate-100 mb-2">按本宣科的「死板秘書」</h3>
                <p class="text-sm text-slate-500 dark:text-slate-400 leading-relaxed mb-4 text-justify">
                  現行的多輪 RAG（如 FLARE、MA-RAG）。它手裡拿著工程師寫死的「公文 SOP」。雖然能多輪查找，但無論問題多簡單，都必須強迫模型跑完一整套複雜、昂貴的多代理開會流程。
                </p>
              </div>
              <div class="text-xs font-semibold text-yellow-500 border-t border-slate-200 dark:border-slate-800 pt-3">
                ⚔️ 特色：極度僵硬、高昂的 Token 費用、缺乏執行期彈性
              </div>
            </div>

            <!-- A-RAG Card -->
            <div class="bg-white rounded-xl p-6 border-2 border-brand-500 dark:bg-slate-900 dark:border-brand-400 shadow-lg glow-shadow transition-all flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between mb-4">
                  <span class="text-xs font-bold text-brand-600 bg-brand-50 dark:bg-brand-950/50 dark:text-brand-300 px-2.5 py-1 rounded-full border border-brand-300">A-RAG Full</span>
                  <span class="text-2xl">🤠</span>
                </div>
                <h3 class="text-lg font-bold text-slate-800 dark:text-slate-100 mb-2">自主決策的「全能探險家」</h3>
                <p class="text-sm text-slate-500 dark:text-slate-400 leading-relaxed mb-4 text-justify">
                  本文提出的 A-RAG。大腦完全自主！配戴著三層降維打擊的層級化神兵，在 ReAct 思考循環中，自己判斷要查什麼、精讀哪裡，並有 Context Tracker 防止重複查閱！
                </p>
              </div>
              <div class="text-xs font-semibold text-brand-500 border-t border-slate-200 dark:border-slate-800 pt-3">
                ⚔️ 特色：高準確度、Token 超級省、測試時擴展性極強
              </div>
            </div>

          </div>
        </section>

        <!-- 第 1-10 章內容開始 -->
        <div class="space-y-24">

          <!-- CHAPTER 1 -->
          <section id="ch1" class="scroll-mt-20 border-t-2 border-slate-300 dark:border-slate-800 pt-12">
            <div class="flex items-center gap-3 mb-6">
              <span class="text-4xl font-extrabold text-brand-500">01</span>
              <h2 class="text-2xl sm:text-3xl font-bold text-slate-800 dark:text-slate-100">第一章：Abstract —— 數據深淵的「探險契書」</h2>
            </div>
            
            <div class="space-y-8">
              <div class="pl-4 border-l-4 border-brand-500 space-y-2">
                <h4 class="text-sm font-bold uppercase tracking-wider text-brand-600">【小說化敘事版】</h4>
                <p class="text-slate-600 dark:text-slate-300 text-justify leading-relaxed">
                  在無邊無際的數位深淵中，沉睡著人類累積的龐大知識庫。傳統的 RAG（檢索增強生成）就像是一條生硬僵死的傳送帶，它在探險開始的一瞬間，就將沉重的 1000-token Chunk（文本區塊）盲目地傾倒在大模型探險家的腳邊。這無疑給探險家戴上了沈重的枷鎖。
                  這份被稱為「A-RAG」的全新探險契書就此誕生！它宣布了一項革命性的範式轉變：不再依靠僵死的工作流（Workflows），而是建立一個<strong>層級化檢索介面（Hierarchical Retrieval Interfaces）</strong>。它把知識拆解為微觀的「關鍵字雷達」、宏觀的「語意導航儀」和高精度的「精讀顯微鏡」，並把完全的決策權交還給探險家。實驗結果證明，當探險家擁有高度自主權，他能在節省大把能量（Token）的同時，以高達 74.1%（MuSiQue）和 94.5%（HotpotQA）的驚人成功率，征服深淵最危險的角落！｡>∀<｡✨
                </p>
              </div>

              <div class="bg-slate-100 dark:bg-slate-900 rounded-xl p-6 border border-slate-300 dark:border-slate-800 space-y-3">
                <h4 class="text-sm font-bold text-slate-700 dark:text-slate-300">【技術白話版】</h4>
                <ul class="list-disc list-inside text-sm text-slate-600 dark:text-slate-300 space-y-2 text-justify">
                  <li><strong>核心問題</strong>：傳統 RAG 依賴寫死的工作流，檢索器與大模型脫節，造成 Context 冗餘及無法動態修正。</li>
                  <li><strong>解決方案</strong>：提出 A-RAG 框架，建立三層檢索 API：Keyword-level、Sentence-level、Chunk-level，並由 LLM 自主決定策略。</li>
                  <li><strong>重大發現</strong>：A-RAG 能隨「測試時計算量（Test-Time Compute）」擴展，且 context 效率大幅領先 HippoRAG 與 GraphRAG 等先進框架。</li>
                </ul>
              </div>

              <div class="bg-indigo-50 dark:bg-slate-900 rounded-xl p-6 border border-indigo-200 dark:border-indigo-950 space-y-2">
                <h4 class="text-sm font-bold text-indigo-700 dark:text-indigo-300">【原文重點對照】</h4>
                <p class="text-xs font-mono text-slate-500 dark:text-slate-400 leading-relaxed text-justify">
                  "To address these limitations, we propose A-RAG, an Agentic RAG framework featuring hierarchical retrieval interfaces. We observe that when equipped with this hierarchical toolset, the agent spontaneously generalizes to diverse workflows tailored to various tasks, yielding consistent performance gains."<br>
                  <span class="text-xs text-indigo-500 font-sans block mt-1">（中譯：為了克服這些限制，我們提出了 A-RAG，一個具備階層式檢索介面的代理式 RAG 框架。我們觀察到，當配備了這套層級化工具集後，代理人能自發地泛化出針對各種任務量身定制的多樣化工作流，帶來持續的效能提升。）</span>
                </p>
              </div>

              <div class="text-xs text-brand-600 dark:text-brand-400 bg-brand-50 dark:bg-brand-950/30 p-4 rounded-lg border border-brand-200">
                💡 <strong>【讀者提醒】</strong>：很多論文喜歡堆疊超複雜的圖譜和強化學習公式，但 A-RAG 卻反其道而行。它證明了「只要提供對代理友善的 API 介面，普通大模型就能自己找出完美的解答路徑」！千萬不要被市面上那些號稱有幾百個 node 的複雜 Agent 架構給嚇傻囉，簡約才是王道！
              </div>
            </div>
          </section>

          <!-- CHAPTER 2 -->
          <section id="ch2" class="scroll-mt-20 border-t border-slate-300 dark:border-slate-800 pt-12">
            <div class="flex items-center gap-3 mb-6">
              <span class="text-4xl font-extrabold text-brand-500">02</span>
              <h2 class="text-2xl sm:text-3xl font-bold text-slate-800 dark:text-slate-100">第二章：Introduction —— 舊秩序的裂痕與自主的微光</h2>
            </div>
            
            <div class="space-y-8">
              <div class="pl-4 border-l-4 border-brand-500 space-y-2">
                <h4 class="text-sm font-bold uppercase tracking-wider text-brand-600">【小說化敘事版】</h4>
                <p class="text-slate-600 dark:text-slate-300 text-justify leading-relaxed">
                  走進前沿研究的聖殿，你會聽見一聲嘆息。傳統的 RAG 技術曾經是一座燈塔，照亮了解決「大模型胡言亂語（幻覺）」的黑暗長路。但隨著任務越來越繁複，燈塔的光芒開始動搖。
                  「我們給模型餵了太多毫無關聯的垃圾，只為了解答一個小問題！」研究員們無奈地看著高昂的 Token 帳單。
                  現有的解決方案試圖打破這種僵局，他們架構了更複雜的 Workflow（工作流）—— 但這些流程依然是程式設計師「提前在代碼裡寫死（Hard-coded）」的套路！模型就像個照著劇本演戲的傀儡。
                  「為什麼不相信模型的大腦？」A-RAG 團隊大膽地發出詰問。他們決定打破這條死板的枷鎖。他們證明了，即使是配備最陽春的單一檢索工具的 <strong>Naive Agentic RAG（基礎代理式 RAG）</strong>，其表現就已經大幅超越了傳統那些寫死代碼的管線（Pipeline）。這說明，自主權，才是解開智慧潛能的最終密鑰！(๑•̀ㅂ•́)و✧✨
                </p>
              </div>

              <div class="bg-slate-100 dark:bg-slate-900 rounded-xl p-6 border border-slate-300 dark:border-slate-800 space-y-3">
                <h4 class="text-sm font-bold text-slate-700 dark:text-slate-300">【技術白話版】</h4>
                <ul class="list-disc list-inside text-sm text-slate-600 dark:text-slate-300 space-y-2 text-justify">
                  <li><strong>現有 RAG 瓶頸</strong>：檢索器與 LLM 之間沒有互動協議，大模型無法適應特定任務，決定何時資訊足夠。</li>
                  <li><strong>初步實驗驚人發現</strong>：哪怕是最簡單的 Naive Agentic RAG（只配備一個向量检索工具，在思考循環中自我呼叫），成績也全面碾壓傳統 LinearRAG 與 Naive RAG。</li>
                  <li><strong>研究貢獻總覽</strong>：倡導從靜態 pipeline 轉向動態 agent；實作 A-RAG 框架；對 Test-Time Scaling 的規律進行首次全面量化分析。</li>
                </ul>
              </div>

              <div class="bg-indigo-50 dark:bg-slate-900 rounded-xl p-6 border border-indigo-200 dark:border-indigo-950 space-y-2">
                <h4 class="text-sm font-bold text-indigo-700 dark:text-indigo-300">【原文重點對照】</h4>
                <p class="text-xs font-mono text-slate-500 dark:text-slate-400 leading-relaxed text-justify">
                  "Neither approach is truly agentic, as the model is not allowed to adapt the workflow based on the specific task, choose different interaction strategies, or decide when sufficient evidence has been gathered to provide an answer."<br>
                  <span class="text-xs text-indigo-500 font-sans block mt-1">（中譯：現有方法都不是真正的代理式，因為模型不被允許根據特定任務動態調整工作流、選擇不同的交互策略，或自主決定何時已經收集到足夠證據來給出回答。）</span>
                </p>
              </div>

              <div class="text-xs text-brand-600 dark:text-brand-400 bg-brand-50 dark:bg-brand-950/30 p-4 rounded-lg border border-brand-200">
                💡 <strong>【讀者提醒】</strong>：讀這裡時請注意「Naive Agentic RAG」和「A-RAG Full」的區別！前者只是「讓 Agent 自主多輪調用普通的單一向量工具」；後者才是「配備了 keyword_search、semantic_search、chunk_read 階層式三神兵的完全體 A-RAG」！這兩者在實驗中是重要的對照組喔。
              </div>
            </div>
          </section>

          <!-- CHAPTER 3 -->
          <section id="ch3" class="scroll-mt-20 border-t border-slate-300 dark:border-slate-800 pt-12">
            <div class="flex items-center gap-3 mb-6">
              <span class="text-4xl font-extrabold text-brand-500">03</span>
              <h2 class="text-2xl sm:text-3xl font-bold text-slate-800 dark:text-slate-100">第三章：Related Work —— 江湖三大門派的宿命對決</h2>
            </div>
            
            <div class="space-y-8">
              <div class="pl-4 border-l-4 border-brand-500 space-y-2">
                <h4 class="text-sm font-bold uppercase tracking-wider text-brand-600">【小說化敘事版】</h4>
                <p class="text-slate-600 dark:text-slate-300 text-justify leading-relaxed">
                  在數據深淵的邊界，豎立著一塊古老的石碑（圖 2）。上面刻著衡量一個檢索系統是否具備「自主意識」的三大黃金法則：
                  <strong>1. 自主策略（Autonomous Strategy）</strong>：模型能不能自己看著辦，隨時更換戰術？
                  <strong>2. 反覆執行（Iterative Execution）</strong>：模型能不能根據之前的線索，發起下一次追問？
                  <strong>3. 交錯工具（Interleaved Tool Use）</strong>：模型能不能在「思考 ➔ 行動 ➔ 觀察」中穿插使用不同工具？
                  在此之前，江湖上有三大門派割據一方：
                  <strong>基礎 RAG 派</strong>就像「盲目的快遞員」，蒙著大腦的眼睛一次性送貨；
                  <strong>Graph RAG 派（如微軟 GraphRAG, HippoRAG）</strong>則是「沉迷畫地圖的完美主義者」，他們建立了極其精緻的關係圖，但依然依賴硬編碼的檢索演算法，大腦無法動態修改路徑；
                  <strong>Workflow RAG 派（如 FLARE, RAGentA）</strong>則像「照本宣科的死板秘書」，流程在代碼設計之初就被鎖死，毫無彈性。
                  而 A-RAG，正是打破這一切，唯一滿足全部三大法則的究極大滿貫！
                </p>
              </div>

              <!-- 論文插圖 Figure 2 -->
              <div class="my-8 text-center bg-white dark:bg-slate-900 p-4 border border-slate-300 dark:border-slate-800 rounded-xl max-w-2xl mx-auto">
                <img src="assets/page03-embedded.png" alt="Figure 2: Three Paradigms Comparison" class="mx-auto rounded-lg shadow-sm border border-slate-200">
                <p class="text-xs text-slate-400 mt-3 font-medium">📜 圖 2 論文原圖對照：三大 RAG 範式（Graph, Workflow, Agentic）的自主權對決</p>
              </div>

              <!-- 自主權對照表 -->
              <div class="overflow-x-auto rounded-xl border border-slate-300 dark:border-slate-800 bg-white dark:bg-slate-900 p-4">
                <h5 class="text-sm font-bold text-slate-700 dark:text-slate-300 mb-3">🛠️ 門派自主權比拼 (論文 Table 4 摘錄)</h5>
                <table class="w-full text-left text-sm text-slate-500 dark:text-slate-400">
                  <thead class="bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200">
                    <tr>
                      <th class="p-3 border-b border-slate-300 dark:border-slate-700">門派 / 方法</th>
                      <th class="p-3 border-b border-slate-300 dark:border-slate-700 text-center">自主策略 (Auto. Strategy)</th>
                      <th class="p-3 border-b border-slate-300 dark:border-slate-700 text-center">反覆執行 (Iter. Execution)</th>
                      <th class="p-3 border-b border-slate-300 dark:border-slate-700 text-center">交錯工具 (Interleaved Tool)</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr class="border-b border-slate-200 dark:border-slate-800">
                      <td class="p-3 font-semibold text-slate-800 dark:text-slate-200">Naive RAG</td>
                      <td class="p-3 text-center text-red-500">❌ 否</td>
                      <td class="p-3 text-center text-red-500">❌ 否</td>
                      <td class="p-3 text-center text-red-500">❌ 否</td>
                    </tr>
                    <tr class="border-b border-slate-200 dark:border-slate-800">
                      <td class="p-3 font-semibold text-slate-800 dark:text-slate-200">GraphRAG / HippoRAG</td>
                      <td class="p-3 text-center text-red-500">❌ 否</td>
                      <td class="p-3 text-center text-red-500">❌ 否</td>
                      <td class="p-3 text-center text-red-500">❌ 否</td>
                    </tr>
                    <tr class="border-b border-slate-200 dark:border-slate-800">
                      <td class="p-3 font-semibold text-slate-800 dark:text-slate-200">MA-RAG / RAGentA</td>
                      <td class="p-3 text-center text-yellow-500">▲ 邊界狀態</td>
                      <td class="p-3 text-center text-green-500">✅ 是</td>
                      <td class="p-3 text-center text-yellow-500">▲ 邊界狀態</td>
                    </tr>
                    <tr class="bg-brand-50/50 dark:bg-brand-950/20 font-bold text-brand-700 dark:text-brand-300">
                      <td class="p-3">A-RAG (本文方法)</td>
                      <td class="p-3 text-center text-green-500">✅ 是</td>
                      <td class="p-3 text-center text-green-500">✅ 是</td>
                      <td class="p-3 text-center text-green-500">✅ 是</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <div class="bg-indigo-50 dark:bg-slate-900 rounded-xl p-6 border border-indigo-200 dark:border-indigo-950 space-y-2">
                <h4 class="text-sm font-bold text-indigo-700 dark:text-indigo-300">【原文重點對照】</h4>
                <p class="text-xs font-mono text-slate-500 dark:text-slate-400 leading-relaxed text-justify">
                  "While these methods incorporate richer structure, they still rely on predefined retrieval algorithms rather than model-driven decisions. If the initially retrieved context is insufficient, the model cannot leverage its reasoning capabilities to iteratively gather more comprehensive and accurate information."<br>
                  <span class="text-xs text-indigo-500 font-sans block mt-1">（中譯：雖然這些方法納入了更豐富的結構，但它們仍然依賴預定義的檢索演算法，而非大模型驅動的決策。如果最初檢索到的上下文不足，模型便無法利用其推理能力來迭代地收集更全面、更準確的資訊。）</span>
                </p>
              </div>

              <div class="text-xs text-brand-600 dark:text-brand-400 bg-brand-50 dark:bg-brand-950/30 p-4 rounded-lg border border-brand-200">
                💡 <strong>【讀者提醒】</strong>：微軟的 GraphRAG 的確非常火熱，但不要迷信名氣！它的主要痛點就是「執行期極其昂貴，且模型在檢索時無法中途轉彎」。A-RAG 讓我們看到，把「策略主導權」還給 LLM 本身，才是真正提升 RAG 效率的智慧之路。
              </div>
            </div>
          </section>

          <!-- CHAPTER 4 -->
          <section id="ch4" class="scroll-mt-20 border-t border-slate-300 dark:border-slate-800 pt-12">
            <div class="flex items-center gap-3 mb-6">
              <span class="text-4xl font-extrabold text-brand-500">04</span>
              <h2 class="text-2xl sm:text-3xl font-bold text-slate-800 dark:text-slate-100">第四章：Methodology —— 三層神兵與無硬編碼的智慧大腦</h2>
            </div>
            
            <div class="space-y-8">
              <div class="pl-4 border-l-4 border-brand-500 space-y-2">
                <h4 class="text-sm font-bold uppercase tracking-wider text-brand-600">【小說化敘事版】</h4>
                <p class="text-slate-600 dark:text-slate-300 text-justify leading-relaxed">
                  進入探險家的武器庫，三件精心打磨的降維神兵呈現在我們眼前：<br>
                  <strong>📡 關鍵字搜尋（keyword_search）—— 微觀精確雷達</strong>：當探險家追蹤極度罕見的實體（如人名或編號）時，字面精準匹配是最高效的手段。打分公式考慮了單詞長度：
                  $$\text{Score}_{\text{kw}}(c_i, K) = \sum_{k \in K} \text{count}(k, T_i) \cdot |k|$$
                  越長的單詞權重越高！為了不讓腦容量爆炸，它僅回傳包含了該關鍵字的句子片段（Snippet）。<br>
                  <strong>🗺️ 語意搜尋（semantic_search）—— 宏觀概念導航儀</strong>：專治「意思相同但字面不同」的概念。利用句子嵌入向量（Embedding）計算餘弦夾角（Cosine Similarity）：
                  $$\text{Score}_{\text{sem}}(s_{i,j}, q) = \frac{v_{i,j}^T v_q}{\|v_{i,j}\| \|v_q\|}$$
                  只拼合出最高分句子所在的父區塊並回傳其 Snippet 片段作為誘餌。<br>
                  <strong>🔍 區塊閱讀（chunk_read）—— 高精度精讀顯微鏡</strong>：這是唯一的實體閱讀工具。探險家看過上述兩大工具回傳的「誘餌（Snippets）」後，如果斷定該區塊至關重要，就會拉取完整全文進行深入精讀。<br>
                  而<strong>上下文追蹤器（Context Tracker）</strong>則在後方默默維護著一張「已讀地圖」 $C_{\text{read}}$，一旦模型試圖重複精讀同個區塊，追蹤器便會溫柔攔阻，避免重覆吞噬 Token 能量！｡>∀<｡✨
                </p>
              </div>

              <!-- 論文插圖 Figure 3 -->
              <div class="my-8 text-center bg-white dark:bg-slate-900 p-4 border border-slate-300 dark:border-slate-800 rounded-xl max-w-2xl mx-auto">
                <img src="assets/page17.png" alt="Figure 3 / Tool Templates" class="mx-auto rounded-lg shadow-sm border border-slate-200">
                <p class="text-xs text-slate-400 mt-3 font-medium">📜 論文原圖對照：A-RAG 三層檢索神兵與 ReAct 自主循環 Prompt 模板定義 (Appendix E)</p>
              </div>

              <div class="bg-slate-100 dark:bg-slate-900 rounded-xl p-6 border border-slate-300 dark:border-slate-800 space-y-3">
                <h4 class="text-sm font-bold text-slate-700 dark:text-slate-300">【技術白話版】</h4>
                <ul class="list-disc list-inside text-sm text-slate-600 dark:text-slate-300 space-y-2 text-justify">
                  <li><strong>階層式索引建置</strong>：線下階段極其輕量。僅需做 1,000-token 句子邊界對齊分塊，並對每個句子計算 Embedding 存檔。關鍵字檢索則在執行期即時計算，無建圖成本！</li>
                  <li><strong>打分優化（公式 1）</strong>：關鍵字打分加入長度權重 $|k|$，因為長詞包含更具體的實體資訊，能大幅減少語意無關的頻繁詞干擾。</li>
                  <li><strong>Context Tracker 機制</strong>：當模型呼叫已被精讀的 $c_i \in C_{\text{read}}$ 時，系統只回傳已讀提示（"This chunk is already in your message history"），防堵無效 Token 浪費，極大限度壓低輸入 Context 大小。</li>
                </ul>
              </div>

              <div class="bg-indigo-50 dark:bg-slate-900 rounded-xl p-6 border border-indigo-200 dark:border-indigo-950 space-y-2">
                <h4 class="text-sm font-bold text-indigo-700 text-justify dark:text-indigo-300">【原文重點對照】</h4>
                <p class="text-xs font-mono text-slate-500 dark:text-slate-400 leading-relaxed text-justify">
                  "This hierarchical design is inherently agent-friendly, allowing the agent to access corpus information at different granularities based on its own judgment. Rather than loading large amounts of context indiscriminately, the agent can incrementally retrieve information on-demand..."<br>
                  <span class="text-xs text-indigo-500 font-sans block mt-1">（中譯：這種層級化的設計本質上是對代理友善的，允許代理人根據自己的判斷以不同的粒度訪問語料庫資訊。代理人可以按需漸進式地檢索資訊，而不是不加區別地加載大量上下文……）</span>
                </p>
              </div>

              <div class="text-xs text-brand-600 dark:text-brand-400 bg-brand-50 dark:bg-brand-950/30 p-4 rounded-lg border border-brand-200">
                💡 <strong>【讀者提醒】</strong>：在自建 RAG 專案時，最容易犯的錯誤就是「一次把 semantic search 命中的前 5 個 full chunk 全塞進 prompt 裡」。這在 A-RAG 裡是不被允許的！正確的做法是像 A-RAG 一樣，只先提供 matched sentence 片段，讓 Agent 自主挑選後，再調用讀取工具載入 full text，這能讓你的 Token 費用大打一折！
              </div>
            </div>
          </section>

          <!-- CHAPTER 5 -->
          <section id="ch5" class="scroll-mt-20 border-t border-slate-300 dark:border-slate-800 pt-12">
            <div class="flex items-center gap-3 mb-6">
              <span class="text-4xl font-extrabold text-brand-500">05</span>
              <h2 class="text-2xl sm:text-3xl font-bold text-slate-800 dark:text-slate-100">第五章：Experiments —— 數據深淵之頂的對決大捷</h2>
            </div>
            
            <div class="space-y-8">
              <div class="pl-4 border-l-4 border-brand-500 space-y-2">
                <h4 class="text-sm font-bold uppercase tracking-wider text-brand-600">【小說化敘事版】</h4>
                <p class="text-slate-600 dark:text-slate-300 text-justify leading-relaxed">
                  探險隊踏上了極具考驗的五個大型資料集戰場（MuSiQue, HotpotQA, 2WikiMultiHop, Medical, Novel）。面對傳統霸主，A-RAG 展現出了無可匹敵的實戰壓制力！
                  在 GPT-5-mini 大腦的全力運轉下，A-RAG（Full）在 MuSiQue 拿下了 74.1% 的歷史性高分，比老牌的 HippoRAG（61.7%）和 LinearRAG（62.4%）高出足足 12 個百分點！在 HotpotQA，更是寫下了 94.5% 的驚人天花板紀錄！
                  「這證明了，大腦的智慧一旦配備了正確的武器，其爆發力是傳統死板腳本完全無法想像的。」哈基米振奮地說。
                  更精采的是<strong>消融實驗（Ablation Study）</strong>：當我們試圖收回任何一件武器時，大腦便會立刻陷入苦戰。拿掉「精確雷達（keyword_search）」，MuSiQue 戰力跌至 72.6%；而一旦拿掉「語意導航儀（semantic_search）」，戰力更是一路狂跌至 69.4%！這充分證明，三件降維神兵缺一不可，它們是完美的互補組合！｡>∀<｡✨
                </p>
              </div>

              <!-- 高對比度、色盲友善的滿血數據圖表 (純 HTML / CSS) -->
              <div class="bg-white dark:bg-slate-900 border border-slate-300 dark:border-slate-800 rounded-xl p-6 space-y-8 glow-shadow">
                <div>
                  <h4 class="text-base font-bold text-slate-800 dark:text-slate-100 mb-1 flex items-center gap-1.5">
                    <span class="inline-block w-3 h-3 bg-brand-500 rounded-full"></span>
                    主力對決：GPT-5-mini 下的主流框架精度 (LLM-Acc) 對比
                  </h4>
                  <p class="text-xs text-slate-400 mb-4">數值利用滿版縱軸高度拉伸顯示（極致數據密度，色盲友善雙重標記 📊）</p>
                  
                  <div class="space-y-4">
                    <!-- MuSiQue -->
                    <div>
                      <div class="flex justify-between text-xs font-bold text-slate-600 dark:text-slate-400 mb-1">
                        <span>MuSiQue (多步推理極難關卡)</span>
                        <span class="text-brand-600 dark:text-brand-400 font-mono">A-RAG Full: 74.1% 🏆</span>
                      </div>
                      <div class="h-8 bg-slate-100 dark:bg-slate-800 rounded overflow-hidden flex items-center p-1 gap-1">
                        <div class="h-full bg-slate-400 text-[10px] text-white font-bold flex items-center px-2 rounded" style="width: 52.8%" title="Naive RAG">Naive: 52.8%</div>
                        <div class="h-full bg-indigo-400 text-[10px] text-white font-bold flex items-center px-2 rounded" style="width: 62.4%" title="LinearRAG">Linear: 62.4%</div>
                        <div class="h-full bg-brand-500 text-[10px] text-white font-bold flex items-center px-2 rounded" style="width: 74.1%" title="A-RAG Full">A-RAG: 74.1%</div>
                      </div>
                    </div>

                    <!-- HotpotQA -->
                    <div>
                      <div class="flex justify-between text-xs font-bold text-slate-600 dark:text-slate-400 mb-1">
                        <span>HotpotQA (雙步推理戰場)</span>
                        <span class="text-brand-600 dark:text-brand-400 font-mono">A-RAG Full: 94.5% 🏆</span>
                      </div>
                      <div class="h-8 bg-slate-100 dark:bg-slate-800 rounded overflow-hidden flex items-center p-1 gap-1">
                        <div class="h-full bg-slate-400 text-[10px] text-white font-bold flex items-center px-2 rounded" style="width: 81.2%" title="Naive RAG">Naive: 81.2%</div>
                        <div class="h-full bg-indigo-400 text-[10px] text-white font-bold flex items-center px-2 rounded" style="width: 86.2%" title="LinearRAG">Linear: 86.2%</div>
                        <div class="h-full bg-brand-500 text-[10px] text-white font-bold flex items-center px-2 rounded" style="width: 94.5%" title="A-RAG Full">A-RAG: 94.5%</div>
                      </div>
                    </div>

                    <!-- 2Wiki -->
                    <div>
                      <div class="flex justify-between text-xs font-bold text-slate-600 dark:text-slate-400 mb-1">
                        <span>2WikiMultiHop (實體關係複雜戰場)</span>
                        <span class="text-brand-600 dark:text-brand-400 font-mono">A-RAG Full: 89.7% 🏆</span>
                      </div>
                      <div class="h-8 bg-slate-100 dark:bg-slate-800 rounded overflow-hidden flex items-center p-1 gap-1">
                        <div class="h-full bg-slate-400 text-[10px] text-white font-bold flex items-center px-2 rounded" style="width: 50.2%" title="Naive RAG">Naive: 50.2%</div>
                        <div class="h-full bg-indigo-400 text-[10px] text-white font-bold flex items-center px-2 rounded" style="width: 87.2%" title="LinearRAG">Linear: 87.2%</div>
                        <div class="h-full bg-brand-500 text-[10px] text-white font-bold flex items-center px-2 rounded" style="width: 89.7%" title="A-RAG Full">A-RAG: 89.7%</div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- 消融實驗水平對比圖 -->
                <div>
                  <h4 class="text-base font-bold text-slate-800 dark:text-slate-100 mb-1 flex items-center gap-1.5">
                    <span class="inline-block w-3 h-3 bg-indigo-500 rounded-full"></span>
                    消融實驗：移除武器後的掉分慘烈現場 (MuSiQue / GPT-5-mini)
                  </h4>
                  <p class="text-xs text-slate-400 mb-4">完美呈現「缺一不可」的互補生態系統 🛠️</p>
                  
                  <div class="space-y-3">
                    <div>
                      <div class="flex justify-between text-xs mb-1">
                        <span class="font-medium text-slate-700 dark:text-slate-300">⚔️ A-RAG Full (完全體)</span>
                        <span class="font-mono text-green-600 dark:text-green-400 font-bold">74.1%</span>
                      </div>
                      <div class="w-full bg-slate-200 dark:bg-slate-800 h-3 rounded-full">
                        <div class="bg-green-500 h-3 rounded-full transition-all" style="width: 74.1%"></div>
                      </div>
                    </div>

                    <div>
                      <div class="flex justify-between text-xs mb-1">
                        <span class="font-medium text-slate-700 dark:text-slate-300">❌ 拔除 keyword_search (字面雷達)</span>
                        <span class="font-mono text-orange-600 dark:text-orange-400 font-bold">72.6% (跌 1.5%)</span>
                      </div>
                      <div class="w-full bg-slate-200 dark:bg-slate-800 h-3 rounded-full">
                        <div class="bg-orange-400 h-3 rounded-full transition-all" style="width: 72.6%"></div>
                      </div>
                    </div>

                    <div>
                      <div class="flex justify-between text-xs mb-1">
                        <span class="font-medium text-slate-700 dark:text-slate-300">❌ 拔除 semantic_search (語意導航)</span>
                        <span class="font-mono text-red-600 dark:text-red-400 font-bold">69.4% (暴跌 4.7%) 🚨</span>
                      </div>
                      <div class="w-full bg-slate-200 dark:bg-slate-800 h-3 rounded-full">
                        <div class="bg-red-500 h-3 rounded-full transition-all" style="width: 69.4%"></div>
                      </div>
                    </div>

                    <div>
                      <div class="flex justify-between text-xs mb-1">
                        <span class="font-medium text-slate-700 dark:text-slate-300">❌ 拔除 chunk_read (精讀顯微鏡)</span>
                        <span class="font-mono text-yellow-600 dark:text-yellow-400 font-bold">73.6% (跌 0.5%)</span>
                      </div>
                      <div class="w-full bg-slate-200 dark:bg-slate-800 h-3 rounded-full">
                        <div class="bg-yellow-400 h-3 rounded-full transition-all" style="width: 73.6%"></div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="bg-indigo-50 dark:bg-slate-900 rounded-xl p-6 border border-indigo-200 dark:border-indigo-950 space-y-2">
                <h4 class="text-sm font-bold text-indigo-700 dark:text-indigo-300">【原文重點對照】</h4>
                <p class="text-xs font-mono text-slate-500 dark:text-slate-400 leading-relaxed text-justify">
                  "When switching to GPT-5-mini with stronger reasoning and tool-calling capabilities, A-RAG (Full) achieves superior results across all benchmarks. The consistent improvements of A-RAG over both baseline methods and Naive A-RAG demonstrate that the A-RAG framework is agent-friendly."<br>
                  <span class="text-xs text-indigo-500 font-sans block mt-1">（中譯：當切換至推理和工具調用能力更強的 GPT-5-mini 時，A-RAG (Full) 在所有基準測試中均取得了優異的結果。A-RAG 相比基準方法和 Naive A-RAG 的持續改進，證明了 A-RAG 框架對代理人是極其友善的。）</span>
                </p>
              </div>

              <div class="text-xs text-brand-600 dark:text-brand-400 bg-brand-50 dark:bg-brand-950/30 p-4 rounded-lg border border-brand-200">
                💡 <strong>【讀者提醒】</strong>：看看這組數據！如果我們拿掉 `semantic_search`，準確率掉得最慘烈。這告訴我們，無論 Agent 的字面搜尋（keyword_search）再怎麼強，它依然需要「語意模糊對齊」來做第一步的大範圍概念錨定！兩者交織，才是真正的核心戰術。
              </div>
            </div>
          </section>

          <!-- CHAPTER 6 -->
          <section id="ch6" class="scroll-mt-20 border-t border-slate-300 dark:border-slate-800 pt-12">
            <div class="flex items-center gap-3 mb-6">
              <span class="text-4xl font-extrabold text-brand-500">06</span>
              <h2 class="text-2xl sm:text-3xl font-bold text-slate-800 dark:text-slate-100">第六章：Analysis and Discussion —— 測試時能量擴展與致命迷霧</h2>
            </div>
            
            <div class="space-y-8">
              <div class="pl-4 border-l-4 border-brand-500 space-y-2">
                <h4 class="text-sm font-bold uppercase tracking-wider text-brand-600">【小說化敘事版】</h4>
                <p class="text-slate-600 dark:text-slate-300 text-justify leading-relaxed">
                  在深淵的底層，隱藏著兩大令人著迷的物理規律。
                  <strong>第一規律：能量與時間的極限拉伸（Test-Time Scaling）</strong>。A-RAG 賦予了大腦完全的自主權，這意味著：如果你在「測試時」給它更多的步數預算，大腦就能泛化出更驚人的精準度！實驗發現（圖 4），當最大探索步數從 5 步一路解鎖到 20 步時，GPT-5-mini 的準確率足足拔高了 8%！大腦在更漫長的征途中展現了無與倫比的探索耐力！<br>
                  <strong>第二規律：極致的能量效率（Token Efficiency）</strong>。傳統 RAG 像是無節制排碳的工廠，而 A-RAG (Full) 則是綠色節能典範！比較 A-RAG (Naive) 和 A-RAG (Full) 在 2Wiki 上的表現，前者像個無頭蒼蠅般吞下了高達 45,406 個 Token；而完全體 (Full) 依靠著「只看 Snippet 誘餌、有用才點開」的階層化介面，僅用了 2,930 個 Token 便達成了更優異的戰果（表 3）！這是一次高達 15 倍的驚人能效躍升！<br>
                  但深淵中依然有「迷霧」——<strong>失敗模式分析（Failure Mode Analysis, 圖 5）</strong>。
                  哈基米親手解剖了 A-RAG 在 MuSiQue 上的 100 個失敗案例，發現了一個震撼的結論：<strong>瓶頸轉移了！</strong>
                  傳統 RAG 的瓶頸是「找不到文檔」（50% 失敗於檢索限額）；而 A-RAG 有 82% 的失敗原因，竟然是<strong>「推導鏈條錯誤（Reasoning Chain Error）」</strong>！也就是说，大模型把文章全找齊了，卻在最後一刻因為<strong>「實體混淆大魔王（Entity Confusion, 佔推導錯誤的 40%）」</strong>，把 A 人物的妻子記成了 B 人物的女兒！這說明，未來的升級方向，不再是精進搜尋演算法，而是如何提升大腦的推理清明度！｡>∀<｡✨
                </p>
              </div>

              <!-- Table 3 Token Efficiency HTML Bar -->
              <div class="bg-white dark:bg-slate-900 border border-slate-300 dark:border-slate-800 rounded-xl p-6 glow-shadow space-y-4">
                <h5 class="text-sm font-bold text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                  <span class="inline-block w-3.5 h-3.5 bg-brand-500 rounded-full"></span>
                  2Wiki 關卡消耗的 Token 數量對比 (表 3 數據可視化) —— 越低越節能！
                </h5>
                <div class="space-y-3">
                  <div>
                    <div class="flex justify-between text-xs mb-1 text-slate-500">
                      <span>Naive Agentic RAG (粗暴吞噬所有 Chunk)</span>
                      <span class="font-mono text-red-500 font-bold">45,406 Tokens 🚨</span>
                    </div>
                    <div class="w-full bg-slate-100 dark:bg-slate-800 h-4 rounded-full overflow-hidden">
                      <div class="bg-red-400 h-full" style="width: 100%"></div>
                    </div>
                  </div>
                  <div>
                    <div class="flex justify-between text-xs mb-1 text-slate-500">
                      <span>A-RAG Full (層級化 Snippet 誘餌機制)</span>
                      <span class="font-mono text-green-600 dark:text-green-400 font-bold">2,930 Tokens (省下 15 倍費用！) 🏆</span>
                    </div>
                    <div class="w-full bg-slate-100 dark:bg-slate-800 h-4 rounded-full overflow-hidden">
                      <div class="bg-green-500 h-full" style="width: 6.4%"></div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 論文插圖 Figure 5 / Failure analysis screenshot -->
              <div class="my-8 text-center bg-white dark:bg-slate-900 p-4 border border-slate-300 dark:border-slate-800 rounded-xl max-w-2xl mx-auto">
                <img src="assets/page16.png" alt="Figure 5: Failure Mode Distribution" class="mx-auto rounded-lg shadow-sm border border-slate-200">
                <p class="text-xs text-slate-400 mt-3 font-medium">📜 圖 5 論文原圖對照：A-RAG 失敗分類學 (Table 7 / Table 8 關聯分析圖)</p>
              </div>

              <div class="bg-indigo-50 dark:bg-slate-900 rounded-xl p-6 border border-indigo-200 dark:border-indigo-950 space-y-2">
                <h4 class="text-sm font-bold text-indigo-700 dark:text-indigo-300">【原文重點對照】</h4>
                <p class="text-xs font-mono text-slate-500 dark:text-slate-400 text-justify leading-relaxed">
                  "For Naive RAG, approximately 50% of failures stem from retrieval limitations... indicating the core problem is 'cannot find documents'. In contrast, A-RAG's dominant failure mode (82% on MuSiQue) is reasoning chain errors, shifting the bottleneck to 'found documents but reasoned incorrectly'."<br>
                  <span class="text-xs text-indigo-500 font-sans block mt-1">（中譯：對於 Naive RAG 而言，大約 50% 的失敗源於檢索限制……表明核心問題在於「找不到文件」。相比之下，A-RAG 的主要失敗模式（在 MuSiQue 上佔 82%）是推理鏈條錯誤，這將瓶頸轉移到了「找到了文件但推理錯誤」。）</span>
                </p>
              </div>

              <div class="text-xs text-brand-600 dark:text-brand-400 bg-brand-50 dark:bg-brand-950/30 p-4 rounded-lg border border-brand-200">
                💡 <strong>【讀者提醒】</strong>：這是一個具有歷史意義的轉捩點！以前做 RAG，大家都在比拼誰的 vector 檢索召回率高（Recall）。但這篇論文點醒了所有人：當你的 Agent 框架夠優秀、能把資料找齊之後，大模型的「邏輯推理能力與專注度」才是一切決策質量的真正天花板！
              </div>
            </div>
          </section>

          <!-- CHAPTER 7 -->
          <section id="ch7" class="scroll-mt-20 border-t border-slate-300 dark:border-slate-800 pt-12">
            <div class="flex items-center gap-3 mb-6">
              <span class="text-4xl font-extrabold text-brand-500">07</span>
              <h2 class="text-2xl sm:text-3xl font-bold text-slate-800 dark:text-slate-100">第七章：Conclusion —— 深淵盡頭的新地平線</h2>
            </div>
            
            <div class="space-y-8">
              <div class="pl-4 border-l-4 border-brand-500 space-y-2">
                <h4 class="text-sm font-bold uppercase tracking-wider text-brand-600">【小說化敘事版】</h4>
                <p class="text-slate-600 dark:text-slate-300 text-justify leading-relaxed">
                  探險的尾聲悄然降臨。當我們登上數據深淵的最高峰，回望來時路，一幅壯麗的全新技術地圖緩緩展開。
                  這篇論文用無懈可擊的實證，為我們指明了「大語言模型與外部大數據交互協議」的未來範式。
                  「我們不再需要絞盡腦汁去構造那些極其脆弱、動輒報錯的硬編碼工作流，」哈基米合上筆記本，欣慰地笑道。
                  「只要給大模型一組乾淨、清晰、層級化的 API 介面，讓大模型作決策的大腦在 ReAct 自主循環中自由呼吸、隨任務特性自主探索，就能用最省錢、最精確的方式，解鎖測試時計算（Test-Time Compute）的無窮寶庫。」
                  這不只是一個框架的勝利，更是「相信大模型大腦」這一純粹哲學的偉大勝利！｡>∀<｡✨
                </p>
              </div>

              <div class="bg-slate-100 dark:bg-slate-900 rounded-xl p-6 border border-slate-300 dark:border-slate-800 space-y-3">
                <h4 class="text-sm font-bold text-slate-700 dark:text-slate-300">【技術白話版】</h4>
                <ul class="list-disc list-inside text-sm text-slate-600 dark:text-slate-300 space-y-2 text-justify">
                  <li><strong>範式革命（Paradigm Shift）</strong>：證實了 agentic RAG 作為未來主流範式的可行性。</li>
                  <li><strong>介面重於演算法</strong>：未來的核心研發方向不應是設計更繁複的單一檢索鏈，而是**「設計對大語言模型最友善的多粒度互動 API 協定」**。</li>
                  <li><strong>釋放 Test-Time Scaling 潛能</strong>：在硬體極限下，透過拉長 agent loop 的步數或使用強化學習（Reasoning model 內置思維），能不用重新訓練便可榨乾模型的智商天花板。</li>
                </ul>
              </div>

              <div class="bg-indigo-50 dark:bg-slate-900 rounded-xl p-6 border border-indigo-200 dark:border-indigo-950 space-y-2">
                <h4 class="text-sm font-bold text-indigo-700 dark:text-indigo-300">【原文重點對照】</h4>
                <p class="text-xs font-mono text-slate-500 dark:text-slate-400 text-justify leading-relaxed">
                  "Our findings suggest that future research should focus on designing agent-friendly interfaces rather than complex retrieval algorithms, and explore new interaction paradigms between language models and external knowledge sources."<br>
                  <span class="text-xs text-indigo-500 font-sans block mt-1">（中譯：我們的研究結果表明，未來的研究應該專注於設計對代理人友善的介面，而不是複雜的檢索演算法，並探索語言模型與外部知識源之間全新的互動範式。）</span>
                </p>
              </div>

              <div class="text-xs text-brand-600 dark:text-brand-400 bg-brand-50 dark:bg-brand-950/30 p-4 rounded-lg border border-brand-200">
                💡 <strong>【讀者提醒】</strong>：這句話是整篇論文的最高核心哲學！「別再去設計什麼超複雜的自定義檢索演算法了，去給 Agent 打造一套好用的三層 API 吧！」記住這條心法，能讓你在研發 Agent 時少走半年彎路！
              </div>
            </div>
          </section>

          <!-- CHAPTER 8 -->
          <section id="ch8" class="scroll-mt-20 border-t border-slate-300 dark:border-slate-800 pt-12">
            <div class="flex items-center gap-3 mb-6">
              <span class="text-4xl font-extrabold text-brand-500">08</span>
              <h2 class="text-2xl sm:text-3xl font-bold text-slate-800 dark:text-slate-100">第八章：Limitations —— 探險家未竟的地平線</h2>
            </div>
            
            <div class="space-y-8">
              <div class="pl-4 border-l-4 border-brand-500 space-y-2">
                <h4 class="text-sm font-bold uppercase tracking-wider text-brand-600">【小說化敘事版】</h4>
                <p class="text-slate-600 dark:text-slate-300 text-justify leading-relaxed">
                  即使是最偉大的契書，也有墨水尚未觸及的泛白邊緣。A-RAG 探險小隊雖然取得了一場場大捷，但科學的探索永無止境，前路依然橫亙著幾座尚未征服的險峰：<br>
                  <strong>第一座險峰：工具的多樣性迷宮</strong>。A-RAG 的研究僅打磨了三神兵。然而在真實的江湖中，是否還有著「摘要工具」、「多文檔關聯工具」等更豐富的輔助神兵？不同的工具子集，會如何改變探險家的性格與決策行為？這依然是一片未知的荒野。<br>
                  <strong>第二座險峰：終極大腦的實證缺席</strong>。受限於當前的算力資源，探險小隊主要使用了 GPT-5-mini 作為核心。然而，如果換成擁有毀天滅地推理威力的 GPT-5 Full 或是 Gemini 3 Ultra，這項層級化 API 的威力是否能迎來超越線性的爆發？這值得更多實證。<br>
                  <strong>第三座險峰：任務邊界的拓展</strong>。目前戰火僅在「多跳問答（Multi-hop QA）」領域燃燒。至於事實核查（Fact Verification）、超長對話系統、以及長文本寫作等更考驗耐性的知識密集型戰場，A-RAG 是否依然能立於不敗之地？一切留待未來的英雄去譜寫！(•̀ω•́)y✨
                </p>
              </div>

              <div class="bg-slate-100 dark:bg-slate-900 rounded-xl p-6 border border-slate-300 dark:border-slate-800 space-y-3">
                <h4 class="text-sm font-bold text-slate-700 dark:text-slate-300">【技術白話版】</h4>
                <ul class="list-disc list-inside text-sm text-slate-600 dark:text-slate-300 space-y-2 text-justify">
                  <li><strong>工具消融不夠徹底</strong>：未窮舉所有可能工具（如段落摘要、實體關係定位等），且對不同工具子集對 Agent 行為變化的理論分析尚淺。</li>
                  <li><strong>模型評估極限</strong>：由於算力開銷，未在最頂尖的超大尺寸闭源推理模型（如 GPT-5 Full / Gemini Ultra）上進行完整吞吐與精度的上限驗證。</li>
                  <li><strong>任務廣度受限</strong>：本研究專注於 multi-hop QA 數據集，尚未在開放域長對話、事實核查或複雜摘要生成等任務中做通用性檢驗。</li>
                </ul>
              </div>

              <div class="bg-indigo-50 dark:bg-slate-900 rounded-xl p-6 border border-indigo-200 dark:border-indigo-950 space-y-2">
                <h4 class="text-sm font-bold text-indigo-700 dark:text-indigo-300">【原文重點對照】</h4>
                <p class="text-xs font-mono text-slate-500 dark:text-slate-400 text-justify leading-relaxed">
                  "Due to computational resource constraints, we have not validated the framework on larger and more powerful models such as GPT-5, and Gemini-3. Given that A-RAG is specifically designed for reasoning models with strong tool-use capabilities, we anticipate that performance gains would be more pronounced with these frontier models..."<br>
                  <span class="text-xs text-indigo-500 font-sans block mt-1">（中譯：由於計算資源的限制，我們尚未在更大、更強大的模型（如 GPT-5 和 Gemini-3）上驗證該框架。鑑於 A-RAG 是專門為具有強大工具調用能力的推理模型設計的，我們預計在這些前沿模型上的效能提升會更加顯著……）</span>
                </p>
              </div>

              <div class="text-xs text-brand-600 dark:text-brand-400 bg-brand-50 dark:bg-brand-950/30 p-4 rounded-lg border border-brand-200">
                💡 <strong>【讀者提醒】</strong>：論文承認「未在大模型完整版上做測試」這是一件大好事！這為我們的科研報告提供了最完美的「Future Work 展望」素材。寫作業時可以把這點拿出來申論，顯得你讀得非常細緻且極具批判性思考！
              </div>
            </div>
          </section>

          <!-- CHAPTER 9 -->
          <section id="ch9" class="scroll-mt-20 border-t border-slate-300 dark:border-slate-800 pt-12">
            <div class="flex items-center gap-3 mb-6">
              <span class="text-4xl font-extrabold text-brand-500">09</span>
              <h2 class="text-2xl sm:text-3xl font-bold text-slate-800 dark:text-slate-100">第九章：Ethical Considerations —— 探險者的自律</h2>
            </div>
            
            <div class="space-y-8">
              <div class="pl-4 border-l-4 border-brand-500 space-y-2">
                <h4 class="text-sm font-bold uppercase tracking-wider text-brand-600">【小說化敘事版】</h4>
                <p class="text-slate-600 dark:text-slate-300 text-justify leading-relaxed">
                  在追求極致智慧的路上，自律是探險家手中最堅實的護盾。
                  這份探險契書沒有染上任何道德與偏見的污點。
                  「我們使用的所有地圖與數據集，都是江湖上完全公開、經過無數先賢嚴格審查的基準測試，」哈基米莊嚴地宣告。
                  此項研究不涉及任何私密個人數據的採集，更沒有招募人類受試者。
                  作為 RAG 江湖底層方法學的純淨貢獻，這項設計本身就像是一把純白的手槍——它不具備主動編造謠言的邪惡本能，它的安全防線，完全與底層承載它的神明（大語言模型本身的對齊機制）同生共死。只要大腦保持善良，A-RAG 便是照亮這片數據海洋最溫柔的純白聖光。｡>∀<｡✨
                </p>
              </div>

              <div class="bg-slate-100 dark:bg-slate-900 rounded-xl p-6 border border-slate-300 dark:border-slate-800 space-y-3">
                <h4 class="text-sm font-bold text-slate-700 dark:text-slate-300">【技術白話版】</h4>
                <ul class="list-disc list-inside text-sm text-slate-600 dark:text-slate-300 space-y-2 text-justify">
                  <li><strong>公開基準測試（Public Benchmarks）</strong>：完全基於公開学术數據集，無版權或個人隱私洩露風險。</li>
                  <li><strong>無新增倫理風險</strong>：作為系統介面層級的學術框架，A-RAG 本身不具備數據生成或自我對齊偏離能力，其倫理邊界完全與其調用的底層 LLM 對齊機制綁定。</li>
                </ul>
              </div>

              <div class="bg-indigo-50 dark:bg-slate-900 rounded-xl p-6 border border-indigo-200 dark:border-indigo-950 space-y-2">
                <h4 class="text-sm font-bold text-indigo-700 dark:text-indigo-300">【原文重點對照】</h4>
                <p class="text-xs font-mono text-slate-500 dark:text-slate-400 text-justify leading-relaxed">
                  "As a methodological contribution to RAG systems, our approach does not introduce additional ethical risks beyond those inherent to the underlying language models."<br>
                  <span class="text-xs text-indigo-500 font-sans block mt-1">（中譯：作為對 RAG 系統的方法學貢獻，我們的方法沒有引入超出底層語言模型固有倫理風險之外的額外風險。）</span>
                </p>
              </div>

              <div class="text-xs text-brand-600 dark:text-brand-400 bg-brand-50 dark:bg-brand-950/30 p-4 rounded-lg border border-brand-200">
                💡 <strong>【讀者提醒】</strong>：這部分是標準的學術論文安全聲明。在學術寫作中，特別是當你的研究涉及 LLM、多輪互動和外部數據拉取時，單獨列出這項聲明能保證你的作業和論文能順利通過學術委員會與教授的審核，非常加分！
              </div>
            </div>
          </section>

          <!-- CHAPTER 10 -->
          <section id="ch10" class="scroll-mt-20 border-t border-slate-300 dark:border-slate-800 pt-12">
            <div class="flex items-center gap-3 mb-6">
              <span class="text-4xl font-extrabold text-brand-500">10</span>
              <h2 class="text-2xl sm:text-3xl font-bold text-slate-800 dark:text-slate-100">第十章：Appendix —— 探險寶典與諸神之契</h2>
            </div>
            
            <div class="space-y-8">
              <div class="pl-4 border-l-4 border-brand-500 space-y-2">
                <h4 class="text-sm font-bold uppercase tracking-wider text-brand-600">【小說化敘事版】</h4>
                <p class="text-slate-600 dark:text-slate-300 text-justify leading-relaxed">
                  在探險家筆記的最後，附錄中密密麻麻地記載著上古對決的詳細配置。
                  這是一本供後世冒險者膜拜的「探險寶典」（表 5 與圖 7/8 說明）。
                  寶典中寫道：所有被召喚出來的 baseline 基底方法，都使用了最高規格的 top-k=5 精細召回，並分配了至少 16,384 個 token 的思維腦空間，絕不讓任何一個方法因為「腦溢出（Reasoning Truncation）」而含冤落敗。
                  微軟的 GraphRAG 配置了 1200 尺寸的厚實分塊，HippoRAG2 採用了「事實與相似度關聯節點圖」，而 A-RAG 則在簡單幹練的 ReAct 循環中配戴上了我們最引以為傲的 `keyword_search`、`semantic_search` 與 `chunk_read` 三段式 Prompt 工具調用契書（見圖 7 說明）。這本寶典保障了這場浩大對決的絕對公正與純粹。｡>∀<｡✨
                </p>
              </div>

              <!-- 論文插圖 Figure 7 / Appendix E Screenshot -->
              <div class="my-8 text-center bg-white dark:bg-slate-900 p-4 border border-slate-300 dark:border-slate-800 rounded-xl max-w-2xl mx-auto">
                <img src="assets/page17.png" alt="Figure 7: Prompt templates" class="mx-auto rounded-lg shadow-sm border border-slate-200">
                <p class="text-xs text-slate-400 mt-3 font-medium">📜 論文原圖對照：Appendix E 中的 Agent 基礎系統 Prompt 與工具 schema 模板說明</p>
              </div>

              <div class="bg-slate-100 dark:bg-slate-900 rounded-xl p-6 border border-slate-300 dark:border-slate-800 space-y-3">
                <h4 class="text-sm font-bold text-slate-700 dark:text-slate-300">【技術白話版】</h4>
                <ul class="list-disc list-inside text-sm text-slate-600 dark:text-slate-300 space-y-2 text-justify">
                  <li><strong>實驗重現細節（表 5）</strong>：基準模型 HippoRAG 採用了 `facts_and_sim_passage_node` 設定，對應 `qa_top_k=5`；LinearRAG 採用官方釋出的 `all-mpnet-base-v2` 嵌入模型。</li>
                  <li><strong>統一評核標準</strong>：為防邏輯思維中斷（reasoning truncation），實驗將上下文限額一律設在 16k 以上。評估基準一律採用強大的 GPT-5-mini 作為最終判定官，消除人為評分主觀誤差。</li>
                </ul>
              </div>

              <div class="bg-indigo-50 dark:bg-slate-900 rounded-xl p-6 border border-indigo-200 dark:border-indigo-950 space-y-2">
                <h4 class="text-sm font-bold text-indigo-700 dark:text-indigo-300">【原文重點對照】</h4>
                <p class="text-xs font-mono text-slate-500 dark:text-slate-400 text-justify leading-relaxed">
                  "All baseline results are reproduced locally under a unified evaluation setting. All methods use top-k=5 for retrieval and max_tokens >= 16384 to prevent reasoning truncation."<br>
                  <span class="text-xs text-indigo-500 font-sans block mt-1">（中譯：所有基準結果均在統一評核設置下於本地重現。所有方法檢索均採用 top-k=5，且最大 tokens 設為 16384 以上以防止推理截斷。）</span>
                </p>
              </div>

              <div class="text-xs text-brand-600 dark:text-brand-400 bg-brand-50 dark:bg-brand-950/30 p-4 rounded-lg border border-brand-200">
                💡 <strong>【讀者提醒】</strong>：這段附錄展示了頂級學術論文的嚴謹。在做自建 RAG 專案或寫學校期末報告時，一定要把所有 Baseline 方法的**重現配置（Reproduction parameters）**交代得清清楚楚。只有在完全一致的上下文長度和檢索 top-k 限制下，做出來的比較數據才具有真正的說服力喔！
              </div>
            </div>
          </section>

        </div>

        <!-- 最終附加章節：一頁式總結與實戰心法 -->
        <div class="space-y-12 border-t-2 border-slate-300 dark:border-slate-800 pt-16">
          
          <!-- 一頁式總結 -->
          <section id="one-page-summary" class="bg-gradient-to-br from-brand-500/10 via-indigo-500/5 to-transparent rounded-2xl p-6 sm:p-8 border border-brand-300 dark:border-indigo-950/50 dark:bg-slate-900/50 scroll-mt-20">
            <h2 class="text-2xl font-bold text-slate-800 dark:text-slate-100 flex items-center gap-2 mb-4">
              <span>📝</span> 探險者契約：A-RAG 一頁式總結
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm text-slate-600 dark:text-slate-300">
              <div class="space-y-3">
                <p class="font-semibold text-slate-800 dark:text-slate-200 text-base">🔑 核心痛點：傳統 RAG 的「代碼鎖死」與「消化不良」</p>
                <p class="text-justify">
                  傳統一次性 RAG 會粗暴地把大量 token 塞入 LLM 導致嚴重噪音，而現行的 Workflow 多輪 RAG 則透過人工硬編碼的工作流控制模型，使得模型缺乏執行期（Runtime）的動態修正能力，遇到多步推理難題時容易迷路且產生巨大費用。
                </p>
              </div>
              <div class="space-y-3">
                <p class="font-semibold text-slate-800 dark:text-slate-200 text-base">💡 解放之路：大腦自主與階層式 API 三神兵</p>
                <p class="text-justify">
                  A-RAG 將知識庫轉化為三個層級介面：
                  <strong>keyword_search</strong> 定位微觀實體並回傳極短 snippet 誘餌；
                  <strong>semantic_search</strong> 定位語意概念並回傳 snippet 誘餌；
                  <strong>chunk_read</strong> 精讀全文。
                  透過 ReAct 極簡大腦自主循環，在省下高達 15 倍 token 的同時，於 MuSiQue 取得 74.1% 的歷史新高準確度！
                </p>
              </div>
            </div>
          </section>

          <!-- 10 個關鍵術語對照表 -->
          <section id="key-terms" class="scroll-mt-20 bg-white dark:bg-slate-900 rounded-2xl p-6 sm:p-8 border border-slate-300 dark:border-slate-800">
            <h2 class="text-2xl font-bold text-slate-800 dark:text-slate-100 flex items-center gap-2 mb-6">
              <span>📋</span> 10 個關鍵術語中英對照表
            </h2>
            <div class="overflow-x-auto rounded-xl border border-slate-300 dark:border-slate-800">
              <table class="w-full text-left text-sm text-slate-500 dark:text-slate-400">
                <thead class="bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200">
                  <tr>
                    <th class="p-3 border-b border-slate-300 dark:border-slate-700">#</th>
                    <th class="p-3 border-b border-slate-300 dark:border-slate-700">繁體中文翻譯</th>
                    <th class="p-3 border-b border-slate-300 dark:border-slate-700">英文原文 (Original Term)</th>
                    <th class="p-3 border-b border-slate-300 dark:border-slate-700">冒險筆記直覺意義</th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">1</td>
                    <td class="p-3 font-medium text-slate-800 dark:text-slate-100">檢索增強生成</td>
                    <td class="p-3 font-mono">Retrieval-Augmented Generation (RAG)</td>
                    <td class="p-3">給住在水晶球裡的大腦模型發配一本參考工具書。</td>
                  </tr>
                  <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">2</td>
                    <td class="p-3 font-medium text-slate-800 dark:text-slate-100">代理式檢索增強生成</td>
                    <td class="p-3 font-mono">Agentic RAG</td>
                    <td class="p-3">給大模型裝上雙手和工具，讓它自己翻書找答案。</td>
                  </tr>
                  <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">3</td>
                    <td class="p-3 font-medium text-slate-800 dark:text-slate-100">階層式檢索介面</td>
                    <td class="p-3 font-mono">Hierarchical Retrieval Interfaces</td>
                    <td class="p-3">將知識切割為微觀、中觀和宏觀的漸進式 API。</td>
                  </tr>
                  <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">4</td>
                    <td class="p-3 font-medium text-slate-800 dark:text-slate-100">測試時計算擴展</td>
                    <td class="p-3 font-mono">Test-Time Scaling</td>
                    <td class="p-3">不重新訓練，只靠拉長探險步數和思維深度來暴漲智商。</td>
                  </tr>
                  <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">5</td>
                    <td class="p-3 font-medium text-slate-800 dark:text-slate-100">關鍵字搜尋</td>
                    <td class="p-3 font-mono">keyword_search</td>
                    <td class="p-3">微觀精確雷達。只靠精確字匹配定位人名和特殊代號。</td>
                  </tr>
                  <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">6</td>
                    <td class="p-3 font-medium text-slate-800 dark:text-slate-100">語意搜尋</td>
                    <td class="p-3 font-mono">semantic_search</td>
                    <td class="p-3">中觀語意導航。算向量夾角，專治「字不同但意同」的概念。</td>
                  </tr>
                  <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">7</td>
                    <td class="p-3 font-medium text-slate-800 dark:text-slate-100">區塊閱讀</td>
                    <td class="p-3 font-mono">chunk_read</td>
                    <td class="p-3">高精度精讀顯微鏡。看過誘餌 snippet 後才加載完整全文。</td>
                  </tr>
                  <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">8</td>
                    <td class="p-3 font-medium text-slate-800 dark:text-slate-100">上下文追蹤器</td>
                    <td class="p-3 font-mono">Context Tracker</td>
                    <td class="p-3">已讀地圖。防止模型重複精讀已讀過的區塊而造成浪費。</td>
                  </tr>
                  <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">9</td>
                    <td class="p-3 font-medium text-slate-800 dark:text-slate-100">推導鏈條錯誤</td>
                    <td class="p-3 font-mono">Reasoning Chain Error</td>
                    <td class="p-3">書全翻對了，大腦卻在最後一步推算時糊塗算錯。</td>
                  </tr>
                  <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">10</td>
                    <td class="p-3 font-medium text-slate-800 dark:text-slate-100">實體混淆</td>
                    <td class="p-3 font-mono">Entity Confusion</td>
                    <td class="p-3">推導出錯的最大元兇。把 A 的妻子記成 B 的女兒。</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </section>

          <!-- 核心貢獻與限制 -->
          <section id="contributions" class="scroll-mt-20 grid grid-cols-1 md:grid-cols-2 gap-8">
            
            <!-- 核心貢獻 -->
            <div class="bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-800 rounded-2xl p-6 sm:p-8">
              <h3 class="text-xl font-bold text-slate-800 dark:text-slate-100 flex items-center gap-2 mb-4">
                <span>🏆</span> 論文三大核心貢獻
              </h3>
              <ul class="space-y-3 text-sm text-slate-600 dark:text-slate-300 text-justify">
                <li class="flex gap-2">
                  <span class="text-brand-500 font-bold">1.</span>
                  <span><strong>範式革命（Paradigm Shift）</strong>：首次大膽宣稱，RAG 研發的核心不應是發明更繁重的圖譜演算法，而是應該將完全的戰術決策自主權交還給大模型探險家。</span>
                </li>
                <li class="flex gap-2">
                  <span class="text-brand-500 font-bold">2.</span>
                  <span><strong>實作 A-RAG 框架</strong>：精巧設計出對代理極度友善、具有漸進式資訊揭露（Progressive disclosure）機制的「三神兵介面」，成功擊碎了微軟 GraphRAG 等複雜體系的實效神話。</span>
                </li>
                <li class="flex gap-2">
                  <span class="text-brand-500 font-bold">3.</span>
                  <span><strong>解碼 Test-Time Scaling 規律</strong>：首次量化分析了 Agentic RAG 在「步數解鎖」與「推理 Effort 解鎖」下的上升曲線，為下一代推理模型的研究鋪平了康莊大道。</span>
                </li>
              </ul>
            </div>

            <!-- 論文限制 -->
            <div class="bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-800 rounded-2xl p-6 sm:p-8">
              <h3 class="text-xl font-bold text-slate-800 dark:text-slate-100 flex items-center gap-2 mb-4">
                <span>⚠️</span> 論文三大核心限制
              </h3>
              <ul class="space-y-3 text-sm text-slate-600 dark:text-slate-300 text-justify">
                <li class="flex gap-2">
                  <span class="text-red-500 font-bold">1.</span>
                  <span><strong>工具完備性尚未探索</strong>：目前實驗僅在三種基礎工具上實作。尚未探討「文檔摘要工具」、「跳轉超連結追蹤工具」等多樣化配置對 Agent 行為產生的深遠影響。</span>
                </li>
                <li class="flex gap-2">
                  <span class="text-red-500 font-bold">2.</span>
                  <span><strong>極致大腦驗證缺席</strong>：受限於 2026 年初的實驗算力，尚未在大規模超強推理模型（如 GPT-5 Full 或 Gemini 3 Ultra）上驗證其爆發極限，實證研究有待補充。</span>
                </li>
                <li class="flex gap-2">
                  <span class="text-red-500 font-bold">3.</span>
                  <span><strong>場景廣度有待擴展</strong>：多數亮眼數據來自「多跳推理問答」。其在開放式長文寫作、極致嚴謹的事實核查（Fact verification）等場景中的通用表現仍待學界進一步挖掘。</span>
                </li>
              </ul>
            </div>

          </section>

          <!-- 我如果要把它用在自己的 RAG agent 專案，應該學到什麼 -->
          <section id="takeaways" class="scroll-mt-20 bg-gradient-to-br from-indigo-500/10 via-brand-500/5 to-transparent border border-brand-400 dark:border-brand-900 rounded-2xl p-6 sm:p-8">
            <h2 class="text-2xl font-bold text-slate-800 dark:text-slate-100 flex items-center gap-2 mb-6">
              <span>💻</span> 銘銘咩的自建 RAG Agent 專案實戰心法！
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-sm text-slate-600 dark:text-slate-300">
              
              <div class="bg-white/50 p-5 rounded-xl border border-slate-300 dark:bg-slate-900/50 dark:border-slate-800 space-y-2">
                <h4 class="font-bold text-slate-800 dark:text-slate-100">🚀 1. 拋棄死板的 SOP 框架</h4>
                <p class="text-xs text-justify leading-relaxed">
                  別再用一堆複雜的硬代碼流程去限制你的 LLM Agent。只要寫一組清晰的 Tool schema（包含 keyword_search, semantic_search, chunk_read），在 Prompt 裡用極簡的 ReAct 教導它「思考 ➔ 行動 ➔ 觀察」，大模型自己就能找出超越你寫死工作流的完美探索路徑！
                </p>
              </div>

              <div class="bg-white/50 p-5 rounded-xl border border-slate-300 dark:bg-slate-900/50 dark:border-slate-800 space-y-2">
                <h4 class="font-bold text-slate-800 dark:text-slate-100">💎 2. 實作「漸進式揭露」</h4>
                <p class="text-xs text-justify leading-relaxed">
                  絕對不要一開始就把向量匹配到的 1,000-token Chunk 全部塞進 Prompt 裡！這不僅會帶來雜訊，還會榨乾你的荷包。一定要先回傳 snippet 句子片段作為「誘餌」，讓 Agent 判定有需要，再發起 `chunk_read` 請求去精讀全文。這能幫你省下十幾倍的費用！
                </p>
              </div>

              <div class="bg-white/50 p-5 rounded-xl border border-slate-300 dark:bg-slate-900/50 dark:border-slate-800 space-y-2">
                <h4 class="font-bold text-slate-800 dark:text-slate-100">🛡️ 3. 務必加上「已讀 Tracker」</h4>
                <p class="text-xs text-justify leading-relaxed">
                  大腦模型在自主多輪探索時，難免會陷入重複精讀同一個 Chunk 的「鬼打牆」狀態。在你的 Agent 後台代碼裡維護一個簡單的 `Cread` Set。一旦發現它重複精讀已讀過的區塊，直接在後台攔阻，並回覆提示引導它去看歷史消息，就能完美封堵這個高昂的 Token 漏洞！
                </p>
              </div>

            </div>
          </section>

        </div>

        <!-- 頁尾 -->
        <footer class="text-center py-12 border-t border-slate-300 dark:border-slate-800 text-xs text-slate-400">
          <p>© 2026 哈基米學術筆記. 本著溫暖、工程腦、有耐心的原則，陪銘銘咩一起把學術冒險做完！(｡♥‿♥｡)✨</p>
        </footer>

      </main>

    </div>
  </div>

  <script>
    // 亮色/暗色切換邏輯
    const themeToggleBtn = document.getElementById('themeToggle');
    const sunIcon = document.getElementById('sunIcon');
    const moonIcon = document.getElementById('moonIcon');

    // 檢查本地存儲或系統偏好
    if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      document.documentElement.classList.add('dark');
      sunIcon.classList.remove('hidden');
      moonIcon.classList.add('hidden');
    } else {
      document.documentElement.classList.remove('dark');
      sunIcon.classList.add('hidden');
      moonIcon.classList.remove('hidden');
    }

    themeToggleBtn.addEventListener('click', () => {
      // 切換
      if (document.documentElement.classList.contains('dark')) {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('color-theme', 'light');
        sunIcon.classList.add('hidden');
        moonIcon.classList.remove('hidden');
      } else {
        document.documentElement.classList.add('dark');
        localStorage.setItem('color-theme', 'dark');
        sunIcon.classList.remove('hidden');
        moonIcon.classList.add('hidden');
      }
    });

    // 簡單的浮動 TOC 高亮
    const sections = document.querySelectorAll('section');
    const tocLinks = document.querySelectorAll('.toc-link');

    window.addEventListener('scroll', () => {
      let currentId = '';
      sections.forEach(section => {
        const sectionTop = section.offsetTop - 120;
        if (pageYOffset >= sectionTop) {
          currentId = section.getAttribute('id');
        }
      });

      tocLinks.forEach(link => {
        link.classList.remove('text-brand-600', 'dark:text-brand-400', 'font-bold', 'bg-slate-100', 'dark:bg-slate-800');
        if (link.getAttribute('href') === `#${currentId}`) {
          link.classList.add('text-brand-600', 'dark:text-brand-400', 'font-bold', 'bg-slate-100', 'dark:bg-slate-800');
        }
      });
    });
  </script>
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML report successfully generated and saved to:", html_path)

# 17_deepseek_Kimi

> DeepSeek 戰略心智與公開敘事研究：梁文鋒講話、開源/剋制定價邏輯、融資事件核查與產業串聯評論。  
> 本專案是 **知識研究 repo**，不是投資建議、不是交易信號源。

- 狀態：Active Knowledge Project
- 工作方式：CLI-first、Markdown-first、多模型角色分工（Writer / Critic / Evidence Checker / Synthesizer）
- Hub 索引：[`30_investment_hub`](../30_investment_hub/README.md)
- 最後更新：2026-07-27（角色清單式 Review **已暫停**）

## Project Identity

| 項 | 值 |
|---|---|
| Project name | DeepSeek 梁文鋒講話與戰略敘事 |
| Canonical path | `/home/arislee1979/0_project/17_deepseek_Kimi` |
| Knowledge Stage | **Analysis**（角色清單式 Review **已暫停**） |
| Last updated | 2026-07-27 |
| Current Synthesis | 尚未建立正式 `synthesis/`；目前最接近權威拆解見下方 |

## Core Question

**DeepSeek 的真實目標函數與商業邏輯是什麼？公開外傳講話、融資節奏與二手產業評論（如 StockWe）分別提供了哪些可核驗事實、有條件推論與過度敘事？**

可拆成三個子問題：

1. 梁文鋒四小時交流稿主張了哪些可複用的戰略原則（願景、剋制、開源、AGI 階梯、定價）？
2. 「第二輪融資暫停」新聞鏈的可信度與因果邊界在哪裡？
3. 把 DeepSeek 與 NVIDIA / 芯片封鎖做成「商業協同」的敘事，哪些成立、哪些需打折？

## Scope

### Included

- 梁文鋒外傳講話精校與心智模型拆解。
- 與融資、開源、API 定價、AGI 路線相關的公開報道核查。
- 二手評論（X / 財經自媒體）的事實層 vs 故事層分離。
- 與「中國製造式降本 / 傑文斯悖論 / 開源擴散」相關的產業邏輯討論（**研究級**，非持倉建議）。

### Excluded

- 不提供買賣 DeepSeek 相關標的或美股（$NVDA 等）的投資建議。
- 不以社群轉述自動當成公司官方立場。
- 不把本 repo 做成完整 AI 產業數據庫或每日新聞流水賬。
- 不在此 repo 內存放 API key、未授權付費全文或敏感個資。

## Why This Matters

- 理解 DeepSeek 的「剋制即戰略」是否自洽，影響對開源模型、算力需求與中美 AI 競爭的判斷框架。
- 外傳講話已成為市場敘事的原材料；需要把 **原文 → 拆解 → 新聞 → 二手串聯** 分層，避免把評論當事實。
- 為 Hub 與其他產業專案（如產能/算力）提供可引用的 Current Synthesis 錨點。

## Current Position（短摘要）

1. Writer 將講話壓縮為 **Maximize P(AGI) s.t. 合理利潤與團隊**——**好用的詮釋標籤**，Critic 判定為有條件成立，非已證目標函數。  
2. 「十個月回本／六倍利潤下開源不衝突」在原文層成立；升成「商業模式已驗證」則資料不足。  
3. Critic 最弱三環：**(a)** 轉寫當準官方 **(b)** 單一目標函數 **(c)** 開源⟂收入依賴脆弱假設鏈。  
4. 2026-07-25 Bloomberg 線：二輪融資口頭暫停、部分與外傳有關；強化「敘事控制 vs 分享戰略」張力。  
5. 正式 Current Synthesis 仍未建立；進入 Synthesis 前需完成 Evidence Checker。

## Current Synthesis

- **正式 Current Synthesis**：尚未建立（目標路徑：`synthesis/04_current_synthesis.md`）。
- **現階段主讀（Analysis；Review 流水線暫停）**：
  - [1_speech_deep_analysis.md](1_speech_deep_analysis.md) — 講話心智模型拆解
  - [2_StockWe_融資暫停串聯分析_核查.md](2_StockWe_融資暫停串聯分析_核查.md) — 事件核查
  - [reviews/02_critic_review.md](reviews/02_critic_review.md) — **非必讀**（格式已暫停，價值評為低）

未再指示前：不寫 `reviews/03_*`、不硬跑角色審查輪。

## Evidence Base（現有材料）

| ID | 證據／來源 | 類型 | 支持或反對什麼 | 可信度 | 日期 |
|---|---|---|---|---|---|
| S01 | [0_speech.md](0_speech.md) 梁文鋒四小時發言精校（大宇 @BTCdayu） | Lead / 二次轉寫 | 開源、剋制、十個月回本、AGI 階梯等主張 | 中（非官方錄音原檔；轉寫精校） | 2026-07 外傳 |
| S02 | [1_speech_deep_analysis.md](1_speech_deep_analysis.md) | Secondary 分析 | 將講話整理為可複用戰略模型 | 中高（依賴 S01） | 2026-07-24 |
| S03 | Bloomberg / Reuters 等二輪融資暫停報道（見 2_ 文內鏈） | Secondary 新聞（匿名信源） | 口頭暫停第二輪；部分因言論外傳 | 中高（主流媒體一致，非官方） | 2026-07-25 |
| S04 | StockWe 推文 2081201760669200886（全文見 2_） | Lead / 評論 | 製造業降本、與 NVDA 協同、政策海關敘事 | 低–中（觀點文，非一手事實） | 2026-07-26 |
| S05 | [2_StockWe_融資暫停串聯分析_核查.md](2_StockWe_融資暫停串聯分析_核查.md) | Evidence check + 評論 | 事實邊界與 StockWe 評價 | 中高（核查層） | 2026-07-27 |
| S06 | [reviews/02_critic_review.md](reviews/02_critic_review.md) | Critic 審查 | 挑戰 Writer 前提、主張分級、替代解釋 | 中高（方法論層） | 2026-07-27 |

來源優先級：Primary（公司官方 / 監管）> Secondary（主流報道、有方法的分析）> Lead（X、論壇、未驗證轉寫）。

## Open Question

**外傳精校稿在定價／開源／算力數字上失真風險有多高？以及二輪融資暫停是否已有任何可核驗的公司側確認？**

## Model Positions

| 模型／角色 | 核心主張 | 最強證據 | 最大弱點 |
|---|---|---|---|
| Writer（`1_`） | 剋制 + 開源 + AGI 主線是自洽 OS | S01 內在一致性；條件句拆假對立 | 依賴外傳轉寫；總綱語氣偏「已證實」 |
| Critic（`reviews/02_`） | 宜當假說目錄；三弱環＝來源／單一目標函數／開源假設鏈 | 原文張力抽樣；替代解釋 A–C | 未做系統性外部事實核查 |
| Evidence Checker（`2_` 部分；正式輪未完） | 停融資方向可信、非官方；惡意未證實 | S03 多家轉述一致 | 尚未出 `03_evidence_check.md` |
| Synthesizer | 尚未產出正式 Current Synthesis | — | — |

## Falsification Conditions

以下任一發生，應強制修訂結論：

- DeepSeek 官方否認「暫停第二輪融資」或給出不同原因。
- 公司改走高溢價閉源、或明確放棄頂級模型開源。
- 出現可驗證的官方錄音/紀要，證明外傳稿系統性歪曲原意。
- API 定價邏輯被證偽（長期明顯虧本補貼或改為利潤最大化）。
- 第二輪融資在無外傳爭議下仍無限期停擺，且公開原因變為監管/制裁/財務危機。

## Decision Log

| 日期 | 決定 | 理由 | 影響文件 |
|---|---|---|---|
| 2026-07-24 | 建立講話精校與深度拆解 | 外傳內容需結構化，避免只在聊天層 | `0_speech.md`, `1_speech_deep_analysis.md` |
| 2026-07-27 | 歸檔 StockWe 並做融資新聞核查 | 區分事實層與故事層 | `2_StockWe_融資暫停串聯分析_核查.md` |
| 2026-07-27 | 按 Hub 規範補齊專案骨架 | 升級為正式知識專案，可被 Hub 索引 | `README.md`, `AGENTS.md`, `00_inbox.md` |
| 2026-07-27 | 將全站內容編譯為 HTML 互動研究門戶並發佈至 GitHub | 滿足視覺化閱讀、互動對比與 GitHub Live Report 需求 | `index.html`, `style.css`, `script.js`, `*.html` |
| 2026-07-27 | 完成 Critic 輪；階段 Analysis → Review | 挑戰 Writer 前提與過度推論，不覆寫原稿 | `reviews/02_critic_review.md` |
| 2026-07-27 | **暫停**角色清單式 Review 流水線 | 老大判定 `02_` 價值低；未再指示前不寫 03／不自動跑角色輪 | `AGENTS.md` §4、本 README |

## Next Action

**暫停角色清單式 Review。** 未再指示前不產出 `reviews/03_*`、不硬跑 Critic／Evidence／Synthesizer。有新材料或真正洞見時再落短檔；否則維持現狀（主讀 `0_`／`1_`／`2_`）。

## Suggested Reading Order

1. 本 `README.md`（身份、範圍、階段、下一步）
2. `index.html`（HTML 互動式戰略研究儀表板與文獻導覽首頁）
3. `AGENTS.md`（作業規則；含 Review 暫停）
4. `00_inbox.md` / `00_inbox.html`（未升級材料）
5. `0_speech.md` / `0_speech.html`（原文）
6. `1_speech_deep_analysis.md` / `1_speech_deep_analysis.html`（分析）
7. `2_StockWe_融資暫停串聯分析_核查.md` / 對應 html（事件核查）
8. `reviews/02_critic_review.md` — **非必讀**（已標價值低／格式暫停）

## Directory Layout（目標）

```text
17_deepseek_Kimi/
├── README.md / README.html
├── AGENTS.md / AGENTS.html
├── 00_inbox.md / 00_inbox.html
├── 0_speech.md / 0_speech.html
├── 1_speech_deep_analysis.md / 1_speech_deep_analysis.html
├── 2_StockWe_融資暫停串聯分析_核查.md / 2_StockWe_...html
├── index.html            # 互動式戰略研究儀表板與文獻導覽首頁
├── style.css             # 深色矽谷科技風 (Silicon Dark Theme) CSS
├── script.js             # 頁面分頁與導航微交互腳本
├── generate_site.py      # Python 零外部依賴 HTML 靜態編譯器
├── sources/              # 可選：來源登記與摘錄
├── research/             # 可選：後續分析輪次
├── reviews/
│   └── 02_critic_review.md   # 已完成
│   # 03_evidence_check.md    # Next Action
└── synthesis/            # 待建立 04_current_synthesis.md
```

資料夾可按需創建；**文件少但角色清楚優於空殼目錄**。Review 產物放 `reviews/`，Synthesis 完成後再更新 Hub 的 Current Synthesis 連結。

## CLI Task Format

```text
目標：
輸入檔：
輸出檔：
模型角色：
不可改動：
驗收條件：
```

## 與 Hub 的關係

- 詳細證據與全文只留在本 repo。
- Hub 只登記：路徑、Knowledge Stage、Current Synthesis 鏈接、一個 Open Question / Next Action、Last Updated。
- 勿在 Hub 內複製本專案長文。

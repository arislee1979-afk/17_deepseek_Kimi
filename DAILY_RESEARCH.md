# Daily Research Intake — 17 DeepSeek / Kimi

> 排程執行者：ChatGPT Scheduled Task（Asia/Taipei 07:00），**不是 GitHub Actions**。
> 寫入目標：`00_inbox.md`。

## 流程

```text
07:00 自動研究
     ↓
沒有重大 delta
→ 只回報，不寫 GitHub

有重大 delta
     ↓
產生 Repo Update Candidate
     ↓
等待使用者明確回覆 YES
     ↓
重新讀取 main 最新版 00_inbox.md
     ↓
只更新 00_inbox.md
     ↓
commit main

若達正式研究升級門檻
     ↓
只提示「建議從 inbox 升級」
     ↓
不得自動建立 research / review / synthesis
```

## 單次 YES 的權限邊界

- `YES` 只批准**該次日報列出的 Candidate**寫入 `00_inbox.md`。
- 寫入前必須重新 fetch `00_inbox.md`，使用最新 blob SHA，避免覆蓋其他修改。
- 不得因 `YES` 修改 README、AGENTS、HTML、正式分析、Hub、Issue、PR 或其他檔案。
- 不得自動升級 Knowledge Stage、Open Question、Next Action 或 Current Synthesis。
- commit message 應描述本次 research intake，不做無關改動。

## 研究範圍

以 README 的核心問題為第一優先：**DeepSeek 的真實目標函數與商業邏輯，以及外傳講話、融資節奏、算力約束與中美 AI 競爭敘事中，哪些是可核驗事實、哪些只是歸因或工作假說。**

每日優先追蹤：

1. DeepSeek 融資、IPO、梁文鋒公開／外傳談話，以及外傳來源鏈的一手驗證。
2. DeepSeek、Kimi／Moonshot 的新模型、開源權重、授權、API 定價、訂閱、限流與算力容量。
3. DeepSeek 自研推理晶片、Huawei Ascend、國產 GPU 採用，以及 NVIDIA／CUDA／TileLang 路徑依賴。
4. 美國對中國 AI 晶片出口管制、第三國轉運執法，以及 NVIDIA／HBM／SK hynix／台日韓友岸供應鏈。
5. 中國模型與美國 frontier labs 的能力、成本／效率、Agent／推理側算力需求差距。
6. 能直接支持或反駁「算力仍是硬頂」「克制定價／開源擴散」「中美兩隊結構」等既有工作假說的事件。

## Delta 與證據門檻

來源優先級：Primary／官方／監管 > 真正獨立的主流報導 > 匿名單一信源 > 社群／Lead。

轉載同一來源不算獨立互證；Reuters 轉述 Bloomberg 仍屬同一來源鏈。外傳講話、X、論壇與未驗證轉寫不得自動升格為 fact。

重大 delta 至少符合一項：

- 公司／監管 Primary source 改變既有判斷。
- 原本匿名／外傳主張得到真正獨立核實或被官方否定。
- 新模型／定價／限流／算力行為直接支持或反駁 repo 的工作假說。
- 出口管制、國產 GPU、NVIDIA／HBM 供應鏈出現足以改變既有框架的新事件。
- 新資訊會改變 README Open Question／Next Action 或值得升級成獨立研究。

## 日報輸出

每次最多 3–8 項，繁體中文。每項包含：事件日期、Delta、來源／證據等級、影響哪個既有文件／假說、支持／反駁／待定、是否建議寫入 `00_inbox.md`。

沒有重大 delta 時直接回報「今日無重大 delta」。有 Candidate 時，結尾明確標示：**Repo Update Candidate — 等待 YES，不寫入。**

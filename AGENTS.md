# AGENTS.md — 17_deepseek_Kimi 作業規則

> 適用範圍：`/home/arislee1979/0_project/17_deepseek_Kimi` 及其所有文件。  
> 本文件是 **知識研究專案** 規則，與 Hub（`30_investment_hub`）規則不同；不要照搬 Hub 的寫入邊界到此 repo。  
> **語言規範**：本專案所有 Markdown 文件、研究報告、Review、Synthesis 以及 Agent 的所有輸出內容，必須統一使用 **繁體中文**（Traditional Chinese）。

## 1. 專案任務

本 repository 研究：

- DeepSeek / 梁文鋒公開與外傳論述中的戰略心智模型。
- 融資、開源、定價、AGI 路線相關事件的事實邊界。
- 二手產業評論（X、財經媒體）的事實層與故事層分離。

本 repository **不是**：

- 投資建議或交易信號源。
- 完整 AI 產業數據庫。
- Knowledge Project Hub（索引在 `30_investment_hub`）。

詳細證據、模型輸出、來源與完整結論必須留在本 repo；Hub 只放鏈接與階段摘要。

## 2. 任務開始前

所有 agent 必須：

1. 執行或確認 `pwd`，確保位於本專案 canonical path。
2. 閱讀本 `AGENTS.md` 與 `README.md`。
3. 若已有 Current Synthesis，先讀 synthesis；否則讀 README 的 Current Position 與建議閱讀順序。
4. 檢查現有文件與 `git status`。
5. 確認任務角色：Writer / Critic / Evidence Checker / Synthesizer / Project Scaffolder / 其他。
6. 保留使用者與其他 agent 的未提交修改。
7. 語言與文字規範：確認本 repo 及其所有產出文件均統一使用繁體中文。

## 3. 知識階段（Knowledge Stage）

只使用 Hub 定義的固定值：

```text
Capture
Framing
Collection
Analysis
Review
Synthesis
Maintenance
Archived
```

語義（與 Hub Issue #2 對齊）：

- **`stage` = 最高已通過的 maturity gate**（不是「本週正在做的工作」）。
- **`Next Action` = 唯一進行中工作**。
- 缺正式 Current Synthesis **只**阻擋 `Synthesis`，不自動打回 `Analysis`。
- 現行：**Review**（已有 critic／evidence 產物與弱環標示；`synthesis/` 未建）。

階段變更時：

1. 更新本專案 `README.md` 的 Knowledge Stage 與 Last Updated。
2. 若已在 Hub 註冊，同步更新 Hub **`projects.yaml`**（再對齊 README Active 表），只改索引字段，不貼全文。

## 4. 多模型知識統合

> **2026-07-27 暫停**：老大指示 **先暫停用 Writer→Critic→Evidence Checker→Synthesizer 這套格式做 Review**。  
> 未再指示前：不要自動開角色審查輪、不要為湊流程寫 `reviews/03_*`；`02_critic_review.md` 已判定價值低，勿當必讀範本。  
> 有真正新洞見再落短檔；沒有就停。恢復時必須短、尖，禁止模板填空長文。

多個模型不等於多數決。**僅在老大明確要求時**再分配角色：

| 角色 | 職責 | 典型輸出 |
|---|---|---|
| Writer | 第一輪完整分析 | `research/NN_*.md` 或編號分析稿 |
| Critic | 錯誤前提、反例、過度推論 | `reviews/NN_critic_*.md` |
| Evidence Checker | 來源、數字、時實效核 | `reviews/NN_evidence_*.md` |
| Synthesizer | 共識 / 分歧 / 未知 / 採用結論 | `synthesis/NN_current_synthesis.md` |

規則（恢復後仍適用）：

1. 不覆寫前序模型原稿；審查與綜合寫新文件。
2. 不為了形成「共識」而隱藏分歧。
3. 事實、有條件推論、未知必須分欄或分節。
4. Hub / README 的 Current Synthesis **只連到**當前權威 synthesis，不列全部中間產物。
5. 社群帖、未驗證轉寫、匿名信源新聞默認是 Lead 或 Secondary，不得自動升格為 Primary 事實。
6. **禁止**為過驗收清單而堆「最弱三環／替代解釋 A-B-C／長判定表」卻無新信息。

## 5. 來源與主張紀律

1. Primary：公司官方聲明、監管文件、可驗證原始數據。
2. Secondary：主流媒體報道（註明是否匿名信源）、有方法的研究分析。
3. Lead：X/論壇/精校轉寫/自媒體串聯——可驅動調查，不可單獨定論。
4. 重大主張儘量附來源 ID 或明確鏈接；缺來源則標「待查證」。
5. 禁止把「可能 / 據稱 / 知情人士」改寫成確定語氣。
6. 本專案不構成投資、法律或商業決策建議；涉及標的代碼時僅作敘事索引。

## 6. 文件寫入規則

1. 新材料不確定是否納入主線時，先寫入 `00_inbox.md`。
2. 穩定分析進 `research/` 或沿用編號文件（`0_` / `1_` / `2_`…），命名可讀。
3. Review 與 Synthesis 分目錄或清晰前綴，避免與 inbox 混放。
4. 不因一篇普通筆記就更新 Hub；僅在建立／歸檔、階段變化、權威 synthesis 變化或核心 Open Question / Next Action 變化時更新 Hub。
5. README 的 Open Question 與 Next Action 各自最多一項。
6. 不得在本 repo 內再嵌套其他專案的 `.git`；亦不要把本專案建在 Hub 目錄內。
7. **語言規範**：本專案所有文件（包含新建立與修訂之 Markdown）、報告、註解與 Agent 輸出，一律統一使用繁體中文。

## 7. Git 與安全

1. 修改前確認 branch 與 working tree。
2. 只 stage 本次任務相關文件。
3. 穩定里程碑才 commit；commit 信息說明知識變化（checkpoint），不要求逐行讀 diff。
4. 未經明確要求，不得 push、發佈、刪除專案或大量搬移文件。
5. API key、帳密、個資、未授權付費全文不得進入 repository。
6. 既有正文覆寫、權限、刪除、外部發布等高風險操作必須檢查 diff 或取得人工確認。

## 8. 輸出格式（capability-aware）

### 8.1 本機 agent（可存取 vault + shortlink）

最終回覆提供：

```text
Path: <本機絕對路徑>
Tailscale: [<短檔名>](http://100.83.106.59:8084/s/<code>.md)
ChromeOS: [<短檔名>](http://100.115.92.198:8084/s/<code>.md)
IDE: [<檔名>](file:///本機絕對路徑)
```

長路徑或中文檔名先：

```bash
/home/arislee1979/bin/shortlink <absolute-file-path> <short-code>
```

### 8.2 GitHub-only／雲端 agent

**禁止偽造** Path／Tailscale／ChromeOS／IDE。改為：

```text
Remote: https://github.com/arislee1979-afk/17_deepseek_Kimi/blob/<branch>/<path>
Commit: <sha 或 PR URL>
Issue: <相關 issue URL，若有>
Note: 未存取本機 vault；未建立 Tailscale／IDE 連結。
```

### 8.3 本專案範例（本機）

```markdown
Path: /home/arislee1979/0_project/17_deepseek_Kimi/README.md
Tailscale: [17_ds_readme](http://100.83.106.59:8084/s/17_ds_readme.md)
ChromeOS: [17_ds_readme](http://100.115.92.198:8084/s/17_ds_readme.md)
IDE: [README.md](file:///home/arislee1979/0_project/17_deepseek_Kimi/README.md)
```

若同時修改多個重要文件，至少對主要產物提供對應格式。

## 9. 與 Hub 同步與跨專案引用

### 9.1 關係

- 本 repo = 敘事／算力邏輯層的**生產者**。
- `30_investment_hub` = 索引與策略卡；**允許讀取並引用**本庫路徑，禁止複製長文。
- `13_semiconductor`／`20_china-overcapacity` = 兄弟深挖庫；只連不抄。

### 9.2 當且僅當符合 Hub 更新條件時

編輯 `/home/arislee1979/0_project/30_investment_hub/README.md` 的 Active 列：

| 字段 | 內容 |
|---|---|
| 專案 | DeepSeek 梁文鋒講話與戰略敘事 |
| 專案路徑 | `17_deepseek_Kimi` |
| 知識階段 | 與本 README 一致（maturity gate） |
| 當前 synthesis | 鏈接到本 repo 權威文件；未建立則寫「尚未建立」（**勿**連 `06` 當 synthesis） |
| 未決問題／下一行動 | 各最多一項，簡短；禁止分號串列 |
| 最後更新 | YYYY-MM-DD |

先改 Hub `projects.yaml`，再對齊 Hub README Active 表，並跑 Hub validator。

若影響中美×台灣主軸命題，可薄更新 Hub `02` 策略卡（如 S3）上游連結與狀態；禁止把 synthesis 或講話全文貼進 Hub。

### 9.3 Hub 如何引用本庫（供對照）

- 本機：`../17_deepseek_Kimi/README.md` 等（自 Hub 目錄出發）
- 權威入口優先：`README.md` · `02_speech_deep_analysis.md`
- 證據身分：外傳講話＝Lead；`06`＝觀點統合，非正式 Current Synthesis

## 10. 完成驗收

任務完成前確認：

- [ ] 文件寫在正確 repository（`17_deepseek_Kimi`）。
- [ ] 事實 / 推論 / 未知已分開。
- [ ] 未把 Lead 來源寫成確定事實。
- [ ] 未誤改其他 agent 文件。
- [ ] `git status` 已檢查。
- [ ] 語言符合規範：所有文件與內容均使用繁體中文。
- [ ] 若階段或權威結論變更，README（及必要時 Hub）已同步。
- [ ] 最終輸出含 Path、Tailscale、ChromeOS、IDE。

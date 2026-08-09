---
date: 2026-08-05
timezone: Asia/Taipei
window_hours: 36
status: daily_capture
generated_by: Hermes (daily intelligence routing; OpenClaw schedule role)
review_required: true
window_start: 2026-08-03T12:00:00+08:00
window_end: 2026-08-05T09:45:00+08:00
spark_handoff_ingested: 2026-08-05T09:45:00+08:00
---
# Daily Industry Intelligence

*署名：Grok 4.5 (high) · Hermes daily routing*

## Executive Summary

- 今日重大新增：
  - **DeepSeek API 官方文件**仍列出模型值 `deepseek-v4-flash`、`deepseek-v4-pro`，並說明 effort levels 支援差異（Pro 暫僅 `high`/`max`，全文支援預期 early August 2026）。
  - **The Register（2026-08-03）**二次報導：阿里 **Qwen 3.8-Max**（稱 2.4T 參數）與 **DeepSeek V4 Flash 0731** 價格／基準敘事；含 API 價與「開放權重」宣稱—**多數為 vendor／媒體 claim，須官方模型卡核對**。
  - **（Spark 補錄）** 阿里正式推 Qwen3.8-Max API 報價敘事 **$2 in / $6 out per MTok**（低於 Kimi K3 $3/$15 敘事），一週內開源權重宣稱；Kingy AI 實測長推理失敗率 **48.9%**（行銷 vs Agent 穩定度落差）。
- 可能推翻既有假設：若開源權重＋可重現評測齊備，才觸及 S3；實測失敗率若可核，削弱「比肩美系」標題。
- 只有敘事、尚無證據：比肩頂尖模型標題；未核 HF／官方模型卡。
- 建議深入查核：Qwen 官方 blog／HF；DeepSeek pricing；Kingy AI 方法；AA 原始榜。
- 今日無重大新增時的明確聲明：**不適用**。
- **分工**：Spark=Google Doc 雷達；本檔=Hermes 本機路由（凌晨首跑 + 上午 Spark 補錄）。

## Events

## DeepSeek：API 文件確認 V4 Flash／Pro 模型標識與 effort 支援邊界

- Event date: 文件頁面檢索日 2026-08-05（文件更新日期未在摘要中獨立標出）
- Published date: 以官方 docs 現行內容為準（retrieved 2026-08-05）
- Retrieved at: 2026-08-05T00:42+08:00
- Route: 17
- Topic: API · model ids · reasoning effort
- Entities: DeepSeek
- Evidence type: fact（官方 API docs 文本）
- Confidence: high（官方文件直接可讀）
- Primary source: https://api-docs.deepseek.com/api/create-chat-completion/
- Secondary source: —
- Source independence: 公司官方
- Existing claim or file affected: README Current Position（模型代際與官方路徑）；**不得**把外傳講話與此混為同一證據層

### Verified facts

- Chat Completions API 要求 `model` 字串；文件列出可能值包含 **`deepseek-v4-flash`**、**`deepseek-v4-pro`**。
- 文件說明：目前僅 `deepseek-v4-flash` 支援三檔 effort；`deepseek-v4-pro` **暫時**僅支援 `high` 與 `max`（`low` 被當作 `high`，`xhigh` 被當作 `max`），並寫明預期 **2026 年 8 月初**支援全部三檔。

### Interpretation

- `fact` 僅限「文件如此寫」；不推導訓練成本、利潤或「不用 NVIDIA」。
- `inference`：產品線已公開使用 V4 命名空間，與專案內歷史 V3／R1 敘事需在週審做**代際對照表**，避免混代引用 benchmark。

### Why it matters

- 提供可引用的**官方模型標識**錨點，供後續價格、benchmark、開源權重宣稱對表。

### Contradictions and missing evidence

- 本輪未同步抓取官方 pricing 頁全文（The Register 報價不得直接升格）。
- 未驗證實際 API 回應是否與文件一致。

### Suggested next action

- `verify_primary_source`（pricing 頁、changelog）
- `compare_with_existing_claim`（README、`02`、`06` 工作假說中的模型代際）
- `monitor`

---

## 媒體：Qwen 3.8-Max 發布敘事與 DeepSeek V4 Flash 成本／基準對照（The Register）

- Event date: 2026-08-03（報導稱 Monday 發布節奏）
- Published date: 2026-08-03
- Retrieved at: 2026-08-05T00:42+08:00
- Route: 17
- Topic: Qwen · open weights · API pricing · competitive benchmarks
- Entities: Alibaba Qwen · DeepSeek · OpenAI · Anthropic · Artificial Analysis（被引）
- Evidence type: lead + estimate（媒體轉述 vendor／第三方榜；非官方模型卡）
- Confidence: low–medium
- Primary source: 未在本輪成功定位並全文核對 Qwen 官方 release note
- Secondary source: https://www.theregister.com/ai-and-ml/2026/08/03/china-turns-up-the-heat-with-open-model-blitz-as-us-model-makers-panic/5282526
- Source independence: 單一西方科技媒體；內引 Artificial Analysis
- Existing claim or file affected: README「開源／定價／兩隊」；`06` 工作假說（非正式 synthesis）；Hub S3

### Verified facts

（僅驗證「The Register 文章寫了什麼」，**不是**驗證模型真實能力。）

- 文章稱阿里發布 **Qwen 3.8-Max**，參數敘事 **2.4 trillion**，並稱首次將最强 Max 級**權重開放下載**（時點敘事「until now top models locked behind API」）。
- 文章稱 QwenCloud API 價約 **US$2 / M input tokens**、**US$6 / M output tokens**（**媒體數字**）。
- 文章稱 DeepSeek **V4 Flash 0731** 在 Artificial Analysis 獨立基準上與 OpenAI 某 budget 模型接近，且每任務成本低約 **40%**；參數敘事 **284B**（皆為媒體／第三方口徑）。
- 文章亦給出 DeepSeek first-party API 價敘事：約 **US$0.14 / M uncached input**、**US$0.0028 / M cached**、**US$0.28 / M output**（**必須回官方 pricing 核**）。

### Interpretation

- `lead`：開放權重 + 低價 API 是中國模型敘事主戰場；與專案「剋制／開源／算力底褲」假說相關，但 **不得**由媒體標題推出「美國領先已被推翻」。
- `estimate`：所有 benchmark 名次與「within a single point」屬第三方方法依賴；需方法論、提示詞、工具使用設定。
- `hypothesis`：若 Max 級開權重屬實，S3「需求結構／兩隊並行」的證據權重上升；若僅 API 行銷，則維持 lead。

### Why it matters

- 直接撞擊 Core Question：開源策略、定價、中美模型生態解讀。
- 對台灣產業：**不**自動等於台廠訂單變化；最多修正「終端推理成本曲線」詮釋（研究級）。

### Contradictions and missing evidence

- 缺 Qwen 官方模型卡、授權全文、HF commit。
- Artificial Analysis 原始結果頁未在本輪打開核對。
- DeepSeek 官方價與 Register 數字可能落差。
- Medium 轉載文（「Claude defeated」）**拒絕**作為獨立源。

### Suggested next action

- `verify_primary_source`（Qwen 官方 + DeepSeek pricing + AA）
- `promote_to_weekly_review`（僅在官方確認開權重與授權後）
- `reject_as_low_quality`（對標題黨二創）

## Spark 雷達補錄（handoff 2026-08-05 上午）

> Gemini Spark → Google Doc → 使用者轉貼。與上節 Register／Qwen 事件**重疊主題**，此節補 API 報價與實測失敗率線索。

### 阿里 Qwen3.8-Max：低價 API 競價 + 開源時程 + 實測落差（Spark）

- Retrieved at: 2026-08-05T09:45+08:00
- Route: 17
- Topic: API pricing · open weights · agent reliability
- Entities: Alibaba Qwen · Kimi · DeepSeek（對照）
- Evidence type: `estimate`（價）+ `lead`（開源時程／實測）
- Confidence: low–medium
- Secondary source（Spark）: Yotta Labs · The Straits Times · Kingy AI
- Existing: 上節 Register Qwen 敘事；README／S3；**06 非 synthesis**

#### Verified facts（轉貼層）

- Spark 稱推出 **Qwen3.8-Max** Sparse MoE（**2.4T** 參數敘事）API。
- 報價敘事：**$2 / $6** per million tokens（in/out），對照 Kimi K3 **$3 / $15**（**媒體層**）。
- 宣稱約一週內釋出開源權重（**未核官方 blog**）。
- Kingy AI 實測：三款中國最新大模型長推理失敗率合計敘事 **48.9%**（方法未核）。

#### Interpretation

- `estimate`：價格戰壓縮推理 API 溢價敘事；須回官方價目。
- `lead`：開源權重時程。
- `inference`：行銷「比肩」與 Agent 穩定度可分離評價；失敗率若可重現，削弱強結論。
- 對 Next Action：適合作「短版 Evidence Gate」候選（有新公開來源時），**現不建空 reviews/**。

#### Suggested next action

- `verify_primary_source`（Qwen 官方定價＋模型卡＋HF）
- `verify_primary_source`（Kingy AI 方法／樣本）
- `compare_with_existing_claim`（上節 Register 事件）
- `promote_to_weekly_review`（僅官方確認後）

## Rejected or Duplicate Items

| Item | Reason |
|---|---|
| Fortune 2026-07-26 Kimi 成本長文 | 超出主要 36h 時窗；無今日官方修正 |
| Sheppard Mulhern 出口管制法律博客 7/23 | 時窗外；可作週審法律背景而非日更 |
| CGTN／Forbes 社群「中國模型主導」影片文案 | 宣傳／導流；無方法 |
| 「中國將限制前沿模型出口」Reddit 傳聞 | 匿名 lead，未核政策原文 |
| 梁文鋒外傳講話重貼 | 已在 `01`/`02`；無新 primary |

## 證據紀律備註

- 官方原文 → 可 `fact`（本檔僅 API docs）。
- 公司／媒體 benchmark → `estimate` 或 `lead`。
- Spark 轉貼 → 預設 `lead`／`estimate`，不得當 IR。
- 匿名或未核演講 → `lead_requires_verification`（本檔未新增此類講話）。

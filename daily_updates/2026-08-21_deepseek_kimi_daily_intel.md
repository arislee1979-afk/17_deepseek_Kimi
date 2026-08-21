# 2026-08-21 DeepSeek／Kimi／China AI Daily Intelligence

- Status: `unreviewed_daily_intel`
- Generated at: 2026-08-21 08:24 Asia/Taipei (UTC+08:00)
- Search cutoff: 2026-08-19 20:18 Asia/Taipei (rolling 36-hour window anchored at run start)

## Qualified Events

### 1. Alibaba 公布 2026 年 6 月季度業績與新的 AI 分部披露

- Event date: 2026-08-20
- Published date: 2026-08-20
- Evidence type: `fact` (company results and filing)
- Primary source: https://www.sec.gov/Archives/edgar/data/1577552/000110465926099220/tm2623667d1_ex99-1.htm
- Primary source check: PASS
- Independent secondary source: None identified in this run; the SEC-filed exhibit is the evidentiary anchor.
- 直接支持的一句事實: Alibaba 的 SEC-filed results 顯示，2026 年 6 月季 AI Cloud and Compute Services 營收為人民幣 484.37 億元、總營收與外部客戶營收均年增 45%，AI-related product revenue 為人民幣 123.76 億元並連續第 12 季達成三位數年增，同季資本支出為人民幣 676.78 億元、年增 75%。
- 研究關聯: 這是中國大型平台公司把雲端、T-Head、模型實驗室與應用分部重新組織後的官方營收與 CapEx 錨點，可用來追蹤 China AI 的商業化與算力需求；它不單獨證明特定加速器、模型或供應商的採用與經濟性。
- 尚缺證據: 公司未在本文件拆分 T-Head 晶片出貨／算力占比、Qwen 各模型 API 使用量、CapEx 的 GPU／CPU／網路／電力或 foundry 配比；vendor capability claims 也未經第三方重現。
- Confidence: `high`
- Suggested action: `monitor`

### 2. Moonshot AI 發布 Kimi Code `0.38.0`

- Event date: 2026-08-20
- Published date: 2026-08-20 13:13:44 UTC (2026-08-20 21:13:44 Asia/Taipei)
- Evidence type: `fact` (official repository release)
- Primary source: https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai%2Fkimi-code%400.38.0
- Primary source check: PASS
- Independent secondary source: None identified in this run.
- 直接支持的一句事實: Moonshot AI 的官方 release notes 為 Kimi Code `0.38.0` 加入 `kimi.ai`／`kimi.com` 兩種 OAuth 登入、可在同一 turn 等待背景任務完成的 `WaitFor` tool、13 個官方 datasource plugin 資料源，並要求修改既有檔案前先讀取且在磁碟內容已變更時拒絕寫入。
- 研究關聯: 這是 Kimi coding-agent 工具在登入、背景任務協調、資料源與寫入安全上的正式版本變更；不代表 Kimi 基礎模型 benchmark、API 價格、使用量或企業採用發生變化。
- 尚缺證據: 尚無獨立使用者測試可量化 `WaitFor`、datasource plugin 或 stale-file guard 的可靠度與實際採用。
- Confidence: `high`
- Suggested action: `monitor`

### 3. Qwen Code 發布 `v0.21.15`

- Event date: 2026-08-20
- Published date: 2026-08-20 17:38:51 UTC (2026-08-21 01:38:51 Asia/Taipei)
- Evidence type: `fact` (official repository release)
- Primary source: https://github.com/QwenLM/qwen-code/releases/tag/v0.21.15
- Primary source check: PASS
- Independent secondary source: None identified in this run.
- 直接支持的一句事實: QwenLM 官方 `v0.21.15` release notes 將 stable `qwen3.8-max` 加入 Token Plan 的 `/model` 清單、為支援的 hybrid models 提供簡化的 Thinking toggle，並新增 Web Shell 附件、review resume 與 authenticated HTTPS Git extension install 等功能，且標示無已知 breaking changes。
- 研究關聯: 這是 Qwen coding-agent 工具對模型可選範圍與推理控制介面的正式變更；「stable」僅指 release 所述的 Token Plan model entry，不能外推為模型能力、服務 SLA、價格或市場採用的獨立證明。
- 尚缺證據: 尚缺對 qwen3.8-max 的獨立 benchmark／可靠度重現、Token Plan 的完整價格與區域可用性核對，以及新版功能的第三方驗證。
- Confidence: `high`
- Suggested action: `monitor`

## Rejected or Duplicate Leads

| Item | Disposition | Reason | URL |
|---|---|---|---|
| Gemini Spark 2026-08-21：LMSYS DeepSeek-V4-Pro H20 serving 報告 | `REJECT_AS_LEAD` | 官方／作者頁明確標示 2026-08-07，並非 Drive 所稱 2026-08-19 發布或 2026-08-20 更新；超出本輪 36 小時視窗。 | https://staging.lmsys.org/blog/2026-08-07-deepseek-v4-pro-engine-optimization-h20 |
| Alibaba June Quarter 2026 results | `WRITE_TO_REPO` | Drive 僅作 lead；本輪重新開啟 2026-08-20 SEC 6-K exhibit，核對營收、增速、CapEx、單位與期間後收錄，並移除「證明自研晶片商業化」等超出原文的推論。 | https://docs.google.com/document/d/1V3BhpwGIYLK3-zjvio-w_ggnp92iP9W6vX3vQCGRtsI/edit |
| DeepSeek Harness `v0.1.0-rc.8` | `DUPLICATE` | 2026-08-20 daily intel 已以官方 release 收錄；本輪沒有新版本或適用範圍變更。 | https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.1.0-rc.8 |
| Kimi Code `0.37.1`／`0.37.2` 與 Qwen Code `v0.21.14` | `DUPLICATE` | 已在 2026-08-20 daily intel 收錄；本輪只收錄新的 Kimi Code `0.38.0` 與 Qwen Code `v0.21.15`。 | — |
| 中國放行 NVIDIA H200 並向字節跳動／騰訊配額的傳聞 | `REQUIRES_PRIMARY_SOURCE` | 未找到中國商務部、美國 BIS、NVIDIA、字節跳動或騰訊的官方文件；媒體與市場轉述不能通過硬閘門。 | — |
| Qwen Code nightly／preview releases | `REJECT_AS_LEAD` | 本輪已有同視窗正式版 `v0.21.15` 作版本錨點；不重複收錄 nightly／preview。 | https://github.com/QwenLM/qwen-code/releases |

## Repository changes

- 本次僅新增 `daily_updates/2026-08-21_deepseek_kimi_daily_intel.md`。
- 本檔不修改 README、AGENTS、正式分析、Current Synthesis、Hub registry、策略卡或 GitHub Issues，也不宣稱改變正式研究結論。

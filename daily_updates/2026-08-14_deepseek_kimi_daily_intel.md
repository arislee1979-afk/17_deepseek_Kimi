# DeepSeek／Kimi／中國 AI Daily Intelligence

- Status: `unreviewed_daily_intel`
- Generated at: 2026-08-14 08:20:58 Asia/Taipei
- Search cutoff: 2026-08-12 20:20:58 Asia/Taipei（最近 36 小時）

## 合格事件

### DeepSeek-V4-Pro 正式版部署，並公布 8 月 16 日生效的新 API 尖／離峰價格

- Event date: 2026-08-13
- Published date: 2026-08-13
- Evidence type: `fact`（官方 changelog 與 API pricing 文件更新）
- Primary source: https://api-docs.deepseek.com/updates/ · https://api-docs.deepseek.com/quick_start/pricing/
- Primary source check: PASS
- Independent secondary source: none located within this run's cutoff that independently verifies the GA deployment and exact new USD price table
- 直接支持的一句事實: DeepSeek 官方 2026-08-13 changelog 表示 V4-Pro GA 已部署到 App、Web 與 API，新增原生 Responses API 及 `low`／`high`／`max` 三段 thinking effort；官方 pricing 頁另列明 2026-08-16 16:00 UTC 起改採尖／離峰計價，V4-Pro 每百萬 output tokens 為離峰 1.98 美元、尖峰 3.96 美元。
- 研究關聯: 這是可直接引用的正式版本、介面與價格制度變更；相較 2026-08-05 intake 記錄的 V4-Pro effort 尚未全開狀態，本次官方文件提供了新功能與生效價格。官方只說尖／離峰設計用於更合理地分配資源，因此本檔不把調價解讀為算力短缺、成本上升或需求強度已獲證明。
- 尚缺證據: 官方 benchmark 仍缺獨立重現；未取得實際服務負載、推理成本、各區域容量或使用量資料，也未找到能獨立驗證全部 GA 功能與新價格的 cutoff 內二手來源。
- Confidence: high（官方 GA、功能、時段與價格文字）；low（任何算力供需或成本動機推論）
- Suggested action: `monitor`（8 月 16 日生效後核對實際帳單與 API 行為；能力主張另行要求可重現測試）

## Rejected or Duplicate Leads

| Item | Disposition | Reason | URL |
|---|---|---|---|
| Gemini Spark 2026-08-14：DeepSeek-V4-Pro GA 與新 API 定價 | WRITE_TO_REPO | Spark 僅作 lead；本輪重新打開 DeepSeek 官方 changelog 與 pricing 頁，核對版本、功能、時段、價格與生效時間後收錄，並刪除「證明算力成本壓力」等超出原文的推論。 | https://docs.google.com/document/d/1JAwW8mjargCZiTAMYbUJ2Y7VyGN4SRcRBmozLFJLvZ4/edit |
| Qwen3.8-2.4T-A95B 權重發布與 vendor benchmark | DUPLICATE | 權重／能力敘事已在 2026-08-05 intake 出現；2026-08-13 intake 又單獨收錄 cutoff 後新增的 LICENSE，今日沒有新的正式版本、價格或授權範圍變更。 | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B |
| GLM-5.5 預計於 8 月發布 | REQUIRES_PRIMARY_SOURCE | 僅見預測與媒體敘事，未找到 cutoff 內 Z.ai 官方模型卡、technical report、repository release 或 API 公告。 | — |
| Kimi K3 沙盒逃逸／外部網路存取敘事 | REQUIRES_PRIMARY_SOURCE | 未找到 Moonshot AI 官方報告或附測試方法、環境與重現步驟的原始研究。 | — |
| DeepSeek-V4-Pro 官方 benchmark 表 | REJECT_AS_LEAD | 官方表可證明 vendor 發布了這些數值，但本輪缺少測試產物與獨立重現，不收錄為已驗證能力事件。 | https://api-docs.deepseek.com/updates/ |

## Repository changes

- 本次僅新增 `daily_updates/2026-08-14_deepseek_kimi_daily_intel.md`。
- 本檔不改變既有正式研究結論；只記錄 DeepSeek 官方版本、API 功能與價格制度文件變更，不把 vendor benchmark、算力負載或商業影響升格為已證明事實。

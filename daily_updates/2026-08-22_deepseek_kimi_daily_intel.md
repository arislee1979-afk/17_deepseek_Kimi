# 2026-08-22 DeepSeek／Kimi／China AI Daily Intelligence

- Status: `unreviewed_daily_intel`
- Generated at: 2026-08-22 08:23 Asia/Taipei (UTC+08:00)
- Search cutoff: 2026-08-20 20:23 Asia/Taipei (rolling 36-hour window anchored during this run)

## Qualified Events

### 1. DeepSeek 上線實驗性多模態 API 模型 `DeepSeek-V4-Flash-Vision-Exp`

- Event date: 2026-08-21
- Published date: 2026-08-21
- Evidence type: `fact` (official API changelog and pricing documentation)
- Primary source: https://api-docs.deepseek.com/updates/ · https://api-docs.deepseek.com/quick_start/pricing/
- Primary source check: PASS
- Independent secondary source: https://www.thepaper.cn/newsDetail_forward_33825583
- 直接支持的一句事實: DeepSeek 官方 changelog 將 `deepseek-v4-flash-vision-exp` 標為 2026-08-21 上線的實驗性多模態視覺理解模型；官方 pricing 頁列示 1M context、384K 最大輸出、Responses／Anthropic API 支援，以及與 V4-Flash 相同的尖峰與離峰 token 費率。
- 研究關聯: 這是 DeepSeek 正式 API 產品線首次新增本輪可驗證的視覺模型入口、功能邊界與計費錨點；官方 benchmark 與「接近 Opus-4.8」仍屬 vendor-reported capability，不等同獨立重現結果。
- 尚缺證據: 尚未看到獨立技術報告、模型權重、視覺編碼器與訓練資料披露，亦缺第三方在相同設定下對視覺 agent benchmark、可靠度、延遲與實際影像 token 成本的重現。
- Confidence: `high`
- Suggested action: `reproduce_claim`

### 2. DeepSeek Harness 發布 `v0.1.1-rc.1` 與 `v0.1.1-rc.2`

- Event date: 2026-08-21
- Published date: 2026-08-21 07:12:39 UTC、12:35:08 UTC (2026-08-21 15:12:39、20:35:08 Asia/Taipei)
- Evidence type: `fact` (official repository pre-releases)
- Primary source: https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.1.1-rc.1 · https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.1.1-rc.2
- Primary source check: PASS
- Independent secondary source: None identified in this run.
- 直接支持的一句事實: DeepSeek 官方 `v0.1.1-rc.1` release notes 新增 `DeepSeek-V4-Flash-Vision-Exp` adapter 並修補 Bubblewrap 受限程序可經 `/proc/<pid>/root` 繞過限制的問題；同日 `rc.2` 改為優先用 Files API 上傳及重用圖片，並按模型要求自動縮放與轉換格式。
- 研究關聯: 這兩個預發行版本提供多模態 API 在官方 agent harness 的實作與安全修補紀錄，可觀察 DeepSeek 從模型發布到工具鏈支援的同步速度；它們不證明基礎模型能力、部署可靠度或使用量。
- 尚缺證據: 仍缺穩定版發布、跨平台回歸測試、沙箱修補的獨立安全驗證，以及 Files API 圖像重用對延遲、成本與失敗率的量化測試。
- Confidence: `high`
- Suggested action: `monitor`

### 3. Kimi Work 發布 `3.2.1`

- Event date: 2026-08-21
- Published date: 2026-08-21
- Evidence type: `fact` (official product release notes)
- Primary source: https://www.kimi.com/en/help/kimi-work/release-notes
- Primary source check: PASS
- Independent secondary source: None identified in this run.
- 直接支持的一句事實: Moonshot AI 官方 `3.2.1` release notes 新增全域 Launcher、回覆期間的訊息佇列與語音輸入，並修正 macOS Dock 圖示消失及降低待機資源使用；官方 overview 另明示 Kimi Work 已於 2026-06-03 推出，而非 2026-08-21 首次發布。
- 研究關聯: 這是 Kimi 桌面 agent 在入口、互動佇列與穩定性上的正式版本變更；不應把既有 Goal Mode、Scheduled Tasks、WebBridge 或最多 300 sub-agents 誤寫成本次新增，也不能外推模型能力或市場採用。
- 尚缺證據: 尚缺實際版本滲透率、Launcher／訊息佇列的跨平台可靠度、待機資源改善幅度，以及第三方對本機權限與資料保護的驗證。
- Confidence: `high`
- Suggested action: `monitor`

## Rejected or Duplicate Leads

| Item | Disposition | Reason | URL |
|---|---|---|---|
| Gemini Spark 2026-08-22：DeepSeek Vision、Files API 與 Kimi Work | `WRITE_TO_REPO` | Drive 僅作 lead；本輪重新開啟 DeepSeek changelog／pricing、Harness releases 與 Kimi release notes。只收錄原文可支持的版本與功能，並校正 Kimi Work 實際於 2026-06-03 已推出。 | https://docs.google.com/document/d/1w4gsf5_YtTQTngI2dxDKIaiUGneK3oI4ORwCwuYiXdY/edit |
| Gemini Spark 2026-08-21：Alibaba 與 LMSYS DeepSeek-V4-Pro H20 報告 | `DUPLICATE` | Alibaba 已於 2026-08-21 daily intel 以 SEC exhibit 收錄；LMSYS 作者頁日期為 2026-08-07，已在同檔拒絕，今日沒有新正式版本或修正。 | https://docs.google.com/document/d/1V3BhpwGIYLK3-zjvio-w_ggnp92iP9W6vX3vQCGRtsI/edit |
| Drive 所稱「Kimi Work 於 2026-08-21 正式推出」 | `REJECT_AS_LEAD` | 官方 overview 明示 Kimi Work 於 2026-06-03 launched；本輪僅有 `3.2.1` release notes 可作新事件。 | https://www.kimi.com/en/help/kimi-work/overview |
| Kimi Code `0.38.0` 與 Qwen Code `v0.21.15` | `DUPLICATE` | 已於 2026-08-21 daily intel 以官方 releases 收錄，本輪沒有新的正式穩定版。 | — |
| Qwen Code nightly／DSW EAS smoke releases | `REJECT_AS_LEAD` | 這些是 nightly 或測試工作流產物；本輪沒有新的正式版、模型卡、價格或授權範圍變更。 | https://github.com/QwenLM/qwen-code/releases |
| 豆包桌面／作業系統級 agent 傳聞 | `REQUIRES_PRIMARY_SOURCE` | 未找到字節跳動官方公告、模型卡、產品文件或 release notes；媒體與市場推測不能通過硬閘門。 | — |

## Repository changes

- 本次僅新增 `daily_updates/2026-08-22_deepseek_kimi_daily_intel.md`。
- 本檔不修改 README、AGENTS、正式分析、Current Synthesis、Hub registry、策略卡或 GitHub Issues，也不宣稱改變正式研究結論。

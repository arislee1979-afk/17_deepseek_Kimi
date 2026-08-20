# 2026-08-20 DeepSeek／Kimi／China AI Daily Intelligence

- Status: `unreviewed_daily_intel`
- Generated at: `2026-08-20 08:23:25 Asia/Taipei (UTC+08:00)`
- Search cutoff: `2026-08-18 20:23:25 Asia/Taipei (UTC+08:00)`
- Scope: 最近 36 小時內的官方模型、repository、授權、API 定價與可重現研究變更；最多三項。

## 合格事件

### 1. DeepSeek Harness 發布 `v0.1.0-rc.8` 預發行版本

- Event date: `2026-08-19`
- Published date: `2026-08-19 15:37:57 UTC`（`2026-08-19 23:37:57 Asia/Taipei`）
- Evidence type: `fact`（官方 repository 的 immutable pre-release）
- Primary source: https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.1.0-rc.8
- Primary source check: PASS
- Independent secondary source: 無（未找到獨立二手來源；本項只記錄官方 release 可直接支持的版本與功能變更）
- 直接支持的一句事實: DeepSeek 官方 GitHub repository 於 2026-08-19 發布 `dsh-v0.1.0-rc.8` 預發行版，release notes 列出原生圖片請求與圖文命令支援、可按需安裝的 Claude Code／Codex 子代理 Profile Bundle、Windows 持久 PowerShell，以及圖片載荷、推理內容回傳與 OpenAI-compatible gateway 的修正。
- 研究關聯: 這是 DeepSeek 官方 agent tooling 的可引用版本錨點，顯示其公開工具面正擴充多模態、子代理與跨平台執行能力；它不是 DeepSeek 基礎模型的新版本或 benchmark 證據。
- 尚缺證據: 未獨立安裝或重現 rc.8；官方標示為 pre-release，且 release notes 明示 SQLite 儲存格式不相容，尚無穩定版採用率、可靠度或效能量測。
- Confidence: `high`（版本／release notes）；功能可靠度與使用影響仍為 `requires_verification`
- Suggested action: `monitor`（等待穩定版與可重現 smoke test）

### 2. Moonshot AI 發布 Kimi Code `0.37.1` 與 `0.37.2` 修補版本

- Event date: `2026-08-18`
- Published date: `2026-08-18 14:32:13 UTC`、`2026-08-18 17:40:37 UTC`（均在 36 小時視窗內）
- Evidence type: `fact`（官方 repository release）
- Primary source: https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai%2Fkimi-code%400.37.1 · https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai%2Fkimi-code%400.37.2
- Primary source check: PASS
- Independent secondary source: 無（未找到獨立二手來源；本項只記錄官方 release 可直接支持的修補內容）
- 直接支持的一句事實: Moonshot AI 官方 repository 在視窗內先後發布 Kimi Code `0.37.1` 與 `0.37.2`；前者修復首次傳送時貼上圖片或影片未送達模型的問題，後者調整 subagent 詳情顯示並新增預設關閉的 Lab 多分頁側欄切換。
- 研究關聯: 這是 Kimi 公開 coding-agent 工具的正式修補序列，可作產品迭代與多模態輸入可靠度的版本錨點；不等同 Kimi 模型卡、權重、API 價格或推理能力變更。
- 尚缺證據: 未獨立重現附件傳送修復；`0.37.2` 的 Lab UI 預設關閉，release notes 未提供使用率、錯誤率或模型端變更證據。
- Confidence: `high`（版本／release notes）；實際可靠度影響仍為 `requires_verification`
- Suggested action: `monitor`（僅在後續穩定版或可重現錯誤率資料出現時升級）

### 3. Qwen Code 發布 `v0.21.14`

- Event date: `2026-08-19`
- Published date: `2026-08-19 02:46:42 UTC`（`2026-08-19 10:46:42 Asia/Taipei`）
- Evidence type: `fact`（官方 repository release）
- Primary source: https://github.com/QwenLM/qwen-code/releases/tag/v0.21.14
- Primary source check: PASS
- Independent secondary source: 無（未找到獨立二手來源；本項只記錄官方 release 可直接支持的版本與功能變更）
- 直接支持的一句事實: Qwen 官方 repository 於 2026-08-19 發布 Qwen Code `v0.21.14`，release notes 列出 `qwen sessions ps` 與 live-session registry、`/advisor` 唯讀第二意見命令、指定 agent working directory，以及 Web Shell 訊息／圖片可靠度修正，並標示無已知 breaking changes。
- 研究關聯: 這是 Qwen coding-agent 工具的正式版本與 session／agent orchestration 功能錨點；不證明 Qwen 基礎模型的 benchmark、token 成本或企業採用變化。
- 尚缺證據: 未獨立安裝或執行 release；官方功能清單未提供錯誤率、效能或與其他 coding agents 的可比測試。
- Confidence: `high`（版本／release notes）；產品效果仍為 `requires_verification`
- Suggested action: `compare_with_existing_claim`（後續若比較中國 coding-agent 工具面，只引用可重現功能，不升格為模型能力）

## Rejected or Duplicate Leads

| Item | Disposition | Reason | URL |
|---|---|---|---|
| Gemini Spark 2026-08-20：今日無合格新增事件 | REJECT_AS_LEAD | Drive 文件本身不是證據；其內容只列無官方逐字稿的梁文鋒傳聞、視窗外或重複事件。直接官方 repository 搜尋另找到上述三個 release。 | https://docs.google.com/document/d/10q6WnazX-O1JiA07ImOwbDdeaOHAi6IhjXzQAmXW2xc/edit |
| Gemini Spark 2026-08-14：DeepSeek V4-Pro GA 與 API 尖／離峰定價 | DUPLICATE | 已於 `2026-08-14_deepseek_kimi_daily_intel.md` 以官方 changelog／pricing 收錄，本輪沒有新價格或適用範圍變更。 | https://docs.google.com/document/d/1JAwW8mjargCZiTAMYbUJ2Y7VyGN4SRcRBmozLFJLvZ4/edit |
| 網傳梁文鋒「4 顆華為晶片抵 1 顆輝達晶片」閉門會議發言 | REQUIRES_PRIMARY_SOURCE | 未找到 DeepSeek 官方逐字稿、錄音、公告或具測試口徑的技術文件；媒體／社群轉述不能作 primary source。 | — |
| Kimi Code `0.37.0` | REJECT_AS_LEAD | 官方 release 時間為 `2026-08-18 11:23:11 UTC`，早於本輪 36 小時 cutoff 約 59 分鐘；不把視窗外 minor release 內容併入本輪事件。 | https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai%2Fkimi-code%400.37.0 |
| Qwen Code nightly、preview 與 DSW smoke/full benchmark releases | REJECT_AS_LEAD | 本輪以同日正式版 `v0.21.14` 作版本錨點；nightly／preview 不重複收錄，DSW release 中的 benchmark 亦未在本輪取得完整可重現產物與獨立驗證。 | https://github.com/QwenLM/qwen-code/releases |
| Qwen3.8、GLM-5.3、DeepSeek V4-Pro 與 API 定價的二手追蹤 | DUPLICATE | 相關模型、授權、文件或定價變更已在 2026-08-05 至 2026-08-14 intake 處理；本輪未見新的正式模型卡、license、價格或適用範圍變更。 | — |

## Repository changes

- 本次只新增 `daily_updates/2026-08-20_deepseek_kimi_daily_intel.md`。
- 本檔不改變 README、Current Synthesis 或既有正式研究結論；三項事件只記錄官方工具 release，不把功能清單升格為模型能力、採用率、成本或算力供應的證據。

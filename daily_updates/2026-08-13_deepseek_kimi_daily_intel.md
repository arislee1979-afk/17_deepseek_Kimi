# DeepSeek／Kimi／中國 AI Daily Intelligence

- Status: `unreviewed_daily_intel`
- Generated at: 2026-08-13 08:27:00 Asia/Taipei
- Search cutoff: 2026-08-11 20:17:12 Asia/Taipei（最近 36 小時）

## 合格事件

### Qwen 官方為 Qwen3.8-2.4T-A95B 權重庫加入專用授權條款

- Event date: 2026-08-12
- Published date: 2026-08-12 18:21:55 Asia/Taipei
- Evidence type: `fact`（官方模型 repository 的授權文件新增）
- Primary source: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/commit/1f1e3183c519099f24a29b1e90f6d04d887b3a67
- Primary source check: PASS
- Independent secondary source: none
- 直接支持的一句事實: Qwen 官方 Hugging Face repository 於 commit `1f1e3183c519` 新增 `Qwen3.8-Max License`，允許使用、修改、散布、部署與微調，但對符合特定規模條件的商業產品，以及連續 12 個月合計營收超過 5,000 萬美元的 Model as a Service／AI Work Assistant 業者，分別加入名稱揭露或另行取得授權的條件。
- 研究關聯: 2026-08-05 intake 已記錄 Qwen3.8-Max 的媒體／Spark 開放權重敘事；本次新增的是可直接引用的官方授權邊界，因此屬於「授權變更」而可重收，不代表模型能力、採用率或商業收入已獲證明。
- 尚缺證據: 尚未取得獨立法律解讀，也未見 Qwen 公布適用案例或另行授權的價格；本檔不判斷個別企業是否落入條款門檻。
- Confidence: high（文件新增與條文字面）；medium（任何實際適用解讀）
- Suggested action: `compare_with_existing_claim`（週審時把 2026-08-05 的「開放權重」敘事改以官方 LICENSE 為授權錨點，能力 benchmark 仍須獨立重現）

## Rejected or Duplicate Leads

| Item | Disposition | Reason | URL |
|---|---|---|---|
| Gemini Spark 2026-08-13：今日無合格中國 AI 事件 | REJECT_AS_LEAD | Drive 文件沒有 article-level 合格新增；所列 GitHub issue／discussion 是社群維護或討論，不能替代官方模型、定價或授權發布。 | https://docs.google.com/document/d/1YWk03hEdVmGO5rb2KvON64yGishFnykVPNm41Ed62lQ/edit |
| 中國 AI 團隊由 CUDA 遷移至 Ascend／CANN 增加至少 50% 時間與成本 | REQUIRES_PRIMARY_SOURCE | 僅有媒體引述與個案敘事，未找到華為官方文件或具方法、可重現的比較研究支持統一比例。 | — |
| Qwen3.8-2.4T-A95B 模型能力與 benchmark 表 | DUPLICATE | 模型發布與 vendor benchmark 敘事已在 2026-08-05 intake 出現；本輪只收錄 cutoff 後新增的 LICENSE，不重複收錄能力主張。 | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B |
| Qwen3.8-2.4T-A95B `config.json` 修正 | REJECT_AS_LEAD | cutoff 內移除 `mrope_*` 欄位，但未附 release note、影響範圍或使用者可觀察結果；不足以形成研究事件。 | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/commit/b15b86386175ffa6032ba70a1ed10443187008fb |
| DeepSeek、Kimi、GLM、MiniMax 主要官方 repositories | NO_NEW_DOCS | cutoff 內所見多為 issue 活動或一般維護；未找到另一項符合模型／權重／定價／授權／可重現研究硬閘門的新事件。 | — |

## Repository changes

- 本次僅新增 `daily_updates/2026-08-13_deepseek_kimi_daily_intel.md`。
- 本檔不改變既有正式研究結論；只記錄 Qwen3.8 權重庫新增的官方授權條文，未把 vendor benchmark、部署採用或商業影響升格為事實。

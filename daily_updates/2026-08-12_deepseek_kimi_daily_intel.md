---
date: 2026-08-12
timezone: Asia/Taipei
status: unreviewed_daily_intel
generated_at: 2026-08-12T08:18:52+08:00
search_cutoff: 2026-08-10T20:18:52+08:00
window_hours: 36
review_required: true
---

# DeepSeek／Kimi／中國 AI Daily Intelligence

## 合格事件

### Z.ai 官方 GLM-5 模型卡新增 SWE-Bench Multilingual 社群評測值

- Event date: 2026-08-11
- Published date: 2026-08-11 15:36:34（Asia/Taipei；Hugging Face commit 時間換算）
- Evidence type: `fact`（官方模型卡版本變更）；評測值的能力解讀仍為 `requires_verification`
- Primary source: https://huggingface.co/zai-org/GLM-5/commit/c183ef8c61faee82855eca1ed9bb3a9a7ce3b0b2
- Primary source check: PASS
- Independent secondary source: none；本次新增 YAML 未提供獨立報告、執行設定或可重現紀錄
- 直接支持的一句事實: Z.ai 官方 GLM-5 Hugging Face repository 於 2026-08-11 合併 commit `c183ef8c61fa`，新增 `.eval_results/swe-bench_multilingual.yaml`，其中將 GLM-5 的 `swe_bench_multilingual_%_resolved` 值記為 73.3。
- 研究關聯: 這是既有 GLM-5 模型卡新增的 benchmark 文件資料，可作中國模型 coding／agent 能力敘事的最新官方錨點，但不是新模型發布，也不是第三方重現結果。
- 尚缺證據: YAML 的 `source` 回指同一模型卡，未列測試 harness 版本、提示詞、推理設定、抽樣範圍、執行日誌或獨立 leaderboard；因此不能由 73.3 推論實際部署可靠度或與其他模型的可比優勢。
- Confidence: high（文件變更與數值）；low（評測結果的獨立可重現性）
- Suggested action: `monitor`；等待 SWE-Bench 或具方法的第三方發布可核對結果後再比較既有能力敘事

## Rejected or Duplicate Leads

| Item | Disposition | Reason | Source |
|---|---|---|---|
| Alibaba Cloud Token Plan Individual Subscription Guide | REJECT_AS_LEAD | Drive 稱為 2026-08-11 新事件，但官方產品文章已在約三週前發布；不符合本輪 36 小時 hard gate。 | https://modelstudio.alibabacloud.com/intl/blog/model-studio-token-plan-individual/ |
| Qoder Knowledge Engine 技術文章 | REJECT_AS_LEAD | Drive 稱 2026-08-11 發布；官方頁明載 2026-07-21，時窗外。 | https://qoder.com/en/blog/qoder-knowledge-engine |
| DeepSeek API 漲價預告 | REQUIRES_PRIMARY_SOURCE | 官方 pricing／changelog 未見 36 小時內具時間戳的新價格表或正式生效公告。 | https://api-docs.deepseek.com/updates/ |
| Kimi K3 沙盒安全敘事 | REQUIRES_PRIMARY_SOURCE | 僅定位到媒體敘事，未找到 Moonshot AI 官方報告或具方法的可重現原文。 | — |
| MiniMax-H3 模型卡 README 更新 | REJECT_AS_LEAD | 2026-08-11 僅確認 README commit；未定位到版本、權重、license、pricing 或評測的實質變更。 | https://huggingface.co/MiniMaxAI/MiniMax-H3 |
| Qwen、DeepSeek、Kimi、GLM、MiniMax 主要官方 GitHub repositories | NO_NEW_DOCS | 自 cutoff 起未找到符合本任務門檻的新 release；一般 issue／維護 commit 不收錄。 | — |

## Repository changes

- 本次僅新增 `daily_updates/2026-08-12_deepseek_kimi_daily_intel.md`。
- 未修改 README、AGENTS、Current Synthesis、正式分析正文或 Hub。
- 本檔不改變既有正式研究結論；GLM-5 的 73.3 僅記錄官方模型卡新增值，仍待獨立重現。

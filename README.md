# 17_deepseek_Kimi

> DeepSeek 战略心智与公开叙事研究：梁文锋讲话、开源/克制定价逻辑、融资事件核查与产业串联评论。  
> 本专案是 **知识研究 repo**，不是投资建议、不是交易信号源。

- 状态：Active Knowledge Project
- 工作方式：CLI-first、Markdown-first、多模型角色分工（Writer / Critic / Evidence Checker / Synthesizer）
- Hub 索引：[`30_investment_hub`](../30_investment_hub/README.md)
- 最后更新：2026-07-27

## Project Identity

| 项 | 值 |
|---|---|
| Project name | DeepSeek 梁文锋讲话与战略叙事 |
| Canonical path | `/home/arislee1979/0_project/17_deepseek_Kimi` |
| Knowledge Stage | **Analysis** |
| Last updated | 2026-07-27 |
| Current Synthesis | 尚未建立正式 `synthesis/`；目前最接近权威拆解见下方 |

## Core Question

**DeepSeek 的真实目标函数与商业逻辑是什么？公开外传讲话、融资节奏与二手产业评论（如 StockWe）分别提供了哪些可核验事实、有条件推论与过度叙事？**

可拆成三个子问题：

1. 梁文锋四小时交流稿主张了哪些可复用的战略原则（愿景、克制、开源、AGI 阶梯、定价）？
2. 「第二轮融资暂停」新闻链的可信度与因果边界在哪里？
3. 把 DeepSeek 与 NVIDIA / 芯片封锁做成「商业协同」的叙事，哪些成立、哪些需打折？

## Scope

### Included

- 梁文锋外传讲话精校与心智模型拆解。
- 与融资、开源、API 定价、AGI 路线相关的公开报道核查。
- 二手评论（X / 财经自媒体）的事实层 vs 故事层分离。
- 与「中国制造式降本 / 杰文斯悖论 / 开源扩散」相关的产业逻辑讨论（**研究级**，非持仓建议）。

### Excluded

- 不提供买卖 DeepSeek 相关标的或美股（$NVDA 等）的投资建议。
- 不以社群转述自动当成公司官方立场。
- 不把本 repo 做成完整 AI 产业数据库或每日新闻流水账。
- 不在此 repo 内存放 API key、未授权付费全文或敏感个资。

## Why This Matters

- 理解 DeepSeek 的「克制即战略」是否自洽，影响对开源模型、算力需求与中美 AI 竞争的判断框架。
- 外传讲话已成为市场叙事的原材料；需要把 **原文 → 拆解 → 新闻 → 二手串联** 分层，避免把评论当事实。
- 为 Hub 与其他产业专案（如产能/算力）提供可引用的 Current Synthesis 锚点。

## Current Position（短摘要）

1. 讲话核心可压缩为：**Maximize P(AGI) subject to 合理利润与团队稳定**，而非 Maximize ARR。  
2. 「十个月回本 / 约六倍利润下开源不冲突 / 不抢 C 端芝麻」与后续公开叙事高度一致。  
3. 2026-07-25 Bloomberg 线：第二轮融资 **口头暂停**、**部分原因**与首轮交流内容外传有关；非官方确认，「恶意」未证实。  
4. StockWe 类串联对战略逻辑转述大体正确，但对停融资的因果升华偏故事化。

## Current Synthesis

- **正式 Current Synthesis**：尚未建立（目标路径：`synthesis/04_current_synthesis.md`）。
- **现阶段权威阅读（Analysis 级）**：
  - [1_speech_deep_analysis.md](1_speech_deep_analysis.md) — 讲话心智模型拆解
  - [2_StockWe_融资暂停串联分析_核查.md](2_StockWe_融资暂停串联分析_核查.md) — 推文归档 + 融资新闻事实核查 + 看法

进入 **Synthesis** 阶段前，应完成至少一轮 Critic / Evidence Checker 并合并为一份正式 synthesis。

## Evidence Base（现有材料）

| ID | 证据／来源 | 类型 | 支持或反对什么 | 可信度 | 日期 |
|---|---|---|---|---|---|
| S01 | [0_speech.md](0_speech.md) 梁文锋四小时发言精校（大宇 @BTCdayu） | Lead / 二次转写 | 开源、克制、十个月回本、AGI 阶梯等主张 | 中（非官方录音原档；转写精校） | 2026-07 外传 |
| S02 | [1_speech_deep_analysis.md](1_speech_deep_analysis.md) | Secondary 分析 | 将讲话整理为可复用战略模型 | 中高（依赖 S01） | 2026-07-24 |
| S03 | Bloomberg / Reuters 等二轮融资暂停报道（见 2_ 文内链） | Secondary 新闻（匿名信源） | 口头暂停第二轮；部分因言论外传 | 中高（主流媒体一致，非官方） | 2026-07-25 |
| S04 | StockWe 推文 2081201760669200886（全文见 2_） | Lead / 评论 | 制造业降本、与 NVDA 协同、政策海关叙事 | 低–中（观点文，非一手事实） | 2026-07-26 |
| S05 | [2_StockWe_融资暂停串联分析_核查.md](2_StockWe_融资暂停串联分析_核查.md) | Evidence check + 评论 | 事实边界与 StockWe 评价 | 中高（核查层） | 2026-07-27 |

来源优先级：Primary（公司官方 / 监管）> Secondary（主流报道、有方法的分析）> Lead（X、论坛、未验证转写）。

## Open Question

**第二轮融资暂停是否已由公司侧以任何可核验渠道确认？后续恢复条件与时间窗口是什么？**

## Model Positions

| 模型／角色 | 核心主张 | 最强证据 | 最大弱点 |
|---|---|---|---|
| Writer（已有：1_） | 克制 + 开源 + AGI 主线是自洽 OS | S01 内在一致性 | 依赖外传转写 |
| Evidence Checker（已有：2_ 部分） | 停融资方向可信、非官方；恶意未证实 | S03 多家转述一致 | 无官方原文、无录音链完整审计 |
| Critic | 尚未独立成文 | — | — |
| Synthesizer | 尚未产出正式 Current Synthesis | — | — |

## Falsification Conditions

以下任一发生，应强制修订结论：

- DeepSeek 官方否认「暂停第二轮融资」或给出不同原因。
- 公司改走高溢价闭源、或明确放弃顶级模型开源。
- 出现可验证的官方录音/纪要，证明外传稿系统性歪曲原意。
- API 定价逻辑被证伪（长期明显亏本补贴或改为利润最大化）。
- 第二轮融资在无外传争议下仍无限期停摆，且公开原因变为监管/制裁/财务危机。

## Decision Log

| 日期 | 决定 | 理由 | 影响文件 |
|---|---|---|---|
| 2026-07-24 | 建立讲话精校与深度拆解 | 外传内容需结构化，避免只在聊天层 | `0_speech.md`, `1_speech_deep_analysis.md` |
| 2026-07-27 | 归档 StockWe 并做融资新闻核查 | 区分事实层与故事层 | `2_StockWe_融资暂停串联分析_核查.md` |
| 2026-07-27 | 按 Hub 规范补齐专案骨架 | 升级为正式知识专案，可被 Hub 索引 | `README.md`, `AGENTS.md`, `00_inbox.md` |

## Next Action

**建立 `reviews/` 对 `1_speech_deep_analysis.md` 做一轮 Critic，并对 S01 转写可信度与 S03 融资新闻做 Evidence Check 清单，为正式 `synthesis/04_current_synthesis.md` 铺路。**

## Suggested Reading Order

1. 本 `README.md`（身份、范围、阶段、下一步）
2. `AGENTS.md`（作业规则）
3. `00_inbox.md`（未升级材料）
4. `0_speech.md`（原文）
5. `1_speech_deep_analysis.md`（分析）
6. `2_StockWe_融资暂停串联分析_核查.md`（事件核查）
7. 未来：`reviews/` → `synthesis/04_current_synthesis.md`

## Directory Layout（目标）

```text
17_deepseek_Kimi/
├── README.md
├── AGENTS.md
├── 00_inbox.md
├── 0_speech.md
├── 1_speech_deep_analysis.md
├── 2_StockWe_融资暂停串联分析_核查.md
├── sources/          # 可选：来源登记与摘录
├── research/         # 可选：后续分析轮次
├── reviews/          # Critic / Evidence Checker 产出
└── synthesis/        # Current Synthesis 权威结论
```

资料夹可按需创建；**文件少但角色清楚优于空壳目录**。现阶段扁平编号文件有效，进入 Review/Synthesis 后再建子目录。

## CLI Task Format

```text
目标：
输入档：
输出档：
模型角色：
不可改动：
验收条件：
```

## 与 Hub 的关系

- 详细证据与全文只留在本 repo。
- Hub 只登记：路径、Knowledge Stage、Current Synthesis 链接、一个 Open Question / Next Action、Last Updated。
- 勿在 Hub 内复制本专案长文。

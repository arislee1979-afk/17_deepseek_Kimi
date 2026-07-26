# AGENTS.md — 17_deepseek_Kimi 作业规则

> 适用范围：`/home/arislee1979/0_project/17_deepseek_Kimi` 及其所有文件。  
> 本文件是 **知识研究专案** 规则，与 Hub（`30_investment_hub`）规则不同；不要照搬 Hub 的写入边界到此 repo。

## 1. 专案任务

本 repository 研究：

- DeepSeek / 梁文锋公开与外传论述中的战略心智模型。
- 融资、开源、定价、AGI 路线相关事件的事实边界。
- 二手产业评论（X、财经媒体）的事实层与故事层分离。

本 repository **不是**：

- 投资建议或交易信号源。
- 完整 AI 产业数据库。
- Knowledge Project Hub（索引在 `30_investment_hub`）。

详细证据、模型输出、来源与完整结论必须留在本 repo；Hub 只放链接与阶段摘要。

## 2. 任务开始前

所有 agent 必须：

1. 执行或确认 `pwd`，确保位于本专案 canonical path。
2. 阅读本 `AGENTS.md` 与 `README.md`。
3. 若已有 Current Synthesis，先读 synthesis；否则读 README 的 Current Position 与建议阅读顺序。
4. 检查现有文件与 `git status`。
5. 确认任务角色：Writer / Critic / Evidence Checker / Synthesizer / Project Scaffolder / 其他。
6. 保留使用者与其他 agent 的未提交修改。

## 3. 知识阶段（Knowledge Stage）

只使用 Hub 定义的固定值：

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

阶段变更时：

1. 更新本专案 `README.md` 的 Knowledge Stage 与 Last Updated。
2. 若已在 Hub 注册，同步更新 `30_investment_hub/README.md` 对应列（只改索引字段，不贴全文）。

## 4. 多模型知识统合

多个模型不等于多数决。需要时分配不同角色：

| 角色 | 职责 | 典型输出 |
|---|---|---|
| Writer | 第一轮完整分析 | `research/NN_*.md` 或编号分析稿 |
| Critic | 错误前提、反例、过度推论 | `reviews/NN_critic_*.md` |
| Evidence Checker | 来源、数字、时实效核 | `reviews/NN_evidence_*.md` |
| Synthesizer | 共识 / 分歧 / 未知 / 采用结论 | `synthesis/NN_current_synthesis.md` |

规则：

1. 不覆写前序模型原稿；审查与综合写新文件。
2. 不为了形成「共识」而隐藏分歧。
3. 事实、有条件推论、未知必须分栏或分节。
4. Hub / README 的 Current Synthesis **只连到**当前权威 synthesis，不列全部中间产物。
5. 社群帖、未验证转写、匿名信源新闻默认是 Lead 或 Secondary，不得自动升格为 Primary 事实。

## 5. 来源与主张纪律

1. Primary：公司官方声明、监管文件、可验证原始数据。
2. Secondary：主流媒体报道（注明是否匿名信源）、有方法的研究分析。
3. Lead：X/论坛/精校转写/自媒体串联——可驱动调查，不可单独定论。
4. 重大主张尽量附来源 ID 或明确链接；缺来源则标「待查证」。
5. 禁止把「可能 / 据称 / 知情人士」改写成确定语气。
6. 本专案不构成投资、法律或商业决策建议；涉及标的代码时仅作叙事索引。

## 6. 文件写入规则

1. 新材料不确定是否纳入主线时，先写入 `00_inbox.md`。
2. 稳定分析进 `research/` 或沿用编号文件（`0_` / `1_` / `2_`…），命名可读。
3. Review 与 Synthesis 分目录或清晰前缀，避免与 inbox 混放。
4. 不因一篇普通笔记就更新 Hub；仅在建立／归档、阶段变化、权威 synthesis 变化或核心 Open Question / Next Action 变化时更新 Hub。
5. README 的 Open Question 与 Next Action 各自最多一项。
6. 不得在本 repo 内再嵌套其他专案的 `.git`；亦不要把本专案建在 Hub 目录内。

## 7. Git 与安全

1. 修改前确认 branch 与 working tree。
2. 只 stage 本次任务相关文件。
3. 稳定里程碑才 commit；commit 信息说明知识变化（checkpoint），不要求逐行读 diff。
4. 未经明确要求，不得 push、发布、删除专案或大量搬移文件。
5. API key、帐密、个资、未授权付费全文不得进入 repository。
6. 既有正文覆写、权限、删除、外部发布等高风险操作必须检查 diff 或取得人工确认。

## 8. 强制链接输出格式

所有 agent 完成文件建立或修改后，最终回复必须提供以下四行，禁止只给其中一种：

```text
Path: <本机绝对路径>
Tailscale: [<短档名>](http://100.83.106.59:8084/s/<code>.md)
ChromeOS: [<短档名>](http://100.115.92.198:8084/s/<code>.md)
IDE: [<档名>](file:///本机绝对路径)
```

### 8.1 Path

- 必须是 canonical absolute path。
- 不得只给相对路径。
- 路径必须指向实际存在的文件。

### 8.2 Tailscale 与 ChromeOS

- 必须使用 Markdown inline link：`[显示文字](URL)`。
- 禁止只输出裸 URL。
- Tailscale：`http://100.83.106.59:8084/`
- ChromeOS：`http://100.115.92.198:8084/`

### 8.3 长路径或中文档名

先建立 shortlink：

```bash
/home/arislee1979/bin/shortlink <absolute-file-path> <short-code>
```

然后使用：

```text
Tailscale: [<short-code>](http://100.83.106.59:8084/s/<short-code>.md)
ChromeOS: [<short-code>](http://100.115.92.198:8084/s/<short-code>.md)
```

### 8.4 IDE

- 使用 `file:///` absolute path。
- 显示文字使用档名。

### 8.5 本专案范例

```markdown
Path: /home/arislee1979/0_project/17_deepseek_Kimi/README.md
Tailscale: [17_ds_readme](http://100.83.106.59:8084/s/17_ds_readme.md)
ChromeOS: [17_ds_readme](http://100.115.92.198:8084/s/17_ds_readme.md)
IDE: [README.md](file:///home/arislee1979/0_project/17_deepseek_Kimi/README.md)
```

若同时修改多个重要文件，至少对主要产物提供四行格式；其他文件可另外列出，但仍须提供 Path。

## 9. 与 Hub 同步

当且仅当符合 Hub 更新条件时，编辑：

`/home/arislee1979/0_project/30_investment_hub/README.md`

的 Active Knowledge Projects 对应列：

| 字段 | 内容 |
|---|---|
| 专案 | DeepSeek 梁文锋讲话与战略叙事 |
| 专案路径 | `17_deepseek_Kimi` |
| 知识阶段 | 与本 README 一致 |
| 当前 synthesis | 链接到本 repo 权威文件；未建立则写「尚未建立」 |
| 未决问题／下一行动 | 各最多一项，简短 |
| 最后更新 | YYYY-MM-DD |

禁止把 synthesis 全文贴进 Hub。

## 10. 完成验收

任务完成前确认：

- [ ] 文件写在正确 repository（`17_deepseek_Kimi`）。
- [ ] 事实 / 推论 / 未知已分开。
- [ ] 未把 Lead 来源写成确定事实。
- [ ] 未误改其他 agent 文件。
- [ ] `git status` 已检查。
- [ ] 若阶段或权威结论变更，README（及必要时 Hub）已同步。
- [ ] 最终输出含 Path、Tailscale、ChromeOS、IDE。

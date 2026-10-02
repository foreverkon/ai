# 论文项目目录

一篇论文对应一个写作项目。使用用户指定的项目根；未指定时在当前工作目录建立 `<paper-id>/`。多篇论文与不同原文的逆向分析使用不同项目根。先检查现有科研目录：复用已有数据、计算与图片的稳定路径，按下述职责找到现有写作文件；已有同用途文件就在原位更新，不为统一名称复制或搬移。没有写作区时按需建立。

下面是按需形成的目录，不是初始化清单。纯粹构树只创建 `manuscript/paper.intent.md`。

```text
<paper-id>/
├── manuscript/
│   ├── paper.intent.md
│   ├── draft.md
│   ├── project.json
│   └── evidence.json
├── sources/
├── research/
│   ├── tasks.json
│   └── TASK-01/
├── figures/
│   └── FIG-01/
├── review/
│   ├── reviews.json
│   ├── outline.audit.json
│   ├── outline.report.json
│   ├── draft.audit.json
│   └── draft.report.json
└── output/
    └── manuscript.md
```

| 位置 | 用途与创建时机 |
|---|---|
| `manuscript/paper.intent.md` | 唯一权威意图树；开始构树或重构原文时创建。 |
| `manuscript/draft.md` | 唯一当前正文，按句子 ID 填写，公式、图注和表格按块 ID 定位；开始写正文时创建。 |
| `manuscript/project.json` | 树外的模式、依赖、节点状态；确有状态需要记录时创建。 |
| `manuscript/evidence.json` | 证据登记与来源定位；填写断言并核查实际材料时创建。 |
| `sources/` | 尚无稳定保存位置的新收到的原文、笔记、数据；接收材料时按需保存。已有材料直接引用，不复制入此目录。 |
| `research/tasks.json` | 必要的补研究问题、方案与判断标准；识别实际缺口时创建。 |
| `research/TASK-01/` | 该补计算的方案、脚本和结果；执行任务时创建，已有计算目录可直接复用。 |
| `figures/FIG-01/` | 一张图的绘图源、图注素材与成图；准备或制作该图时创建，已有图片直接引用。 |
| `review/` | 实际人审记录、当前评价输入 audit 与报告 report；确认或评价时只创建所需文件。局部评价可用 `PAR-R1.draft.audit.json` 等范围名。 |
| `output/` | 从当前树与正文导出的阅读稿、投稿稿及其他交付格式；实际导出时创建。 |

## 读写约定

- 先读当前树、正文及本次涉及的辅助记录，再修改目标范围。树不放评分、任务状态或操作提醒；正文不重复意图。导出稿是派生文件，修改返回树或 `draft.md`，之后重新导出。
- `project.json`、`draft.md`、`evidence.json` 与树保持同目录，工具会自动发现。复用不同布局时用相应命令支持的 `--project`、`--draft`、`--evidence` 指定文件；`review`、`gate`、`export` 显式传 `--reviews review/reviews.json`。任务文件由 agent 维护，工具不会自动读取它。
- 节点 ID 在重排时保持不变。补研究以稳定 `TASK-01` 等 ID 对应目录，在现有 `project.json.node_data[节点ID].tasks` 中关联；图以稳定 `FIG-01` 等 ID 对应目录，并可作为 `evidence.json.items` 的来源 ID，由句子的 `evidence` 引用。显示编号改变不重命名这些 ID。
- 多人或多 agent 按节点 ID 或 TASK/FIG 目录分工，同一权威文件由指定写入者合并。
- 证据的本地 `items.path` 以登记文件所在目录为基准；例如本布局用 `../figures/FIG-01/figure.png`。登记文件迁移时重算相对路径。本地材料改变后重新核查并更新登记的 `sha256`，再评价受影响正文。
- 正文图块中的图片路径以 `draft.md` 所在目录为基准；工具导出时重算相对路径。图块及其证据登记引用同一张实际成图，图注直接写在正文块中。
- `project.json.basis` 中若记录文件路径，agent 约定以树所在目录为基准，例如 `../sources/results.csv`。工具只存储这些字符串并绑定评价上下文，不会读取或核查 basis 文件。命令行显式路径则以执行命令的当前目录为基准。
- 更新当前权威文件时保留无关内容；人审记录由 `review` 命令追加。audit/report 按阶段、范围命名，重新评价需保留已有评分和实际人审反馈，旧版本可加明确版本名。生成 audit 模板会覆盖同名文件，已有评分时使用新文件名。新任务或新图使用新 ID，不覆盖另一任务的结果。
- 导出会覆盖 `--out` 指定文件；覆盖前检查是否有手工修改，有则先回写 `draft.md` 或使用新导出名。同一当前导出可重新生成，已交付版本用明确版本名保留。工具拒绝将生成文件写到树、正文、状态、证据登记及其本地来源、正文图片或本次传入的审查输入路径，包括指向同一文件的别名；不同时维护多份当前大纲或正文。
- 不建空目录、空状态文件、开发日志或聊天记录，也不另建目录映射清单。不同项目可以引用同一份原材料，但各自的树、正文、状态、审查与导出相互隔离。

## 命令示例

在论文项目根运行。先将下面的工具占位路径替换为本次实际读取的技能目录中 `scripts/paper_tree.py` 的绝对路径；无需将工具复制进论文项目。

```bash
python "<技能目录绝对路径>/scripts/paper_tree.py" validate manuscript/paper.intent.md --level architecture
python "<技能目录绝对路径>/scripts/paper_tree.py" export manuscript/paper.intent.md --reviews review/reviews.json --audit review/draft.audit.json --out output/manuscript.md
```

完成稿导出需当前审查及 A/B 正文评价；审阅中的未完成稿按 [评价](evaluation.md) 使用 `--allow-incomplete`。

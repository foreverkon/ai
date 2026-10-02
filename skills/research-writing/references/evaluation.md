# 量化分级

先说明评价的阶段与范围：章节架构、段落、句子意图，或已写正文。评价记录单独保存，意图树继续只呈现论证。

## 硬指标

| 指标 | 计数 |
|---|---|
| 意图完整性 | 有意图节点 / 全部节点 |
| 句子展开度 | 句子叶 / 全部叶子，按当前审查层次解释 |
| 正文填写度 | 已填写句子 / 计划句子 |
| 语义检查覆盖 | 已评单位 / 当前范围应评单位 |
| 填写证据可定位性 | 记录有效的已写断言 / 全部已写断言 |

工具检查ID、父子顺序、展开程度与记录；质量判断需要读实际意图、正文和材料。

## 语义维度

| 阶段 | 维度 / 检查单位 | 判定问题 |
|---|---|---|
| 意图 | specificity / 节点 | 任务及对象是否具体到能指导写作？ |
| 意图 | parent_fit / 父子关系 | 这些孩子怎样共同完成父任务？ |
| 意图 | sequence / 相邻孩子 | 前提、比较、解释和结论的顺序是否成立？ |
| 意图 | focus / 段落 | 各句是否围绕一个主任务？ |
| 意图 | dependency / 已声明前提 | 依赖是否实际需要？ |
| 正文 | realization / 句子 | 内容是否实现对应意图？ |
| 正文 | evidence_fit / 科学断言 | 实际来源支持哪些具体子句？ |
| 正文 | strength / 科学断言 | 结论范围与材料支持程度是否一致？ |
| 正文 | reader_flow / 相邻单元 | 读者能否顺着已有信息理解下一步？ |
| 正文 | economy / 段落 | 每句是否推进任务，必要条件是否保留？ |
| 正文 | terminology / 句子 | 对象、符号和术语是否准确一致？ |

每单位记定位、具体锚点、分数和理由。0–2的问题另记影响、修改动作与可检查的完成条件。3分只需简洁说明实际检查依据。

| 分数 | 含义 |
|---|---|
| 3 | 当前测试未发现缺陷 |
| 2 | 局部修改即可保留现有论证 |
| 1 | 需要改变前提、结论或补关键判别证据 |
| 0 | 核心论证无法成立或有关键歪曲 |
| null | 尚未检查或材料不足 |

各维度报告`100 × 总分 / (3 × 已评单位)`及覆盖`已评/应评`。指数是有序评分的归一化数值。最终等级由最严重问题决定：全3为A；有2且无更重问题为B；有1且无0为C；有0或关键硬错误为D；语义覆盖不足为U。零分母用null。

局部范围可有等级，正文未全部填写时整篇仍U。未知科学支持与已发现表达缺陷分开；原始数据不可得本身不证明写作有major问题。保存评者分歧及理由，按同一单位比较。

## 用工具评价

`audit-template`生成当前范围的检查单位；实际填行后用`evaluate`得到报告。按 [项目目录](project-structure.md) 将audit/report放在`review/`。意图评价使用树和相关上下文，正文评价还读取与树同目录的draft.md与引用证据。意图变化需重评受影响内容，正文修正只重评正文。

工具检查已写断言时，`project.json.node_data`以句子ID记录`claim_type`（observation、method、inference、hypothesis、definition、background或transition）、`evidence_state`（unassessed、located、missing或conflicting）及`evidence`来源ID列表。`evidence.json`的`items`记录来源的`id`、`kind`、`locator`、实际`checked_by/checked_at`和`path`或`url`；本地来源另记检查时的`sha256`。纯过渡句可用transition。构树阶段不需要这些记录。

在论文项目根运行，将工具占位路径替换为实际技能目录的绝对路径。

```bash
python "<技能目录绝对路径>/scripts/paper_tree.py" audit-template manuscript/paper.intent.md --stage outline --scope PAR-R1 --out review/PAR-R1.outline.audit.json
python "<技能目录绝对路径>/scripts/paper_tree.py" evaluate manuscript/paper.intent.md --stage outline --scope PAR-R1 --audit review/PAR-R1.outline.audit.json --out review/PAR-R1.outline.report.json
```

在模板中填写`reviewer`及实际检查行的分数、原文锚点和理由；正文评价改用`--stage draft`。

`gate`汇总当前三层人审：全篇架构、各节段落、各段句子。`export`将已填写句子按段落合成正文；完成稿使用当前A/B正文评价，标记的未完成稿可使用`--allow-incomplete`。

分析已发表论文时，单独选定原文/图像观察单元并列明分母。图形检查比较设计、坐标/归一化、视觉编码、读出与图文一致性。其评分与重构树评分分开；原始科学未复核部分记U。使用真实案例逐步修订评分锚点，不以期刊身份赋分。

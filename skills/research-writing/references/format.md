# Markdown 意图树

`paper.intent.md` 是唯一的大纲，默认位于 `manuscript/`；文件职责与路径基准见 [项目目录](project-structure.md)。采用以下语法，按原文或计划的阅读顺序排列。

```markdown
# [P] 文章标题

概述：整篇文章要回答的问题、中心论点或主要解释。

论证顺序：各部分如何逐步建立这个解释。

## [SEC-R] Results

概述：这一节需要建立什么认识。

论证顺序：先比较现象，再解释结构变化。

### [SUB-R] Mode selection

概述：解释两类模态如何竞争。

#### [PAR-R1] 比较两类模态随参数变化的增长率，确定主导模态的切换。

- [S-R01] 说明两类模态的比较条件。
- [S-R02] 描述它们的增长率如何随参数变化。
- [S-R03] 从两条曲线的交点确定主导模态的切换。
```

## 各层写什么

- 文章、章节、小节：标题标明主题，`概述：`写论证任务；需要解释顺序时加 `论证顺序：`。
- 段落：标题本身就是该段的意图，不再用正文重复。孩子的排列与内容呈现段内逻辑。
- 句子：列表项写沟通意图，可包含比较对象、想建立的关系或待回答的问题。具体英文措辞在填写阶段产生。

ID保持稳定：根为`P`；章节建议`SEC-`，小节`SUB-`，段落用`PAR-`，句子用`S-`。标题层级决定父子关系；句子属于最近的段落。各级连续展开，句子为叶子。ID可用字母、数字、短横线或下划线。修改顺序时保留ID，新增意图使用新ID。

最初的章节树允许尚未展开；段落审查时展开到段落，句子审查时每段展开到句子。纯粹构树只需要这一个文件。概述用概括性的任务连接孩子，不把每个孩子复制成一串文字。

意图描述论证本身。例如“用能量项比较解释两类模态的供能差异”。“需要核查证据”“避免过度声称”是工作提醒，写在任务或评价里。科学内容中真实的假设、条件与反例仍属于论证。

## 填写及辅助文件

正文保存在与树同目录的`draft.md`：`- [S-R01] Actual English sentence.`。按段落组织，可加段落标题；写过的句子才出现，长句可以缩进续行。与树共享ID，不复制意图。工具按树的段落顺序将这些句子拼成普通`output/manuscript.md`，这是派生阅读稿。

需要工具状态时才创建同目录`project.json`。可记录`mode`（`compose`或`reverse-analysis`）、`language`、`maturity`、研究`basis`；`node_data`按ID记录必要的依赖、术语或填写阶段证据。默认compose、英文、developing，构树不要求先填写状态。

已有论文可在根概述之前放一行`[原文](DOI链接)`，工具据此默认采用reverse-analysis。实际任务明确为新稿时，在project.json指定compose。

人审记录在`review/reviews.json`，证据在与树同目录的`evidence.json`，补研究任务在`research/tasks.json`，评价在`review/`的独立audit/report里；各文件按需要生成。这些数据不嵌入意图树。

## 检查与检索

在论文项目根运行，将工具占位路径替换为实际技能目录的绝对路径。

```bash
python "<技能目录绝对路径>/scripts/paper_tree.py" validate manuscript/paper.intent.md --level architecture
python "<技能目录绝对路径>/scripts/paper_tree.py" validate manuscript/paper.intent.md --level paragraphs
python "<技能目录绝对路径>/scripts/paper_tree.py" validate manuscript/paper.intent.md --level sentences
python "<技能目录绝对路径>/scripts/paper_tree.py" show manuscript/paper.intent.md PAR-R1
```

`show`带祖先与相邻分支上下文；`--no-context`只读目标子树，`--json`输出结构供程序使用。检查或评价局部范围时用`--scope ID`。

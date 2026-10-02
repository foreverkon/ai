---
name: research-writing
description: 通过清晰的 Markdown 意图树协作规划、撰写和修改科研论文，分析已有论文的论证结构，并按阶段量化分级。适用于从已有研究结果发展文章、写作中补充计算或图片的任务。
---

# 科研写作协作

以 `paper.intent.md` 决定文章写什么、怎样论证：文章概述 → 章节概述 → 段落任务 → 句子意图。默认使用标题和列表构成的普通 Markdown；每项意图只出现一次。正文的主线是科学问题、发现和解释。

## 开始工作

- 新建或接手论文项目：先读 [项目目录](references/project-structure.md)，定位唯一当前意图树与正文，按需创建辅助文件；一篇论文一项目，已有科研材料直接复用。
- 构建或修改树：读 [格式](references/format.md) 与 [协作流程](references/collaboration.md)，参考 [完整示例](assets/example/manuscript/paper.intent.md)。
- 分析已有论文：读 [逆向分析](references/reverse-analysis.md)。
- 评价：读 [量化分级](references/evaluation.md)。
- 填写英文内容：读 [英文表达](references/english.md)。
- 流体论文写作：读 [段落、语言、术语与图文](references/domains/fluid-writing.md)；数值流动稳定性任务另读 [数值研究](references/domains/flow-stability.md)。

从已有研究、结果和图片确定中心问题及候选答案。先构建文章与章节的逻辑，再展开段落，最后展开句子意图；在这三个层次分别取得研究者确认。完整的约定范围确认后开始填正文。已有结果是规划基础，待补证据可以在填写时通过计算、作图或修改论证解决。

句子意图写清本句让读者理解或接受什么。段落意图说明这些句子共同完成的任务；章节概述解释这些段落怎样回答问题。文章自己的条件、反例和未决问题放在其论证位置。来源记录、评分、操作提醒、工具状态放在树外。

填写时按段落推进，结合实际材料检验解释；独立公式、图片和表格在正文中按句子 ID 定位，语法见 [格式](references/format.md)。变化若涉及意图，修改相应子树并重新确认；保持意图的正文修正直接完成。用 [协作流程](references/collaboration.md) 处理研究缺口。

## 工具

技能目录中的 `scripts/paper_tree.py` 读取这份 Markdown 树，可检查结构、检索子树、记录确认、评价及导出正文。`show` 默认展示意图和上下文，其他命令见 `--help`。在论文项目根运行命令，工具路径指向实际技能目录；不要假定项目内存在脚本。

意图树是唯一大纲，`draft.md` 是唯一当前正文；`project.json` 与 `evidence.json` 保持与树同目录，审查、补研究、作图及导出按 [项目目录](references/project-structure.md) 分开保存。所有文件按实际需要生成，导出稿只作派生交付，不作为另一份当前正文修改。

交付时给出当前意图树、所改分支及下一步研究或写作动作。详细评分在需要评价时单独交付。

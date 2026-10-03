# 🤖 具身智能论文整理

> 基于 CEAI 2025 "具身智能十五大重点方向"，系统整理具身智能领域核心论文
> 每篇论文 = 精读笔记 + 翻译 + 个人理解，多维度深度拆解

---

## 📋 十五大方向

按四大类组织，点击方向名或子方向标签直接进入。

### A. 感知与认知 (Perception & Cognition)

#### [01 · 多模态具身感知](cards/01-perception/)
[`视觉感知`](cards/01-perception/visual-perception/)
[`触觉感知`](cards/01-perception/tactile-perception/)
[`听觉感知`](cards/01-perception/auditory-perception/)
[`多模态融合`](cards/01-perception/multimodal-fusion/)

#### [02 · 具身知识推理](cards/09-knowledge-reasoning/)
[`常识推理`](cards/09-knowledge-reasoning/common-sense/)
[`因果推理`](cards/09-knowledge-reasoning/causal-reasoning/)
[`知识图谱`](cards/09-knowledge-reasoning/knowledge-graph/)
[`符号推理`](cards/09-knowledge-reasoning/symbolic-reasoning/)

#### [03 · 具身意识与情感](cards/15-consciousness-emotion/)
[`情感计算`](cards/15-consciousness-emotion/affective-computing/)
[`意识建模`](cards/15-consciousness-emotion/consciousness-modeling/)
[`情感交互`](cards/15-consciousness-emotion/emotional-interaction/)
[`心理建模`](cards/15-consciousness-emotion/mental-modeling/)

### B. 学习与模型 (Learning & Models)

#### [04 · 具身自主学习](cards/02-autonomous-learning/)
[`自主探索`](cards/02-autonomous-learning/autonomous-exploration/)
[`课程学习`](cards/02-autonomous-learning/curriculum-learning/)
[`持续学习`](cards/02-autonomous-learning/continual-learning/)
[`元学习`](cards/02-autonomous-learning/meta-learning/)

#### [05 · 具身大模型](cards/03-embodied-llm/)
[`VLA 模型`](cards/03-embodied-llm/vla-models/)
[`多模态大模型`](cards/03-embodied-llm/multimodal-llm/)
[`指令微调`](cards/03-embodied-llm/instruction-tuning/)
[`工具学习`](cards/03-embodied-llm/tool-learning/)

#### [06 · 具身世界模型构建](cards/04-world-model/)
[`物理世界建模`](cards/04-world-model/physics-modeling/)
[`动力学模型`](cards/04-world-model/dynamics-model/)
[`预测编码`](cards/04-world-model/predictive-coding/)
[`3D 重建`](cards/04-world-model/3d-reconstruction/)

#### [07 · 具身强化学习与自适应控制](cards/14-rl-adaptive-control/)
[`深度强化学习`](cards/14-rl-adaptive-control/deep-rl/)
[`模仿学习`](cards/14-rl-adaptive-control/imitation-learning/)
[`逆强化学习`](cards/14-rl-adaptive-control/inverse-rl/)
[`自适应控制`](cards/14-rl-adaptive-control/adaptive-control/)

### C. 行动与交互 (Action & Interaction)

#### [08 · 具身操作](cards/05-manipulation/)
[`抓取操作`](cards/05-manipulation/grasping/)
[`灵巧操作`](cards/05-manipulation/dexterous-manipulation/)
[`工具使用`](cards/05-manipulation/tool-use/)
[`装配任务`](cards/05-manipulation/assembly/)

#### [09 · 具身导航与路径规划](cards/06-navigation/)
[`视觉导航`](cards/06-navigation/visual-navigation/)
[`SLAM`](cards/06-navigation/slam/)
[`运动规划`](cards/06-navigation/motion-planning/)
[`路径规划`](cards/06-navigation/path-planning/)

#### [10 · 具身对话与交互](cards/13-dialogue-interaction/)
[`多模态对话`](cards/13-dialogue-interaction/multimodal-dialogue/)
[`指令理解`](cards/13-dialogue-interaction/instruction-understanding/)
[`人机对话`](cards/13-dialogue-interaction/human-robot-dialogue/)
[`交互学习`](cards/13-dialogue-interaction/interactive-learning/)

### D. 系统与生态 (Systems & Ecology)

#### [11 · 具身人机协同](cards/07-human-robot-collab/)
[`人机协作`](cards/07-human-robot-collab/human-robot-collaboration/)
[`共享控制`](cards/07-human-robot-collab/shared-control/)
[`意图理解`](cards/07-human-robot-collab/intention-understanding/)
[`遥操作`](cards/07-human-robot-collab/teleoperation/)

#### [12 · 群体具身智能](cards/08-swarm-intelligence/)
[`多机器人协同`](cards/08-swarm-intelligence/multi-robot-collab/)
[`群体涌现`](cards/08-swarm-intelligence/swarm-emergence/)
[`分布式规划`](cards/08-swarm-intelligence/distributed-planning/)
[`群体通信`](cards/08-swarm-intelligence/swarm-communication/)

#### [13 · 具身智能仿真平台](cards/10-simulation-platform/)
[`仿真器`](cards/10-simulation-platform/simulators/)
[`数据集`](cards/10-simulation-platform/datasets/)
[`Benchmark`](cards/10-simulation-platform/benchmarks/)
[`评估方法`](cards/10-simulation-platform/evaluation/)

#### [14 · Sim-to-Real 迁移与泛化](cards/11-sim-to-real/)
[`域适应`](cards/11-sim-to-real/domain-adaptation/)
[`域随机化`](cards/11-sim-to-real/domain-randomization/)
[`虚实迁移`](cards/11-sim-to-real/sim2real-transfer/)
[`零样本泛化`](cards/11-sim-to-real/zero-shot-generalization/)

#### [15 · 具身智能安全](cards/12-safety/)
[`安全约束`](cards/12-safety/safety-constraints/)
[`鲁棒性`](cards/12-safety/robustness/)
[`可信 AI`](cards/12-safety/trustworthy-ai/)
[`伦理规范`](cards/12-safety/ethics/)

---

## 📂 论文示例

### 05 · 具身大模型 → VLA 模型

| 论文 | 会议/年份 | 原文 | 精读 | 翻译 | 个人理解 |
|------|----------|------|------|------|---------|
| Attention Is All You Need | NeurIPS 2017 | [📄 arXiv](https://arxiv.org/abs/1706.03762) | [📝 笔记](cards/03-embodied-llm/vla-models/attention-is-all-you-need/) | [🌐 翻译](cards/03-embodied-llm/vla-models/attention-is-all-you-need/07-translation.md) | [💭 理解](cards/03-embodied-llm/vla-models/attention-is-all-you-need/08-understanding.md) |

_更多论文见各子方向目录_

---

## 🎴 每篇论文包含什么

| 内容 | 文件 | 说明 |
|------|------|------|
| 速览卡 | README.md | 论文基本信息 + 关键数据 + 各模块索引 |
| 精读笔记 | 01-06 六维卡片 | 6 个不同视角的深度拆解 |
| 论文翻译 | 07-translation.md | 论文核心章节中文翻译 |
| 个人理解 | 08-understanding.md | 个人阅读后的理解与思考 |

---

## 🚀 如何贡献

请阅读 [贡献指南](CONTRIBUTING.md)。

快速上手：
1. 复制 `templates/paper-card-template/` 到对应子方向目录
2. 重命名为论文短标题（如 `rt-2`）
3. 填写 **README.md**（速览卡）+ 精读笔记
4. 补充 **翻译** 和 **个人理解**
5. 提 PR，等待 review

---

## 📐 仓库结构

```
paper-cards/
├── README.md                    # 本文件（十五大方向索引）
├── CONTRIBUTING.md              # 贡献指南
├── CODEOWNERS                   # 自动分配 reviewer
├── LICENSE
│
├── cards/                       # 📚 论文整理（核心）
│   ├── 01-perception/           # 大方向：多模态具身感知
│   │   ├── README.md            # 方向总览 + 各子方向论文列表
│   │   ├── visual-perception/   # 子方向：视觉感知
│   │   │   ├── README.md
│   │   │   └── paper-title/     # 单篇论文
│   │   └── ...
│   ├── 02-autonomous-learning/  # 具身自主学习
│   ├── 03-embodied-llm/        # 具身大模型
│   └── ...（共15个大方向）
│
├── templates/                   # 📋 模板文件
│   └── paper-card-template/     # 论文卡片模板（8个文件）
│
└── scripts/                     # 🔧 辅助脚本
    └── add-paper.py             # 一键创建论文卡片
```

---

> 💡 十五大方向来源：第二届中国具身智能大会（CEAI 2025）发布的"具身智能十五大重点方向"

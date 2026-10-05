# 🤖 具身智能与大模型论文整理

> 基于 CEAI 2025 "具身智能十五大重点方向"，系统整理具身智能领域核心论文；另设「大模型基础」方向收录 LLM 经典论文
> 每篇论文 = 速览卡 + 精读笔记（含个人理解）+ 翻译，多维度深度拆解

---

## 📋 十六大方向

按「大模型基础 + 四大类具身方向」组织。各方向下的论文卡片由成员自行添加与组织子方向。

| 方向 | 说明 | 索引 |
|------|------|------|
| **大模型基础** | | |
| 00 · 大模型基础 | 不限于具身场景的 LLM 经典论文，作为各方向的公共基础 | [cards/00-llm](cards/00-llm/README.md) |
| **A. 感知与认知** | | |
| 01 · 多模态具身感知 | 让机器人看得见、摸得着、听得清：多感官信息的获取与融合 | [cards/01-perception](cards/01-perception/README.md) |
| 09 · 具身知识推理 | 常识、因果与符号推理能力 | [cards/09-knowledge-reasoning](cards/09-knowledge-reasoning/README.md) |
| 15 · 具身意识与情感 | 情感计算、意识建模与情感交互 | [cards/15-consciousness-emotion](cards/15-consciousness-emotion/README.md) |
| **B. 学习与模型** | | |
| 02 · 具身自主学习 | 机器人如何自我探索、持续学习与进化 | [cards/02-autonomous-learning](cards/02-autonomous-learning/README.md) |
| 03 · 具身大模型 | 大模型驱动的具身智能：VLA、多模态大模型与工具学习 | [cards/03-embodied-llm](cards/03-embodied-llm/README.md) |
| 04 · 具身世界模型构建 | 让机器人理解物理世界的运行规律 | [cards/04-world-model](cards/04-world-model/README.md) |
| 14 · 具身强化学习与自适应控制 | 通过强化学习获得运动与控制能力 | [cards/14-rl-adaptive-control](cards/14-rl-adaptive-control/README.md) |
| **C. 行动与交互** | | |
| 05 · 具身操作 | 机器人手眼协调，完成抓取、操作与装配 | [cards/05-manipulation](cards/05-manipulation/README.md) |
| 06 · 具身导航与路径规划 | 机器人在环境中的定位、建图与移动 | [cards/06-navigation](cards/06-navigation/README.md) |
| 13 · 具身对话与交互 | 自然语言驱动的多模态人机交互 | [cards/13-dialogue-interaction](cards/13-dialogue-interaction/README.md) |
| **D. 系统与生态** | | |
| 07 · 具身人机协同 | 人与机器人的协作、意图理解与共享控制 | [cards/07-human-robot-collab](cards/07-human-robot-collab/README.md) |
| 08 · 群体具身智能 | 多机器人与集群的协同行为与涌现 | [cards/08-swarm-intelligence](cards/08-swarm-intelligence/README.md) |
| 10 · 具身智能仿真平台 | 仿真器、数据集与评测基准 | [cards/10-simulation-platform](cards/10-simulation-platform/README.md) |
| 11 · Sim-to-Real 迁移与泛化 | 从仿真到真实世界的迁移与泛化 | [cards/11-sim-to-real](cards/11-sim-to-real/README.md) |
| 12 · 具身智能安全 | 安全约束、鲁棒性与可信 AI | [cards/12-safety](cards/12-safety/README.md) |

---

## 🎴 每篇论文包含什么

| 模块 | 文件 | 说明 |
|------|------|------|
| 速览卡 | README.md | 论文基本信息 + 关键数据 + 导航 |
| 精读笔记 | reading-notes.md | 精读 + 个人理解（角度按论文特点灵活取舍） |
| 论文翻译 | translation.md | 全文中文翻译 |

---

## 🚀 如何贡献

请阅读 [贡献指南](CONTRIBUTING.md)。

快速上手：
1. 选好方向后，用脚本一键建卡（推荐）：

   ```bash
   python scripts/add-paper.py --title "论文标题" --field 03-embodied-llm --paper-url "https://arxiv.org/abs/xxxx.xxxxx"
   ```

2. 填写 **README.md**（速览卡）+ **reading-notes.md**（精读 + 个人理解）
3. 可选补充 **翻译**
4. 提 PR，等待 review

---

## 📐 仓库结构

```
paper-cards/
├── README.md                    # 本文件（十六大方向总览）
├── CONTRIBUTING.md              # 贡献指南
├── CODEOWNERS                   # 自动分配 reviewer
├── LICENSE
│
├── cards/                       # 📚 论文整理（核心）
│   ├── 00-llm/                  # 大方向：大模型基础（不限于具身场景）
│   ├── 01-perception/           # 大方向：多模态具身感知
│   │   ├── README.md            # 方向总览 + 论文索引
│   │   └── paper-title/         # 单篇论文（可自行按子方向建目录组织）
│   │       ├── README.md        # 速览卡
│   │       ├── reading-notes.md # 精读笔记（含个人理解）
│   │       └── translation.md   # 论文翻译（可选）
│   └── ...（00 大模型基础 + 15 个具身大方向）
│
├── templates/                   # 📋 模板文件
│   └── paper-card-template/     # 论文卡片模板（3个文件）
│
└── scripts/                     # 🔧 辅助脚本
    └── add-paper.py             # 一键创建论文卡片
```

---

> 💡 具身智能十五大方向来源：第二届中国具身智能大会（CEAI 2025）发布的"具身智能十五大重点方向"；大模型基础（00）为仓库自行增设

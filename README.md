# 🎴 具身智能论文知识卡片库

> 基于 CEAI 2025 "具身智能十五大重点方向"，多维度论文精读知识库
> 一篇论文 = 6 张知识卡片，不同视角各取所需

---

## 📋 这是什么

这是团队级别的**具身智能论文知识库**，基于 2025 年第二届中国具身智能大会发布的"具身智能十五大重点方向"组织。

每篇论文从 **6 个不同视角** 解构，形成 6 张独立的知识卡片：

| 视角 | 四要素 | 适合谁看 |
|------|--------|---------|
| 🏗️ 落地复用 | Input / Operation / Cost / Gain | 工程向、做复现 |
| 🔍 批判挑错 | Omission / Flaw / Precondition / DefectResult | 找创新、写综述 |
| 💡 创新拆解 | Inherit / Modify / Break / Margin | 研究向、写论文 |
| 🧪 学术假设 | Hypothesis / Design / Constraint / Conclusion | 理论向、机理分析 |
| ⚔️ 对标 SOTA | Difference / Advantage / Disadvantage / Tradeoff | 组会汇报、选型 |
| 📚 知识沉淀 | Knowledge / Law / Experience / Lesson | 所有人长期积累 |

---

## 🗺️ 十五大方向路线图

不知道从哪开始读？从路线图入手。

### A. 感知与认知

| # | 方向 | 状态 | 进入 |
|---|------|------|------|
| 1 | 多模态具身感知 | ⚪ 未开始 | [cards/01-perception/](cards/01-perception/) |
| 2 | 具身知识推理 | ⚪ 未开始 | [cards/09-knowledge-reasoning/](cards/09-knowledge-reasoning/) |
| 3 | 具身意识与情感 | ⚪ 未开始 | [cards/15-consciousness-emotion/](cards/15-consciousness-emotion/) |

### B. 学习与模型

| # | 方向 | 状态 | 进入 |
|---|------|------|------|
| 4 | 具身自主学习 | ⚪ 未开始 | [cards/02-autonomous-learning/](cards/02-autonomous-learning/) |
| 5 | 具身大模型 | 🟢 进行中 | [cards/03-embodied-llm/](cards/03-embodied-llm/) |
| 6 | 具身世界模型构建 | ⚪ 未开始 | [cards/04-world-model/](cards/04-world-model/) |
| 7 | 具身强化学习与自适应控制 | ⚪ 未开始 | [cards/14-rl-adaptive-control/](cards/14-rl-adaptive-control/) |

### C. 行动与交互

| # | 方向 | 状态 | 进入 |
|---|------|------|------|
| 8 | 具身操作 | ⚪ 未开始 | [cards/05-manipulation/](cards/05-manipulation/) |
| 9 | 具身导航与路径规划 | ⚪ 未开始 | [cards/06-navigation/](cards/06-navigation/) |
| 10 | 具身对话与交互 | ⚪ 未开始 | [cards/13-dialogue-interaction/](cards/13-dialogue-interaction/) |

### D. 系统与生态

| # | 方向 | 状态 | 进入 |
|---|------|------|------|
| 11 | 具身人机协同 | ⚪ 未开始 | [cards/07-human-robot-collab/](cards/07-human-robot-collab/) |
| 12 | 群体具身智能 | ⚪ 未开始 | [cards/08-swarm-intelligence/](cards/08-swarm-intelligence/) |
| 13 | 具身智能仿真平台 | ⚪ 未开始 | [cards/10-simulation-platform/](cards/10-simulation-platform/) |
| 14 | Sim-to-Real 迁移与泛化 | ⚪ 未开始 | [cards/11-sim-to-real/](cards/11-sim-to-real/) |
| 15 | 具身智能安全 | ⚪ 未开始 | [cards/12-safety/](cards/12-safety/) |

> 📍 完整路线图（含学习路径和推荐顺序）：[具身智能路线图](roadmaps/embodied-intelligence-roadmap.md)

---

## 📂 论文卡片索引

### 5. 具身大模型 (03-embodied-llm)

| 论文 | 会议/年份 | 速览卡 | 重点卡片 |
|------|----------|--------|---------|
| Attention Is All You Need | NeurIPS 2017 | [➡️ 进入](cards/03-embodied-llm/attention-is-all-you-need/) | ③ 创新拆解 · ⑥ 知识沉淀 |

_其他方向待补充_

---

## 🚀 如何贡献

请阅读 [贡献指南](CONTRIBUTING.md)。

快速上手：
1. 复制 `templates/paper-card-template/` 到对应方向目录
2. 重命名为论文短标题（如 `rt-2`)
3. 先填 **README.md** + **① 落地复用** + **③ 创新拆解**（必选）
4. 其他卡片按需补充
5. 提 PR，等待 review

---

## 📐 仓库结构

```
paper-cards/
├── README.md                    # 本文件
├── CONTRIBUTING.md              # 贡献指南
├── CODEOWNERS                   # 自动分配 reviewer
├── LICENSE
│
├── roadmaps/                    # 🗺️ 路线图
│   ├── README.md
│   └── embodied-intelligence-roadmap.md  # 15大方向路线图
│
├── cards/                       # 🎴 论文卡片（核心）
│   ├── 01-perception/           # 多模态具身感知
│   ├── 02-autonomous-learning/  # 具身自主学习
│   ├── 03-embodied-llm/        # 具身大模型
│   ├── 04-world-model/          # 具身世界模型构建
│   ├── 05-manipulation/         # 具身操作
│   ├── 06-navigation/          # 具身导航与路径规划
│   ├── 07-human-robot-collab/  # 具身人机协同
│   ├── 08-swarm-intelligence/   # 群体具身智能
│   ├── 09-knowledge-reasoning/  # 具身知识推理
│   ├── 10-simulation-platform/  # 具身智能仿真平台
│   ├── 11-sim-to-real/          # Sim-to-Real 迁移与泛化
│   ├── 12-safety/               # 具身智能安全
│   ├── 13-dialogue-interaction/ # 具身对话与交互
│   ├── 14-rl-adaptive-control/  # 具身强化学习与自适应控制
│   └── 15-consciousness-emotion/ # 具身意识与情感
│
├── templates/                   # 📋 模板文件
│   ├── paper-card-template/     # 论文卡片模板（7个文件）
│   └── roadmap-template.md      # 路线图模板
│
└── scripts/                     # 🔧 辅助脚本
    └── add-paper.py             # 一键创建论文卡片
```

---

> 💡 十五大方向来源：第二届中国具身智能大会（CEAI 2025）发布的"具身智能十五大重点方向"

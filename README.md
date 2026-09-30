# 🤖 具身智能论文整理

> 基于 CEAI 2025 "具身智能十五大重点方向"，系统整理具身智能领域核心论文
> 每篇论文 = 精读笔记 + 翻译 + 个人理解，多维度深度拆解

---

## 📋 十五大方向

按四大类组织，每个大方向下包含多个子方向。

### A. 感知与认知 (Perception & Cognition)

| # | 方向 | 子方向 | 进入 |
|---|------|--------|------|
| 1 | 多模态具身感知 | 视觉感知 · 触觉感知 · 听觉感知 · 多模态融合 | [cards/01-perception/](cards/01-perception/) |
| 2 | 具身知识推理 | 常识推理 · 因果推理 · 知识图谱 · 符号推理 | [cards/09-knowledge-reasoning/](cards/09-knowledge-reasoning/) |
| 3 | 具身意识与情感 | 情感计算 · 意识建模 · 情感交互 · 心理建模 | [cards/15-consciousness-emotion/](cards/15-consciousness-emotion/) |

### B. 学习与模型 (Learning & Models)

| # | 方向 | 子方向 | 进入 |
|---|------|--------|------|
| 4 | 具身自主学习 | 自主探索 · 课程学习 · 持续学习 · 元学习 | [cards/02-autonomous-learning/](cards/02-autonomous-learning/) |
| 5 | 具身大模型 | VLA 模型 · 多模态大模型 · 指令微调 · 工具学习 | [cards/03-embodied-llm/](cards/03-embodied-llm/) |
| 6 | 具身世界模型构建 | 物理世界建模 · 动力学模型 · 预测编码 · 3D 重建 | [cards/04-world-model/](cards/04-world-model/) |
| 7 | 具身强化学习与自适应控制 | 深度强化学习 · 模仿学习 · 逆强化学习 · 自适应控制 | [cards/14-rl-adaptive-control/](cards/14-rl-adaptive-control/) |

### C. 行动与交互 (Action & Interaction)

| # | 方向 | 子方向 | 进入 |
|---|------|--------|------|
| 8 | 具身操作 | 抓取操作 · 灵巧操作 · 工具使用 · 装配任务 | [cards/05-manipulation/](cards/05-manipulation/) |
| 9 | 具身导航与路径规划 | 视觉导航 · SLAM · 运动规划 · 路径规划 | [cards/06-navigation/](cards/06-navigation/) |
| 10 | 具身对话与交互 | 多模态对话 · 指令理解 · 人机对话 · 交互学习 | [cards/13-dialogue-interaction/](cards/13-dialogue-interaction/) |

### D. 系统与生态 (Systems & Ecology)

| # | 方向 | 子方向 | 进入 |
|---|------|--------|------|
| 11 | 具身人机协同 | 人机协作 · 共享控制 · 意图理解 · 遥操作 | [cards/07-human-robot-collab/](cards/07-human-robot-collab/) |
| 12 | 群体具身智能 | 多机器人协同 · 群体涌现 · 分布式规划 · 群体通信 | [cards/08-swarm-intelligence/](cards/08-swarm-intelligence/) |
| 13 | 具身智能仿真平台 | 仿真器 · 数据集 · Benchmark · 评估方法 | [cards/10-simulation-platform/](cards/10-simulation-platform/) |
| 14 | Sim-to-Real 迁移与泛化 | 域适应 · 域随机化 · 虚实迁移 · 零样本泛化 | [cards/11-sim-to-real/](cards/11-sim-to-real/) |
| 15 | 具身智能安全 | 安全约束 · 鲁棒性 · 可信 AI · 伦理规范 | [cards/12-safety/](cards/12-safety/) |

---

## 📂 论文卡片示例

### 5. 具身大模型 → VLA 模型

| 论文 | 会议/年份 | 原文 | 精读 | 翻译 | 个人理解 |
|------|----------|------|------|------|---------|
| Attention Is All You Need | NeurIPS 2017 | [📄 arXiv](https://arxiv.org/abs/1706.03762) | [📝 笔记](cards/03-embodied-llm/attention-is-all-you-need/) | [🌐 翻译](cards/03-embodied-llm/attention-is-all-you-need/07-translation.md) | [💭 理解](cards/03-embodied-llm/attention-is-all-you-need/08-understanding.md) |

_更多方向论文待补充_

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
1. 复制 `templates/paper-card-template/` 到对应方向的子方向目录
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
│   ├── 01-perception/           # 多模态具身感知
│   │   ├── README.md            # 方向汇总 + 子方向分类
│   │   ├── visual-perception/   # 子方向：视觉感知
│   │   │   └── paper-title/     # 单篇论文
│   │   └── ...
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
│   └── paper-card-template/     # 论文卡片模板
│       ├── README.md            # 速览卡
│       ├── 01-reuse.md          # ① 落地复用
│       ├── 02-critique.md       # ② 批判挑错
│       ├── 03-innovation.md     # ③ 创新拆解
│       ├── 04-hypothesis.md     # ④ 学术假设
│       ├── 05-sota-compare.md   # ⑤ 对标 SOTA
│       ├── 06-knowledge.md      # ⑥ 知识沉淀
│       ├── 07-translation.md    # ⑦ 论文翻译
│       └── 08-understanding.md  # ⑧ 个人理解
│
└── scripts/                     # 🔧 辅助脚本
    └── add-paper.py             # 一键创建论文卡片
```

---

> 💡 十五大方向来源：第二届中国具身智能大会（CEAI 2025）发布的"具身智能十五大重点方向"

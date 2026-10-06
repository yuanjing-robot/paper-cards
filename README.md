# 🤖 具身智能与大模型论文整理

> 基于 CEAI 2025 "具身智能十五大重点方向"，系统整理具身智能领域核心论文；另设「大模型基础」方向收录 LLM 经典论文
> 每篇论文 = 速览卡 + 精读笔记（含个人理解）+ 翻译，多维度深度拆解

---

## 📋 十六大方向

按「大模型基础 + 四大类具身方向」组织。每个方向下收录 3 篇代表性经典论文，作为入门与贡献参考。

---

### 00 · 大模型基础（LLM Fundamentals）

> 不限于具身场景的大模型经典论文，作为具身智能各方向的公共基础。详细索引见 [cards/00-llm](cards/00-llm)。

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](cards/00-llm/bert/) | NAACL 2019 | [📄 原文](https://arxiv.org/abs/1810.04805) | [📝 精读笔记](cards/00-llm/bert/reading-notes.md) | [🌐 翻译](cards/00-llm/bert/translation.md) |
| [Language Models are Few-Shot Learners (GPT-3)](cards/00-llm/gpt-3/) | NeurIPS 2020 | [📄 原文](https://arxiv.org/abs/2005.14165) | [📝 精读笔记](cards/00-llm/gpt-3/reading-notes.md) | [🌐 翻译](cards/00-llm/gpt-3/translation.md) |
| [LLaMA: Open and Efficient Foundation Language Models](cards/00-llm/llama/) | arXiv 2023 | [📄 原文](https://arxiv.org/abs/2302.13971) | [📝 精读笔记](cards/00-llm/llama/reading-notes.md) | [🌐 翻译](cards/00-llm/llama/translation.md) |

---

### 01 · 多模态具身感知

> 让机器人看得见、摸得着、听得清：多感官信息的获取与融合。详细索引见 [cards/01-perception](cards/01-perception)。

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation](cards/01-perception/pointnet/) | CVPR 2017 | [📄 原文](https://arxiv.org/abs/1612.00593) | [📝 精读笔记](cards/01-perception/pointnet/reading-notes.md) | [🌐 翻译](cards/01-perception/pointnet/translation.md) |
| [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](cards/01-perception/vit/) | ICLR 2021 | [📄 原文](https://arxiv.org/abs/2010.11929) | [📝 精读笔记](cards/01-perception/vit/reading-notes.md) | [🌐 翻译](cards/01-perception/vit/translation.md) |
| [Learning Transferable Visual Models From Natural Language Supervision (CLIP)](cards/01-perception/clip/) | ICML 2021 | [📄 原文](https://arxiv.org/abs/2103.00020) | [📝 精读笔记](cards/01-perception/clip/reading-notes.md) | [🌐 翻译](cards/01-perception/clip/translation.md) |

---

### 02 · 具身自主学习

> 机器人如何自我探索、持续学习与进化。详细索引见 [cards/02-autonomous-learning](cards/02-autonomous-learning)。

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge Base](cards/02-autonomous-learning/minedojo/) | NeurIPS 2022 | [📄 原文](https://arxiv.org/abs/2206.08853) | [📝 精读笔记](cards/02-autonomous-learning/minedojo/reading-notes.md) | [🌐 翻译](cards/02-autonomous-learning/minedojo/translation.md) |
| [Voyager: An Open-Ended Embodied Agent with Large Language Models](cards/02-autonomous-learning/voyager/) | TMLR 2023 | [📄 原文](https://arxiv.org/abs/2305.16291) | [📝 精读笔记](cards/02-autonomous-learning/voyager/reading-notes.md) | [🌐 翻译](cards/02-autonomous-learning/voyager/translation.md) |
| [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](cards/02-autonomous-learning/open-x-embodiment/) | ICRA 2024 | [📄 原文](https://arxiv.org/abs/2310.08864) | [📝 精读笔记](cards/02-autonomous-learning/open-x-embodiment/reading-notes.md) | [🌐 翻译](cards/02-autonomous-learning/open-x-embodiment/translation.md) |

---

### 03 · 具身大模型

> 大模型驱动的具身智能：VLA、多模态大模型与工具学习。详细索引见 [cards/03-embodied-llm](cards/03-embodied-llm)。

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances (SayCan)](cards/03-embodied-llm/saycan/) | CoRL 2022 | [📄 原文](https://arxiv.org/abs/2204.01691) | [📝 精读笔记](cards/03-embodied-llm/saycan/reading-notes.md) | [🌐 翻译](cards/03-embodied-llm/saycan/translation.md) |
| [PaLM-E: An Embodied Multimodal Language Model](cards/03-embodied-llm/palm-e/) | ICML 2023 | [📄 原文](https://arxiv.org/abs/2303.03378) | [📝 精读笔记](cards/03-embodied-llm/palm-e/reading-notes.md) | [🌐 翻译](cards/03-embodied-llm/palm-e/translation.md) |
| [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](cards/03-embodied-llm/rt-2/) | CoRL 2023 | [📄 原文](https://arxiv.org/abs/2307.15818) | [📝 精读笔记](cards/03-embodied-llm/rt-2/reading-notes.md) | [🌐 翻译](cards/03-embodied-llm/rt-2/translation.md) |

---

### 04 · 具身世界模型构建

> 让机器人理解物理世界的运行规律。详细索引见 [cards/04-world-model](cards/04-world-model)。

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [World Models](cards/04-world-model/world-models/) | NeurIPS 2018 | [📄 原文](https://arxiv.org/abs/1803.10122) | [📝 精读笔记](cards/04-world-model/world-models/reading-notes.md) | [🌐 翻译](cards/04-world-model/world-models/translation.md) |
| [Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model (MuZero)](cards/04-world-model/muzero/) | Nature 2019 | [📄 原文](https://arxiv.org/abs/1911.08265) | [📝 精读笔记](cards/04-world-model/muzero/reading-notes.md) | [🌐 翻译](cards/04-world-model/muzero/translation.md) |
| [Mastering Diverse Domains through World Models (DreamerV3)](cards/04-world-model/dreamer-v3/) | arXiv 2023 | [📄 原文](https://arxiv.org/abs/2301.04104) | [📝 精读笔记](cards/04-world-model/dreamer-v3/reading-notes.md) | [🌐 翻译](cards/04-world-model/dreamer-v3/translation.md) |

---

### 05 · 具身操作

> 机器人手眼协调，完成抓取、操作与装配。详细索引见 [cards/05-manipulation](cards/05-manipulation)。

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [Dex-Net 2.0: Deep Learning to Plan Robust Grasps with Synthetic Point Clouds and Analytic Metrics](cards/05-manipulation/dexnet-2/) | RSS 2017 | [📄 原文](https://arxiv.org/abs/1703.09312) | [📝 精读笔记](cards/05-manipulation/dexnet-2/reading-notes.md) | [🌐 翻译](cards/05-manipulation/dexnet-2/translation.md) |
| [QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation](cards/05-manipulation/qt-opt/) | CoRL 2018 | [📄 原文](https://arxiv.org/abs/1806.10293) | [📝 精读笔记](cards/05-manipulation/qt-opt/reading-notes.md) | [🌐 翻译](cards/05-manipulation/qt-opt/translation.md) |
| [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](cards/05-manipulation/diffusion-policy/) | RSS 2023 | [📄 原文](https://arxiv.org/abs/2303.04137) | [📝 精读笔记](cards/05-manipulation/diffusion-policy/reading-notes.md) | [🌐 翻译](cards/05-manipulation/diffusion-policy/translation.md) |

---

### 06 · 具身导航与路径规划

> 机器人在环境中的定位、建图与移动。详细索引见 [cards/06-navigation](cards/06-navigation)。

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [ORB-SLAM2: an Open-Source SLAM System for Monocular, Stereo and RGB-D Cameras](cards/06-navigation/orb-slam2/) | IEEE T-RO 2017 | [📄 原文](https://arxiv.org/abs/1610.06475) | [📝 精读笔记](cards/06-navigation/orb-slam2/reading-notes.md) | [🌐 翻译](cards/06-navigation/orb-slam2/translation.md) |
| [Visual Language Maps for Robot Navigation (VLMaps)](cards/06-navigation/vlmaps/) | ICRA 2023 | [📄 原文](https://arxiv.org/abs/2210.05714) | [📝 精读笔记](cards/06-navigation/vlmaps/reading-notes.md) | [🌐 翻译](cards/06-navigation/vlmaps/translation.md) |
| [ViNT: A Foundation Model for Visual Navigation](cards/06-navigation/vint/) | CoRL 2023 | [📄 原文](https://arxiv.org/abs/2306.14846) | [📝 精读笔记](cards/06-navigation/vint/reading-notes.md) | [🌐 翻译](cards/06-navigation/vint/translation.md) |

---

### 07 · 具身人机协同

> 人与机器人的协作、意图理解与共享控制。详细索引见 [cards/07-human-robot-collab](cards/07-human-robot-collab)。

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [Cooperative Inverse Reinforcement Learning (CIRL)](cards/07-human-robot-collab/cirl/) | NeurIPS 2016 | [📄 原文](https://arxiv.org/abs/1606.03137) | [📝 精读笔记](cards/07-human-robot-collab/cirl/reading-notes.md) | [🌐 翻译](cards/07-human-robot-collab/cirl/translation.md) |
| [Shared Autonomy via Deep Reinforcement Learning](cards/07-human-robot-collab/shared-autonomy-drl/) | RSS 2018 | [📄 原文](https://arxiv.org/abs/1803.07169) | [📝 精读笔记](cards/07-human-robot-collab/shared-autonomy-drl/reading-notes.md) | [🌐 翻译](cards/07-human-robot-collab/shared-autonomy-drl/translation.md) |
| [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ALOHA)](cards/07-human-robot-collab/aloha/) | RSS 2023 | [📄 原文](https://arxiv.org/abs/2304.13705) | [📝 精读笔记](cards/07-human-robot-collab/aloha/reading-notes.md) | [🌐 翻译](cards/07-human-robot-collab/aloha/translation.md) |

---

### 08 · 群体具身智能

> 多机器人与集群的协同行为与涌现。详细索引见 [cards/08-swarm-intelligence](cards/08-swarm-intelligence)。

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments (MADDPG)](cards/08-swarm-intelligence/maddpg/) | NeurIPS 2017 | [📄 原文](https://arxiv.org/abs/1706.02275) | [📝 精读笔记](cards/08-swarm-intelligence/maddpg/reading-notes.md) | [🌐 翻译](cards/08-swarm-intelligence/maddpg/translation.md) |
| [QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent RL](cards/08-swarm-intelligence/qmix/) | ICML 2018 | [📄 原文](https://arxiv.org/abs/1803.11485) | [📝 精读笔记](cards/08-swarm-intelligence/qmix/reading-notes.md) | [🌐 翻译](cards/08-swarm-intelligence/qmix/translation.md) |
| [The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games (MAPPO)](cards/08-swarm-intelligence/mappo/) | NeurIPS 2022 | [📄 原文](https://arxiv.org/abs/2103.01955) | [📝 精读笔记](cards/08-swarm-intelligence/mappo/reading-notes.md) | [🌐 翻译](cards/08-swarm-intelligence/mappo/translation.md) |

---

### 09 · 具身知识推理

> 常识、因果与符号推理能力。详细索引见 [cards/09-knowledge-reasoning](cards/09-knowledge-reasoning)。

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [Translating Embeddings for Modeling Multi-relational Data (TransE)](cards/09-knowledge-reasoning/transe/) | NeurIPS 2013 | [📄 原文](https://arxiv.org/abs/1301.3785) | [📝 精读笔记](cards/09-knowledge-reasoning/transe/reading-notes.md) | [🌐 翻译](cards/09-knowledge-reasoning/transe/translation.md) |
| [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](cards/09-knowledge-reasoning/chain-of-thought/) | NeurIPS 2022 | [📄 原文](https://arxiv.org/abs/2201.11903) | [📝 精读笔记](cards/09-knowledge-reasoning/chain-of-thought/reading-notes.md) | [🌐 翻译](cards/09-knowledge-reasoning/chain-of-thought/translation.md) |
| [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](cards/09-knowledge-reasoning/tree-of-thoughts/) | NeurIPS 2023 | [📄 原文](https://arxiv.org/abs/2305.10601) | [📝 精读笔记](cards/09-knowledge-reasoning/tree-of-thoughts/reading-notes.md) | [🌐 翻译](cards/09-knowledge-reasoning/tree-of-thoughts/translation.md) |

---

### 10 · 具身智能仿真平台

> 仿真器、数据集与评测基准。详细索引见 [cards/10-simulation-platform](cards/10-simulation-platform)。

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [Habitat: A Platform for Embodied AI Research](cards/10-simulation-platform/habitat/) | ICCV 2019 | [📄 原文](https://arxiv.org/abs/1904.01201) | [📝 精读笔记](cards/10-simulation-platform/habitat/reading-notes.md) | [🌐 翻译](cards/10-simulation-platform/habitat/translation.md) |
| [SAPIEN: A SimulAted Part-based Interactive ENvironment](cards/10-simulation-platform/sapien/) | CVPR 2020 | [📄 原文](https://arxiv.org/abs/2003.08515) | [📝 精读笔记](cards/10-simulation-platform/sapien/reading-notes.md) | [🌐 翻译](cards/10-simulation-platform/sapien/translation.md) |
| [Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning](cards/10-simulation-platform/isaac-gym/) | arXiv 2021 | [📄 原文](https://arxiv.org/abs/2108.10470) | [📝 精读笔记](cards/10-simulation-platform/isaac-gym/reading-notes.md) | [🌐 翻译](cards/10-simulation-platform/isaac-gym/translation.md) |

---

### 11 · Sim-to-Real 迁移与泛化

> 从仿真到真实世界的迁移与泛化。详细索引见 [cards/11-sim-to-real](cards/11-sim-to-real)。

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](cards/11-sim-to-real/domain-randomization/) | IROS 2017 | [📄 原文](https://arxiv.org/abs/1703.06907) | [📝 精读笔记](cards/11-sim-to-real/domain-randomization/reading-notes.md) | [🌐 翻译](cards/11-sim-to-real/domain-randomization/translation.md) |
| [Sim-to-Real Transfer of Robotic Control with Dynamics Randomization](cards/11-sim-to-real/dynamics-randomization/) | ICRA 2018 | [📄 原文](https://arxiv.org/abs/1710.06537) | [📝 精读笔记](cards/11-sim-to-real/dynamics-randomization/reading-notes.md) | [🌐 翻译](cards/11-sim-to-real/dynamics-randomization/translation.md) |
| [Learning Dexterous In-Hand Manipulation (Dactyl)](cards/11-sim-to-real/dactyl/) | IJRR 2019 | [📄 原文](https://arxiv.org/abs/1808.00177) | [📝 精读笔记](cards/11-sim-to-real/dactyl/reading-notes.md) | [🌐 翻译](cards/11-sim-to-real/dactyl/translation.md) |

---

### 12 · 具身智能安全

> 安全约束、鲁棒性与可信 AI。详细索引见 [cards/12-safety](cards/12-safety)。

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [Concrete Problems in AI Safety](cards/12-safety/concrete-problems/) | arXiv 2016 | [📄 原文](https://arxiv.org/abs/1606.06565) | [📝 精读笔记](cards/12-safety/concrete-problems/reading-notes.md) | [🌐 翻译](cards/12-safety/concrete-problems/translation.md) |
| [Constrained Policy Optimization (CPO)](cards/12-safety/cpo/) | ICML 2017 | [📄 原文](https://arxiv.org/abs/1705.10528) | [📝 精读笔记](cards/12-safety/cpo/reading-notes.md) | [🌐 翻译](cards/12-safety/cpo/translation.md) |
| [Control Barrier Functions: Theory and Applications](cards/12-safety/cbf/) | ECC 2019 | [📄 原文](https://arxiv.org/abs/1903.11199) | [📝 精读笔记](cards/12-safety/cbf/reading-notes.md) | [🌐 翻译](cards/12-safety/cbf/translation.md) |

---

### 13 · 具身对话与交互

> 自然语言驱动的多模态人机交互。详细索引见 [cards/13-dialogue-interaction](cards/13-dialogue-interaction)。

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [Inner Monologue: Embodied Reasoning through Planning with Language Models](cards/13-dialogue-interaction/inner-monologue/) | CoRL 2022 | [📄 原文](https://arxiv.org/abs/2207.05608) | [📝 精读笔记](cards/13-dialogue-interaction/inner-monologue/reading-notes.md) | [🌐 翻译](cards/13-dialogue-interaction/inner-monologue/translation.md) |
| [LLM-Planner: Grounded Planning for Embodied Agents with Large Language Models](cards/13-dialogue-interaction/llm-planner/) | NeurIPS 2023 | [📄 原文](https://arxiv.org/abs/2312.10435) | [📝 精读笔记](cards/13-dialogue-interaction/llm-planner/reading-notes.md) | [🌐 翻译](cards/13-dialogue-interaction/llm-planner/translation.md) |
| [TidyBot: Personalized Robot Assistance with Large Language Models](cards/13-dialogue-interaction/tidybot/) | IROS 2023 | [📄 原文](https://arxiv.org/abs/2305.18712) | [📝 精读笔记](cards/13-dialogue-interaction/tidybot/reading-notes.md) | [🌐 翻译](cards/13-dialogue-interaction/tidybot/translation.md) |

---

### 14 · 具身强化学习与自适应控制

> 通过强化学习获得运动与控制能力。详细索引见 [cards/14-rl-adaptive-control](cards/14-rl-adaptive-control)。

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [Human-level control through deep reinforcement learning (DQN)](cards/14-rl-adaptive-control/dqn/) | Nature 2015 | [📄 原文](https://arxiv.org/abs/1312.5602) | [📝 精读笔记](cards/14-rl-adaptive-control/dqn/reading-notes.md) | [🌐 翻译](cards/14-rl-adaptive-control/dqn/translation.md) |
| [Proximal Policy Optimization Algorithms (PPO)](cards/14-rl-adaptive-control/ppo/) | arXiv 2017 | [📄 原文](https://arxiv.org/abs/1707.06347) | [📝 精读笔记](cards/14-rl-adaptive-control/ppo/reading-notes.md) | [🌐 翻译](cards/14-rl-adaptive-control/ppo/translation.md) |
| [Soft Actor-Critic: Off-Policy Maximum Entropy Deep RL (SAC)](cards/14-rl-adaptive-control/sac/) | ICML 2018 | [📄 原文](https://arxiv.org/abs/1801.01290) | [📝 精读笔记](cards/14-rl-adaptive-control/sac/reading-notes.md) | [🌐 翻译](cards/14-rl-adaptive-control/sac/translation.md) |

---

### 15 · 具身意识与情感

> 情感计算、意识建模与情感交互。详细索引见 [cards/15-consciousness-emotion](cards/15-consciousness-emotion)。

| 论文 | 会议/年份 | 原文 | 精读笔记 | 翻译 |
|------|----------|------|---------|------|
| [Using millions of emoji occurrences to learn pre-trained representations for detecting sentiment, emotion and sarcasm (DeepMoji)](cards/15-consciousness-emotion/deepmoji/) | ACL 2017 | [📄 原文](https://arxiv.org/abs/1508.06615) | [📝 精读笔记](cards/15-consciousness-emotion/deepmoji/reading-notes.md) | [🌐 翻译](cards/15-consciousness-emotion/deepmoji/translation.md) |
| [The Consciousness Prior](cards/15-consciousness-emotion/consciousness-prior/) | arXiv 2017 | [📄 原文](https://arxiv.org/abs/1709.08568) | [📝 精读笔记](cards/15-consciousness-emotion/consciousness-prior/reading-notes.md) | [🌐 翻译](cards/15-consciousness-emotion/consciousness-prior/translation.md) |
| [Machine Theory of Mind](cards/15-consciousness-emotion/machine-theory-of-mind/) | ICML 2018 | [📄 原文](https://arxiv.org/abs/1802.07740) | [📝 精读笔记](cards/15-consciousness-emotion/machine-theory-of-mind/reading-notes.md) | [🌐 翻译](cards/15-consciousness-emotion/machine-theory-of-mind/translation.md) |

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

> 💡 具身智能十五大方向来源：第二届中国具身智能大会（CEAI 2025）发布的"具身智能十五大重点方向"；大模型基础（00）为仓库自行增设

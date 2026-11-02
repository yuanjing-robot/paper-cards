# 深度阅读：Learning to Grasp the Ungraspable with Emergent Extrinsic Dexterity
> 📄 对应论文：[Learning to Grasp the Ungraspable with Emergent Extrinsic Dexterity](https://arxiv.org/abs/2211.01500)
> 整理者：@asang
> 最后更新：2026-11-02
---
## 1. 问题与动机
- **要解决什么问题？** 这篇论文研究的是 "Occluded Grasping"（遮挡抓取）问题：一个目标抓取姿态在物体初始放置时被桌面/环境遮挡了，简单两指夹爪无法直接飞过去抓住。想想一个侧放在桌上的麦片盒——理想的抓取点在盒子底部，正顶着桌面，夹爪根本伸不进去。
- **为什么重要？** 现实世界里这种情况太普遍了：东西掉在角落、放在墙边、摞在一堆里……如果机器人只能抓那些"正好放得开"的物体，实用性大打折扣。更关键的是，昂贵的灵巧手（dexterous hand）又贵又脆弱，工业上大量用的还是便宜耐用的两指夹爪（parallel gripper）。如果简单夹爪也能"借力打力"完成复杂任务，经济价值巨大。
- **之前的做法卡在哪？** 前人工作的三个主要问题（§2.1）：
  1. **运动是手工设计的**（hand-crafted trajectories）。比如给机器人硬编码好"先推三下再翻一下"的轨迹，换个物体尺寸就不灵了。
  2. **依赖特定接触假设**。比如假设夹指和物体之间有固定数量的 sticking contact，一到真机上接触模式一变就崩。
  3. **需要特殊末端执行器**。Sun et al. 2011 那篇最接近的工作，为了做 pre-grasp 运动用了特制末端执行器，然后还要第二个夹爪来抓。
- **本文怎么绕过这些坑？** 用模型无关强化学习（model-free RL）训练一个闭环策略，不让人来规划运动序列。策略学出来之后，它会**自己涌现**出推物体到墙边旋转、调整姿态等 extrinsic dexterity 行为——没有显式奖励这些中间行为，只奖励最终成功抓取。
## 2. 核心方法
论文 §4 描述的系统设计，看似简单实则每个环节都是为了让 RL 能学到有意义的接触操作行为。拆成六个关键点：

### 2.1 RL 问题设计
- **状态空间**：目标抓取配置 ${}^{O}g$（物体坐标系下）、末端执行器位姿 ${}^{W}E$（世界坐标系）、物体位姿 ${}^{W}O$（世界坐标系）。
- **动作空间**：末端执行器在其局部坐标系下的 delta pose $\Delta E$（6-DoF 增量）。
- **算法**：Goal-conditioned Soft Actor-Critic (SAC)，用 rlkit 框架。Goal 就是目标抓取位姿。

### 2.2 奖励函数（关键设计）
- 奖励函数很朴素——**没有任何显式奖励 extrinsic dexterity 行为**。只在 episode 结束时判断是否成功（位置差 $\Delta T < \epsilon_T$ 且姿态差 $\Delta\theta < \epsilon_\theta$），成功给 +1，否则 0。
- 这意味着策略必须**自己发现**推、翻、旋转这些中间步骤是有用的。论文把这个称为 "emergent behaviors"（涌现行为）。

### 2.3 Extrinsic Environment（容器）
- 把物体放在一个"盒子"（bin）里训练。这个 bin 不是随便加的，它**自然限制了物体的运动范围**：物体被推到墙边只能旋转不能乱飞，被推到角落会被卡住。
- 如果没有 bin，物体被一推就飞出去，RL agent 根本学不到"推了有什么效果"。bin 的存在让接触动力学变得足够可控。

### 2.4 柔顺底层控制器（Compliant Controller）
- 这是另一个关键设计。论文 §4.4 没有用硬的位置/速度控制器，而是用了**柔顺控制器**——夹爪在接触时会"让一让"，而不是硬刚。
- 原因很直观：接触操作（contact-rich manipulation）需要大量高力接触，硬控制器在仿真里还行，一到真机上因为微小的模型误差就会产生巨大的接触力，要么把物体推飞，要么触发安全停止。柔顺控制让接触行为更稳定。

### 2.5 多抓取训练与选择
- 一个物体可能有多个可行的抓取配置。论文 §4.5 用**课程学习（curriculum learning）** 来训练：一开始只给一个容易的抓取目标，逐步增加到多个、更难的抓取目标。
- 评估时需要从多个候选抓取中选一个实际执行。论文试过两种选择策略：
  - 简单策略：选离末端最近的那个（nearest neighbor）
  - Q-maximizer：选 Q 值最高的那个
  - 两者效果差不多，简单策略就够用了。

### 2.6 自动域随机化（ADR）
- 用 Automatic Domain Randomization（来自 OpenAI 2018）来提升 sim2real 鲁棒性。
- ADR 会根据当前策略的成功率自动调节物理参数的随机范围：成功率高 → 扩大随机范围（让模拟更难）；成功率低 → 缩小随机范围（让模拟更容易）。
- 随机化的参数包括：物体质量、摩擦系数、恢复系数、物体尺寸、初始位置噪声等。
- **关键数据**：真机实验中，不开 ADR 的成功率只有 33%，开了 ADR 跳到 78%（Table 5）——这是 sim2real 的核心杠杆。

## 3. 关键结果
### 3.1 仿真结果
- **训练曲线**（Figure 5）：cereal box 训练到大约 500 万步时成功率接近 100%。
- **消融实验**（Figure 6）：去掉任何一个关键组件性能都大幅下降——
  - 去掉 bin：成功率掉到 ~60%
  - 去掉柔顺控制：成功率掉到 ~30%
  - 去掉 ADR：仿真中还行但真机崩了
  - 去掉课程学习：多抓取训练时学不动

### 3.2 涌现行为
- 策略自己学会了**推物体到墙边旋转**（Figure 7）：先快速推一下让物体靠上垂直墙，然后持续施力让它沿墙旋转，直到目标抓取姿态暴露出来，然后抓。
- **恢复行为**（Recovery Behaviors）：从不确定中自动恢复。项目主页视频里有展示——物体没有按预期落位时，策略能即时调整，继续推。

### 3.3 真机实验（§5.5，论文核心贡献）
- **硬件**：Sawyer 机械臂 + 平行夹爪 + Kinect 深度相机。
- **视觉**：ICP 做物体位姿估计，把点云配准到已知物体模板。
- **测试物体**：7 种没见过的物体（mug、container、box、toy truck 等），跨大小、密度、摩擦系数、形状。
- **核心数据**（Table 5）：
  | 指标 | 数值 |
  |------|------|
  | with ADR, 平均 | **78%** |
  | without ADR, 平均 | 33% |
  | init-pose（固定初始姿态） | 56% |
- **不同物体差异大**：最容易的 container 能到 10/10，最难的 toy truck 只有 4/10（with ADR）。

### 3.4 泛化能力
- 策略**跨物体泛化**到没见过的物体，只要物体大致有一个平面可以靠墙旋转。
- 论文附录 A.1 做了物理参数敏感性分析，ADR 训练的策略对参数扰动更鲁棒。

## 4. 批判性思考
### 4.1 局限性（论文 §6 自己列的）
1. **只能处理有平面的物体**。Occluded Grasping 任务假设物体能靠在墙上旋转，球形物体或者没有平面的物体直接就不行了。
2. **需要外部"辅助物"**（墙、容器）。如果场景里什么都没有，策略也无能为力。这其实是 extrinsic dexterity 的固有局限——名字里就写了要"利用外部资源"。
3. **视觉位姿估计是瓶颈**。真机实验依赖精确的物体位姿估计（ICP），一旦视觉估计不准，整个 pipeline 就崩了。论文附录 A.2 测试了位姿噪声的影响，噪声一大成功率就掉。
4. **任务只定义了一种 occluded grasping**。物体被墙挡住是一种常见情况，但还有很多其他遮挡模式（物体摞在一起、被其他物体压住……），这篇论文没覆盖。

### 4.2 没说但值得想的
- **为什么没有显式奖励也能学到推物体？** 直觉上，推物体到正确位置要好多步，稀疏奖励怎么传得回去？可能的原因是：bin 让状态空间足够小，随机探索就能偶尔撞到"碰巧推对了"的轨迹，SAC 的 off-policy 特性让这些稀有样本被反复利用。
- **柔顺控制器是必须的吗？** 论文消融实验里硬控制器仿真成功率只有 30%。可能原因是硬控制器在接触时产生大的作用力，让物体运动变得不可预测，RL 很难学到稳定的策略。
- **为什么不用更多机器人先验？** 比如给策略一个"向前推"的基元。论文选择让所有行为自己涌现，这是个风格选择——简洁但可能牺牲样本效率。

## 5. 个人收获
- **简单方法也能做出强结果**：整个系统的技术栈非常朴素——模型无关 SAC、标准仿真环境、自动域随机化、柔顺控制。没有 fancy 的网络结构、没有复杂的层次 RL、没有 world model。但就是这些**正确的工程设计选择**拼在一起，让 sim2real 跑通了。这提醒我不要总是追着新方法跑，先把经典方法的工程细节做扎实。
- **接触操作的 RL 痛点**：之前总觉得 RL 在真实机器人上难落地是因为数据不够，但这篇论文让我意识到更根本的问题——**接触动力学的 sim-to-real gap**。ADR 解决的不是"见得多了就不会差"，而是让策略在各种物理参数下都学到一个鲁棒的行为模式。柔顺控制器的设计也很点睛——与其让仿真和真机精确匹配，不如让策略对小的物理误差不敏感。
- **Extrinsic Dexterity 这个视角**：机器人操作不应该只考虑"机器人+物体"二元关系，还要把**环境**当成第三个参与者。墙、桌面、角落……这些"免费的工具"在日常操作里被人类无意识地大量利用，但机器人研究里长期被忽略。这个视角值得深入。

## 6. 延伸阅读（可选）
- **前序 extrinsic dexterity 工作**：
  - [A Framework for Dexterous Manipulation with Simple Grippers](https://ieeexplore.ieee.org/document/5979662) (Sun et al., 2011) — 最相关的前序工作，用特制末端执行器做 pre-grasp
  - [Prehensile Pushing: In-Hand Manipulation with Alternating Slip Events](https://ieeexplore.ieee.org/document/6631123) (Dafle et al., 2014) — 两指夹爪的推操作
- **Sim2Real RL 基础**：
  - [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](https://arxiv.org/abs/1703.06907) (Tobin et al., 2017) — Domain Randomization 思想起源
  - [Automatic Domain Randomization](https://arxiv.org/abs/1810.10562) (OpenAI, 2018) — ADR 原始论文
- **后续延伸**（David Held 实验室）：
  - [Learning Extrinsic Dexterity with Parameterized Manipulation Primitives](https://arxiv.org/abs/2310.17785) (Zhou et al., 2023) — 引入参数化操作基元
  - [DexDiff: Towards Extrinsic Dexterity Manipulation of Ungraspable Objects](https://arxiv.org/abs/2409.05493) — Diffusion 模型做 extrinsic dexterity
- **Grasping 领域基础**：
  - [A Survey on Grasp Synthesis](https://ieeexplore.ieee.org/document/8446950) (Bohg et al., 2014) — 抓取综述
  - [Dex-Net 2.0](https://arxiv.org/abs/1703.09312) (Mahler et al., 2017) — 经典数据驱动抓取

---
> ✍️ **写作提示**
> - 引用数据标明出处（论文 Table X / Figure Y）
> - 不编造信息，不确定的内容标注「待确认」
> - 不要复述论文原文，用自己的话写

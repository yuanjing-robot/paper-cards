# 论文翻译

> 📄 对应论文原文：[A Comprehensive Survey on World Models for Embodied AI](https://arxiv.org/abs/2510.16732)
> 翻译者：@WSB-666
> 最后更新：2026-10-31

---

## 📝 翻译说明

- 依据版本：arXiv 2510.16732v3（2026-06-25）
- 翻译范围：正文全文（§I–§VII）。表 I–VI 的逐行数据从略，仅保留表头说明与关键结论，需要逐行数值请查原文
- 翻译原则：直译为主，专业术语首次出现保留英文；公式以文字准确释义；参考文献编号原样保留

### 术语表

| 英文 | 中文 | 备注 |
|------|------|------|
| World Model | 世界模型 | 内部模拟器，刻画环境动力学 |
| Embodied AI | 具身智能 | — |
| Decision-Coupled | 决策耦合 | 与特定控制目标绑定 |
| General-Purpose | 通用 | 任务无关模拟器 |
| Sequential Simulation and Inference | 序列仿真与推断 | 自回归逐步展开 |
| Global Difference Prediction | 全局差分预测 | 并行预测未来状态 |
| Global Latent Vector (GLV) | 全局隐向量 | 紧凑隐状态 |
| Token Feature Sequence (TFS) | 词元特征序列 | 离散 token 序列 |
| Spatial Latent Grid (SLG) | 空间隐网格 | BEV / 体素 |
| Decomposed Rendering Representation (DRR) | 分解式渲染表示 | NeRF / 3DGS |
| Rollout | 推演 | 沿隐状态向前展开 |
| Occupancy | 占用 | 3D 占用预测 |
| BEV | 鸟瞰图 | Bird's-Eye View |
| Sim-to-Real (S2R) | 仿真到现实 | — |

---

## 📖 摘要 (Abstract)

具身智能（embodied AI）要求智能体能够感知复杂环境、在其中行动，并预判其行动将如何重塑未来的世界状态。世界模型（world model）充当内部模拟器，刻画环境动力学（dynamics），使前向与反事实推演（rollout）成为可能，从而支撑感知、预测与决策。本综述提出具身智能中世界模型的统一框架。具体而言，我们形式化问题设定与学习目标，并提出一个三轴分类体系，涵盖：(1) 功能（Functionality），决策耦合（decision-coupled）与通用（general-purpose）；(2) 时间建模（Temporal Modeling），序列仿真与推断（Sequential Simulation and Inference）与全局差异预测（Global Difference Prediction）；(3) 空间表示（Spatial Representation），全局隐向量（Global Latent Vector）、词元特征序列（Token Feature Sequence）、空间隐网格（Spatial Latent Grid）与分解渲染表示（Decomposed Rendering Representation）。我们系统梳理机器人、自动驾驶与通用视频场景下的数据资源与评估指标，涵盖像素预测质量、状态级理解与任务性能。此外，我们对最先进模型进行定量比较，并提炼关键开放挑战，包括统一数据集的稀缺、评估指标需从像素保真度转向物理一致性的需求、模型性能与实时控制所需计算效率之间的权衡，以及在缓解误差累积的同时实现长时程时间一致性的核心建模难点。最后，我们在 https://github.com/Li-Zn-H/AwesomeWorldModels 维护一份精选文献目录。

关键词：世界模型、具身智能、时间建模、空间表示。

## 🔑 I 引言 (Introduction)

具身智能旨在使智能体能够感知复杂的多模态环境、在其中行动，并预判其行动将如何改变未来的世界状态 [batra2020rearrangement, gupta2024essential]。这一能力的核心是世界模型，即一种内部模拟器，它刻画环境动力学，以支撑用于感知、预测与决策的前向与反事实推演 [liu2025aligning, ding2024understanding]。本综述聚焦于能为具身智能体给出可执行预测的世界模型，并将其与静态场景描述或不能刻画可控动力学的纯生成式视觉模型区分开来。

认知科学表明，人类通过整合感官输入来构建关于世界的内部模型。这些模型不仅预测与仿真未来事件，也塑造感知并引导行动 [clark1998being, barsalou1999perceptions, friston2010free]。受此观点启发，早期关于世界模型的 AI 研究植根于基于模型的强化学习（model-based RL），其中隐状态转移模型被用于提升样本效率与规划（planning）性能 [fung2025embodied]。Ha 与 Schmidhuber 的开创性工作 [ha2018recurrent] 明确了"世界模型"这一术语，并启发了 Dreamer 系列 [hafner2020dream, hafner2021mastering, hafner2025mastering]，凸显了学习到的动力学如何驱动基于想象的策略（policy）优化。更近期，大规模生成建模与多模态学习的进展将世界模型从最初聚焦策略学习扩展到能够高保真预测未来的通用环境模拟器，其代表如 Sora [brooks2024video] 与 V-JEPA 2 [assran2025v]。这一扩展使功能角色、时间建模策略与空间表示趋于多样，同时在各个子领域之间引入了术语与分类上的不一致。

忠实刻画环境动力学需要同时处理状态的时间演化与场景的空间编码 [liu2025aligning]。长时程推演容易受到误差累积的影响，这使得一致性成为视频预测与策略想象的核心挑战 [venkatraman2015improving, asadi2018lipschitz]。类似地，粗糙或以二维为中心的布局无法提供足够的几何细节，难以应对遮挡、物体恒存性与几何感知规划等挑战。与之相对，神经场 [agro2024uno] 与结构化体素网格 [wei2024occllama] 等体积化或三维占据表示提供了几何结构，更好地支撑预测与控制。综合来看，这些论点使时间建模与空间表示成为核心设计维度，从根本上影响具身智能体的预测时程、物理保真度与下游性能。

近年来已有若干综述梳理了这一快速增长的文献。总体而言，这些综述遵循两条主要路径。其一是面向功能的视角。例如，Ding 等人 [ding2024understanding] 依据理解与预测这两项核心功能对相关工作分类，而 Zhu 等人 [zhu2024sora] 则提出了基于世界模型核心能力的框架。其二是应用驱动的路径，聚焦于自动驾驶等特定领域。值得注意的是，Guan 等人 [guan2024world] 与 Feng 等人 [feng2025survey] 给出了自动驾驶领域世界模型技术的概览。为补充这些视角，我们采用围绕决策耦合、时间建模与空间表示的三轴分类体系，并将其一致地应用于机器人、自动驾驶与通用视频世界模型。

论文结构（图 1）：

- §I 引言
- §II 背景
- §III 分类体系
- §IV 数据与指标
- §V 性能
- §VI 挑战与趋势
- §VII 结论

- 核心概念（§II-A）
- 决策耦合（§III-A）
- 通用（§III-B）
- 序列式（§III-A1 与 §III-B1）：循环结构、自回归方法
- 全局（§III-A2 与 §III-B2）：全局预测、掩码 JEPA
- 空间表示：全局隐向量、词元特征序列、空间隐网格、分解渲染表示

图 1：本综述的结构。该图沿三个轴对世界模型进行分类，并展示每一轴的代表性方法，从而提供该领域的统一视图。图的设计部分受 [assran2025v, hafner2025mastering, lu2025infinicube, chen2024drivinggpt] 启发。

为弥补具身智能语境下统一分类体系的缺失，本工作提出一个以功能、时间建模与空间表示这三个核心轴为中心的框架。在功能层面，该框架区分决策耦合与通用模型。在时间层面，它区分序列仿真与推断同全局差异预测。最后，在空间层面，它涵盖从隐特征到显式几何与神经场的一系列表示。该框架为组织现有方法提供了统一结构，并整合了标准化的数据集与评估指标。这一结构便于定量比较，并为未来研究提供全景式、可操作的知识地图。

图 1 给出了本文结构与分类体系的概览。我们在 §II 首先概述世界模型的核心概念与理论基础。§III 介绍我们的三轴分类体系，并将代表性方法映射到该框架上。§IV 梳理用于训练与评估的数据集及评估指标。§V 给出最先进模型的定量比较。§VI 讨论开放挑战与有前景的研究方向，§VII 对全综述作结。

## 📚 II 背景 (Background)

### II-A 核心概念 (Core Concepts)

如 §I 所述，世界模型可被视为一种内部模拟器，它实现"压缩—预测—控制"流程：高维观测首先被压缩为隐状态，动力学模型预测该状态在动作作用下将如何演化，而策略或规划器通过对想象的隐状态推演进行推理来控制智能体。在操作层面，这一功能可分解为三个紧密耦合的方面：

- 仿真与规划（Simulation & Planning）：利用学习到的动力学生成合理的情景，使智能体无需与真实世界交互即可通过想象评估潜在动作。
- 时间演化（Temporal Evolution）：学习编码后的状态如何演化，从而实现时间上一致的推演。
- 空间表示（Spatial Representation）：以适当保真度编码场景几何，使用隐词元或神经场等格式为控制提供上下文。

这三根支柱共同实例化了"压缩—预测—控制"的视角，并共同决定世界模型如何在计算效率、长时程一致性与视觉保真度之间的基本权衡中取舍。它们为 §III 提出的分类体系提供了概念基础，并在下文的数学框架中得到形式化。

### II-B 世界模型的数学表述 (Mathematical Formulation of World Models)

我们将环境交互形式化为部分可观测马尔可夫决策过程（POMDP）[smallwood1973optimal]。为保持记号一致，我们在 t=0 处定义空的初始动作 a0，使动力学可以统一书写。在每一步 t≥1，智能体接收到观测 o_t 并采取动作 a_t，而真实状态 s_t 始终不可观测。为处理这种部分可观测性，世界模型使用单步滤波后验（posterior）推断学习到的隐状态 z_t，其中假定前一隐状态 z_{t-1} 已概括了相关历史。最后，z_t 被用于重构（reconstruction）o_t：

- 动力学先验 pθ(z_t | z_{t-1}, a_{t-1})；
- 滤波后验 qφ(z_t | z_{t-1}, a_{t-1}, o_t)；
- 重构 pθ(o_t | z_t)。

(1)

与马尔可夫结构一致，观测与隐状态的联合分布分解为：初始隐状态先验 pθ(z0) 与各时刻动力学先验 pθ(z_t | z_{t-1}, a_{t-1})、重构项 pθ(o_t | z_t) 从 t=1 到 T 的连乘，即 pθ(o_{1:T}, z_{0:T} | a_{0:T-1}) 等于该乘积。

(2)

为推断隐状态，我们必须以一个按时间因子化的变分分布来近似难以计算的真实后验 pθ(z_{0:T} | o_{1:T}, a_{0:T-1})：该变分分布 qφ(z_{0:T} | o_{1:T}, a_{0:T-1}) 等于初始后验 qφ(z0 | o1) 与各时刻滤波后验 qφ(z_t | z_{t-1}, a_{t-1}, o_t) 从 t=1 到 T 的连乘。

(3)

当忽略动作 a 的输入时，该式确实退化为无动作情形。直接最大化对数似然 log pθ(o_{1:T} | a_{0:T-1}) 难以计算。因此，我们改用近似后验 qφ 优化证据下界（ELBO），从而为学习模型参数提供可处理的目标：对数似然等于对联合分布 pθ(o_{1:T}, z_{0:T} | a_{0:T-1}) 关于 z_{0:T} 的积分取对数，该式不小于在 qφ 下联合分布与变分分布之比的对数期望，并记该下界为 L(θ, φ)。

(4)

在 pθ 与 qφ 均满足马尔可夫分解的假设下，该 ELBO 分解为一个重构目标与一个 KL 正则（KL regularization）项：L(θ, φ) 等于各时刻在 qφ(z_t) 下 log pθ(o_t | z_t) 的期望之和，减去 qφ(z_{0:T} | o_{1:T}, a_{0:T-1}) 与 pθ(z_{0:T} | a_{0:T-1}) 之间的 KL 散度。

(5)

因此，现代世界模型采用"重构—正则"的训练范式：似然项 log pθ(o_t | z_t) 促使模型忠实地预测观测，而 KL 正则项使滤波后验 qφ(z_t | z_{t-1}, a_{t-1}, o_t) 与动力学先验 pθ(z_t | z_{t-1}, a_{t-1}) 对齐。此类世界模型可用循环模型 [sun2024learning, zhai2025recurrent, aljalbout2025accelerating]、基于 Transformer 的架构 [chen2022transdreamer, robine2023transformerbased, zhang2023storm] 或基于扩散的解码器 [zhu2025unified, qi2025strengthening, guo2025flowdreamer, huang2025enerverse, alhaija2025cosmos] 实现。无论采用哪种方式，学习到的隐状态轨迹 z_{1:T} 都充当紧凑的预测性记忆，以支撑具身智能中的下游策略优化、模型预测控制与反事实推理。

---

## 🧩 III 分类法 (Taxonomy)

我们从三个核心维度对世界模型进行归类，这些维度为本综述后续的分析提供了基础。

第一个维度是决策耦合（decision coupling），它区分决策耦合（Decision-Coupled）与通用（General-Purpose）世界模型。决策耦合模型是任务专用的，其学习到的动力学与某一特定控制目标紧密对齐，这提升了样本效率与闭环性能，但削弱了在训练分布之外的泛化能力。相比之下，通用模型是与任务无关的模拟器，优先覆盖广泛的视觉与物理现象，便于跨任务、跨领域迁移，但其预训练目标常与下游控制失配，除非被显式缓解，否则会导致次优或脆弱的行为。

第二个维度是时序推理（temporal reasoning），它划分出两种不同的预测范式。序列仿真与推断（Sequential Simulation and Inference）以自回归（autoregressive）方式建模动力学，逐步展开未来状态。这提供了细粒度控制，并天然支持闭环规划，但在长时域上会出现误差累积，且计算成本随 rollout 长度线性增长。相比之下，全局差分预测（Global Difference Prediction）并行地直接估计未来状态，将计算在时间上摊销，并降低长时域想象的墙钟时延，但其全局更新削弱了闭环交互性，并倾向于平滑掉细粒度的局部动力学，因此不太适合需要频繁反馈与精确逐步控制的任务。

第三个维度是空间表示（spatial representation），它包含当前研究用于建模空间状态的四种主要策略。这些策略位于连贯性—保真度—效率（coherence-fidelity-efficiency）权衡的不同位置：

1. 全局隐向量（Global Latent Vector）将世界状态编码为紧凑向量，支持高效的实时展开，但牺牲了细粒度空间细节。

2. 词元特征序列（Token Feature Sequence）将世界状态离散化为词元序列，通过注意力建模词元—词元依赖，支持细粒度多模态建模，但通常需要大数据、大模型与高推理成本。

3. 空间隐网格（Spatial Latent Grid）通过将场景编码为鸟瞰图（BEV）或体素网格来注入空间先验，保留局部拓扑并支持多视图融合与类地图规划，但内存开销大、分辨率受限，且对非结构化环境的适应性较弱。

4. 分解式渲染表示（Decomposed Rendering Representation）将场景分解为可渲染基元（例如 3D 高斯泼溅（3DGS）[kerbl20233d]、神经辐射场（NeRF）[mildenhall2020nerf]），并通过可微渲染重建观测，从而获得几何一致、高保真且对象级可控的视图，但训练代价高昂，且处理快速动态或拓扑变化的能力有限。

下列表格应用这一分类法对代表性工作进行归类。表 I 回顾机器人领域的方法，而表 II 聚焦自动驾驶。两者共同为后续各节的详细分析提供了路线图。

> 表 I：机器人与通用领域代表性世界模型汇总（Dec/Seq/GLV 等缩写含义见速览卡；逐行数据见原文 Table I，此处从略。）

> 表 II：自动驾驶领域代表性世界模型汇总（分类法缩写与特征说明见原文表注；逐行数据见原文 Table II，此处从略。）

### III-A 决策耦合世界模型

#### III-A1 序列仿真与推断

全局隐向量（Global Latent Vector）。早期的决策耦合世界模型将序列推断与全局隐状态相结合。这些方法主要使用循环神经网络（Recurrent Neural Networks，RNNs）以实现高效的实时与长时域预测。

Ha 与 Schmidhuber [ha2018recurrent] 提出了一个早期世界模型，将观测编码到隐空间，并用 RNN 建模动力学以支持策略优化。在此基础上，PlaNet [hafner2019learning] 引入了循环状态空间模型（Recurrent State-Space Model，RSSM），它将确定性记忆与随机成分融合，从而实现稳健的长时域想象。其后继模型 Dreamer、DreamerV2 与 DreamerV3 [hafner2020dream, hafner2021mastering, hafner2025mastering] 进一步完善了这一形式，并启发了大量后续研究。

在 RSSM 基础上，若干变体修改或移除解码器以更好地捕捉动力学。例如，Dreaming [okada2021dreaming] 使用对比学习与线性方法缓解状态漂移，而 DreamerPro [deng2022dreamerpro] 用原型替代解码器以抑制视觉干扰。为进一步增强鲁棒性，研究者提出了 HRSSM [sun2024learning]，其特点是双分支架构，可在不重建的情况下对齐隐观测并共享信息。除架构改进之外，DisWM [wang2025disentangled] 将语义知识从视频内容中解耦，并将其蒸馏进世界模型，从而实现跨领域泛化。LeWorldModel [maes2026leworldmodel] 将这种紧凑隐变量路线扩展到 RSSM 式目标之外，它通过下一嵌入损失与 SIGReg 防坍缩正则联合训练像素编码器与动作条件 Transformer 预测器，用于无奖励的隐空间规划。

近期 RSSM 扩展的一个共同主题是可迁移性，它反映跨模态、跨任务与跨具身的泛化能力，以支撑稳健的真实机器人应用。在表示层面，PreLAR [zhang2024prelar] 学习隐式动作抽象，以衔接视频预训练表示与控制微调。类似地，Wang 等人 [wang2025latent] 使用光流作为与具身无关的动作表示来细化行为克隆策略，促进跨不同具身的迁移。SENSEI [sancaktar2025sensei] 蒸馏视觉语言模型（Vision-Language Model，VLM）以获得语义奖励，并采用一个 RSSM 在内部学习预测与传播这些奖励。在有限监督下，SR-AIF [nguyen2025sr] 利用先验偏好学习与自我修正，在稀疏奖励、连续控制场景中实现自适应学习。为缓解仿真到现实（Sim-to-Real，S2R）差距，ReDRAW [lanier2025adapting] 在仿真中预训练，并用少量无奖励数据在真实环境中适配，对隐动力学施加残差修正。为处理失配，AdaWM [wang2025adawm] 识别学习到的动力学与规划器之间的差异，并有选择地微调关键组件。WMP [lai2025world] 等方法处理困难任务的 S2R 迁移，DayDreamer [wu2023daydreamer] 则展示了在物理机器人上的样本高效部署。为拓宽迁移，FOUNDER [wang2025founder] 将基础模型的表示锚定到世界模型的状态空间，用时序距离预测处理灵活目标；LUMOS [nematollahi2025lumos] 引入了语言条件模仿框架，在隐空间中同策略运行并带内在奖励，从而实现到真实世界机器人的零样本迁移。

基于 RSSM 的模型也被用于自动驾驶。MILE [hu2022model] 利用离线专家数据，实现用于规划的想象未来状态。SEM2 [gao2024enhance] 将语义过滤与多源采样结合，以提取驾驶相关特征并平衡数据分布。Popov 等 [popov2025mitigating] 通过一个隐生成世界模型处理协变量偏移，使策略与专家状态重新对齐。为提升安全性，VL-SAFE [qu2025vl] 使用 VLM 导出的安全分数监督世界模型，以生成安全轨迹。最后，CALL [wang2025ego] 通过引入以自车为中心的信息共享，将 RSSM 框架扩展到多智能体强化学习（Multi-Agent RL），增强了规划能力。

与 RSSM 不同，TransDreamer [chen2022transdreamer] 引入了 Transformer 状态空间模型（Transformer State-Space Model，TSSM），替换 Dreamer 中的循环核心，从而显著增强了捕捉长时域依赖的能力。与之互补的 OSVI-WM [goswami2025osvi] 采用因果 Transformer 做单样本模仿学习（Imitation Learning，IL），自回归预测未来隐轨迹并解码为物理路点，用于机器人控制。

一些方法继续使用 RNN 捕捉时序依赖。在建模方面，RWM [li2025robotic] 引入了一个双自回归、领域无关的神经模拟器，用于长时域预测。相比之下，X-MOBILITY [liu2025x] 将建模与策略学习解耦，先用多头解码器进行大规模预训练，随后通过监督微调得到强策略。对于人形运动，DWL [gu2024advancing] 与 WMR [sun2025learning] 采用端到端（end-to-end，E2E）框架。这些框架通过去噪或梯度阻断状态估计器从部分观测重建状态，从而支持跨复杂真实地形的零样本迁移。

近来，以 Mamba 为代表的状态空间模型（State Space Models，SSMs）作为 RNN 与 Transformer 的替代方案出现，兼具线性时间复杂度与长时域建模能力。在此基础上，GLAM [he2025glam] 通过基于 Mamba 的并行框架提升保真度与效率，该框架整合全局与局部模块，以捕捉上下文与细粒度动力学。

除前向时序建模之外，逆动力学建模（inverse dynamics modeling，IDM）是世界模型构建中的一个关键范式。IDM 推断从初始状态转移到目标状态所需的动作。Agrawal 等 [agrawal2016learning] 将前向模型与 IDM 集成用于多步预测，为后续研究奠定了基础。更近期的工作包括 GLAMOR [paster2021planning]，它训练一个对象条件 IDM 来预测到达指定目标所需的动作。在 Dreamer 风格智能体中，Iso-Dream [pan2022iso] 利用 IDM 将世界模型分解为可控与不可控成分，并用不可控状态的展开来指导策略学习。

词元特征序列（Token Feature Sequence）。该范式集中于建模离散词元之间的依赖关系。这一表示支持因果推断、多模态整合以及大语言模型（Large Language Model，LLM）的复用。

近期以 RSSM 为中心的研究开始利用词元级依赖来增强表示学习与时序推理。例如，MWM [seo2023masked] 通过掩码自编码器将视觉词元与基于 RSSM 的动力学解耦，同时提升性能与数据效率。NavMorph [yao2025navmorph] 引入了带上下文演化记忆的自演化 RSSM，用于在线适应。为获得时间抽象，WISTER [burchi2025learning] 采用动作条件对比预测编码训练 TSSM，捕捉高层时序特征。类似地，TWM [robine2023transformerbased] 在训练时用 Transformer 将多模态词元与历史状态对齐，而在推理时依赖轻量策略。为处理长时域任务，一些方法将 LLM 与 RSSM 集成，以把目标分解为子任务。例如 EvoAgent [feng2025evoagent] 用 LLM 指导低层动作并正则化 RSSM 更新。相比之下，RoboHorizon [chen2025robohorizon] 用稠密奖励增强任务识别，并通过掩码自编码器利用关键任务片段。

在自动驾驶中，基于词元的序列表示越来越常被采用，以建模跨模态交互与时空结构。DrivingWorld [hu2024drivingworld] 将用于时序动力学的下一状态预测与用于空间结构的下一词元预测配对。对于多模态控制，Doe-1 [zheng2024doe] 将闭环驾驶表述为对感知—描述—动作词元的自回归预测，统一了感知、预测与规划；DrivingGPT [chen2024drivinggpt] 交错视觉与动作词元，将世界建模与轨迹规划转化为下一词元预测。为增强多样性与安全性，LatentDriver [xiao2025learning] 将未来动作建模为混合分布，并用规划器采样的中间动作驱动世界模型。与此同时，Vasudevan 等 [vasudevan2025planning] 提出了一个自适应模型，对周围智能体进行预测以实现安全导航。

基于词元的范式也扩展到更广的机器人领域。在强化学习（RL）中，IRIS [micheli2023transformers] 与 TWM [dedieu2025improving] 利用离散词元，通过想象式或混合 rollout 实现数据高效的策略学习。DyWA [lyu2025dywa] 以轨迹动力学为条件，并联合预测未来状态（含单视图点云与本体感觉模态），从而改进动作学习。EgoAgent [chen2025egoagent] 在 Transformer 内交错状态—动作序列建模，实现统一的感知、预测与动作推断。词元化表示统一了视觉、语言与动作（VLA）等多模态输入，使通用智能体具备跨域适应性，如 WorldVLA [cen2025worldvla] 所示。DreamZero [ye2026world] 进一步将该范式实例化为建立在预训练视频扩散骨干之上的世界动作模型（World Action Model），它从语言、视觉历史与本体感觉自回归预测未来视频与动作，以支持实时闭环机器人控制。近期研究将环境状态编码为离散符号词元，并以动作为条件下一个词元预测，如 DCWM [scannell2025discrete] 与 TrajWorld [yin2025trajectory] 所示。

近期研究强化了词元化表示与规划之间的联系，尤其是通过对象中心方法。这些模型，如 CarFormer [hamdan2024carformer]、Jeong 等 [jeong2025object] 的工作以及 Dyn-O [wang2025dyn]，将场景表示为一组槽（slot）。CarFormer 在 BEV 中自回归建模这些槽之间的关系。Jeong 等加入了语言引导的操作，而 Dyn-O 使用带 dropout 调度的 Mamba 进行时序建模，并将静态与动态要素解耦。

Δ-IRIS [micheli2024efficient] 引入了混合 Transformer，将词元与随机 Δ-词元整合以捕捉动力学。D²PO [wang2025world] 采用偏好学习联合优化状态预测与动作选择，增强模型对底层动力学的理解。为提升效率，MineWorld [guo2025mineworld] 通过并行预测序列加速词元生成，并引入 IDM 作为可控性度量。同时，PIVOT-R [zhang2024pivot] 与 ReOI [chen2025reimagination] 将 VLM 纳入控制。PIVOT-R 解析指令以产生基于路点的计划，再由动作模块解码为低层控制；而 ReOI 检测不合理的预测元素，重新想象这些干扰项，并重新整合修正后的内容。

在词元化基础上，一些研究采用自回归扩散以实现稳定生成与长时域规划。Epona [zhang2025epona] 将时空建模（由 Transformer 处理）与长时域多模态生成（通过轨迹与视觉扩散 Transformer（Diffusion Transformers，DiTs）实现）解耦。Goff 等 [goff2025learning] 用 DiT 实例化状态转移，从而支持同策略训练与数秒级闭环 rollout。SceneDiffuser++ [tan2025scenediffuser++] 进一步将其推进到城市级交通仿真，对智能体与交通灯施加多张量扩散，产生稳定的闭环 rollout。在导航方面，NWM [bar2025navigation] 引入高效的条件 DiT，以模拟视觉轨迹用于零样本规划。

另一个新兴方向是利用 LLM 与思维链（Chain-of-Thought，CoT）向世界模型注入显式推理。NavCoT [lin2025navcot] 将导航分解为想象、过滤与预测，支持参数高效的域内训练；ECoT [zawalski2025robotic] 利用基础模型组成的流水线生成推理标签，以训练 VLA 策略。像 MineDreamer [zhou2025minedreamer] 这样的变体引入了想象链（Chain-of-Imagination，CoI），由多模态 LLM 想象未来观测以引导扩散并指导动作；FSDrive [zeng2025futuresightdrive] 生成物理约束的未来场景并将其作为 CoT 监督，使 VLM 能作为 IDM 用于规划。

其他方法直接将 LLM 与世界模型耦合，以实现规划与数据生成。Dyna-Think [yu2025dyna] 通过蒸馏得到的 LLM 融合推理与行动；RIG [zhao2025rig] 端到端地统一推理与想象，形成通用策略。在显式动力学与长时域方面，Gkountouras 等 [gkountouras2025language] 训练了一个因果世界模型模拟器，将 LLM 锚定到环境的因果推理与规划技能之中；Statler [yoneda2024statler] 使 LLM 能维护结构化的世界状态，用读取器负责规划、写入器负责更新；Inner Monologue [huang2023inner] 将闭环反馈纳入 LLM，使智能体能够像人类思维那样推理与斟酌。最后，WoMAP [yin2025womap] 合成 3DGS 场景并训练一个世界模型，用于细化 VLM 指令以实现精确执行。

空间隐网格（Spatial Latent Grid）。通过将特征编码到几何对齐的网格上，或引入显式空间先验，该范式保留局部性，并支持高效的卷积或注意力更新与流式 rollout。

在自动驾驶中，许多研究将基于 RNN 的动力学与空间网格耦合以指导规划。例如，DriveDreamer [wang2024drivedreamer] 与 GenAD [zheng2024genad] 在网格或实例中心词元上采用基于 GRU 的动力学，以预测运动并解码轨迹。相比之下，DriveWorld [min2024driveworld] 与 Raw2Drive [yang2025raw2drive] 在 BEV 词元上实例化 RSSM 动力学。DriveWorld 以词元与动作为条件进行联合预测，而 Raw2Drive 采用双流设计进行时空学习。

许多研究聚焦于自回归预测未来 3D 占用（occupancy）表示，以支持自动驾驶的运动规划。一支路线将场景离散化为占用词元用于序列预测，例如 OccWorld [zheng2024occworld] 与 RenderWorld [yan2025renderworld]。另一支路线直接预测体积特征或嵌入，如 Drive-OccWorld [yang2025driving] 与 PreWorld [li2025semi]。自监督变体则从当前线索预测未来表示。例如，LAW [li2025enhancing] 以当前表示与轨迹为条件，SSR [li2025navigation] 将场景压缩为稀疏 BEV 词元以获得未来 BEV 特征，NeMo [huang2024neural] 将多帧图像体素化并预测占用，以支持基于模仿的规划。在这些表示的基础上，FASTopoWM [yang2025fastopowm] 采用统一解码器对齐来自车辆位姿的快、慢系统，从而实现车道拓扑推理；WoTE [li2025end] 在 BEV 中模拟候选轨迹，并用奖励模型从中选择。扩展这一范式，OccLLaMA [wei2024occllama] 将占用、动作与文本统一到单一词元词表中，并用 LLaMA 进行下一词元预测、规划与问答。

除自动驾驶之外，类似的表述也被扩展到更广的机器人领域。WMNav [nie2025wmnav] 借助 VLM 维护好奇心驱动的价值图，并采用分阶段决策实现零样本、对象驱动的导航。RoboOccWorld [zhang2025occupancy] 面向室内机器人，用位姿条件的自回归 Transformer 预测细粒度 3D 占用，从而支持探索与决策。为实现高保真动力学，EnerVerse [huang2025enerverse] 应用带稀疏记忆机制的块级自回归视频扩散以产生 4D 隐动力学，并集成 4DGS 以缓解机器人执行中的 S2R 差距。对于操作任务，ParticleFormer [huang2025particleformer] 用基于 Transformer 的粒子化动力学模型预测未来点云，从而稳健处理多物体与多材质交互。将这种点流视角进一步扩展，PointWorld [huang2026pointworld] 将场景状态与机器人动作统一为 3D 点流，用点云 Transformer 骨干从 RGB-D 观测预测动作条件的全场景位移，用于基于模型预测控制（MPC）的真实世界操作。在表示层面，DINO-WM [zhou2025dino] 在 DINOv2 特征空间中学习动力学，并预测未来状态以支持零样本规划。

分解式渲染表示（Decomposed Rendering Representation）。该范式用 NeRF 与 3DGS 等显式可渲染基元表示场景，通过更新这些基元来模拟动力学并渲染未来观测。它提供视图一致的预测、对象级组合性，以及与物理先验和数字孪生的无缝集成，从而支持长时域 rollout。

在 3DGS 基础上，GAF [chai2025gaf] 为泼溅增加可学习的运动属性以预测未来状态，并用扩散细化初始动作。ManiGaussian [lu2024manigaussian] 预测逐点变化，以在当前状态与动作下生成用于操作的未来高斯场景；ManiGaussian++ [yu2025manigaussian++] 增加了分层的领导者—跟随者设计，配合面向任务的泼溅来建模多体与双臂技能中的基元形变。在仿真与数字孪生耦合方面，DreMa [barcellona2025dream] 将高斯泼溅与物理模拟器集成，构建用于模仿学习数据合成的孪生体；Abou-Chakra 等 [abou2025physically] 引入了双重高斯—粒子表示，其中高斯点附着于由视觉损失力驱动的粒子；DexSim2Real2 [jiang2025dexsim2real] 用生成模型为铰接物体构建孪生体，并用基于采样的规划实现精确操作；PIN-WM [li2025pin] 将 3DGS 与可微物理结合，从有限观测估计物理参数，并生成数字表亲用于零样本 S2R 策略学习；PWTF [ning2025prompting] 构建交互式孪生体，模拟候选动作的结果，并用 VLM 评估与选择。在表示层面，DTT [xu2025delta] 采用三平面表示与多尺度 Transformer 自回归捕捉增量变化，形成一个用于预测与规划的 4D 世界模型。

#### III-A2 全局差分预测

词元特征序列（Token Feature Sequence）。紧凑的全局隐向量表示丢弃了细粒度时空细节，因此很少用于全局预测。相比之下，词元特征序列并行预测未来序列，在减少误差累积的同时支持多模态多样性。

在表示方面，TOKEN [tian2025tokenize] 将场景词元化为对象级词元，使世界表示与推理对齐，并借助 LLM 为长尾场景预测完整未来轨迹。GeoDrive [chen2025geodrive] 提取 3D 表示，渲染轨迹条件视图，并编辑车辆位置以引导 DiT 产生可编辑的生成结果。对于控制，FLARE [zheng2025flare] 将扩散策略与隐未来表示对齐，避免像素空间视频生成，并能从无动作视频中有效学习。在相关方向上，LaDi-WM [huang2025ladi] 在与视觉基础模型对齐的隐空间中通过交互式扩散预测未来状态，整合几何与语义特征，同时迭代细化扩散策略以提升性能与泛化。Cosmos Policy [kim2026cosmos] 将 Cosmos-Predict2 适配为统一的视觉运动策略，把本体感觉、动作块、未来观测与价值作为隐帧注入，使单一视频扩散模型可同时充当策略、世界模型与价值函数，用于基于模型的规划。villa-X [chen2025villa] 与 VidMan [wen2024vidman] 都将基于扩散的模型与 IDM 耦合用于控制。villa-X 推断隐动作，将其与以自车为中心的前向动力学对齐，并通过联合扩散进行映射；VidMan 则用自注意力适配器将预训练视频扩散模型适配为 IDM，以实现精确的动作预测。

空间隐网格（Spatial Latent Grid）。空间网格模型从自车稳定的视图并行预测 BEV 或体素图，在保留局部性与不确定性的同时，产生可直接供规划器使用的地图以支持快速控制。

基于扩散的世界模型常用于并行生成。EmbodiedDreamer [wang2025embodiedreamer] 将可微物理与视频扩散耦合，渲染出照片级真实且物理一致的未来。TesserAct [zhen2025tesseract] 通过联合生成 RGB、深度与法线视频重建 4D 时空一致场景，用于基于 IDM 的动作学习。DFIT-OccWorld [zhang2024efficient] 将预测重构为解耦的体素变形，并采用图像辅助的单阶段训练，以实现可靠且高效的动态场景建模。对于指令条件控制，RoboDreamer [zhou2024robodreamer] 将指令分解为引导视频扩散的低层基元，在训练分布之外合成新颖的组合场景，同时通过 IDM 锚定执行；ManipDreamer [li2025manipdreamer] 以动作树先验连同深度与语义引导扩展该设计，提升指令遵循与时序一致性。

在规划方面，3DFlowAction [zhi20253dflowaction] 采用预训练的 3D 光流世界模型，将未来运动视为统一的动作线索，通过闭环优化实现无标签、跨机器人的操作。Imagine-2-Drive [garg2025imagine] 将视频扩散与多模态扩散策略集成，以加速策略学习。Drive-WM [wang2024driving] 使用多视图扩散与基于图像的奖励来选择更安全的轨迹，而 World4Drive [zheng2025world4drive] 利用基于视觉的先验构建意图感知的世界模型，支持自监督的多意图想象。COMBO [zhang2025combo] 用扩散组合多智能体动作，借助 VLM 推断目的，并整合树搜索进行在线协作规划。

### III-B 通用世界模型

#### III-B1 序列仿真与推断

词元特征序列（Token Feature Sequence）。通用模型预训练与任务无关的动力学，以捕捉环境物理并生成未来场景，优先考虑可迁移性而非特定任务。

一些通用世界模型越来越多地在无标签视频上预训练，并使用词元化隐空间来实现稳健的预测与生成。iVideoGPT [wu2024ivideogpt] 在大规模交互视频上预训练，用于无动作预测，随后适配到下游控制。Genie [bruce2024genie] 学习离散隐动作与时空词元，通过自回归动力学实现用户可控的交互环境。RoboScape [shang2025roboscape] 联合学习视频生成与时序深度和关键点动力学，以提升物理真实感。PACT [bonatti2023pact] 对多模态感知与动作进行词元化，并训练因果 Transformer 以获得可用于多样任务的统一表示；DINO-world [baldassarre2025back] 通过从大规模无标签视频语料预测 DINOv2 特征的时间演化来学习可泛化的动力学。在语言先验的基础上，EVA [chi2025empowering] 引入了生成反思（Reflection-of-Generation，RoG）策略，用 VLM 进行迭代的自我修正，从而增强长时域预测。沿着同一思路，Owl-1 [huang2024owl] 用 VLM 以当前状态与已生成片段为条件预测世界动力学，显式引导后续片段并实现连贯的长时域视频合成；World4Omni [chen2025world4omni] 采用反思式世界模型，由 VLM 细化来自图像生成器的子目标图像，并将这些图像与预训练模块集成，用于零样本机器人操作。

近期工作将视频扩散模型适配为可控的世界模型，以自回归方式想象未来场景。AdaWorld [gao2025adaworld] 引入动作感知的预训练方案，从相邻帧提取自监督隐动作以条件化扩散，从而以极少的交互实现高效迁移。Vid2World [huang2025vid2world] 通过因果化与因果动作引导机制，将预训练视频扩散模型适配为自回归的交互式世界模型。GenAD [yang2024generalized] 采用两阶段策略将扩散适配为以文本与动作为条件的通用视频预测模型，支持大规模驾驶仿真与规划。Pandora [xiang2024pandora] 用指令微调的 LLM 自回归驱动一个独立的视频扩散生成器，实现显式、目标导向的控制；Yume [mao2025yume] 将相机运动量化为文本词元以引导掩码 Video DiT，从而实现动态 3D 探索世界的自回归合成。

为保持几何保真度与长时域稳定性，近期方法在基于扩散的世界模型中将显式的 3D 先验与时序一致性模块耦合。在几何层面，Geometry Forcing [wu2025geometry] 将隐特征与几何基础模型对齐以注入显式 3D 先验，从而提升几何一致性；DeepVerse [chen2025deepverse] 整合视觉与几何预测目标，并引入几何感知记忆以维持一致的长时域生成。为提升时序稳定性，VRAG [chen2025learning] 提出了视频检索增强生成（Video Retrieval-Augmented Generation，RAG）框架，它以全局状态为条件检索历史帧，以稳定自回归 rollout；StateSpaceDiffuser [savov2025statespacediffuser] 将 Mamba 与扩散结合，缓解短上下文窗口下的长期记忆丢失与内容漂移；InfinityDrive [guo2024infinitydrive] 在 DiT 中注入记忆并采用自适应损失，产生分钟级的驾驶视频，具备高保真度、时序一致性与多样内容。作为补充设计，LongDWM [wang2025longdwm] 通过蒸馏缓解长时域视频生成中的误差累积——其中细粒度的 DiT 学习连续运动以指导粗粒度模型；而 MiLA [wang2025mila] 采用由粗到细的策略，预测稀疏锚帧并在插值过程中对其进行细化，以提升时序一致性与长期保真度。最后，在动力学与条件化方面，Orbis [mousakhan2025orbis] 采用连续空间流匹配表述，在长时域 rollout 中表现出比离散词元方案更强的鲁棒性；DriVerse [li2025driverse] 利用多模态轨迹提示与隐运动对齐，从单张图像与导航轨迹合成长期驾驶视频。

序列世界模型越来越多地充当学习到的模拟器，提供动作条件的 rollout 用于策略评估与训练。WorldGym [quevedo2025worldgym] 与 WorldEval [li2025worldeval] 生成动作条件的 rollout，并使用基于 VLM 的评论器进行评估，WorldEval 还进一步利用隐动作表示驱动基于 DiT 的合成器。RLVR-World [wu2025rlvr] 用可验证奖励强化学习（RL with Verifiable Rewards，RLVR）微调世界模型，用显式指标缩小预训练目标与任务目标之间的差距。对于安全风险预测，Guan 等 [guan2025world] 提出了一个自动驾驶事故预测框架，用融入领域知识的世界模型增强数据，并利用图卷积与时序卷积增强时空推理。

在扩散之外，序列模型拓宽了长程一致性的能力。Po 等 [po2025long] 将用于长期记忆的块状状态空间模型与用于短期连贯的局部注意力整合，实现具有持续记忆与一致动力学的视频生成。S2-SSM [petri2025learning] 用 Mamba 层建模对象槽的独立演化，并用稀疏正则化的交叉注意力机制捕捉它们之间的因果交互，从而实现对环境的因果推理。

空间隐网格（Spatial Latent Grid）。以自监督时空目标预训练几何对齐的空间图，空间隐网格范式保留局部性，并支持高效的 rollout、多模态融合与可迁移的规划就绪地图。

在这一范式基础上，结构化网格与物理信息方法编码几何与动力学，以实现可控的 rollout。PhyDNet [guen2020disentangling] 将以偏微分方程表示的物理先验与视觉因素解耦，改进预测效果。ViDAR [Yang2024visual] 通过点云预测的预训练任务与一个隐渲染算子，统一语义、几何与动力学，为下游自动驾驶任务提供可扩展的基础。FOLIAGE [liu2025foliage] 用增长图网络（Accretive Graph Network）与基于 Transformer 的预测器建模动力学，并在仿真数据上执行 rollout。作为对上述网格与物理路线的补充，MindJourney [yang2025mindjourney] 将 VLM 与可控世界模型耦合，沿规划的相机轨迹渲染以自车为中心的 rollout，从而实现多视图推理。

在基于网格的表示之上，基于扩散的预测已成为稳定长时域生成的主流。在网格中心的预测器中，DOME [gu2024dome] 将观测编码到连续隐空间，并应用时空 DiT 进行场景预测；Copilot4D [zhang2024copilot4d] 对点云进行词元化，并将时空 Transformer 与离散扩散结合，以提升保真度与连贯性；LidarDM [zyrianov2025lidardm] 生成布局条件的静态场景，将其与动态对象组合，并集成 LiDAR 仿真以产生可控视频。对于长视频生成，Vista [gao2024vista] 采用两阶段大规模训练方案，生成可控、高保真的驾驶视频；Delphi [ma2024unleashing] 通过共享噪声与特征对齐实现长时域多视图一致性，并采用失败驱动的框架合成定向数据以改进规划。为增强长时域稳定性，GEM [hassan2025gem] 通过大规模训练以及对运动、动力学与姿态的细粒度控制，实现可控的自车视角生成；Zhou 等 [zhou2025learning] 维护持久的 RGB-D 3D 记忆图以指导后续帧；STAGE [wang2025stage] 引入了基于多阶段训练的分层时序特征迁移。

分解式渲染表示（Decomposed Rendering Representation）。场景被分解为显式基元，以在长时域上合成视图一致、可模拟的轨迹。在该范式中，GaussianWorld [zuo2025gaussianworld] 将场景演化建模为自车运动、对象动力学与新观测区域三部分，并迭代更新 3D 高斯基元，以实现准确且高效的动态感知。InfiniCube [lu2025infinicube] 引入混合流水线，结合体素生成、视频合成与动态高斯重建，以高清地图（HD map）、边界框与文本为条件，实现大规模动态 3D 驾驶场景。作为补充，Wu 等 [wu2025video] 为视频世界模型增加了基于重建几何的长期空间记忆与情节记忆，二者共同条件化序列生成以实现长程一致性。

#### III-B2 全局差分预测

词元特征序列（Token Feature Sequence）。对于通用世界模型，词元化的特征序列通过掩码建模与生成式建模支持全局预测，使并行的长时域 rollout 具备全局约束与多模态条件。

在联合嵌入预测架构（Joint-Embedding Predictive Architecture，JEPA）[LeCun2022Path] 中，V-JEPA [bardes2024revisiting] 将该架构扩展到视频，预测被遮挡时空区域的隐特征，无需像素重建或对比学习即可学习外观与运动的可泛化表示。在此基础上，V-JEPA 2 [assran2025v] 以更大的模型将预训练扩展到大规模互联网视频，并纳入有限的机器人交互数据进行后训练，从而迁移到机器人规划。V-JEPA 2.1 [mur2026v] 进一步修改这一方案，对可见与掩码词元均做稠密预测，采用深度自监督与图像—视频词元化器，在提升局部时空特征的同时保持全局预测与具身规划能力。DINO-Foresight [karypidis2026dino] 类似地将预训练的 DINO/VFM 特征视为语义隐词元，用掩码特征 Transformer 预测未来驾驶场景表示，这些表示可由分割、深度与表面法线头解码。AD-L-JEPA [zhu2025ad] 将 JEPA 适配到 BEV LiDAR，以自监督方式预测掩码嵌入。在 JEPA 式预测之外，WorldDreamer [wang2024worlddreamer] 将世界建模视为掩码视觉序列预测，以学习物理与运动，用于多样的视频生成与编辑；而 MaskGWM [ni2025maskgwm] 将扩散与掩码特征重建、双分支掩码策略结合，提升长时域一致性与泛化。

与此同时，基于扩散的方法已成为全局差分建模的核心。Sora [brooks2024video] 将视频表示为统一的时空块，并用 DiT 大规模生成长期连贯序列。将该路线扩展到物理 AI，Cosmos 3 [agarwal2026cosmos] 在混合 Transformer 架构中统一语言、图像、视频、音频与动作序列，将全模态世界模型定位为用于理解、生成、仿真与动作预测的通用骨干。ForeDiff [zhang2025consistent] 通过添加确定性预测流并用预训练预测器引导生成，将条件化与去噪解耦，提升准确性与一致性。对于领域特定的合成，AirScape [zhao2025airscape] 引入航拍视频意图数据集，应用监督微调以增强可控性，并借助 VLM 施加时空约束；MarsGen [li2025martian] 用几何基础模型从 NASA 稀疏的漫游车立体影像构建多模态火星数据集，然后训练可控生成器，产生视觉真实、几何一致的火星视频。在临床引导中，EchoWorld [yue2025echoworld] 提出用于超声心动图探头控制的运动感知世界模型，它在区域与运动结果预测上进行预训练，并微调注意力以融合视觉与运动线索，实现精确引导。

空间隐网格（Spatial Latent Grid）。空间网格模型并行预测体素网格，并将多视图视觉特征融合为统一地图，从而学习一个通用世界模型。

近期工作趋向于统一的场景理解与未来预测。UniFuture [liang2025seeing] 将双重隐共享与多尺度隐交互结合，联合建模未来驾驶场景中的外观与深度；HERMES [zhou2025hermes] 将多视图 BEV 特征整合进 LLM，并用世界查询在单一框架内连接场景理解与未来预测。BEVWorld [zhang2024bevworld] 通过统一的词元化器将图像与 LiDAR 映射到紧凑的 BEV 隐空间，并应用隐 BEV 扩散模型进行同步的多模态预测。网格与占用预测方面的进展包括：Khurana 等 [khurana2022differentiable, khurana2023point] 通过带代理重构的可微光线投射实现传感器无关的运动学习；Mersch 等 [mersch2022self] 用 LiDAR 到距离图像的 3D 时空卷积。Cam4DOcc [ma2024cam4docc] 建立了首个仅视觉的基准与端到端 3D CNN 基线；Liu 等 [liu2025towards] 通过高比例压缩与隐流匹配增强跨任务迁移。

在生成方面，词元化的 4D 表示使可控场景合成成为可能。OccSora [wang2024occsora] 用 4D 词元化器获得紧凑表示，用于轨迹条件扩散；DynamicCity [bian2025dynamiccity] 用 VAE 将 4D 占用编码为 HexPlanes 表示，并采用条件 DiT 实现高保真、可控的动力学。保真度与一致性通过以下方式得到提升：在 COME [shi2025come] 中将自车运动与场景演化解耦，在 DrivePhysica [yang2024physical] 中引入物理信息约束，在 Liu 等 [liu2025geometry] 中进行跨视图点图对齐，以及在 PosePilot [jin2025posepilot] 中采用基于光度形变的监督。对于可控条件化，DriveDreamer 2 [zhao2025drivedreamer] 将提示翻译为智能体轨迹与高清地图，以支持可定制的视频生成；EOT-WM [zhu2025other] 将自车与周围轨迹编码为轨迹视频，以实现轨迹一致的合成；ORV [yang2025orv] 用 4D 语义占用序列指导带 S2R 迁移的动作条件视频。AETHER [team2025aether] 在合成的 4D 数据上训练，统一了动态 4D 重建、动作条件视频预测与基于视觉的规划，并实现对真实场景的零样本泛化。

分解式渲染表示（Decomposed Rendering Representation）。该范式通过将显式 3D 结构与视频生成先验结合来执行全局预测。

一个趋势是将视频生成与高斯泼溅结合。DriveDreamer4D [zhao2025drivedreamer4d] 利用变道等复杂驾驶轨迹引导视频合成并优化 4DGS 模型，从而从新视角提升重建保真度与时空连贯性。ReconDreamer [ni2025recondreamer] 引入在线修复模块以及渐进式数据复用，以修正高斯渲染视图中的伪影，并实现大规模轨迹的可靠重建。MagicDrive3D [gao2024magicdrive3d] 以 BEV 地图、3D 框与文本为条件生成多视图街道场景，并通过容错的高斯泼溅将输出进一步转换为完整 3D 环境。相比之下，隐场方法用连续神经表示替代高斯泼溅。UnO [agro2024uno] 利用未来点云学习 NeRF 式的 4D 占用场，从而支持无标注预测，并在点云预测中取得优于监督基线的强迁移性能。

总之，决策耦合规定了世界模型与特定控制目标绑定的强度，时序建模决定预测如何随时间展开，空间表示决定几何细节与局部性的水平。这些轴的不同组合会带来具有特征性的权衡：带全局隐向量的决策耦合 RSSM 式模型利于样本效率与快速 rollout，但代价是视觉细节；基于词元的模拟器，尤其是在全局预测之下，提升了保真度与语义丰富度，但带来更高的计算与数据需求；基于网格与分解式渲染的模型提供强的几何与多视图一致性，但在严格的时延与内存预算下仍难以部署。

---

## 📚 IV 数据资源与指标 (Data Resources & Metrics)

具身智能（Embodied AI）中的世界模型（world model）需要应对涵盖操作（manipulation）、导航（navigation）与自动驾驶（autonomous driving）的多样任务，因而需要异构资源与严谨的评测体系。据此，我们在 §IV-A 中介绍数据资源，在 §IV-B 中介绍指标，聚焦于最广泛采用的平台与评测度量，作为跨领域评估的统一基础。

### IV-A 数据资源

为满足具身 AI 的多样化需求，我们将数据资源划分为四类：仿真平台（Simulation Platforms）、交互基准（Interactive Benchmarks）、离线数据集（Offline Datasets）与真机机器人平台（Real-world Robot Platforms），详见以下各小节。表 III 对上述资源作了全面梳理。

> 表 III：具身世界模型训练与评测数据资源总览（仿真平台 / 交互基准 / 离线数据集 / 真机平台四类，逐行数据见原文 Table III，此处从略。）

#### IV-A1 仿真平台 (Simulation Platforms)

仿真平台为世界模型的训练与评测提供可控、可扩展的虚拟环境。

- MuJoCo [todorov2012mujoco] 是一款可定制的物理引擎，因其能高效模拟机器人学与控制研究中的关节体系统与接触动力学而广受采用。
- NVIDIA Isaac 是一套端到端、GPU 加速的仿真技术栈，由 Isaac Sim、Isaac Gym [makoviychuk2021isaac] 与 Isaac Lab [mittal2023orbit] 组成，具备照片级真实感渲染与大规模强化学习（RL）能力。
- CARLA [dosovitskiy2017carla] 是基于 Unreal Engine 的开源城市自动驾驶仿真器，提供真实感渲染、多种传感器以及闭环评测协议。
- Habitat [savva2019habitat] 是面向具身 AI 的高性能仿真器，专长于照片级真实感的三维室内导航。

#### IV-A2 交互基准 (Interactive Benchmarks)

交互基准提供标准化的任务套件与协议，用于对世界模型进行可复现的闭环评测。

- DeepMind Control（DMC）[tassa2018deepmind] 是基于 MuJoCo 的标准控制任务套件，为比较从状态观测或像素观测中学习的智能体提供了一致的基准。
- Atari [bellemare2013arcade] 是一套基于像素、动作为离散取值的游戏，用于评估智能体表现。其中 Atari100k [kaiser2020model] 专门通过将交互限制在 10 万步内来考察样本效率。
- Meta-World [yu2020meta] 是多任务与元强化学习（meta-RL）基准，包含 50 个多样的机器人操作任务，在 MuJoCo 中以 Sawyer 机械臂在标准化评测协议下执行。
- RLBench [james2020rlbench] 提供 100 个仿真桌面操作任务，奖励稀疏、观测丰富且多模态，旨在检验复杂技能与快速适应能力。
- LIBERO [liu2023libero] 是面向终身机器人操作的基准，提供 130 个程序化生成的任务与人类示范，用于评估样本高效学习与持续学习。
- nuPlan [caesar2021nuplan] 是自动驾驶规划基准，使用轻量级闭环仿真器与超过 1 500 h 的真实驾驶日志来评估长时程性能。

#### IV-A3 离线数据集 (Offline Datasets)

离线数据集是预先采集的大规模轨迹集合，免除交互式 rollout（回合推演），为可复现评测与世界模型的数据高效预训练提供基础。

- RT-1 [brohan2022rt] 是用于机器人学习的真实世界数据集，历时 17 个月、由 13 台 Everyday Robots 移动操作机器人采集，包含 130 000 条示范、覆盖 700 余个任务，将语言指令与图像观测同机械臂和移动底盘的离散化 11 自由度动作配对。
- Open X-Embodiment（OXE）[o2024open] 是汇聚 21 家机构 60 个来源的语料库，涵盖 22 种机器人本体、527 项技能、逾百万条轨迹，并以统一格式支持跨本体训练。在 OXE 上训练的模型展现出超越单机器人基线的强迁移能力，凸显了跨平台数据共享的有效性。
- Habitat-Matterport 3D（HM3D）[ramakrishnan2021habitatmatterport] 是包含 1 000 个室内重建场景的大规模数据集，可导航面积达 112 500 m²，显著扩展了具身 AI 仿真的范围与多样性；其面向 Habitat 平台发布，并提供无缝使用所需的元数据与资源。
- nuScenes [caesar2020nuscenes] 是大规模多模态驾驶数据集，配备 360 度传感器组，包括六部相机、五部雷达、一部 LiDAR 与 GPS/IMU。它包含在波士顿与新加坡采集的 1 000 个 20 秒场景，附有 23 个类别的密集三维标注与 HDMap，为多模态融合与长时程预测提供了核心基准。
- Waymo [sun2020scalability] 是多模态自动驾驶基准，包含来自旧金山、凤凰城与山景城的 1 150 个 20 秒场景、采样率 10 Hz，配有五部 LiDAR 与五部相机，以及约 1 200 万个三维与二维标注，是建模交通动态的大规模资源。
- Occ3D [tian2023occ3d] 定义由环视图像进行三维占用预测（3D occupancy prediction）的任务，提供区分自由、占用与未观测状态的体素标签。Occ3D-nuScenes 以 0.4 m 分辨率包含约 40 000 帧，Occ3D-Waymo 则以 0.05 m 分辨率提供约 200 000 帧。这种体素级监督使整体场景理解超越了边界框层面。
- Something-Something v2（SSv2）[goyal2017something] 是用于细粒度动作理解的视频数据集，包含 174 个类别的 220 847 个片段，由众包工作者按文本提示（例如 "Putting something into something"）采集，划分为 168 913 条训练、24 777 条验证与 27 157 条测试视频。
- OpenDV [yang2024generalized] 是迄今规模最大的自动驾驶视频—文本数据集，由 GenAD 提出，支持视频预测与世界模型预训练。它包含来自 YouTube 与七个公开数据集的 2 059 小时、6 510 万帧，覆盖 40 多个国家与 244 座城市，并提供指令与上下文标注，以支持语言条件与动作条件的预测和规划。
- VideoMix22M [assran2025v] 是随 V-JEPA 2 一同提出、用于自监督预训练的大规模数据集，规模从 200 万扩展到 2 200 万个样本，取材于 YT-Temporal-1B [zellers2022merlot]、HowTo100M [miech2019howto100m]、Kinetics [carreira2019short]、SSv2 与 ImageNet [deng2009imagenet]。其中体量最大的来源 YT-Temporal-1B 经基于检索的过滤以抑制噪声，而 ImageNet 图像则被转换为静态视频片段以保持一致性。
- VisionMix163M [mur2026v] 在 VideoMix 式自监督预训练的基础上扩展，融合 SSv2、Kinetics、HowTo100M、YT-Temporal-1B 与 LVD-142M 图像数据。它用以规模大得多的精选图像来源替代 V-JEPA 2 中使用的 ImageNet 子集，并将视频采样向运动丰富的内容倾斜，以支撑稠密且时序一致的视觉特征。

#### IV-A4 真机机器人平台 (Real-world Robot Platforms)

真机机器人平台提供可供交互的物理本体，从而支持闭环评测、高保真数据采集以及真实世界约束下的 S2R（仿真到真实，sim-to-real）验证。

- Franka Emika [haddadin2022franka] 是配备关节力矩传感器的 7 自由度协作机械臂，可实现精确的力控制。通过其控制接口，它支持面向富接触任务的 1 kHz 力矩控制，且其 ROS 集成使其成为通用平台。
- Unitree Go1 [unitree_go1_web] 是性价比高、应用广泛的四足机器人，配备全景深度感知套件、1.5 TFLOPS 的机载算力与 4.7 m/s 的最高速度，已成为运动控制与具身 AI 研究的标准平台。
- Unitree G1 [unitree_g1_web] 是面向研究的紧凑型人形机器人，最多 43 个自由度，膝关节力矩达 120 N·m，并集成三维 LiDAR 与深度相机。凭借多模态感知、机载算力、ROS 支持与可换电池，这一低成本平台为训练与评测具身世界模型提供了实用的真机试验平台。

### IV-B 指标 (Metrics)

指标用于评估世界模型捕捉动态、泛化到未见场景以及随资源增加而扩展的能力。我们将其组织为三个抽象层级：§IV-B1 像素生成质量（Pixel Generation Quality）、§IV-B2 状态级理解（State-level Understanding）与 §IV-B3 任务表现（Task Performance），对应从低层信号逼真度到高层目标达成的递进。

#### IV-B1 像素生成质量 (Pixel Generation Quality)

在最基础的层面上，世界模型的评测关注其重建感知输入与生成真实序列的能力。相关指标考察图像逼真度、时序一致性与感知相似度，为模型在多大程度上捕捉原始环境动态提供定量度量。

**Fréchet 初始距离（FID）[heusel2017gans]。** FID 是评估生成图像真实性与多样性的指标。它在 ImageNet 预训练的 Inception-v3 [szegedy2016rethinking] 的特征空间中比较真实图像分布与生成图像分布，将嵌入建模为均值 μ_x、μ_y 与协方差 Σ_x、Σ_y 的高斯分布。其定义为

FID(x, y) = ‖μ_x − μ_y‖₂² + Tr(Σ_x + Σ_y − 2(Σ_xΣ_y)^{1/2})，(6)

其中 Tr 表示矩阵的迹。FID 越低，表示真实分布与生成分布越接近。该指标通过比较一阶与二阶矩，同时惩罚逼真度损失（均值偏移）与模式坍缩（协方差失配），从而给出生成性能的整体度量。

**Fréchet 视频距离（FVD）[unterthiner2018towards]。** FVD 将 FID 扩展到视频，同时评估逐帧质量与时序一致性。它以在 Kinetics-400 [kay2017kinetics] 上预训练的 I3D [carreira2017quo] 取代基于图像的 Inception 网络，并在运动感知特征上沿用式 (6) 的同一 Fréchet 距离，从而给出整体的视频质量分数。取值越低，说明分布在外观与动态两方面越接近，同时会惩罚不自然运动或闪烁等时序伪影。

**结构相似性指数（SSIM）[wang2004image]。** SSIM 是图像质量的感知指标，比较生成图像与其参考图像在亮度、对比度与结构上的相似性。对于两个图像块 x 与 y，设其均值为 μ_x、μ_y，方差为 Σ_x²、Σ_y²，协方差为 Σ_xy，则 SSIM 定义为

SSIM(x, y) = [(2μ_xμ_y + C₁)(2Σ_xy + C₂)] / [(μ_x² + μ_y² + C₁)(Σ_x² + Σ_y² + C₂)]，(7)

其中 C₁、C₂ 是为避免除以零而设的稳定常数。最终分数由滑动窗口上的 SSIM 取平均得到，取值越接近 1 表示相似度越高。

**峰值信噪比（PSNR）[hore2010image]。** PSNR 度量重建结果与其参考之间的逐像素失真。设 N 个像素上的均方误差（MSE）为

MSE = (1/N) Σ_{i=1}^{N} (x_i − y_i)²，(8)

并令 MAX 表示可能的最大像素值（例如 RGB 图像为 255，归一化图像为 1），则

PSNR(x, y) = 10 · log₁₀(MAX² / MSE)，(9)

PSNR 越高，表示失真越小、逼真度越高。

**学习感知图像块相似度（LPIPS）[zhang2018unreasonable]。** LPIPS 通过比较预训练网络提取的特征，与人类判断具有良好相关性。设 f̂^l_x 与 f̂^l_y 表示输入 x 与 y 在第 l 层经单位归一化的激活，w_l 为逐通道权重，则 LPIPS 定义为

LPIPS(x, y) = Σ_l [1/(H_l W_l)] Σ_{h,w} ‖w_l ⊙ (f̂^l_{h,w,x} − f̂^l_{h,w,y})‖₂²，(10)

其中 H_l、W_l 为该层特征图的高与宽，⊙ 表示逐元素相乘。LPIPS 越低表示相似度越高；相较基于像素的指标，它能提供更好的逼真度度量并对失真更鲁棒。

**VBench [huang2024vbench]。** VBench 是面向视频生成的综合基准，从 16 个维度评估性能，这些维度归为两类：视频质量（如主体一致性、运动平滑度）与视频—条件一致性（如物体类别、人物动作）。它提供精心整理的提示词套件与大规模人类偏好标注，以确保与人类感知高度对齐，从而可对模型能力与局限进行细粒度评测。

#### IV-B2 状态级理解 (State-level Understanding)

除像素逼真度之外，状态级理解考察模型能否捕捉物体、布局与语义，并预测其演化。相关指标涵盖语义、BEV（鸟瞰图）与三维的分割、检测、占用、几何与轨迹精度，强调外观之外的结构性理解。

**平均交并比（mIoU）。** mIoU 通过在所有类别上对交并比（IoU）取平均来评估语义分割。对于类别 c，

IoU = TP / (TP + FP + FN)，(11)

其中 TP、FP、FN 分别表示真阳性、假阳性与假阴性。IoU 量化与真值的重叠程度，同时惩罚分割错误。数据集级得分为

mIoU = (1/|C|) Σ_{c∈C} IoU_c，(12)

其中 C 为类别集合。mIoU 越高，表示语义场景理解越精确。

**平均精度均值（mAP）。** mAP 通过对各类别的平均精度（AP）取平均来评估检测与实例分割。对于类别 c 在 IoU 阈值 τ 下，预测按置信度排序，并在 IoU ≥ τ 时与真值一一匹配，未匹配的预测计为 FP，未匹配的真值计为 FN。精确率与召回率为

Precision = TP / (TP + FP)，Recall = TP / (TP + FN)，(13)

设 P_{c,τ}(r) 表示经单调插值得到的精确率—召回率包络，则类别 c 在阈值 τ 下的 AP 为

AP_{c,τ} = ∫₀¹ P_{c,τ}(r) dr，(14)

mAP 则在类别与阈值集合 T 上对 AP 取平均：

mAP = (1/|C|) Σ_{c∈C} [ (1/|T|) Σ_{τ∈T} AP_{c,τ} ]，(15)

mAP 越高，表示实例识别更好、定位更准、置信度估计更校准。

**位移误差（Displacement Error）。** 位移误差指标通过度量关键点、物体中心与轨迹路点的空间精度来评估状态级理解。L2 轨迹误差计算预测路点与真值路点之间的欧氏距离。常见变体包括平均位移误差（ADE），计算平均位移；以及最终位移误差（FDE），度量最后一步的位移。取值越低表示定位越准确。

**倒角距离（Chamfer Distance, CD）[fan2017point]。** CD 通过对两个集合的最近邻距离平方求和，量化预测 S₁ 与真值 S₂ 之间的几何相似性：

CD(S₁, S₂) = Σ_{x∈S₁} min_{y∈S₂} ‖x − y‖₂² + Σ_{y∈S₂} min_{x∈S₁} ‖x − y‖₂²，(16)

不同于像素级指标，CD 能捕捉表面、占用、BEV 与三维结构；其可微性使其既可作为训练损失，也可作为与 IoU 互补的评测指标。

#### IV-B3 任务表现 (Task Performance)

归根结底，世界模型的价值在于支撑有效的决策，任务级指标即在具身场景下考察模型在安全与效率约束下达成目标的程度。

**成功率（Success Rate, SR）。** SR 以满足预设成功条件的评测回合占比来量化性能。在导航与操作中，该条件通常是二值的，例如到达目标或正确放置物体。在自动驾驶中要求更严格，须在无碰撞、无重大违规的前提下完成路线。最终 SR 报告为所有测试回合二值结果的均值。

**样本效率（Sample Efficiency, SE）。** SE 量化达到目标性能所需的样本量。其评测方式包括固定预算的基准（如 Atari-100k）、数据—性能曲线，或在机器人学中用以达到给定成功率所需的示范数量。

**奖励（Reward）。** 在强化学习（RL）中，奖励是 t 时刻的信号 r_t。目标是最大化折扣回报 G_t = Σ_{k=0}^{∞} γ^k r_{t+k+1}，其中 γ 为折扣因子。结果以累计奖励或平均回报报告，通常进行归一化以便跨任务比较。

**碰撞（Collision）。** 安全性通过基于碰撞的指标来评估。主要度量是碰撞率，即至少发生一次碰撞的评测回合占比，在室内导航中较为常用。在自动驾驶中则采用按暴露量归一化的变体，例如每公里碰撞数或每小时碰撞数。

---

## 📊 V 性能对比 (Performance Comparison)

鉴于世界模型变体激增、评估指标异质，我们按任务目标组织比较，并依托标准化基准，以简洁的表格呈现各方法的优势与局限。

### V-A 像素生成

**nuScenes 上的生成（Generation on nuScenes）。** 驾驶视频生成被视为一项世界建模任务，即在固定长度的片段中合成合理的场景动态。典型协议生成短序列，并用 FID 评估外观保真度、用 FVD 评估时间一致性。在 nuScenes 验证集上进行公平比较时，近期方法已取得显著进展，如表 IV 所示。DrivePhysica 提供最佳的视觉保真度，而 MiLA 实现最强的时间连贯性，二者共同确立了新的最先进性能。

> 表 IV：nuScenes 视频生成性能对比（逐行数据见原文 Table IV，此处从略）。DrivePhysica FID 4.0 最低，MiLA FVD 14.9 最低（其 FID 为 4.1）；Vista 的 FID 为 6.9、FVD 为 89.4。

### V-B 场景理解

**Occ3D-nuScenes 上的 4D 占用预测（4D Occupancy Forecasting）。** 4D 占用预测被视为一项代表性的世界建模任务。给定 2 s 的过去 3D 占用（occupancy），模型预测随后 3 s 的场景动态。评估遵循 Occ3D-nuScenes 协议，报告 mIoU（平均交并比）与各预测时域的 IoU。如表 V 所总结，我们按输入模态、辅助监督（auxiliary supervision）以及自车轨迹（ego trajectory）的使用来比较方法，以揭示时空预测中的设计选择。使用占用输入的方法优于仅使用相机的变体，而加入辅助监督与 GT 自车轨迹进一步缓解了 2–3 s 处的性能衰减。在所有方法中，COME（使用 GT 自车轨迹）取得最佳的平均 mIoU 与各时域 IoU。

> 表 V：Occ3D-nuScenes 基准上的 4D 占用预测性能对比（逐行数据见原文 Table V，此处从略）。COME-O（GT 自车轨迹）平均 mIoU 34.23%、平均 IoU 44.13%，均为最佳；DOME-O 平均 mIoU 27.10%、平均 IoU 36.36%。

### V-C 控制任务

**DMC 上的评估（Evaluation on DMC）。** 多数研究探查世界模型学习控制相关动态的能力，通常采用以 64×64×3 观测为输入的像素级设置。主要指标是回合回报（Episode Return），定义为 1 000 步内的累积奖励，在 r_t ∈ [0,1] 下理论最大值为 1 000。为便于比较，表 VI 报告了步数预算，并按任务得分与任务数量汇总性能。结果表明数据效率有所提升，近期模型在远少得多的训练步数下即达到强性能。然而，不一致的评估协议与任务子集阻碍了对泛化性的公平评估，构建跨任务、模态与数据集的广泛可迁移模型仍是开放挑战。

> 表 VI：DMC 基准性能对比（逐行数据见原文 Table VI，此处从略）。Dreamer 平均 823（共 20 项任务），PlaNet 为 333/20；HRSSM 仅用 500k 步即达平均 938（3 项任务），DisWM 用 1M 步达 879/5。

**RLBench 上的评估。** RLBench 使用 7 自由度（7-DoF）仿真 Franka 机械臂评估操作任务，常被用来检验世界模型是否捕获任务相关动态并支持条件动作生成。主要指标是成功率（Success Rate），即在步数上限内达到目标的回合比例。如表 VII 所总结，各实现在回合预算、分辨率与模态上各不相同，使同类比较变得复杂。尽管存在这种异质性，仍可看出若干趋势。近期方法越来越多地利用多模态输入，并采用更强的骨干网络，如 3DGS 与 DiT。VidMan 在最广的任务集上取得较高的平均成功率，显示 IDM 是一个颇有前景的架构方向。

> 表 VII：RLBench 操作任务性能对比（逐行数据见原文 Table VII，此处从略）。VidMan 平均成功率 67%（共 18 项任务）为最高，TesserAct 为 63/10，ManiGaussian 为 45/10。

**nuScenes 上的规划（Planning on nuScenes）。** 开放环规划被视为 nuScenes 验证集上的一项世界建模任务，模型从有限历史预测自车运动。方法观测 2 s 的过去轨迹，并将未来 3 s 预测为 2D BEV 路点。评估报告多个时域的 L2 误差与碰撞率，表 VIII 按输入模态、辅助监督与指标设置汇总结果。在该共享协议下，出现了一个明显的权衡：UniAD+DriveWorld 借助大量辅助监督取得最低的 L2；而 SSR 在无额外监督的情况下，以有竞争力的 L2 取得最佳的碰撞率。基于相机的方法如今已超过使用特权占用（privileged occupancy）的模型，反映出端到端（E2E）规划日益成熟。

> 表 VIII：nuScenes 验证集开放环规划性能对比（逐行数据见原文 Table VIII，此处从略）。UniAD+DriveWorld 平均 L2 0.69 m 为最低；SSR 平均碰撞率 0.15% 为最低（其平均 L2 为 0.75 m）。

## 🚧 VI 挑战与趋势 (Challenges and Trends)

本节回顾具身 AI 中世界模型的开放挑战与新兴方向。我们按三个维度组织这些内容：§VI-A 数据与评估、§VI-B 计算效率、§VI-C 建模策略。

### VI-A 数据与评估

**挑战。** 从数据角度看，核心挑战在于现有语料的稀缺性与异质性。尽管具身 AI 涵盖导航、操作与自动驾驶等多样领域，统一的大规模数据集仍然缺失。这种碎片化限制了世界模型的能力，并显著阻碍其泛化，尤其当模型规模的增长快于可用的任务相关数据时。多智能体交互数据尤为不足，限制了社会感知与协作式世界模型的进展。

评估实践面临类似的局限。多数指标，如 FID 与 FVD，强调像素保真度，却忽视物理一致性、动态与因果性。结果，模型可能在外观层面的逼真度上表现出色，却产生物理上不合理或因果不一致的推演（rollouts）。现有基准（如 EWM-Bench [yue2025ewmbench]）开始引入更有结构的指标，但仍局限于特定任务，缺乏跨域标准；此外，视频模拟器（如 Sora 风格模型）的评估方式与具身控制器的评判方式之间仍存在差距。

**未来方向。** 诸如 OpenDV-2K [yang2024generalized]、VideoMix22M [assran2025v] 与 VisionMix163M [mur2026v] 等近期举措，凸显了对大规模预训练与更广模态覆盖日益增长的关注，但资源仍然碎片化且局限于特定领域。一个关键方向是构建统一、多模态、跨域的基准，将场景、动作与奖励耦合起来，并明确覆盖多智能体交互与安全关键事件。与此同时，评估协议应超越感知逼真度，转向评估物理一致性、因果推理与长时域误差累积的指标。若大型视频模型要成为下游控制的可靠基础，弥合以视频为中心的世界模拟器与具身动作基准之间的评估差距至关重要。

### VI-B 计算效率

**挑战。** 具身 AI 任务在计算效率方面面临显著挑战，实时场景中尤为突出。尽管 Transformer 与基于扩散的解码器取得了强性能，其高昂的推理成本与内存占用却与机载机器人平台的延迟和能耗约束相冲突。快速增长的模型规模与边缘设备相对有限的算力预算之间的失配，进一步加剧了这一矛盾。因此，许多实际系统仍依赖紧凑的循环模型与全局潜向量，以有限的容量换取可预测的实时行为。

**未来方向。** 为应对这一挑战，未来研究应强调联合优化保真度与效率的架构与训练方案。量化、剪枝、低秩与稀疏计算等模型压缩技术，是降低延迟与内存、同时保持控制相关性能的自然候选。诸如 SSM 的序列模型提供线性时间扩展，在紧张算力预算下的长时域推理方面展现出潜力。更广泛地说，将世界模型设计为自适应系统可能是有益的：它可以根据可用资源调整分辨率、推演时域或模态使用。例如，高容量视频扩散组件可主要用于离线数据生成或仿真，而轻量核心则保留给在线控制与安全监控。

### VI-C 建模策略

**挑战。** 尽管进展迅速，世界模型仍在长时域时间动态与高效空间表示方面存在困难。一个核心难题是平衡循环仿真与全局预测：自回归设计紧凑且样本高效，却受误差累积之苦；而全局预测以沉重的计算代价与较弱的闭环交互性，换取了更好的多步连贯性。

在空间方面，效率与归纳偏置仍是瓶颈。潜向量、token 序列、空间网格与分解式渲染表示，在表现力、几何保真度与计算成本之间各自呈现出不同的权衡。高度逼真的视频或 3D 生成模型往往捕获外观上的相关性，却缺乏稳健的因果结构，导致视觉上合理、物理上错误的预测。

**未来方向。** 已出现若干有望解决这些瓶颈的途径。基于 SSM 的架构（如 Mamba）与自回归建模天然契合，并提供线性时间可扩展性；而掩码预测框架（如 JEPA 风格的目标）支持全局、并行的预测与更强的表示学习。将局部自回归与全局或掩码更新相结合的混合设计，若再有显式记忆模块或分层规划的支持，可减少误差累积并改善长时域稳定性。

在空间轴上，未来工作应寻求更显式地编码几何与物理、同时对控制保持可处理的表示。例如，混合 token-grid 或基于神经场（neural field）的模型，可向下游策略暴露因果结构与不确定性。展望未来，一个统一的视角是将世界模型视为共享基础设施，协调具身智能体的感知、预测与决策。实现这一视角，需要紧耦合时间与空间建模、随模型与数据规模有效扩展，并支持有原则的多智能体、多任务与多模态交互的架构。

## 💡 VII 结论 (Conclusion)

本综述以横跨决策耦合、时间建模与空间表示的三轴框架，组织了具身 AI 中的世界模型。借助这一视角，我们将机器人、自动驾驶与通用视频建模中的方法映射到统一的设计空间，总结了代表性架构与基准，并分析了这些轴的不同组合如何在保真度、效率与交互性上产生不同的权衡。

展望未来，具身世界模型的进展可能由三个汇聚的趋势驱动：扩展通用视频与 3D 世界模型；通过动作与奖励条件训练加强其与控制的耦合；以及通过具有因果与物理基础的目标提升稳健性。我们预期出现的不是单一的统一基准，而是跨域、多模态的套件族，在仿真到现实（sim-to-real, S2R）偏移下联合评估预测质量、决策与安全。尽管世界模型不太可能完全弥合仿真与现实的差距，几何、物理与不确定性建模的进步应使仿真推演对下游规划与策略学习更具信息量，从而将世界模型定位为具身 AI 系统中的共享预测基础设施。

---


> ⚠️ 翻译仅供学习参考，如有歧义以原文为准。

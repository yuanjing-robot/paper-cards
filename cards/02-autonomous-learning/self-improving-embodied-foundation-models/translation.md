# 论文翻译

> 📄 对应论文原文：[Self-Improving Embodied Foundation Models](https://arxiv.org/abs/2509.15155)
> 翻译者：@sk233333
> 最后更新：2026-10-31

---

## 📝 翻译说明

- 翻译范围：**正文全译**（摘要 + §1–§7，含 Figure 1–9 图注、Algorithm 1、公式 1–5）＝ PDF p1–15；**附录按要点概述**＝ p21–29（A–J）。参考文献 p16–20 不译
- 底本：arXiv:2509.15155**v1**（2025-09-18，共 30 页；NeurIPS 2025）。下文页码均指 **PDF 物理页号**；原论文没有独立表格，结果都以图或正文数字给出
- 翻译原则：直译为主，专业术语保留英文；公式保留数学记号，便于对照原文
- 口径说明：论文原文章节顺序是「引言 → 方法 → 实验 → 相关工作 → 未来工作与局限 → 结论」，本卡按模板栏目顺序（摘要 → 引言 → 相关工作 → 方法 → 实验 → 结论）排列，但每节标题保留论文原编号（如「5 相关工作」）；§6 并入「结论」栏
- 进度：**全篇完成**——正文全译（摘要、§1、§2 全节、§3 全节、§4 全节、§5、§6、§7，含 Figure 1–9 图注、Algorithm 1、公式 1–5，PDF p1–15）+ 附录 A–J 要点概述（p21–29）
- 原文自己用词不统一处照原样保留：`steps-to-go` 全文不译；`Self-Improvement`（首字母大写）指本文第二阶段，`self-improvement`（小写）指一般概念；`episode` 视语境译「回合」或「轨迹片段」；`fleet of robots` 译「机器人集群」

| 英文 | 中文 | 备注 |
|------|------|------|
| Embodied Foundation Models (EFMs) | 具身基础模型 | 本文核心对象：以 web-scale 预训练的多模态 foundation model 为底座、经机器人数据微调后直接输出低层动作的策略（§1 p1、§5 p12）。与 VLA 基本同义，但本文偏好 EFM；不要与「具身智能体（agent）」混译 |
| Supervised Fine-Tuning (SFT) | 监督微调 | 本文第一阶段，含 BC 与 steps-to-go 两个目标（§2.1 p3）。与 LLM 后训练里的 SFT 同名，但这里多了一个「剩余步数」预测头，不是单纯 BC |
| behavioral cloning (BC) | 行为克隆 | 最大化数据集动作在 $(o_t,g)$ 条件下的对数似然（$\mathcal{L}_{\text{BC}}$，§2.1 p3）。本文 Stage 1 的 BC 策略「exactly equivalent RT-2 policies」（§4 p7），所以 RT-2 是主基线 |
| steps-to-go prediction | 剩余步数预测 | 预测从当前观测到完成 goal 还有多少 timestep（§2.1 p3）；实现上是离散 token 分类而非回归（App A.1 p21、App E p24）。全文不译 |
| self-predicted reward / reward function | 自预测奖励 / 奖励函数 | $r(o_t,a_t,o_{t+1},g)=d(o_t,g)-d(o_{t+1},g)$（式 2 p3）；$d$ 是 steps-to-go 的期望（式 1 p3）。本质是基于势能的奖励塑形（potential-based reward shaping），见 §3 p5–6、Ng et al. 1999 |
| success detector | 成功检测器 | $\text{success}(o,g)=\mathbb{1}[d(o,g)\le s]$（式 3 p4）。$s$ 原文只说「a very small number of timesteps」，未给具体值（待确认） |
| fleet of robots | 机器人集群 | 多台 robot station 并行自主练习，由一名人类操作员监控（§1 p2、§4.1.2 p9、App F p24）；真实实验用 3–4 台（Fig 6 p9、Fig 10 p25） |
| Self-Improvement | 自我改进（第二阶段） | 用自预测 reward + success detector 做 online RL；名字来自 reward 由 EFM 自身导出（§2.2 p3）。首字母大写时指本文方法，保留英文更稳 |
| online RL / on-policy REINFORCE | 在线强化学习 / 同策略 REINFORCE | Stage 2 用 on-policy REINFORCE、不做 data reuse，$\gamma=0.9$、$c=5\times10^{-2}$（§2.2 p4、App C p22）。目的是避开 deadly triad 的 off-policy learning 与 bootstrapping 两个顶点 |
| sample efficiency | 样本效率 | 本文口径是「达到同等成功率所需的机器人回合数」，不是 wall-clock 或 GPU/TPU 时；比较对象是扩大 imitation dataset（§4.1 p8–10） |
| Real2Sim | 真实到仿真 | 用真实数据训练 Stage 1，在仿真里做 Stage 2（§4.3.1 p11）。注意本文没有做 Sim2Real 实验，只说结果「预期可强烈指示」Sim2Real |
| BananaTable | 香蕉桌（保留英文） | 把 LanguageTable 的方块换成一根假香蕉，指令改为把香蕉推到桌面九个方位之一（App D.2 p23）；用来测 behavioral generalization（§4.3.2 p11–12） |
| Block2Block | 方块到方块（保留英文） | LanguageTable 中「把某方块移到/推到某方块附近」的指令子集，约占仿真 47%、真实 49%（App H p26）；Stage 2 只在这个子集上练习 |
| action chunking / action horizon | 动作分块 / 动作视野 | Aloha 用 $N=5$、10 Hz，动作 $14\times5=70$ 维，rollout 时整块执行（App D.3 p23）；LanguageTable 是 2D 单步动作 |
| rollout / episode | rollout（一次执行）/ 回合 | rollout 保留英文；episode 视语境译「回合」或「轨迹片段」。本文成功率都是训练中/评测时的 rollout 统计，不是离线指标 |
| teleoperation | 遥操作 | 人类用 leader 机械臂或 VR 头显采集示教（App D.3 p23）；real-world LanguageTable 的示教采集是 1 人对 1 机，Self-Improvement 是 1 人对多机（§4.1.2 p9） |

---

## 📖 摘要 (Abstract)

在大规模网络数据上训练的基础模型已经革新了机器人学，但它们在低层控制上的应用仍基本局限于行为克隆（behavioral cloning）。受大语言模型微调中强化学习阶段成功的启发，我们提出一种面向机器人的两阶段后训练（post-training）方法。第一阶段，监督微调（Supervised Fine-Tuning，SFT），同时使用 a) 行为克隆与 b) steps-to-go 预测两个目标对预训练基础模型做微调。第二阶段，Self-Improvement，steps-to-go 预测使模型能够导出一个形状良好的奖励函数（reward function）与一个鲁棒的成功检测器（success detector），从而使一支机器人集群（fleet of robots）能在极少人类监督下自主练习下游任务。通过在真实世界与仿真机器人具身形态上的大量实验，我们这一新的后训练配方在具身基础模型（Embodied Foundation Models）上揭示了若干重要结果。首先，我们证明 SFT 与 Self-Improvement 的组合在样本效率（sample efficiency）上显著优于扩大模仿数据采集的监督学习，并且能得到成功率显著更高的策略。进一步的消融表明，网络规模预训练（web-scale pretraining）与 Self-Improvement 的组合是这种样本效率的关键。其次，我们证明所提出的组合独特地解锁了当前方法无法实现的一项能力：自主练习并获得新技能，且这些技能泛化到远超训练中所用模仿学习数据集的行为。这些发现凸显了将预训练基础模型与在线 Self-Improvement 结合、实现机器人自主技能获取的变革潜力。

---

## 🔑 引言 (Introduction)

### 1 引言

近期工作已经证明，基础模型可以被有效地微调，直接充当低层机器人策略（Brohan et al., 2023; Padalkar et al., 2023; Reed et al., 2022; Octo Model Team et al., 2024; Kim et al., 2024; Durante et al., 2024; Black et al., 2024）；并且由于其所源自的基础模型经过 web-scale 预训练，这些策略继承了显著的泛化与鲁棒能力。到目前为止，具身基础模型（Embodied Foundation Models，EFMs）的训练范式仍局限于行为克隆（即监督学习）（Brohan et al., 2023; Padalkar et al., 2023; Reed et al., 2022; Octo Model Team et al., 2024; Kim et al., 2024; Durante et al., 2024; Black et al., 2024）。相比之下，从大语言模型（LLM）文献中可以看到，初始预训练之后，面向下游任务的后训练通常分为两个阶段：1）监督微调（SFT），随后是 2）强化学习（RL）。已有研究表明，对 LLM 做 RL 微调（RL-tuning）能显著且迅速地提升下游任务表现，超过 SFT（Stiennon et al., 2020; Ouyang et al., 2022），并已成为基础模型训练配方中的关键阶段（Guo et al., 2025; Achiam et al., 2023; Team et al., 2024; Dubey et al., 2024）。

尽管在真实世界机器人场景下研究基础模型的 RL 微调存在独特的算法与工程挑战，但前述 LLM 文献中的样本效率与性能收益，强烈地促使我们去研究它。在本工作中，我们直接应对这些挑战，并设计了一个受 LLM 后训练过程启发的两阶段框架：在第一阶段「监督微调」（SFT）中，给定一个模仿学习数据集，我们用两个目标对 EFM 做微调：a) 行为克隆，b) 预测完成期望目标所需的「steps-to-go」数目。在第二阶段「Self-Improvement」中，我们利用模型的 steps-to-go 预测来导出一个形状良好的奖励函数以及一个鲁棒的成功检测器。这些关键组件使一名人类操作员能够同时监控多台机器人，让它们自主练习下游任务。关键在于，我们数据驱动的奖励设计消除了对 ground-truth 奖励的需求，并利用了底层基础模型的鲁棒性与泛化属性。

通过在两个机器人具身形态——LanguageTable（Lynch et al., 2023）与 Aloha（Zhao et al., 2023; Aldaco et al., 2024）——上于真实世界与仿真中开展的大量实验，我们展示了这一新后训练框架令人意外的有效性。首先，我们证明 Self-Improvement 不仅能鲁棒地把策略性能提升到行为克隆之上，而且 SFT 与 Self-Improvement 的组合在样本效率上显著优于单纯扩大模仿数据采集的监督学习。举例来说，在 LanguageTable 域（Lynch et al., 2023）上，以 Self-Improvement 形式增加的 10% 机器人时间，把策略成功率从 45% 提升到 75%；相比之下，把机器人模仿数据量扩大 8 倍，只带来从 45% 到 60% 的微弱提升。进一步的消融突出了基础模型预训练在实现这种样本效率与鲁棒性方面的关键作用。

令人兴奋的是，我们这种在线 Self-Improvement 与 web-scale 预训练的新组合，还解锁了此前方法无法提供的一项独特能力：让机器人自主练习并获得新技能。与先前那些展示语义泛化（semantic generalization）的工作——例如在新情境下执行相同的 pick-and-place 动作（Brohan et al., 2023）——不同，我们证明这一组合能够实现行为泛化（behavioral generalization），其范围远远超出 Stage 1 所用的模仿数据。我们的工作凸显了把预训练基础模型与在线 Self-Improvement 结合、从而在机器人学中解锁自主技能获取的变革潜力。项目网站见：self-improving-efms.github.io。

> Figure 1 | 我们提出的两阶段微调方法概览。第一阶段（监督微调）：从预训练的多模态基础模型出发，使用机器人模仿学习数据集，以 a) 行为克隆与 b) steps-to-go 预测两个目标对 EFM 做微调。第二阶段（Self-Improvement）：自预测的奖励与成功检测使一支机器人集群能够在极少人类监督下自主练习下游任务。借助这些自预测信号，在线强化学习快速提升策略，并实现分布外（out-of-distribution）新任务的获取。

---

## 🧠 相关工作 (Related Work)

### 5 相关工作

**具身基础模型（Embodied Foundation Models）**

许多先前工作已经把预训练多模态基础模型用作机器人策略。Driess et al. (2023) 展示了分别预训练的视觉与语言基础模型如何被联合训练成多模态基础模型，并强调这些多模态模型可以学会查询低层机器人控制器以完成高层目标。沿着这一方向，Brohan et al. (2023) 把连续机器人动作离散化并映射到语言模型 token 空间。这一方法被称为 RT-2，使预训练视觉-语言模型（VLM）能够被微调为机器人策略。该做法随后通过应用到 Open X-Embodiment（Collaboration et al., 2023）数据集得到进一步验证，该数据集包含来自 21 个机构的 100 多万条机器人轨迹；它也是我们工作所基于的策略架构。

自 RT-2 以来，多种工作通过加入动作预测头来扩展预训练 VLM。动作头架构的例子包括扩散模型（Octo Model Team et al., 2024; Wen et al., 2024，建立在 Chi et al. (2023)、Ho et al. (2020) 之上）、flow matching（Black et al., 2024; Intelligence et al., 2025，建立在 Lipman et al. (2022) 之上）以及 L1 回归（Kim et al., 2024）。

关键在于，在先前工作中，预训练与后训练的界线是由离线监督微调所用的任务与数据配比来划分的。据我们所知，我们的工作是第一个走出监督学习、训练机器人基础模型的工作。我们的核心贡献是提出一个通用、无需奖励工程（reward-engineering-free）的在线 Self-Improvement 过程；它不仅带来快速的策略提升，还能获得模型训练数据之外的新行为。这种形式的行为泛化只能通过在线后训练机制实现。

**在没有 ground-truth 奖励的情况下改进机器人策略（Improving Robot Policies Without Ground-Truth Rewards）**

我们的目标是设计方法，使通用机器人基础模型能够自主地在任意下游任务上变得熟练。通过强化学习实现通用 Self-Improvement 的一个关键障碍是，我们通常无法获得 ground-truth 奖励函数与成功度量：要么是因为设计奖励本身很难（奖励工程，reward engineering），要么是因为在真实世界中测量它们很难（奖励测量，reward instrumentation）。有一类先前工作被我们称为「Code-As-Rewards」，它利用 LLM 编写代码来做奖励工程（Ma et al., 2023; Yu et al., 2023; Venuto et al., 2024）。随后用设计出的奖励训练策略，并把成功率等反馈提供给 LLM 以改进奖励函数。这类方法有一些缺点，使其不适用于真实世界中的通用机器人学习：1）通过奖励工程得到期望的策略是出了名的困难，尤其是灵巧操作任务；2）用给定奖励训练策略、再根据结果打补丁的迭代循环，对真实机器人来说不切实际；3）这类奖励函数所需的变量往往需要专门的 instrumentation 才能在仿真之外测量；4）我们仍然需要一个 ground-truth 成功检测器来给设计奖励的 LLM 提供反馈。

除 Code-As-Rewards 外，还有大量关于数据驱动奖励函数的文献。这类方法不再手工设计奖励，而是设计可随数据规模扩展的表达性表征。一个重要的工作类别（Bhateja et al., 2023; Ma et al., 2022; Sermanet et al., 2018; Chen et al., 2021）学习观测的隐表征，并在其上定义奖励与价值函数（例如用隐空间中到目标 goal 的 L2 距离）。Kumar et al. (2022) 使用一个启发式：把模仿学习数据集中接近成功状态的地方标为 +1 奖励，其余为 0；他们证明，结合目标任务与已有数据的离线/在线 RL 可以样本高效地提升机器人策略性能。Eysenbach et al. (2022) 设计了一种对比学习目标，它对应于一种目标条件 Q-Learning。Chebotar et al. (2021) 证明，带重标注 goal 的离线目标条件 RL 可以对新任务实现样本高效的下游微调。与上述工作相比，我们方法的关键优势是与 web-scale 预训练基础模型的直接整合。

RoboCat（Bousmalis et al., 2023）在一个多样化机器人任务集合上训练了一个大型行为克隆（BC）Transformer，其架构与 Gato（Reed et al., 2022）相似。他们证明，可以通过 rollout BC 策略、用实际完成的目标对回合做事后重标注（hindsight relabeling）、再把轨迹加回模仿数据集来提升策略性能。然而需要注意的是，把 hindsight relabeling 后的监督学习当作策略改进过程，可能会有重要的失败案例（Ghugare et al., 2024）。

与我们最接近的是那些基于时间步距离学习的工作。Hartikainen et al. (2019) 提出了一个迭代过程：1）rollout 策略以采集轨迹；2）通过监督学习更新状态之间的 steps-to-go 预测；3）用负距离奖励函数通过 RL 更新策略。在离线设定下，Hejna et al. (2023) 也用监督学习学习状态间的 steps-to-go，估计状态与 goal 之间的最短路径，并用加权行为克隆得到改进的策略。除了设定上的重要差异，我们工作的重点在基础模型与泛化，证明 steps-to-go 的策略改进是一条通向通用、自我改进机器人策略的可行路径。

除了提供稠密奖励信号，我们的工作还把 steps-to-go 阈值化作为获得鲁棒开放式成功检测器的新途径；这类检测器通常通过二分类训练（Du et al., 2023）。

最后，我们强调两项对本文工作的扩展。Yang et al. (2023) 证明我们的方法在基于生成式视频基础模型构建的真实世界仿真器中有效。Ma et al. (2024) 提出了本文工作的一个扩展，他们证明最先进基础模型的长上下文能力支持 in-context steps-to-go 预测，可用于离线 RL、成功检测与数据集过滤，而无需微调基础模型。

---

## 📐 方法 (Method)

### 2 方法（Methodology）

本工作的重点是研究 RL 后训练在机器人具身基础模型上的有效性。然而，机器人强化学习——尤其是操作任务——的一个关键挑战是奖励工程（reward engineering）问题。设计有效的奖励函数需要反复试错地训练策略、并给奖励定义打补丁以缓解非预期结果。此外，即使定义完美，在真实世界中测量奖励也需要大量工程投入。因此，随着我们走向训练机器人完成越来越广泛任务集的未来，手工奖励设计对真实世界机器人而言将变得不可持续。

我们通过学习数据驱动的奖励函数来克服这一障碍，这些奖励函数还从底层基础模型的 web-scale 预训练中继承鲁棒性与泛化属性。我们提出的后训练框架由两个阶段组成：1）监督微调（SFT），我们用行为克隆以及 steps-to-go 预测目标对 EFM 做微调；2）Self-Improvement（在线 RL），EFM 自主练习下游任务，并通过优化自预测奖励快速提升。

### 2.1 第一阶段：监督微调（SFT）

我们框架的第一阶段是监督微调（SFT）阶段。令 $\mathcal{D}$ 表示一个模仿学习数据集。我们假设可以采样元组 $(o_t,a_t,g_{t'})\sim\mathcal{D}$，其中 $o_t$ 与 $a_t$ 分别表示时间步 $t$ 的观测与动作，$g_{t'}$ 表示在同一轨迹中 $(o_t,a_t)$ 之后（即 $t\le t'$）发生的目标、事件或结果。这一假设涵盖了大多数模仿学习数据集，包括 hindsight 重标注数据集以及单任务数据集¹。我们对数据集轨迹的最优性不做任何假设。给定 $\mathcal{D}$，我们用一个预训练基础模型初始化 EFM，并用以下目标做监督微调：

$$\mathcal{L}_{\text{BC}}(\texttt{EFM})=-\mathbb{E}_{(o_t,a_t,g_{t'})\sim\mathcal{D}}\left[\log p^{\texttt{EFM}}_{\text{action}}\left(a_t\mid o_t,g_{t'}\right)\right]$$

$$\mathcal{L}_{\text{steps-to-go}}(\texttt{EFM})=-\mathbb{E}_{(o_t,a_t,g_{t'})\sim\mathcal{D}}\left[\log p^{\texttt{EFM}}_{\text{steps-to-go}}\left(t'-t\mid o_t,g_{t'}\right)\right]$$

$\mathcal{L}_{\text{BC}}$ 表示目标条件的行为克隆损失，我们最大化数据集动作在观测与 goal 条件下的对数似然。第二个目标 $\mathcal{L}_{\text{steps-to-go}}$ 教 EFM 在给定当前观测时预测策略距离完成预期目标还有多少时间步。该目标对实现第二阶段 Self-Improvement 起关键作用²。

> 脚注 1：例如，我们可以把单任务数据集视为一个目标条件数据集：所有回合共享同一个 goal，且该 goal 在每个回合的最后一个时间步达成。
>
> 脚注 2：在 Stage 1 中我们也可以加入额外的辅助监督目标。例如，在 LanguageTable 域的实验中，我们让模型以回合的第一帧和最后一帧为条件，预测该回合执行的指令。

### 2.2 第二阶段：Self-Improvement

在第二阶段，我们的目标是用在线 RL 在下游任务上微调 EFM，以快速提升策略性能。正如后文实验（§4.3.1 与 §4.3.2）所示，下游任务甚至可能与 Stage 1 所用数据集 $\mathcal{D}$ 中出现的任务显著不同。

**奖励函数（Reward Function）** 令

$$d(o,g):=\mathbb{E}_{p^{\texttt{EFM}}_{\text{steps-to-go}}(\text{steps-to-go}\mid o,g)}\left[\text{steps-to-go}\right]\qquad(1)$$

表示模型预测的、在观测 $o$ 下完成 goal $g$ 所需「steps-to-go」的期望值。我们用于在线 RL 微调的奖励函数定义如下：

$$r(o_t,a_t,o_{t+1},g):=d(o_t,g)-d(o_{t+1},g)\qquad(2)$$

直观上，该奖励函数预测的是：在执行动作 $a_t$ 之后，机器人离完成 goal $g$ 近了多少。由于奖励函数由 $d(o,g)$ 导出，而 $d(o,g)$ 是 EFM 自身的函数，我们因此把这一 RL 微调过程称为「Self-Improvement」。式 1 选择期望值是为了简单，并与 RL 中价值函数的概念对齐（§3）。我们把 CVaR（Alexander & Baptista, 2004，用于风险感知策略）或分布强化学习（Bellemare et al., 2023）等替代定义留给未来工作。

**成功检测（Success Detection）** 机器人回合在成功完成预期目标时终止，这一点很重要；否则采集数据中会有很大一部分是机器人停在成功状态。在没有 ground-truth 成功检测器的设定中（例如真实世界实验），我们使用由模型导出的如下成功指示：

$$\text{success}(o,g):=\mathbb{1}[d(o,g)\le s]\qquad(3)$$

其中 $s$ 是一个很小的步数。我们发现这种成功检测形式即使在低数据条件下也非常鲁棒，并且显著比在 Stage 1 中显式加入一个成功检测二分类目标更可靠。

**Self-Improvement** 在奖励函数与成功检测器就位后，我们可以对期望的下游任务做 EFM 的在线 RL 微调。我们用一份冻结的 Stage 1 checkpoint 计算奖励函数与成功检测，同时也用一份 Stage 1 checkpoint 初始化 Stage 2 策略³。Self-Improvement 循环的每一轮如下进行：用当前策略，我们通过采样一条指令 $g$、执行机器人策略，并在以下任一条件满足时终止回合，来采集一组机器人轨迹：1）成功检测器指示成功（即 $\text{success}(o,g)==1$）；2）达到预设的最大回合长度；3）人类操作员手动终止回合（例如机器人站点进入不良构型）。随后，对采集到的轨迹中的每个时间步，我们计算 Monte Carlo return $R_t\leftarrow\sum_{i=t}^{T}\gamma^{i-t}\cdot r(o_t,a_t,o_{t+1},g)$，并把 $(o_t,a_t,g,R_t)$ 放入 replay buffer。收集到足够数据后，我们用 REINFORCE 损失执行 $N$ 次策略更新：

$$-c\cdot R_t\cdot\log p^{\texttt{EFM}}_{\text{action}}\left(a_t\mid o_t,g\right)\qquad(4)$$

从 replay buffer 中无放回地采样 minibatch⁴。$N$ 次更新后，清空 replay buffer 中剩余条目，开始下一轮。上面的 Algorithm 1 给出了我们提出的 Stage 2 Self-Improvement 过程的伪代码。

尽管样本效率是本工作的关键考量，我们选择不做数据复用的 on-policy RL。On-policy 方法训练更稳定；具体使用 REINFORCE 还免去了训练价值函数的需要。这些选择消除了 deadly triad（Van Hasselt et al., 2018）中的两个顶点：Off-Policy Learning 与 Bootstrapping。在 §3 中，我们讨论所选的奖励函数如何产生一个形状良好的目标，从而减少 REINFORCE 估计器对 baseline 的需求。我们把包括 off-policy 方法在内的替代 RL 算法留待未来工作。

> 脚注 3：注意这些 checkpoint 不一定相同。关于 checkpoint 选择的讨论，感兴趣的读者参见附录 B。
>
> 脚注 4：我们使用 $\gamma=0.9$，$c=5\text{e-}2$。进一步讨论见附录 C。

> **Algorithm 1 Self-Improvement（算法 1：Self-Improvement）**
>
> **输入：** 用一份 Stage 1 checkpoint 初始化策略 $p^{\text{EFM}}_{\text{action}}$；初始化并冻结另一份 Stage 1 checkpoint，用于奖励计算与成功检测。
>
> **while true do**
>
> 　初始化空 replay buffer；
>
> 　**while** replay buffer 小于 $N\times B$ **do**
>
> 　　采样指令 $g$；
>
> 　　执行当前策略 $p^{\text{EFM}}_{\text{action}}(a_t\mid o_t,g)$，并在以下任一条件满足时结束回合：
>
> 　　- 成功检测器指示成功：$\text{success}(o_t,g)==1$
> 　　- 达到最大回合长度
> 　　- 人类操作员手动终止回合
>
> 　　用式 2 计算 Monte Carlo return：$R_t\leftarrow\sum_{i=t}^{T}\gamma^{i-t}\cdot r(o_t,a_t,o_{t+1},g)$；
>
> 　　将 $(o_t,a_t,g,R_t)$ 元组放入 replay buffer；
>
> 　**end while**
>
> 　用 REINFORCE 损失 $[-c\cdot R_t\cdot\log p^{\text{EFM}}_{\text{action}}(a_t\mid o_t,g)]$ 执行 $N$ 次策略更新；
>
> **end while**

### 3 奖励函数的直觉

**视觉直觉（Visual Intuition）**

我们可以通过可视化模型在感兴趣域上的预测，开始建立关于 steps-to-go 预测有效性的直觉。图 2 与图 3 展示了 Aloha Single Insertion 任务上的可视化。在该任务中，左臂必须先拿起一个蓝色 socket，随后右臂必须拿起红色 peg 并把它完全插入 socket。这些图的图注会带读者了解 Stage 1 训练中 steps-to-go 目标所能学到的精细细节程度。我们也鼓励读者访问补充材料网站，观看更多可视化（如视频），包括 LanguageTable 域上的。

> Figure 2 | Aloha Single Insertion 任务的一条示例轨迹，以及表示模型预测下 $\mathbb{E}[\text{steps-to-go}]$（即 $d(o,g)$）的曲线。关键时刻：1）模型认为回合即将成功完成；2）策略意外掉落 peg，$d(o,g)$ 增大；3）策略以不适合插入的错误角度重新抓取 peg，因此 $d(o,g)$ 保持高位；4）策略掉落 peg，这提供了正确重新抓取的机会，使 $d(o,g)$ 降低；5）策略正把 peg 往里推，$d(o,g)$ 表明策略即将成功；6）右手把 socket 从左手的抓握中撞出，导致 $d(o,g)$ 增大。

> Figure 3 | 上面两幅图展示了模型在 Stage 1 中从 steps-to-go 预测目标里学到的精细细节程度。每幅图截取 Aloha Single Insertion 任务一次 rollout 中的一个有趣时刻，各由 5 个连续帧组成；每帧下方可视化模型对「距离成功还有多少 steps-to-go」预测的概率分布。横轴表示 steps-to-go 的步数，纵轴表示概率质量。**上** 在第一帧，策略即将成功插入 peg 并完成任务，因此模型预测策略很可能很快成功。然而在下一帧，策略过早松开 peg，peg 即将掉落；于是预测的 steps-to-go 急剧变宽，变成一个多峰分布，考虑了从快速恢复到较长恢复时间的各种可能。随着策略在第四、五帧恢复，模型的预测重新收窄为单峰分布，认为近期成功的可能性很高。**下** 在前两帧，策略正朝成功完成任务的轨道前进，因此模型预测策略很可能很快成功。然而在第三帧，socket 开始从左夹爪中滑出。尽管这一滑动从左腕相机几乎不可见、在其他任何相机视角也完全不可见，模型立刻捕捉到了这一事件，其预测显著变宽并出现多个峰。具体来说，模型把一部分概率质量放在「立即挽救」上，其余概率质量分布在各种可能的恢复时间上。在第四、五帧，socket 完全滑出夹爪，因此模型去掉了「立即挽救」这一结果上的概率质量。

**数学直觉（Mathematical Intuition）**

令 $\mu$ 表示对应于模仿学习数据集 $\mathcal{D}$ 的策略（例如，如果数据集是通过遥操作采集的，$\mu$ 就代表「人类策略」）。考虑奖励函数 $-\mathbb{1}[o_t\text{ satisfies }g]$：当 goal 被满足时为 0，否则为 -1。令 $V^\mu$ 表示策略 $\mu$ 在该奖励函数下的无折扣价值函数。我们有

$$V^\mu(o_t,g)=\mathbb{E}_\mu\left[\sum_{i=t}^{T}-\mathbb{1}[o_i\text{ satisfies }g]\right]=\mathbb{E}_\mu\left[-1\cdot\text{steps-to-go}\right]=:-d(o_t,g)$$

把 $V^\mu$ 代入式 2，得到

$$r(o_t,a_t,o_{t+1},g)=V^\mu(o_{t+1},g)-V^\mu(o_t,g)=\underbrace{(1-\gamma)\cdot V^\mu(o_{t+1},g)}_{\text{core reward}}+\underbrace{\left[\gamma\cdot V^\mu(o_{t+1},g)-V^\mu(o_t,g)\right]}_{\text{reward shaping}}\qquad(5)$$

其中 $\gamma$ 是 Stage 2 RL 更新所用的折扣因子。可以看到，$r(o_t,a_t,o_{t+1},g)$ 隐式地是一个形状良好的奖励函数（Ng et al., 1999）：在 $\mu$ 知道如何表现好的状态中，它给出更高的奖励（即 core reward $(1-\gamma)\cdot V^\mu(o_{t+1},g)$ 较高）。因此，Self-Improvement 得到的策略比数据集策略 $\mu$ 更高效地完成预期目标，同时被隐式正则到 $\mu$ 擅长的状态空间区域附近！

用式 5 化简 Monte Carlo return 中的裂项求和，得到

$$R_t=\sum_{i=t}^{T}\gamma^{i-t}\cdot r(o_i,a_i,o_{i+1},g)=\left[(1-\gamma)\cdot\sum_{i=t}^{T}\gamma^{i-t}\cdot V^\mu(o_{i+1},g)\right]-\underbrace{V^\mu(o_t,g)}_{\text{baseline}}$$

baseline $V^\mu(o_t,g)$ 带来低方差估计，这在我们使用 REINFORCE 估计器时尤其有用。当 $\gamma$ 接近 0 时，$R_t=V^\mu(o_{t+1},g)-V^\mu(o_t,g)$，这很接近针对 $-\mathbb{1}[o_t\text{ satisfies }g]$ 奖励的单步策略改进。当 $\gamma\to1$ 时，$R_t$ 鼓励策略沿状态在数据集策略 $\mu$ 下价值高（即 $V^\mu$ 高）的轨迹行进。

**点质量导航域（Pointmass Navigation Domain）**

在补充材料网站中，我们提供了一个自包含的 Python notebook，在点质量导航域上实现 Self-Improvement。每个回合中，点质量从随机位置出发，目标是到达另一个随机采样的目标位置。我们为这个任务刻意构造了一个次优的模仿学习数据集：用 PD 控制器先导航到 5 个 waypoint，再前往目标位置。然后我们用 MLP 策略与 steps-to-go 预测模型，在这个模仿数据集上执行所提出的微调过程。图 4 展示了数据集中的样本轨迹，以及 BC（Stage 1）与 Self-Improved（Stage 2）策略的轨迹。正如预期，BC 策略模仿了数据集的次优性。然而在第二阶段，在无法访问 ground-truth 奖励的情况下，我们提出的 Self-Improvement 过程非常迅速地把策略带到接近最优。若想用我们自包含的 Colab notebook 复现，或观看轨迹与 steps-to-go 预测的可视化视频，请参阅补充材料网站。

> Figure 4 | 点质量导航域。来自模仿学习数据集的样本轨迹，以及 BC（Stage 1）与 Self-Improved（Stage 2）策略的轨迹。

---

## 📊 实验 (Experiments)

### 4 实验

在我们的实验中，我们试图验证所提出的 Self-Improvement 框架，并回答以下问题：

- **Q1**：Self-Improvement 能否在监督学习阶段之外提升下游任务的性能？
- **Q2**：监督学习与 Self-Improvement 的组合是否比单独监督学习更样本高效？
- **Q3**：依赖 RL 的 Self-Improvement 是否足够可靠、可复现，能用于真实世界机器人？
- **Q4**：预训练对我们的 Self-Improvement 过程有多大贡献？
- **Q5**：web-scale 基础模型预训练能否让 Self-Improvement 作用于那些泛化到模仿数据集之外的任务？

我们用 LanguageTable（Lynch et al., 2023）与 Aloha（Zhao et al., 2023; Aldaco et al., 2024）机器人具身形态，在仿真与真实世界中研究这些问题。全文使用 PaLI 30 亿参数视觉-语言模型（Chen et al., 2022; Chen et al., 2023）作为基础预训练模型。PaLI EFM 的输入是图像以及一段文本序列，文本表示指令、辅助信息（如关节位置）、以及是预测动作还是 steps-to-go。输出是一个 token 序列。为了把 PaLI 模型用作策略，我们沿用 RT-2（Brohan et al., 2023）的策略参数化，预测 token 化动作。因此，我们的 Stage 1 行为克隆策略与 RT-2 策略完全等价，后者将作为关键基线。关于模型、环境、tokenization 与训练的完整细节，见附录 A。

### 4.1 Self-Improvement 有效、鲁棒，且比单独监督学习更高效

#### 4.1.1 仿真 LanguageTable

我们用于训练仿真 LanguageTable 域 Stage 1 策略的数据集，是原始工作（Lynch et al., 2023）提供的那个。该数据集包含 181,020 条人类生成的轨迹，以及 78,623 条描述轨迹目标的唯一指令。我们对该数据集下采样，构造出三个新数据集，分别为原大小的 10%、20%、80%。

对每个数据规模，我们在 Stage 1 训练后执行 Stage 2 微调，并跑 3 个 seed 以验证 Self-Improvement 过程的可靠性。我们在 Block2Block 任务子集（例如「把蓝色月亮移到红色五边形」）上执行 Stage 2 微调⁵。我们在附录 H 的分析表明，Block2Block 指令在仿真与真实 LanguageTable 数据集中分别约占 47% 与 49%。当策略成功率看起来进入平台期时，我们停止 Stage 2 训练。

**结果** 图 5（第一幅图）展示了仿真 LanguageTable 域上的结果：橙色标记表示 Stage 1 之后的 BC 策略性能（等价于 RT-2），蓝色标记表示 Stage 2 Self-Improvement 之后的策略性能。可以看到，在所有数据规模（10%、20%、80%）下，我们提出的 Self-Improvement 过程都带来非常显著的成功率提升（至少 1.5 倍的性能提升），并且在 episode 数量上具有惊人的样本效率（Self-Improvement 阶段采集的额外 episode 不到 2%）。

尤其值得注意的是，在 10% 数据规模之上只增加 1% 的额外 episode，Self-Improvement 得到的策略就显著优于用 20% 与 80% 数据规模训练出的 BC 策略。在附录 G 中我们还展示了 Self-Improvement 在不同随机 seed 下是鲁棒且可复现的。

> 脚注 5：我们在附录 H 的分析显示，Block2Block 指令在仿真与真实 LanguageTable 数据集中分别约占 47% 与 49%。

> Figure 5 | Stage 2 Self-Improvement 结果。橙色：Stage 1 行为克隆策略（等价于 RT-2 基线，Brohan et al., 2023）。蓝色：经过 Stage 2 在线 Self-Improvement、只增加极少 episode 后的策略。仿真与真实 LanguageTable 以及 Aloha 域上的结果表明，我们提出的两阶段后训练方法以显著更高的样本效率取得更高成功率，优于单独监督学习。我们的 Real2Sim LanguageTable、尤其是 BananaTable 结果证明，在线 Self-Improvement 与 web-scale 预训练的新组合，使策略能够快速获得远超 Stage 1 模仿学习数据集的新技能。不同随机 seed 之间的变化很小，凸显了方法的鲁棒性。以上数值为 3 个 seed 的平均（未聚合结果见 Figure 10 与 Figure 11）。由于 Stage 1 的 LanguageTable 数据集包含多种任务，为公平起见，上文 LanguageTable 图的横轴统计的是 Block2Block episode 数量（占完整模仿学习数据集中 Block2Block episode 总数的百分比）。

#### 4.1.2 真实世界 LanguageTable

上述结果显著的样本效率与鲁棒性表明，我们的 Self-Improvement 过程可能确实适用于真实世界机器人。我们把所提出的方法应用到真实世界 LanguageTable 域，使用 20% 与 80% 两个模仿学习数据集规模⁶。我们在 80% 数据实验中用 3 台机器人站点跑了一次，在 20% 数据实验中跑了两次，一次用 3 台、一次用 4 台站点。与仿真设定一样，我们在 Block2Block 任务子集上执行 Stage 2 微调。由于指令采样、奖励标注与成功检测完全是自动化过程，在 Self-Improvement 期间，一名人类操作员就能监控我们整个 LanguageTable 机器人站点集群。人类操作员的唯一职责是：当方块掉下桌子，或某个站点在 5 分钟内没有被 shuffle 时，重置该站点。每次实验大约运行 20 小时。关于真实世界 LanguageTable 实验流程的细节，见附录 F。

> 脚注 6：我们在 80% 数据实验中用 3 台机器人站点跑了一次；20% 数据实验跑了两次，一次用 3 台、一次用 4 台站点。

> Figure 6 | LanguageTable 环境。**左** 真实世界实验所用的四台 LanguageTable 机器人站点。**右上** 真实世界 LanguageTable 机器人站点的相机视角。**右下** 仿真 LanguageTable 机器人站点的相机视角。

**结果** 图 5（第二幅图）展示了我们的结果。在 20% 与 80% 两个数据设置下，我们的 Stage 2 Self-Improvement 过程都把策略成功率从约 62–63% 提升到约 87–88%，且只额外采集约 3% 的 Block2Block episode。换个角度看，这意味着用相当于 20%（模仿数据集规模）+ 3%（Self-Improvement episode）的总经验量，我们得到的策略就远超用 80% 模仿数据集规模训练出的 BC（RT-2）策略！此外，与遥操作模仿数据采集所需的 1 人对 1 机比例不同，Self-Improvement 由于实现了 1 人对多机的比例，只需要一小部分人类投入。

#### 4.1.3 仿真 Aloha 单手插入任务

我们还在第二个机器人具身形态——双臂 Aloha 操作平台（Zhao et al., 2023; Aldaco et al., 2024）——上验证所提出的微调框架。我们设计并采集了一个双臂插入任务的数据：左夹爪必须拿起一个 socket，右夹爪必须拿起一个 peg 并把它插入 socket。图 7 展示了该任务的可视化，视频见补充材料网站。由于观测复杂得多、动作空间为 70 维、且模仿数据集小得多，这是一个更具挑战性的设定，用于进一步验证我们的方法。关于环境与数据采集过程的细节，见附录 D.3。我们构造了 5K、10K、15K 三个模仿数据集规模。我们在 5K 与 10K 规模上应用两阶段微调，同时也报告 15K 数据集上的监督学习结果，以便更好地定位这些数字。

与 LanguageTable 域实验相比，方法上的差异如下：1）Stage 2 策略初始化的 checkpoint 选择（附录 B）；2）我们注意到成功条件（peg 完全到达 socket 底部）从相机不可观测，因此当成功条件满足时，我们在奖励函数上加一个小正常数。

> Figure 7 | 仿真 Aloha Single-Insertion 任务中的四个相机视角。

**结果** 图 5（中间一幅）展示了结果。可以看到，在两个数据规模下，Self-Improvement 都显著提升了策略成功率。如前所述，我们也观察到显著的样本效率收益：用 5K（模仿）+ 2.5K（Self-Improvement）episode 训练的策略，优于用 10K 模仿 episode 训练的策略（即 RT-2），并能与用 15K 模仿 episode 训练的策略的成功率相匹敌。

**§4.1 关键结论**

- **A1**：Self-Improvement 显著提升策略性能，超出监督学习阶段。
- **A2**：监督学习 + Self-Improvement 的组合比单独监督学习样本高效得多。
- **A3**：Self-Improvement 对真实世界机器人学习鲁棒且有效。

### 4.2 基础模型预训练的重要性

研究我们提出的 Self-Improvement 过程的成功在多大程度上来自我们所起始的 PaLI（Chen et al., 2022; Chen et al., 2023）视觉-语言基础模型的 web-scale 预训练，这一点至关重要。为了消融嵌入 PaLI 的多模态知识的影响，我们从 PaLI 模型的若干替代变体出发，运行所提出的两阶段微调过程：

- **Scratch**：使用 PaLI 架构，但参数随机初始化。
- **Uni-PaLI**：PaLI 参数分别从视觉模型与语言模型初始化，各自以单模态方式预训练，未做任何联合多模态视觉-语言微调。细节见附录 A.1。

我们在仿真 LanguageTable 域上，用与 §4.1.1 相同的设定比较这些变体。尽管我们尽了最大努力并进行了很长的训练，我们观察到由 Scratch 与 Uni-PaLI 得到的 Stage 1 BC 策略显著劣于 PaLI BC 策略。因此，我们把消融集中在 Self-Improvement 阶段：从 PaLI Stage 1 checkpoint 初始化策略，并用 Scratch 或 Uni-PaLI checkpoint 计算奖励。

> Figure 8 | **左** 消融结果表明，基础模型的 web-scale 预训练对实现有效的 Stage 2 训练起关键作用，尤其是在小数据规模区间。**右** LanguageTable Real2Sim 域迁移任务上 Stage 2 Self-Improvement 期间的「Success Rate」曲线。来自 PaLI 模型的奖励标签使 Self-Improvement 显著快于 Uni-PaLI 模型。

**结果** 图 8（左）展示了结果。性能上有清晰的排序：PaLI reward model 最好，其次是 Uni-PaLI，最后是 Scratch。Scratch reward model 在不同随机 seed 下方差很大，且在低数据（10% 与 20%）条件下几乎无法带来任何有意义的提升。Uni-PaLI reward model 虽好于 Scratch，但全面显著差于 PaLI reward model，且差距在低数据设定下更明显。事实上，20% 数据规模下用 PaLI reward model 的 Self-Improvement，得到的策略优于 80% 规模下用 Uni-PaLI reward model 的 Self-Improvement！这些结果清楚展示了多模态预训练对 Self-Improvement 的巨大价值。

**§4.2 关键结论**

- **A4**：多模态预训练能显著改善 Self-Improved 策略，是样本效率的关键使能因素。

### 4.3 泛化

我们提出的在线 Self-Improvement 过程与预训练多模态基础模型的新组合，解锁了一项独特能力：让策略能够练习那些泛化到 Stage 1 模仿学习数据集所覆盖范围之外的新任务。本节展示两种难度递增的泛化形式。

#### 4.3.1 仿真与真实之间的域迁移

从一种较简单的泛化形式开始，本节研究仿真与真实之间的域迁移。Sim2Real 是一类重要的方法，可以显著减少训练高性能机器人策略所需的真实世界经验，并已在许多设定中成功应用（Pinto et al., 2017; Tan et al., 2018; Akkaya et al., 2019; Rao et al., 2020; Kataoka et al., 2023）。为了让实验更简单，本节在 LanguageTable 域上研究反问题：Real2Sim 迁移。我们用 80% 的真实世界 LanguageTable 数据集训练 Stage 1 模型，并在仿真 LanguageTable 环境中执行 Stage 2 Self-Improvement。与 §4.2 的消融类似，我们也用 Uni-PaLI reward model 变体训练 Stage 2 模型，以突出基础模型预训练在实现域迁移中的作用。

**结果** 图 8（右）展示了结果。仅用目标域（仿真 LanguageTable）中 3% 的额外 episode，我们的 Self-Improvement 过程就把策略性能从约 22% 提升到约 59%。这一性能相当于用目标域 80% 模仿数据集训练出的 BC 策略。此外，图 8（右）显示 Uni-PaLI reward model 导致 Self-Improvement 过程显著更慢，突出了预训练的关键优势。鉴于我们在 §4.1.2 中强劲的真实世界 LanguageTable 结果，我们预期 Real2Sim 结果也能强烈地预示 Sim2Real 迁移。

#### 4.3.2 学习新技能的强泛化

走向更强形式的泛化，我们研究在预训练基础模型上做 Self-Improvement，是否能让策略练习并获得 Stage 1 所用模仿学习数据集之外的新行为技能。我们从用真实世界 LanguageTable 数据集训练出的策略与奖励模型出发⁷，在一个我们称为「BananaTable」的新任务上执行 Self-Improvement（图 9）。在该任务中，我们把 LanguageTable 的方块替换成一根假香蕉，并要求策略把香蕉推到桌面上不同位置（例如「把香蕉移到桌面左侧中央」）。LanguageTable 数据集中没有香蕉，也没有任何「方块不在桌上」的回合。因此，我们完全依赖底层 PaLI 基础模型的泛化能力——策略、奖励函数与成功检测器都由它导出。

与先前展示机器人基础模型语义泛化能力的工作（例如 RT-2 在新情境下执行相同的 pick-and-place 动作；Brohan et al., 2023）不同，迁移到 BananaTable 任务需要行为泛化，要求策略学习新技能。举例来说，由于香蕉的细长几何形状，推动不准确会让它绕自身旋转，而不是朝预期方向移动（图 9 上）。

> 脚注 7：我们用 §4.1.2 中 80% 数据实验的奖励模型与 Self-Improved 策略初始化 BananaTable 的 Self-Improvement 过程。

> Figure 9 | 对 BananaTable 的强泛化。**上** 在 BananaTable 域做 Stage 2 微调之前，由于几何形状困难，策略难以有效地在桌面上移动香蕉。**左下** 经过 Stage 2 微调后，策略在 BananaTable 任务上明显更熟练（视频见补充材料网站）。**右下** 在 BananaTable 的 Stage 2 微调之前，策略与奖励模型从未见过 BananaTable 任务，这构成了一个非常具有挑战性的泛化问题。

**结果** 用 2 台机器人站点进行约 8 小时的 Self-Improvement 后，策略成功率从约 63% 提升到约 85%。除定量结果外，补充材料网站上的视频（以及图 9）显示，策略明显更熟练地完成 BananaTable 任务，并摸索出在桌面上移动香蕉的有效策略。Self-Improvement 之后，策略学会了从香蕉中段或两端推，而不是从其余部位推，以防止香蕉绕自身旋转。

**§4.3 关键结论**

- **A5**：我们提出的在线 Self-Improvement 过程与 web-scale 预训练基础模型的新组合，使策略能够快速获得新技能，且泛化远超其模仿学习数据集所覆盖的任务。

---

## 💡 结论 (Conclusion)

### 6 未来工作与局限

**回合边界与技能串联（Episode Boundaries & Skill–Chaining）**

支撑我们 Self-Improvement 阶段的 steps-to-go 辅助损失，天然适合分层控制。通过显式标注子技能的开始与终止，同一个进度估计器可以被复用，产生稠密的子任务奖励，从而实现类似 option-based RL 的长程技能串联。在推理时，高层规划器——无论是有限状态机、人类遥操作员，还是推理型基础模型——都可以调用学到的子策略，并依赖 steps-to-go 预测来决定何时切换到下一个技能。主要障碍是可扩展的回合与技能边界标注：手工标注成本高得不可行，需要创造性策略——例如利用现有多模态基础模型——从原始交互日志中恢复一致的边界。探索这种自动分割是未来研究的一个激动人心的方向。

**奖励模型（Reward Models）**

由于奖励推断在我们的框架中没有实时性要求，延迟约束很小；因此我们可以分配大得多的模型——甚至迭代式、chain-of-thought 风格的推理（Guo et al., 2025）——来获得更高保真的标签。从基于模仿的数据集学习奖励模型的一个关键挑战，是处理失败状态落在数据集 support 之外、且这些分布外（OOD）状态缺少恢复轨迹的设定。更具表达力的 steps-to-go 估计器，若能利用更广泛的数据源——机器人数据或其他数据——或许能识别这些 OOD 状态，并分配合适的形状奖励，或触发切换到恢复技能，从而提升部署时的鲁棒性。另一个可能有前景的处理 OOD 状态的方法，是用机器人策略采集一组 rollout 数据集，并为这些轨迹打标签以训练 steps-to-go 估计器。

**具身基础模型（Embodied Foundation Models）**

我们的研究微调的是通用视觉-语言骨干，这些骨干在预训练期间从未接触机器人数据。随着更大规模的多模态机器人经验语料变得可用，设计能为具身基础模型赋予强物理推理先验、同时保留其广泛视觉-语义知识的预训练课程将变得至关重要（Intelligence et al., 2025; Team et al., 2025）。在后训练一侧，不同于我们工作中针对特定下游任务的后训练，一个类似语言模型的通用后训练阶段可能使得到的策略在纯零样本（zero-shot）方式下有效，从而减少甚至消除对任务特定下游微调的需求。一个令人鼓舞的迹象是，我们 LanguageTable 实验的初步证据提示：通过 Self-Improvement 强化一个任务（Block2Block），可以明显提升其他指令（例如把方块移到特定位置）的成功率。

**RL 算法（RL Algorithms）**

为了简单与稳定，我们选择不做数据复用的 on-policy REINFORCE。这一选择消除了 deadly triad（Van Hasselt et al., 2018）中的两个顶点：Bootstrapping 与 Off-Policy Learning。然而，这一选择也放弃了现代 off-policy 算法的数据复用收益。研究能扩展到大型模型的 off-policy 变体（Farebrother et al., 2024），有望进一步降低机器人小时需求。对我们所选奖励函数与策略更新过程做理论研究，也是有前景的未来方向。如 §3 所讨论，我们的 Self-Improvement 算法隐式地把策略正则到行为克隆策略附近，但其机制与常用的 KL 正则方法（Guo et al., 2025）明显不同。我们的方法更广泛地适用于任意价值函数，而不只是 steps-to-go。最后，我们观察到把 Self-Improvement 推过性能峰值会降低成功率，这表明需要更好的停止准则或自适应正则器，以防止对形状奖励的过度优化。对我们奖励函数选择的理论研究，也可能揭示这种退化的原因。

**小结（Summary）**

我们提出的 Self-Improvement 配方已经解锁了可观的收益，只需极少的奖励工程，并由一名人类监督多台机器人。然而，要扩展到通用自主技能获取，解决上述挑战至关重要。我们期待未来研究把我们的基础工作扩展到长程任务、更丰富的奖励推断、与域对齐的预训练，以及更样本高效的强化学习。

### 7 结论

受大语言模型微调中强化学习阶段成功的启发，本工作提出了一个面向具身基础模型的两阶段后训练方法。第一阶段，监督微调（SFT），用两个目标对预训练多模态基础模型做微调：a) 行为克隆，b) steps-to-go 预测。第二阶段，在线 Self-Improvement，利用 steps-to-go 预测进行 RL 后训练。无需任务特定的奖励工程，也只需极少人类监督，这一阶段就能让一支机器人集群自主练习下游任务并获得新技能。通过在真实世界与仿真域的大量实验，我们证明 Self-Improvement 显著提升策略性能，超出监督学习阶段；并且监督学习与 Self-Improvement 的组合比单独监督学习样本高效得多。我们还证明，web-scale 基础模型预训练与 Self-Improvement 的组合能显著改善 Self-Improved 策略，是样本效率的关键使能因素。最后，我们证明这一新组合独特地解锁了当前方法无法实现的能力：自主获得新技能，且泛化远超模仿学习数据集所覆盖的任务。这些发现凸显了把预训练基础模型与在线 Self-Improvement 结合、实现机器人自主技能获取的变革潜力。

---

## 📎 附录 (Appendix)

附录（p21–29，共十节 A–J）不做逐字翻译，以下为**要点概述**。原文附录的主体是环境说明、tokenization 细节、额外曲线与基础设施架构；逐字译对理解主线帮助有限，卡片引用的数值都已在正文标注出处。页码均指 PDF 物理页号。

- **附录 A 实现细节（p21–22）**：A.1 交代底座 PaLI-3B（Chen et al., 2022, 2023）：ViT 把图像编码成 visual token，与 token 化文本拼接后送入 encoder-decoder Transformer，输出文本 token；权重先用分别单模态预训练的 Transformer LM 与 ViT 初始化，再做多模态微调。RT-2 部分重申动作离散化到文本 token、用 BC 微调；本文的 steps-to-go 也同样离散化到 PaLI token 空间。A.3 训练细节：SFT batch size 128、AdamW、全参数训练；每个 batch 在 BC / steps-to-go 目标间均匀分配；LanguageTable 还加「由首末帧预测指令」的辅助目标，但**未做消融**。Stage 2 batch 64、ViT 冻结（未做消融）、每轮 RL 循环采够做 $N=16$ 次更新的数据；$N$ 越小离策略程度越低，$N$ 越大 replay buffer 多样性越高。A.4 算力：SFT 用 64 TPUv4（2x4x4）或 128 TPUv3；Stage 2 的 learner 用 SFT 一半资源，另有 4 TPUv4 跑 reward model、4 TPUv4 跑 success detector。
- **附录 B Stage 2 初始化 checkpoint 选择（p22）**：用于 reward/success 的冻结 checkpoint 不一定与策略初始化 checkpoint 相同，因为 steps-to-go 与 BC 的最佳验证点可能不同；全文大多取各目标最佳验证 loss 的 checkpoint。**Aloha 是例外**：BC 在最佳验证 loss（约 5K–10K 步）时成功率不合理，故意继续训练到过拟合（约 100K–300K 步）后成功率才大幅提升。
- **附录 C REINFORCE 乘性常数（p22）**：仿真里发现小的正常数 $c$ 对稳定训练很关键；它不等价于缩放学习率（因为会与 weight decay 等正则交互）。全文 $c=5\text{e-}2$，未精细调参。直觉是令 $-cR_t\in[-1,1]$：若假设每步靠近目标 $N$ 步，则 $R_t\simeq N/(1-\gamma)$，于是 $c=(1-\gamma)/N$；取 $\gamma=0.9$、假设 $N\in[-2,2]$（例如 Stage 2 策略效率可达 BC 的两倍），得 $c=5\text{e-}2$。作者强调这只是粗略猜测，猜错只影响 loss 尺度，不约束学习。
- **附录 D 环境与任务（p23）**：D.1 LanguageTable 是 2D 平面 $\Delta x,\Delta y$ 动作；数据集 181,020 条人类轨迹、78,623 条唯一指令；Stage 2 用 Block2Block 子集（「把蓝色方块移到绿色星形」这类），仿真/真实占比 47%/49%；输入给 PaLI 的是当前帧与上一帧两张图。D.2 BananaTable 移除所有方块、只留一根香蕉；指令形式「X the banana to the Y of the table」，X 是与「推」同义的动词集合，Y 是 left、top left、top center、top right、right、bottom right、bottom、bottom left、center 九个方位之一。D.3 Aloha 是 14 DoF 双臂平台，关节位置控制；**预测 10 Hz 动作而非默认 50 Hz**；用动作分块 $N=5$，动作空间 $14\times5=70$ 维，rollout 时整块执行；输入额外拼接 14 个 0–255 的关节 token；4 个相机竖着拼成 2 张图（top+table 一张，left+right wrist 一张，中间加黑带分隔），224×224 输入意味着每个视角有效分辨率约 100×100，远低于 Aloha 常见的 480×640。数据采集：用 VR 头显显示 MuJoCo 仿真、用真实 Aloha leader 机械臂控制虚拟机器人，采 800 条示教；再用一个小 diffusion policy 在这 800 条上训练，生成 5K/10K/15K 三个数据集（只含成功 rollout，最大回合长度放宽到 1500 步以允许从错误中恢复）。成功的关键还包括采用 Chi et al. (2024) 的 semi-global 动作表示，并把 Stage 1 训练到远超 BC 最佳验证 loss 的位置。
- **附录 E Tokenization（p24）**：LanguageTable/BananaTable 的 2D 动作表示为 4 个 token：符号、$[0,10]$ 的数、符号、$[0,10]$ 的数；steps-to-go 取数据集中回合长度的上分位数 100 步，把 0–100 离散成 50 个 bin、每 bin 一个 token。Aloha 每个动作维一个 token、共 70 个 token（0–255），连续动作范围 $[-1,1]$；steps-to-go 上界 1500 步，因动作分块 5、rollout 时整块执行，最大回合长度降为 300 步，0–300 每个数一个 token；关节同样 14 个 token（0–255）。
- **附录 F 真实世界 LanguageTable 实验流程（p24）**：所有真实实验由 1 名人类负责监控所有机器人并执行重置；**操作员不向模型提供任何标签或成功指示**；当方块掉下桌子、或站点在最近 3–5 分钟内没有被 shuffle/reset 时执行重置。
- **附录 G 额外曲线（p25）**：Figure 10 是真实 LanguageTable 的 Stage 2 成功率曲线，共跑 3 次：1）Stage 1 用 80% 数据、Stage 2 同时用 3 台机器人；2）20% 数据 + 3 台；3）20% 数据 + 4 台。所有 Stage 2 实验都由 1 人监控并周期性重置；每次约 20 小时（4 小时 × 5 天）；横轴是 Stage 2 额外采集的 episode 占完整 LanguageTable 数据集中 Block2Block episode 总数的百分比。Figure 11 左是仿真 LanguageTable 的结果与消融，作者特别提醒 Stage 1 与 Stage 2 的横轴看起来相同但**不是 bug**，只是 Stage 2 太样本高效、差异在图上不可见；右是 Aloha Single Insertion 的「Success Rate」与「Mean Episode Length」曲线（5K 与 10K 两个设置各 3 个 seed）。这些图同样说明 SFT + Self-Improvement 比把全部机器人时间预算用于采模仿数据更样本高效。
- **附录 H Block2Block 指令占比（p26）**：用 Gemini 1.5 Pro 的结构化输出（structured outputs）把指令二分类为 Block2Block / 非 Block2Block；仿真与真实数据集各随机抽 $N=5000$ 条指令，占比分别为 47% 与 49%；按 Hoeffding 不等式，$N=5000$ 时估计误差在 2.8% 以内、置信度 99.9%。附录还完整抄了分类 prompt 与正反例。
- **附录 I 有趣观察与未完成实验（p27）**：**正迁移**——在 Block2Block 上做 Self-Improvement 不仅提升该子集，真实 rollout 显示它其实提升了所有 LanguageTable 任务。**全指令实验**——真实 LanguageTable 上，先单独训练一个 PaLI 模型「由当前图像生成目标指令」，然后以 50:50 混合 Block2Block 与模型生成指令做 Self-Improvement，并逐步把 Block2Block 比例降到 0；观察到所有任务成功率明显提升，但部分训练时段操作员没有正确设置机器人站点，因此**结果未收入论文**，也因时间关系未能重跑。**真实 Aloha**——用 3D 打印件复刻仿真插入任务、用 Aloha 遥操作采示教，Stage 1 BC 成功率合理；为支持 10 Hz 控制搭了 Version 2 基础设施，但**完整 Self-Improvement 实验没做完**就结束了项目（Figure 12 是真实复刻任务的照片）。
- **附录 J 基础设施（p28–29）**：**Version 1（非本地策略）** 用客户端-服务器结构：同一组 TPU 在数据采集阶段当 action inference server、在学习阶段当 learner；单独的 steps-to-go inference nodes 托管冻结的 Stage 1 checkpoint，负责算 $d(o,g)$（既用于式 2 的奖励差分，也用于式 3 的 success 判定）；actors 是真实机器人站点或仿真环境，按「取观测 → 请求动作 → 执行」循环；后台进程异步查询最新观测的 success 条件（因此不是每个观测都被检查）；回合结束后逐观测标 steps-to-go、算奖励与 Monte Carlo return，送入 Reverb replay buffer；中央协调器监控 buffer 大小并切换采集/学习阶段。**Version 2（本地策略）** 针对 Aloha 的 10 Hz 需求，把策略推理放到 actor 机器本地，消除网络延迟；TPU 只负责学习，每轮更新后把权重广播到所有 actor；steps-to-go 推理节点、Reverb、中央协调器保持不变。代价是每台 actor 要存完整策略模型。**本文所有报告实验都用 Version 1**，它支持最高 5 Hz 的仿真与真实环境；Version 2 只做了简短测试。

---

> ⚠️ **翻译仅供学习参考，如有歧义以原文为准。**

# 深度阅读：Self-Improving Embodied Foundation Models

> 📄 对应论文：[Self-Improving Embodied Foundation Models](https://arxiv.org/abs/2509.15155)
> 整理者：@sk233333
> 最后更新：2026-10-31

---

## 1. 问题与动机

- 一句话：把 LLM 后训练那套「SFT → RL」搬到机器人，让 VLA 不再只会 behavior cloning，而是靠自己预测的「还剩几步」导出 reward，在机器人集群上自主练习。
- 卡点一：具身基础模型（Embodied Foundation Models，EFMs）这几年的能力主要来自 web-scale 预训练 + 大规模示教，但训练目标基本只有 behavior cloning（§1 p1）。BC 只能模仿数据里出现过的行为，策略上限被示教分布框死；想让它「比人演示得更好」或「练出数据里没有的技能」，BC 本身做不到。
- 卡点二：机器人 RL 的 reward engineering 太贵。手写 reward 要反复试错打补丁，真实世界还要专门 instrumentation 才能测（§2 p3）。任务一多，人工设计 reward 根本不可扩展。
- 卡点三：真实世界 RL 的样本效率与稳定性。LLM 的 RL 后训练能快速涨点，但真机 rollout 慢、贵、不可回滚，on-policy RL 的方差和安全性都是问题（§1 p1–2）。
- 作者的切口很巧：Stage 1 多训一个 steps-to-go 预测头；Stage 2 直接用它的期望值差分当 reward，用它的阈值当 success detector。这样 reward 是「模型自己」给的，不需要 ground-truth，也不需要为每个任务写 reward（§2.2 p3–4）。

## 2. 核心方法

两阶段，所有实验底座是 PaLI-3B（§4 p7；App A.1 p21），策略参数化照 RT-2：把动作离散成 token，用 VLM 自回归输出（App A.1 p21）。

**Stage 1：SFT = BC + steps-to-go**

- 数据假设很宽松：从模仿数据集 $\mathcal{D}$ 采样 $(o_t,a_t,g_{t'})$，$g_{t'}$ 是同一轨迹未来发生的目标/事件/结果，$t \le t'$。这个假设覆盖了 hindsight relabelling 和单任务数据集（单任务可视为所有回合共享同一个 goal、最后一个 timestep 达成；脚注 1，p3）。不要求轨迹最优。
- 两个损失各管一头（§2.1 p3）：
  - $\mathcal{L}_{\text{BC}} = -\mathbb{E}_{(o_t,a_t,g_{t'})\sim\mathcal{D}}[\log p^{\text{EFM}}_{\text{action}}(a_t\mid o_t,g_{t'})]$：目标条件的行为克隆。
  - $\mathcal{L}_{\text{steps-to-go}} = -\mathbb{E}_{(o_t,a_t,g_{t'})\sim\mathcal{D}}[\log p^{\text{EFM}}_{\text{steps-to-go}}(t'-t\mid o_t,g_{t'})]$：预测还有多少 timestep 完成 goal。
- 实现上 steps-to-go 也是离散 token 分类，不是回归：LanguageTable 把 0–100 步切成 50 个 bin，Aloha 把 0–300 步每个数一个 token（App E p24）。这点很关键——它和动作 token 共用同一个 VLM 输出头，Stage 1 只是多了一个「预测剩余步数」的序列任务。
- LanguageTable 还加了一个辅助目标：给首帧和末帧，让模型预测这一回合执行了什么指令（§2.1 脚注 2，p3；App A.3 p21）。作者没做消融，所以这项贡献大小未知。

**Stage 2：Self-Improvement = 自预测 reward + 自预测 success + 集群 online RL**

- 定义 $d(o,g) := \mathbb{E}_{p^{\text{EFM}}_{\text{steps-to-go}}}[\text{steps-to-go}]$（式 1，p3），即模型预测的剩余步数期望。
- reward 就是相邻两步 $d$ 的差：$r(o_t,a_t,o_{t+1},g) := d(o_t,g)-d(o_{t+1},g)$（式 2，p3）。直观上，动作让机器人「离 goal 更近」就为正。因为 reward 由 EFM 自己导出，所以叫 Self-Improvement。
- success detector：$\text{success}(o,g) := \mathbb{1}[d(o,g)\le s]$（式 3，p4），$s$ 是「一个非常小的步数」。作者说这比在 Stage 1 显式加一个二分类 success 目标更稳（§2.2 p4），但没给 $s$ 的具体数值（待确认）。
- 一个关键工程点：reward/success 用的是**冻结的 Stage 1 checkpoint**，和 Stage 2 正在训的策略不是同一个模型（§2.2 p4；App B p22）。作者明确说这两个 checkpoint 不一定相同：steps-to-go 和 BC 的最佳验证点可能不在同一时刻；Aloha 还发现 BC 最佳验证 loss 时（约 5K–10K 步）策略成功率不行，要故意过拟合到约 100K–300K 步才明显变好（App B p22）。
- RL 算法极简：on-policy REINFORCE，不做 data reuse。每轮采 $N\times B$ 条数据，算 Monte Carlo return $R_t=\sum_{i=t}^{T}\gamma^{i-t}r$，放 replay buffer，做 $N=16$ 次更新，然后清空 buffer（Algorithm 1 p4；App A.3 p21）。$\gamma=0.9$，loss 乘一个常数 $c=5\times10^{-2}$（§2.2 p4；App C p22）。
- 为什么用 REINFORCE 而不是 PPO/off-policy：作者要稳定，且 REINFORCE 不需要 value function，这样就去掉了 deadly triad 里的 off-policy learning 和 bootstrapping 两个顶点（§2.2 p4）。代价是完全没有数据复用；作者自己在 §6 认了这一点（p14）。
- 理论直觉（§3 p5–6）：把数据集策略 $\mu$ 对奖励 $-\mathbb{1}[o_t\text{ satisfies }g]$ 的价值记作 $V^\mu$，则 $V^\mu=-d$。代进式 2 可拆成 $r=(1-\gamma)V^\mu(o_{t+1},g)+[\gamma V^\mu(o_{t+1},g)-V^\mu(o_t,g)]$，前一项是 core reward，后一项是 reward shaping（式 5，p6）。也就是说这个 reward 本质是 potential-based shaping（Ng et al., 1999），会隐式把策略正则到「$\mu$ 擅长的状态区域」。Monte Carlo return 裂项后自带 $V^\mu(o_t,g)$ 这个 baseline，降低 REINFORCE 方差（p6）。
- 机器人集群怎么跑：一名人类操作员监控整队 robot station；指令采样、reward 标注、success 判定全自动。操作员只负责在方块掉下桌子、或站点 5 分钟没被 shuffle 时重置（§4.1.2 p9；App F p24）。真实 LanguageTable 一次实验约 20 小时（4 小时 × 5 天，Fig 10 注 p25），用 3 或 4 台站点（Fig 6 p9；Fig 10 p25）。

## 3. 关键结果

- **仿真 LanguageTable 主结果**（§4.1.1 p8；Fig 5 第一幅）：数据集 181,020 条人类轨迹、78,623 条唯一指令；取 10%/20%/80% 三个子集，各跑 3 个 seed。三种数据规模下 Self-Improvement 都把成功率至少提高 1.5 倍；Stage 2 只多采了不到 2% 的 episode。最扎眼的是：10% 数据 + 1% 额外 episode 的策略，已经明显超过 20% 和 80% 数据训出来的 BC（RT-2）。
- **真实 LanguageTable**（§4.1.2 p9；Fig 5 对应子图、Fig 10 p25）：20% 和 80% 两个设置，成功率从约 62–63% 提到约 87–88%，只多采约 3% 的 Block2Block episode。换算下来，20% 示教 + 3% 自主练习的总经验，已经超过 80% 示教的 BC。人类监督从遥操作的 1:1 变成 1:多。
- **仿真 Aloha 双手插入**（§4.1.3 p9–10；Fig 5 中间子图、Fig 11 右 p25）：70 维动作（14 DoF × 5 动作分块，10 Hz），数据集 5K/10K/15K。5K 示教 + 2.5K 自我练习超过 10K 纯示教，并追平 15K 纯示教。注意这里是 **+50%** 的额外 episode，不是 LanguageTable 那种 <2%/3%。
- **预训练消融**（§4.2 p10–11；Fig 8 左）：PaLI reward > Uni-PaLI reward > Scratch reward。Scratch 在 10%/20% 低数据下基本没带来有意义提升，且跨 seed 方差很大；Uni-PaLI 全面差于 PaLI，低数据差距更大。最狠的一句：20% 数据 + PaLI reward 的策略，好于 80% 数据 + Uni-PaLI reward。
- **Real2Sim 域迁移**（§4.3.1 p11；Fig 8 右）：真实 80% 数据训 Stage 1，仿真里做 Stage 2；只多 3% 目标域 episode，成功率从约 22% 到约 59%，相当于目标域 80% 示教的 BC。Uni-PaLI reward 下提升明显更慢。
- **BananaTable 新技能**（§4.3.2 p11–12；Fig 9）：LanguageTable 数据里没有香蕉，也没有「方块不在桌上」的回合；把方块换成一根假香蕉，要求推到桌面九个方位之一。用真实 LanguageTable 80% 实验的 policy + reward model 初始化，2 台站点练约 8 小时，成功率从约 63% 到约 85%；定性上学会了从香蕉中段或两端推、避免它原地打转。
- **引言里的对比数字**（§1 p2）：LanguageTable 上「10% additional robot time 的 Self-Improvement」把成功率从 45% 提到 75%；而把模仿数据扩大 8 倍（10%→80%）只从 45% 提到 60%。
- **点质量导航 toy domain**（§3 p7；Fig 4）：故意用 PD 控制器绕 5 个 waypoint 造出次优数据集，BC 学到的也是次优轨迹；Stage 2 在没有 ground-truth reward 的情况下很快接近最优。这个例子主要是给「steps-to-go reward 能纠偏」提供直觉，不是机器人实验。
- **定性证据**（§3 p5–6；Fig 2、Fig 3）：Aloha 插入任务里，模型能在夹爪打滑的瞬间把 steps-to-go 分布从单峰拉宽成多峰，甚至捕捉到「只有左腕相机 barely visible、其他视角完全看不到」的 socket 滑落。这是全文最有说服力的一段可视化，但仍是定性。

## 4. 批判性思考

- **成功检测器的可靠性没有被量化。** success 只用 $d(o,g)\le s$ 一个阈值，$s$ 只在 §2.2 p4 说是「a very small number of timesteps」，全文没给具体值。更关键的是没有任何 calibration / precision-recall / 假阳性率指标：我们不知道模型在 OOD（香蕉、没见过的视角）上会不会过早判成功。一旦误判，episode 提前结束，后面全变成「成功态静止」的数据；论文自己在 §2.2 说这是要避免的，但没有证据说明它真的避免了。
- **Aloha 实验其实偷偷用了 ground-truth。** §4.1.3 p10 明说：成功条件（peg 完全插到 socket 底部）从相机不可见，所以「when the success condition is met」给 reward 加一个小正常数。这个 success condition 在仿真里只能来自 simulator state，等于在 reward 里塞了任务特定的成功信号；常数取值也没给（待确认）。这让「no task-specific reward engineering」的口号在 Aloha 上打了折扣——至少不是纯自预测 reward。
- **奖励是 potential-based shaping，天然偏向数据集策略。** §3 p5–6 自己推导出 reward 会隐式正则到 $\mu$ 擅长的区域。这解释了大方向上为什么稳，但也意味着「练出新技能」依赖的是 foundation model 的视觉先验，而不是 reward 本身对香蕉的物理理解。BananaTable 只改了几何形状、没改动作空间和具身形态，所谓 behavioral generalization 的边界比摘要里的「far beyond」窄得多：没有抓取、没有插入、没有新具身、没有新相机视角。真实世界的 Aloha 双手插入实验根本没做完（App I p27），只验证了 Stage 1 BC 能跑。
- **「比扩大模仿数据更样本高效」的比较口径有坑。** 第一，引言的「10% additional robot time → 45%→75%」和 §4.1.1 的「<2% extra episodes」对不上；「robot time」到底指 episode 数、墙钟时间还是总算力，原文没定义（待确认）。第二，Aloha 的自我练习是 +2.5K episodes（相对 5K 是 +50%），和 LanguageTable 的 <2% 完全不是一个量级，跨域引用「sample-efficient」时要小心。第三，x 轴只数 Block2Block episode，Stage 1 的百分比却是整数据集百分比；两种分母不同。第四，对照的「8× 模仿数据」是 10%→80% 的同一分布扩量，并没有和「同样 3% 预算拿去多采示教」做对比，所以只能说明「比盲目堆数据好」，不能说明「比主动选数据好」。
- **机器人集群的成本与安全被轻描淡写。** 真实实验要 3–4 台 LanguageTable 站点、1 名操作员全程盯着、每次约 20 小时；Stage 2 还要额外的 reward 模型 4 台 TPUv4 + success detector 4 台 TPUv4，learner 用 SFT 一半资源（App A.4 p22）。这不是「minimal human supervision」的字面成本。安全层面更空白：没有力/力矩限制、碰撞检测、急停策略，也没有报告任何事故率；操作员手动终止是唯一兜底（§2.2 p4），论文自己也举了「机器人站点进入 bad configuration」的例子。让一群 RL 策略在真机上探索，风险没有被量化。
- **真实世界探索代价并不低。** 20 小时 × 3–4 台只是 LanguageTable 的 2D 推方块；BananaTable 8 小时 × 2 台。Aloha 仿真要 2.5K 额外回合，真实 Aloha 的 10 Hz 基础设施（Version 2）只「briefly tested」，完整实验没跑完（App J p28–29）。所以「真实世界 online RL 可行」的证据集中在低成本、低维动作、可快速重置的平面推动任务上。
- **RL 算法只测了一种，且没有基线对比。** on-policy REINFORCE、无数据复用、固定 $\gamma=0.9$、$c=5\times10^{-2}$；没有 PPO、没有 off-policy、没有 KL 正则、没有 value-based 方法。§6 p14 自己承认放弃数据复用，并把 off-policy 留作未来工作；也承认「练过头会掉成功率」，需要更好的 stopping criterion。这意味着实际使用时要靠人看曲线早停，和「自主」有张力。
- **实验统计强度偏弱。** 仿真 3 个 seed，真实 80% 只跑 1 次、20% 跑 2 次（3 台和 4 台，Fig 10 注 p25）；成功率大多从图 5 的曲线上读，正文只给约数（~62–63%、~87–88%），没有逐任务表、没有置信区间。Aloha 的 3 seed 也只覆盖仿真。跨 seed 方差小这句话（Fig 5 注 p8）没有给出数值。
- **官方代码基本没开。** 项目主页只挂了 pointmass 的 notebook，没有训练、reward model、真机集群的代码；PaLI-3B 权重是否公开可下载仍存疑（待确认）；机器人站点、TPU 集群、Aloha 的 VR 数据采集流程都不可复制。加上 $s$、Aloha reward 常数、最大 episode 长度、真实实验的指令采样细节都没写全，复现难度极高。这不是「开源复现」类论文，更像「工业实验室内部可复现」。
- **相关工作定位有选择性。** 和 RoboCat（Bousmalis et al., 2023）的对比只停在「hindsight relabeling + supervised learning 有 failure case」，没有同任务同数据的实验对比；和 SOAR、LiReN 这类同样做 fleet autonomous improvement 的工作也没有直接比。论文说自己是「first to move past supervised learning for robot foundation models」，这个「first」的边界取决于怎么定义 foundation model 和 online post-training，至少需要和并发工作对齐口径（待确认）。
- **奖励模型的 OOD 问题被自己点出但没解。** §6 p14 说 failure states 可能落在数据集 support 外、缺少 recovery 轨迹；解决办法是更大模型/更多数据/CoT。这其实承认了 BananaTable 的成功有很大运气成分：reward model 对香蕉的泛化没有被单独评测。

## 5. 个人收获

- 最值得抄的是「**多一个 steps-to-go 头**」。它几乎不增加架构复杂度（和动作 token 共用 VLM 输出头），却同时给出三样东西：dense reward、success detector、以及一个可解释的进度曲线。以后做 VLA 微调，如果数据里有完整的成功回合，我会优先加这个辅助目标，而不是一上来就上 RL。
- 第二个是「**reward 模型和策略解耦**」。Stage 2 用冻结的 Stage 1 checkpoint 算 reward，不让 reward 和 policy 一起更新，避免 reward 被策略带偏。这个工程习惯很重要；很多 online RL 崩掉就是 reward model 跟着 policy 漂。
- 第三个是「**success = 剩余步数低于阈值**」这个视角。它把 open-ended 的成功检测变成了一个标量预测问题，比训二分类器更省标签；但阈值 $s$ 必须自己校准，不能照搬。用在我们的任务上，我会先在离线数据上画 $d(o,g)$ 的分布，再定阈值，并单独统计假阳性。
- 第四个是「**1 人多机的运营模型**」。真正贵的不是算法，是重置和异常处理；论文把操作员的职责压缩到「掉桌/5 分钟没 shuffle 就重置」，这是可以工程化的。如果我们以后搭多机器人实验平台，应该先把重置、指令采样、日志和急停做成自动化，再谈 RL。
- 最后是一个反直觉的点：这篇论文的「新技能」不是靠 RL 从零探索出来的，而是靠 foundation model 的视觉先验 + 少量在线练习「唤醒」的。这提醒我，做具身项目时，预训练先验的质量可能比 RL 算法本身更决定上限。

## 6. 延伸阅读（可选）

- **RoboCat**（Bousmalis et al., 2023，arXiv:2306.11706）：同样叫 self-improving，但走的是「rollout → hindsight relabel → 把成功轨迹加回监督数据集」的路线，没有 online RL。对照它可以看出本文的差异：本文用 steps-to-go 导出的 dense reward 做 policy gradient，RoboCat 用 relabel 后的 BC。本文 §5 p12–13 专门点了 RoboCat 的 failure case（Ghugare et al., 2024）。
- **SOAR**（Zhou et al.，arXiv:2407.20635，*Autonomous Improvement of Instruction Following Skills via Foundation Models*）：同样主张「机器人集群自主采数据 + 无人工标注地提升指令跟随」，但更偏数据采集与筛选/模仿学习，和本文的 online RL + self-predicted reward 是两条路线。适合拿来对比「自主数据」和「自主 reward」哪个更 scalable（细节待核对原文）。
- **LiReN**（Stachowicz et al.，*Lifelong Autonomous Improvement of Navigation Foundation Models in the Wild*，CoRL 2024，PMLR v270 于 2025 年出版；任务描述写 CoRL 2025，年份口径待确认）：把「部署中持续自主微调」做到导航 foundation model，和本文的 manipulation 版本互补。它的重点是 lifelong + 真实开放环境，本文的重点是 steps-to-go reward；可以对照两者对「success / reward 从哪来」的处理。
- **RT-2**（Brohan et al., 2023，arXiv:2307.15818）：本文 Stage 1 的 BC 策略就是 RT-2 参数化，主基线也是它；本仓库已有 RT-2 卡片，可以直接对照动作 tokenization 和 co-fine-tuning。
- **LanguageTable**（Lynch et al., 2023）与 **Aloha**（Zhao et al., 2023；Aldaco et al., 2024）：两个主力具身环境/平台，前者是 2D 推方块，后者是 14 DoF 双臂。
- **steps-to-go 的上游**：Hartikainen et al. (2019) 的 iterative steps-to-go + negative distance reward、Hejna et al. (2023) 的离线 shortest-path + weighted BC，都是本文 §5 自己认的近亲；想理解「为什么用剩余步数当 reward」值得回看。
- 项目主页 self-improving-efms.github.io 有 Aloha/LanguageTable 的 steps-to-go 可视化视频和 pointmass Colab notebook；前者比 Figure 3 更能看出分布怎么随事件变宽/变窄。

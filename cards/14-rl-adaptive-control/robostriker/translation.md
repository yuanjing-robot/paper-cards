# RoboStriker：面向自主人形机器人拳击的隐空间策略博弈

> 原文：**RoboStriker: Latent-Space Strategic Games for Autonomous Humanoid Boxing**  
> 原文版本：[arXiv:2608.16195v1](https://arxiv.org/abs/2608.16195v1)，2026-08-17  
> [PDF](https://arxiv.org/pdf/2608.16195v1) · 项目页：论文中给出，具体链接待补充
> 整理者：@wbxxmz · 最后更新：2026-11-02  
> 翻译状态：摘要、正文 §I–§V、表 I–II 与图 1–4 图注已译；参考文献保留原文。  
> 本文为 AI 辅助中文学习译稿，未经作者审校，尚待整理者人工复核。译文中的“我们”指论文作者，不代表整理者自行完成了这些实验。专有方法名、模型名与数据集名保留英文。

**作者**：Kangning Yin¹,²,³\*、Kaige Liu⁴,²,³\*、Zhe Cao²\*、Wentao Dong¹,²、Weishuai Zeng²、Tianyi Zhang¹、Qiang Zhang⁵、Jingbo Wang²、Jiangmiao Pang²、Yang Li¹,²†、Ming Zhou²†、Weinan Zhang¹,²†

¹上海交通大学、²上海人工智能实验室、³上海创智学院、⁴华中科技大学、⁵中国科学技术大学

（\* 共同第一作者；† 共同通讯作者）

> arXiv:2608.16195v1 [cs.RO] 2026 年 8 月 17 日

## 术语约定

| 英文 | 本文译法 |
|------|------|
| latent-space zero-sum Markov game | 隐空间零和马尔可夫博弈 |
| motion tracker | 运动跟踪器 |
| latent manifold | 隐流形 |
| motion decoder | 运动解码器 |
| adversarial motion prior / AMP | 对抗运动先验 |
| Neural Fictitious Self-Play / NFSP | 神经虚拟自博弈 |
| best response | 最优响应 |
| average policy | 平均策略 |
| reservoir sampling | 水库采样 |
| engagement rate / ER | 交战率 |
| offensive landing rate | 进攻命中率 |
| base orientation stability / BOS | 基座朝向稳定性 |
| torque smoothness | 力矩平滑度 |
| retargeting | 重定向 |
| sim-to-real | 仿真到现实 |

## 摘要

在人形机器人上实现人类水平的**竞争智能**与**身体敏捷性**仍是一项深刻挑战，在拳击这类接触密集、高度动态的任务中尤为突出。多智能体强化学习（MARL）虽然为策略交互提供了原则性框架，但若直接作用于**无结构的原始运动空间**，必然导致关节层面的身体崩溃，使任何可行的格斗战术都无法涌现。为化解"策略探索"与"物理可行性"之间的这一根本冲突，我们把人形机器人格斗任务表述为一种新的**双人隐空间零和马尔可夫博弈**。在标准的正则性假设与近似最优响应假设下，我们证明隐空间表述会在**解码器可达的动作流形**上诱导出一个等价博弈，从而为由此产生的自博弈动力学提供近似 Nash 均衡解释。为实例化这一理论表述，我们提出 **RoboStriker**——一个将高层推理与低层执行解耦的分层框架：它首先把预定义拳击动作的跟踪专长蒸馏到一个**拓扑有界的隐流形**中；这一结构化的隐空间基础随后通过**隐空间神经虚拟自博弈**（Latent-Space Neural Fictitious Self-Play）驱动多智能体共同进化。大量实验结果表明，在这一结构化隐空间中进行博弈，显著优于直接探索。通过用预训练运动解码器约束策略探索，RoboStriker 大幅减少了原始动作空间方法中出现的灾难性失衡，并在竞争胜率与击打效率两方面取得更优的战术表现。最后，我们成功将学到的格斗策略部署到真实人形机器人上并完成验证。代码、视频与补充材料见项目页 RoboStriker。

## I. 引言

人形机器人是具身智能的关键前沿。近期突破已展现出卓越的运动与敏捷机动能力 [1–4]。然而这些成功高度依赖静态或可预测的环境，其主要目标是**单智能体**的全身运动跟踪与轨迹生成 [2, 5]。当把人形控制扩展到竞争性的多智能体物理交互（如拳击）时，问题本质从孤立的轨迹跟踪，转变为在严苛物理约束下的**策略性协同适应**。这一转变自然将人形竞赛框定为多智能体强化学习问题。

然而，让人形机器人参与竞争性物理交互，面临一个深刻的科学挑战：**无约束的策略交互与严格物理可行性之间的根本冲突**。从机器人学角度看，Unitree G1 这类人形机器人工作在高维、无结构的原始运动空间中，核心难点在于该无约束空间中的绝大多数关节组合都对应物理上无效的动作。要发现竞争性战术，强化学习本质上需要主动、多样的探索；但在脆弱的动作空间中执行这种无约束探索，往往在形成任何有意义的策略交互之前就已发生灾难性失衡 [5, 6]。因此机器人因这些基础物理违规而被严厉惩罚，形成**具身冷启动问题**——连发现一个有效格斗动作都极其困难 [7]。而在多智能体场景下，一个主动、不断演化的对手会持续带来不可预测的物理扰动 [8, 9]，使这种物理脆弱性被进一步放大。原始运动空间中没有任何结构性约束来抵御这些冲撞，学习过程常常在维持基本平衡的重负下崩溃，完全阻断了更高层战术智能的涌现。

为突破这一瓶颈，我们把人形拳击表述为**双人隐空间零和马尔可夫博弈**：策略竞争发生在一个有界的隐域上，由预训练的低层运动解码器把隐动作映射到解码器可达的运动流形。在标准正则性假设与近似最优响应假设下，所得隐博弈在该解码器诱导的动作流形上具备近似 Nash 解释（详见第 III-A 节）。

在此理论表述之上，我们提出 RoboStriker，一个把具身 MARL 分解为三个耦合层次的分层框架：物理可行的运动库、用于策略表示的结构化隐运动空间、以及在该隐空间上的多智能体策略演化。第一层建立跟踪策略，忠实复现多样的人类运动原语；第二层把这些技能蒸馏到支持多样运动生成的有界隐运动空间；最后引入**隐空间 NFSP（LS-NFSP）**，在这一紧凑流形内实现多智能体共同进化。此外，我们用**对抗运动先验（AMP）[6] 课程预热**来初始化策略，缓解竞争性冷启动问题并显著降低非平稳性。我们在使用 Unitree G1 机器人 [10] 的人形拳击任务上评估该框架。实验结果显示，通过把策略探索限制在物理可行的隐空间，RoboStriker 从根本上避免了现有基线固有的平衡崩溃。

核心贡献总结如下：

- 我们把竞争性人形拳击表述为由预训练运动解码器诱导的**双人隐空间零和马尔可夫博弈**。在标准正则性与近似最优响应假设下，刻画隐策略与解码器可达物理动作流形之间的对应关系，并对所得博弈给出近似 Nash 分析。
- 我们提出 **RoboStriker** 这一分层算法框架，通过把高层策略推理与低层物理执行解耦来实例化该隐博弈。通过将运动跟踪专长蒸馏到拓扑结构化的连续流形，该框架经由隐空间神经虚拟自博弈顺利驱动鲁棒的多智能体共同进化。
- 我们在 29 自由度 Unitree G1 人形机器人上进行实证验证，表明 RoboStriker 在竞争胜率与击打效率上超越现有基线，取得更优战术表现。实验进一步显示，隐空间策略学习相比原始动作空间探索显著提升物理稳定性；而 29-DoF+AMP 基线则证实这些收益不能仅用运动正则化解释。最后，我们在真实人形硬件上验证了所学策略，如图 3 所示。

## II. 相关工作

### A. 人形运动合成与控制

基于物理的人形控制已从特定动作模仿 [5]，发展到对抗运动先验（AMP）[6] 以及近期的通用运动跟踪器 [2, 4, 11]。这些方法能在物理约束下鲁棒地复现多样人类运动，为可复用的全身控制提供了有效基础。但它们主要关注**单智能体**的运动跟踪，或由外部指定运动目标的任务执行。竞争性人形交互带来额外挑战：控制器不仅要维持平衡与动作质量，还必须持续适应一个**非平稳、且存在物理交互的对手**。RoboStriker 以鲁棒运动跟踪作为低层运动基础，研究如何把这类运动专长暴露为一个紧凑接口，供多智能体策略学习使用。

### B. 隐运动表示与运动先验

学习可复用的隐运动表示，是降低高维角色与人形控制复杂度的常见手段。ASE [12] 以超球面隐表示学习可复用的对抗技能嵌入；CALM [13] 发展条件隐模型以实现可控角色行为；PULSE [7] 则学习**状态条件**的隐运动表示，把广泛的人形运动专长蒸馏为面向下游控制的紧凑接口。这些工作表明，学习到的隐变量可为复杂运动行为提供有效抽象。

我们的工作并不把超球参数化本身当作新的运动表示机制，而是把一个**有界隐运动接口**作为竞争性人形博弈的策略动作空间。预训练的状态条件解码器把高层隐决策映射到解码器可达的运动流形，而多智能体学习完全在该紧凑接口上进行。这一表述使我们能明确研究隐动作抽象如何与对抗运动正则化及竞争性自博弈相互作用。

### C. 竞争性角色控制与多智能体强化学习

竞争性控制已在多智能体强化学习与物理仿真角色动画中得到广泛研究。经典自博弈 [8, 9] 让智能体通过反复交互提升；虚拟博弈 [14] 与神经虚拟自博弈 [15] 通过纳入对手的历史或平均策略来稳定学习。已有工作还展示了物理仿真角色从事竞争性运动，包括双人竞技交互 [16]；近期的人形系统也在交互式运动场景中探索学习到的运动技能 [17]。

RoboStriker 在这些研究基础上，把竞争性学习放在一个**预训练的隐运动接口**而非完整运动空间上。结合神经虚拟自博弈，这既把依赖对手的策略学习与低层全身执行解耦，又把优化限制在一个紧凑隐域内；这一表述同时构成我们对诱导隐博弈做近似 Nash 分析的基础。

## III. 方法

实现自主人形拳击，需要克服**无约束多智能体策略探索**与**高维运动控制的极度物理脆弱性**之间的根本冲突。为化解这种内在不稳定性，我们提出 RoboStriker——一个把理论博弈表述与鲁棒执行流水线整合起来的分层竞争学习框架。我们首先在第 III-A 节把格斗任务形式化为双人隐空间零和马尔可夫博弈，其中策略交互被限制在由预训练运动解码器诱导的有界隐域内（该诱导博弈的形式化近似 Nash 分析见项目页）。为实例化这一表述，我们的流水线通过三个紧密耦合的阶段系统地解耦高层意图与低层执行：通过通用运动跟踪器学习鲁棒物理基础（第 III-B 节）；将多样运动专长蒸馏到拓扑结构化的隐空间（第 III-C 节）；以及通过 AMP 正则化预热与隐空间神经虚拟自博弈逐步演化多智能体策略（第 III-D、III-E 节）。

> **图 1：RoboStriker 总览。** 阶段 I 预训练运动跟踪器，产生物理合理的人形行为；阶段 II 把这些行为压缩到有界隐空间，用于高层控制；阶段 III(a) 在阶段 II 之上进行预热训练，随后进入阶段 III(b)——在隐空间上运行 NFSP，把双人拳击求解为隐空间零和博弈。

### A. 双人隐空间零和马尔可夫博弈

我们把双人拳击任务形式化为隐空间零和马尔可夫博弈，其定义为元组

$$\mathcal{M}=\langle \mathcal{I},\mathcal{S},\{\mathcal{O}\}^{i\in\mathcal{I}},\{\mathcal{A}\}^{i\in\mathcal{I}},\{\mathcal{Z}\}^{i\in\mathcal{I}},D_\psi,\mathcal{P},\{\mathcal{U}\}^{i\in\mathcal{I}},\gamma\rangle$$

其中 $\mathcal{I}=\{1,2\}$ 为玩家集合，$\mathcal{S}$ 为底层状态空间，$\{\mathcal{O}\}^{i\in\mathcal{I}}$ 为各玩家观测空间集合。

关键之处在于，为区分高层策略推理与低层物理执行，我们明确把 $\{\mathcal{A}\}^{i\in\mathcal{I}}$ 定义为原始运动动作空间集合，特别指定 $\mathcal{A}^i\subset\mathbb{R}^{29}$ 为 29 自由度关节位置目标。同时定义 $\{\mathcal{Z}\}^{i\in\mathcal{I}}$ 为有界连续隐策略空间集合，其中 $\mathcal{Z}^i\subset\mathbb{R}^d$。环境中执行的动作由预训练、共享的运动解码器 $D_\psi:\mathcal{S}\times\mathcal{Z}^i\to\mathcal{A}^i$ 从隐空间映射得到。于是环境的底层转移动力学 $\mathcal{P}_{env}:\mathcal{S}\times\mathcal{A}^1\times\cdots\times\mathcal{A}^{|\mathcal{I}|}\to\Delta(\mathcal{S})$ 与原始效用函数 $u^i_{env}:\mathcal{S}\times\mathcal{A}^1\times\cdots\times\mathcal{A}^{|\mathcal{I}|}\to\mathbb{R}$ 诱导出隐层转移函数 $\mathcal{P}:\mathcal{S}\times\mathcal{Z}^1\times\cdots\times\mathcal{Z}^{|\mathcal{I}|}\to\Delta(\mathcal{S})$ 与效用函数 $u^i\in\mathcal{U}^i:\mathcal{S}\times\mathcal{Z}^1\times\cdots\times\mathcal{Z}^{|\mathcal{I}|}\to\mathbb{R}$。这里 $\Delta(\cdot)$ 表示给定集合上的概率单纯形。具体地，诱导效用为 $u^i(s,z^1,z^2)=u^i_{env}(s,D_\psi(s,z^1),D_\psi(s,z^2))$，$\gamma\in[0,1)$ 为折扣因子。

设每个玩家 $i\in\mathcal{I}$ 采用隐策略 $\pi^i_z:\mathcal{O}^i\to\Delta(\mathcal{Z}^i)$，联合策略记为 $\pi_z=(\pi^1_z,\pi^2_z)$。在联合策略 $\pi_z$ 下，玩家 $i$ 从状态 $s\in\mathcal{S}$ 出发的期望回报为

$$V^i_{\pi_z}(s)=\mathbb{E}\left[\sum_{t=0}^{\infty}\gamma^t u^i(s_t,z^i_t,z^{-i}_t)\mid s_0=s\right]$$

其中 $-i$ 表示对手。在严格零和设定 $u^1=-u^2$ 下，我们不直接求解静态优化目标，而是让每个智能体针对对手的经验策略分布计算**近似最优响应**并迭代更新策略。若把策略更新视作对经验对手策略的有界误差近似最优响应，则所得经验策略在隐博弈中具备 $\epsilon$-Nash 刻画；相应近似误差取决于所学最优响应的质量与优化中引入的正则化。

关于隐空间近似 Nash 收敛（含假设与证明思路）的形式化分析见项目页。接下来我们通过三阶段分层流水线实例化该隐博弈表述。

### B. 学习专家级运动跟踪器

如图 1（阶段 I）所示，第一阶段学习一个鲁棒低层控制器，它能忠实跟踪多样的人形拳击动作，并为高层策略学习提供稳定运动基础。跟踪器 $\pi_{trk}(a_t\mid s^{self}_t,s^{ref}_t)$ 使用人类动捕数据训练，并在所有机器人间共享，其中 $s^{self}_t=(s^{prop}_t,s^{priv}_t)$。此处 $s^{prop}_t$ 表示机器人本体感知状态，$s^{priv}_t$ 表示机器人机载传感器无法获取的特权观测。$s^{ref}_t$ 指定由人类动捕数据导出的参考运动目标，表示为一个按时间索引的全身人形姿态与速度序列，从动捕数据集 $\mathcal{D}_{motion}$ 中提取。每个 $s^{ref}_t$ 编码了标准人形运动学树中的根位置与朝向、关节角及对应关节速度。所有动作在时间上对齐并重定向到仿真人形形态，从而在多样拳击行为上实现一致的跟踪。优化目标是在参考轨迹 $\tau^{ref}$ 上最大化期望跟踪奖励 $r_{trk}$，在保持高保真模仿的同时维持物理合理性：

$$\pi^*_{trk}=\arg\max_{\pi_{trk}}\ \mathbb{E}_{s^{ref}\sim\tau^{ref},\ \tau^{ref}\sim\mathcal{D}_{motion}}\left[J_{\pi_{trk}}(s^{ref})\right] \tag{1}$$

其中 $J_{\pi_{trk}}(s^{ref})=\mathbb{E}_{a_t\sim\pi_{trk}}\left[\sum_{t=0}^{T}\gamma^t r_{trk}(s^{self}_t,a_t;s^{ref})\right]$。

具体而言，我们用 Xsens 动捕系统 [18] 采集职业拳手的拳击动作，并通过左右镜像将语料翻倍，得到约 30 分钟、50 Hz 的运动序列，覆盖击打、防守、步法与转换。采集序列经广义运动重定向（Generalized Motion Retargeting）[19] 重定向到 Unitree G1 形态，形成 $\mathcal{D}_{motion}$。跟踪观测拼接本体感知 $s^{prop}_t$、长度 $K=3$ 的未来姿态短时窗参考，以及上一动作 $a_{t-1}$；动作为 29 自由度关节位置目标，由 PD 控制器跟踪。奖励 $r_{trk}$ 是若干指数项的加权和，涵盖根与身体姿态/朝向跟踪、线速度与角速度匹配，以及控制正则化（动作速率、关节限位、非期望接触）。参照 [5]，出现姿态崩塌、末端执行器高度违规或 10 s 时长上限时提前终止回合。精确奖励权重与缩放系数见项目页。

### C. 通过拓扑隐蒸馏编码运动

如图 1（阶段 II）所示，为支持可学习的策略控制，我们把高维运动空间投影到紧凑连续隐空间 $\mathcal{Z}$。这通过教师—学生蒸馏框架 [20] 实现，包含编码器 $E_\phi$、解码器 $D_\psi$ 与状态条件隐先验 $P_\xi$。编码器把观测 $o_t=(s^{self}_t,s^{ref}_t)$ 映射到隐码分布 $z_t\sim E_\phi(\cdot\mid o_t)$。实现中把 $E_\phi(z_t)$ 建模为对角高斯 $\mathcal{N}(z_t\mid\mu^e_t,\sigma^e_t)$。随后训练解码器，以 $(s^{prop}_t,z_t)$ 为条件重建教师动作 $a_t\sim\pi_{trk}(\cdot\mid o_t)$：

$$D^\star_\psi=\arg\min_{D_\psi}\ \|a_t-\hat{a}_t\| \tag{2}$$

其中 $\hat{a}_t\sim D_\psi(\cdot\mid s^{prop}_t,z_t)$。考虑到运动生成固有的状态依赖性，我们显式学习状态条件隐先验 $P_\xi(z_t\mid s^{prop}_t)=\mathcal{N}(z_t\mid\mu^p_t,\sigma^p_t)$。该先验用于建模从当前本体感知状态出发的有效转移，并通过 KL 正则化 [21] 约束编码器 $E_\phi(z_t\mid o_t)$，从而防止后验坍缩，即

$$(E^\star_\phi,P^\star_\xi)=\arg\min_{(E_\phi,P_\xi)}\ D_{KL}\left(E_\phi(z_t\mid o_t)\,\middle\|\,P_\xi(z_t\mid s^{prop}_t)\right) \tag{3}$$

一个关键设计是**有界化策略隐域**。为此我们把隐码归一化到单位超球面，为高层优化提供紧凑参数化。预训练的状态条件解码器随后把这些隐决策映射到其学到的运动流形上，后者即构成诱导博弈的有效物理动作空间。实现中令 $z$ 满足如下归一化要求：

$$\hat{z}=\mathrm{Normalize}(z)=\frac{E_\phi(o)}{\|E_\phi(o)\|_2} \tag{4}$$

从而把 $z$ 的隐表示约束在单位超球面上。学生同时优化动作重建与先验对齐：

$$\mathcal{L}_{rec}=\mathbb{E}\left[\|a_t-\hat{a}_t\|^2\right] \tag{5}$$

$$\mathcal{L}_{prior}=\mathbb{E}\left[D_{KL}\left(E_\phi(z_t\mid o_t)\,\middle\|\,P_\xi(z_t\mid s^{prop}_t)\right)\right] \tag{6}$$

$$\mathcal{L}_{distill}=\mathcal{L}_{rec}+\lambda_{prior}\mathcal{L}_{prior} \tag{7}$$

其中 $\lambda_{prior}=0.001$。这一双重目标既恢复了教师的运动专长，又为后续竞争性共同进化构建出结构化、先验条件化的流形。

### D. 基于对抗先验的行为预热

为规避在没有基本战术能力时直接启动自博弈所带来的严重不稳定性，我们设计了行为预热阶段，如图 1（阶段 IIIa）所示。智能体针对一个严格保持稳定站姿的**静止对手**学习有效击打行为。一个可学习残差策略 $\pi_\theta(\cdot\mid s^{goal}_t)$ 在第二阶段固定行为先验 $P^\perp_\xi$ 之上输出残差隐指令 $\Delta z_t$，从而保证稳定且类人的运动。于是 $\pi_z$ 的完整形式为

$$\pi_z(\cdot\mid s^{prop},s^{goal})=\pi_\theta(\cdot\mid s^{goal})\oplus P^\perp_\xi(\cdot\mid s^{prop}_t) \tag{8}$$

其中算子 $\oplus$ 定义连续动作空间中的归一化残差相加。相应地，$z_t$ 的生成方式为

$$z_t=\mathrm{Normalize}(\Delta z_t+z^p_t) \tag{9}$$

其中 $\Delta z_t\sim\pi_\theta(\cdot\mid s^{goal})$，$z^p_t\sim P^\perp_\xi(\cdot\mid s^{prop})$。

与跟踪不同，自主拳击没有显式运动指令。因此残差策略以目标观测 $s^{goal}$ 为条件，该观测拼接了自我中心的攻防几何信息：从自身拳到对手躯干的相对向量，以及从对手拳到自身躯干的相对向量，全部旋转到自我根坐标系，使击打与威胁线索具备朝向不变性。为防止动作质量退化，我们用 AMP [6] 对预热进行正则化。判别器 $C$ 区分由 $(\pi_z,D_\psi)$ 产生的运动转移与 $\mathcal{D}_{motion}$ 中的参考片段，判别器特征包括局部关节旋转/速度与基座角速度。对真实转移施加梯度惩罚，判别器训练目标为

$$\arg\min_{C}\ \mathbb{E}_{d\in\mathcal{D}_{motion}}\left[(C(o^{disc}_t,o^{disc}_{t+1})-1)^2\right]+\mathbb{E}_{d\sim\pi_z,D_\psi}\left[(C(o^{disc}_t,o^{disc}_{t+1})+1)^2\right]+w_{gp}\mathbb{E}_{d\in\mathcal{D}_{motion}}\left[\|\nabla C(o^{disc}_t,o^{disc}_{t+1})\|^2\right] \tag{10}$$

并为策略提供风格奖励 $r_{style}$。因此学习目标是最大化期望回报：

$$\pi^\star_z=\arg\max_{\pi_z}\ \mathbb{E}_{\tau\sim(\pi_z,D_\psi)}\left[\sum_{t=0}^{T}\gamma^t R(s_t,z_t)\right] \tag{11}$$

其中 $R(s_t,z_t)=w_{task}\cdot r_{task}(s_t)+w_{style}\cdot r_{style}(s_t,s_{t+1})$，任务项进一步分解为朝向对齐、接近速度、门控击打距离与接触验证命中奖励。详细的预热塑形公式与数值权重见项目页。

### E. 隐空间神经虚拟自博弈

在行为预热阶段的基础上，我们采用**隐空间神经虚拟自博弈**（Latent-Space NFSP）驱动竞争性共同进化，如图 1（阶段 IIIb）所示。无约束运动空间中的标准虚拟自博弈常因人形机器人严重的物理脆弱性而崩溃。通过把竞争动力学严格实现在结构化隐动作空间 $\mathcal{Z}$ 而非原始运动空间上，我们的方法成功中和了这些不稳定性。

在该框架中，每个玩家由独立智能体控制，各自维护一个通过同步自博弈交互学习的**双策略系统**。智能体把经验记录到两个不同的缓冲区：存储近期转移的强化学习数据集 $\mathcal{D}_{RL}$，以及充当其历史最优响应行为水库的监督学习数据集 $\mathcal{D}_{SL}$。对每个智能体，我们用近端策略优化（PPO）[22] 在 $\mathcal{D}_{RL}$ 的样本上训练最优响应策略 $\pi^{RL}_z$。关键在于，由于隐流形 $\mathcal{Z}$ 在单位超球面上拓扑有界，这一强化学习优化天然避免了会导致灾难性遗忘与失衡的分布外物理动作。

同时，我们从 $\mathcal{D}_{SL}$ 通过监督学习训练平均策略 $\bar{\pi}_z$，以模仿历史最优响应的分布。在学习迭代 $k=1,\ldots,K$ 中，监督数据集按下式增量更新：

$$\mathcal{D}^k_{SL}=\mathcal{D}^{k-1}_{SL}\cup\mathcal{D}^k_{RL},\quad \forall k=1,\ldots,K \tag{12}$$

为使 $\bar{\pi}_z$ 代表完整行为历史而不仅是最新迭代，$\mathcal{D}_{SL}$ 以容量 $K$ 的水库采样维护：新经验 $n>K$ 以概率 $K/n$ 替换一个均匀选中的条目。连续隐空间上的动作选择遵循由**预期参数** $\eta\in[0,1)$ 控制的混合策略：

$$\sigma=\eta\cdot\bar{\pi}_z+(1-\eta)\cdot\pi^{RL}_z \tag{13}$$

隐动作按 $z_t\sim\sigma(\cdot\mid s^{prop}_t,s^{goal}_t)$ 采样。

在该表述下，$\pi^{RL}_z$ 表示对对手混合策略的近似最优响应，而 $\bar{\pi}_z$ 充当稳定的策略锚点。正如我们此前的理论分析所确立，有界隐参数化提供了分析所需的紧凑策略域。当 PPO 更新以有界误差逼近最优响应时，所得经验策略可被解释为解码器诱导隐博弈的近似均衡。**算法 1** 总结了完整训练循环。竞争阶段的奖励项及其权重见项目页。

**算法 1：隐空间神经虚拟自博弈（LS-NFSP）**

```
输入：双人零和博弈环境 M；预期参数 η∈[0,1]；时间跨度 T
输入：最优响应（RL）策略 {π^RL_{z,θ_i}}_{i∈{1,2}}；平均策略 {π̄_{z,φ_i}}_{i∈{1,2}}
输入：同策略缓冲区 {D^i_RL}_{i∈{1,2}}；水库缓冲区 {D^i_SL}_{i∈{1,2}}
1: for 迭代 k = 1, 2, ... do
2:     重置 M，观测 o^1_1, o^2_1
3:     for t = 1, 2, ..., T do
4:         for 每个玩家 i ∈ {1,2} do
5:             采样模式 m_i ~ Bernoulli(η)
6:             if m_i = 1 then
7:                 采样 z^i_t ~ π^RL_{z,θ_i}(·|o^i_t)
8:                 通过水库采样把 (o^i_t, z^i_t) 插入 D^i_SL
9:             else
10:                采样 z^i_t ~ π̄_{z,φ_i}(·|o^i_t)
11:            end if
12:        end for
13:        用 (z^1_t, z^2_t) 执行 M 一步；获得 (r^1_t, r^2_t) 与 (o^1_{t+1}, o^2_{t+1})
14:        for 每个玩家 i ∈ {1,2} do
15:            把 (o^i_t, z^i_t, r^i_t, o^i_{t+1}) 追加到 D^i_RL
16:        end for
17:    end for
18:    for 每个玩家 i ∈ {1,2} do
19:        在 D^i_RL 上用 PPO 更新 θ_i
20:        通过最小化 L_SL = E_{(o,z)~D^i_SL}[‖π̄_{z,φ_i}(o) − z‖²] 更新 φ_i
21:    end for
22: end for
23: 返回平均策略 {π̄_{z,φ_i}}_{i∈{1,2}}
```

## IV. 实验

### A. 实验设置

我们在 Isaac Lab [23] 中于单块 NVIDIA RTX 4090 GPU 上训练 29 自由度 Unitree G1 人形机器人 [10]，使用 4096 个并行环境、200 Hz 物理循环与 50 Hz 控制策略。策略共同进化在 32 维隐流形上进行。在最终 LS-NFSP 阶段，混合系数设为 $\eta=0.1$，每个智能体的策略水库容量 $K=10^6$ 样本，任务与 AMP 风格权重 $w_{task}=0.8$、$w_{style}=0.2$，先验系数 $\lambda_{prior}=0.001$。

为促进 sim-to-real 迁移，训练全程随机化接触材质、关节偏置、躯干质心以及间歇性外力推动。完整随机化范围见项目页。

我们把 RoboStriker 与分别隔离**对手建模**与**策略平均**、**课程设计**、**隐空间抽象**、**运动正则化**的基线进行比较。**Naive SP** 使用与我们相同的隐动作空间，但始终针对对手最新策略训练 [8, 9]；**Fictitious SP** 从历史对手策略中均匀采样 [14]，不学习显式平均策略网络；**PPO-Only** 用 PPO 针对固定对手训练 [22]；**Static-Target Specialist** 直接评估竞争性自博弈之前的预热策略；**SP w/o Warmup** 从零开始启动自博弈，以检验行为课程的作用。

为把隐动作抽象与运动先验正则化的作用分开，我们进一步比较四种受控变体。**RoboStriker w/o AMP** 在保留隐式分层的同时移除 AMP 风格奖励 [6]；**29-DoF Action-Space SP** 直接在学习解码器缺失的 29 自由度关节位置目标空间中执行自博弈；**29-DoF Action-Space + AMP** 在该原始动作空间基线上叠加与 RoboStriker 相同的 AMP 风格目标，但仍直接预测关节目标。连同完整 RoboStriker 模型，这些变体用于分辨性能增益究竟来自 AMP 行为正则化，还是来自通过所学隐运动流形结构化策略探索。

### B. 评估指标

我们从专业拳击与鲁棒机器人控制的原则出发，沿三个互补维度评估所有方法：

**战术熟练度。** **胜率（Win Rate）** 衡量总体优势，定义为评估回合的获胜百分比；当任何非足部身体部位触地时，该回合终止。**进攻命中率** $\eta_{hit}$ 是接触力超过 $F_{th}=10\ \mathrm{N}$ 的进攻尝试所占比例。**交战率（ER）** 是智能体同时维持有效击打距离 $d_t\in[0.5,1.2]\ \mathrm{m}$ 与朝向对齐 $\cos(\theta_t)>\tau_{face}=0.9$ 的时间占比，从而惩罚战术性回避。

**物理稳定性。** 物理稳定性通过**基座朝向稳定性（BOS）** 与**力矩平滑度（TS_τ）** 评估。BOS 以重力向量角偏差度量扰动下的直立姿态：$\mathrm{BOS}=\mathbb{E}[\exp\{-\|g_{base}-g_{world}\|_2\}]$，越高越好。TS_τ 以相邻力矩的平均变化量化高频电机振荡：$\mathrm{TS}_\tau=\mathbb{E}[\|\tau_t-\tau_{t-1}\|]$，越低越好。

**风格真实性。** 我们通过仿真快照定性评估类人性，检查滑步、反击、节奏性步法等关键拳击动作的存在，以及无约束强化学习策略典型的非自然或物理上不可维持姿态的缺失。

### C. 策略熟练度比较

基于第 IV-A 小节的基线，我们首先考察策略熟练度。如表 I 所示，RoboStriker 持续优于对比方法，对 Fictitious SP 胜率 **68.52%**、对 Naive SP **76.24%**、对 PPO-Only **84.47%**。除交叉对战胜率外，定量战术指标进一步印证其策略优势：RoboStriker 取得最高交战率 **0.824** 与最高进攻命中率 **0.685**。为原始动作空间基线加入 AMP 后，$\eta_{hit}$/ER 从 0.142/0.315 提升至 0.285/0.465，但 RoboStriker 仍在其交叉对战回合中赢下 **92.50%**，并达到 0.685/0.824，说明仅靠 AMP 无法解释隐空间控制的优势。图 2 子图 (b) 所展示的训练动力学揭示了各基线具体局限：缺少竞争性共同进化的 PPO-Only 表现出被动行为，交战率仅 0.495，且完全未能发现主动进攻策略，命中率只有 0.231；Naive SP 受非传递策略循环与灾难性遗忘驱动的严重周期性振荡困扰，交战率仅 0.580；Fictitious SP 虽缓解了振荡并把交战率提升到 0.650，但其平均策略收敛仍导致进攻命中率显著偏低（0.420）。通过在隐流形内整合神经虚拟自博弈，RoboStriker 成功中和了策略循环，并平滑收敛到最高战术熟练度。

**表 I：交叉对战与战术表现的胜率（%）**。每个胜率为行智能体对列智能体的胜率，在 20 轮评估、每轮 4096 场并行对战中取平均。进攻命中率（$\eta_{hit}$）与交战率（ER）均针对 Naive 自博弈（隐空间）评估。粗体为表中最优值。

| 方法 | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) | (9) | $\eta_{hit}$↑ | ER↑ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| (1) RoboStriker | – | 68.52 | 76.24 | 82.41 | 84.47 | 95.38 | 98.50 | 100.0 | 92.50 | **0.685±0.03** | **0.824±0.02** |
| (2) Fictitious SP | – | – | 62.35 | 71.84 | 75.16 | 92.11 | 96.18 | 99.42 | 88.14 | 0.420±0.03 | 0.650±0.04 |
| (3) Naive SP | – | – | – | 68.45 | 70.38 | 88.61 | 94.52 | 98.53 | 85.25 | 0.350±0.04 | 0.580±0.05 |
| (4) RoboStriker w/o AMP | – | – | – | – | 62.12 | 82.14 | 88.37 | 95.18 | 78.40 | 0.490±0.03 | 0.720±0.05 |
| (5) PPO-Only | – | – | – | – | – | 45.24 | 77.86 | 82.11 | 68.55 | 0.231±0.03 | 0.495±0.02 |
| (6) Static-Target Specialist | – | – | – | – | – | – | 60.33 | 85.58 | 62.18 | 0.210±0.04 | 0.450±0.06 |
| (7) RoboStriker w/o Warmup | – | – | – | – | – | – | – | 94.17 | 51.34 | 0.050±0.02 | 0.120±0.05 |
| (8) 29Dof Action-Space SP | – | – | – | – | – | – | – | – | 11.50 | 0.142±0.05 | 0.315±0.08 |
| (9) 29Dof Action-Space + AMP | – | – | – | – | – | – | – | – | – | 0.285±0.04 | 0.465±0.05 |

### D. 隐空间相对原始动作空间的优势

为把隐空间抽象的贡献与 AMP 正则化分开，我们比较 RoboStriker 与（加/不加 AMP 的）直接 29 自由度动作空间自博弈。如图 2 所示，无正则化的动作空间基线严重不稳定、进攻表现很差，而加入 AMP 后物理稳定性与战术指标都明显改善。

然而，29-DoF Action-Space + AMP 与 RoboStriker 之间仍存在明显差距。尽管 AMP 把运动正则到参考分布附近，策略探索仍在高维关节空间中直接进行。相反，RoboStriker 通过预训练解码器在结构化隐流形上开展探索，取得更高的稳定性、交战率、击打效率与力矩平滑度。这些结果表明 AMP 与隐空间抽象提供**互补**收益：AMP 改善运动规整性，而隐接口进一步结构化策略搜索空间。

> **图 2：综合性能评估。** 子图 (a)(b) 展示所有方法在基座稳定性与进攻命中率上的训练收敛。子图 (c)(d) 比较 RoboStriker 与（加/不加 AMP 的）直接 29-DoF 动作空间自博弈，隔离运动先验正则化与隐空间动作抽象对战技与物理稳定性的影响。阴影区域表示 5 个独立随机种子的标准差。

### E. 真实世界部署

除仿真之外，我们还验证所学策略可迁移到物理硬件。我们把仿真系数与实测物理属性对齐，并在所有训练阶段施加前述域随机化。参照 [1]，关节 PD 增益按惯量成比例设定，$k_{p,j}=I_j\omega^2$、$k_{d,j}=2I_j\zeta\omega$，自然频率 $\omega=10$、阻尼比 $\zeta=2$。我们在动捕环境中部署两台 Unitree G1 人形机器人 [10]：策略通过 ONNX Runtime 在机载 CPU 上以 50 Hz 运行，并经 ROS 2 [24] 协调。以 100 Hz 跟踪的骨盆标记提供机器人间空间关系；结合本体感知与正运动学，得到拳击策略所需的进攻目标观测。为避免力矩突变，两台机器人先以高刚度站立控制器初始化，再过渡到动态拳击。如图 3 所示，机器人在硬件上执行稳定、接触密集的动作，证实结构化隐流形把策略推理与物理不稳定性隔离开来。

> **图 3：RoboStriker 的真实世界验证。**
> **图 4：RoboStriker 与去除 AMP 版本在 MuJoCo 中的可视化。**

### F. 消融研究

我们通过表 I、图 2 与图 4 系统评估核心组件。首先，如表 I 所定量记录，移除 AMP 模块会严重削弱进攻效率，尽管交战率仍保持较高。此外，图 2 中的相应训练轨迹与图 4 中的仿真快照显示：没有 AMP 时，智能体虽积极接近对手，但击打动作杂乱，完全放弃标准防御姿态，呈现物理上不自然的体态。

相应地，为 29-DoF 动作空间基线加入 AMP 可改善其稳定性与动作质量，但无法恢复 RoboStriker 的性能。这些消融共同表明，AMP 正则化与隐空间抽象发挥互补作用：AMP 鼓励类人行为，隐解码器则为策略探索提供结构化的运动接口。

接下来我们验证行为预热课程。如图 2 所示，从零开始启动竞争性自博弈会因严重奖励稀疏而使战术表现近乎停滞在零附近。反之，Static-Target Specialist 能熟练击打被动目标，但面对动态对手则失效，RoboStriker 对其取得压倒性的 **95.38%** 胜率。因此，渐进式课程设计与 AMP 引导运动的协同，对于产出物理真实且策略占优的控制器不可或缺。

最后，我们评估隐维度在表达能力与多智能体稳定性之间的权衡。如表 II 所示，较低维度过度约束运动编码，产生僵硬行为与较高跟踪偏差（此处以**平均关键点位置误差 MPKPE** 量化）。扩展到 32 维显著改善运动学，而 64 维带来的物理增益微乎其微；在策略层面，64 维扩展会使连续搜索流形过于复杂，表示冗余拖慢收敛，把进攻命中率降至 0.520。最终，32 维空间在动作保真与紧凑流形之间取得最佳平衡，保证稳定的策略学习。

**表 II：隐维度消融研究**

| 隐维度 | MPKPE (mm) | 对 32 维的胜率 | $\eta_{hit}$ |
|---|---|---|---|
| 8 | 128.2±4.4 | 7.1% | 0.328±0.03 |
| 16 | 85.9±1.7 | 23.6% | 0.334±0.03 |
| **32（本文）** | **38.5±0.4** | – | **0.685±0.03** |
| 64 | 35.0±0.4 | 39.2% | 0.520±0.08 |

## V. 结论

为解决多智能体策略探索与人形机器人物理脆弱性之间的冲突，我们把竞争性拳击表述为**解码器诱导的隐空间零和马尔可夫博弈**，并在标准正则性与近似最优响应假设下给出近似 Nash 分析。我们通过 RoboStriker 实例化这一理论基础——一个分层框架，借助拓扑有界流形把策略推理与低层平衡控制解耦，并用隐空间神经虚拟自博弈驱动竞争性共同进化。包括交叉对战锦标赛与系统性消融在内的大量仿真评估表明，相较所评估的基线，物理稳定性与战术熟练度均有显著提升。

## 参考文献

（保留原文，未翻译）

[1] Q. Liao, T. E. Truong, X. Huang, G. Tevet, K. Sreenath, and C. K. Liu, *BeyondMimic: From motion tracking to versatile humanoid control via guided diffusion*, 2025. arXiv:2508.08241 [cs.RO].

[2] K. Yin et al., "UniTracker: Learning universal whole-body motion tracker for humanoid robots," arXiv preprint arXiv:2507.07356, 2025.

[3] W. Zeng et al., *Behavior foundation model for humanoid robots*, 2025. arXiv:2509.13780 [cs.RO].

[4] Z. Zhang et al., "Track any motions under any disturbances," arXiv preprint arXiv:2509.13833, 2025.

[5] X. B. Peng, P. Abbeel, S. Levine, and M. Van de Panne, "DeepMimic: Example-guided deep reinforcement learning of physics-based character skills," *ACM Transactions on Graphics (TOG)*, vol. 37, no. 4, pp. 1–14, 2018.

[6] X. B. Peng, Z. Ma, P. Abbeel, S. Levine, and A. Kanazawa, "AMP: Adversarial motion priors for stylized physics-based character control," *ACM Transactions on Graphics (TOG)*, vol. 40, no. 4, pp. 1–20, 2021.

[7] Z. Luo et al., "Universal humanoid motion representations for physics-based control," arXiv preprint arXiv:2310.04582, 2023.

[8] A. L. Samuel, "Some studies in machine learning using the game of checkers," *IBM Journal of Research and Development*, vol. 3, no. 3, pp. 210–229, 1959.

[9] D. Hernandez et al., "A generalized framework for self-play training," in *2019 IEEE Conference on Games (CoG)*, IEEE, 2019, pp. 1–8.

[10] Unitree, *Unitree G1 humanoid agent AI avatar*, 2024.

[11] Z. Chen, M. Ji, X. Cheng, X. Peng, X. B. Peng, and X. Wang, "GMT: General motion tracking for humanoid whole-body control," arXiv:2506.14770, 2025.

[12] X. B. Peng, Y. Guo, L. Halper, S. Levine, and S. Fidler, "ASE: Large-scale reusable adversarial skill embeddings for physically simulated characters," *ACM Transactions on Graphics (TOG)*, vol. 41, no. 4, pp. 1–17, 2022.

[13] C. Tessler, Y. Kasten, Y. Guo, S. Mannor, G. Chechik, and X. B. Peng, "CALM: Conditional adversarial latent models for directable virtual characters," in *ACM SIGGRAPH 2023 Conference Proceedings*, 2023, pp. 1–9.

[14] G. W. Brown, "Iterative solution of games by fictitious play," *Act. Anal. Prod Allocation*, vol. 13, no. 1, p. 374, 1951.

[15] J. Heinrich and D. Silver, "Deep reinforcement learning from self-play in imperfect-information games," arXiv preprint arXiv:1603.01121, 2016.

[16] J. Won, D. Gopinath, and J. Hodgins, "Control strategies for physically simulated characters performing two-player competitive sports," *ACM Trans. Graph.*, vol. 40, no. 4, Jul. 2021.

[17] Z. Zhang et al., *Learning athletic humanoid tennis skills from imperfect human motion data*, 2026. arXiv:2603.12686 [cs.RO].

[18] Xsens Technologies, *Xsens MVN: Inertial motion capture system*, Accessed: 2026-01-28, 2024.

[19] J. P. Araujo, Y. Ze, P. Xu, J. Wu, and C. K. Liu, *Retargeting matters: General motion retargeting for humanoid motion tracking*, 2025. arXiv:2510.02252 [cs.RO].

[20] S. Ross, G. J. Gordon, and J. A. Bagnell, *A reduction of imitation learning and structured prediction to no-regret online learning*, 2011. arXiv:1011.0686 [cs.LG].

[21] J. R. Hershey and P. A. Olsen, "Approximating the Kullback-Leibler divergence between Gaussian mixture models," in *2007 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP'07)*, IEEE, vol. 4, 2007, pp. IV–317.

[22] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, *Proximal policy optimization algorithms*, 2017. arXiv:1707.06347 [cs.LG].

[23] NVIDIA et al., *Isaac Lab: A GPU-accelerated simulation framework for multi-modal robot learning*, 2025. arXiv:2511.04831 [cs.RO].

[24] S. Macenski, T. Foote, B. Gerkey, C. Lalancette, and W. Woodall, "Robot operating system 2: Design, architecture, and uses in the wild," in *Science Robotics*, vol. 7, 2022.

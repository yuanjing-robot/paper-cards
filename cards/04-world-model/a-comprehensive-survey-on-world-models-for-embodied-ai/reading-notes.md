# 深度阅读：A Comprehensive Survey on World Models for Embodied AI

> 📄 对应论文：[A Comprehensive Survey on World Models for Embodied AI](https://arxiv.org/abs/2510.16732)
> 整理者：@WSB-666
> 最后更新：2026-10-31

---

> 💡 深度阅读与个人理解合并为一份。以下角度**按论文特点取舍**，不要求全部填写；建议至少写「核心方法」和「个人收获」。

## 1. 问题与动机

- 具身智能要求智能体不仅能感知和行动，还要预判「动作会如何改变未来世界状态」；世界模型就是这个内部模拟器，支持前向 rollout 和反事实 rollout（§I）。
- 领域现状是**术语和分类不统一**：早期世界模型源自 model-based RL（Ha & Schmidhuber 的 RNN 世界模型、Dreamer 系列），近年又被 Sora、V-JEPA 2 这类大规模生成模型拉向「通用环境模拟器」，两条脉络的「世界模型」含义并不相同。
- 已有综述要么按功能划分（理解 / 预测），要么按应用划分（主要聚焦自动驾驶），缺少一个能同时覆盖机器人、自动驾驶、通用视频的统一坐标系（§I）。
- 两个绕不开的技术矛盾：长时 rollout 的**误差累积**（coherence），以及粗糙/2D 表示不足以处理遮挡、物体恒存和几何规划（§I）。

## 2. 核心方法

- **形式化**：把交互建模为 POMDP，真实状态 `s_t` 不可观测，世界模型用一步滤波后验推断隐状态 `z_t`，再重构观测 `o_t`（§II-B）。三个部件是 dynamics prior `p(z_t|z_{t-1},a_{t-1})`、filtered posterior `q(z_t|z_{t-1},a_{t-1},o_t)`、reconstruction `p(o_t|z_t)`。
- **训练目标**：直接最大化似然不可解，用变分下界 ELBO；在马尔可夫分解下，ELBO = 逐帧重构项 − KL 正则项。这解释了现代世界模型为什么普遍采用「重构 + KL」范式（§II-B）。
- **三轴分类法**（本文的核心贡献，§III）：
  1. **功能（Functionality）**：Decision-Coupled（与特定控制目标绑定，样本效率高但泛化弱）vs General-Purpose（任务无关模拟器，迁移性好但与下游控制目标可能错位）。
  2. **时间建模（Temporal Modeling）**：Sequential Simulation & Inference（自回归逐步展开，支持闭环但误差累积、成本随 horizon 线性增长）vs Global Difference Prediction（并行预测未来，延迟低但闭环交互弱、易抹平局部动态）。
  3. **空间表示（Spatial Representation）**：Global Latent Vector（紧凑、实时，但丢细节）→ Token Feature Sequence（细粒度多模态，但吃数据和算力）→ Spatial Latent Grid（BEV/体素，保留局部拓扑，但内存大、分辨率有限）→ Decomposed Rendering Representation（NeRF/3DGS，几何一致、可对象级编辑，但训练贵、难处理快速拓扑变化）。
- **数据资源**分四类：仿真平台、交互基准、离线数据集、真机平台（Tab. III，§IV-A）。
- **评测指标**分三层：像素生成质量（FID、FVD、SSIM、PSNR、LPIPS、VBench）→ 状态级理解（mIoU、mAP、位移误差、Chamfer Distance）→ 任务表现（成功率、样本效率、奖励、碰撞率）（§IV-B）。

## 3. 关键结果

- **视频生成（nuScenes，Tab. IV）**：DrivePhysica 取得最低 FID **4.0**（FVD 38.1），MiLA 取得最低 FVD **14.9**（FID 4.1），两项分别代表当前视觉保真与时序一致性的最好水平（§V-A）。注意各方法分辨率差异很大，不能只看单一数字。
- **4D 占用预测（Occ3D-nuScenes，Tab. V）**：给定 2 s 历史占用，预测未来 3 s。结论有三点：① 用占用（occupancy）作为输入的方法整体优于纯相机输入；② 加入辅助监督 + GT ego 轨迹能缓解 2–3 s 的性能衰减；③ COME（Occ 输入 + GT ego）取得最佳平均 mIoU **34.23%**、平均 IoU **44.13%**（§V-B）。
- **控制任务（DMC，Tab. VI）**：以 64×64×3 像素输入、Episode Return（满分 1000）为指标。Dreamer 在 5M steps 下 20 任务均值 **823**；较新的方法用更少训练步数达到接近水平，说明数据效率在提升，但评测协议和任务子集不一致，跨方法泛化性仍难判定（§V-C）。
- **挑战总结（§VI）**：① 数据碎片化，缺统一大规模数据集，多智能体交互数据尤其少；② 指标偏像素保真（FID/FVD），忽视物理一致性与因果；③ 大模型推理成本与机载实时/能耗约束冲突；④ 长时一致性与误差累积仍是核心建模难点。

## 4. 批判性思考

- **综述本身不产生新方法**：三轴是「事后归类」，不是可证明最优的分类；边界案例不少，比如 EnerVerse 同时带 Dec + Seq + SLG 标签（Tab. I），说明真实系统常是混合体。
- **定量对比的公平性有限**：Tab. IV 的分辨率、Tab. VI 的训练步数与任务子集都不统一，文中也承认这一点；引用「SOTA」时容易被单个指标误导。
- **评测盲区**：FID/FVD 高不代表物理正确，一个外观逼真但物体穿模的 rollout 仍可能得高分；论文提出的「物理一致性指标」目前还没有公认实现。
- **偏自动驾驶**：数据资源和大量案例集中在 nuScenes / Occ3D，机械臂操作与室内导航的基准覆盖相对薄；多智能体、安全关键场景几乎是空白。
- **时效性**：参考文献已含 2026 年工作，领域迭代极快，分类表中的代表方法可能很快过时，需配合 AwesomeWorldModels 持续更新。

## 5. 个人收获

- 三轴其实是一套**选型 checklist**：做机器人项目时先问四个问题——要不要闭环控制（决定 Dec vs Gen）、能不能接受逐步自回归（决定 Seq vs Glo）、空间精度要求多高（决定 GLV/TFS/SLG/DRR）、机载延迟预算是多少。
- 「重构 + KL」的 ELBO 视角能统一理解 RSSM、Dreamer、TransDreamer 乃至部分视频扩散世界模型的训练目标，比逐个记模型更省力。
- 评测不能只看 FID/FVD；至少要补任务成功率、物理合理性（穿模/碰撞）和长时 rollout 的稳定性。
- 与已有卡片的连接：RT-2 / OpenVLA 属于「决策耦合 + Token 序列」的 VLA 路线，可作为本综述分类框架下的具体实例。

## 6. 延伸阅读（可选）

- 配套文献库：[AwesomeWorldModels](https://github.com/Li-Zn-H/AwesomeWorldModels)
- Dreamer 系列（RSSM 主线）：Dreamer、DreamerV2、DreamerV3
- 通用世界模型：V-JEPA / V-JEPA 2、Sora、Cosmos 系列
- 本仓库相关卡片：[RT-2](../03-embodied-llm/rt-2/)、[OpenVLA](../03-embodied-llm/openvla/)

---

> ✍️ **写作提示**
> - 引用数据标明出处（论文表 X / 图 Y）
> - 不编造信息，不确定的内容标注「待确认」
> - 不要复述论文原文，用自己的话写

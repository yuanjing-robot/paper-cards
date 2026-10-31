# A Comprehensive Survey on World Models for Embodied AI

> 📄 [论文原文](https://arxiv.org/abs/2510.16732) · 💻 [配套文献库](https://github.com/Li-Zn-H/AwesomeWorldModels) · 📝 [深度阅读](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Xinqing Li, Xin He, Le Zhang, Min Wu, Xiaoli Li, Yun Liu（南开大学 / 天津理工大学 / 电子科技大学 / A*STAR I2R / 新加坡科技设计大学），**arXiv 2025**（v1: 2025-10-19，本卡依据 v3: 2026-06-25）
> 领域标签: #世界模型 #具身智能 #综述 #视频生成 #VLA
> 首次笔记: @WSB-666 | 最后更新: 2026-10-31

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/2510.16732) |
| 代码 | _无官方模型代码_；配套 [AwesomeWorldModels](https://github.com/Li-Zn-H/AwesomeWorldModels) 是持续维护的文献清单 |
| 成员实现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

把具身世界模型按「决策耦合度 / 时间建模方式 / 空间表示」三个轴统一分类，横跨机器人、自动驾驶、通用视频三类场景梳理数据集与评测指标，并给出跨方法的定量对比；价值不在提出新模型，而在提供一张能对齐术语的领域地图，同时指出当前评测仍偏像素保真、缺少物理一致性指标。

---

## 📑 内容导航

| 模块 | 说明 | 文件 |
|------|------|------|
| 📝 深度阅读 | 精读 + 个人理解 | [reading-notes.md](reading-notes.md) |
| 🌐 论文翻译 | 全文中文翻译 | [translation.md](translation.md) |

---

## 📊 关键数据速览

| 指标 | 数值 | 备注 |
|------|------|------|
| 参数量 | 不适用（综述） | 被综述方法跨度很大：RSSM 类小模型 → 数十亿参数视频扩散 / VLM 骨干 |
| 训练数据 | 汇总而非单一统计 | Tab. III 按「仿真平台 / 交互基准 / 离线数据集 / 真机平台」四类整理；文中举例 OpenDV-2K、VideoMix22M、VisionMix163M（§VI-A） |
| 核心指标 | nuScenes 视频生成：DrivePhysica **FID 4.0**（视觉保真最优）、MiLA **FVD 14.9**（时序一致性最优）<br>Occ3D-nuScenes 4D 占用预测：COME-O + GT ego **平均 mIoU 34.23%**<br>DMC 控制：Dreamer **20 任务均值 823** @ 5M steps | 分别出自 Tab. IV、Tab. V、Tab. VI |
| 训练成本 | `-` | 综述未给统一成本口径；§VI-B 指出扩散/Transformer 的推理成本与机载实时约束冲突 |

---

## 💬 讨论与备注

- **版本**：v1 2025-10-19、v2 2025-11-29、v3 2026-06-25（本卡依据 v3）。PDF/HTML 均未标注正式发表会议或期刊，属 arXiv 预印本；若后续有 camera-ready 版，以正式版为准。
- **分类缩写**：表中 `Dec/Gen` = 决策耦合 / 通用；`Seq/Glo` = 序列仿真 / 全局差分预测；`GLV/TFS/SLG/DRR` = 全局隐向量 / Token 特征序列 / 空间隐网格 / 分解式渲染表示。
- **配套仓库定位**：AwesomeWorldModels 是文献索引，不是可运行实现；本卡「代码」一栏据此填写。
- **数字可比性警告**：Tab. IV 各方法的输出分辨率不同（如 128×192 到 576×1024），Tab. VI 的训练步数与任务子集也不统一；跨表、跨方法的数值不能直接横向比较，只能在同一张表内看相对强弱。
- **覆盖时间**：参考文献含 2026 年工作（如 Cosmos 3、V-JEPA 2.1、DINO-Foresight），属快速更新领域，阅读时注意版本。

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「深度阅读」
> - 想看读后的思考与收获？看「深度阅读」的个人收获部分

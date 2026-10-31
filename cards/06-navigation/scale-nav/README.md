# ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation

> 📄 [论文原文](https://arxiv.org/abs/2610.25690) · 📝 [深度阅读](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Yihui Yang, Yuanhong Yu, Jiawei Wang, Zhongrui Yu, Jia Shi, Kun Zhan, Ruizhen Hu, Xiaowei Zhou, Yu Liu, Sida Peng
> **arXiv 预印本，2026**（此处不代表已被会议或期刊录用）
> 领域标签：#具身导航 #世界动作模型 #视频预训练
> 首次笔记：@cisyam555 | 最后更新：2026-10-31

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/2610.25690) |
| PDF | [完整论文](https://arxiv.org/pdf/2610.25690) |
| 项目主页 | [ScaleNav](https://zju3dv.github.io/ScaleNav/) |
| 代码 | 请从项目主页查看官方发布情况，独立链接待补充 |
| 成员实现代码 | 暂无 |

## 🎯 一句话概括

ScaleNav 先用不带机器人动作标签的互联网第一视角视频学习语言目标引导的视觉变化，再通过带动作标签的仿真数据学习动作生成，实现对初始视野内目标的局部导航。

## 📑 内容导航

| 模块 | 说明 | 文件 |
|------|------|------|
| 深度阅读 | 方法、实验、局限与学习记录 | [reading-notes.md](reading-notes.md) |
| 论文翻译 | 摘要、正文与附录中文译稿，待人工复核；参考文献保留原文 | [translation.md](translation.md) |

## 📊 关键数据速览

以下为论文报告的结果，尚未自行复现实验。

| 指标 | 数值 | 来源与说明 |
|------|------|------|
| 视频基础模型 | Wan2.2-TI2V-5B | §3.2 |
| 互联网导航视频片段 | 18.2K，约 18,200 段 | §3.3；视频经过筛选并配有导航指令 |
| 带动作标签的仿真轨迹 | 约 2.6K，约 2,600 条 | §3.3；来自 650 个场景 |
| Short-Horizon OVON 成功率 | 86.5% | 表 1；作者采用单视图适配版本 |
| HabitatGS-LN 成功率 | 94.9% | 表 1；作者构建的基准 |
| 真机总体成功率 | 83.3% | 表 3；大厅、休息区、办公室，每种方法共 60 次试验 |

## 💬 讨论与备注

研究任务是语言条件局部导航：目标在初始视野中可见。上述结果不能直接推广为任意环境下的长距离导航能力。

本卡片借助 AI 整理并对照论文原文核对；个人理解部分待整理者补充，不表示已经完成全文精读或代码复现。

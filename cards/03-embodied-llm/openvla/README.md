# OpenVLA: An Open-Source Vision-Language-Action Model

> 📄 [论文原文](https://arxiv.org/abs/2406.09246) · 💻 [代码](https://github.com/openvla/openvla) · 📝 [深度阅读](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Kim, Pertsch, Karamcheti et al.（前三位标注同等贡献）, **CoRL 2024**
> 领域标签: #VLA #具身大模型 #开源 #机器人操作
> 首次笔记: @kingdream-cn | 最后更新: 2026-10-30

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/2406.09246)（底本 **v3**，2024-09-05） |
| 代码 | [GitHub](https://github.com/openvla/openvla) |
| 成员实现代码 | _待补充_ |
| 项目主页 | [openvla.github.io](https://openvla.github.io/)（arXiv 摘要页 Comments 行标注） |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

_用一句话说清这篇论文做了什么、核心价值是什么_

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
| 参数量 | - | 基础模型大小 |
| 训练数据 | - | 预训练数据量 |
| 核心指标 | - | 在 xxx 上达到 xx |
| 训练成本 | - | GPU 时 / 美元 |

---

## 💬 讨论与备注

- **版本依据**：本卡以 **arXiv:2406.09246v3**（2024-09-05）为底本。标题栏的「CoRL 2024」与 PMLR 卷页 **270:2679-2713** 出自 PMLR 页面（`proceedings.mlr.press/v270/kim25c.html`），属**外部信息**；arXiv 摘要页的 Comments 行只写 `Website: https://openvla.github.io/`，未标会议。待 PDF 到手后核对首页是否自标会议，若 camera-ready 版数据有变动，以正式版为准。
- **作者排序**：前三位 Moo Jin Kim、Karl Pertsch、Siddharth Karamcheti 标注同等贡献，**按贡献排而非字母序**（与 RT-2 卡的情况相反），因此 `Kim et al.` 可作主导作者理解。
- **与 RT-2 卡的承接关系**：RT-2 §5 点名「可用的通用 VLM 底座数量极少且基本闭源」，OpenVLA 正是这条局限的开源回应；两卡通读。
- **速览数据暂空**：下表数值待原文核对后填入，按工作区红线（每个数字带出处）**不预先估算**。

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「深度阅读」
> - 想看读后的思考与收获？看「深度阅读」的个人收获部分

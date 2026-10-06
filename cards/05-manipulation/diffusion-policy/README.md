# Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

> 📄 [论文原文](https://arxiv.org/abs/2303.04137) · 💻 [官方代码](https://github.com/real-stanford/diffusion_policy) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Cheng Chi, Siyuan Feng, Yilun Du et al., **RSS 2023**
> 领域标签: #模仿学习 #扩散模型 #操作
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/2303.04137) |
| 官方代码 | [GitHub](https://github.com/real-stanford/diffusion_policy) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

把机器人策略表示成动作序列上的扩散模型，能表达多峰动作分布并稳定闭环控制，在大量仿真与真实任务上大幅超越此前基线。

---

## 📑 内容导航

| 模块 | 说明 | 文件 |
|------|------|------|
| 📝 精读笔记 | 精读 + 个人理解（角度按论文特点灵活取舍） | [reading-notes.md](reading-notes.md) |
| 🌐 论文翻译 | 全文中文翻译 | [translation.md](translation.md) |

---

## 📊 关键数据速览

| 指标 | 数值 | 备注 |
|------|------|------|
| 参数量 | CNN/Transformer 变体 | 约数百 M |
| 训练数据 | 50 条演示/任务 | 行为克隆设定 |
| 核心指标 | 15 个仿真任务平均 +46.9% | 真实任务也全面领先 |
| 训练成本 | 单机多卡可复现 | 论文报告 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分

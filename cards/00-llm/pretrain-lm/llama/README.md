# LLaMA: Open and Efficient Foundation Language Models

> 📄 [论文原文](https://arxiv.org/abs/2302.13971) · 💻 [官方代码（权重申请）](https://github.com/meta-llama/llama) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, et al., **Meta AI, arXiv 2023**
> 领域标签: #开源大模型 #高效训练 #Transformer
> 首次笔记: @zeng417 | 最后更新: 2026-10-05

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/2302.13971) |
| 官方代码 | [GitHub (meta-llama/llama)](https://github.com/meta-llama/llama) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

LLaMA 证明「更小的模型 + 更多高质量公开数据」能追平甚至超越更大的闭源模型（13B 在多数基准上超过 GPT-3 175B），其开源权重直接引爆了开源大模型生态。

---

## 📑 内容导航

| 模块 | 说明 | 文件 |
|------|------|------|
| 📝 精读笔记 | 精读 + 个人理解（角度灵活取舍） | [reading-notes.md](reading-notes.md) |
| 🌐 论文翻译 | 全文中文翻译 | [translation.md](translation.md) |

---

## 📊 关键数据速览

| 指标 | 数值 | 备注 |
|------|------|------|
| 参数量 | 7B / 13B / 33B / 65B | 标准 Transformer decoder + 若干工程优化 |
| 训练数据 | 约 1.0~1.4T tokens | 全部公开数据：C4、GitHub、维基、书籍、ArXiv、StackExchange |
| 核心指标 | 13B 多数基准 > GPT-3 175B；65B MMLU 63.4 | 论文报告 |
| 训练成本 | 65B：2048 块 A100 × 约 21 天 | 与同等性能闭源模型相比明显省钱 |

---

## 💬 讨论与备注

- 读这篇重点看**工程配方**（RMSNorm、SwiGLU、RoPE），都是今天开源模型的标配
- 后续版本：LLaMA 2（商用许可 + 对话版）、LLaMA 3，建议按时间线对比读
- 权重泄露后社区微调生态（Alpaca、Vicuna 等）是理解"开源飞轮"的好案例

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分

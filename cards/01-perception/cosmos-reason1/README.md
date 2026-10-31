# Cosmos-Reason1: From Physical Common Sense To Embodied Reasoning

> 📄 [论文原文](https://arxiv.org/abs/2503.15558) · 💻 [代码与模型](https://github.com/nvidia-cosmos/cosmos-reason1) · 📝 [深度阅读](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> NVIDIA（作者列表见论文附录 C），**arXiv preprint** 2025
> 领域标签: #物理AI #多模态大模型 #具身推理 #长思维链 #强化学习
> 首次笔记: @VoVL773 | 最后更新: 2026-10-31

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv:2503.15558](https://arxiv.org/abs/2503.15558)（[HTML](https://arxiv.org/html/2503.15558v3) / [PDF](https://arxiv.org/pdf/2503.15558)） |
| 代码与权重 | [nvidia-cosmos/cosmos-reason1](https://github.com/nvidia-cosmos/cosmos-reason1)（NVIDIA Open Model License） |
| 成员实现代码 | _待补充_ |
| 项目主页 | _待补充_（论文以 GitHub 仓库作为发布入口） |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

NVIDIA 用两套本体论（物理常识的「空间 / 时间 / 基础物理」三分法，以及具身推理的「4 种能力 × 5 类智能体」二维表）把「物理世界理解」拆成可标注、可评测的题目，再以约 400 万条视频-文本标注做 Physical AI SFT、用基于规则可验证奖励的 GRPO 做 Physical AI RL，得到 7B 与 56B 两个能通过长思维链输出具身决策的多模态模型。

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
| 参数量 | **7B**：dense Transformer，基于 Qwen2.5-VL<br>**56B**：Hybrid Mamba-MLP-Transformer，InternViT-300M-V2.5 + Nemotron-H | 架构与配置见论文 §3、Table 3 |
| 训练数据 | SFT：**1.81M** understanding + **1.93M** reasoning ≈ **3.74M**（论文正文称「约 4M」）<br>RL：**30,304** 道 MCQ | SFT 见 Table 4；RL 见 Table 5；数据来自 BridgeData V2、RoboVQA、AgiBot、HoloAssist、AV 等 |
| 核心指标 | 物理常识 Avg：**54.3**（7B，+6.9）/ **60.2**（56B，+2.0）<br>具身推理 Avg：**61.8**（7B，+11.0）/ **63.7**（56B，+10.2）<br>直觉物理 Avg：**74.5 → 81.5**（7B，SFT → +RL） | Table 7 / Table 8 / Table 10；括号内为相对各自 backbone 的提升 |
| 训练成本 | 论文未披露 GPU 时数或费用 | 仅给出迭代数：7B 12.5K iter；56B 30K + 20K iter（§7.1） |

---

## 💬 讨论与备注

- **版本依据**：本卡片以 **arXiv v3**（2025-05-19）为底本；v1 为 2025-03-18。论文未标注会议或期刊，按 preprint 引用。
- **「约 4M」的口径**：正文 §1 称整理约 4M 条视频-文本标注；Table 4 两行合计为 1.81M（understanding）+ 1.93M（reasoning）= 3.74M。引用时建议写「约 3.7–4M」，并注明出处。
- **MCQ 数量的正文/表格差异**：§5.1.1 称用 1.2M clips 构造约 **2.4M** understanding MCQ，而 Table 4 记 **1.2M**。可能是「生成量 vs 入库量」的差别，论文未解释；本卡片表格一律采用 Table 4 数值。
- **「超过 10%」的适用范围**：结论称 SFT 在两个基准上提升「超过 10%」，但 Table 7 的常识提升只有 +6.9（7B）与 +2.0（56B）；真正超过 10% 的是具身推理（+11.0 / +10.2）。引用结论句时要加限定，详见深度阅读 §4。
- **「略超 o1」仅限物理常识**：Table 7 中 56B 为 60.2，o1 为 59.9；Table 8 具身推理则是 63.7 对 54.5，领先明显。不要把「略超」推广到全部基准。
- **56B 不是纯 Transformer**：其 LLM backbone 为 Nemotron-H 的 Hybrid Mamba-MLP-Transformer（118 层），视觉编码器为 InternViT-300M-V2.5；7B 才是 dense Transformer（28 层）。
- **评测只算最终答案**：论文明确说基准只测最终答案正确率，思维链质量评估留作未来工作（§6）。因此分数不能直接等同于「推理过程可靠」。
- **模型输出的是自然语言决策**，不是底层关节/末端动作，也未做真机闭环执行；把它当高层推理器/规划器更准确。

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「深度阅读」
> - 想看读后的思考与收获？看「深度阅读」的个人收获部分

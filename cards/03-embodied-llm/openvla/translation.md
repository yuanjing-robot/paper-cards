# 论文翻译

> 📄 对应论文原文：[OpenVLA](https://arxiv.org/abs/2406.09246)
> 翻译者：@kingdream-cn
> 最后更新：2026-10-30

---

## 📝 翻译说明

- 翻译范围：**正文全译**（摘要 + §1–§6，含图表注）＝ PDF p1–11；**附录按要点概述**＝ p21–37。参考文献 p12–20 不译
- 底本：arXiv:2406.09246**v3**（v1 2024-06-13 / v2 09-04 / v3 09-05，共 37 页）。下文页码均指 **PDF 物理页号**，行号指逐页 `pdftotext -layout` 的输出行，可用 `sed -n '7p' pages/p05.txt` 复现
- 翻译原则：直译为主，专业术语保留英文
- 术语表每条的「出现位置」与原文定义句都经过逐页 grep 核对；原文未定义的，标注「原文未下定义」而不代为补定义

| 英文 | 中文 | 备注 |
|------|------|------|
| vision-language-action model (VLA) | 视觉-语言-动作模型 | 类别名沿用 RT-2（Brohan et al. [7]），本文未重新定义，§2 p3 L43 只写「such models are often referred to as vision-language-action models」。缩写 VLA 全文保留英文（标题 p1 L2、摘要 p1 L48 与 L53、Fig 1 注 p1 L38、§3 开篇 p4 L31、§6 p11 L20） |
| Prismatic-7B VLM | Prismatic-7B 视觉-语言模型 | 本文选定的主干，名称保留英文。构成：600M 参数视觉编码器 + 小型 2 层 MLP projector + 7B 参数 Llama 2 语言主干（§3.1 p4 L46–48） |
| fused vision encoder / DinoSigLIP | 融合视觉编码器 | 视觉塔由预训练 SigLIP [79] 与 DinoV2 [25] 两部分组成，图像 patch 分别过两个编码器，输出特征向量**按通道拼接**（concatenated channel-wise，§3.1 p4 L49–50）；p6 L13 写作 `fused SigLIP-DinoV2 backbones`。**简称 `DinoSigLIP` 全文只出现 1 次**（§5.4 p10 L60）。大小写原文不统一：摘要 p1 L55 作 `DINOv2`，正文作 `DinoV2` |
| action tokenization / 256 bins | 动作 token 化 / 256 个 bin | token、bin 均不译（译「箱」歧义大）。每个动作维度各自离散为 256 档之一（§3.2 p5 L7–8）；bin 宽按训练数据该维动作 **1st 与 99th 分位**之间均分（p5 L9）。改分位是为避开离群动作把区间撑大、削弱离散粒度（p5 L10–12，原文明说这是对 Brohan et al. min-max 的替换）。离散化本身沿用 Brohan et al. [7]，非本文首创 |
| overwrite the 256 least used tokens | 覆盖 256 个最低频 token | Llama tokenizer 只预留 100 个 special token，放不下 256 个动作 token，于是直接用动作 token 覆盖词表中「使用最少的 256 个」（即最后 256 个）token（§3.2 p5 L15–18）。与 RT-2 里 PaLM-E 那条路线同源，**不是 OpenVLA 的新做法**，卡片要标「沿用」 |
| next-token prediction, cross-entropy on action tokens only | 下一 token 预测；损失只落在动作 token 上 | §3.2 p5 L19–20。这是本文自己的限定表述；RT-2 全文（p1–19）grep 不到 `cross-entropy`/`loss`/`mixed objective`，**两者不可做损失函数层面的对比**，别写成「与 RT-2 不同」 |
| data mixture | 数据配比 | §3.3 p5 L35（沿用 Octo [5] 的启发式配比）、p5 L43 与 Table 3 脚注 6（DROID 在最后三分之一训练移出并把权重重新分配到其余数据集）、§5.4 p10 L59 脚注 4（§5.3/§5.4 用的是更小配比）。别与「数据集条数」混译 |
| parameter-efficient fine-tuning (PEFT) | 参数高效微调 | §5.3 标题 p10 L1。本文比较 5 种：full fine-tuning / last layer only / frozen vision / sandwich / LoRA。定义写在 Table 1 左栏，与图注**交错排版**，整段抽读极易串行（p10 L8–21） |
| sandwich fine-tuning | 三明治微调（保留英文原词） | **本文自定义口径**：解冻视觉编码器、token embedding 矩阵与最后一层（p10 L18–20），未给文献出处。译时保留英文并加注，不要按外部同名术语的原始定义改写 |
| LoRA | LoRA（低秩适配，不译） | Hu et al. [26]，施加于模型所有线性层（p10 L23）；只训 **1.4%** 参数即匹配全量微调（p10 L30–32、Table 1）；rank 对性能影响可忽略，推荐默认 **r = 32**（p10 L33）；单张 A100 **10–15 小时**，较全量微调省 **8 倍**算力（p10 L34–35；对比基线是 p10 L2–3 的「8 张 A100、每任务 5–15 小时」） |
| quantization（bfloat16 / int8 / int4） | 量化 | §5.4 标题 p10 L36，正文 p10 L53–p11 L19；Table 2 数值 p10 L41–43，图注 p10 L45–52（**8 个代表性 BridgeData V2 任务、每方法 80 rollouts，明细见 Table 5**）。**推理侧的坑**：8-bit 在多数 GPU 上反而更慢（量化算子开销），4-bit 更快（p11 L9–11）；A5000 上只有非阻塞 **5 Hz** 控制器能吃下这个延迟（p11 L13–15 及其脚注 5）。**注意显存原文有三个值**：bfloat16 在 §3.5 p6 L39 作 `15GB`、§5.4 p10 L56 作 `only 16GB`、Table 2 p10 L41 作 `16.8 GB` — 译时原样保留并加注，不要替它统一 |
| out-of-the-box | 开箱即用 | 原文自己**加引号**使用（§5.1 p7 L55、§5.2 p8 L55、p10 L61），也有不加引号的（p3 L28、§6 p11 L21）。首次出现建议「开箱即用（out-of-the-box）」，后文统一中文 |
| co-fine-tuning / co-training | 联合微调 / 联合训练 | **两个词在本文各只出现 1 次，且都不是描述 OpenVLA**：`co-fine-tuned`（p8 L44）说的是 RT-2-X；`co-training`（p11 L38）是 §6 列出的未做设计问题。RT-2 卡片里这个词是核心方法，两篇同名不同命，翻译时别顺手上岗成 OpenVLA 的做法 |
| action chunking | 动作分块 | 仅作改进方向出现：§6 p11 L32（提高吞吐量的手段之一）；p9 L60/70 说明 OpenVLA 推理不用分块、只出单步相对位置控制。**别译成已实现特性** |
| proprioceptive input | 本体感知状态输入（proprio 保留英文） | §6 p11 L26 明写当前不支持；p9 L64/69 交代对比用的 Diffusion Policy 完整版带图像 + proprio 两步历史、匹配版无 proprio |
| embodiment / cross-embodiment | 具身形态 / 跨具身形态 | `cross-embodiment` 正文**仅 1 次**（§6 p11 L21；另 1 次在参考文献 p17 L14，属被引论文标题，不算）。正文实际说法是 `robot embodiments`（§5.1 p7 L56、§5.2 p9 L34、p2 L45、§3.3 p5 L25） |
| rollout | rollout（一次实机执行） | 机器人语境通行不译。分母随表变：Table 1 图注 p10 L9 是 33 rollouts、Fig 3 图注 p7 L34 是 170 rollouts、Table 2 图注 p10 L51 是 80 rollouts，不能跨表直接比数值 |

---

## 📖 摘要 (Abstract)

_摘要全文翻译_

---

## 🔑 引言 (Introduction)

_引言全文翻译_

---

## 🧠 相关工作 (Related Work)

_相关工作全文翻译_

---

## 📐 方法 (Method)

_方法全文翻译_

---

## 📊 实验 (Experiments)

_实验全文翻译_

---

## 💡 结论 (Conclusion)

_结论全文翻译_

---

## 📎 附录 (Appendix)

_附录全文翻译（如有）_

---

> ⚠️ **翻译仅供学习参考，如有歧义以原文为准。**

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
- 进度：**摘要 + §1 已译**（含 Figure 1 图注与 §1 脚注 1，2026-10-30）；§2–§6 分批追加进本 PR，每批一条 `docs:` commit
- 原文自己用词不统一的地方，译文照各处原样保留、不替它统一：`970k` 三处分别译作片段（episodes）/ 演示（demonstrations）/ 轨迹（trajectories）；数据集名 `Open X-Embodiment` 与 `Open-X Embodiment` 并存；视觉编码器 `DINOv2` 与 `DinoV2` 并存

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

> Figure 1 | 我们提出 OpenVLA，一个 7B 参数的开源视觉-语言-动作模型（vision-language-action model，VLA），在来自 Open X-Embodiment 数据集 [1] 的 970k 个机器人片段（episodes）上训练。OpenVLA 为通用机器人操作策略树立了新的最优水平（state of the art）。它支持开箱即用（out of the box）地控制多种机器人具身形态，并可通过参数高效微调（parameter-efficient fine-tuning）快速适配到新的机器人领域。OpenVLA 的检查点与 PyTorch 训练流水线完全开源，模型可从 HuggingFace 下载并微调。

在大规模互联网视觉-语言数据与多样化机器人演示的组合上预训练的大型策略，有潜力改变我们教机器人新技能的方式：与其从零训练新行为，我们可以微调这类视觉-语言-动作（VLA）模型，以获得用于视觉运动控制的鲁棒、可泛化的策略。然而，VLA 在机器人领域的广泛采用一直颇具挑战，因为 1) 现有 VLA 大多是封闭的、公众无法获取，2) 先前工作未能探索高效微调 VLA 以用于新任务的方法，而这是采用的关键一环。为应对这些挑战，我们提出 OpenVLA，一个 7B 参数的开源 VLA，在 970k 条真实世界机器人演示（demonstrations）的多样集合上训练。OpenVLA 构建在一个 Llama 2 语言模型之上，并结合一个视觉编码器，该编码器融合来自 DINOv2 与 SigLIP 的预训练特征。作为新增数据多样性与新模型组件的产物，OpenVLA 在通用操作上展现出强结果，在跨 29 个任务与多种机器人具身形态的绝对任务成功率上，以 16.5% 超过 RT-2-X (55B) 这类封闭模型，且参数量少 7x。我们进一步表明，我们能够有效地针对新场景微调 OpenVLA，在多物体、多任务环境中取得尤其强的泛化结果与很强的语言 grounding 能力，并相较 Diffusion Policy 这类表达力强的从零模仿学习方法高出 20.4%。我们还探索计算效率；作为一项单独的贡献，我们表明 OpenVLA 可以通过现代低秩适配（low-rank adaptation）方法在消费级 GPU 上微调，并通过量化（quantization）高效服务，而不损失下游成功率。最后，我们发布模型检查点、微调 notebook，以及我们的 PyTorch 代码库，内置支持在 Open X-Embodiment 数据集上大规模训练 VLA。

---

## 1 引言

学习得到的机器人操作策略的一个关键弱点，是它们无法泛化到训练数据之外：虽然针对单项技能或语言指令训练的现有策略有能力把行为外推到新的初始条件（如物体位置或光照）[2, 3]，但它们对场景干扰物（distractor）或新物体缺乏鲁棒性 [4, 5]，并且难以执行未见过的任务指令 [6, 7]。然而在机器人之外，视觉与语言领域现有的基础模型（foundation model），如 CLIP [8]、SigLIP [9] 与 Llama 2 [10]，能够实现这类泛化乃至更多，这源于其互联网规模预训练数据集所捕获的先验。尽管为机器人复现这一预训练规模仍是一个未解决的挑战——即便最大的机器人操作数据集 [1, 11] 也只有 100K 到 1M 个样本——这种不平衡提示了一个机会：把视觉与语言领域现有的基础模型用作核心构件，来训练能够泛化到训练数据之外的物体、场景与任务的机器人策略。

朝着这一目标，已有工作探索了把预训练的语言模型与视觉-语言模型整合用于机器人表征学习 [12–14]，以及作为模块化系统中任务规划与执行的组件 [15, 16]。更近期，它们被用于直接学习用于控制的视觉-语言-动作模型 [VLAs; 1, 7, 17, 18]。VLA 提供了把预训练的视觉-语言基础模型用于机器人的一种直接实例化方式，即直接微调 PaLI [19, 20] 这类以视觉为条件的语言模型（VLM），使其生成机器人控制动作。通过建立在互联网规模数据上训练的强基础模型之上，RT-2 [7] 这类 VLA 展现出令人印象深刻的鲁棒性结果，以及泛化到新物体与新任务的能力，为通用机器人策略树立了新的标准。然而，有两个关键原因阻碍了现有 VLA 的广泛使用：1) 当前模型 [1, 7, 17, 18] 是封闭的，对模型架构、训练流程与数据配比（data mixture）的可见性有限，2) 现有工作没有提供把 VLA 部署并适配到新机器人、新环境与新任务的最佳实践——尤其是在通用硬件（例如消费级 GPU）上。我们认为，为了发展一个面向未来研究与开发的丰富基础，机器人领域需要开源、通用的 VLA，它们支持有效的微调与适配，类似于围绕开源语言模型 [21–24] 的现有生态。

为此，我们提出 OpenVLA，一个 7B 参数的开源 VLA，它为通用机器人操作策略确立了新的最优水平¹。OpenVLA 由一个预训练的、以视觉为条件的语言模型主干构成，该主干捕获多种粒度的视觉特征，并在来自 Open-X Embodiment [1] 数据集的大规模、多样化的 970k 条机器人操作轨迹（trajectories）上微调——该数据集覆盖广泛的机器人具身形态、任务与场景。作为数据多样性提升与新模型组件的产物，OpenVLA 在 WidowX 与 Google Robot 具身形态的 29 个评测任务上，以 16.5% 的绝对成功率超过 55B 参数的 RT-2-X 模型 [1, 7]——此前的 state-of-the-art VLA。我们另外研究了面向 VLA 的高效微调策略，这是一项先前工作未探索的新贡献，覆盖 7 个多样化操作任务，行为从物体抓放到擦拭桌面。我们发现，微调后的 OpenVLA 策略明显优于微调后的预训练策略（如 Octo [5]）。与使用扩散策略 [3] 的从零模仿学习相比，微调后的 OpenVLA 在涉及把语言 grounding 到行为、且处于多物体多任务环境的任务上展现出显著提升。承接这些结果，我们首次证明了利用低秩适配 [LoRA; 26] 与模型量化 [27] 的计算高效微调方法的有效性，使 OpenVLA 模型能够在消费级 GPU 而非大型服务器节点上适配，同时不牺牲性能。作为最后一项贡献，我们开源了所有模型、部署与微调 notebook，以及用于大规模训练 VLA 的 OpenVLA 代码库，希望这些资源能够促成未来探索并适配 VLA 用于机器人的工作。

> 脚注 1：OpenVLA 使用多个预训练模型组件：SigLIP [9] 与 DinoV2 [25] 视觉编码器，以及一个 Llama 2 [10] 语言模型主干。对这三个模型而言，权重是开放的，但其训练数据与代码不开放。我们发布训练数据、代码与模型权重，以便在这些组件之上复现 OpenVLA。

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

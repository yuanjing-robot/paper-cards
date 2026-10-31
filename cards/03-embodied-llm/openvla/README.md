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
| 项目主页 | [openvla.github.io](https://openvla.github.io/)（arXiv 摘要页 Comments 行标注） |
| 解读视频 | [B 站 · 具身智能领域的里程碑：OpenVLA讲解](https://www.bilibili.com/video/BV1HAkZYLEZb)（UP：NobleAI，2024-12-25，42:46） |

---

## 🎯 一句话概括

RT-2 说「开放底座太少、都闭着」，OpenVLA 就是把这句话兑现成实物：7B 参数、Prismatic 主干、970k 机器人演示训出来的跨具身策略，代码、权重、数据配比和 PyTorch 训练框架全放开，还接进了 HuggingFace 的 AutoModel。做法上不新奇——动作离散成 token、跟 VLM 一样做下一 token 预测——真正下功夫的是把微调成本压到单卡级（LoRA 只训 1.4% 参数、一张 A100 十来个钟头）和把推理显存压到 7 GB（int4，成功率与 bfloat16 打平）。评测读数在 BridgeData V2 是 70.6%、Google robot 是 85.0%，摘要口径比闭源 55B 的 RT-2-X 高 16.5 个绝对百分点、参数少 7 倍；但原文自己承认 semantic generalization 那一类还是 RT-2-X 更高，所以不是全面反超。

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
| 参数量 | **7B** | 主干是 Prismatic-7B：600M 参数视觉编码器（SigLIP 与 DinoV2 分别编码、特征按通道拼接）+ 2 层 MLP projector + Llama 2 7B（§3.1 p4 L46–50）。对照列：RT-1-X **35M**、Octo **93M**（§5.1 p8 L4），§5.4 p10 L53 另称 Octo `<100M`；RT-2-X **55B**（摘要 p1 L58）。摘要称比 RT-2-X 少 **7x** 参数（p1 L58–59）——倍数照原文写，不自算 |
| 训练数据 | **970k** 机器人演示（筛选后） | 源头是 Open X-Embodiment 全量 70+ 个数据集、2M+ 条轨迹（§3.3 p5），最终配比取 27 个数据集（表 3，p21）。DROID 以 10% 权重加入，最后三分之一训练时被移除、权重重新分配给其余数据集——这句只在表 3 脚注 6 里，正文没写。对比句：RT-2-X 是 **350k**（§5.1 p8 L50）。注意 970k 与 2M+ 不是一个层级，别写成「在 2M 条 OpenX 上训练」；原文 p8 L50 把 970k 叫 trajectories，别处叫 episodes / demonstrations |
| 核心指标 | BridgeData V2（17 任务 × 10 trials = **170 rollouts**）平均成功率：**OpenVLA 70.6±3.2%** / RT-2-X 50.6±3.5% / Octo 20.0±2.6% / RT-1-X 18.5±2.7%（表 4，p26 L34）<br>Google robot（12 任务 × 5 trials = **60 rollouts**）：**OpenVLA 85.0±4.6%** / RT-2-X 78.3±5.4% / RT-1-X 33.3±6.1% / Octo 26.7±5.8%（表 6，p28 L47）<br>摘要头条：29 任务上比闭源 RT-2-X（55B）高 **16.5 个绝对百分点**（p1 L58–59、p2 L44–45） | 不是全面反超：semantic generalization 那一类 RT-2-X 更高，图 3 图注 p7 L33 自己就写了「除语义泛化外」。归因见 p8 L40–47（RT-2-X 的网络预训练规模更大、且与机器人数据联合微调）。论文没印两个 embodiment 的合并均值行，16.5% 是摘要口径，卡片不复算。两表分母不同（170 与 60 rollouts），别横向比数值 |
| 训练成本 | **64 张 A100 × 14 天 = 21,500 A100-hours**，batch size 2048（§3.5 p6 L38–39） | 超参：27 个 epoch，动作 token 准确率过 95% 前真机表现一直在涨（§3.4 p6 L29–33）；固定学习率 2e-5，warmup 没带来收益（§3.4 p6 L34–36）。论文未给美元费用，也没提中断次数 |
| 推理与部署 | bfloat16 权重 **约 6 Hz @ RTX 4090**，明写不含编译、投机解码等加速（§3.5 p6 L40–42）<br>显存原文给了三个数：§3.5 p6 L39 的 `15GB`、§5.4 p10 L56 的 `only 16GB`、表 2 p10 L41 的 `16.8 GB`<br>int4 = **7.0 GB**，成功率 71.9±4.7% 与 bfloat16 打平；int8 掉到 58.1±5.1%（表 2，p10 L41–43） | 三个显存值是原文既成的不一致，卡片照列、不替它统一。图 6 图注补了一句用 TensorRT-LLM 之类还能再提速（p10 L47–52），所以 6 Hz 不是上限。要留意 p10 脚注 4：§5.3 与 §5.4 用的是更小数据混合、视觉塔只留 SigLIP 的版本，这两张表的读数不能当主模型引用 |
| 微调成本 | LoRA（r=32）只训 **1.4%** 参数就追上全量微调，单张 A100 **10–15 小时**，算力省 **8 倍**（§5.3 p10 L30–35；8 倍的基线是 p10 L2–3 的「8 张 A100、每任务 5–15 小时」） | 表 1 其余档位：全量微调 69.7±7.2%、last layer only 30.3±6.1%、frozen vision 47.0±6.9%、sandwich 62.1±7.9%（p10 L16–21，33 rollouts）。表头单位是「可训参数 ×10⁶」；两格显存带的星号是用 FSDP 分片到 2 张卡的意思，不是显著性标记 |

---

## 💬 讨论与备注

- **版本依据**：本卡以 **arXiv:2406.09246v3**（首页水印 `arXiv:2406.09246v3 [cs.RO] 5 Sep 2024`，37 页）为底本。PDF 正文自始至终没印会议名，CoRL 只出现在参考文献里；唯一一手线索是 PDF 元数据 `Subject: Proceedings of the 8th Conference on Robot Learning (CoRL 2024)`，而同处 `Author: Anonymous Submission`（camera-ready 模板没改干净）。标题栏的 CoRL 2024 与 PMLR 卷页 270:2679-2713 来自 PMLR 页面，属外部信息，不是论文自述。跟 RT-2 卡（v1 全文也无会议字样）是同一条坑。
- **作者排序**：前三位 Moo Jin Kim、Karl Pertsch、Siddharth Karamcheti 标注同等贡献（首页脚注「∗ 表示同等贡献」），按贡献排而非字母序，与 RT-2 卡的情况相反，所以 `Kim et al.` 可以读成主导作者。
- **与 RT-2 卡的承接关系**：RT-2 §5 点名「可用的通用 VLM 底座数量极少且基本闭源」，OpenVLA 正是这条局限的开源回应。要比 RT-2-X 得先拿 API 这件事，作者在 Acknowledgments 里留了一手证据：感谢 Google DeepMind 给的是 RT-2-X API 的 alpha 访问权限（p11 L43–48）——闭源不是推测，是他自己的致谢措辞。两卡通读。
- **代码与权重的出处口径**：论文给的入口只有项目主页 openvla.github.io（p1 L9 首页印着，§4 p6 L51、§5.1 p8 L38 各一处），正文没印 GitHub 仓库路径，也没印 HuggingFace 模型名。上链的 `github.com/openvla/openvla` 和 `openvla/openvla-7b` 是我另行实测确认存在的（前者用 git ls-remote 拿到 HEAD，后者经 hf-mirror API 返回 MIT 许可），出处写「实测」而不是「论文所给」。
- **速览表数值全部来自逐页 grep 的台账**，每条括注节号、物理页和行号（页文本行号可用 `sed -n '34p' pages/p26.txt` 复现）。台账另记了几条「原文确实没给」：训练美元费用、OpenX 筛选过程的中间计数、OpenVLA 相对 Octo 的参数倍数句。

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「深度阅读」
> - 想看读后的思考与收获？看「深度阅读」的个人收获部分

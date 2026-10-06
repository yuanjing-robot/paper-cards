# Dex-Net 2.0: Deep Learning to Plan Robust Grasps with Synthetic Point Clouds and Analytic Metrics

> 📄 [论文原文](https://arxiv.org/abs/1703.09312) · 💻 [官方代码](https://github.com/BerkeleyAutomation/gqcnn) · 📝 [精读笔记](reading-notes.md) · 🌐 [中文翻译](translation.md)
>
> Jeffrey Mahler et al., **RSS 2017**
> 领域标签: #抓取 #合成数据 #深度学习
> 首次笔记: @zeng417 | 最后更新: 2026-10-06

---

## 🔗 资源链接

| 类型 | 链接 |
|------|------|
| 论文原文 | [arXiv](https://arxiv.org/abs/1703.09312) |
| 官方代码 | [GitHub](https://github.com/BerkeleyAutomation/gqcnn) |
| 复现代码 | _待补充_ |
| 项目主页 | _待补充_ |
| 解读视频 | _待补充_ |

---

## 🎯 一句话概括

用 670 万条合成深度图 + 解析式鲁棒性指标训练 GQ-CNN 抓取质量网络，把抓取规划做成"看一眼打分"，是数据驱动抓取的代表作。

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
| 参数量 | GQ-CNN 较小 | 深度图输入 |
| 训练数据 | 6.7M 合成深度图 | + 5k 真实抓取验证 |
| 核心指标 | 抓取成功率 93% | 抗扰抓取设定 |
| 训练成本 | - | 合成数据生成为主 |

---

## 💬 讨论与备注

_有什么疑问、想法、补充，都可以写在这里_

---

> 💡 **快速使用指南**
> - 想看中文版？看「论文翻译」
> - 想快速了解论文核心？看「精读笔记」
> - 想看读后的思考与收获？看「精读笔记」的个人收获部分

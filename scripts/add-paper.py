#!/usr/bin/env python3
"""
一键创建论文卡片文件夹

用法:
    python scripts/add-paper.py \
      --title "Attention Is All You Need" \
      --field llm \
      --author "Vaswani et al." \
      --conference "NeurIPS 2017" \
      --paper-url "https://arxiv.org/abs/1706.03762" \
      --code-url "https://github.com/tensorflow/tensor2tensor"

参数:
    --title         论文标题（必填）
    --field         研究领域：llm / cv / diffusion / rl / ...（必填）
    --author        作者列表（可选）
    --conference    会议/期刊 + 年份（可选）
    --paper-url     论文链接（可选）
    --code-url      官方代码链接（可选）
    --tags          标签，用逗号分隔（可选）
    --output-dir    输出目录，默认 cards/（可选）
"""

import argparse
import shutil
import os
import re
from pathlib import Path


def slugify(title: str) -> str:
    """将论文标题转为文件夹名：全小写，空格转 -，移除非字母数字字符"""
    # 只保留英文、数字、空格、连字符
    title = re.sub(r'[^a-zA-Z0-9\s-]', '', title)
    # 空格转连字符
    title = re.sub(r'\s+', '-', title.strip().lower())
    # 多个连字符转一个
    title = re.sub(r'-+', '-', title)
    return title.strip('-')


def main():
    parser = argparse.ArgumentParser(description='一键创建论文卡片文件夹')
    parser.add_argument('--title', required=True, help='论文标题')
    parser.add_argument('--field', required=True, help='研究领域：llm/cv/diffusion/rl/...')
    parser.add_argument('--author', default='', help='作者列表')
    parser.add_argument('--conference', default='', help='会议/期刊 + 年份')
    parser.add_argument('--paper-url', default='', help='论文链接')
    parser.add_argument('--code-url', default='', help='官方代码链接')
    parser.add_argument('--tags', default='', help='标签，用逗号分隔')
    parser.add_argument('--output-dir', default='cards', help='输出目录，默认 cards/')
    args = parser.parse_args()

    # 仓库根目录（脚本在 scripts/ 下，往上一层就是根目录）
    repo_root = Path(__file__).parent.parent
    template_dir = repo_root / 'templates' / 'paper-card-template'
    output_dir = repo_root / args.output_dir / args.field

    # 生成文件夹名
    folder_name = slugify(args.title)
    target_dir = output_dir / folder_name

    if target_dir.exists():
        print(f'❌ 目标文件夹已存在：{target_dir}')
        print(f'   如果要重新生成，请先删除该文件夹')
        return

    if not template_dir.exists():
        print(f'❌ 模板文件夹不存在：{template_dir}')
        return

    # 复制模板
    shutil.copytree(template_dir, target_dir)
    print(f'✅ 已创建卡片文件夹：{target_dir}')

    # 替换 README.md 中的占位符
    readme_path = target_dir / 'README.md'
    if readme_path.exists():
        content = readme_path.read_text(encoding='utf-8')

        # 替换标题
        content = content.replace('[论文标题]', args.title)

        # 替换作者和会议
        author_line = f'{args.author}, **{args.conference}**' if args.author and args.conference else \
                      f'{args.author}' if args.author else \
                      f'**{args.conference}**' if args.conference else \
                      '作者, **会议/期刊** 年份'
        content = content.replace('作者列表, **会议/期刊** 年份', author_line)

        # 替换标签
        if args.tags:
            tags = ' '.join(f'#{t.strip()}' for t in args.tags.split(','))
            content = content.replace('#标签1 #标签2 #标签3', tags)

        # 替换论文链接
        if args.paper_url:
            content = content.replace(
                '[arXiv](https://arxiv.org/abs/xxxx.xxxxx)',
                f'[论文链接]({args.paper_url})'
            )

        # 替换代码链接
        if args.code_url:
            content = content.replace(
                '[GitHub](https://github.com/xxx)',
                f'[GitHub]({args.code_url})'
            )

        readme_path.write_text(content, encoding='utf-8')
        print(f'✅ 已更新 README.md')

    print()
    print('🎉 论文卡片创建成功！')
    print(f'   路径：{target_dir}')
    print()
    print('📝 下一步：')
    print(f'   1. cd {target_dir.relative_to(repo_root)}')
    print('   2. 先填 README.md（速览卡）')
    print('   3. 填写 01-reuse.md（落地复用）+ 03-innovation.md（创新拆解）')
    print('   4. 其他卡片按需补充')
    print('   5. 提 PR')


if __name__ == '__main__':
    main()

import os
import re
import json
from pathlib import Path

def format_code_blocks(file_path):
    """格式化Markdown文件中的JSON和JavaScript代码块"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 匹配JSON和JavaScript代码块
        code_block_pattern = re.compile(r"```(json|javascript|js)\n(.*?)```", re.DOTALL)
        formatted_content = content

        for match in code_block_pattern.finditer(content):
            language = match.group(1)
            code = match.group(2)

            try:
                if language == "json":
                    # 格式化JSON代码
                    parsed_json = json.loads(code)
                    formatted_code = json.dumps(parsed_json, indent=4, ensure_ascii=False)
                elif language in ["javascript", "js"]:
                    # 格式化JavaScript代码（简单缩进处理）
                    formatted_code = "\n".join(line.strip() for line in code.splitlines())
                else:
                    continue

                # 替换原始代码块为格式化后的代码块
                formatted_content = formatted_content.replace(
                    match.group(0),
                    f"```{language}\n{formatted_code}\n```"
                )
            except Exception as e:
                print(f"跳过无法格式化的代码块: {e}")

        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(formatted_content)

        print(f"已格式化文件: {file_path}")

    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")


def process_markdown_files(directory):
    """批量处理目录中的Markdown文件"""
    markdown_files = Path(directory).rglob("*.md")
    for file_path in markdown_files:
        format_code_blocks(file_path)


if __name__ == "__main__":
    # 设置Markdown文件所在目录
    markdown_dir = "data"  # 修改为你的Markdown文件目录
    if not os.path.exists(markdown_dir):
        print(f"目录不存在: {markdown_dir}")
    else:
        process_markdown_files(markdown_dir)
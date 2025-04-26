import os
from datetime import datetime
import re

def get_date_from_filename(filename):
    """从文件名中提取日期"""
    # 匹配文件名中的日期格式 YYYYMMDD
    patterns = [
        r'(\d{8})_\d{6}',  # harmonyos-guides_YYYYMMDD_HHMMSS
        r'(\d{8})',        # YYYYMMDD
        r'merged_(\d{8})'  # merged_YYYYMMDD
    ]
    
    for pattern in patterns:
        match = re.search(pattern, filename)
        if match:
            return match.group(1)
    return None

def merge_daily_files():
    """合并同一天的文档"""
    # 获取data目录
    data_dir = 'data'
    if not os.path.exists(data_dir):
        print("data目录不存在")
        return
    
    # 获取所有Markdown文件
    md_files = [f for f in os.listdir(data_dir) if f.endswith('.md')]
    if not md_files:
        print("没有找到Markdown文件")
        return
    
    # 按日期分组文件
    daily_files = {}
    for file in md_files:
        date = get_date_from_filename(file)
        if date:
            if date not in daily_files:
                daily_files[date] = []
            daily_files[date].append(file)
    
    # 合并同一天的文件
    for date, files in daily_files.items():
        print(f"\n处理 {date} 的文件: {', '.join(files)}")
        
        # 创建合并后的文件名
        merged_filename = f'merged_{date}.md'
        merged_path = os.path.join(data_dir, merged_filename)
        
        # 检查合并文件是否已存在
        if os.path.exists(merged_path):
            print(f"合并文件 {merged_filename} 已存在，跳过处理")
            continue
        
        # 合并文件
        with open(merged_path, 'w', encoding='utf-8') as outfile:
            # 写入合并文件的元数据
            outfile.write(f"# 合并文件\n")
            outfile.write(f"合并时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # 合并每个文件的内容
            for file in files:
                file_path = os.path.join(data_dir, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.readlines()
                        # 删除空白行并替换“收起深色代码主题复制”为换行符
                        content = [line.replace("收起深色代码主题复制", "\n").strip() for line in content if line.strip()]
                        outfile.write("\n".join(content))
                        outfile.write("\n\n")
                except Exception as e:
                    print(f"处理文件 {file} 时出错: {str(e)}")
                    continue
        
        print(f"已合并到: {merged_filename}")
        
        # 验证合并文件是否成功创建
        if os.path.exists(merged_path) and os.path.getsize(merged_path) > 0:
            # 删除原始文件
            for file in files:
                try:
                    os.remove(os.path.join(data_dir, file))
                    print(f"已删除: {file}")
                except Exception as e:
                    print(f"删除文件 {file} 时出错: {str(e)}")
        else:
            print(f"警告: 合并文件 {merged_filename} 创建失败或为空")

if __name__ == "__main__":
    merge_daily_files()
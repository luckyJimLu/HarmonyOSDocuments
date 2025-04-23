import os
from datetime import datetime
import re

def get_date_from_filename(filename):
    """从文件名中提取日期"""
    # 匹配文件名中的日期格式 YYYYMMDD
    match = re.search(r'(\d{8})', filename)
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
    
    # 获取所有txt文件
    txt_files = [f for f in os.listdir(data_dir) if f.endswith('.txt')]
    if not txt_files:
        print("没有找到txt文件")
        return
    
    # 按日期分组文件
    daily_files = {}
    for file in txt_files:
        date = get_date_from_filename(file)
        if date:
            if date not in daily_files:
                daily_files[date] = []
            daily_files[date].append(file)
    
    # 合并同一天的文件
    for date, files in daily_files.items():
        if len(files) > 1:  # 只处理同一天有多个文件的情况
            print(f"\n处理 {date} 的文件:")
            print(f"找到 {len(files)} 个文件: {', '.join(files)}")
            
            # 创建合并后的文件名
            merged_filename = f'merged_{date}.txt'
            merged_path = os.path.join(data_dir, merged_filename)
            
            # 合并文件
            with open(merged_path, 'w', encoding='utf-8') as outfile:
                # 写入合并文件的元数据
                outfile.write(f"""合并文件: {', '.join(files)}
合并时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
来源: Huawei Developer

""")
                
                # 合并每个文件的内容
                for file in files:
                    file_path = os.path.join(data_dir, file)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(f"\n{'='*50}\n")
                        outfile.write(f"文件: {file}\n")
                        outfile.write(f"{'='*50}\n\n")
                        outfile.write(content)
                        outfile.write("\n\n")
            
            print(f"已合并到: {merged_filename}")
            
            # 删除原始文件
            for file in files:
                os.remove(os.path.join(data_dir, file))
                print(f"已删除: {file}")

if __name__ == "__main__":
    merge_daily_files() 
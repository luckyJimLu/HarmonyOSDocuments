from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import os
from datetime import datetime
import urllib3
import certifi
import time

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def ensure_data_directory():
    """确保数据目录存在"""
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    return data_dir

def save_to_txt(content, filename=None):
    """保存内容到TXT文件"""
    data_dir = ensure_data_directory()
    
    if filename is None:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'markdown_content_{timestamp}.txt'
    
    filepath = os.path.join(data_dir, filename)
    
    # 检查文件是否存在
    file_exists = os.path.exists(filepath)
    
    # 以追加模式打开文件
    with open(filepath, 'a', encoding='utf-8') as f:
        # 如果文件是新创建的，添加元数据
        if not file_exists:
            f.write(f"""URL: {url}
爬取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
来源: Huawei Developer

""")
        # 添加分隔线
        f.write("\n" + "="*50 + "\n\n")
        # 写入新内容
        f.write(content)
    
    return filepath

def extract_markdown_content(soup):
    """提取tiledSection类的内容"""
    # 查找class为tiledSection的div元素
    tiled_sections = soup.find_all('div', class_='tiledSection')
    print(f"找到的tiledSection元素数量: {len(tiled_sections)}")
    
    if not tiled_sections:
        print("未找到tiledSection元素")
        return "未找到tiledSection内容"
    
    # 打印每个找到的元素的内容预览
    for i, section in enumerate(tiled_sections, 1):
        print(f"\n第 {i} 个tiledSection元素:")
        print(f"类名: {section.get('class')}")
        print(f"内容预览: {section.get_text(strip=True)[:100]}...")
    
    # 提取所有找到的tiledSection内容
    all_content = []
    for section in tiled_sections:
        # 获取所有子元素
        for element in section.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'div', 'span', 'li', 'pre', 'code']):
            text = element.get_text(strip=True)
            if text:
                # 根据元素类型添加适当的格式
                if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    all_content.append(f"\n{text}\n")
                elif element.name in ['pre', 'code']:
                    all_content.append(f"\n```\n{text}\n```\n")
                else:
                    all_content.append(text)
    
    # 清理和格式化文本
    cleaned_text = []
    for text in all_content:
        # 移除多余的空格和换行
        text = ' '.join(text.split())
        # 移除特殊字符
        text = text.replace('\u200b', '')  # 移除零宽空格
        text = text.replace('\xa0', ' ')   # 替换不间断空格
        if text and text not in cleaned_text:  # 去重
            cleaned_text.append(text)
    
    return '\n\n'.join(cleaned_text)

def scrape_huawei_training(url):
    try:
        with sync_playwright() as p:
            # 启动浏览器
            browser = p.chromium.launch(headless=False)  # 设置为非无头模式以便调试
            page = browser.new_page()
            
            try:
                # 访问页面
                print("正在加载页面...")
                page.goto(url, wait_until="networkidle")
                
                # 等待页面加载
                print("等待页面加载...")
                time.sleep(10)  # 等待时间
                
                # 打印页面标题和URL
                print(f"页面标题: {page.title()}")
                print(f"当前URL: {page.url}")
                
                # 等待tiledSection元素出现
                print("等待tiledSection元素...")
                try:
                    # 使用复合选择器
                    page.wait_for_selector('div.tiledSection', timeout=60000)
                except Exception as e:
                    print(f"等待tiledSection元素超时: {str(e)}")
                    # 打印页面内容以便调试
                    print("页面内容预览:")
                    print(page.content()[:1000])
                    return None
                
                # 获取页面内容
                content = page.content()
                soup = BeautifulSoup(content, 'html.parser')
                
                # 提取内容
                markdown_content = extract_markdown_content(soup)
                
                # 添加元数据
                metadata = f"""URL: {url}
爬取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
来源: Huawei Developer

"""
                full_content = metadata + markdown_content
                
                return full_content
                
            finally:
                # 关闭浏览器
                browser.close()
                
    except Exception as e:
        print(f"爬取过程中出现错误: {str(e)}")
        return None

if __name__ == "__main__":
    url = "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-categories-and-access"
    markdown_content = scrape_huawei_training(url)
    
    if markdown_content:
        print("爬取成功！")
        filepath = save_to_txt(markdown_content)
        print(f"数据已保存到: {filepath}")
    else:
        print("爬取失败！") 
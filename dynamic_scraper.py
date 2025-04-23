from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import os
from datetime import datetime
import urllib3
import certifi
import time
import json

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def load_config():
    """加载配置文件"""
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"加载配置文件失败: {str(e)}")
        return None

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
        # 如果文件是新创建的，直接写入内容
        if not file_exists:
            f.write(content)
        else:
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

def scrape_huawei_training(url, settings):
    try:
        with sync_playwright() as p:
            # 启动浏览器
            browser = p.chromium.launch(headless=settings.get('headless', False))
            page = browser.new_page()
            
            try:
                # 访问页面
                print("正在加载页面...")
                page.goto(url, wait_until="networkidle")
                
                # 等待页面加载
                print("等待页面加载...")
                time.sleep(settings.get('wait_time', 10))
                
                # 打印页面标题和URL
                print(f"页面标题: {page.title()}")
                print(f"当前URL: {page.url}")
                
                # 等待tiledSection元素出现
                print("等待tiledSection元素...")
                try:
                    page.wait_for_selector('div.tiledSection', timeout=settings.get('timeout', 60000))
                except Exception as e:
                    print(f"等待tiledSection元素超时: {str(e)}")
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
                browser.close()
                
    except Exception as e:
        print(f"爬取过程中出现错误: {str(e)}")
        return None

def process_all_urls():
    """处理配置文件中的所有URL"""
    config = load_config()
    if not config:
        print("无法加载配置文件，程序退出")
        return
    
    settings = config.get('settings', {})
    urls = config.get('urls', [])
    
    if not urls:
        print("配置文件中没有找到URL")
        return
    
    print(f"找到 {len(urls)} 个URL需要处理")
    
    for url_data in urls:
        url = url_data.get('url')
        description = url_data.get('description', '')
        category = url_data.get('category', '')
        
        print(f"\n处理URL: {url}")
        print(f"描述: {description}")
        print(f"分类: {category}")
        
        markdown_content = scrape_huawei_training(url, settings)
        
        if markdown_content:
            # 使用分类和描述作为文件名的一部分
            filename = f"{category}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            filepath = save_to_txt(markdown_content, filename)
            print(f"数据已保存到: {filepath}")
        else:
            print("爬取失败！")

if __name__ == "__main__":
    process_all_urls() 
import logging
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import os
from datetime import datetime
import urllib3
import time
import json
import re

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 配置日志模块
logging.basicConfig(
    level=logging.INFO,  # 设置日志级别
    format="%(asctime)s - %(levelname)s - %(message)s",  # 日志格式
    handlers=[
        logging.FileHandler("scraper.log", encoding="utf-8"),  # 日志写入文件
        logging.StreamHandler()  # 日志输出到控制台
    ]
)

def load_urls(file_path='urls.txt'):
    """加载URL列表"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip()]
        return urls
    except Exception as e:
        logging.error(f"加载URL文件失败: {str(e)}")
        return []

def ensure_data_directory():
    """确保数据目录存在"""
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    return data_dir

def save_to_markdown(content, filename=None):
    """保存内容到Markdown文件"""
    data_dir = ensure_data_directory()
    
    if filename is None:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'markdown_content_{timestamp}.md'
    
    filepath = os.path.join(data_dir, filename)
    
    # 格式化 JSON 内容为紧凑格式
    try:
        json_blocks = re.findall(r"```json\n(.*?)\n```", content, re.DOTALL)
        for block in json_blocks:
            parsed_json = json.loads(block)
            compact_json = json.dumps(parsed_json, separators=(',', ':'), ensure_ascii=False)
            content = content.replace(block, compact_json)
    except Exception as e:
        logging.warning(f"JSON 格式化失败: {str(e)}")
    
    content = content.replace('\n', '\r\n')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    logging.info(f"内容已保存到文件: {filepath}")
    return filepath

def extract_markdown_content(soup):
    """提取tiledSection类、ulinks类和markdown-body类的内容，并处理图像、JSON、JavaScript和表格"""
    # 提取 tiledSection 类的内容
    tiled_sections = soup.find_all('div', class_='tiledSection')
    logging.info(f"找到的tiledSection元素数量: {len(tiled_sections)}")
    
    # 提取 ulinks 类的内容
    ulinks_sections = soup.find_all('ul', class_='ulinks')
    logging.info(f"找到的ulinks元素数量: {len(ulinks_sections)}")
    
    # 提取 markdown-body 类的内容
    if not tiled_sections:
        tiled_sections = soup.find_all('div', class_=re.compile(r'\bmarkdown-body\b'))
        logging.info(f"找到的markdown-body元素数量: {len(tiled_sections)}")
    
    if not tiled_sections and not ulinks_sections:
        logging.warning("未找到tiledSection、ulinks或markdown-body元素")
        return "未找到tiledSection、ulinks或markdown-body内容"
    
    all_content = []
    
    # 处理 tiledSection 内容
    for section in tiled_sections:
        for element in section.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'div', 'span', 'li', 'pre', 'code', 'img', 'ol', 'table']):
            # 跳过 <div class="handle-hover-tips"> 元素及其所有子元素
            if element.find_parent('div', class_='handle-hover-tips'):
                logging.info("跳过 handle-hover-tips 的内容")
                continue
            elif element.name == 'img':
                # 处理 img 元素
                img_src = element.get('src', '')
                if img_src:
                    all_content.append(f"![Image]({img_src})")
            elif element.name == 'pre':
                # 判断是否为 JSON 或 TypeScript 格式
                pre_class = element.get('class', [])
                if any('json' in cls for cls in pre_class):
                    # 处理 JSON 格式内容
                    try:
                        json_text = ''.join(li.get_text(strip=True) for li in element.find_all('li'))
                        parsed_json = json.loads(json_text)
                        formatted_json = json.dumps(parsed_json, indent=4, ensure_ascii=False)
                        all_content.append(f"\n```json\n{formatted_json}\n```\n")
                    except json.JSONDecodeError:
                        logging.warning(f"跳过无法解析的JSON内容: {json_text[:50]}...")
                elif any('ts' in cls or 'typescript' in cls for cls in pre_class):
                    # 处理 TypeScript 格式内容
                    ts_text = '\n'.join(li.get_text(strip=True) for li in element.find_all('li'))
                    all_content.append(f"\n```typescript\n{ts_text}\n```\n")
            elif element.name == 'table':
                # 处理表格元素
                table_md = convert_table_to_markdown(element)
                all_content.append(table_md)
            else:
                text = element.get_text(strip=True)
                if text:
                    if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'p']:
                        all_content.append(f"\n{text}\n")
                    else:
                        logging.debug(f"未处理的元素: {element.name}, 内容: {text}")
    
    # 处理 ulinks 内容
    for ulinks in ulinks_sections:
        for li in ulinks.find_all('li'):
            text = li.get_text(strip=True)
            if text:
                all_content.append(f"- {text}")
    
    # 清理文本
    cleaned_text = []
    for text in all_content:
        text = ' '.join(text.split())
        text = text.replace('\u200b', '').replace('\xa0', ' ')
        if text and text not in cleaned_text:
            cleaned_text.append(text)
    
    return '\n\n'.join(cleaned_text)

def convert_table_to_markdown(table):
    """将HTML表格转换为Markdown表格"""
    rows = table.find_all('tr')
    if not rows:
        return ""
    
    table_md = []
    for i, row in enumerate(rows):
        cols = row.find_all(['th', 'td'])
        col_text = [col.get_text(strip=True) for col in cols]
        table_md.append(f"| {' | '.join(col_text)} |")
        # 添加表头分隔符
        if i == 0:
            table_md.append(f"| {' | '.join(['---'] * len(col_text))} |")
    
    return "\n".join(table_md)

def scrape_huawei_training(url, wait_time=10, timeout=60000, headless=False):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=headless)
            page = browser.new_page()
            
            try:
                logging.info("正在加载页面...")
                page.goto(url, wait_until="networkidle")
                logging.info("等待页面加载...")
                time.sleep(wait_time)
                logging.info(f"页面标题: {page.title()}")
                logging.info(f"当前URL: {page.url}")
                logging.info("等待包含 markdown-body 的元素...")
                try:
                    page.wait_for_selector("div[class*='markdown-body']", timeout=timeout)
                except Exception as e:
                    logging.error(f"等待包含 markdown-body 的元素超时: {str(e)}")
                    logging.info("页面内容预览:")
                    logging.info(page.content()[:1000])  # 打印前 1000 个字符
                    return None
                
                content = page.content()
                soup = BeautifulSoup(content, 'html.parser')

                logging.info("格式化后的 HTML 内容:")
                logging.info(soup.prettify()[:1000])  # 限制打印长度

                markdown_content = extract_markdown_content(soup)
                
                metadata = f"""URL: {url}
爬取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
来源: Huawei Developer

"""
                full_content = metadata + markdown_content
                
                return full_content
                
            finally:
                browser.close()
                
    except Exception as e:
        logging.error(f"爬取过程中出现错误: {str(e)}")
        return None

def save_all_to_markdown(contents, filename="all_content.md"):
    """将所有内容保存到一个Markdown文件"""
    data_dir = ensure_data_directory()
    filepath = os.path.join(data_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(contents)
    
    logging.info(f"所有内容已保存到文件: {filepath}")
    return filepath

def process_all_urls():
    """处理文本文件中的所有URL"""
    urls = load_urls()
    if not urls:
        logging.error("无法加载URL文件，程序退出")
        return
    
    logging.info(f"找到 {len(urls)} 个URL需要处理")
    
    processed_urls = set()
    
    for url in urls:
        if url in processed_urls:
            logging.info(f"跳过已处理的URL: {url}")
            continue
        
        logging.info(f"处理URL: {url}")
        
        markdown_content = scrape_huawei_training(url)
        
        if markdown_content:
            filename = f"url_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            filepath = save_to_markdown(markdown_content, filename)
            logging.info(f"数据已保存到: {filepath}")
            processed_urls.add(url)
        else:
            logging.error("爬取失败！")
    
    logging.info(f"处理完成！共处理 {len(processed_urls)} 个URL")

if __name__ == "__main__":
    process_all_urls()
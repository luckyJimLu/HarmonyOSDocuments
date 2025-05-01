import logging
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import os
from datetime import datetime
import urllib3
import time
import re
from tqdm import tqdm  # 引入 tqdm 库
import sys

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
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    logging.info(f"内容已保存到文件: {filepath}")
    return filepath

def extract_markdown_content(soup):
    """提取markdown-body类的内容，并处理图像、JSON、JavaScript、表格和有序列表"""
    # 提取 markdown-body 类的内容
    tiled_sections = soup.find_all('div', class_=re.compile(r'\bmarkdown-body\b'))
    logging.info(f"找到的markdown-body元素数量: {len(tiled_sections)}")
    
    all_content = []
    
    # 处理 tiledSection 内容
    for section in tiled_sections:
        for element in section.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'div', 'span', 'li', 'pre', 'code', 'img', 'ol', 'table', 'ul']):
            # 跳过 <div class="handle-hover-tips"> 元素及其所有子元素
            if element.find_parent('div', class_='handle-hover-tips'):
                logging.info("跳过 handle-hover-tips 的内容")
                continue
            elif element.name == 'ul':
                # 处理 ul 元素
                for li in element.find_all('li'):
                    if li.find_parent('ol', class_='linenums'):
                        continue
                    p_elements = li.find_all('p')
                    pre_element = li.find('pre')
                    if p_elements:
                        temp_p = ''
                        # 提取所有 p 元素的文本内容
                        for p in p_elements:
                            text = p.get_text(strip=True)
                            if text:
                                temp_p = temp_p + ' ' + text
                        all_content.append(f"- {temp_p}")
                    if pre_element:
                        pre_content = process_pre_element(pre_element)
                        if pre_content:
                            all_content.append(pre_content)
            elif element.name == 'ol':
                # 处理 ol 元素
                count = 1
                for i, li in enumerate(element.find_all('li'), start=1):
                    # pre > ol > li 不进行处理
                    if li.find_parent('ol', class_='linenums'):
                        continue
                    p_elements = li.find_all('p')
                    pre_element = li.find('pre')
                    if p_elements:
                        temp_p = ''
                        # 提取所有 p 元素的文本内容
                        for p in p_elements:
                            text = p.get_text(strip=True)
                            if text:
                                temp_p = temp_p + ' '+ text
                        all_content.append(f"{count}. {temp_p}")
                        count += 1
                    if pre_element:
                        pre_content = process_pre_element(pre_element)
                        if pre_content:
                            all_content.append(pre_content)
            elif element.name == 'img':
                # 处理 img 元素
                img_src = element.get('src', '')
                if img_src:
                    all_content.append(f"![Image]({img_src})")
            elif element.name == 'pre':
                    # 如果祖先元素中包含 <li>，直接跳过
                if element.find_parent('li'):
                    logging.debug(f"跳过祖先元素为 <li> 的 <pre> 元素: {element.get_text(strip=True)}")
                    continue
                pre_content = process_pre_element(element)
                if pre_content:
                    all_content.append(pre_content)
            elif element.name == 'table':
                # 处理表格元素
                table_md = '\n' + convert_table_to_markdown(element)
                all_content.append(table_md)
            else:
                text = element.get_text(strip=True)
                if text:
                    if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                        all_content.append(f"\n{text}\n")
                    elif element.name == 'p':
                        # 如果 <p> 的父节点是 <li>，跳过处理
                        if element.find_parent('li'):
                            logging.debug(f"跳过父节点为 <li> 的 <p> 元素: {element.get_text(strip=True)}")
                            continue
                        # 否则正常处理 <p> 元素
                        all_content.append(f"\n{text}\n")
                    else:
                        logging.debug(f"未处理的元素: {element.name}, 内容: {text}")
    return '\n'.join(all_content)

def process_pre_element(element):
    """
    处理 <pre> 元素，支持 JSON、TypeScript 和 XML 格式
    """
    # 判断 <pre> 的 class 属性
    pre_class = element.get('class', [])
    if any('json' in cls for cls in pre_class):
        # 处理 JSON 格式内容
        json_text = '\n'.join(li.get_text(strip=False) for li in element.find_all('li'))
        return f"\n```json\n{json_text}\n```\n"
    elif any('ts' in cls or 'typescript' in cls for cls in pre_class):
        # 处理 TypeScript 格式内容
        ts_text = '\n'.join(li.get_text(strip=False) for li in element.find_all('li'))
        return f"\n```typescript\n{ts_text}\n```\n"
    elif any('XML' in cls for cls in pre_class):
        # 处理 XML 格式内容
        xml_text = '\n'.join(li.get_text(strip=False) for li in element.find_all('li'))
        return f"\n```xml\n{xml_text}\n```\n"
    elif any('shell' in cls for cls in pre_class):
        # 处理 XML 格式内容
        shell_text = '\n'.join(li.get_text(strip=False) for li in element.find_all('li'))
        return f"\n```shell\n{shell_text}\n```\n"
    else:
        logging.debug(f"未识别的 <pre> 元素格式: {element.get_text(strip=True)}")
        return None

def convert_table_to_markdown(table):
    """将HTML表格转换为Markdown表格"""
    rows = table.find_all('tr')
    if not rows:
        return ""
    
    table_md = []
    for i, row in enumerate(rows):
        cols = row.find_all(['th', 'td'])
        col_text = [col.get_text(strip=False) for col in cols]
        table_md.append(f"| {' | '.join(col_text)} |")
        # 添加表头分隔符
        if i == 0:
            table_md.append(f"| {' | '.join(['---'] * len(col_text))} |")
    
    return "\n".join(table_md)

def scrape_huawei_training(url, wait_time=10, timeout=60000, headless=True):
    try:
        with sync_playwright() as p:
            # 启动浏览器时设置 headless=True
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

def save_all_to_markdown(contents, filename="all_content.txt"):
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
    
    # 使用 tqdm 显示进度条
    with tqdm(total=len(urls), desc="处理进度", unit="URL", file=sys.stdout) as pbar:
        for url in urls:
            if url in processed_urls:
                logging.info(f"跳过已处理的URL: {url}")
                pbar.update(1)  # 更新进度条
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
            
            pbar.update(1)  # 更新进度条
    
    logging.info(f"处理完成！共处理 {len(processed_urls)} 个URL")

if __name__ == "__main__":
    process_all_urls()
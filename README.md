# HarmonyOSDocuments

这是一个用于爬取华为开发者社区 HarmonyOS 文档的自动化工具。该工具可以批量获取 HarmonyOS 相关文档内容，并保存为结构化的文本文件。

## 功能特点

- 支持通过配置文件批量爬取多个URL
- 自动提取文档内容并保存为文本文件
- 支持自定义爬取参数（等待时间、超时设置等）
- 自动处理页面加载和内容提取
- 保存完整的元数据信息

## 环境要求

- Python 3.7+
- Playwright
- BeautifulSoup4
- 其他依赖包（见 requirements.txt）

## 安装步骤

1. 克隆项目到本地：
```bash
git clone https://github.com/yourusername/HarmonyOSDocuments.git
cd HarmonyOSDocuments
```

2. 创建并激活虚拟环境：
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 安装 Playwright 浏览器：
```bash
playwright install
```

## 使用方法

1. 配置 `config.json` 文件：
```json
{
    "urls": [
        {
            "url": "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/your-doc-url",
            "description": "文档描述",
            "category": "文档分类"
        }
    ],
    "settings": {
        "wait_time": 10,
        "headless": false,
        "timeout": 60000
    }
}
```

2. 运行爬虫：
```bash
python dynamic_scraper.py
```

3. 查看结果：
- 爬取的文档将保存在 `data` 目录下
- 文件名格式：`{category}_{timestamp}.txt`

## 配置说明

### URL配置
- `url`: 要爬取的文档URL
- `description`: 文档描述
- `category`: 文档分类

### 爬虫设置
- `wait_time`: 页面加载等待时间（秒）
- `headless`: 是否使用无头模式（true/false）
- `timeout`: 元素等待超时时间（毫秒）

## 注意事项

1. 请确保网络连接稳定
2. 遵守网站的爬虫政策和使用条款
3. 适当设置等待时间，避免频繁请求
4. 建议使用代理IP进行大规模爬取

## 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进项目。

## 许可证

MIT License
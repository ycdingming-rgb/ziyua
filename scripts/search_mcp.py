#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Awesome MCP Servers 搜索引擎
在内置的分类数据中按关键词搜索匹配的 MCP 服务器。
"""

import json
import sys
import os

# Fix encoding for Windows console
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# MCP 服务器数据 — 按分类组织
MCP_DATA = {
    "聚合器 (Aggregators)": [
        {"name": "agent", "url": "https://github.com/1mcp-app/agent", "desc": "统一的 MCP 服务器，聚合多个 MCP 服务器"},
        {"name": "OpenMCP", "url": "https://github.com/wegotdocs/open-mcp", "desc": "快速将 Web API 转换为 MCP 服务器"},
        {"name": "MetaMCP", "url": "https://github.com/metatool-ai/metatool-app", "desc": "通过 GUI 管理 MCP 连接的中间件服务器"},
        {"name": "PersonalizationMCP", "url": "https://github.com/YangLiangwei/PersonalizationMCP", "desc": "集成 Steam, YouTube, Spotify 等平台的个人数据聚合"},
    ],
    "浏览器自动化 (Browser Automation)": [
        {"name": "server-puppeteer", "url": "https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer", "desc": "官方实现的网页抓取和交互"},
        {"name": "mcp-playwright", "url": "https://github.com/executeautomation/mcp-playwright", "desc": "基于 Playwright 的浏览器自动化"},
        {"name": "browser-use-rs", "url": "https://github.com/BB-fat/browser-use-rs", "desc": "基于 Rust 的轻量级浏览器自动化"},
        {"name": "web-search", "url": "https://github.com/pskill9/web-search", "desc": "支持免费 Google 搜索的服务器"},
    ],
    "艺术与文化 (Art and Culture)": [
        {"name": "rijksmuseum-mcp", "url": "https://github.com/r-huijts/rijksmuseum-mcp", "desc": "荷兰国立博物馆 API 集成"},
        {"name": "bazi-mcp", "url": "https://github.com/cantian-ai/bazi-mcp", "desc": "提供八字排盘和测算信息"},
        {"name": "ani-mcp", "url": "https://github.com/gavxm/ani-mcp", "desc": "AniList 集成，用于动漫推荐和管理"},
    ],
    "生物学/医学/生物信息学 (Bio, Medical & Bioinformatics)": [
        {"name": "biomcp", "url": "https://github.com/genomoncology/biomcp", "desc": "访问 PubMed, ClinicalTrials.gov"},
        {"name": "fhir-mcp-server", "url": "https://github.com/wso2/fhir-mcp-server", "desc": "FHIR API 集成，支持临床医疗数据分析"},
        {"name": "gget-mcp", "url": "https://github.com/longevity-genie/gget-mcp", "desc": "强大的生物信息学基因组查询工具"},
    ],
    "云平台 (Cloud Platforms)": [
        {"name": "Cloudflare MCP Server", "url": "https://github.com/cloudflare/mcp-server-cloudflare", "desc": "Cloudflare Workers, KV, R2 集成"},
        {"name": "mcp-k8s-go", "url": "https://github.com/strowk/mcp-k8s-go", "desc": "通过 MCP 操作 Kubernetes 集群"},
        {"name": "alibaba-cloud-ops-mcp-server", "url": "https://github.com/aliyun/alibaba-cloud-ops-mcp-server", "desc": "阿里云资源运维管理"},
        {"name": "tfmcp", "url": "https://github.com/nwiizo/tfmcp", "desc": "Terraform 环境管理和状态分析"},
    ],
    "编程智能体 (Coding Agents)": [
        {"name": "leetcode-mcp-server", "url": "https://github.com/jinzcdev/leetcode-mcp-server", "desc": "LeetCode 题目获取、解题及提交记录分析"},
    ],
    "命令行 (Command Line)": [
        {"name": "openclaw-mcp", "url": "https://github.com/freema/openclaw-mcp", "desc": "集成 OpenClaw AI 助手"},
        {"name": "iterm-mcp", "url": "https://github.com/ferrislucas/iterm-mcp", "desc": "iTerm 终端访问与交互"},
        {"name": "mcp-shell-server", "url": "https://github.com/tumf/mcp-shell-server", "desc": "安全的 Shell 命令执行服务器"},
    ],
    "社交与通讯 (Communication)": [
        {"name": "server-slack", "url": "https://github.com/modelcontextprotocol/servers/tree/main/src/slack", "desc": "Slack 频道管理和消息传递"},
        {"name": "line-bot-mcp-server", "url": "https://github.com/line/line-bot-mcp-server", "desc": "LINE 官方账号集成"},
        {"name": "open-feishu-mcp-server", "url": "https://github.com/ztxtxwd/open-feishu-mcp-server", "desc": "飞书文档管理工具"},
        {"name": "inbox-zero", "url": "https://github.com/elie222/inbox-zero/tree/main/apps/mcp-server", "desc": "Gmail 邮件管理"},
    ],
    "客户数据平台 (Customer Data Platforms)": [
        {"name": "mcp-server-iaptic", "url": "https://github.com/iaptic/mcp-server-iaptic", "desc": "查询客户购买记录和营收统计"},
        {"name": "mcp-server-chart", "url": "https://github.com/antvis/mcp-server-chart", "desc": "基于 AntV 生成数据可视化图表"},
        {"name": "mcp-echarts", "url": "https://github.com/hustcc/mcp-echarts", "desc": "AI 动态生成 ECharts 可视化图表"},
    ],
    "数据库 (Databases)": [
        {"name": "server-postgres", "url": "https://github.com/modelcontextprotocol/servers-archived/tree/main/src/postgres", "desc": "PostgreSQL 官方集成"},
        {"name": "server-sqlite", "url": "https://github.com/modelcontextprotocol/servers-archived/tree/main/src/sqlite", "desc": "SQLite 官方集成，内置分析功能"},
        {"name": "postgres-mcp", "url": "https://github.com/crystaldba/postgres-mcp", "desc": "全能型 Postgres 开发运维工具"},
        {"name": "mysql_mcp_server", "url": "https://github.com/designcomputer/mysql_mcp_server", "desc": "MySQL 集成，支持可配置访问控制"},
        {"name": "vikingdb-mcp-server", "url": "https://github.com/KashiwaByte/vikingdb-mcp-server", "desc": "VikingDB 向量存储和查询"},
        {"name": "mcp-server-qdrant", "url": "https://github.com/qdrant/mcp-server-qdrant", "desc": "Qdrant 向量数据库集成"},
    ],
    "数据平台 (Data Platforms)": [
        {"name": "mcp-flowcore-platform", "url": "https://github.com/flowcore-io/mcp-flowcore-platform", "desc": "通过自然语言执行数据操作和分析"},
    ],
    "开发者工具 (Developer Tools)": [
        {"name": "Figma-Context-MCP", "url": "https://github.com/GLips/Figma-Context-MCP", "desc": "为编码代理提供 Figma 数据访问"},
        {"name": "openapi-mcp-server", "url": "https://github.com/snaggle-ai/openapi-mcp-server", "desc": "基于 OpenAPI 规范连接 HTTP/REST API"},
        {"name": "mcpProxy", "url": "https://github.com/JetBrains/mcpProxy", "desc": "连接 JetBrains IDE"},
        {"name": "dash-mcp-server", "url": "https://github.com/Kapeli/dash-mcp-server", "desc": "macOS API 文档浏览器 Dash 的集成"},
        {"name": "godoc-mcp-server", "url": "https://github.com/yikaiia/godoc-mcp-server", "desc": "查询 Golang 包文档"},
    ],
    "数据科学工具 (Data Science Tools)": [
        {"name": "fermat-mcp", "url": "https://github.com/abhiphile/fermat-mcp", "desc": "统一 SymPy, NumPy 和 Matplotlib 的数学引擎"},
        {"name": "dingo", "url": "https://github.com/DataEval/dingo", "desc": "数据质量评估工具"},
    ],
    "文件系统 (File Systems)": [
        {"name": "server-filesystem", "url": "https://github.com/modelcontextprotocol/servers-archived/tree/main/src/filesystem", "desc": "直接访问本地文件系统"},
        {"name": "server-google-drive", "url": "https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive", "desc": "Google Drive 集成"},
        {"name": "smart-tree", "url": "https://github.com/8b-is/smart-tree", "desc": "AI 原生目录可视化"},
    ],
    "金融与金融科技 (Finance & Fintech)": [
        {"name": "base-mcp", "url": "https://github.com/base/base-mcp", "desc": "Base 网络链上工具集成（钱包、DeFi）"},
        {"name": "coincap-mcp", "url": "https://github.com/QuantGeekDev/coincap-mcp", "desc": "实时加密货币市场数据"},
        {"name": "evm-mcp-server", "url": "https://github.com/mcpdotdirect/evm-mcp-server", "desc": "支持 30+ EVM 网络的区块链服务"},
        {"name": "cryptopanic-mcp", "url": "https://github.com/kukapay/cryptopanic-mcp", "desc": "加密货币新闻聚合"},
    ],
    "游戏 (Gaming)": [
        {"name": "godot-mcp", "url": "https://github.com/Coding-Solo/godot-mcp", "desc": "Godot 游戏引擎交互"},
        {"name": "mcp-unity", "url": "https://github.com/CoderGamester/mcp-unity", "desc": "Unity3d 游戏引擎集成"},
        {"name": "opgg-mcp", "url": "https://github.com/opgginc/opgg-mcp", "desc": "英雄联盟等热门游戏实时数据分析"},
    ],
    "知识与记忆 (Knowledge & Memory)": [
        {"name": "server-memory", "url": "https://github.com/modelcontextprotocol/servers-archived/tree/main/src/memory", "desc": "基于知识图谱的长期记忆系统"},
        {"name": "ApeRAG", "url": "https://github.com/apecloud/ApeRAG", "desc": "生产级 RAG 平台，结合 Graph RAG 和向量搜索"},
        {"name": "mem0-mcp", "url": "https://github.com/mem0ai/mem0-mcp", "desc": "管理编码偏好和代码实现记忆"},
    ],
    "法律 (Legal)": [
        {"name": "us-legal-mcp", "url": "https://github.com/JamesANZ/us-legal-mcp", "desc": "提供全面的美国法规数据"},
    ],
    "位置服务 (Location Services)": [
        {"name": "server-google-maps", "url": "https://github.com/modelcontextprotocol/servers-archived/tree/main/src/google-maps", "desc": "Google 地图集成"},
        {"name": "cesium-mcp", "url": "https://github.com/gaopengbin/cesium-mcp", "desc": "AI 操控三维地球 (CesiumJS)"},
        {"name": "MCP-Geo", "url": "https://github.com/webcoderz/MCP-Geo", "desc": "支持 Nominatim, ArcGIS, Bing 的地理编码"},
    ],
    "营销 (Marketing)": [
        {"name": "tiktok-ads-mcp-server", "url": "https://github.com/AdsMCP/tiktok-ads-mcp-server", "desc": "TikTok 广告活动管理"},
    ],
    "监测 (Monitoring)": [
        {"name": "server-sentry", "url": "https://github.com/modelcontextprotocol/servers/tree/main/src/sentry", "desc": "Sentry 错误跟踪集成"},
        {"name": "mcp-grafana", "url": "https://github.com/grafana/mcp-grafana", "desc": "Grafana 仪表盘搜索和数据查询"},
        {"name": "logfire-mcp", "url": "https://github.com/pydantic/logfire-mcp", "desc": "OpenTelemetry 追踪和指标访问"},
    ],
    "搜索 (Search)": [
        {"name": "brave-search-mcp-server", "url": "https://github.com/brave/brave-search-mcp-server", "desc": "Brave 搜索 API 集成"},
        {"name": "exa-mcp-server", "url": "https://github.com/exa-labs/exa-mcp-server", "desc": "Exa AI 搜索 API 集成"},
        {"name": "arxiv-mcp-server", "url": "https://github.com/blazickjp/arxiv-mcp-server", "desc": "搜索 ArXiv 研究论文"},
        {"name": "mcp-server-rag-web-browser", "url": "https://github.com/apify/mcp-server-rag-web-browser", "desc": "网页搜索、抓取并返回 Markdown"},
    ],
    "安全 (Security)": [
        {"name": "Wireshark-MCP", "url": "https://github.com/bx33661/Wireshark-MCP", "desc": "Wireshark 网络数据包分析"},
        {"name": "binary_ninja_mcp", "url": "https://github.com/Vector35/binaryninja-mcp", "desc": "Binary Ninja 二进制分析"},
        {"name": "mcp-shodan", "url": "https://github.com/BurtTheCoder/mcp-shodan", "desc": "Shodan 资产和漏洞查询"},
        {"name": "mcp-virustotal", "url": "https://github.com/BurtTheCoder/mcp-virustotal", "desc": "VirusTotal 文件/URL 扫描"},
    ],
    "嵌入式系统 (Embedded Systems)": [
        {"name": "embedded-debugger-mcp", "url": "https://github.com/adancurusul/embedded-debugger-mcp", "desc": "基于 probe-rs 的 ARM/RISC-V 调试"},
        {"name": "serial-mcp-server", "url": "https://github.com/adancurusul/serial-mcp-server", "desc": "串口通信 MCP 服务器"},
    ],
    "客户支持与服务管理 (Support and Service Management)": [
        {"name": "freshdesk-mcp", "url": "https://github.com/effytech/freshdesk_mcp", "desc": "Freshdesk 支持操作集成"},
        {"name": "jira-mcp", "url": "https://github.com/nguyenvanduocit/jira-mcp", "desc": "Jira 问题管理和 Sprint 计划"},
    ],
    "体育 (Sports)": [
        {"name": "firstcycling-mcp", "url": "https://github.com/r-huijts/firstcycling-mcp", "desc": "自行车比赛数据访问"},
    ],
    "翻译服务 (Translation Services)": [
        {"name": "lara-mcp", "url": "https://github.com/translated/lara-mcp", "desc": "Lara 翻译 API 集成"},
    ],
    "旅行与交通 (Travel and Transportation)": [
        {"name": "mcp-server-airbnb", "url": "https://github.com/openbnb-org/mcp-server-airbnb", "desc": "Airbnb 房源搜索"},
        {"name": "ns-mcp-server", "url": "https://github.com/r-huijts/ns-mcp-server", "desc": "荷兰铁路信息"},
    ],
    "版本控制 (Version Control)": [
        {"name": "server-github", "url": "https://github.com/modelcontextprotocol/servers-archived/tree/main/src/github", "desc": "GitHub API 集成"},
        {"name": "server-gitlab", "url": "https://github.com/modelcontextprotocol/servers-archived/tree/main/src/gitlab", "desc": "GitLab 平台集成"},
        {"name": "server-git", "url": "https://github.com/modelcontextprotocol/servers-archived/tree/main/src/git", "desc": "本地 Git 仓库操作"},
    ],
    "其他工具和集成 (Other Tools and Integrations)": [
        {"name": "homeassistant-mcp", "url": "https://github.com/tevonsb/homeassistant-mcp", "desc": "Home Assistant 智能家居控制"},
        {"name": "notion_mcp", "url": "https://github.com/danhilse/notion_mcp", "desc": "Notion API 集成"},
        {"name": "qrcode_mcp", "url": "https://github.com/2niuhe/qrcode_mcp", "desc": "QR 码生成"},
        {"name": "mcp-miro", "url": "https://github.com/evalstate/mcp-miro", "desc": "Miro 白板访问"},
        {"name": "mcp-manager", "url": "https://github.com/zueai/mcp-manager", "desc": "MCP 服务器 Web UI 管理"},
    ],
}


def normalize(text):
    """归一化文本：转为小写，移除多余空格"""
    return " ".join((text or "").lower().split())


def search(keyword):
    """按关键词搜索 MCP 服务器"""
    kw = normalize(keyword)
    if not kw:
        return None  # 返回 None 表示列出全部

    results = []  # (分类名, 服务器列表)
    for category, servers in MCP_DATA.items():
        matched = []
        for srv in servers:
            # 在服务器名、描述、分类名中搜索
            if (kw in normalize(srv["name"]) or
                kw in normalize(srv["desc"]) or
                kw in normalize(category)):
                matched.append(srv)
        if matched:
            results.append((category, matched))
    return results


def print_results(results):
    """打印搜索结果"""
    if not results:
        print("未找到匹配的 MCP 服务器。")
        return

    print(f"找到 {sum(len(s) for _, s in results)} 个匹配的 MCP 服务器：\n")
    for category, servers in results:
        print(f"### {category}")
        for srv in servers:
            print(f"- **{srv['name']}** — {srv['desc']}")
            print(f"  🔗 {srv['url']}")
        print()


def print_all():
    """打印全部分类"""
    print("=" * 60)
    print("Awesome MCP Servers — 完整分类目录")
    print("=" * 60)
    total = 0
    for category, servers in MCP_DATA.items():
        total += len(servers)
        print(f"\n### {category} ({len(servers)} 个)")
        for srv in servers:
            print(f"  - {srv['name']}: {srv['desc']}")
    print(f"\n总计: {total} 个 MCP 服务器")
    print(f"完整列表: https://github.com/punkpeye/awesome-mcp-servers")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python search_mcp.py <关键词>")
        print("关键词为空时列出全部 MCP 服务器")
        print()
        print("示例:")
        print("  python search_mcp.py 数据库")
        print("  python search_mcp.py github")
        print("  python search_mcp.py finance")
        print("  python search_mcp.py 浏览器")
        print("  python search_mcp.py 搜索")
        print()
        print("=" * 60)
        print("30 大分类速览:")
        print("=" * 60)
        for i, cat in enumerate(MCP_DATA.keys(), 1):
            print(f"  {i}. {cat}")
        sys.exit(0)

    keyword = " ".join(sys.argv[1:])
    results = search(keyword)
    if results is None:
        print_all()
    else:
        print_results(results)

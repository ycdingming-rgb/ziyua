---
name: awesome-mcp-servers
description: 查询 Awesome MCP Servers 项目中 2700+ 个 MCP 服务器列表。支持按功能分类（聚合器、浏览器、数据库、金融、搜索、社交、安全、版本控制等）查找和安装 MCP 服务器。当用户提供 MCP 相关需求、想要扩展 AI 能力、或询问"有哪些 MCP 服务器"/"帮我找一个 MCP 实现 XX 功能的服务器"时触发。
agent_created: true
---

# Awesome MCP Servers

## 概述

Awesome MCP Servers 是 GitHub 上由 punkpeye 维护的权威 MCP 服务器资源集合，包含 2700+ 个经过分类和验证的 MCP 服务器实现。本技能提供快速查询和检索 MCP 服务器的能力，按功能分类覆盖从基础设施到垂直领域的广泛集成。

## 快速开始

当用户提出 MCP 相关需求时，使用 `scripts/search_mcp.py` 脚本按关键词搜索匹配的服务器：

```bash
python "C:/Users/Administrator/.workbuddy/skills/awesome-mcp-servers/scripts/search_mcp.py" <关键词>
```

示例：
```bash
python "C:/Users/Administrator/.workbuddy/skills/awesome-mcp-servers/scripts/search_mcp.py" 数据库
python "C:/Users/Administrator/.workbuddy/skills/awesome-mcp-servers/scripts/search_mcp.py" finance
python "C:/Users/Administrator/.workbuddy/skills/awesome-mcp-servers/scripts/search_mcp.py" github
```

## 分类目录速查

以下为完整的 30 大分类目录及重点服务器。当搜索脚本无法覆盖时，直接按以下目录定位。

### 1. 聚合器 (Aggregators)
通过单个 MCP 服务器访问多个应用程序和工具。
- **agent** — 统一的 MCP 服务器，聚合多个 MCP 服务器
- **OpenMCP** — 快速将 Web API 转换为 MCP 服务器
- **MetaMCP** — 通过 GUI 管理 MCP 连接的中间件服务器
- **PersonalizationMCP** — 集成 Steam, YouTube, Spotify 等个人数据

### 2. 浏览器自动化 (Browser Automation)
Web 内容访问、抓取和自动化操作。
- **server-puppeteer** — 官方实现的网页抓取和交互
- **mcp-playwright** — 基于 Playwright 的浏览器自动化
- **browser-use-rs** — 基于 Rust 的轻量级浏览器自动化
- **web-search** — 支持免费 Google 搜索的服务器

### 3. 艺术与文化 (Art and Culture)
艺术收藏、文化遗产及多媒体内容处理。
- **rijksmuseum-mcp** — 荷兰国立博物馆 API 集成
- **bazi-mcp** — 提供八字排盘和测算信息
- **ani-mcp** — AniList 集成，用于动漫推荐和管理

### 4. 生物学、医学和生物信息学 (Bio, Medical & Bioinformatics)
- **biomcp** — 访问 PubMed, ClinicalTrials.gov
- **fhir-mcp-server** — FHIR API 集成，支持临床医疗数据分析
- **gget-mcp** — 强大的生物信息学基因组查询工具

### 5. 云平台 (Cloud Platforms)
- **Cloudflare MCP Server** — Cloudflare Workers, KV, R2 集成
- **mcp-k8s-go** — 通过 MCP 操作 Kubernetes 集群
- **alibaba-cloud-ops-mcp-server** — 阿里云资源运维管理
- **tfmcp** — Terraform 环境管理和状态分析

### 6. 编程智能体 (Coding Agents)
- **leetcode-mcp-server** — LeetCode 题目获取、解题及提交记录分析

### 7. 命令行 (Command Line)
- **openclaw-mcp** — 集成 OpenClaw AI 助手
- **iterm-mcp** — iTerm 终端访问与交互
- **mcp-shell-server** — 安全的 Shell 命令执行服务器

### 8. 社交与通讯 (Communication)
- **server-slack** — Slack 频道管理和消息传递
- **line-bot-mcp-server** — LINE 官方账号集成
- **open-feishu-mcp-server** — 飞书文档管理工具
- **inbox-zero** — Gmail 邮件管理（识别需回复邮件）

### 9. 客户数据平台 (Customer Data Platforms)
- **iaptic/mcp-server-iaptic** — 查询客户购买记录和营收统计
- **mcp-server-chart** — 基于 AntV 生成数据可视化图表
- **mcp-echarts** — AI 动态生成 ECharts 可视化图表

### 10. 数据库 (Databases)
支持多种数据库的连接、查询、分析及安全访问控制。
- **server-postgres** — PostgreSQL 官方集成
- **server-sqlite** — SQLite 官方集成，内置分析功能
- **postgres-mcp** — 全能型 Postgres 开发运维工具
- **mysql_mcp_server** — MySQL 集成，支持可配置访问控制
- **vikingdb-mcp-server** — VikingDB 向量存储和查询
- **mcp-server-qdrant** — Qdrant 向量数据库集成

### 11. 数据平台 (Data Platforms)
- **mcp-flowcore-platform** — 通过自然语言执行数据操作和分析

### 12. 开发者工具 (Developer Tools)
- **Figma-Context-MCP** — 为编码代理提供 Figma 数据访问
- **openapi-mcp-server** — 基于 OpenAPI 规范连接 HTTP/REST API
- **mcpProxy** — 连接 JetBrains IDE
- **dash-mcp-server** — macOS API 文档浏览器 Dash 的集成
- **godoc-mcp-server** — 查询 Golang 包文档

### 13. 数据科学工具 (Data Science Tools)
- **fermat-mcp** — 统一 SymPy, NumPy 和 Matplotlib 的数学引擎
- **dingo** — 数据质量评估工具

### 14. 文件系统 (File Systems)
- **server-filesystem** — 直接访问本地文件系统
- **server-google-drive** — Google Drive 集成
- **smart-tree** — AI 原生目录可视化

### 15. 金融与金融科技 (Finance & Fintech)
- **base-mcp** — Base 网络链上工具集成（钱包、DeFi）
- **coincap-mcp** — 实时加密货币市场数据
- **evm-mcp-server** — 支持 30+ EVM 网络的区块链服务
- **cryptopanic-mcp** — 加密货币新闻聚合

### 16. 游戏 (Gaming)
- **godot-mcp** — Godot 游戏引擎交互
- **mcp-unity** — Unity3d 游戏引擎集成
- **opgg-mcp** — 英雄联盟等热门游戏实时数据分析

### 17. 知识与记忆 (Knowledge & Memory)
- **server-memory** — 基于知识图谱的长期记忆系统
- **ApeRAG** — 生产级 RAG 平台，结合 Graph RAG 和向量搜索
- **mem0-mcp** — 管理编码偏好和代码实现记忆

### 18. 法律 (Legal)
- **us-legal-mcp** — 提供全面的美国法规数据

### 19. 位置服务 (Location Services)
- **server-google-maps** — Google 地图集成
- **cesium-mcp** — AI 操控三维地球 (CesiumJS)
- **MCP-Geo** — 支持 Nominatim, ArcGIS, Bing 的地理编码

### 20. 营销 (Marketing)
- **tiktok-ads-mcp-server** — TikTok 广告活动管理

### 21. 监测 (Monitoring)
- **server-sentry** — Sentry 错误跟踪集成
- **mcp-grafana** — Grafana 仪表盘搜索和数据查询
- **logfire-mcp** — OpenTelemetry 追踪和指标访问

### 22. 搜索 (Search)
- **brave-search-mcp-server** — Brave 搜索 API 集成
- **exa-mcp-server** — Exa AI 搜索 API 集成
- **arxiv-mcp-server** — 搜索 ArXiv 研究论文
- **mcp-server-rag-web-browser** — 网页搜索、抓取并返回 Markdown

### 23. 安全 (Security)
- **Wireshark-MCP** — Wireshark 网络数据包分析
- **binary_ninja_mcp** — Binary Ninja 二进制分析
- **mcp-shodan** — Shodan 资产和漏洞查询
- **mcp-virustotal** — VirusTotal 文件/URL 扫描

### 24. 嵌入式系统 (Embedded Systems)
- **embedded-debugger-mcp** — 基于 probe-rs 的 ARM/RISC-V 调试
- **serial-mcp-server** — 串口通信 MCP 服务器

### 25. 客户支持与服务管理 (Support and Service Management)
- **freshdesk-mcp** — Freshdesk 支持操作集成
- **jira-mcp** — Jira 问题管理和 Sprint 计划

### 26. 体育 (Sports)
- **firstcycling-mcp** — 自行车比赛数据访问

### 27. 翻译服务 (Translation Services)
- **lara-mcp** — Lara 翻译 API 集成，支持上下文感知翻译

### 28. 旅行与交通 (Travel and Transportation)
- **mcp-server-airbnb** — Airbnb 房源搜索
- **ns-mcp-server** — 荷兰铁路信息

### 29. 版本控制 (Version Control)
- **server-github** — GitHub API 集成
- **server-gitlab** — GitLab 平台集成
- **server-git** — 本地 Git 仓库操作

### 30. 其他工具和集成 (Other Tools and Integrations)
- **homeassistant-mcp** — Home Assistant 智能家居控制
- **notion_mcp** — Notion API 集成，管理待办事项
- **qrcode_mcp** — QR 码生成
- **mcp-miro** — Miro 白板访问
- **mcp-manager** — 简单的 Web UI 用于管理 MCP 服务器

## 框架与基础设施

构建 MCP 服务器的框架：
- **Python**: FastMCP
- **TypeScript/JavaScript**: FastMCP, LiteMCP
- **Go**: Foxy Contexts, mcp-go
- **Java**: Spring AI MCP, Quarkus MCP
- **.NET**: ModelContextProtocol.NET

## 使用说明

- 服务器实现语言标识：🐍 Python / 📇 TypeScript / 🏎️ Go / 🦀 Rust / ☁️ 云服务 / 🏠 本地服务 / 🎖️ 官方实现
- 完整列表及更多详情访问：https://github.com/punkpeye/awesome-mcp-servers/blob/main/README-zh.md

## 资源

- **scripts/search_mcp.py** — 按关键词搜索 MCP 服务器，返回匹配结果、分类和 GitHub 链接

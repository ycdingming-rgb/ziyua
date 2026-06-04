📋 项目概述
awesome-mcp-servers 是由 punkpeye 维护的权威 MCP（Model Context Protocol）服务器资源集合，包含 2700+ 个经过分类和验证的 MCP 服务器实现，涵盖生产和实验性服务器。

📂 完整分类目录
1. 🔗 聚合器 (Aggregators)
通过单个 MCP 服务器访问多个应用程序

1mcp/agent — 统一 MCP 服务器，聚合多个 MCP 服务器
OpenMCP — 快速将 Web API 转换为 MCP 服务器
MetaMCP — 通过 GUI 管理 MCP 连接的中间件
PersonalizationMCP — 集成 Steam、YouTube、Spotify 等个人数据
2. 🌐 浏览器自动化 (Browser Automation)
server-puppeteer — 官方网页抓取和交互
playwright-mcp-server — 基于 Playwright 的浏览器自动化
browser-use-rs — 基于 Rust 的轻量级浏览器自动化
web-search — 支持免费 Google 搜索
3. 🎨 艺术与文化 (Art and Culture)
rijksmuseum-mcp — 荷兰国立博物馆 API
bazi-mcp — 八字排盘和测算
ani-mcp — AniList 动漫推荐和管理
4. 🧬 生物医学 (Bio, Medical & Bioinformatics)
biomcp — 访问 PubMed、ClinicalTrials.gov
fhir-mcp-server — FHIR API 临床医疗数据分析
gget-mcp — 生物信息学基因组查询
5. ☁️ 云平台 (Cloud Platforms)
cloudflare/mcp-server-cloudflare — Cloudflare Workers/KV/R2
mcp-k8s-go — 操作 Kubernetes 集群
alibaba-cloud-ops-mcp-server — 阿里云资源运维
tfmcp — Terraform 环境管理
6. 💻 编程智能体 (Coding Agents)
leetcode-mcp-server — LeetCode 题目获取、解题和提交
7. 🖥️ 命令行 (Command Line)
openclaw-mcp — 集成 OpenClaw AI 助手
iterm-mcp — iTerm 终端访问
mcp-shell-server — 安全的 Shell 命令执行
8. 💬 社交与通讯 (Communication)
server-slack — Slack 频道管理和消息
line-bot-mcp-server — LINE 官方账号集成
open-feishu-mcp-server — 飞书文档管理
inbox-zero — Gmail 邮件管理
9. 👤 客户数据平台 (CDP)
mcp-server-iaptic — 客户购买记录和营收统计
mcp-server-chart — 基于 AntV 生成数据可视化图表
mcp-echarts — AI 动态生成 ECharts 图表
10. 🗄️ 数据库 (Databases)
server-postgres — PostgreSQL 官方集成
server-sqlite — SQLite 官方集成
postgres-mcp — 全能 Postgres 开发运维
mysql_mcp_server — MySQL 集成
vikingdb-mcp-server — VikingDB 向量存储
mcp-server-qdrant — Qdrant 向量数据库
11. 💾 数据平台 (Data Platforms)
mcp-flowcore-platform — 自然语言数据操作和分析
12. 💻 开发者工具 (Developer Tools)
Figma-Context-MCP — Figma 数据访问
openapi-mcp-server — 基于 OpenAPI 连接 REST API
mcpProxy — 连接 JetBrains IDE
dash-mcp-server — Dash API 文档浏览器
godoc-mcp-server — 查询 Go 包文档
13. 🧮 数据科学 (Data Science)
fermat-mcp — 统一 SymPy、NumPy、Matplotlib
dingo — 数据质量评估工具
14. 📂 文件系统 (File Systems)
server-filesystem — 本地文件系统直接访问
server-google-drive — Google Drive 集成
smart-tree — AI 原生目录可视化
15. 💰 金融与金融科技 (Finance & Fintech)
base-mcp — Base 链上工具（钱包、DeFi）
coincap-mcp — 实时加密货币市场数据
evm-mcp-server — 支持 30+ EVM 网络
cryptopanic-mcp — 加密货币新闻聚合
16. 🎮 游戏 (Gaming)
godot-mcp — Godot 游戏引擎
mcp-unity — Unity3D 引擎集成
opgg-mcp — 英雄联盟等游戏实时数据分析
17. 🧠 知识与记忆 (Knowledge & Memory)
server-memory — 基于知识图谱的长期记忆
ApeRAG — 生产级 RAG 平台
mem0-mcp — 管理编码偏好和代码实现记忆
18. ⚖️ 法律 (Legal)
us-legal-mcp — 美国法规数据
19. 🗺️ 位置服务 (Location Services)
server-google-maps — Google 地图集成
cesium-mcp — AI 操控三维地球 CesiumJS
MCP-Geo — 多源地理编码
20. 🎯 营销 (Marketing)
tiktok-ads-mcp-server — TikTok 广告活动管理
21. 📊 监测 (Monitoring)
server-sentry — Sentry 错误跟踪
mcp-grafana — Grafana 仪表盘搜索
logfire-mcp — OpenTelemetry 追踪
22. 🔎 搜索 (Search)
brave-search-mcp-server — Brave 搜索 API
exa-mcp-server — Exa AI 搜索 API
arxiv-mcp-server — ArXiv 研究论文搜索
mcp-server-rag-web-browser — 网页搜索和抓取
23. 🔒 安全 (Security)
Wireshark-MCP — 网络数据包分析
binary_ninja_mcp — 二进制分析
mcp-shodan — Shodan 资产和漏洞查询
mcp-virustotal — VirusTotal 文件/URL 扫描
24. 📟 嵌入式系统 (Embedded Systems)
embedded-debugger-mcp — ARM/RISC-V 调试
serial-mcp-server — 串口通信
25. 🎧 客户支持 (Support and Service Management)
freshdesk-mcp — Freshdesk 支持操作
jira-mcp — Jira 问题管理和 Sprint 计划
26. 🏃 体育 (Sports)
firstcycling-mcp — 自行车比赛数据
27. 🌎 翻译服务 (Translation)
lara-mcp — Lara 翻译 API，上下文感知翻译
28. 🚆 旅行与交通 (Travel)
mcp-server-airbnb — Airbnb 房源搜索
ns-mcp-server — 荷兰铁路信息
29. 🔄 版本控制 (Version Control)
server-github — GitHub API 集成
server-gitlab — GitLab 平台集成
server-git — 本地 Git 仓库操作
30. 🛠️ 其他工具 (Other Tools)
homeassistant-mcp — Home Assistant 智能家居
notion_mcp — Notion API 集成
qrcode_mcp — QR 码生成
mcp-miro — Miro 白板访问
mcp-manager — Web UI 管理 MCP 服务器
🏗️ 框架与基础设施
语言	框架
🐍 Python	FastMCP
📇 TypeScript	FastMCP, LiteMCP
🏎️ Go	Foxy Contexts, mcp-go
☕ Java	Spring AI MCP, Quarkus MCP
🔷 .NET	ModelContextProtocol.NET
🦀 Rust	多个原生实现

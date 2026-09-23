# -*- coding: utf-8 -*-
"""Build full i18n dict and wire data-i18n onto all site HTML main content."""
from __future__ import annotations

import html as html_lib
import json
import re
from pathlib import Path

ROOT = Path(r"C:\Users\saran\OneDrive\Desktop\메스도스랩-홈페이지")

# key -> {ko, en, zh}
T: dict[str, dict[str, str]] = {}


def add(key: str, ko: str, en: str, zh: str) -> None:
    T[key] = {"ko": ko, "en": en, "zh": zh}


# --- load existing keys from i18n-dict.js via regex is hard; redefine core + new ---
# Nav / shared (keep compatible with existing HTML data-i18n keys)
add("nav.aria", "주 메뉴", "Main menu", "主导航")
add("nav.products", "제품", "Products", "产品")
add("nav.download", "다운로드", "Download", "下载")
add("nav.learn", "학습", "Learn", "学习")
add("nav.community", "커뮤니티", "Community", "社区")
add("nav.about", "소개", "About", "关于")
add("nav.desktop", "Desktop · 설치형", "Desktop · Install", "Desktop · 安装版")
add("nav.cloud", "Cloud · SaaS", "Cloud · SaaS", "Cloud · SaaS")
add("nav.basic.desc", "통계분석 프로그램", "Statistics analysis", "统计分析程序")
add("nav.q.desc", "Q방법론 분석", "Q methodology", "Q方法分析")
add("nav.g.desc", "근거이론 분석", "Grounded theory", "扎根理论分析")
add("nav.methodos.desc", "절차적 단계 AI 연구방법", "Procedural AI research methods", "程序性 AI 研究方法")
add("nav.studiumr.desc", "End-to-End AI Research OS", "End-to-End AI Research OS", "端到端 AI Research OS")
add("nav.compare", "제품 비교", "Compare", "产品比较")
add("nav.compare.desc", "Desktop / SaaS 한눈에", "Desktop / SaaS at a glance", "Desktop / SaaS 一览")
add("nav.desktopInstall", "Desktop 설치", "Desktop install", "Desktop 安装")
add("nav.desktopInstall.desc", "basic · Q · G", "basic · Q · G", "basic · Q · G")
add("nav.cloudStart", "Cloud 시작", "Start on Cloud", "Cloud 开始")
add("nav.cloudStart.desc", "methodos · StudiumR", "methodos · StudiumR", "methodos · StudiumR")
add("nav.requirements", "시스템 요구사항", "System requirements", "系统要求")
add("nav.requirements.desc", "권장 사양", "Recommended specs", "推荐配置")
add("nav.gettingStarted", "시작하기", "Getting started", "快速开始")
add("nav.gettingStarted.desc", "첫 실행 가이드", "First-run guide", "首次运行指南")
add("nav.guides", "사용자 가이드", "User guides", "用户指南")
add("nav.guides.desc", "가이드", "Guides", "指南")
add("nav.tutorials", "튜토리얼", "Tutorials", "教程")
add("nav.tutorials.desc", "영상", "Videos", "视频")
add("nav.blog", "블로그", "Blog", "博客")
add("nav.blog.desc", "소식", "News", "动态")
add("nav.lab.desc", "연구소 소개", "About the lab", "实验室介绍")
add("nav.mission", "미션", "Mission", "使命")
add("nav.mission.desc", "비전과 목표", "Vision & goals", "愿景与目标")
add("nav.contact", "문의", "Contact", "联系")
add("nav.cta", "StudiumR 열기", "Open StudiumR", "打开 StudiumR")
add("nav.methodosOpen", "methodos 열기", "Open methodos", "打开 methodos")
add("nav.menu", "메뉴 열기", "Open menu", "打开菜单")
add("nav.productsOverview", "제품 개요", "Products overview", "产品概览")
add("nav.downloadHome", "다운로드 홈", "Download home", "下载首页")
add("footer.blurb", "연구방법을 위한 Desktop 분석 도구와 AI Research SaaS를 만드는 연구소입니다.", "A lab building desktop analysis tools and AI Research SaaS for research methods.", "打造研究方法用 Desktop 分析工具与 AI Research SaaS 的实验室。")
add("footer.resources", "Resources", "Resources", "资源")
add("footer.lab", "Lab", "Lab", "实验室")
add("footer.tag", "Research methods · Desktop & SaaS", "Research methods · Desktop & SaaS", "研究方法 · Desktop & SaaS")
add("crumb.home", "홈", "Home", "首页")
add("page.products", "제품", "Products", "产品")
add("page.download", "다운로드", "Download", "下载")
add("page.learn", "학습", "Learn", "学习")
add("page.about", "소개", "About", "关于")
add("page.community", "커뮤니티", "Community", "社区")
add("page.mission", "미션", "Mission", "使命")
add("page.contact", "문의", "Contact", "联系")
add("page.blog", "블로그", "Blog", "博客")
add("page.guides", "사용자 가이드", "User guides", "用户指南")
add("page.gettingStarted", "시작하기", "Getting started", "快速开始")
add("page.tutorials", "튜토리얼", "Tutorials", "教程")
add("page.compare", "제품 비교", "Compare products", "产品比较")
add("page.requirements", "시스템 요구사항", "System requirements", "系统要求")
add("common.learnMore", "자세히 보기", "Learn more", "了解更多")
add("common.open", "열기", "Open", "打开")
add("common.download", "다운로드", "Download", "下载")
add("common.more", "더보기", "More", "更多")
add("common.atAGlance", "한눈에", "At a glance", "一览")
add("common.downloadGuide", "다운로드 안내", "Download guide", "下载说明")
add("common.shortcuts", "바로가기", "Shortcuts", "快捷入口")
add("common.artifacts", "배포물", "Binaries", "发布包")
add("common.liveLinks", "라이브 링크", "Live links", "在线链接")
add("common.live", "실시간 지원", "Realtime support", "实时支持")
add("common.openApp", "앱 열기", "Open app", "打开应用")
add("common.productPage", "제품 페이지", "Product page", "产品页")
add("common.desktopDownload", "Desktop 다운로드", "Desktop download", "Desktop 下载")
add("common.installed", "설치형", "Installer", "安装版")
add("common.portable", "실행형", "Portable", "便携版")
add("desc.stats", "통계분석", "Statistics", "统计分析")
add("desc.q", "Q방법론", "Q methodology", "Q方法")
add("desc.gt", "근거이론", "Grounded theory", "扎根理论")
add("desc.methodosOs", "연구방법 OS", "Research methods OS", "研究方法 OS")
add("cta.compareView", "제품 비교 보기", "View product comparison", "查看产品比较")
add("cta.tutorialsHowTo", "튜토리얼 · 실행방법", "Tutorials · How-to", "教程 · 使用方法")
add("guide.switcherAll", "전체", "All", "全部")
add("crumb.compare", "비교", "Compare", "比较")
add("crumb.requirements", "요구사항", "Requirements", "要求")
add("crumb.guides", "가이드", "Guides", "指南")

# Home
add(
    "home.h1",
    "Methodos Lab은 연구 분석 방법, 문헌 연구, 논문 집필 과정에서 발생하는 복잡한 문제들을 근거 기반 AI와 절차적 솔루션으로 체계적으로 해결합니다. 이를 통해 연구자는 보다 효율적이고 신뢰성 있는 학술 성과를 도출할 수 있게 합니다.",
    "Methodos Lab systematically solves complex problems in research analysis, literature work, and academic writing with evidence-based AI and procedural solutions—so researchers can produce more efficient, trustworthy scholarly outcomes.",
    "Methodos Lab 以循证 AI 与程序性方案，系统解决研究分析、文献研究与论文写作中的复杂问题，帮助研究者更高效、更可靠地产出学术成果。",
)
add(
    "home.lead",
    "통계·Q방법론·근거이론 설치형 분석 프로그램과, 절차적 연구방법·엔드투엔드 AI Research SaaS까지 — 연구 실행에 필요한 도구를 Methodos Lab이 설계합니다.",
    "From desktop tools for statistics, Q methodology, and grounded theory to procedural methods and end-to-end AI Research SaaS — Methodos Lab designs the tools research needs.",
    "从统计、Q方法、扎根理论的安装型分析程序，到程序性研究与端到端 AI Research SaaS——Methodos Lab 设计研究所需的工具。",
)
add("home.ctaProducts", "제품 살펴보기", "Explore products", "查看产品")
add("home.ctaStudiumr", "StudiumR 바로가기", "Go to StudiumR", "前往 StudiumR")
add("home.ctaCompare", "제품 비교 보기", "View product comparison", "查看产品比较")
add("common.menuAlt", "메뉴", "Menu", "菜单")
add("gBasic.imgAlt", "Methodos Basic 소개", "Methodos Basic intro", "Methodos Basic 介绍")

add("home.productsTitle", "Methodos Lab 제품 구성", "Methodos Lab products", "Methodos Lab 产品构成")
add("home.productsSub", "Desktop용 프로그램과 SaaS용 프로그램으로 구성되어 있습니다.", "Desktop programs and SaaS products.", "由 Desktop 程序与 SaaS 产品组成。")
add("home.desktopTitle", "Desktop용 프로그램", "Desktop programs", "Desktop 程序")
add("home.desktopBody", "methodos-basic, methodosQ, methodosG로 구성되어 있습니다.", "Includes methodos-basic, methodosQ, and methodosG.", "包含 methodos-basic、methodosQ、methodosG。")
add("home.saasTitle", "SaaS용 프로그램", "SaaS programs", "SaaS 程序")
add("home.saasBody", "methodos, StudiumR로 구성되어 있습니다.", "Includes methodos and StudiumR.", "包含 methodos、StudiumR。")
add("home.flowTitle", "연구 흐름을 제품이 받쳐 줍니다", "Products support the research flow", "产品支撑研究流程")
add("home.flowSub", "방법 선택부터 분석·검증·논문 생산까지, Lab 제품이 단계별로 연결됩니다.", "From method choice to analysis, validation, and writing—Lab products connect each stage.", "从方法选择到分析、验证与论文产出，Lab 产品按阶段衔接。")
add("home.flow1", "방법 선택", "Choose a method", "方法选择")
add("home.flow1p", "methodos가 연구질문·자료유형에 맞는 연구방법을 추천합니다.", "methodos recommends methods that fit your question and data.", "methodos 根据研究问题与资料类型推荐方法。")
add("home.flow2", "전문 분석", "Specialized analysis", "专业分析")
add("home.flow2p", "통계·Q방법론·근거이론은 Desktop 제품으로 깊게 수행합니다.", "Statistics, Q methodology, and grounded theory run deeply on Desktop.", "统计、Q方法、扎根理论在 Desktop 产品中深入完成。")
add("home.flow3", "연구 프로세스", "Research process", "研究过程")
add("home.flow3p", "단계 워크벤치와 검토·검증으로 절차를 남깁니다.", "Stage workbenches leave a clear procedural trail with review and validation.", "阶段工作台与审阅验证留下清晰程序痕迹。")
add("home.flow4", "논문 생산", "Paper production", "论文产出")
add("home.flow4p", "StudiumR이 문헌·작성·크리틱까지 End-to-End로 이어 줍니다.", "StudiumR continues through literature, writing, and critique end-to-end.", "StudiumR 贯通文献、写作与批评，端到端衔接。")
add("home.secTitle", "로컬 우선 · 클라우드 메타데이터", "Local-first · cloud metadata", "本地优先 · 云端元数据")
add("home.secSub", "StudiumR·methodos와 같은 보안 중심 파일 체계를 Lab 전체의 원칙으로 둡니다.", "Security-minded file practice from StudiumR and methodos is a Lab-wide principle.", "以 StudiumR、methodos 同类的安全文件体系作为 Lab 共同原则。")
add("home.localTitle", "연구 산출물은 PC·브라우저에", "Research outputs stay on PC / browser", "研究成果留在 PC / 浏览器")
add("home.localBody", "Desktop 프로그램과 로컬 우선 SaaS가 민감 데이터를 사용자 쪽에 둡니다.", "Desktop apps and local-first SaaS keep sensitive data with the user.", "Desktop 与本地优先 SaaS 将敏感数据保留在用户侧。")
add("home.cloudTitle", "계정·협업 상태만 동기화", "Sync only account & collaboration state", "仅同步账号与协作状态")
add("home.cloudBody", "가벼운 메타데이터로 협업과 권한을 유지합니다.", "Light metadata keeps collaboration and permissions working.", "轻量元数据维系协作与权限。")
add("home.whyTitle", "연구분석도구를 쉽고 편리하고 근거있게", "Research analysis tools that are easy, practical, and evidence-based", "让研究分析工具更易用、更便捷、更有依据")
add("home.why1", "방법론 특화", "Method-specialized", "方法论专精")
add("home.why1p", "일반 통계를 넘어 Q방법론·근거이론 등 연구 분석 워크벤치를 제공합니다.", "Beyond general stats—dedicated workbenches for Q methodology and grounded theory.", "不止一般统计——提供 Q方法、扎根理论等研究分析工作台。")
add("home.why2", "AI와 절차의 결합", "AI with procedure", "AI 与程序结合")
add("home.why2p", "연구방법 추천부터 단계 실행까지, AI가 절차를 깨지 않고 돕습니다.", "From method recommendation to staged execution, AI helps without breaking procedure.", "从方法推荐到分步执行，AI 在不打断程序的前提下协助。")
add("home.why3", "연구자 데이터 주권", "Researcher data sovereignty", "研究者数据主权")
add("home.why3p", "설치형과 로컬 우선 SaaS로 연구 파일의 통제권을 사용자에게 둡니다.", "Installable apps and local-first SaaS keep control of research files with users.", "安装版与本地优先 SaaS 把研究文件掌控权交给用户。")
add("home.ctaBand", "지금 바로 SaaS를 열어보세요", "Open SaaS now", "立即打开 SaaS")
add("home.ctaBandP", "완성된 Cloud 제품은 즉시 실행할 수 있습니다. Desktop은 다운로드 페이지에서 안내합니다.", "Cloud products are ready to run. Desktop install guidance is on the Download page.", "Cloud 产品可立即使用。Desktop 安装说明见下载页。")

# Tutorials (existing)
add("tut.title", "튜토리얼 · 영상", "Tutorials · Video", "教程 · 视频")
add("tut.openGuide", "절차 가이드 열기", "Open procedure guide", "打开流程指南")
add("tut.videoGuide", "동영상 가이드", "Video guide", "视频指南")
add("tut.b1", "01 · methodos-basic 실행방법", "01 · methodos-basic how-to", "01 · methodos-basic 使用方法")
add("tut.b1p", "절차 A·B로 예제 분석과 학습 경로를 따라가 봅니다.", "Follow example analysis and learning paths with procedures A & B.", "通过流程 A·B 跟随示例分析与学习路径。")
add("tut.b1a", "절차 A · 예제를 통한 분석", "Path A · Analyze with examples", "流程 A · 通过示例分析")
add("tut.b1ap", "예제 자료 불러오기 → 기법 선택 → 변수·척도 → 분석 → 그래프·결과", "Load example → choose method → variables/scales → run → charts/results", "加载示例 → 选择方法 → 变量/尺度 → 运行 → 图表/结果")
add("tut.b1b", "절차 B · 학습으로 통계 익히기", "Path B · Learn statistics by practice", "流程 B · 通过学习掌握统计")
add("tut.b1bp", "명칭 → 초·중·고급 → 예제 확인 → 작업대 적용", "Names → beginner/mid/advanced → verify with examples → workbench", "名称 → 初/中/高级 → 用示例验证 → 工作台")
add("tut.q1", "02 · methodosQ 실행방법", "02 · methodosQ how-to", "02 · methodosQ 使用方法")
add("tut.q1p", "Q방법론 8단계·학습 트랙을 번호 절차로 따라갑니다.", "Follow Q methodology’s 8 stages and learning tracks step by step.", "按编号跟随 Q方法 8 阶段与学习轨道。")
add("tut.q1a", "절차 A · 예제로 Q분석", "Path A · Q analysis with examples", "流程 A · 用示例做 Q 分析")
add("tut.q1ap", "예제 → 포맷 → 내 자료 → 연구 8단계 → 해석·보고", "Example → format → your data → 8 research stages → interpretation", "示例 → 格式 → 我的资料 → 研究 8 步 → 解释报告")
add("tut.q1b", "절차 B · 학습 트랙", "Path B · Learning tracks", "流程 B · 学习轨道")
add("tut.q1bp", "입문 → 연구중 → 논문대비 → 개념사전 → 예제 확인", "Intro → in research → thesis prep → glossary → verify with examples", "入门 → 研究中 → 论文准备 → 概念词典 → 用示例验证")
add("tut.g1", "03 · methodosG 실행방법", "03 · methodosG how-to", "03 · methodosG 使用方法")
add("tut.g1p", "예제 자료(다문화 가족 사례)로 근거이론 코딩·이론화 절차를 따라갑니다.", "Follow grounded-theory coding and theorizing with the multicultural-family example.", "用示例资料（多文化家庭案例）跟随扎根理论编码与理论化。")
add("tut.g1a", "절차 A · 예제 → 코딩", "Path A · Example → coding", "流程 A · 示例 → 编码")
add("tut.g1ap", "예제 자료 → 문제 설정 → 근거자료 → 의미추출 → 범주연결 → 이론응축", "Examples → problem → evidence → meaning → categories → theory", "示例资料 → 问题设定 → 依据资料 → 意义提取 → 范畴联结 → 理论凝练")
add("tut.g1b", "절차 B · 이론화 → 보고", "Path B · Theorize → report", "流程 B · 理论化 → 报告")
add("tut.g1bp", "결과 그래프 → 이론 결과 → 절차형 실습 → 홈 진행 → 논문형 결과", "Result graphs → theory results → practice → home progress → thesis-style output", "结果图 → 理论结果 → 程序练习 → 主页进度 → 论文型结果")
add("tut.s1", "04 · methodos / StudiumR 실행방법", "04 · methodos / StudiumR how-to", "04 · methodos / StudiumR 使用方法")
add("tut.s1p", "Cloud SaaS에서 방법 추천·워크벤치와 AI Research 트랙을 절차로 익힙니다.", "Learn method recommendation, workbench, and AI research tracks on Cloud SaaS.", "在 Cloud SaaS 中按流程学习方法推荐、工作台与 AI Research 轨道。")
add("tut.s1a", "절차 A · methodos", "Path A · methodos", "流程 A · methodos")
add("tut.s1ap", "방법 추천 → 프로세스 → 워크벤치 → 검토·검증", "Recommend → process → workbench → review/validate", "方法推荐 → 过程 → 工作台 → 审阅/验证")
add("tut.s1b", "절차 B · StudiumR", "Path B · StudiumR", "流程 B · StudiumR")
add("tut.s1bp", "대시보드 → 트랙 → 문헌·설계 → 작성 → 크리틱", "Dashboard → tracks → literature/design → writing → critique", "仪表盘 → 轨道 → 文献/设计 → 写作 → 批评")

# Products
add("prod.h1", "Methodos Lab 제품", "Methodos Lab products", "Methodos Lab 产品")
add("prod.lead", "Desktop 설치형 분석 프로그램 3종과 Cloud SaaS 2종으로 연구방법을 지원합니다.", "Three installable Desktop analysis apps and two Cloud SaaS products for research methods.", "以三款 Desktop 安装版分析程序与两款 Cloud SaaS 支持研究方法。")
add("basic.lead", "통계분석 프로그램 — 설치형·실행형 Desktop 애플리케이션입니다.", "Statistics analysis — installable and portable Desktop app.", "统计分析程序——安装版与便携版 Desktop 应用。")
add("basic.glance", "methodos-basic은 모든 학술분야에서 연구자가 자주 쓰는 통계 절차를 GUI로 수행하는 Desktop 통계분석 프로그램입니다. Methodos Lab의 Desktop 트랙 기본 통계분석 제품입니다.", "methodos-basic is a Desktop statistics app that runs common statistical procedures via GUI for researchers across all academic fields. It is Methodos Lab’s core Desktop statistics product.", "methodos-basic 是面向所有学术领域研究者的 Desktop 统计分析程序，以 GUI 完成常用统计流程，也是 Methodos Lab Desktop 线的基础统计分析产品。")
add("basic.featuresTitle", "주요 기능 (요약)", "Key features (summary)", "主要功能（摘要）")
add("basic.f1", "데이터 불러오기 · 변수 관리 · 기초통계", "Data import · variable management · descriptive stats", "数据导入 · 变量管理 · 基础统计")
add("basic.f2", "추론통계 · 회귀 · 분산분석 계열 워크플로", "Inferential stats · regression · ANOVA-family workflows", "推断统计 · 回归 · 方差分析类流程")
add("basic.f3", "결과 표·그래프 내보내기", "Export result tables and charts", "导出结果表与图表")
add("basic.f4", "설치형(Setup) 및 포터블(실행형) 배포", "Installer (Setup) and portable builds", "安装版（Setup）与便携版发布")
add("basic.deployTitle", "배포 형태", "Distribution", "发布形式")
add("basic.deployBody", "설치형 Setup.exe · 포터블 실행 파일 형태로 제공될 예정입니다. 로컬 개발 산출물: MethodosBasic-LT 계열.", "Will ship as Setup.exe installer and portable executables. Local build line: MethodosBasic-LT.", "将以 Setup.exe 安装包与便携可执行文件提供。本地构建线：MethodosBasic-LT。")
add("q.lead", "Q방법론 분석 프로그램 — 아키타입 단계·태스크 기반 Desktop 워크벤치입니다.", "Q methodology analysis — archetype stage/task Desktop workbench.", "Q方法分析程序——基于原型阶段与任务的 Desktop 工作台。")
add("q.glance", "methodosQ는 Q방법론(Q Methodology)의 표준 절차를 단계·태스크로 구조화한 분석 프로그램입니다.", "methodosQ structures standard Q Methodology into stages and tasks as an analysis program.", "methodosQ 将 Q 方法标准流程结构化为阶段与任务的分析程序。")
add("q.wfTitle", "워크플로 하이라이트", "Workflow highlights", "流程亮点")
add("q.wf1", "아키타입 기반 다단계·다태스크 진행", "Archetype-based multi-stage, multi-task progress", "基于原型的多阶段、多任务推进")
add("q.wf2", "분석 단계별 산출물·QC 체크", "Per-stage outputs and QC checks", "各分析阶段产出与质控检查")
add("q.wf3", "Q표집·요인 관련 작업 흐름 지원", "Support for Q sampling and factor workflows", "支持 Q 抽样与因子相关流程")
add("q.wf4", "Electron 기반 Desktop 실행", "Electron-based Desktop runtime", "基于 Electron 的 Desktop 运行")
add("g.lead", "근거이론(Grounded Theory) 분석 프로그램 — 설치형·실행형 Desktop 도구입니다.", "Grounded Theory analysis — installable and portable Desktop tool.", "扎根理论分析程序——安装版与便携版 Desktop 工具。")
add("g.glance", "methodosG는 근거이론 코딩·범주화·이론화 절차를 지원하는 분석 프로그램입니다.", "methodosG is an analysis program that supports grounded-theory coding, categorizing, and theorizing.", "methodosG 是支持扎根理论编码、范畴化与理论化的分析程序。")
add("g.supportTitle", "지원 방향", "What it supports", "支持方向")
add("g.s1", "질적 자료 코딩 워크벤치", "Qualitative coding workbench", "质性资料编码工作台")
add("g.s2", "개방·축·선택 코딩 흐름 안내", "Open, axial, and selective coding guidance", "开放·主轴·选择编码流程引导")
add("g.s3", "메모·범주·이론 메모 관리", "Memo, category, and theory-memo management", "备忘·范畴·理论备忘管理")
add("g.s4", "로컬 프로젝트 저장", "Local project storage", "本地项目保存")
add("methodos.lead", "절차적 단계 AI 연구분석방법 프로그램 — Cloud SaaS입니다.", "Procedural AI research-methods program — Cloud SaaS.", "程序性 AI 研究分析方法程序——Cloud SaaS。")
add("methodos.body", "methodos는 연구방법 추천·프로세스·카탈로그·11단계 워크벤치·시각화까지 한 흐름으로 지원하는 Research Methods OS입니다.", "methodos is a Research Methods OS covering method recommendation, process, catalog, an 11-stage workbench, and visualization in one flow.", "methodos 是贯通方法推荐、流程、目录、11 阶段工作台与可视化的 Research Methods OS。")
add("methodos.runTitle", "바로 실행", "Run now", "立即运行")
add("methodos.runBody", "실시간서비스를 지원합니다.", "Realtime service is supported.", "支持实时服务。")
add("thumb.tagline", "절차로 익히는 연구 통계", "Research statistics learned by procedure", "通过流程掌握研究统计")
add("thumb.s1", "데이터 수집", "Data collection", "数据收集")
add("thumb.s2", "자료 구조화", "Structure data", "资料结构化")
add("thumb.s3", "변수 설정", "Set variables", "变量设置")
add("thumb.s4", "분석 수행", "Run analysis", "执行分析")
add("thumb.s5", "결과 해석", "Interpret results", "结果解释")
add("methodos.modulesTitle", "핵심 모듈", "Core modules", "核心模块")
add("methodos.m1", "연구방법 추천", "Method recommendation", "研究方法推荐")
add("methodos.m1p", "질문·자료 유형 기반 AI·규칙 추천", "AI and rule-based recommendations from question and data type", "基于问题与资料类型的 AI / 规则推荐")
add("methodos.m2p", "표준 방법 단계와 아키타입 공통절차", "Standard method stages and shared archetype procedures", "标准方法阶段与原型共用程序")
add("methodos.m3", "11단계 워크벤치", "11-stage workbench", "11 阶段工作台")
add("methodos.m3p", "단계·태스크 실행, 설문·통계·코딩", "Run stages/tasks; surveys, stats, coding", "执行阶段/任务，问卷·统计·编码")
add("methodos.m4", "검토·검증", "Review & validation", "审阅与验证")
add("methodos.m4p", "산출물 입력·검증·재현 기록", "Output intake, validation, reproducibility log", "产出录入、验证与可复现记录")
add("studiumr.lead", "End-to-End AI Research 프로그램 — 연구준비자(RDOS)와 연구자(AI-Research-OS) 트랙을 제공합니다.", "End-to-end AI Research — prep (RDOS) and researcher (AI-Research-OS) tracks.", "端到端 AI Research——提供研究准备者（RDOS）与研究者（AI-Research-OS）轨道。")
add("studiumr.body", "StudiumR은 문헌 연구부터 논문 구조·크리틱·참고문헌까지 이어 주는 AI Research Operating System입니다. Methodos Lab 홈페이지의 시각·섹션 포맷 레퍼런스이기도 합니다.", "StudiumR is an AI Research OS from literature through paper structure, critique, and references. It also informs Methodos Lab’s visual and section format.", "StudiumR 是贯通文献到论文结构、批评与参考文献的 AI Research OS，也是 Methodos Lab 官网视觉与版式参考。")
add("studiumr.tracksTitle", "두 트랙", "Two tracks", "两条轨道")
add("studiumr.prep", "연구준비자", "Research prep", "研究准备者")
add("studiumr.prepP", "대학원 진학 예정자·석사과정·연구 입문자 — 논문·연구 역량 개발.", "Prospective grads, master’s students, beginners — build paper and research skills.", "拟读研者、硕士生、研究入门者——培养论文与研究能力。")
add("studiumr.researcher", "연구자", "Researcher", "研究者")
add("studiumr.researcherP", "석사 이상·논문 저자·교수·연구원 — 실제 연구 수행·논문 생산.", "Master’s+ authors, faculty, researchers — run studies and produce papers.", "硕士以上作者、教授、研究员——开展研究并产出论文。")
add("compare.lead", "Desktop과 SaaS 제품의 역할 차이를 한눈에 봅니다.", "See Desktop vs SaaS roles at a glance.", "一览 Desktop 与 SaaS 产品角色差异。")
add("compare.th.type", "유형", "Type", "类型")
add("compare.th.focus", "초점", "Focus", "焦点")
add("compare.th.access", "접속", "Access", "访问")

# Download / learn / community / about
add("dl.h1", "다운로드 · 시작하기", "Download · Get started", "下载 · 开始")
add("dl.lead", "Desktop은 설치 파일을, SaaS는 브라우저 접속으로 시작합니다. (jamovi·JASP·Orange의 Download 메뉴 패턴)", "Desktop starts from installers; SaaS starts in the browser. (Download-menu pattern like jamovi, JASP, Orange)", "Desktop 用安装包开始，SaaS 在浏览器中开始。（参考 jamovi、JASP、Orange 的 Download 菜单）")
add("dl.reqCard", "권장 사양 안내", "Recommended specs", "推荐配置说明")
add("dlDesktop.h1", "Desktop 설치 프로그램", "Desktop installers", "Desktop 安装程序")
add("dlDesktop.basicFiles", "MethodosBasic-LT-Setup.exe (설치형) · MethodosBasic-LT.exe (포터블)", "MethodosBasic-LT-Setup.exe (installer) · MethodosBasic-LT.exe (portable)", "MethodosBasic-LT-Setup.exe（安装版）· MethodosBasic-LT.exe（便携版）")
add("dlSaas.h1", "Cloud · SaaS 시작하기", "Start Cloud · SaaS", "开始 Cloud · SaaS")
add("dlSaas.lead", "설치 없이 브라우저에서 바로 실행합니다.", "Run in the browser with no install.", "无需安装，在浏览器中直接运行。")
add("label.methodsOsShort", "방법 추천 · 프로세스 · 워크벤치", "Method recommend · process · workbench", "方法推荐 · 流程 · 工作台")
add("label.tracksPrepResearcher", "연구준비자 · 연구자 트랙", "Prep & researcher tracks", "研究准备者 · 研究者轨道")
add("req.ram", "RAM: 8GB 이상 권장", "RAM: 8GB+ recommended", "内存：建议 8GB 及以上")
add("req.disk", "Disk: 500MB~2GB 여유 공간 (제품별 상이)", "Disk: 500MB–2GB free (varies by product)", "磁盘：约 500MB–2GB 可用空间（因产品而异）")
add("req.saas", "SaaS: 최신 Chrome / Edge / Safari", "SaaS: latest Chrome / Edge / Safari", "SaaS：最新 Chrome / Edge / Safari")
add("gs.s1", "제품 고르기", "Pick a product", "选择产品")
add("gs.s1p", "통계·Q·근거이론 Desktop 또는 methodos·StudiumR SaaS", "Stats / Q / GT Desktop, or methodos / StudiumR SaaS", "统计·Q·扎根理论 Desktop，或 methodos·StudiumR SaaS")
add("gs.s2", "설치 / 가입", "Install / sign up", "安装 / 注册")
add("gs.s2p", "Desktop 설치 또는 Cloud 회원가입", "Install Desktop or create a Cloud account", "安装 Desktop 或注册 Cloud")
add("gs.s3", "샘플로 연습", "Practice with samples", "用示例练习")
add("gs.s3p", "예시 데이터·튜토리얼로 첫 분석", "First analysis with sample data and tutorials", "用示例数据与教程完成首次分析")
add("gs.s4", "가이드 심화", "Go deeper with guides", "深入指南")
add("gs.s4p", "사용자 가이드·튜토리얼로 확장", "Expand with user guides and tutorials", "通过用户指南与教程扩展")
add("guides.basicTitle", "methodos-basic 가이드", "methodos-basic guide", "methodos-basic 指南")
add("guides.basicP", "절차로 익히는 연구용 통계 · 소개 & 절차 가이드", "Learn research stats by procedure · intro & procedure guide", "按流程学习研究统计 · 介绍与流程指南")
add("guides.qTitle", "methodosQ 가이드", "methodosQ guide", "methodosQ 指南")
add("guides.qP", "Q방법론 학습형 워크벤치 · 소개 & 메뉴 가이드", "Q methodology learning workbench · intro & menu guide", "Q方法学习型工作台 · 介绍与菜单指南")
add("guides.gTitle", "methodosG 가이드", "methodosG guide", "methodosG 指南")
add("guides.gP", "근거이론 코딩·이론화 · 소개 & 절차 가이드", "Grounded-theory coding & theorizing · intro & procedure guide", "扎根理论编码与理论化 · 介绍与流程指南")
add("guides.saasTitle", "methodos / StudiumR 가이드", "methodos / StudiumR guide", "methodos / StudiumR 指南")
add("guides.saasP", "연구방법 OS · End-to-End AI Research", "Research methods OS · End-to-end AI Research", "研究方法 OS · 端到端 AI Research")
add("comm.lead", "jamovi Community · JASP Community 메뉴를 Lab에 맞게 구성했습니다.", "Community menu patterned after jamovi and JASP, adapted for the Lab.", "参照 jamovi / JASP Community 菜单，按 Lab 需求组织。")
add("comm.blogP", "Lab 소식", "Lab news", "实验室动态")
add("blog.p1", "Methodos Lab 홈페이지 오픈", "Methodos Lab homepage launch", "Methodos Lab 官网上线")
add("blog.p1m", "2026-09-22 · Lab 소개", "2026-09-22 · About the Lab", "2026-09-22 · 实验室介绍")
add("blog.p2", "Desktop vs SaaS, 언제 무엇을?", "Desktop vs SaaS — when to use which?", "Desktop vs SaaS，何时用哪个？")
add("blog.p2m", "제품 선택 가이드", "Product selection guide", "产品选择指南")
add("blog.p3", "StudiumR 업데이트 노트", "StudiumR release notes", "StudiumR 更新说明")
add("blog.p3m", "릴리즈 하이라이트", "Release highlights", "发布亮点")
add("lab.lead", "연구방법 Desktop 도구와 AI Research SaaS를 설계·배포하는 연구소입니다.", "A lab that designs and ships research-methods Desktop tools and AI Research SaaS.", "设计并发布研究方法 Desktop 工具与 AI Research SaaS 的实验室。")
add("lab.body", "Methodos Lab은 통계분석(methodos-basic), Q방법론(methodosQ), 근거이론(methodosG) 설치형 프로그램과, 절차적 연구방법(methodos), End-to-End AI Research(StudiumR) SaaS를 하나의 브랜드 아래에서 제공합니다.", "Under one brand, Methodos Lab offers installable stats (methodos-basic), Q (methodosQ), and grounded theory (methodosG), plus procedural methods (methodos) and end-to-end AI Research (StudiumR) SaaS.", "Methodos Lab 在同一品牌下提供统计分析（methodos-basic）、Q方法（methodosQ）、扎根理论（methodosG）安装版，以及程序性研究（methodos）与端到端 AI Research（StudiumR）SaaS。")
add("lab.productsTitle", "제품 구성", "Product lineup", "产品构成")
add("mission.h1", "미션", "Mission", "使命")
add(
    "mission.p",
    "Methodos Lab의 목표는 연구자가 방법 선택에서 분석과 논문 작성에 이르기까지 연구 과정 전반을 끊김 없이 이어갈 수 있도록 지원하는 것입니다.",
    "Methodos Lab’s goal is to help researchers move seamlessly from method selection through analysis and paper writing across the full research process.",
    "Methodos Lab 的目标是帮助研究者从方法选择到分析与论文写作，连贯推进研究全过程。",
)
add("mission.li0", "연구방법의 절차를 소프트웨어로 표준화한다", "Standardize research-method procedures in software", "把研究方法程序软件化、标准化")
add("mission.li1", "연구 데이터 활용의 자율성을 사용자에게 보장합니다", "We ensure users retain autonomy in how research data is used.", "保障用户对研究数据使用的自主权。")
add("mission.li2", "전문 분석(Desktop)과 AI Research(SaaS)를 연결한다", "Connect specialized Desktop analysis with AI Research SaaS", "连接专业分析（Desktop）与 AI Research（SaaS）")
add("mission.li3", "교육·워크숍으로 연구 역량 확산을 돕는다", "Spread research capability through education and workshops", "通过教育与工作坊帮助扩散研究能力")
add("contact.lead", "협업·교육·라이선스 문의는 아래 이메일로 연락해 주세요.", "For collaboration, education, or licensing, email us below.", "合作、教育或许可相关咨询请发邮件至下方地址。")
add("contact.general", "일반 문의", "General inquiries", "一般咨询")
add("contact.edu", "교육 · 워크숍", "Education · workshops", "教育 · 工作坊")

# Guide detail pages — key phrases
add("gBasic.eyebrow", "Desktop · 통계분석", "Desktop · Statistics", "Desktop · 统计分析")
add("gBasic.lead", "절차로 익히는 연구용 통계 — 소개와 절차 가이드입니다.", "Learn research statistics by procedure — intro and procedure guide.", "按流程学习研究统计——介绍与流程指南。")
add("gBasic.interactive", "인터랙티브 절차 가이드", "Interactive procedure guide", "交互式流程指南")
add("gQ.eyebrow", "Desktop · Q방법론", "Desktop · Q methodology", "Desktop · Q方法")
add("gQ.lead", "개념과 의미를 절차로 익히게 돕는 Q방법론 학습형 워크벤치입니다.", "A Q methodology learning workbench that teaches concepts through procedure.", "通过流程帮助掌握概念与含义的 Q 方法学习型工作台。")
add("gG.eyebrow", "Desktop · 근거이론", "Desktop · Grounded theory", "Desktop · 扎根理论")
add("gG.lead", "코딩에서 이론화까지 근거이론 절차를 Desktop 워크벤치로 표준화합니다.", "Standardizes grounded-theory procedure from coding to theorizing on a Desktop workbench.", "在 Desktop 工作台上标准化从编码到理论化的扎根理论流程。")
add("gS.lead", "연구방법 OS와 End-to-End AI Research 플랫폼을 브라우저에서 바로 시작합니다.", "Start the research-methods OS and end-to-end AI Research platform in the browser.", "在浏览器中直接启动研究方法 OS 与端到端 AI Research 平台。")

# --- Guide detail bodies (previously unwired) ---
add(
    "gBasic.body",
    "Methodos Basic은 분석을 도와주는 자동화 프로그램입니다. 결과만 넘기지 않고, 절차적 단계와 통계 이해를 함께 높이도록 만들었습니다. 예제·학습으로 개념을 익힌 뒤, 자료를 보고 변수를 배정하며 분석·그래프·결과까지 같은 흐름으로 진행합니다. 쉬운 주석 · 한·영·중 전환으로 해외 유학생도 함께 씁니다.",
    "Methodos Basic is an automation program that assists analysis. It does not just hand over results—it raises procedural steps and statistical understanding together. Learn concepts with examples and study, then inspect data, assign variables, and move through analysis, graphs, and results in one flow. Plain-language notes and KO/EN/ZH switching support international students.",
    "Methodos Basic 是协助分析的自动化程序。它不只交付结果，还同步提升流程步骤与统计理解。通过示例与学习掌握概念后，查看资料、分配变量，并在同一流程中完成分析、图表与结果。简明注释与韩/英/中切换也方便留学生使用。",
)
add("gBasic.note", "번호 + 메뉴 자막이 단계별로 이어지는 Framer Motion 절차입니다. 절차 A·B는 같은 앱 안에 있습니다.", "A Framer Motion procedure with numbered steps and menu captions. Procedures A and B live in the same app.", "带编号与菜单字幕的 Framer Motion 流程。流程 A·B 位于同一应用中。")
add("gBasic.stepsA", "01 자료 보기 → 02 포맷 받기 → 03 내 형식 변환 → 04 변수 칸 → 05 변수 선택 → 06 분석 → 07 그래프 → 08 결과", "01 View data → 02 Get format → 03 Convert to your form → 04 Variable slots → 05 Select variables → 06 Analyze → 07 Graphs → 08 Results", "01 查看资料 → 02 获取格式 → 03 转为自有格式 → 04 变量栏 → 05 选择变量 → 06 分析 → 07 图表 → 08 结果")
add("gBasic.procB", "절차 B · 학습으로 쌓기", "Procedure B · Build through learning", "流程 B · 通过学习积累")
add("gBasic.stepsB", "01 명칭 → 02 초급 → 03 중급 → 04 고급 → 05 예제 확인 → 06 작업대 적용", "01 Terms → 02 Beginner → 03 Intermediate → 04 Advanced → 05 Check examples → 06 Apply on workbench", "01 名称 → 02 初级 → 03 中级 → 04 高级 → 05 确认示例 → 06 应用到工作台")
add("gBasic.menuTitle", "왼쪽 메뉴 · 요약 절차", "Left menu · Procedure summary", "左侧菜单 · 流程摘要")
add("gBasic.homeP", "단계 카드 확인 후 방법 정하기 / 통계 계산", "Review step cards, then choose methods / run stats", "查看步骤卡片后选定方法 / 统计计算")
add("gBasic.statsH", "통계방법 정하기·찾기·라이브러리", "Choose · find · library of statistical methods", "确定·查找·统计方法库")
add("gBasic.statsP", "목적→기법 연결, 예제 실행", "Link purpose to technique; run examples", "目的→方法连接，运行示例")
add("gBasic.exH", "예제 자료", "Example data", "示例资料")
add("gBasic.exP", "분류·설명 후 작업대에 올리기", "Classify, explain, then load onto the workbench", "分类说明后放到工作台")
add("gBasic.wbH", "작업대·통계 계산", "Workbench · statistical calculation", "工作台·统计计算")
add("gBasic.wbP", "자료→변수 배정→실행", "Data → assign variables → run", "资料→分配变量→运行")
add("gBasic.graphH", "그래프·결과", "Graphs · results", "图表·结果")
add("gBasic.graphP", "패턴과 해석 문장 대조", "Compare patterns with interpretation sentences", "对照模式与解释句子")
add("gBasic.learnH", "학습·설정", "Learning · settings", "学习·设置")
add("gBasic.learnP", "명칭/초·중·고급, 언어(한·영·중)", "Terms / beginner–advanced; language (KO/EN/ZH)", "名称/初·中·高级，语言（韩/英/中）")
add("gBasic.oneLiner", "핵심 한 줄: 예제 포맷을 받아 내 자료로 바꾼 뒤, 같은 메뉴 절차로 분석·그래프·결과를 읽습니다.", "One line: take the example format, adapt your data, then read analysis, graphs, and results with the same menu procedure.", "一句话：获取示例格式并换成自己的资料后，用同一菜单流程阅读分析、图表与结果。")

add("gQ.introH", "한 줄 소개", "One-line intro", "一句话介绍")
add(
    "gQ.body",
    "methodosQ는 연구 초점부터 해석·보고까지 Q방법론 8단계를 화면에서 따라가며 배우는 데스크톱 프로그램입니다. 자동 결과가 아니라 왜 이 단계가 필요한지를 쉬운 설명과 주석으로 보여 주고, 한국어·영어 UI 전환으로 해외 유학생도 함께 학습할 수 있습니다.",
    "methodosQ is a desktop program that teaches Q methodology’s 8 stages on screen—from research focus through interpretation and reporting. It explains why each step matters with plain notes, not just automated results, and KO/EN UI switching supports international students.",
    "methodosQ 是一款桌面程序，在屏幕上跟随学习从研究焦点到解释与报告的 Q 方法 8 个阶段。它用简明说明与注释展示每一步为何必要，而非只给自动结果，并通过韩/英 UI 切换支持留学生一起学习。",
)
add("gQ.p1h", "01 · 절차 학습", "01 · Learn by procedure", "01 · 流程学习")
add("gQ.p1p", "8단계·37세부 절차로 개념을 순서대로 체득", "Master concepts in order across 8 stages and 37 sub-steps", "通过 8 阶段·37 细分流程按序掌握概念")
add("gQ.p2h", "02 · 쉬운 주석", "02 · Plain-language notes", "02 · 简明注释")
add("gQ.p2p", "학술 용어 아래 쉬운 말·예시·개념사전 연결", "Plain wording, examples, and glossary links under academic terms", "学术术语下连接易懂说法、示例与概念词典")
add("gQ.p3h", "03 · 다국어", "03 · Multilingual", "03 · 多语言")
add("gQ.p3p", "한국어·English UI · 중문 가이드로 해외 유학생 지원", "Korean · English UI · Chinese guides for international students", "韩语·English UI · 中文指南支持留学生")
add("gQ.flowH", "핵심 흐름", "Core flow", "核心流程")
add(
    "gQ.flowP",
    "학습 → 예제 분석 → 포맷 변환 → 재분석. 예제 열기 → 포맷(CSV/Excel) 받기 → 내 자료로 바꿔 넣기 → 분석 다시 돌리기. 학습 트랙(입문·연구·논문·개념사전)을 번호 절차로 따라갑니다.",
    "Learn → example analysis → format convert → re-analyze. Open an example → get CSV/Excel format → swap in your data → run again. Follow numbered learning tracks (intro · research · paper · glossary).",
    "学习 → 示例分析 → 格式转换 → 再分析。打开示例 → 获取 CSV/Excel 格式 → 换成自己的资料 → 再跑分析。按编号学习轨道（入门·研究·论文·概念词典）跟进。",
)
add("gQ.menuH", "앱 상단 메뉴", "App top menu", "应用顶部菜单")
add("gQ.file", "파일", "File", "文件")
add("gQ.fileP", "새/열기/저장 · CSV·Q자료 입출력 · 리포트·백업 · 끝내기", "New/Open/Save · CSV·Q I/O · report·backup · Quit", "新建/打开/保存 · CSV·Q 资料出入 · 报告·备份 · 退出")
add("gQ.edit", "편집", "Edit", "编辑")
add("gQ.editP", "실행취소 · 다시실행 · 잘라내기/복사/붙여넣기", "Undo · Redo · Cut/Copy/Paste", "撤销 · 重做 · 剪切/复制/粘贴")
add("gQ.view", "보기", "View", "查看")
add("gQ.viewP", "테마 · 언어(한국어/English) · 단축키 · 확대/축소", "Theme · language (Korean/English) · shortcuts · zoom", "主题 · 语言（韩语/English） · 快捷键 · 缩放")
add("gQ.proc", "절차", "Procedure", "流程")
add("gQ.procP", "4단계 Gate · 연구 8단계(Ctrl+1~8)와 세부 절차", "4-step Gate · research 8 stages (Ctrl+1–8) and sub-steps", "4 步 Gate · 研究 8 阶段（Ctrl+1~8）与细分流程")
add("gQ.learnP", "처음/연구중/논문대비 · 개념사전 · 예제 자료", "Intro / in-progress / paper-ready · glossary · example data", "入门/研究中/论文准备 · 概念词典 · 示例资料")
add("gQ.help", "도움말", "Help", "帮助")
add("gQ.helpP", "정보 · 계산 근거 고지 · 설정", "About · computation basis notice · settings", "信息 · 计算依据说明 · 设置")
add("gQ.stepsH", "Q 연구 절차 · 단계", "Q research procedure · stages", "Q 研究流程 · 阶段")
add("gQ.s1h", "1 · 연구 초점", "1 · Research focus", "1 · 研究焦点")
add("gQ.s1p", "주제 확정 → 연구질문 → 방법 적합성 → 포함/제외 → 초점 요약", "Confirm topic → research question → method fit → include/exclude → focus summary", "确定主题 → 研究问题 → 方法适配 → 纳入/排除 → 焦点摘要")
add("gQ.s2h", "2 · 의견장 (Concourse)", "2 · Concourse", "2 · 意见场 (Concourse)")
add("gQ.s2p", "수집 → 기록 → 정리 → 찬/반 균형 → 포화 → Q표본 후보", "Collect → record → organize → pro/con balance → saturation → Q-sample candidates", "收集 → 记录 → 整理 → 正反平衡 → 饱和 → Q 样本候选")
add("gQ.s3h", "3 · Q표본 구성", "3 · Build Q-sample", "3 · 构成 Q 样本")
add("gQ.s3p", "축소 기준 → 목표 진술 수 → 구조화 → 정제 → 파일럿 → 최종 연결", "Reduction criteria → target statement count → structure → refine → pilot → final link", "缩减标准 → 目标陈述数 → 结构化 → 精炼 → 试测 → 最终连接")
add("gQ.s48h", "4–8 · 정렬·요인·해석", "4–8 · Sort · factors · interpretation", "4–8 · 排序·因子·解释")
add("gQ.s48p", "P표본·정렬 → 요인추출 → 해석 → 보고까지 단계 워크플로", "P-sample · sort → extract factors → interpret → report workflow", "P 样本·排序 → 因子提取 → 解释 → 报告的分步工作流")
add("gQ.oneLiner", "핵심 한 줄: 통계를 대신 눌러 주는 도구가 아니라, Q방법론을 절차로 익히게 돕는 학습형 워크벤치입니다.", "One line: not a tool that clicks stats for you—a learning workbench that teaches Q methodology by procedure.", "一句话：不是替你点统计的工具，而是通过流程帮助掌握 Q 方法的学习型工作台。")

add("gG.titleH", "methodosG · 근거이론 분석", "methodosG · Grounded-theory analysis", "methodosG · 扎根理论分析")
add(
    "gG.body",
    "methodosG는 근거이론의 코딩·범주화·이론화 절차를 Desktop에서 따라가며 수행하는 분석 프로그램입니다. Setup.exe와 Portable.exe로 설치·실행하며, 질적 자료의 개방·축·선택 코딩 흐름과 메모·범주 관리를 한 워크벤치에서 지원합니다.",
    "methodosG is a Desktop analysis program that walks grounded-theory coding, categorizing, and theorizing. Install or run via Setup.exe and Portable.exe; one workbench covers open/axial/selective coding plus memo and category management.",
    "methodosG 是在 Desktop 上跟随执行扎根理论编码、范畴化与理论化流程的分析程序。通过 Setup.exe 与 Portable.exe 安装/运行，在同一工作台支持开放/轴心/选择编码以及备忘与范畴管理。",
)
add("gG.procA", "절차 A · 자료 → 코딩", "Procedure A · Data → coding", "流程 A · 资料 → 编码")
add("gG.stepsA", "01 자료 불러오기 → 02 개방 코딩 → 03 축 코딩 → 04 선택 코딩", "01 Load data → 02 Open coding → 03 Axial coding → 04 Selective coding", "01 导入资料 → 02 开放编码 → 03 轴心编码 → 04 选择编码")
add("gG.procB", "절차 B · 이론화 → 보고", "Procedure B · Theorize → report", "流程 B · 理论化 → 报告")
add("gG.stepsB", "01 메모 → 02 범주 정리 → 03 이론 스케치 → 04 보고서 내보내기", "01 Memos → 02 Organize categories → 03 Sketch theory → 04 Export report", "01 备忘 → 02 整理范畴 → 03 理论草图 → 04 导出报告")
add("gG.deploy", "배포물", "Downloads", "发布包")
add("gG.setup", "설치형", "Installer", "安装版")
add("gG.portable", "실행형", "Portable", "便携版")
add("gG.localH", "로컬 저장", "Local storage", "本地存储")
add("gG.localP", "프로젝트·코딩 산출물을 PC에 보관", "Keep projects and coding outputs on your PC", "将项目与编码产出保存在本机")
add("gG.oneLiner", "핵심 한 줄: 코딩에서 이론화까지 근거이론 절차를 Desktop 워크벤치로 표준화합니다.", "One line: standardize grounded-theory procedure from coding to theorizing on a Desktop workbench.", "一句话：在 Desktop 工作台上标准化从编码到理论化的扎根理论流程。")
add("common.downloadGuide", "다운로드 안내", "Download guide", "下载说明")

add("gS.saasH", "SaaS 제품군", "SaaS product family", "SaaS 产品族")
add(
    "gS.body",
    "methodos는 절차적 단계 AI 연구방법 OS이고, StudiumR은 End-to-End AI Research 플랫폼입니다. 브라우저에서 바로 시작해 연구방법 선택부터 논문 생산까지 이어 줍니다.",
    "methodos is a procedural AI research-methods OS; StudiumR is an end-to-end AI Research platform. Start in the browser and go from method selection through paper production.",
    "methodos 是程序性 AI 研究方法 OS，StudiumR 是端到端 AI Research 平台。在浏览器中直接开始，从方法选择贯通到论文产出。",
)
add("gS.methodosH", "methodos · 연구방법 OS", "methodos · Research-methods OS", "methodos · 研究方法 OS")
add("gS.methodosP", "01 방법 추천 → 02 프로세스 → 03 워크벤치 → 04 검토·검증", "01 Recommend method → 02 Process → 03 Workbench → 04 Review · verify", "01 方法推荐 → 02 流程 → 03 工作台 → 04 审阅·验证")
add("gS.studiumP", "01 트랙 선택 → 02 문헌·설계 → 03 작성 → 04 크리틱", "01 Pick track → 02 Literature · design → 03 Writing → 04 Critique", "01 选择轨道 → 02 文献·设计 → 03 写作 → 04 批评")
add("gS.startH", "시작 요약", "Getting started summary", "开始摘要")
add("gS.signup", "회원가입", "Sign up", "注册")
add("gS.signupP", "Google · GitHub · 이메일", "Google · GitHub · email", "Google · GitHub · 邮箱")
add("gS.trackH", "StudiumR 트랙", "StudiumR tracks", "StudiumR 轨道")
add("gS.trackP", "연구준비자(RDOS) / 연구자(AI-Research-OS)", "Research preparer (RDOS) / Researcher (AI-Research-OS)", "研究准备者 (RDOS) / 研究者 (AI-Research-OS)")
add("gS.secH", "보안", "Security", "安全")
add("gS.secP", "연구 산출물 로컬 우선 · 메타데이터만 클라우드", "Research outputs local-first · metadata only in the cloud", "研究产出本地优先 · 仅元数据上云")
add("gS.oneLiner", "핵심 한 줄: methodos로 방법을 절차화하고, StudiumR로 문헌·작성·검증까지 End-to-End로 이어 갑니다.", "One line: proceduralize methods with methodos, then continue end-to-end through literature, writing, and verification with StudiumR.", "一句话：用 methodos 将方法流程化，再用 StudiumR 贯通文献、写作与验证。")
add("gS.methodosProduct", "methodos 제품", "methodos product", "methodos 产品")
add("gS.studiumProduct", "StudiumR 제품", "StudiumR product", "StudiumR 产品")
add("guide.aria", "가이드 전환", "Guide switcher", "指南切换")


def write_dict_js() -> None:
    packs = {"ko": {}, "en": {}, "zh": {}}
    for key, tri in T.items():
        for lang in packs:
            packs[lang][key] = tri[lang]
    # emit JS
    lines = ["/** Auto-generated full site i18n dictionary */", "window.METHODOS_I18N = {"]
    for lang in ("ko", "en", "zh"):
        lines.append(f"  {lang}: {{")
        for k, v in packs[lang].items():
            lines.append(f"    {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)},")
        lines.append("  },")
    lines.append("};")
    lines.append("")
    (ROOT / "js" / "i18n-dict.js").write_text("\n".join(lines), encoding="utf-8")
    print("wrote i18n-dict.js keys=", len(T))


def wire_html(path: Path) -> int:
    """Add data-i18n to tags whose exact text matches a ko string."""
    html = path.read_text(encoding="utf-8")
    # skip procedure SPA shells
    if "procedure" in path.as_posix() and path.name == "index.html" and "methodos" in path.as_posix():
        if "i18n-dict" not in html and "<div id=\"root\">" in html or 'id="root"' in html:
            return 0

    # build ko -> key (longest first); compare after HTML-entity unescape
    pairs = sorted(((tri["ko"], key) for key, tri in T.items()), key=lambda x: -len(x[0]))
    count = 0
    tags = "h1|h2|h3|h4|p|li|a|span|small|strong|th|td|button|label|div"

    def repl(m: re.Match) -> str:
        nonlocal count
        open_tag, text, close = m.group(1), m.group(2), m.group(3)
        raw = html_lib.unescape(text).strip()
        # already has data-i18n
        if "data-i18n=" in open_tag:
            return m.group(0)
        # skip pure brand / empty
        if not raw or raw in {"Products", "Resources", "Lab", "Desktop", "SaaS", "Local Storage", "Cloud Metadata"}:
            return m.group(0)
        for ko, key in pairs:
            if raw == ko:
                # inject attribute before >
                new_open = open_tag[:-1] + f' data-i18n="{key}">'
                count += 1
                return f"{new_open}{text}{close}"
        return m.group(0)

    # Only match leaf-ish tags without nested tags in text
    pattern = re.compile(rf"(<(?:{tags})(?:\s[^>]*)?>)([^<]+)(</(?:{tags})>)", re.I)
    html2 = pattern.sub(repl, html)
    if html2 != html:
        path.write_text(html2, encoding="utf-8")
    return count


def ensure_scripts(path: Path) -> None:
    html = path.read_text(encoding="utf-8")
    if "i18n-dict.js" in html:
        return
    # depth
    rel = path.relative_to(ROOT).as_posix()
    depth = "../" * (rel.count("/"))
    if path.name == "index.html" and path.parent == ROOT:
        depth = ""
    inject = (
        f'<script src="{depth}js/i18n-dict.js"></script>\n'
        f'<script src="{depth}js/i18n.js"></script>\n'
    )
    if "</body>" in html:
        html = html.replace("</body>", inject + "</body>")
        path.write_text(html, encoding="utf-8")


def write_i18n_js() -> None:
    (ROOT / "js" / "i18n.js").write_text(
        r"""(() => {
  const KEY = "methodos-lab-locale";
  const dict = window.METHODOS_I18N || {};

  function readLocale() {
    try {
      const saved = localStorage.getItem(KEY);
      if (saved && dict[saved]) return saved;
    } catch (_) {}
    return "ko";
  }

  function writeLocale(locale) {
    try {
      localStorage.setItem(KEY, locale);
      // Keep Framer procedure guides in sync with site chrome locale
      localStorage.setItem("methodos-guide-locale", locale);
    } catch (_) {}
  }

  function t(locale, key) {
    const pack = dict[locale] || dict.ko || {};
    if (pack[key] != null) return pack[key];
    if (dict.ko && dict.ko[key] != null) return dict.ko[key];
    return null;
  }

  function setText(el, val) {
    if (el.childElementCount && el.querySelector("img, svg")) {
      const labeled = el.querySelector("[data-i18n-text]");
      if (labeled) { labeled.textContent = val; return; }
      for (const node of el.childNodes) {
        if (node.nodeType === Node.TEXT_NODE && node.textContent.trim()) {
          const lead = /^\s*/.exec(node.textContent)[0];
          const trail = /\s*$/.exec(node.textContent)[0];
          node.textContent = lead + val + trail;
          return;
        }
      }
      return;
    }
    el.textContent = val;
  }

  function apply(locale) {
    if (!dict[locale]) locale = "ko";
    document.documentElement.lang = locale === "zh" ? "zh-CN" : locale;
    document.documentElement.dataset.locale = locale;

    document.querySelectorAll("[data-i18n]").forEach((el) => {
      const key = el.getAttribute("data-i18n");
      const val = t(locale, key);
      if (val != null) setText(el, val);
    });

    document.querySelectorAll("[data-i18n-html]").forEach((el) => {
      const key = el.getAttribute("data-i18n-html");
      const val = t(locale, key);
      if (val != null) el.innerHTML = val;
    });

    document.querySelectorAll("[data-i18n-aria]").forEach((el) => {
      const key = el.getAttribute("data-i18n-aria");
      const val = t(locale, key);
      if (val != null) el.setAttribute("aria-label", val);
    });

    document.querySelectorAll("[data-i18n-alt]").forEach((el) => {
      const key = el.getAttribute("data-i18n-alt");
      const val = t(locale, key);
      if (val != null) el.setAttribute("alt", val);
    });

    document.querySelectorAll("[data-i18n-title]").forEach((el) => {
      const key = el.getAttribute("data-i18n-title");
      const val = t(locale, key);
      if (val != null) document.title = `${val} · Methodos Lab`;
    });

    // Exact-text fallback: translate any remaining Korean leaves / icon-adjacent text
    if (locale !== "ko") {
      const rev = {};
      Object.keys(dict.ko || {}).forEach((k) => {
        const src = dict.ko[k];
        const dst = (dict[locale] || {})[k];
        if (src && dst && src !== dst) rev[src] = dst;
      });
      const skip = new Set(["SCRIPT", "STYLE", "NOSCRIPT", "TEXTAREA", "CODE", "PRE"]);
      const walk = (node) => {
        if (!node) return;
        if (node.nodeType === Node.ELEMENT_NODE) {
          if (skip.has(node.tagName)) return;
          if (node.hasAttribute("data-i18n") || node.hasAttribute("data-i18n-html")) return;
          // still walk children — data-i18n on parent would have returned; children may need text-node fix beside icons
          for (const child of Array.from(node.childNodes)) walk(child);
          return;
        }
        if (node.nodeType === Node.TEXT_NODE) {
          const raw = node.textContent || "";
          const trimmed = raw.trim();
          if (!trimmed || !rev[trimmed]) return;
          // Do not rewrite if parent already has data-i18n (handled above) or is an option/input
          const parent = node.parentElement;
          if (!parent || skip.has(parent.tagName)) return;
          if (parent.hasAttribute("data-i18n") || parent.hasAttribute("data-i18n-html")) return;
          const lead = /^\s*/.exec(raw)[0];
          const trail = /\s*$/.exec(raw)[0];
          node.textContent = lead + rev[trimmed] + trail;
        }
      };
      walk(document.body);
      document.querySelectorAll("img[alt]").forEach((img) => {
        const alt = (img.getAttribute("alt") || "").trim();
        if (rev[alt]) img.setAttribute("alt", rev[alt]);
      });
      document.querySelectorAll("[aria-label]").forEach((el) => {
        if (el.hasAttribute("data-i18n-aria")) return;
        const v = (el.getAttribute("aria-label") || "").trim();
        if (rev[v]) el.setAttribute("aria-label", rev[v]);
      });
    }

    document.querySelectorAll(".lang-switch__btn").forEach((btn) => {
      const on = btn.dataset.locale === locale;
      btn.classList.toggle("is-on", on);
      btn.setAttribute("aria-pressed", on ? "true" : "false");
    });

    writeLocale(locale);
    document.dispatchEvent(new CustomEvent("methodos:locale", { detail: { locale } }));
  }

  function bind() {
    document.querySelectorAll(".lang-switch__btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        const locale = btn.dataset.locale;
        if (!locale || !dict[locale]) return;
        apply(locale);
      });
    });
  }

  const boot = () => { bind(); apply(readLocale()); };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
  window.MethodosI18n = { apply, readLocale, t };
})();
""",
        encoding="utf-8",
    )
    print("wrote i18n.js")


def main() -> None:
    write_dict_js()
    write_i18n_js()
    html_files = []
    for p in ROOT.rglob("*.html"):
        s = p.as_posix()
        if any(x in s for x in ("/Q/", "/G/", "/basic/", "node_modules", "유튜브", "-procedure/")):
            continue
        html_files.append(p)

    total = 0
    for p in html_files:
        ensure_scripts(p)
        n = wire_html(p)
        total += n
        if n:
            print(f"  wired {n:3d}  {p.relative_to(ROOT)}")
    print("TOTAL wired attrs added this pass:", total)
    print("HTML files:", len(html_files))


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Generate Methodos Lab HTML prototype pages."""
from pathlib import Path

ROOT = Path(r"C:\Users\saran\OneDrive\Desktop\메스도스랩-홈페이지")


def asset(depth: str, path: str) -> str:
    return f"{depth}{path}"


def nav(depth: str) -> str:
    a = lambda p: asset(depth, p)
    return f"""
<header class="site-header">
  <div class="container nav-inner">
    <a class="brand" href="{a('index.html')}">
      <img src="{a('assets/logo/methodos-lab-logo.svg')}" alt="Methodos Lab 로고" />
      <span>Methodos <em>Lab</em></span>
    </a>
    <nav class="nav-desktop" aria-label="주 메뉴">
      <div class="nav-item">
        <a class="nav-link" href="{a('pages/products/index.html')}" aria-haspopup="true" aria-expanded="false">제품 <img class="chev" src="{a('assets/icons/chevron-down.svg')}" alt="" /></a>
        <div class="dropdown wide" role="menu">
          <div class="drop-label">Desktop · 설치형</div>
          <a class="drop-item" href="{a('pages/products/methodos-basic.html')}"><img src="{a('assets/icons/bar-chart-3.svg')}" alt="" /><span><strong>methodos-basic</strong><small>통계분석 프로그램</small></span></a>
          <a class="drop-item" href="{a('pages/products/methodosQ.html')}"><img src="{a('assets/icons/layers.svg')}" alt="" /><span><strong>methodosQ</strong><small>Q방법론 분석</small></span></a>
          <a class="drop-item" href="{a('pages/products/methodosG.html')}"><img src="{a('assets/icons/network.svg')}" alt="" /><span><strong>methodosG</strong><small>근거이론 분석</small></span></a>
          <div class="drop-label">Cloud · SaaS</div>
          <a class="drop-item" href="{a('pages/products/methodos.html')}"><img src="{a('assets/icons/workflow.svg')}" alt="" /><span><strong>methodos</strong><small>절차적 단계 AI 연구방법</small></span></a>
          <a class="drop-item" href="{a('pages/products/studiumr.html')}"><img src="{a('assets/icons/brain.svg')}" alt="" /><span><strong>StudiumR</strong><small>End-to-End AI Research OS</small></span></a>
          <a class="drop-item" href="{a('pages/products/compare.html')}"><img src="{a('assets/icons/layout-dashboard.svg')}" alt="" /><span><strong>제품 비교</strong><small>Desktop / SaaS 한눈에</small></span></a>
        </div>
      </div>
      <div class="nav-item">
        <a class="nav-link" href="{a('pages/download/index.html')}" aria-haspopup="true" aria-expanded="false">다운로드 <img class="chev" src="{a('assets/icons/chevron-down.svg')}" alt="" /></a>
        <div class="dropdown" role="menu">
          <a class="drop-item" href="{a('pages/download/desktop.html')}"><img src="{a('assets/icons/download.svg')}" alt="" /><span><strong>Desktop 설치</strong><small>basic · Q · G</small></span></a>
          <a class="drop-item" href="{a('pages/download/saas.html')}"><img src="{a('assets/icons/cloud.svg')}" alt="" /><span><strong>Cloud 시작</strong><small>methodos · StudiumR</small></span></a>
          <a class="drop-item" href="{a('pages/download/requirements.html')}"><img src="{a('assets/icons/monitor.svg')}" alt="" /><span><strong>시스템 요구사항</strong><small>권장 사양</small></span></a>
        </div>
      </div>
      <div class="nav-item">
        <a class="nav-link" href="{a('pages/learn/getting-started.html')}" aria-haspopup="true" aria-expanded="false">학습 <img class="chev" src="{a('assets/icons/chevron-down.svg')}" alt="" /></a>
        <div class="dropdown" role="menu">
          <a class="drop-item" href="{a('pages/learn/getting-started.html')}"><img src="{a('assets/icons/compass.svg')}" alt="" /><span><strong>시작하기</strong><small>첫 실행 가이드</small></span></a>
          <a class="drop-item" href="{a('pages/learn/guides.html')}"><img src="{a('assets/icons/book-open.svg')}" alt="" /><span><strong>사용자 가이드</strong><small>가이드</small></span></a>
          <a class="drop-item" href="{a('pages/learn/tutorials.html')}"><img src="{a('assets/icons/video.svg')}" alt="" /><span><strong>튜토리얼</strong><small>영상</small></span></a>
        </div>
      </div>
      <div class="nav-item">
        <a class="nav-link" href="{a('pages/community/index.html')}" aria-haspopup="true" aria-expanded="false">커뮤니티 <img class="chev" src="{a('assets/icons/chevron-down.svg')}" alt="" /></a>
        <div class="dropdown" role="menu">
          <a class="drop-item" href="{a('pages/community/blog.html')}"><img src="{a('assets/icons/file-text.svg')}" alt="" /><span><strong>블로그</strong><small>소식</small></span></a>
        </div>
      </div>
      <div class="nav-item">
        <a class="nav-link" href="{a('pages/about/lab.html')}" aria-haspopup="true" aria-expanded="false">소개 <img class="chev" src="{a('assets/icons/chevron-down.svg')}" alt="" /></a>
        <div class="dropdown" role="menu">
          <a class="drop-item" href="{a('pages/about/lab.html')}"><img src="{a('assets/icons/flask-conical.svg')}" alt="" /><span><strong>Methodos Lab</strong><small>연구소 소개</small></span></a>
          <a class="drop-item" href="{a('pages/about/mission.html')}"><img src="{a('assets/icons/target.svg')}" alt="" /><span><strong>미션</strong><small>비전과 목표</small></span></a>
          <a class="drop-item" href="{a('pages/about/contact.html')}"><img src="{a('assets/icons/mail.svg')}" alt="" /><span><strong>문의</strong><small>Contact</small></span></a>
        </div>
      </div>
    </nav>
    <a class="nav-cta" href="https://ai-research-os-web.vercel.app/" target="_blank" rel="noopener">StudiumR 열기 <img src="{a('assets/icons/arrow-right.svg')}" alt="" /></a>
    <button class="nav-toggle" type="button" aria-label="메뉴 열기" aria-expanded="false" data-icon-depth="{depth}">
      <img src="{a('assets/icons/menu.svg')}" alt="메뉴" />
    </button>
  </div>
</header>
<div class="mobile-panel" id="mobile-panel">
  <div class="mobile-group">
    <button type="button">제품 <img src="{a('assets/icons/chevron-down.svg')}" width="16" height="16" alt="" /></button>
    <div class="mobile-links">
      <a href="{a('pages/products/index.html')}">제품 개요</a>
      <a href="{a('pages/products/methodos-basic.html')}">methodos-basic</a>
      <a href="{a('pages/products/methodosQ.html')}">methodosQ</a>
      <a href="{a('pages/products/methodosG.html')}">methodosG</a>
      <a href="{a('pages/products/methodos.html')}">methodos (SaaS)</a>
      <a href="{a('pages/products/studiumr.html')}">StudiumR (SaaS)</a>
      <a href="{a('pages/products/compare.html')}">제품 비교</a>
    </div>
  </div>
  <div class="mobile-group">
    <button type="button">다운로드 <img src="{a('assets/icons/chevron-down.svg')}" width="16" height="16" alt="" /></button>
    <div class="mobile-links">
      <a href="{a('pages/download/index.html')}">다운로드 홈</a>
      <a href="{a('pages/download/desktop.html')}">Desktop 설치</a>
      <a href="{a('pages/download/saas.html')}">Cloud 시작</a>
      <a href="{a('pages/download/requirements.html')}">시스템 요구사항</a>
    </div>
  </div>
  <div class="mobile-group">
    <button type="button">학습 <img src="{a('assets/icons/chevron-down.svg')}" width="16" height="16" alt="" /></button>
    <div class="mobile-links">
      <a href="{a('pages/learn/getting-started.html')}">시작하기</a>
      <a href="{a('pages/learn/guides.html')}">사용자 가이드</a>
      <a href="{a('pages/learn/tutorials.html')}">튜토리얼</a>
    </div>
  </div>
  <div class="mobile-group">
    <button type="button">커뮤니티 <img src="{a('assets/icons/chevron-down.svg')}" width="16" height="16" alt="" /></button>
    <div class="mobile-links">
      <a href="{a('pages/community/blog.html')}">블로그</a>
    </div>
  </div>
  <div class="mobile-group">
    <button type="button">소개 <img src="{a('assets/icons/chevron-down.svg')}" width="16" height="16" alt="" /></button>
    <div class="mobile-links">
      <a href="{a('pages/about/lab.html')}">Methodos Lab</a>
      <a href="{a('pages/about/mission.html')}">미션</a>
      <a href="{a('pages/about/contact.html')}">문의</a>
    </div>
  </div>
  <div class="mobile-cta">
    <a class="btn btn-solid" href="https://ai-research-os-web.vercel.app/" target="_blank" rel="noopener">StudiumR 열기</a>
    <a class="btn btn-outline" href="https://methodos-eight.vercel.app/" target="_blank" rel="noopener">methodos 열기</a>
  </div>
</div>
"""


def footer(depth: str) -> str:
    a = lambda p: asset(depth, p)
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="{a('assets/logo/methodos-lab-logo.svg')}" alt="" />
        <div>
          <strong>Methodos Lab</strong>
          <p>연구방법을 위한 Desktop 분석 도구와 AI Research SaaS를 만드는 연구소입니다.</p>
        </div>
      </div>
      <div class="footer-col">
        <h4>Products</h4>
        <a href="{a('pages/products/methodos-basic.html')}">methodos-basic</a>
        <a href="{a('pages/products/methodosQ.html')}">methodosQ</a>
        <a href="{a('pages/products/methodosG.html')}">methodosG</a>
        <a href="{a('pages/products/methodos.html')}">methodos</a>
        <a href="{a('pages/products/studiumr.html')}">StudiumR</a>
      </div>
      <div class="footer-col">
        <h4>Resources</h4>
        <a href="{a('pages/learn/getting-started.html')}">시작하기</a>
        <a href="{a('pages/download/index.html')}">다운로드</a>
        </div>
      <div class="footer-col">
        <h4>Lab</h4>
        <a href="{a('pages/about/lab.html')}">소개</a>
        <a href="{a('pages/about/mission.html')}">미션</a>
        <a href="{a('pages/about/contact.html')}">문의</a>
        </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Methodos Lab</span>
      <span>Research methods · Desktop &amp; SaaS</span>
    </div>
  </div>
</footer>
"""


def page(title: str, depth: str, body: str, description: str = "") -> str:
    desc = description or f"{title} — Methodos Lab"
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="description" content="{desc}" />
  <title>{title} · Methodos Lab</title>
  <link rel="icon" href="{asset(depth, 'assets/logo/methodos-lab-logo.svg')}" type="image/svg+xml" />
  <link rel="stylesheet" href="{asset(depth, 'css/styles.css')}" />
</head>
<body>
{nav(depth)}
<main>
{body}
</main>
{footer(depth)}
<script src="{asset(depth, 'js/main.js')}"></script>
</body>
</html>
"""


def crumbs(items):
    parts = []
    for i, (label, href) in enumerate(items):
        if href and i < len(items) - 1:
            parts.append(f'<a href="{href}">{label}</a><span>/</span>')
        else:
            parts.append(f"<span>{label}</span>")
    return '<div class="breadcrumb">' + "".join(parts) + "</div>"


# ---------- Index ----------
index_body = f"""
<section class="hero">
  <div class="container hero-inner">
    <div class="hero-brand">
      <img src="assets/logo/methodos-lab-logo.svg" alt="Methodos Lab" />
      <strong>Methodos Lab</strong>
    </div>
    <h1>Methodos Lab은 연구 분석 방법, 문헌 연구, 논문 집필 과정에서 발생하는 복잡한 문제들을 근거 기반 AI와 절차적 솔루션으로 체계적으로 해결합니다. 이를 통해 연구자는 보다 효율적이고 신뢰성 있는 학술 성과를 도출할 수 있게 합니다.</h1>
    <p class="lead">통계·Q방법론·근거이론 설치형 분석 프로그램과, 절차적 연구방법·엔드투엔드 AI Research SaaS까지 — 연구 실행에 필요한 도구를 Methodos Lab이 설계합니다.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="pages/products/index.html">제품 살펴보기 <img src="assets/icons/arrow-right.svg" alt="" /></a>
      <a class="btn btn-ghost" href="https://ai-research-os-web.vercel.app/" target="_blank" rel="noopener">StudiumR 바로가기 <img class="invert" src="assets/icons/external-link.svg" alt="" /></a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Products</span>
      <h2>Methodos Lab 제품 구성</h2>
      <p>Desktop용 프로그램과 SaaS용 프로그램으로 구성되어 있습니다.</p>
    </div>
    <div class="tracks">
      <article class="track reveal">
        <span class="badge"><img src="assets/icons/laptop.svg" width="14" height="14" alt="" style="display:inline;vertical-align:-2px;filter:invert(34%) sepia(24%) saturate(1200%) hue-rotate(131deg)" /> Desktop</span>
        <h3>Desktop용 프로그램</h3>
        <p>methodos-basic, methodosQ, methodosG로 구성되어 있습니다.</p>
        <div class="product-list">
          <a class="product-row" href="pages/products/methodos-basic.html"><span class="meta"><span class="icon-wrap"><img src="assets/icons/bar-chart-3.svg" alt="" /></span><span><strong>methodos-basic</strong><small>통계분석 프로그램</small></span></span><span class="chip">Desktop</span></a>
          <a class="product-row" href="pages/products/methodosQ.html"><span class="meta"><span class="icon-wrap"><img src="assets/icons/layers.svg" alt="" /></span><span><strong>methodosQ</strong><small>Q방법론 분석</small></span></span><span class="chip">Desktop</span></a>
          <a class="product-row" href="pages/products/methodosG.html"><span class="meta"><span class="icon-wrap"><img src="assets/icons/network.svg" alt="" /></span><span><strong>methodosG</strong><small>근거이론 분석</small></span></span><span class="chip">Desktop</span></a>
        </div>
      </article>
      <article class="track saas reveal">
        <span class="badge blue"><img src="assets/icons/cloud.svg" width="14" height="14" alt="" style="display:inline;vertical-align:-2px;filter:invert(34%) sepia(40%) saturate(900%) hue-rotate(170deg)" /> SaaS</span>
        <h3>SaaS용 프로그램</h3>
        <p>methodos, StudiumR로 구성되어 있습니다.</p>
        <div class="product-list">
          <a class="product-row" href="pages/products/methodos.html"><span class="meta"><span class="icon-wrap"><img src="assets/icons/workflow.svg" alt="" /></span><span><strong>methodos</strong><small>절차적 단계 AI 연구방법</small></span></span><span class="chip">SaaS</span></a>
          <a class="product-row" href="pages/products/studiumr.html"><span class="meta"><span class="icon-wrap"><img src="assets/icons/brain.svg" alt="" /></span><span><strong>StudiumR</strong><small>End-to-End AI Research</small></span></span><span class="chip">SaaS</span></a>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Research flow</span>
      <h2>연구 흐름을 제품이 받쳐 줍니다</h2>
      <p>방법 선택부터 분석·검증·논문 생산까지, Lab 제품이 단계별로 연결됩니다.</p>
    </div>
    <div class="flow">
      <div class="flow-item reveal"><h3>방법 선택</h3><p>methodos가 연구질문·자료유형에 맞는 연구방법을 추천합니다.</p></div>
      <div class="flow-item reveal"><h3>전문 분석</h3><p>통계·Q방법론·근거이론은 Desktop 제품으로 깊게 수행합니다.</p></div>
      <div class="flow-item reveal"><h3>연구 프로세스</h3><p>단계 워크벤치와 검토·검증으로 절차를 남깁니다.</p></div>
      <div class="flow-item reveal"><h3>논문 생산</h3><p>StudiumR이 문헌·작성·크리틱까지 End-to-End로 이어 줍니다.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Security</span>
      <h2>로컬 우선 · 클라우드 메타데이터</h2>
      <p>StudiumR·methodos와 같은 보안 중심 파일 체계를 Lab 전체의 원칙으로 둡니다.</p>
    </div>
    <div class="layers">
      <div class="layer local reveal">
        <span class="badge" style="background:rgba(255,255,255,.12);color:#e8fffb">Local Storage</span>
        <h3>연구 산출물은 PC·브라우저에</h3>
        <p>Desktop 프로그램과 로컬 우선 SaaS가 민감 데이터를 사용자 쪽에 둡니다.</p>
        <div class="tag-row"><span>Projects</span><span>Datasets</span><span>Exports</span><span>AI Cache</span><span>Versions</span></div>
      </div>
      <div class="layer cloud reveal">
        <span class="badge blue" style="background:rgba(255,255,255,.12);color:#d9f0ff">Cloud Metadata</span>
        <h3>계정·협업 상태만 동기화</h3>
        <p>가벼운 메타데이터로 협업과 권한을 유지합니다.</p>
        <div class="tag-row"><span>Account</span><span>Permissions</span><span>Sync Index</span><span>Activity</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Why Methodos Lab</span>
      <h2>연구분석도구를 쉽고 편리하고 근거있게</h2>
    </div>
    <div class="feature-grid">
      <article class="feature reveal"><img src="assets/icons/microscope.svg" alt="" /><h3>방법론 특화</h3><p>일반 통계를 넘어 Q방법론·근거이론 등 연구 분석 워크벤치를 제공합니다.</p></article>
      <article class="feature reveal"><img src="assets/icons/cpu.svg" alt="" /><h3>AI와 절차의 결합</h3><p>연구방법 추천부터 단계 실행까지, AI가 절차를 깨지 않고 돕습니다.</p></article>
      <article class="feature reveal"><img src="assets/icons/shield.svg" alt="" /><h3>연구자 데이터 주권</h3><p>설치형과 로컬 우선 SaaS로 연구 파일의 통제권을 사용자에게 둡니다.</p></article>
    </div>
  </div>
</section>

<div class="cta-band reveal">
  <div>
    <h2>지금 바로 SaaS를 열어보세요</h2>
    <p>완성된 Cloud 제품은 즉시 실행할 수 있습니다. Desktop은 다운로드 페이지에서 안내합니다.</p>
  </div>
  <div class="cta-actions">
    <a class="btn btn-primary" href="https://ai-research-os-web.vercel.app/" target="_blank" rel="noopener">StudiumR</a>
    <a class="btn btn-ghost" href="https://methodos-eight.vercel.app/" target="_blank" rel="noopener">methodos</a>
    <a class="btn btn-ghost" href="pages/download/index.html">다운로드</a>
  </div>
</div>
"""

# ---------- Shared page bodies ----------
PAGES = {}

PAGES["pages/products/index.html"] = (
    "제품",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("제품", None)])}
<h1>Methodos Lab 제품</h1>
<p>Desktop 설치형 분석 프로그램 3종과 Cloud SaaS 2종으로 연구방법을 지원합니다.</p>
</div></section>
<section class="content-block"><div class="container">
<div class="tracks">
  <article class="track"><span class="badge">Desktop</span><h3>Desktop용 프로그램</h3><p>methodos-basic, methodosQ, methodosG로 구성되어 있습니다.</p>
  <div class="product-list">
    <a class="product-row" href="methodos-basic.html"><span class="meta"><span class="icon-wrap"><img src="../../assets/icons/bar-chart-3.svg" alt="" /></span><span><strong>methodos-basic</strong><small>통계분석</small></span></span><span class="chip">Desktop</span></a>
    <a class="product-row" href="methodosQ.html"><span class="meta"><span class="icon-wrap"><img src="../../assets/icons/layers.svg" alt="" /></span><span><strong>methodosQ</strong><small>Q방법론</small></span></span><span class="chip">Desktop</span></a>
    <a class="product-row" href="methodosG.html"><span class="meta"><span class="icon-wrap"><img src="../../assets/icons/network.svg" alt="" /></span><span><strong>methodosG</strong><small>근거이론</small></span></span><span class="chip">Desktop</span></a>
  </div></article>
  <article class="track saas"><span class="badge blue">SaaS</span><h3>SaaS용 프로그램</h3><p>methodos, StudiumR로 구성되어 있습니다.</p>
  <div class="product-list">
    <a class="product-row" href="methodos.html"><span class="meta"><span class="icon-wrap"><img src="../../assets/icons/workflow.svg" alt="" /></span><span><strong>methodos</strong><small>연구방법 OS</small></span></span><span class="chip">SaaS</span></a>
    <a class="product-row" href="studiumr.html"><span class="meta"><span class="icon-wrap"><img src="../../assets/icons/brain.svg" alt="" /></span><span><strong>StudiumR</strong><small>AI Research OS</small></span></span><span class="chip">SaaS</span></a>
  </div></article>
</div>
<p style="margin-top:1.5rem"><a class="btn btn-outline" href="compare.html">제품 비교 보기</a></p>
</div></section>
""",
)

PAGES["pages/products/methodos-basic.html"] = (
    "methodos-basic",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("제품", "index.html"), ("methodos-basic", None)])}
<h1>methodos-basic</h1>
<p>통계분석 프로그램 — 설치형·실행형 Desktop 애플리케이션입니다.</p>
</div></section>
<section class="content-block"><div class="container two-col">
<div class="prose">
  <h2>한눈에</h2>
  <p>methodos-basic은 사회과학·교육·보건 연구자가 자주 쓰는 통계 절차를 GUI로 수행하는 Desktop 통계분석 프로그램입니다. Methodos Lab의 Desktop 트랙 기본 제품입니다.</p>
  <h2>주요 기능 (요약)</h2>
  <ul>
    <li>데이터 불러오기 · 변수 관리 · 기초통계</li>
    <li>추론통계 · 회귀 · 분산분석 계열 워크플로</li>
    <li>결과 표·그래프 내보내기</li>
    <li>설치형(Setup) 및 포터블(실행형) 배포</li>
  </ul>
  <h2>배포 형태</h2>
  <p>설치형 Setup.exe · 포터블 실행 파일 형태로 제공될 예정입니다. 로컬 개발 산출물: MethodosBasic-LT 계열.</p>
  <p style="margin-top:1.2rem;display:flex;gap:.6rem;flex-wrap:wrap">
    <a class="btn btn-solid" href="../download/desktop.html">다운로드 안내</a>
    <a class="btn btn-outline" href="../learn/getting-started.html">시작하기</a>
  </p>
</div>
<aside class="side-panel">
  <h3>바로가기</h3>
  <a href="../download/desktop.html"><img src="../../assets/icons/download.svg" alt="" /> Desktop 다운로드</a>
  <a href="compare.html"><img src="../../assets/icons/layout-dashboard.svg" alt="" /> 제품 비교</a>
  <a href="../learn/guides.html"><img src="../../assets/icons/book-open.svg" alt="" /> 가이드</a>
</aside>
</div></section>
""",
)

PAGES["pages/products/methodosQ.html"] = (
    "methodosQ",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("제품", "index.html"), ("methodosQ", None)])}
<h1>methodosQ</h1>
<p>Q방법론 분석 프로그램 — 아키타입 단계·태스크 기반 Desktop 워크벤치입니다.</p>
</div></section>
<section class="content-block"><div class="container two-col">
<div class="prose">
  <h2>한눈에</h2>
  <p>methodosQ는 Q방법론(Q Methodology)의 표준 절차를 단계·태스크로 구조화한 설치형 분석 프로그램입니다.</p>
  <h2>워크플로 하이라이트</h2>
  <ul>
    <li>아키타입 기반 다단계·다태스크 진행</li>
    <li>분석 단계별 산출물·QC 체크</li>
    <li>Q표집·요인 관련 작업 흐름 지원</li>
    <li>Electron 기반 Desktop 실행</li>
  </ul>
  <p style="margin-top:1.2rem;display:flex;gap:.6rem;flex-wrap:wrap">
    <a class="btn btn-solid" href="../download/desktop.html">다운로드 안내</a>
  </p>
</div>
<aside class="side-panel">
  <h3>배포물</h3>
  <a href="../download/desktop.html"><img src="../../assets/icons/package.svg" alt="" /> methodosQ-v6-Setup.exe</a>
  <a href="../download/desktop.html"><img src="../../assets/icons/laptop.svg" alt="" /> methodosQ-v6-portable.exe</a>
</aside>
</div></section>
""",
)

PAGES["pages/products/methodosG.html"] = (
    "methodosG",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("제품", "index.html"), ("methodosG", None)])}
<h1>methodosG</h1>
<p>근거이론(Grounded Theory) 분석 프로그램 — 설치형·실행형 Desktop 도구입니다.</p>
</div></section>
<section class="content-block"><div class="container two-col">
<div class="prose">
  <h2>한눈에</h2>
  <p>methodosG는 근거이론 코딩·범주화·이론화 절차를 지원하는 Desktop 분석 프로그램입니다. Setup.exe와 Portable.exe로 배포됩니다.</p>
  <h2>지원 방향</h2>
  <ul>
    <li>질적 자료 코딩 워크벤치</li>
    <li>개방·축·선택 코딩 흐름 안내</li>
    <li>메모·범주·이론 메모 관리</li>
    <li>로컬 프로젝트 저장</li>
  </ul>
  <p style="margin-top:1.2rem"><a class="btn btn-solid" href="../download/desktop.html">다운로드 안내</a></p>
</div>
<aside class="side-panel">
  <h3>배포물</h3>
  <a href="../download/desktop.html"><img src="../../assets/icons/package.svg" alt="" /> MethodosG-v6-Setup.exe</a>
  <a href="../download/desktop.html"><img src="../../assets/icons/laptop.svg" alt="" /> MethodosG-v6-portable.exe</a>
</aside>
</div></section>
""",
)

PAGES["pages/products/methodos.html"] = (
    "methodos",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("제품", "index.html"), ("methodos", None)])}
<h1>methodos</h1>
<p>절차적 단계 AI 연구분석방법 프로그램 — Cloud SaaS입니다.</p>
</div></section>
<section class="content-block"><div class="container two-col">
<div class="prose">
  <p>methodos는 연구방법 추천·프로세스·카탈로그·11단계 워크벤치·시각화까지 한 흐름으로 지원하는 Research Methods OS입니다.</p>
  <h2>바로 실행</h2>
  <p>라이브 서비스가 배포되어 있습니다.</p>
  <p style="display:flex;gap:.6rem;flex-wrap:wrap;margin-top:1rem">
    <a class="btn btn-solid" href="https://methodos-eight.vercel.app/" target="_blank" rel="noopener">methodos 열기 <img class="invert" src="../../assets/icons/external-link.svg" alt="" style="width:14px;height:14px" /></a>
  </p>
  <h2>핵심 모듈</h2>
  <div class="card-list" style="margin-top:1rem">
    <div class="info-card"><h3>연구방법 추천</h3><p>질문·자료 유형 기반 AI·규칙 추천</p></div>
    <div class="info-card"><h3>Process Hub</h3><p>표준 방법 단계와 아키타입 공통절차</p></div>
    <div class="info-card"><h3>11단계 워크벤치</h3><p>단계·태스크 실행, 설문·통계·코딩</p></div>
    <div class="info-card"><h3>검토·검증</h3><p>산출물 입력·검증·재현 기록</p></div>
  </div>
</div>
<aside class="side-panel">
  <h3>라이브 링크</h3>
  <a href="https://methodos-eight.vercel.app/" target="_blank" rel="noopener"><img src="../../assets/icons/external-link.svg" alt="" /> methodos-eight.vercel.app</a>
  <a href="studiumr.html"><img src="../../assets/icons/brain.svg" alt="" /> StudiumR</a>
  <a href="../download/saas.html"><img src="../../assets/icons/cloud.svg" alt="" /> Cloud 시작</a>
</aside>
</div></section>
""",
)

PAGES["pages/products/studiumr.html"] = (
    "StudiumR",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("제품", "index.html"), ("StudiumR", None)])}
<h1>StudiumR</h1>
<p>End-to-End AI Research 프로그램 — 연구준비자(RDOS)와 연구자(AI-Research-OS) 트랙을 제공합니다.</p>
</div></section>
<section class="content-block"><div class="container two-col">
<div class="prose">
  <p>StudiumR은 문헌 연구부터 논문 구조·크리틱·참고문헌까지 이어 주는 AI Research Operating System입니다. Methodos Lab 홈페이지의 시각·섹션 포맷 레퍼런스이기도 합니다.</p>
  <p style="display:flex;gap:.6rem;flex-wrap:wrap;margin-top:1rem">
    <a class="btn btn-solid" href="https://ai-research-os-web.vercel.app/" target="_blank" rel="noopener">StudiumR 열기</a>
  </p>
  <h2>두 트랙</h2>
  <div class="tracks" style="margin-top:1rem">
    <div class="track"><span class="badge">RDOS</span><h3>연구준비자</h3><p>대학원 진학 예정자·석사과정·연구 입문자 — 논문·연구 역량 개발.</p></div>
    <div class="track saas"><span class="badge blue">AI-Research-OS</span><h3>연구자</h3><p>석사 이상·논문 저자·교수·연구원 — 실제 연구 수행·논문 생산.</p></div>
  </div>
</div>
<aside class="side-panel">
  <h3>라이브 링크</h3>
  <a href="https://ai-research-os-web.vercel.app/" target="_blank" rel="noopener"><img src="../../assets/icons/external-link.svg" alt="" /> ai-research-os-web.vercel.app</a>
  <a href="methodos.html"><img src="../../assets/icons/workflow.svg" alt="" /> methodos</a>
</aside>
</div></section>
""",
)

PAGES["pages/products/compare.html"] = (
    "제품 비교",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("제품", "index.html"), ("비교", None)])}
<h1>제품 비교</h1>
<p>Desktop과 SaaS 제품의 역할 차이를 한눈에 봅니다.</p>
</div></section>
<section class="content-block"><div class="container">
<div class="table-wrap">
<table class="compare">
  <thead><tr><th>제품</th><th>유형</th><th>초점</th><th>접속</th></tr></thead>
  <tbody>
    <tr><td>methodos-basic</td><td>Desktop</td><td>통계분석</td><td><a href="../download/desktop.html">다운로드 안내</a></td></tr>
    <tr><td>methodosQ</td><td>Desktop</td><td>Q방법론</td><td><a href="../download/desktop.html">다운로드 안내</a></td></tr>
    <tr><td>methodosG</td><td>Desktop</td><td>근거이론</td><td><a href="../download/desktop.html">다운로드 안내</a></td></tr>
    <tr><td>methodos</td><td>SaaS</td><td>연구방법 OS</td><td><a href="https://methodos-eight.vercel.app/" target="_blank" rel="noopener">라이브</a></td></tr>
    <tr><td>StudiumR</td><td>SaaS</td><td>End-to-End Research</td><td><a href="https://ai-research-os-web.vercel.app/" target="_blank" rel="noopener">라이브</a></td></tr>
  </tbody>
</table>
</div>
</div></section>
""",
)

# Download pages
PAGES["pages/download/index.html"] = (
    "다운로드",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("다운로드", None)])}
<h1>다운로드 · 시작하기</h1>
<p>Desktop은 설치 파일을, SaaS는 브라우저 접속으로 시작합니다. (jamovi·JASP·Orange의 Download 메뉴 패턴)</p>
</div></section>
<section class="content-block"><div class="container">
<div class="feature-grid">
  <a class="feature" href="desktop.html"><img src="../../assets/icons/download.svg" alt="" /><h3>Desktop 설치</h3><p>methodos-basic · Q · G</p></a>
  <a class="feature" href="saas.html"><img src="../../assets/icons/cloud.svg" alt="" /><h3>Cloud 시작</h3><p>methodos · StudiumR</p></a>
  <a class="feature" href="requirements.html"><img src="../../assets/icons/monitor.svg" alt="" /><h3>시스템 요구사항</h3><p>권장 사양 안내</p></a>
</div>
</div></section>
""",
)

PAGES["pages/download/desktop.html"] = (
    "Desktop 다운로드",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("다운로드", "index.html"), ("Desktop", None)])}
<h1>Desktop 설치 프로그램</h1>
</div></section>
<section class="content-block"><div class="container">
<div class="card-list">
  <div class="info-card"><h3>methodos-basic</h3><p>MethodosBasic-LT-Setup.exe (설치형) · MethodosBasic-LT.exe (포터블)</p></div>
  <div class="info-card"><h3>methodosQ</h3><p>methodosQ-v6-Setup.exe · methodosQ-v6-portable.exe</p></div>
  <div class="info-card"><h3>methodosG</h3><p>MethodosG-v6-Setup.exe · MethodosG-v6-portable.exe</p></div>
</div>
</div></section>
""",
)

PAGES["pages/download/saas.html"] = (
    "Cloud 시작",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("다운로드", "index.html"), ("Cloud", None)])}
<h1>Cloud · SaaS 시작하기</h1>
<p>설치 없이 브라우저에서 바로 실행합니다.</p>
</div></section>
<section class="content-block"><div class="container">
<div class="tracks">
  <article class="track"><span class="badge">methodos</span><h3>연구방법 OS</h3><p>방법 추천 · 프로세스 · 워크벤치</p>
  <p style="margin-top:1rem"><a class="btn btn-solid" href="https://methodos-eight.vercel.app/" target="_blank" rel="noopener">앱 열기</a></p></article>
  <article class="track saas"><span class="badge blue">StudiumR</span><h3>AI Research OS</h3><p>연구준비자 · 연구자 트랙</p>
  <p style="margin-top:1rem"><a class="btn btn-solid" href="https://ai-research-os-web.vercel.app/" target="_blank" rel="noopener">앱 열기</a></p></article>
</div>
</div></section>
""",
)

PAGES["pages/download/requirements.html"] = (
    "시스템 요구사항",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("다운로드", "index.html"), ("요구사항", None)])}
<h1>시스템 요구사항</h1>
</div></section>
<section class="content-block"><div class="container prose">
<ul>
  <li>OS: Windows 10/11 64-bit</li>
  <li>RAM: 8GB 이상 권장</li>
  <li>Disk: 500MB~2GB 여유 공간 (제품별 상이)</li>
  <li>SaaS: 최신 Chrome / Edge / Safari</li>
</ul>
</div></section>
""",
)

# Learn
PAGES["pages/learn/getting-started.html"] = (
    "시작하기",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("학습", None), ("시작하기", None)])}
<h1>시작하기</h1>
</div></section>
<section class="content-block"><div class="container">
<div class="flow">
  <div class="flow-item"><h3>제품 고르기</h3><p>통계·Q·근거이론 Desktop 또는 methodos·StudiumR SaaS</p></div>
  <div class="flow-item"><h3>설치 / 가입</h3><p>Desktop 설치 또는 Cloud 회원가입</p></div>
  <div class="flow-item"><h3>샘플로 연습</h3><p>예시 데이터·튜토리얼로 첫 분석</p></div>
  <div class="flow-item"><h3>가이드 심화</h3><p>사용자 가이드·튜토리얼로 확장</p></div>
</div>
</div></section>
""",
)

PAGES["pages/learn/guides.html"] = (
    "사용자 가이드",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("학습", "getting-started.html"), ("가이드", None)])}
<h1>사용자 가이드</h1>
</div></section>
<section class="content-block"><div class="container">
<div class="card-list">
  <a class="info-card" href="guides/methodos-basic.html"><h3>methodos-basic 가이드</h3><p>절차로 익히는 연구용 통계 · 소개 &amp; 절차 가이드</p></a>
  <a class="info-card" href="guides/methodosQ.html"><h3>methodosQ 가이드</h3><p>Q방법론 학습형 워크벤치 · 소개 &amp; 메뉴 가이드</p></a>
  <a class="info-card" href="guides/methodosG.html"><h3>methodosG 가이드</h3><p>근거이론 코딩·이론화 · 소개 &amp; 절차 가이드</p></a>
  <a class="info-card" href="guides/methodos-studiumr.html"><h3>methodos / StudiumR 가이드</h3><p>연구방법 OS · End-to-End AI Research</p></a>
</div>
</div></section>
""",
)

PAGES["pages/learn/tutorials.html"] = (
    "튜토리얼",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("학습", "getting-started.html"), ("튜토리얼", None)])}
<h1>튜토리얼 · 영상</h1>
</div></section>
<section class="content-block"><div class="container">
<div class="card-list">
  <article class="info-card tutorial-detail">
    <h3>01 · methodos-basic 실행방법</h3>
    <p>Framer Motion 절차 A·B로 예제 분석과 학습 경로를 따라가 봅니다.</p>
    <div class="tutorial-cols">
      <div>
        <h4>절차 A · 예제를 통한 분석</h4>
        <p>예제 자료 불러오기 → 기법 선택 → 변수·척도 → 분석 → 그래프·결과</p>
      </div>
      <div>
        <h4>절차 B · 학습으로 통계 익히기</h4>
        <p>명칭 → 초·중·고급 → 예제 확인 → 작업대 적용</p>
      </div>
    </div>
    <div class="tutorial-meta">
      <p class="tutorial-actions">
        <a class="btn btn-solid" href="guides/methodos-basic-procedure/index.html">절차 가이드 열기</a>
      </p>
    </div>
  </article>
  <article class="info-card tutorial-detail">
    <h3>02 · methodosQ 실행방법</h3>
    <p>Q방법론 8단계·학습 트랙을 번호 절차로 따라갑니다.</p>
    <div class="tutorial-cols">
      <div>
        <h4>절차 A · 예제로 Q분석</h4>
        <p>예제 → 포맷 → 내 자료 → 연구 8단계 → 해석·보고</p>
      </div>
      <div>
        <h4>절차 B · 학습 트랙</h4>
        <p>입문 → 연구중 → 논문대비 → 개념사전 → 예제 확인</p>
      </div>
    </div>
    <div class="tutorial-meta">
      <p class="tutorial-actions">
        <a class="btn btn-solid" href="guides/methodosQ-procedure/index.html">절차 가이드 열기</a>
      </p>
    </div>
  </article>
  <article class="info-card tutorial-detail">
    <h3>03 · methodosG 실행방법</h3>
    <p>근거이론 코딩·이론화 절차를 Desktop 워크벤치에서 따라갑니다.</p>
    <div class="tutorial-cols">
      <div>
        <h4>절차 A · 자료 → 코딩</h4>
        <p>불러오기 → 개방 → 축 → 선택 코딩</p>
      </div>
      <div>
        <h4>절차 B · 이론화 → 보고</h4>
        <p>메모 → 범주 → 이론 스케치 → 보고서</p>
      </div>
    </div>
    <div class="tutorial-meta">
      <p class="tutorial-actions">
        <a class="btn btn-solid" href="guides/methodosG-procedure/index.html">절차 가이드 열기</a>
      </p>
    </div>
  </article>
  <article class="info-card tutorial-detail">
    <h3>04 · methodos / StudiumR 실행방법</h3>
    <p>Cloud SaaS에서 방법 추천·워크벤치와 AI Research 트랙을 절차로 익힙니다.</p>
    <div class="tutorial-cols">
      <div>
        <h4>절차 A · methodos</h4>
        <p>방법 추천 → 프로세스 → 워크벤치 → 검토·검증</p>
      </div>
      <div>
        <h4>절차 B · StudiumR</h4>
        <p>대시보드 → 트랙 → 문헌·설계 → 작성 → 크리틱</p>
      </div>
    </div>
    <div class="tutorial-meta">
      <p class="tutorial-actions">
        <a class="btn btn-solid" href="guides/methodos-studiumr-procedure/index.html">절차 가이드 열기</a>
        <a class="btn btn-outline" href="https://methodos-eight.vercel.app/app" target="_blank" rel="noopener">methodos</a>
        <a class="btn btn-outline" href="https://ai-research-os-web.vercel.app/dashboard" target="_blank" rel="noopener">StudiumR</a>
      </p>
    </div>
  </article>
</div>
</div></section>
""",
)

# Community
PAGES["pages/community/index.html"] = (
    "커뮤니티",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("커뮤니티", None)])}
<h1>커뮤니티</h1>
<p>jamovi Community · JASP Community 메뉴를 Lab에 맞게 구성했습니다.</p>
</div></section>
<section class="content-block"><div class="container feature-grid">
  <a class="feature" href="blog.html"><img src="../../assets/icons/file-text.svg" alt="" /><h3>블로그</h3><p>Lab 소식</p></a>
</div></section>
""",
)

PAGES["pages/community/blog.html"] = (
    "블로그",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("커뮤니티", "index.html"), ("블로그", None)])}
<h1>블로그</h1>
</div></section>
<section class="content-block"><div class="container card-list">
  <div class="info-card"><h3>Methodos Lab 홈페이지 오픈</h3><p>2026-09-22 · Lab 소개</p></div>
  <div class="info-card"><h3>Desktop vs SaaS, 언제 무엇을?</h3><p>제품 선택 가이드</p></div>
  <div class="info-card"><h3>StudiumR 업데이트 노트</h3><p>릴리즈 하이라이트</p></div>
</div></section>
""",
)

# About
PAGES["pages/about/lab.html"] = (
    "Methodos Lab",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("소개", None), ("Lab", None)])}
<h1>Methodos Lab</h1>
<p>연구방법 Desktop 도구와 AI Research SaaS를 설계·배포하는 연구소입니다.</p>
</div></section>
<section class="content-block"><div class="container two-col">
<div class="prose">
  <p>Methodos Lab은 통계분석(methodos-basic), Q방법론(methodosQ), 근거이론(methodosG) 설치형 프로그램과, 절차적 연구방법(methodos), End-to-End AI Research(StudiumR) SaaS를 하나의 브랜드 아래에서 제공합니다.</p>
  <h2>제품 구성</h2>
  <ul>
    <li>Desktop: methodos-basic · methodosQ · methodosG</li>
    <li>SaaS: methodos · StudiumR</li>
  </ul>
</div>
<aside class="side-panel">
  <h3>더보기</h3>
  <a href="mission.html"><img src="../../assets/icons/target.svg" alt="" /> 미션</a>
  <a href="contact.html"><img src="../../assets/icons/mail.svg" alt="" /> 문의</a>
</aside>
</div></section>
""",
)

PAGES["pages/about/mission.html"] = (
    "미션",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("소개", "lab.html"), ("미션", None)])}
<h1>미션 · 비전</h1>
<p>Methodos Lab의 목표는 연구자가 방법 선택에서 분석과 논문 작성에 이르기까지 연구 과정 전반을 끊김 없이 이어갈 수 있도록 지원하는 것입니다.</p>
</div></section>
<section class="content-block"><div class="container prose">
<ul>
  <li>연구방법의 절차를 소프트웨어로 표준화한다</li>
  <li>전문 분석(Desktop)과 AI Research(SaaS)를 연결한다</li>
  <li>연구 데이터 활용의 자율성을 사용자에게 보장합니다</li>
  <li>교육·워크숍으로 연구 역량 확산을 돕는다</li>
</ul>
</div></section>
""",
)

PAGES["pages/about/contact.html"] = (
    "문의",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html"), ("소개", "lab.html"), ("문의", None)])}
<h1>문의</h1>
<p>협업·교육·라이선스 문의는 아래 이메일로 연락해 주세요.</p>
</div></section>
<section class="content-block"><div class="container">
<div class="card-list">
  <div class="info-card"><h3>일반 문의</h3><p><a href="mailto:sarangred777@gmail.com">sarangred777@gmail.com</a></p></div>
  <div class="info-card"><h3>교육 · 워크숍</h3><p><a href="mailto:shonpaul@daum.net">shonpaul@daum.net</a></p></div>
</div>
</div></section>
""",
)

# Pricing
def main():
    (ROOT / "index.html").write_text(page("홈", "", index_body, "Methodos Lab — 근거 기반 AI와 절차적 연구 솔루션"), encoding="utf-8")
    for rel, (title, depth, body) in PAGES.items():
        path = ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(page(title, depth, body), encoding="utf-8")
    # README
    (ROOT / "README.md").write_text(
        """# Methodos Lab Homepage (HTML Prototype)

Methodos Lab 공식 홈페이지 HTML 시안입니다. 최종 구현은 React로 이식하기 위한 디자인·정보구조 프로토타입입니다.

## Live SaaS
- methodos: https://methodos-eight.vercel.app/
- StudiumR: https://ai-research-os-web.vercel.app/

## Open locally
`index.html` 을 브라우저에서 엽니다.

## Stack note
- Fonts: NanumSquareNeo (로컬 복사)
- Icons: Lucide (free icon) + custom Lab logo
- Design reference: StudiumR landing structure
- Menu reference: JASP, jamovi, Orange
""",
        encoding="utf-8",
    )
    print("Generated", 1 + len(PAGES), "pages")


if __name__ == "__main__":
    main()

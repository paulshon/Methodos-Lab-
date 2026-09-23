# -*- coding: utf-8 -*-
"""Generate Methodos Lab HTML prototype pages."""
from pathlib import Path

ROOT = Path(r"C:\Users\saran\OneDrive\Desktop\메스도스랩-홈페이지")


def asset(depth: str, path: str) -> str:
    return f"{depth}{path}"


def lang_switch() -> str:
    return """
<div class="lang-switch" role="group" aria-label="Language">
  <button type="button" class="lang-switch__btn" data-locale="ko" aria-pressed="true">KO</button>
  <button type="button" class="lang-switch__btn" data-locale="en" aria-pressed="false">EN</button>
  <button type="button" class="lang-switch__btn" data-locale="zh" aria-pressed="false">ZH</button>
</div>
"""


def nav(depth: str) -> str:
    a = lambda p: asset(depth, p)
    return f"""
<header class="site-header">
  <div class="container nav-inner">
    <a class="brand" href="{a('index.html')}">
      <img src="{a('assets/logo/methodos-lab-logo.svg')}" alt="Methodos Lab" />
      <span>Methodos <em>Lab</em></span>
    </a>
    <nav class="nav-desktop" aria-label="주 메뉴" data-i18n-aria="nav.aria">
      <div class="nav-item">
        <a class="nav-link" href="{a('pages/products/index.html')}" aria-haspopup="true" aria-expanded="false"><span data-i18n="nav.products">제품</span> <img class="chev" src="{a('assets/icons/chevron-down.svg')}" alt="" /></a>
        <div class="dropdown wide" role="menu">
          <div class="drop-label" data-i18n="nav.desktop">Desktop · 설치형</div>
          <a class="drop-item" href="{a('pages/products/methodos-basic.html')}"><img src="{a('assets/icons/bar-chart-3.svg')}" alt="" /><span><strong>methodos-basic</strong><small data-i18n="nav.basic.desc">통계분석 프로그램</small></span></a>
          <a class="drop-item" href="{a('pages/products/methodosQ.html')}"><img src="{a('assets/icons/layers.svg')}" alt="" /><span><strong>methodosQ</strong><small data-i18n="nav.q.desc">Q방법론 분석</small></span></a>
          <a class="drop-item" href="{a('pages/products/methodosG.html')}"><img src="{a('assets/icons/network.svg')}" alt="" /><span><strong>methodosG</strong><small data-i18n="nav.g.desc">근거이론 분석</small></span></a>
          <div class="drop-label" data-i18n="nav.cloud">Cloud · SaaS</div>
          <a class="drop-item" href="{a('pages/products/methodos.html')}"><img src="{a('assets/icons/workflow.svg')}" alt="" /><span><strong>methodos</strong><small data-i18n="nav.methodos.desc">절차적 단계 AI 연구방법</small></span></a>
          <a class="drop-item" href="{a('pages/products/studiumr.html')}"><img src="{a('assets/icons/brain.svg')}" alt="" /><span><strong>StudiumR</strong><small data-i18n="nav.studiumr.desc">End-to-End AI Research OS</small></span></a>
          <a class="drop-item" href="{a('pages/products/compare.html')}"><img src="{a('assets/icons/layout-dashboard.svg')}" alt="" /><span><strong data-i18n="nav.compare">제품 비교</strong><small data-i18n="nav.compare.desc">Desktop / SaaS 한눈에</small></span></a>
        </div>
      </div>
      <div class="nav-item">
        <a class="nav-link" href="{a('pages/download/index.html')}" aria-haspopup="true" aria-expanded="false"><span data-i18n="nav.download">다운로드</span> <img class="chev" src="{a('assets/icons/chevron-down.svg')}" alt="" /></a>
        <div class="dropdown" role="menu">
          <a class="drop-item" href="{a('pages/download/desktop.html')}"><img src="{a('assets/icons/download.svg')}" alt="" /><span><strong data-i18n="nav.desktopInstall">Desktop 설치</strong><small data-i18n="nav.desktopInstall.desc">basic · Q · G</small></span></a>
          <a class="drop-item" href="{a('pages/download/saas.html')}"><img src="{a('assets/icons/cloud.svg')}" alt="" /><span><strong data-i18n="nav.cloudStart">Cloud 시작</strong><small data-i18n="nav.cloudStart.desc">methodos · StudiumR</small></span></a>
          <a class="drop-item" href="{a('pages/download/requirements.html')}"><img src="{a('assets/icons/monitor.svg')}" alt="" /><span><strong data-i18n="nav.requirements">시스템 요구사항</strong><small data-i18n="nav.requirements.desc">권장 사양</small></span></a>
        </div>
      </div>
      <div class="nav-item">
        <a class="nav-link" href="{a('pages/learn/getting-started.html')}" aria-haspopup="true" aria-expanded="false"><span data-i18n="nav.learn">학습</span> <img class="chev" src="{a('assets/icons/chevron-down.svg')}" alt="" /></a>
        <div class="dropdown" role="menu">
          <a class="drop-item" href="{a('pages/learn/getting-started.html')}"><img src="{a('assets/icons/compass.svg')}" alt="" /><span><strong data-i18n="nav.gettingStarted">시작하기</strong><small data-i18n="nav.gettingStarted.desc">첫 실행 가이드</small></span></a>
          <a class="drop-item" href="{a('pages/learn/guides.html')}"><img src="{a('assets/icons/book-open.svg')}" alt="" /><span><strong data-i18n="nav.guides">사용자 가이드</strong><small data-i18n="nav.guides.desc">가이드</small></span></a>
          <a class="drop-item" href="{a('pages/learn/tutorials.html')}"><img src="{a('assets/icons/video.svg')}" alt="" /><span><strong data-i18n="nav.tutorials">튜토리얼</strong><small data-i18n="nav.tutorials.desc">영상</small></span></a>
        </div>
      </div>
      <div class="nav-item">
        <a class="nav-link" href="{a('pages/community/index.html')}" aria-haspopup="true" aria-expanded="false"><span data-i18n="nav.community">커뮤니티</span> <img class="chev" src="{a('assets/icons/chevron-down.svg')}" alt="" /></a>
        <div class="dropdown" role="menu">
          <a class="drop-item" href="{a('pages/community/blog.html')}"><img src="{a('assets/icons/file-text.svg')}" alt="" /><span><strong data-i18n="nav.blog">블로그</strong><small data-i18n="nav.blog.desc">소식</small></span></a>
        </div>
      </div>
      <div class="nav-item">
        <a class="nav-link" href="{a('pages/about/lab.html')}" aria-haspopup="true" aria-expanded="false"><span data-i18n="nav.about">소개</span> <img class="chev" src="{a('assets/icons/chevron-down.svg')}" alt="" /></a>
        <div class="dropdown" role="menu">
          <a class="drop-item" href="{a('pages/about/lab.html')}"><img src="{a('assets/icons/flask-conical.svg')}" alt="" /><span><strong>Methodos Lab</strong><small data-i18n="nav.lab.desc">연구소 소개</small></span></a>
          <a class="drop-item" href="{a('pages/about/mission.html')}"><img src="{a('assets/icons/target.svg')}" alt="" /><span><strong data-i18n="nav.mission">미션</strong><small data-i18n="nav.mission.desc">비전과 목표</small></span></a>
          <a class="drop-item" href="{a('pages/about/contact.html')}"><img src="{a('assets/icons/mail.svg')}" alt="" /><span><strong data-i18n="nav.contact">문의</strong><small>Contact</small></span></a>
        </div>
      </div>
    </nav>
    {lang_switch()}
    <a class="nav-cta" href="https://ai-research-os-web.vercel.app/" target="_blank" rel="noopener"><span data-i18n="nav.cta">StudiumR 열기</span> <img src="{a('assets/icons/arrow-right.svg')}" alt="" /></a>
    <button class="nav-toggle" type="button" aria-label="메뉴 열기" data-i18n-aria="nav.menu" aria-expanded="false" data-icon-depth="{depth}">
      <img src="{a('assets/icons/menu.svg')}" alt="메뉴" />
    </button>
  </div>
</header>
<div class="mobile-panel" id="mobile-panel">
  <div class="mobile-lang">{lang_switch()}</div>
  <div class="mobile-group">
    <button type="button"><span data-i18n="nav.products">제품</span> <img src="{a('assets/icons/chevron-down.svg')}" width="16" height="16" alt="" /></button>
    <div class="mobile-links">
      <a href="{a('pages/products/index.html')}" data-i18n="nav.productsOverview">제품 개요</a>
      <a href="{a('pages/products/methodos-basic.html')}">methodos-basic</a>
      <a href="{a('pages/products/methodosQ.html')}">methodosQ</a>
      <a href="{a('pages/products/methodosG.html')}">methodosG</a>
      <a href="{a('pages/products/methodos.html')}">methodos (SaaS)</a>
      <a href="{a('pages/products/studiumr.html')}">StudiumR (SaaS)</a>
      <a href="{a('pages/products/compare.html')}" data-i18n="nav.compare">제품 비교</a>
    </div>
  </div>
  <div class="mobile-group">
    <button type="button"><span data-i18n="nav.download">다운로드</span> <img src="{a('assets/icons/chevron-down.svg')}" width="16" height="16" alt="" /></button>
    <div class="mobile-links">
      <a href="{a('pages/download/index.html')}" data-i18n="nav.downloadHome">다운로드 홈</a>
      <a href="{a('pages/download/desktop.html')}" data-i18n="nav.desktopInstall">Desktop 설치</a>
      <a href="{a('pages/download/saas.html')}" data-i18n="nav.cloudStart">Cloud 시작</a>
      <a href="{a('pages/download/requirements.html')}" data-i18n="nav.requirements">시스템 요구사항</a>
    </div>
  </div>
  <div class="mobile-group">
    <button type="button"><span data-i18n="nav.learn">학습</span> <img src="{a('assets/icons/chevron-down.svg')}" width="16" height="16" alt="" /></button>
    <div class="mobile-links">
      <a href="{a('pages/learn/getting-started.html')}" data-i18n="nav.gettingStarted">시작하기</a>
      <a href="{a('pages/learn/guides.html')}" data-i18n="nav.guides">사용자 가이드</a>
      <a href="{a('pages/learn/tutorials.html')}" data-i18n="nav.tutorials">튜토리얼</a>
    </div>
  </div>
  <div class="mobile-group">
    <button type="button"><span data-i18n="nav.community">커뮤니티</span> <img src="{a('assets/icons/chevron-down.svg')}" width="16" height="16" alt="" /></button>
    <div class="mobile-links">
      <a href="{a('pages/community/blog.html')}" data-i18n="nav.blog">블로그</a>
    </div>
  </div>
  <div class="mobile-group">
    <button type="button"><span data-i18n="nav.about">소개</span> <img src="{a('assets/icons/chevron-down.svg')}" width="16" height="16" alt="" /></button>
    <div class="mobile-links">
      <a href="{a('pages/about/lab.html')}">Methodos Lab</a>
      <a href="{a('pages/about/mission.html')}" data-i18n="nav.mission">미션</a>
      <a href="{a('pages/about/contact.html')}" data-i18n="nav.contact">문의</a>
    </div>
  </div>
  <div class="mobile-cta">
    <a class="btn btn-solid" href="https://ai-research-os-web.vercel.app/" target="_blank" rel="noopener" data-i18n="nav.cta">StudiumR 열기</a>
    <a class="btn btn-outline" href="https://methodos-eight.vercel.app/" target="_blank" rel="noopener" data-i18n="nav.methodosOpen">methodos 열기</a>
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
          <p data-i18n="footer.blurb">연구방법을 위한 Desktop 분석 도구와 AI Research SaaS를 만드는 연구소입니다.</p>
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
        <h4 data-i18n="footer.resources">Resources</h4>
        <a href="{a('pages/learn/getting-started.html')}" data-i18n="nav.gettingStarted">시작하기</a>
        <a href="{a('pages/download/index.html')}" data-i18n="nav.download">다운로드</a>
        </div>
      <div class="footer-col">
        <h4 data-i18n="footer.lab">Lab</h4>
        <a href="{a('pages/about/lab.html')}" data-i18n="nav.about">소개</a>
        <a href="{a('pages/about/mission.html')}" data-i18n="nav.mission">미션</a>
        <a href="{a('pages/about/contact.html')}" data-i18n="nav.contact">문의</a>
        </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Methodos Lab</span>
      <span data-i18n="footer.tag">Research methods · Desktop &amp; SaaS</span>
    </div>
  </div>
</footer>
"""


def page(title: str, depth: str, body: str, description: str = "", title_key: str = "") -> str:
    desc = description or f"{title} — Methodos Lab"
    tkey = title_key or ""
    title_attr = f' data-i18n-title="{tkey}"' if tkey else ""
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="description" content="{desc}" />
  <title{title_attr}>{title} · Methodos Lab</title>
  <link rel="icon" href="{asset(depth, 'assets/logo/methodos-lab-logo.svg')}" type="image/svg+xml" />
  <link rel="stylesheet" href="{asset(depth, 'css/styles.css')}" />
</head>
<body>
{nav(depth)}
<main>
{body}
</main>
{footer(depth)}
<script src="{asset(depth, 'js/i18n-dict.js')}"></script>
<script src="{asset(depth, 'js/i18n.js')}"></script>
<script src="{asset(depth, 'js/main.js')}"></script>
</body>
</html>
"""


def crumbs(items):
    parts = []
    for i, item in enumerate(items):
        if len(item) == 3:
            label, href, key = item
        else:
            label, href = item
            key = None
        attr = f' data-i18n="{key}"' if key else ""
        if href and i < len(items) - 1:
            parts.append(f'<a href="{href}"{attr}>{label}</a><span>/</span>')
        else:
            parts.append(f"<span{attr}>{label}</span>")
    return '<div class="breadcrumb">' + "".join(parts) + "</div>"


def video_guide(ko: str, en: str, zh: str) -> str:
    return f"""
<div class="video-guide" role="group" aria-label="Video guide">
  <span class="video-guide__label" data-i18n="tut.videoGuide">동영상 가이드</span>
  <div class="video-guide__langs">
    <a class="video-lang" href="{ko}" target="_blank" rel="noopener">KO</a>
    <a class="video-lang" href="{en}" target="_blank" rel="noopener">EN</a>
    <a class="video-lang" href="{zh}" target="_blank" rel="noopener">ZH</a>
  </div>
</div>
"""

# ---------- Index ----------
index_body = f"""
<section class="hero">
  <div class="container hero-inner">
    <div class="hero-brand">
      <img src="assets/logo/methodos-lab-logo.svg" alt="Methodos Lab" />
      <strong>Methodos Lab</strong>
    </div>
    <h1 data-i18n="home.h1">Methodos Lab은 연구 분석 방법, 문헌 연구, 논문 집필 과정에서 발생하는 복잡한 문제들을 근거 기반 AI와 절차적 솔루션으로 체계적으로 해결합니다. 이를 통해 연구자는 보다 효율적이고 신뢰성 있는 학술 성과를 도출할 수 있게 합니다.</h1>
    <p class="lead" data-i18n="home.lead">통계·Q방법론·근거이론 설치형 분석 프로그램과, 절차적 연구방법·엔드투엔드 AI Research SaaS까지 — 연구 실행에 필요한 도구를 Methodos Lab이 설계합니다.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="pages/products/index.html"><span data-i18n="home.ctaProducts">제품 살펴보기</span> <img src="assets/icons/arrow-right.svg" alt="" /></a>
      <a class="btn btn-ghost" href="https://ai-research-os-web.vercel.app/" target="_blank" rel="noopener"><span data-i18n="home.ctaStudiumr">StudiumR 바로가기</span> <img class="invert" src="assets/icons/external-link.svg" alt="" /></a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Products</span>
      <h2 data-i18n="home.productsTitle">Methodos Lab 제품 구성</h2>
      <p data-i18n="home.productsSub">Desktop용 프로그램과 SaaS용 프로그램으로 구성되어 있습니다.</p>
    </div>
    <div class="tracks">
      <article class="track reveal">
        <span class="badge"><img src="assets/icons/laptop.svg" width="14" height="14" alt="" style="display:inline;vertical-align:-2px;filter:invert(34%) sepia(24%) saturate(1200%) hue-rotate(131deg)" /> Desktop</span>
        <h3 data-i18n="home.desktopTitle">Desktop용 프로그램</h3>
        <p data-i18n="home.desktopBody">methodos-basic, methodosQ, methodosG로 구성되어 있습니다.</p>
        <div class="product-list">
          <a class="product-row" href="pages/products/methodos-basic.html"><span class="meta"><span class="icon-wrap"><img src="assets/icons/bar-chart-3.svg" alt="" /></span><span><strong>methodos-basic</strong><small>통계분석 프로그램</small></span></span><span class="chip">Desktop</span></a>
          <a class="product-row" href="pages/products/methodosQ.html"><span class="meta"><span class="icon-wrap"><img src="assets/icons/layers.svg" alt="" /></span><span><strong>methodosQ</strong><small>Q방법론 분석</small></span></span><span class="chip">Desktop</span></a>
          <a class="product-row" href="pages/products/methodosG.html"><span class="meta"><span class="icon-wrap"><img src="assets/icons/network.svg" alt="" /></span><span><strong>methodosG</strong><small>근거이론 분석</small></span></span><span class="chip">Desktop</span></a>
        </div>
      </article>
      <article class="track saas reveal">
        <span class="badge blue"><img src="assets/icons/cloud.svg" width="14" height="14" alt="" style="display:inline;vertical-align:-2px;filter:invert(34%) sepia(40%) saturate(900%) hue-rotate(170deg)" /> SaaS</span>
        <h3 data-i18n="home.saasTitle">SaaS용 프로그램</h3>
        <p data-i18n="home.saasBody">methodos, StudiumR로 구성되어 있습니다.</p>
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
      <h2 data-i18n="home.flowTitle">연구 흐름을 제품이 받쳐 줍니다</h2>
      <p data-i18n="home.flowSub">방법 선택부터 분석·검증·논문 생산까지, Lab 제품이 단계별로 연결됩니다.</p>
    </div>
    <div class="flow">
      <div class="flow-item reveal"><h3 data-i18n="home.flow1">방법 선택</h3><p data-i18n="home.flow1p">methodos가 연구질문·자료유형에 맞는 연구방법을 추천합니다.</p></div>
      <div class="flow-item reveal"><h3 data-i18n="home.flow2">전문 분석</h3><p data-i18n="home.flow2p">통계·Q방법론·근거이론은 Desktop 제품으로 깊게 수행합니다.</p></div>
      <div class="flow-item reveal"><h3 data-i18n="home.flow3">연구 프로세스</h3><p data-i18n="home.flow3p">단계 워크벤치와 검토·검증으로 절차를 남깁니다.</p></div>
      <div class="flow-item reveal"><h3 data-i18n="home.flow4">논문 생산</h3><p data-i18n="home.flow4p">StudiumR이 문헌·작성·크리틱까지 End-to-End로 이어 줍니다.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Security</span>
      <h2 data-i18n="home.secTitle">로컬 우선 · 클라우드 메타데이터</h2>
      <p data-i18n="home.secSub">StudiumR·methodos와 같은 보안 중심 파일 체계를 Lab 전체의 원칙으로 둡니다.</p>
    </div>
    <div class="layers">
      <div class="layer local reveal">
        <span class="badge" style="background:rgba(255,255,255,.12);color:#e8fffb">Local Storage</span>
        <h3 data-i18n="home.localTitle">연구 산출물은 PC·브라우저에</h3>
        <p data-i18n="home.localBody">Desktop 프로그램과 로컬 우선 SaaS가 민감 데이터를 사용자 쪽에 둡니다.</p>
        <div class="tag-row"><span>Projects</span><span>Datasets</span><span>Exports</span><span>AI Cache</span><span>Versions</span></div>
      </div>
      <div class="layer cloud reveal">
        <span class="badge blue" style="background:rgba(255,255,255,.12);color:#d9f0ff">Cloud Metadata</span>
        <h3 data-i18n="home.cloudTitle">계정·협업 상태만 동기화</h3>
        <p data-i18n="home.cloudBody">가벼운 메타데이터로 협업과 권한을 유지합니다.</p>
        <div class="tag-row"><span>Account</span><span>Permissions</span><span>Sync Index</span><span>Activity</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Why Methodos Lab</span>
      <h2 data-i18n="home.whyTitle">연구분석도구를 쉽고 편리하고 근거있게</h2>
    </div>
    <div class="feature-grid">
      <article class="feature reveal"><img src="assets/icons/microscope.svg" alt="" /><h3 data-i18n="home.why1">방법론 특화</h3><p data-i18n="home.why1p">일반 통계를 넘어 Q방법론·근거이론 등 연구 분석 워크벤치를 제공합니다.</p></article>
      <article class="feature reveal"><img src="assets/icons/cpu.svg" alt="" /><h3 data-i18n="home.why2">AI와 절차의 결합</h3><p data-i18n="home.why2p">연구방법 추천부터 단계 실행까지, AI가 절차를 깨지 않고 돕습니다.</p></article>
      <article class="feature reveal"><img src="assets/icons/shield.svg" alt="" /><h3 data-i18n="home.why3">연구자 데이터 주권</h3><p data-i18n="home.why3p">설치형과 로컬 우선 SaaS로 연구 파일의 통제권을 사용자에게 둡니다.</p></article>
    </div>
  </div>
</section>

<div class="cta-band reveal">
  <div>
    <h2 data-i18n="home.ctaBand">지금 바로 SaaS를 열어보세요</h2>
    <p data-i18n="home.ctaBandP">완성된 Cloud 제품은 즉시 실행할 수 있습니다. Desktop은 다운로드 페이지에서 안내합니다.</p>
  </div>
  <div class="cta-actions">
    <a class="btn btn-primary" href="https://ai-research-os-web.vercel.app/" target="_blank" rel="noopener">StudiumR</a>
    <a class="btn btn-ghost" href="https://methodos-eight.vercel.app/" target="_blank" rel="noopener">methodos</a>
    <a class="btn btn-ghost" href="pages/download/index.html" data-i18n="nav.download">다운로드</a>
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
  <p>methodos-basic은 모든 학술분야에서 연구자가 자주 쓰는 통계 절차를 GUI로 수행하는 Desktop 통계분석 프로그램입니다. Methodos Lab의 Desktop 트랙 기본 통계분석 제품입니다.</p>
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
  <h3 data-i18n="common.shortcuts">바로가기</h3>
  <a href="../download/desktop.html"><img src="../../assets/icons/download.svg" alt="" /> <span data-i18n="common.desktopDownload">Desktop 다운로드</span></a>
  <a href="compare.html"><img src="../../assets/icons/layout-dashboard.svg" alt="" /> <span data-i18n="nav.compare">제품 비교</span></a>
  <a href="../learn/guides.html"><img src="../../assets/icons/book-open.svg" alt="" /> <span data-i18n="nav.guides.desc">가이드</span></a>
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
  <p>methodosQ는 Q방법론(Q Methodology)의 표준 절차를 단계·태스크로 구조화한 분석 프로그램입니다.</p>
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
  <p>methodosG는 근거이론 코딩·범주화·이론화 절차를 지원하는 분석 프로그램입니다.</p>
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
<section class="content-block"><div class="container">
<div class="prose">
  <p>methodos는 연구방법 추천·프로세스·카탈로그·11단계 워크벤치·시각화까지 한 흐름으로 지원하는 Research Methods OS입니다.</p>
  <h2>바로 실행</h2>
  <p>실시간서비스를 지원합니다.</p>
  <p style="display:flex;gap:.6rem;flex-wrap:wrap;margin-top:1rem">
    <a class="btn btn-solid" href="https://methodos-eight.vercel.app/" target="_blank" rel="noopener" data-i18n="nav.methodosOpen">methodos 열기 <img class="invert" src="../../assets/icons/external-link.svg" alt="" style="width:14px;height:14px" /></a>
  </p>
  <h2>핵심 모듈</h2>
  <div class="card-list" style="margin-top:1rem">
    <div class="info-card"><h3>연구방법 추천</h3><p>질문·자료 유형 기반 AI·규칙 추천</p></div>
    <div class="info-card"><h3>Process Hub</h3><p>표준 방법 단계와 아키타입 공통절차</p></div>
    <div class="info-card"><h3>11단계 워크벤치</h3><p>단계·태스크 실행, 설문·통계·코딩</p></div>
    <div class="info-card"><h3>검토·검증</h3><p>산출물 입력·검증·재현 기록</p></div>
  </div>
</div>
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
<section class="content-block"><div class="container">
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
    <tr><td>methodos</td><td>SaaS</td><td>연구방법 OS</td><td><a href="https://methodos-eight.vercel.app/" target="_blank" rel="noopener">실시간 지원</a></td></tr>
    <tr><td>StudiumR</td><td>SaaS</td><td>End-to-End Research</td><td><a href="https://ai-research-os-web.vercel.app/" target="_blank" rel="noopener">실시간 지원</a></td></tr>
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
{crumbs([("홈", "../../index.html", "crumb.home"), ("학습", "getting-started.html", "nav.learn"), ("튜토리얼", None, "nav.tutorials")])}
<h1 data-i18n="tut.title">튜토리얼 · 영상</h1>
</div></section>
<section class="content-block"><div class="container">
<div class="card-list">
  <article class="info-card tutorial-detail">
    <h3 data-i18n="tut.b1">01 · methodos-basic 실행방법</h3>
    <p data-i18n="tut.b1p">절차 A·B로 예제 분석과 학습 경로를 따라가 봅니다.</p>
    <div class="tutorial-cols">
      <div>
        <h4 data-i18n="tut.b1a">절차 A · 예제를 통한 분석</h4>
        <p data-i18n="tut.b1ap">예제 자료 불러오기 → 기법 선택 → 변수·척도 → 분석 → 그래프·결과</p>
      </div>
      <div>
        <h4 data-i18n="tut.b1b">절차 B · 학습으로 통계 익히기</h4>
        <p data-i18n="tut.b1bp">명칭 → 초·중·고급 → 예제 확인 → 작업대 적용</p>
      </div>
    </div>
    <div class="tutorial-meta">
      <div class="tutorial-actions">
        <a class="btn btn-solid" href="guides/methodos-basic-procedure/index.html" data-i18n="tut.openGuide">절차 가이드 열기</a>
        {video_guide("https://youtu.be/tV5cnbs04l0", "https://youtu.be/hjxgEtSTjZE", "https://youtu.be/6wMh3WetF4w")}
      </div>
    </div>
  </article>
  <article class="info-card tutorial-detail">
    <h3 data-i18n="tut.q1">02 · methodosQ 실행방법</h3>
    <p data-i18n="tut.q1p">Q방법론 8단계·학습 트랙을 번호 절차로 따라갑니다.</p>
    <div class="tutorial-cols">
      <div>
        <h4 data-i18n="tut.q1a">절차 A · 예제로 Q분석</h4>
        <p data-i18n="tut.q1ap">예제 → 포맷 → 내 자료 → 연구 8단계 → 해석·보고</p>
      </div>
      <div>
        <h4 data-i18n="tut.q1b">절차 B · 학습 트랙</h4>
        <p data-i18n="tut.q1bp">입문 → 연구중 → 논문대비 → 개념사전 → 예제 확인</p>
      </div>
    </div>
    <div class="tutorial-meta">
      <div class="tutorial-actions">
        <a class="btn btn-solid" href="guides/methodosQ-procedure/index.html" data-i18n="tut.openGuide">절차 가이드 열기</a>
        {video_guide("https://youtu.be/f0T824pN8BY", "https://youtu.be/ajOUS-qB8Go", "https://youtu.be/o2wNfGSPZsI")}
      </div>
    </div>
  </article>
  <article class="info-card tutorial-detail">
    <h3 data-i18n="tut.g1">03 · methodosG 실행방법</h3>
    <p data-i18n="tut.g1p">예제 자료(다문화 가족 사례)로 근거이론 코딩·이론화 절차를 따라갑니다.</p>
    <div class="tutorial-cols">
      <div>
        <h4 data-i18n="tut.g1a">절차 A · 예제 → 코딩</h4>
        <p data-i18n="tut.g1ap">예제 자료 → 문제 설정 → 근거자료 → 의미추출 → 범주연결 → 이론응축</p>
      </div>
      <div>
        <h4 data-i18n="tut.g1b">절차 B · 이론화 → 보고</h4>
        <p data-i18n="tut.g1bp">결과 그래프 → 이론 결과 → 절차형 실습 → 홈 진행 → 논문형 결과</p>
      </div>
    </div>
    <div class="tutorial-meta">
      <div class="tutorial-actions">
        <a class="btn btn-solid" href="guides/methodosG-procedure/index.html" data-i18n="tut.openGuide">절차 가이드 열기</a>
        {video_guide("https://youtu.be/6UICh51nlRU", "https://youtu.be/6jWPaLiLK_c", "https://youtu.be/wM_tQsWB6QU")}
      </div>
    </div>
  </article>
  <article class="info-card tutorial-detail">
    <h3 data-i18n="tut.s1">04 · methodos / StudiumR 실행방법</h3>
    <p data-i18n="tut.s1p">Cloud SaaS에서 방법 추천·워크벤치와 AI Research 트랙을 절차로 익힙니다.</p>
    <div class="tutorial-cols">
      <div>
        <h4 data-i18n="tut.s1a">절차 A · methodos</h4>
        <p data-i18n="tut.s1ap">방법 추천 → 프로세스 → 워크벤치 → 검토·검증</p>
      </div>
      <div>
        <h4 data-i18n="tut.s1b">절차 B · StudiumR</h4>
        <p data-i18n="tut.s1bp">대시보드 → 트랙 → 문헌·설계 → 작성 → 크리틱</p>
      </div>
    </div>
    <div class="tutorial-meta">
      <div class="tutorial-actions">
        <a class="btn btn-solid" href="guides/methodos-studiumr-procedure/index.html" data-i18n="tut.openGuide">절차 가이드 열기</a>
        <a class="btn btn-outline" href="https://methodos-eight.vercel.app/app" target="_blank" rel="noopener">methodos</a>
        <a class="btn btn-outline" href="https://ai-research-os-web.vercel.app/dashboard" target="_blank" rel="noopener">StudiumR</a>
      </div>
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
  <a href="mission.html"><img src="../../assets/icons/target.svg" alt="" /> <span data-i18n="nav.mission">미션</span></a>
  <a href="contact.html"><img src="../../assets/icons/mail.svg" alt="" /> <span data-i18n="nav.contact">문의</span></a>
</aside>
</div></section>
""",
)

PAGES["pages/about/mission.html"] = (
    "미션",
    "../../",
    f"""
<section class="page-hero"><div class="container">
{crumbs([("홈", "../../index.html", "crumb.home"), ("소개", "lab.html", "nav.about"), ("미션", None, "nav.mission")])}
<h1 data-i18n="mission.h1">미션</h1>
<p data-i18n="mission.p">Methodos Lab의 목표는 연구자가 방법 선택에서 분석과 논문 작성에 이르기까지 연구 과정 전반을 끊김 없이 이어갈 수 있도록 지원하는 것입니다.</p>
</div></section>
<section class="content-block"><div class="container prose">
<ul>
  <li>연구방법의 절차를 소프트웨어로 표준화한다</li>
  <li>전문 분석(Desktop)과 AI Research(SaaS)를 연결한다</li>
  <li data-i18n="mission.li1">연구 데이터 활용의 자율성을 사용자에게 보장합니다</li>
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
    (ROOT / "index.html").write_text(
        page("홈", "", index_body, "Methodos Lab — 근거 기반 AI와 절차적 연구 솔루션", title_key="crumb.home"),
        encoding="utf-8",
    )
    for rel, (title, depth, body) in PAGES.items():
        path = ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(page(title, depth, body), encoding="utf-8")
    # README
    (ROOT / "README.md").write_text(
        """# Methodos Lab Homepage

Methodos Lab official homepage (static HTML). Supports Korean / English / 中文 via the KO·EN·ZH switcher.

## Live SaaS
- methodos: https://methodos-eight.vercel.app/
- StudiumR: https://ai-research-os-web.vercel.app/

## Open locally
Serve the folder root (e.g. `python -m http.server 8765`) and open `index.html`.

## Regenerate
```
python _generate_site.py
python _rebuild_guides.py
```
""",
        encoding="utf-8",
    )
    print("Generated", 1 + len(PAGES), "pages")


if __name__ == "__main__":
    main()

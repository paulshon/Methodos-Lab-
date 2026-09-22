# -*- coding: utf-8 -*-
"""Rebuild guide pages with Methodos Lab site chrome for continuous UX."""
from pathlib import Path

ROOT = Path(r"C:\Users\saran\OneDrive\Desktop\메스도스랩-홈페이지")
GUIDES = ROOT / "pages" / "learn" / "guides"
TEMPLATE = (ROOT / "pages" / "learn" / "guides.html").read_text(encoding="utf-8")

# Extract chrome from guides.html (learn-depth ../../) and deepen to ../../../
head_end = TEMPLATE.find("<main>")
foot_start = TEMPLATE.find("<footer")
chrome_top = (
    TEMPLATE[:head_end]
    .replace("../../", "../../../")
    .replace("사용자 가이드 · Methodos Lab", "{title} · Methodos Lab")
    .replace(
        'content="사용자 가이드 — Methodos Lab"',
        'content="{title} — Methodos Lab"',
    )
    .replace("<body>", '<body class="guide-shell">')
)
chrome_bottom = TEMPLATE[foot_start:].replace("../../", "../../../")


def switcher(active: str) -> str:
    items = [
        ("../guides.html", "전체", active == "index"),
        ("methodos-basic.html", "methodos-basic", active == "methodos-basic.html"),
        ("methodosQ.html", "methodosQ", active == "methodosQ.html"),
        ("methodosG.html", "methodosG", active == "methodosG.html"),
        ("methodos-studiumr.html", "methodos / StudiumR", active == "methodos-studiumr.html"),
    ]
    links = []
    for href, label, is_on in items:
        cls = "guide-tab is-active" if is_on else "guide-tab"
        links.append(f'<a class="{cls}" href="{href}">{label}</a>')
    return (
        '<nav class="guide-switcher" aria-label="가이드 전환">'
        + "".join(links)
        + "</nav>"
    )


def page(filename: str, title: str, eyebrow: str, lead: str, body: str) -> str:
    main = f"""
<main class="guide-main">
<section class="page-hero guide-hero"><div class="container">
<div class="breadcrumb"><a href="../../../index.html">홈</a><span>/</span><a href="../guides.html">사용자 가이드</a><span>/</span><span>{title}</span></div>
<p class="eyebrow">{eyebrow}</p>
<h1>{title}</h1>
<p>{lead}</p>
{switcher(filename)}
</div></section>
<section class="content-block guide-content"><div class="container guide-body">
{body}
</div></section>
</main>

"""
    return chrome_top.format(title=title) + main + chrome_bottom


PAGES = {}

PAGES["methodos-basic.html"] = page(
    "methodos-basic.html",
    "methodos-basic 가이드",
    "Desktop · 통계분석",
    "절차로 익히는 연구용 통계 — 소개와 절차 가이드입니다.",
    """
<figure class="guide-hero-media">
  <img src="methodos-thumb-ko.png" alt="Methodos Basic 소개" />
</figure>
<div class="info-card guide-lead-card">
  <h3>Methodos Basic LT-4</h3>
  <p>Methodos Basic은 분석을 도와주는 자동화 프로그램입니다. 결과만 넘기지 않고, 절차적 단계와 통계 이해를 함께 높이도록 만들었습니다. 예제·학습으로 개념을 익힌 뒤, 자료를 보고 변수를 배정하며 분석·그래프·결과까지 같은 흐름으로 진행합니다. 쉬운 주석 · 한·영·중 전환으로 해외 유학생도 함께 씁니다.</p>
</div>
<h2 class="guide-h2">인터랙티브 절차 가이드</h2>
<p class="guide-note">번호 + 메뉴 자막이 단계별로 이어지는 Framer Motion 절차입니다. 절차 A·B는 같은 앱 안에 있습니다.</p>
<div class="tutorial-cols">
  <div>
    <h4>절차 A · 예제를 통한 분석</h4>
    <p>01 자료 보기 → 02 포맷 받기 → 03 내 형식 변환 → 04 변수 칸 → 05 변수 선택 → 06 분석 → 07 그래프 → 08 결과</p>
  </div>
  <div>
    <h4>절차 B · 학습으로 쌓기</h4>
    <p>01 명칭 → 02 초급 → 03 중급 → 04 고급 → 05 예제 확인 → 06 작업대 적용</p>
  </div>
</div>
<h2 class="guide-h2">왼쪽 메뉴 · 요약 절차</h2>
<div class="card-list">
  <div class="info-card"><h3>홈</h3><p>단계 카드 확인 후 방법 정하기 / 통계 계산</p></div>
  <div class="info-card"><h3>통계방법 정하기·찾기·라이브러리</h3><p>목적→기법 연결, 예제 실행</p></div>
  <div class="info-card"><h3>예제 자료</h3><p>분류·설명 후 작업대에 올리기</p></div>
  <div class="info-card"><h3>작업대·통계 계산</h3><p>자료→변수 배정→실행</p></div>
  <div class="info-card"><h3>그래프·결과</h3><p>패턴과 해석 문장 대조</p></div>
  <div class="info-card"><h3>학습·설정</h3><p>명칭/초·중·고급, 언어(한·영·중)</p></div>
</div>
<div class="guide-callout">
  <p>핵심 한 줄: 예제 포맷을 받아 내 자료로 바꾼 뒤, 같은 메뉴 절차로 분석·그래프·결과를 읽습니다.</p>
</div>
<p class="tutorial-actions">
  <a class="btn btn-solid" href="methodos-basic-procedure/index.html">절차 가이드 열기</a>
  <a class="btn btn-outline" href="../tutorials.html">튜토리얼 · 실행방법</a>
  <a class="btn btn-outline" href="../../products/methodos-basic.html">제품 페이지</a>
</p>
""",
)

PAGES["methodosQ.html"] = page(
    "methodosQ.html",
    "methodosQ 가이드",
    "Desktop · Q방법론",
    "개념과 의미를 절차로 익히게 돕는 Q방법론 학습형 워크벤치입니다.",
    """
<div class="info-card guide-lead-card">
  <h3>한 줄 소개</h3>
  <p>methodosQ는 연구 초점부터 해석·보고까지 Q방법론 8단계를 화면에서 따라가며 배우는 데스크톱 프로그램입니다. 자동 결과가 아니라 왜 이 단계가 필요한지를 쉬운 설명과 주석으로 보여 주고, 한국어·영어 UI 전환으로 해외 유학생도 함께 학습할 수 있습니다.</p>
</div>
<div class="feature-grid guide-pillars">
  <article class="feature"><h3>01 · 절차 학습</h3><p>8단계·37세부 절차로 개념을 순서대로 체득</p></article>
  <article class="feature"><h3>02 · 쉬운 주석</h3><p>학술 용어 아래 쉬운 말·예시·개념사전 연결</p></article>
  <article class="feature"><h3>03 · 다국어</h3><p>한국어·English UI · 중문 가이드로 해외 유학생 지원</p></article>
</div>
<h2 class="guide-h2">핵심 흐름</h2>
<div class="info-card">
  <p>학습 → 예제 분석 → 포맷 변환 → 재분석. 예제 열기 → 포맷(CSV/Excel) 받기 → 내 자료로 바꿔 넣기 → 분석 다시 돌리기. 학습 트랙(입문·연구·논문·개념사전)을 번호 절차로 따라갑니다.</p>
</div>
<h2 class="guide-h2">앱 상단 메뉴</h2>
<div class="table-wrap">
<table class="compare">
  <tbody>
    <tr><th>파일</th><td>새/열기/저장 · CSV·Q자료 입출력 · 리포트·백업 · 끝내기</td></tr>
    <tr><th>편집</th><td>실행취소 · 다시실행 · 잘라내기/복사/붙여넣기</td></tr>
    <tr><th>보기</th><td>테마 · 언어(한국어/English) · 단축키 · 확대/축소</td></tr>
    <tr><th>절차</th><td>4단계 Gate · 연구 8단계(Ctrl+1~8)와 세부 절차</td></tr>
    <tr><th>학습</th><td>처음/연구중/논문대비 · 개념사전 · 예제 자료</td></tr>
    <tr><th>도움말</th><td>정보 · 계산 근거 고지 · 설정</td></tr>
  </tbody>
</table>
</div>
<h2 class="guide-h2">Q 연구 절차 · 단계</h2>
<div class="card-list">
  <div class="info-card"><h3>1 · 연구 초점</h3><p>주제 확정 → 연구질문 → 방법 적합성 → 포함/제외 → 초점 요약</p></div>
  <div class="info-card"><h3>2 · 의견장 (Concourse)</h3><p>수집 → 기록 → 정리 → 찬/반 균형 → 포화 → Q표본 후보</p></div>
  <div class="info-card"><h3>3 · Q표본 구성</h3><p>축소 기준 → 목표 진술 수 → 구조화 → 정제 → 파일럿 → 최종 연결</p></div>
  <div class="info-card"><h3>4–8 · 정렬·요인·해석</h3><p>P표본·정렬 → 요인추출 → 해석 → 보고까지 단계 워크플로</p></div>
</div>
<div class="guide-callout">
  <p>핵심 한 줄: 통계를 대신 눌러 주는 도구가 아니라, Q방법론을 절차로 익히게 돕는 학습형 워크벤치입니다.</p>
</div>
<p class="tutorial-actions">
  <a class="btn btn-outline" href="../../products/methodosQ.html">제품 페이지</a>
  <a class="btn btn-outline" href="../../download/desktop.html">다운로드 안내</a>
</p>
""",
)

PAGES["methodosG.html"] = page(
    "methodosG.html",
    "methodosG 가이드",
    "Desktop · 근거이론",
    "코딩에서 이론화까지 근거이론 절차를 Desktop 워크벤치로 표준화합니다.",
    """
<div class="info-card guide-lead-card">
  <h3>methodosG · 근거이론 분석</h3>
  <p>methodosG는 근거이론의 코딩·범주화·이론화 절차를 Desktop에서 따라가며 수행하는 분석 프로그램입니다. Setup.exe와 Portable.exe로 설치·실행하며, 질적 자료의 개방·축·선택 코딩 흐름과 메모·범주 관리를 한 워크벤치에서 지원합니다.</p>
</div>
<div class="tutorial-cols">
  <div>
    <h4>절차 A · 자료 → 코딩</h4>
    <p>01 자료 불러오기 → 02 개방 코딩 → 03 축 코딩 → 04 선택 코딩</p>
  </div>
  <div>
    <h4>절차 B · 이론화 → 보고</h4>
    <p>01 메모 → 02 범주 정리 → 03 이론 스케치 → 04 보고서 내보내기</p>
  </div>
</div>
<h2 class="guide-h2">배포물</h2>
<div class="card-list">
  <div class="info-card"><h3>MethodosG-v6-Setup.exe</h3><p>설치형</p></div>
  <div class="info-card"><h3>MethodosG-v6-portable.exe</h3><p>실행형</p></div>
  <div class="info-card"><h3>로컬 저장</h3><p>프로젝트·코딩 산출물을 PC에 보관</p></div>
</div>
<div class="guide-callout">
  <p>핵심 한 줄: 코딩에서 이론화까지 근거이론 절차를 Desktop 워크벤치로 표준화합니다.</p>
</div>
<p class="tutorial-actions">
  <a class="btn btn-outline" href="../../products/methodosG.html">제품 페이지</a>
  <a class="btn btn-outline" href="../../download/desktop.html">다운로드 안내</a>
</p>
""",
)

PAGES["methodos-studiumr.html"] = page(
    "methodos-studiumr.html",
    "methodos / StudiumR 가이드",
    "Cloud · AI Research",
    "연구방법 OS와 End-to-End AI Research 플랫폼을 브라우저에서 바로 시작합니다.",
    """
<div class="info-card guide-lead-card">
  <h3>SaaS 제품군</h3>
  <p>methodos는 절차적 단계 AI 연구방법 OS이고, StudiumR은 End-to-End AI Research 플랫폼입니다. 브라우저에서 바로 시작해 연구방법 선택부터 논문 생산까지 이어 줍니다.</p>
</div>
<div class="tutorial-cols">
  <div>
    <h4>methodos · 연구방법 OS</h4>
    <p>01 방법 추천 → 02 프로세스 → 03 워크벤치 → 04 검토·검증</p>
    <p style="margin-top:0.75rem"><a class="btn btn-solid" href="https://methodos-eight.vercel.app/" target="_blank" rel="noopener">methodos 열기</a></p>
  </div>
  <div>
    <h4>StudiumR · AI Research OS</h4>
    <p>01 트랙 선택 → 02 문헌·설계 → 03 작성 → 04 크리틱</p>
    <p style="margin-top:0.75rem"><a class="btn btn-solid" href="https://ai-research-os-web.vercel.app/" target="_blank" rel="noopener">StudiumR 열기</a></p>
  </div>
</div>
<h2 class="guide-h2">시작 요약</h2>
<div class="card-list">
  <div class="info-card"><h3>회원가입</h3><p>Google · GitHub · 이메일</p></div>
  <div class="info-card"><h3>StudiumR 트랙</h3><p>연구준비자(RDOS) / 연구자(AI-Research-OS)</p></div>
  <div class="info-card"><h3>보안</h3><p>연구 산출물 로컬 우선 · 메타데이터만 클라우드</p></div>
</div>
<div class="guide-callout">
  <p>핵심 한 줄: methodos로 방법을 절차화하고, StudiumR로 문헌·작성·검증까지 End-to-End로 이어 갑니다.</p>
</div>
<p class="tutorial-actions">
  <a class="btn btn-outline" href="../../products/methodos.html">methodos 제품</a>
  <a class="btn btn-outline" href="../../products/studiumr.html">StudiumR 제품</a>
</p>
""",
)


def main():
    for name, html in PAGES.items():
        (GUIDES / name).write_text(html, encoding="utf-8")
        print("wrote", name)


if __name__ == "__main__":
    main()

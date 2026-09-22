# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(r"C:\Users\saran\OneDrive\Desktop\메스도스랩-홈페이지\pages\learn\guides")


def page(folder, brand, kicker, title, pillars, paths, data, live_links=""):
    pillars_html = "".join(
        '<div class="hero__pillar"><span class="hero__pillar-n">{n}</span>'
        "<div><strong>{t}</strong><span>{s}</span></div></div>".format(**p)
        for p in pillars
    )
    paths_html = "".join(
        f'<a class="btn btn--ghost" href="#{hid}">{label}</a>' for hid, label in paths
    )
    data_js = "{\n  sections: " + json.dumps(data["sections"], ensure_ascii=False, indent=2) + "\n}"
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{brand} 절차 가이드 · Methodos Lab</title>
  <link rel="icon" href="../../../../assets/logo/methodos-lab-logo.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="../procedure-shared/procedure.css" />
</head>
<body>
  <div class="page">
    <header class="topbar">
      <div class="topbar__brand">
        <img src="../../../../assets/logo/methodos-lab-logo.svg" alt="" />
        <span>{brand}</span>
      </div>
      <a class="topbar__back" href="../../tutorials.html">← 튜토리얼</a>
    </header>
    <section class="hero">
      <div class="hero__copy">
        <p class="hero__kicker">{kicker}</p>
        <h1 class="hero__brand">{brand}</h1>
        <p class="hero__title">{title}</p>
        <div class="hero__cta">
          {paths_html}
          {live_links}
        </div>
      </div>
      <div class="hero__panel">{pillars_html}</div>
    </section>
    <div id="guide-root"></div>
    <p class="foot">© Methodos Lab</p>
  </div>
  <script src="../procedure-shared/procedure.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", function () {{
      MethodosProcedure.mount("#guide-root", {data_js});
    }});
  </script>
</body>
</html>
"""
    out = ROOT / folder / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("wrote", out)


page(
    "methodosQ-procedure",
    "methodosQ",
    "Desktop · Q방법론",
    "개념과 의미를 절차로 익히는 Q방법론 실행 가이드",
    [
        {"n": "01", "t": "절차 학습", "s": "8단계·세부 절차로 체득"},
        {"n": "02", "t": "쉬운 주석", "s": "용어 아래 쉬운 설명"},
        {"n": "03", "t": "다국어", "s": "한·영 UI"},
    ],
    [("analyze", "예제로 Q분석"), ("learn", "학습 트랙")],
    {
        "sections": [
            {
                "id": "analyze",
                "eyebrow": "핵심 절차 A",
                "title": "예제로 Q분석 따라가기",
                "sub": "예제 열기 → 포맷 받기 → 내 자료 변환 → 연구 8단계 → 해석·보고",
                "shotNote": "methodosQ 화면에서 클릭할 곳 · 번호 · 액션 자막을 따라가세요.",
                "play": "절차 재생",
                "pause": "일시정지",
                "replay": "처음부터",
                "menuLabel": "메뉴",
                "clickHint": "여기를 클릭",
                "railTitle": "methodosQ",
                "railItems": ["홈", "학습", "절차", "예제 자료", "파일", "도움말"],
                "steps": [
                    {"n": "01", "menu": "예제 자료 ▸ 예제 열기", "title": "예제 고르기", "action": "예제 자료에서 샘플 Q연구를 엽니다", "detail": "연구 초점·의견장·표본 구조가 채워진 예제로 시작합니다.", "chips": ["예제", "Q연구"], "x": 28, "y": 42},
                    {"n": "02", "menu": "파일 ▸ 포맷 받기", "title": "포맷 받기", "action": "CSV·Excel 포맷을 내려받습니다", "detail": "예제와 같은 열 구조로 내 자료를 맞출 준비가 됩니다.", "chips": ["CSV", "Excel"], "x": 72, "y": 22},
                    {"n": "03", "menu": "파일 ▸ 자료 넣기", "title": "내 자료 변환", "action": "포맷에 맞춰 내 자료를 넣고 다시 불러옵니다", "detail": "진술문·P표본·정렬 자료를 같은 절차로 연결합니다.", "chips": ["변환", "불러오기"], "x": 68, "y": 48},
                    {"n": "04", "menu": "절차 ▸ 1~3", "title": "초점·의견장·Q표본", "action": "연구 초점 → 의견장 → Q표본을 순서대로 확정합니다", "detail": "8단계 중 앞 3단계로 연구 설계를 고정합니다.", "chips": ["초점", "Concourse", "Q표본"], "x": 40, "y": 55},
                    {"n": "05", "menu": "절차 ▸ 4~5", "title": "P표본·정렬", "action": "P표본을 구성하고 Q정렬을 진행합니다", "detail": "정렬 보드에서 동의·비동의 분포를 만듭니다.", "chips": ["P표본", "Q-sort"], "x": 58, "y": 50},
                    {"n": "06", "menu": "절차 ▸ 6", "title": "요인 추출", "action": "요인추출·회전을 실행합니다", "detail": "요인 수·설명력을 확인하며 해석 후보를 고릅니다.", "chips": ["요인", "회전"], "x": 62, "y": 58},
                    {"n": "07", "menu": "절차 ▸ 7~8", "title": "해석·보고", "action": "요인 해석과 보고서 초안을 작성합니다", "detail": "쉬운 주석과 함께 해석 문장을 정리합니다.", "chips": ["해석", "보고"], "x": 48, "y": 62},
                    {"n": "08", "menu": "파일 ▸ 저장", "title": "저장·내보내기", "action": "프로젝트와 리포트를 저장합니다", "detail": "같은 절차를 다른 자료에도 반복합니다.", "chips": ["저장", "리포트"], "x": 18, "y": 18},
                ],
            },
            {
                "id": "learn",
                "eyebrow": "핵심 절차 B",
                "title": "학습 트랙으로 개념 익히기",
                "sub": "입문 → 연구중 → 논문대비 → 개념사전 → 예제 확인",
                "shotNote": "학습 메뉴의 번호 절차를 따라 개념을 쌓습니다.",
                "play": "절차 재생",
                "pause": "일시정지",
                "replay": "처음부터",
                "menuLabel": "메뉴",
                "clickHint": "여기를 클릭",
                "railTitle": "학습",
                "railItems": ["처음", "연구중", "논문대비", "개념사전", "예제"],
                "steps": [
                    {"n": "01", "menu": "학습 ▸ 처음", "title": "입문 트랙", "action": "「처음」트랙을 엽니다", "detail": "Q방법론 기초 용어와 전체 흐름을 익힙니다.", "chips": ["입문"], "x": 30, "y": 28},
                    {"n": "02", "menu": "학습 ▸ 연구중", "title": "연구중 트랙", "action": "「연구중」트랙을 따라갑니다", "detail": "설계·표집·정렬 실무 포인트를 확인합니다.", "chips": ["연구중"], "x": 42, "y": 28},
                    {"n": "03", "menu": "학습 ▸ 논문대비", "title": "논문대비", "action": "「논문대비」트랙을 엽니다", "detail": "해석·보고·한계 서술 체크리스트를 봅니다.", "chips": ["논문"], "x": 54, "y": 28},
                    {"n": "04", "menu": "학습 ▸ 개념사전", "title": "개념사전", "action": "개념사전에서 용어를 검색합니다", "detail": "학술 용어 아래 쉬운 설명을 함께 읽습니다.", "chips": ["사전"], "x": 66, "y": 28},
                    {"n": "05", "menu": "예제 자료", "title": "예제로 확인", "action": "예제 자료로 학습 내용을 바로 검증합니다", "detail": "학습 → 예제 → 내 자료 순으로 이어갑니다.", "chips": ["예제"], "x": 36, "y": 55},
                ],
            },
        ]
    },
)

page(
    "methodosG-procedure",
    "methodosG",
    "Desktop · 근거이론",
    "코딩에서 이론화까지 근거이론 실행 가이드",
    [
        {"n": "01", "t": "코딩", "s": "개방·축·선택"},
        {"n": "02", "t": "메모", "s": "해석을 기록"},
        {"n": "03", "t": "보고", "s": "근거와 함께 내보내기"},
    ],
    [("coding", "자료 → 코딩"), ("theory", "이론화 → 보고")],
    {
        "sections": [
            {
                "id": "coding",
                "eyebrow": "핵심 절차 A",
                "title": "자료 → 코딩",
                "sub": "자료 불러오기 → 개방 코딩 → 축 코딩 → 선택 코딩",
                "shotNote": "methodosG Desktop 워크벤치의 코딩 절차를 따라가세요.",
                "play": "절차 재생",
                "pause": "일시정지",
                "replay": "처음부터",
                "menuLabel": "메뉴",
                "clickHint": "여기를 클릭",
                "railTitle": "methodosG",
                "railItems": ["홈", "자료", "개방코딩", "축코딩", "선택코딩", "메모"],
                "steps": [
                    {"n": "01", "menu": "자료 ▸ 불러오기", "title": "자료 불러오기", "action": "인터뷰·관찰 문서를 프로젝트에 올립니다", "detail": "텍스트 단위로 분절해 코딩 준비를 합니다.", "chips": ["자료"], "x": 32, "y": 40},
                    {"n": "02", "menu": "개방코딩", "title": "개방 코딩", "action": "의미 단위에 개방 코드를 부착합니다", "detail": "가능한 한 현장에 가까운 라벨로 시작합니다.", "chips": ["개방"], "x": 48, "y": 48},
                    {"n": "03", "menu": "축코딩", "title": "축 코딩", "action": "코드 간 관계로 축을 잡습니다", "detail": "조건·행위·결과 축으로 범주를 묶습니다.", "chips": ["축"], "x": 58, "y": 52},
                    {"n": "04", "menu": "선택코딩", "title": "선택 코딩", "action": "핵심 범주를 선택해 이론 뼈대를 만듭니다", "detail": "이야기선을 한 줄로 요약합니다.", "chips": ["선택"], "x": 62, "y": 56},
                    {"n": "05", "menu": "메모", "title": "코딩 메모", "action": "코딩 중 떠오른 해석을 메모합니다", "detail": "메모가 이론화의 재료가 됩니다.", "chips": ["메모"], "x": 70, "y": 36},
                    {"n": "06", "menu": "홈 ▸ 진행 확인", "title": "진행 점검", "action": "코딩 진행률과 미처리 구간을 확인합니다", "detail": "빠진 구간을 보완한 뒤 이론화로 넘어갑니다.", "chips": ["점검"], "x": 24, "y": 28},
                ],
            },
            {
                "id": "theory",
                "eyebrow": "핵심 절차 B",
                "title": "이론화 → 보고",
                "sub": "메모 → 범주 정리 → 이론 스케치 → 보고서 내보내기",
                "shotNote": "이론화와 보고 산출물까지 같은 워크벤치에서 이어집니다.",
                "play": "절차 재생",
                "pause": "일시정지",
                "replay": "처음부터",
                "menuLabel": "메뉴",
                "clickHint": "여기를 클릭",
                "railTitle": "이론화",
                "railItems": ["메모", "범주", "이론", "보고서", "내보내기"],
                "steps": [
                    {"n": "01", "menu": "메모 ▸ 정리", "title": "메모 묶기", "action": "코딩 메모를 주제별로 묶습니다", "detail": "중복·충돌 메모를 정리합니다.", "chips": ["메모"], "x": 35, "y": 40},
                    {"n": "02", "menu": "범주", "title": "범주 정리", "action": "축·선택 코딩 범주를 정제합니다", "detail": "정의·속성·차원을 표로 맞춥니다.", "chips": ["범주"], "x": 50, "y": 45},
                    {"n": "03", "menu": "이론 스케치", "title": "이론 스케치", "action": "핵심 범주와 관계를 도식화합니다", "detail": "근거이론의 이야기선을 스케치합니다.", "chips": ["이론"], "x": 58, "y": 52},
                    {"n": "04", "menu": "보고서", "title": "보고서 초안", "action": "결과·근거 인용을 보고서로 옮깁니다", "detail": "코딩 근거와 해석을 함께 배치합니다.", "chips": ["보고"], "x": 64, "y": 48},
                    {"n": "05", "menu": "내보내기", "title": "내보내기", "action": "보고서·코딩표를 내보냅니다", "detail": "로컬에 프로젝트와 산출물을 보관합니다.", "chips": ["내보내기"], "x": 72, "y": 30},
                ],
            },
        ]
    },
)

page(
    "methodos-studiumr-procedure",
    "methodos / StudiumR",
    "Cloud · AI Research",
    "연구방법 OS와 End-to-End AI Research 실행 가이드",
    [
        {"n": "01", "t": "methodos", "s": "방법 추천·워크벤치"},
        {"n": "02", "t": "StudiumR", "s": "트랙·작성·크리틱"},
        {"n": "03", "t": "Cloud", "s": "브라우저에서 바로"},
    ],
    [("methodos", "methodos"), ("studiumr", "StudiumR")],
    {
        "sections": [
            {
                "id": "methodos",
                "eyebrow": "핵심 절차 A",
                "title": "methodos · 방법 추천 → 워크벤치",
                "sub": "열기 → 로그인 → 방법 추천 → 프로세스 → 워크벤치 → 검토·검증",
                "shotNote": "실제 Cloud 화면 캡처와 번호 핀을 따라가세요.",
                "play": "절차 재생",
                "pause": "일시정지",
                "replay": "처음부터",
                "menuLabel": "화면",
                "clickHint": "여기를 클릭",
                "railTitle": "methodos",
                "railItems": ["홈", "추천", "프로세스", "워크벤치", "검토"],
                "steps": [
                    {"n": "01", "menu": "methodos 홈", "title": "methodos 열기", "action": "브라우저에서 methodos를 엽니다", "detail": "https://methodos-eight.vercel.app/ 로 시작합니다.", "shot": "./shots/a01-methodos.png", "chips": ["열기"], "x": 50, "y": 42},
                    {"n": "02", "menu": "/app", "title": "워크스페이스 진입", "action": "앱 화면으로 이동합니다", "detail": "로그인 후 연구방법 OS 워크스페이스에 들어갑니다.", "shot": "./shots/a02-methodos-app.png", "chips": ["진입"], "x": 50, "y": 48},
                    {"n": "03", "menu": "방법 추천", "title": "방법 추천", "action": "연구 질문에 맞는 방법을 추천받습니다", "detail": "목적·자료 유형을 입력하면 후보 방법이 제시됩니다.", "chips": ["추천"], "x": 40, "y": 45},
                    {"n": "04", "menu": "프로세스", "title": "프로세스 확인", "action": "추천 방법의 절차 카드를 확인합니다", "detail": "단계별 산출물과 체크포인트를 봅니다.", "chips": ["프로세스"], "x": 55, "y": 50},
                    {"n": "05", "menu": "워크벤치", "title": "워크벤치 작업", "action": "워크벤치에서 단계 작업을 진행합니다", "detail": "가이드 질문에 답하며 산출물을 채웁니다.", "chips": ["워크벤치"], "x": 60, "y": 52},
                    {"n": "06", "menu": "검토·검증", "title": "검토·검증", "action": "검토·검증 단계로 결과의 타당성을 점검합니다", "detail": "누락·비약을 고친 뒤 다음 단계로 넘깁니다.", "chips": ["검토"], "x": 65, "y": 55},
                ],
            },
            {
                "id": "studiumr",
                "eyebrow": "핵심 절차 B",
                "title": "StudiumR · 대시보드 → 트랙",
                "sub": "대시보드 → 로그인 → 트랙 선택 → 문헌·설계 → 작성 → 크리틱",
                "shotNote": "AI Research OS 대시보드 흐름을 번호로 따라갑니다.",
                "play": "절차 재생",
                "pause": "일시정지",
                "replay": "처음부터",
                "menuLabel": "화면",
                "clickHint": "여기를 클릭",
                "railTitle": "StudiumR",
                "railItems": ["대시보드", "트랙", "문헌", "작성", "크리틱"],
                "steps": [
                    {"n": "01", "menu": "StudiumR 홈", "title": "StudiumR 열기", "action": "StudiumR 사이트에 접속합니다", "detail": "https://ai-research-os-web.vercel.app/ 로 시작합니다.", "shot": "./shots/b01-studiumr.png", "chips": ["열기"], "x": 50, "y": 40},
                    {"n": "02", "menu": "/dashboard", "title": "대시보드·로그인", "action": "대시보드에서 로그인합니다", "detail": "Google·GitHub·이메일로 진입합니다.", "shot": "./shots/b02-dashboard.png", "chips": ["로그인"], "x": 50, "y": 52},
                    {"n": "03", "menu": "트랙 선택", "title": "트랙 선택", "action": "연구준비자 또는 연구자 트랙을 고릅니다", "detail": "RDOS / AI-Research-OS 목적에 맞게 선택합니다.", "chips": ["트랙"], "x": 42, "y": 48},
                    {"n": "04", "menu": "문헌·설계", "title": "문헌·설계", "action": "문헌 탐색과 연구설계를 진행합니다", "detail": "주제·질문·설계 초안을 워크스페이스에 쌓습니다.", "chips": ["문헌", "설계"], "x": 55, "y": 50},
                    {"n": "05", "menu": "작성", "title": "작성", "action": "원고·산출물 작성을 이어갑니다", "detail": "섹션별로 초안을 채우고 근거를 연결합니다.", "chips": ["작성"], "x": 60, "y": 52},
                    {"n": "06", "menu": "크리틱", "title": "크리틱", "action": "크리틱으로 논리·근거를 점검합니다", "detail": "피드백을 반영해 End-to-End 연구를 마무리합니다.", "chips": ["크리틱"], "x": 65, "y": 55},
                ],
            },
        ]
    },
    live_links=(
        '<a class="btn btn--primary" href="https://methodos-eight.vercel.app/app" target="_blank" rel="noopener">methodos 열기</a>'
        '<a class="btn btn--ghost" href="https://ai-research-os-web.vercel.app/dashboard" target="_blank" rel="noopener">StudiumR</a>'
    ),
)

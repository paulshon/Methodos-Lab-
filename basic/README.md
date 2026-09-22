# Methodos Basic — Framer Motion 핵심 절차 패키지

## 포함
- `guide/` — 바로 실행되는 빌드본 (핵심 절차 A·B)
- `email/` — 소개 HTML + 섬네일 (KO/EN/ZH)
- `source/guide-landing/` — 수정·재빌드용 전체 소스 (src, public, package.json 등)

## 미리보기
`미리보기.bat` 실행 → http://127.0.0.1:5180/

또는:
```
cd guide
npx --yes serve -l 5180 .
```

## 소스에서 다시 빌드
```
cd source\guide-landing
npm install
npm run build
# dist 내용을 ..\..\guide 로 복사
```

## 핵심 절차
- A: 예제를 통한 분석
- B: 학습으로 통계 익히기

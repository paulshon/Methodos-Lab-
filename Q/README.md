# methodosQ 절차 가이드 (Framer Motion 소스)

홈페이지 게시용 **methodosQ** 튜토리얼 소스입니다.  
basic의 `guide-landing`과 동일한 구조(`ProcedureShowcase.jsx` + `copy.js` + Framer Motion)입니다.

## 구성

- `src/ProcedureShowcase.jsx` — 번호 핀·말풍선·재생 절차 UI
- `src/copy.js` — 한·영·중 절차 문구 (실제 methodosQ v6 왼쪽 메뉴 기준)
- `public/shots/` — methodosQ Desktop 실창 캡처 + 단계별 핫스팟
- `public/shots/hotspots.json` — 클릭 좌표

## 실행

```bash
cd Q
npm install
npm run dev
```

미리보기: http://127.0.0.1:5181/

## 빌드 (홈페이지 배포용)

```bash
npm run build
```

산출물: `Q/dist/` → 사이트 `pages/learn/guides/methodosQ-procedure/` 등으로 복사해 게시합니다.

## 원본 앱

`methodosQ-v6.exe` (Desktop)를 열어 Q 연구 절차 메뉴를 시현한 뒤 캡처를 `public/shots/`에 반영했습니다.

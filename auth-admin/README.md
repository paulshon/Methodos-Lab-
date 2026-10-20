# Methodos Lab — 회원 · 인증키 서버 (`auth-admin`)

메스도스랩 홈페이지(이 저장소 루트의 정적 사이트)에 붙는 **회원 서버**다. Next.js + Clerk + Supabase.

```
메스도스랩-홈페이지/            ← GitHub: paulshon/Methodos-Lab-
├─ index.html, pages/, js/ …   정적 홈페이지 (상단에 로그인·회원가입 버튼이 붙는다)
└─ auth-admin/                 이 폴더 — 회원가입·로그인(Clerk), 내 계정, 관리자(인증키 발급), 앱용 라이선스 API
```

## 역할 분담 (중요)
| | 어디서 | 누가 |
|---|---|---|
| **회원가입 · 로그인 · 내 인증키 보기** | **메스도스랩 홈페이지** (`pages/member/`, `js/member.js`) | 방문자·회원 |
| **가입자 확인 · 인증키 발급 · 연장 · 해지** | **이 서버의 `/admin`** | **관리자만** (Clerk 로그인 + `ADMIN_EMAILS`) |

둘이 **같은 Clerk 앱**을 쓰기 때문에, 홈페이지에서 가입한 사람이 곧바로 이 서버의 회원 목록에 나타난다(`/admin` 의 「회원」 탭, 인증키 대기).
관리자 계정도 Clerk 사용자이므로 **홈페이지에서 한 번 가입**해 두고, 그 이메일을 `ADMIN_EMAILS` 에 적는다.

## 한 줄 흐름
1. 방문자가 홈페이지에서 **회원가입**(Clerk, 이메일 인증) → 2. 관리자가 이 서버 `/admin` 의 **회원** 탭에서 확인하고 기간을 골라 **인증키 발급** →
3. 회원이 홈페이지 **내 계정**에서 키를 보고(홈페이지가 Clerk 토큰을 `Authorization: Bearer` 로 `/api/my-keys` 에 보낸다) → 4. 데스크톱 앱에 입력해 PC 를 활성화.

| 주소 | 누가 | 용도 |
|---|---|---|
| `/login` | 관리자 | Clerk 로그인(허용 목록에 있어야 `/admin` 이 열린다). `/` 는 `/admin` 으로 간다 |
| `/admin` | **관리자만** | 탭 ①회원(가입자 목록·인증키 대기·발급) ②인증키(전체 내역·연장·해지·PC 해제·직접 발급) |
| `/api/activate` 외 | 데스크톱 앱 | 활성화·갱신·해지·오프라인 (`/offline` 페이지 포함) |
| `/api/my-keys` | 홈페이지의 로그인 회원 | **본인에게 발급된 키만**. CORS 는 `NEXT_PUBLIC_HOMEPAGE_URL`·`ALLOWED_ORIGINS` 출처에만 |
| `/api/me` | 이 서버 상단 | 관리자 로그인 표시 |
| `/api/download/<id>` | 누구나 | GitHub Release 로 302 이동 |

회원과 키의 연결: 키 기록에 `memberId`(Clerk 사용자 ID)·`memberEmail` 이 들어간다. 이메일은 클라이언트가 보낸 값이 아니라
서버가 Clerk 에서 다시 읽어 적고, **이메일 인증이 끝나지 않은 회원에게는 발급을 거부**한다(409).

## 처음 설정 (한 번)
1. **Clerk** (https://dashboard.clerk.com): 앱 생성 → *Email address* 를 가입 식별자로 켜고 인증 코드 필수. API Keys 의
   `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`·`CLERK_SECRET_KEY` 를 환경변수로.
   배포 뒤 Clerk 의 **Domains / Allowed origins** 에 이 서버의 주소를 등록.
2. **Supabase**: SQL editor 에서 `supabase/license_keys.sql`(그리고 선택으로 `download_events.sql`) 실행 →
   `NEXT_PUBLIC_SUPABASE_URL`·`NEXT_PUBLIC_SUPABASE_ANON_KEY`·`SUPABASE_SERVICE_ROLE_KEY`.
3. **서명 키**: `LICENSE_PRIVATE_KEY`(앱에 구운 공개키와 한 쌍), `LICENSE_ADMIN_TOKEN`(길고 무작위로).
4. **관리자**: `ADMIN_EMAILS=내이메일` — 먼저 **홈페이지에서** 그 이메일로 회원가입해 두면(이 서버에는 가입 화면이 없다) `/admin` 이 열린다. `NEXT_PUBLIC_HOMEPAGE_URL` 도 꼭 넣는다(CORS).
5. Vercel 에 배포(Root Directory = `auth-admin`). `https://<배포주소>/api/license-health` 가
   `store: "supabase"`, `signingKey: true`, `adminToken: true` 인지 본다.
6. **홈페이지 연결**: 홈페이지의 `js/member.js` 맨 위 `CONFIG` 에 `clerkPublishableKey`(같은 Clerk 앱의 pk_…, 공개해도 되는 값)와 `authBase`(이 서버 주소)를 적고 푸시한다. 상단에 로그인·회원가입 버튼이 나타난다.
7. **앱 연결**: 앱이 부르는 서버 주소를 바꾼다 — 설치된 앱의 `resources/license-server.json` 의 `url` 을 고치거나,
   새로 빌드할 때 `LICENSE_SERVER_URL=https://<배포주소> node build-lt4-all.cjs`.
8. **배포 파일**: GitHub `paulshon/Methodos-Lab-` 의 Releases 에 태그 `v22.20.1-authv1` 로 `MethodosBasic-LT-4-all-v4-R20-Learn-AuthV1.exe` 와 `…-Setup.exe` 를 올린다.

## 로컬 실행
```bash
cp .env.example .env.local     # 값 채우기
npm install
npm run dev                    # http://localhost:3000  (127.0.0.1 말고 localhost 로 연다 — Clerk 프록시가 localhost 로 간다)
```
정적 홈페이지는 저장소 루트에서 `python -m http.server 8765` 후
`http://localhost:8765/pages/member/index.html?mode=signup&clerkPk=pk_test_…&authBase=http://localhost:3000` 을 한 번 열면 두 값이 그 브라우저에 기억된다(빈 값으로 지운다).

### Clerk 키 없이 실제 가입·로그인 시연
`.env.local` 에 `NEXT_PUBLIC_CLERK_KEYLESS=1` 만 넣고 `npm run dev` → Clerk 가 임시 개발 인스턴스를 만들어 준다(개발 전용).
`NEXT_PUBLIC_CLERK_KEYLESS=1` 에서는 서버 라우트가 Bearer 토큰을 못 읽는 한계가 있으므로, 홈페이지↔서버 연동을 시험할 때는 `.clerk/.tmp/keyless.json` 의 pk·sk 를 일반 환경변수(`NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`·`CLERK_SECRET_KEY`)로 넣어 쓴다. 이메일을 `이름+clerk_test@example.com` 꼴로 가입하면 인증 코드는 항상 `424242` 다. 관리자로 쓸 계정은
`ADMIN_EMAILS` 에 같은 이메일을 적는다.

## 검증
```bash
npm run test:admin   # 관리자 판정 단위 시험
npm run verify       # 타입검사 + 운영빌드 + (Clerk 없이) 회원→발급→앱 활성화→좌석 제한→해지 API 흐름 + GitHub 배포처
```

자세한 라이선스 규칙·CLI 는 `LICENSE-SERVER.md`.

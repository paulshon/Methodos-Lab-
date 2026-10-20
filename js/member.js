// 메스도스랩 홈페이지 회원 기능 — Clerk 로 회원가입·로그인, 상단 버튼, 내 계정(인증키 조회).
//
// 두 값만 채우면 된다 (둘 다 공개해도 되는 값이다).
//   clerkPublishableKey : Clerk 대시보드 → API keys 의 Publishable key (pk_test_… / pk_live_…)
//                         관리자 서버(auth-admin)와 **같은 Clerk 앱**의 키여야 가입자가 관리자 화면에 나타난다.
//   authBase            : 관리자 서버 주소(예: https://methodos-lab-q11s.vercel.app) — 내 인증키 조회용
// 개발 중에는 주소창에 ?clerkPk=pk_test_…&authBase=http://localhost:3100 을 한 번 붙이면 이 브라우저에 기억된다(빈 값으로 지운다).
(() => {
  const CONFIG = {
    clerkPublishableKey: "",
    authBase: "https://methodos-lab-q11s.vercel.app",
  };

  const store = {
    get: (k) => { try { return localStorage.getItem(k); } catch (_) { return null; } },
    set: (k, v) => { try { v ? localStorage.setItem(k, v) : localStorage.removeItem(k); } catch (_) {} },
  };
  const qs = new URLSearchParams(location.search);
  for (const [q, k] of [["clerkPk", "methodos-clerk-pk"], ["authBase", "methodos-auth-base"]]) {
    if (qs.has(q)) store.set(k, qs.get(q));
  }
  const PK = (store.get("methodos-clerk-pk") || CONFIG.clerkPublishableKey || "").trim();
  const AUTH_BASE = (store.get("methodos-auth-base") || CONFIG.authBase || "").trim().replace(/\/+$/, "");

  const ROOT = new URL("../", document.currentScript ? document.currentScript.src : location.href).href;
  const MEMBER_URL = (mode) => `${ROOT}pages/member/index.html?mode=${mode}`;
  const RELEASE = "https://github.com/paulshon/Methodos-Lab-/releases/download/v22.20.1-authv1/";
  const FILES = {
    setup: "MethodosBasic-LT-4-all-v4-R20-Learn-AuthV1-Setup.exe",
    portable: "MethodosBasic-LT-4-all-v4-R20-Learn-AuthV1.exe",
  };

  const T = {
    ko: {
      login: "로그인", signup: "회원가입", account: "내 계정", logout: "로그아웃",
      needLogin: "로그인이 필요합니다.", loading: "불러오는 중…",
      myKeys: "내 인증키",
      none: "가입이 접수되었습니다. 관리자가 확인하면 인증키가 이곳에 나타납니다.",
      copy: "키 복사", copied: "복사됨", active: "사용 가능", revoked: "해지됨",
      term: "기간", expires: "만료", pcs: "사용 중인 PC",
      dl: "프로그램 내려받기", dlSetup: "설치형 다운로드", dlPortable: "포터블 다운로드",
      dlNote: "설치한 뒤 처음 실행하면 인증키 창이 뜹니다. 위 인증키를 붙여 넣으세요.",
      noServer: "인증키 서버 주소가 설정되지 않았습니다.", fail: "인증키를 불러오지 못했습니다.",
      noClerk: "회원 기능이 아직 설정되지 않았습니다.",
      mo: "개월", yr: "년",
    },
    en: {
      login: "Log in", signup: "Sign up", account: "My account", logout: "Log out",
      needLogin: "Please log in.", loading: "Loading…",
      myKeys: "My license keys",
      none: "Your sign-up has been received. Your key will appear here once the administrator issues it.",
      copy: "Copy key", copied: "Copied", active: "Active", revoked: "Revoked",
      term: "Term", expires: "Expires", pcs: "PCs in use",
      dl: "Download", dlSetup: "Download installer", dlPortable: "Download portable",
      dlNote: "An activation-key window appears on first launch. Paste your key above.",
      noServer: "The license server address is not configured.", fail: "Could not load your keys.",
      noClerk: "Member features are not configured yet.",
      mo: " mo", yr: " yr",
    },
    zh: {
      login: "登录", signup: "注册", account: "我的账户", logout: "退出",
      needLogin: "请先登录。", loading: "加载中…",
      myKeys: "我的授权密钥",
      none: "已收到您的注册。管理员发放密钥后将显示在此处。",
      copy: "复制密钥", copied: "已复制", active: "可用", revoked: "已撤销",
      term: "期限", expires: "到期", pcs: "已使用的电脑",
      dl: "下载程序", dlSetup: "下载安装版", dlPortable: "下载便携版",
      dlNote: "首次运行会弹出授权密钥窗口，请粘贴上面的密钥。",
      noServer: "未配置授权服务器地址。", fail: "无法加载密钥。",
      noClerk: "会员功能尚未配置。",
      mo: "个月", yr: "年",
    },
  };
  const loc = () => { const l = store.get("methodos-lab-locale") || "ko"; return T[l] ? l : "ko"; };
  const tr = (k) => T[loc()][k];
  const termLabel = (m) => (m == null ? "" : m % 12 === 0 ? `${m / 12}${tr("yr")}` : `${m}${tr("mo")}`);

  function el(tag, attrs, ...kids) {
    const e = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs || {})) {
      if (k === "class") e.className = v;
      else if (k.startsWith("on")) e.addEventListener(k.slice(2), v);
      else e.setAttribute(k, v);
    }
    for (const kid of kids) e.append(kid);
    return e;
  }

  // ── 상단 버튼 ──────────────────────────────────────────────────────────────
  const desk = el("div", { class: "auth-links" });
  const mob = el("div", { class: "auth-links auth-links--mobile" });
  function mount() {
    const cta = document.querySelector(".nav-inner .nav-cta");
    const toggle = document.querySelector(".nav-toggle");
    if (cta && cta.parentElement) cta.parentElement.insertBefore(desk, cta);
    else if (toggle && toggle.parentElement) toggle.parentElement.insertBefore(desk, toggle);
    const box = document.querySelector(".mobile-panel .mobile-cta") || document.querySelector(".mobile-panel");
    if (box) box.prepend(mob);
  }
  function renderButtons(user, clerk) {
    for (const box of [desk, mob]) {
      box.replaceChildren();
      if (user) {
        box.append(el("a", { class: "auth-link", href: MEMBER_URL("account") }, tr("account")));
        box.append(el("button", {
          class: "auth-link auth-link--admin", type: "button",
          onclick: async () => { await clerk.signOut(); location.href = ROOT + "index.html"; },
        }, tr("logout")));
      } else {
        box.append(el("a", { class: "auth-link", href: MEMBER_URL("login") }, tr("login")));
        box.append(el("a", { class: "auth-link auth-link--solid", href: MEMBER_URL("signup") }, tr("signup")));
      }
    }
  }

  // ── Clerk 불러오기 ─────────────────────────────────────────────────────────
  function frontendApi(pk) {
    try {
      const raw = atob(pk.split("_").slice(2).join("_"));
      return raw.replace(/\$$/, "");
    } catch (_) { return ""; }
  }
  function loadClerk() {
    return new Promise((resolve, reject) => {
      if (!PK) return reject(new Error("no-pk"));
      const fapi = frontendApi(PK);
      if (!fapi) return reject(new Error("bad-pk"));
      const s = document.createElement("script");
      s.async = true;
      s.crossOrigin = "anonymous";
      s.setAttribute("data-clerk-publishable-key", PK);
      s.src = `https://${fapi}/npm/@clerk/clerk-js@5/dist/clerk.browser.js`;
      s.onload = async () => {
        try { await window.Clerk.load(); resolve(window.Clerk); } catch (e) { reject(e); }
      };
      s.onerror = () => reject(new Error("clerk-js load failed"));
      document.head.appendChild(s);
    });
  }

  // ── 회원 페이지 (pages/member/index.html) ─────────────────────────────────
  async function renderMemberPage(clerk) {
    const root = document.getElementById("member-root");
    if (!root) return;
    const mode = qs.get("mode") || "account";
    root.replaceChildren();

    if (!clerk) {
      root.append(el("p", {}, tr("noClerk")));
      return;
    }
    if (mode === "signup" || mode === "login") {
      if (clerk.user) { location.replace(MEMBER_URL("account")); return; }
      const holder = el("div", { class: "member-clerk" });
      root.append(holder);
      const common = { routing: "virtual", forceRedirectUrl: MEMBER_URL("account"), fallbackRedirectUrl: MEMBER_URL("account") };
      if (mode === "signup") clerk.mountSignUp(holder, { ...common, signInUrl: MEMBER_URL("login") });
      else clerk.mountSignIn(holder, { ...common, signUpUrl: MEMBER_URL("signup") });
      return;
    }

    // 내 계정
    if (!clerk.user) {
      root.append(el("p", {}, tr("needLogin")), el("p", {},
        el("a", { class: "btn btn-solid", href: MEMBER_URL("login") }, tr("login")), " ",
        el("a", { class: "btn btn-outline", href: MEMBER_URL("signup") }, tr("signup"))));
      return;
    }
    const email = clerk.user.primaryEmailAddress ? clerk.user.primaryEmailAddress.emailAddress : "";
    root.append(el("p", { class: "member-email" }, email));
    const keysBox = el("div", { class: "member-keys" }, tr("loading"));
    root.append(el("h2", {}, tr("myKeys")), keysBox);
    root.append(
      el("h2", {}, tr("dl")),
      el("p", { class: "member-dl" },
        el("a", { class: "btn btn-solid", href: RELEASE + FILES.setup, rel: "noopener" }, tr("dlSetup")), " ",
        el("a", { class: "btn btn-outline", href: RELEASE + FILES.portable, rel: "noopener" }, tr("dlPortable"))),
      el("p", { class: "member-note" }, tr("dlNote")),
    );

    if (!AUTH_BASE) { keysBox.textContent = tr("noServer"); return; }
    try {
      const token = await clerk.session.getToken();
      const res = await fetch(`${AUTH_BASE}/api/my-keys`, { headers: { authorization: `Bearer ${token}` }, cache: "no-store" });
      const json = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(json.message || String(res.status));
      keysBox.replaceChildren();
      if (!json.keys.length) { keysBox.append(el("p", { class: "member-empty" }, tr("none"))); return; }
      for (const k of json.keys) {
        const copyBtn = el("button", { class: "btn btn-outline", type: "button" }, tr("copy"));
        copyBtn.addEventListener("click", () => {
          (navigator.clipboard ? navigator.clipboard.writeText(k.key) : Promise.reject()).then(() => {
            copyBtn.textContent = tr("copied");
            setTimeout(() => (copyBtn.textContent = tr("copy")), 1500);
          }).catch(() => {});
        });
        keysBox.append(el("div", { class: "member-key" },
          el("code", { "data-testid": "my-key" }, k.key), " ", copyBtn,
          el("span", { class: `member-badge ${k.status === "active" ? "ok" : "bad"}` }, k.status === "active" ? tr("active") : tr("revoked")),
          el("div", { class: "member-meta" },
            `${termLabel(k.termMonths) ? `${tr("term")} ${termLabel(k.termMonths)} · ` : ""}${tr("expires")}: ${k.expires} · ${tr("pcs")} ${k.devices.length}/${k.maxDevices}`),
        ));
      }
    } catch (e) {
      keysBox.textContent = `${tr("fail")} (${e.message})`;
    }
  }

  // ── 시작 ───────────────────────────────────────────────────────────────────
  mount();
  if (!PK) {
    // Clerk 가 없으면: 관리자 서버 주소만 있을 때는 그쪽 로그인·가입 화면으로 보낸다. 둘 다 없으면 버튼을 숨긴다.
    if (AUTH_BASE) {
      for (const box of [desk, mob]) {
        box.append(el("a", { class: "auth-link", href: `${AUTH_BASE}/login` }, tr("login")),
          el("a", { class: "auth-link auth-link--solid", href: `${AUTH_BASE}/signup` }, tr("signup")));
      }
    }
    renderMemberPage(null);
    return;
  }
  renderButtons(null);
  loadClerk()
    .then((clerk) => {
      renderButtons(clerk.user, clerk);
      clerk.addListener(({ user }) => renderButtons(user, clerk));
      return renderMemberPage(clerk);
    })
    .catch(() => renderMemberPage(null));
  // 언어 전환 시 버튼 글자 갱신
  document.querySelectorAll(".lang-switch__btn").forEach((b) =>
    b.addEventListener("click", () => setTimeout(() => window.Clerk && renderButtons(window.Clerk.user, window.Clerk), 50)));
})();

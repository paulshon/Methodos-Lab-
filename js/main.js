(() => {
  const header = document.querySelector(".site-header");
  const toggle = document.querySelector(".nav-toggle");
  const mobile = document.querySelector(".mobile-panel");
  const body = document.body;

  const onScroll = () => {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 8);
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  if (toggle && mobile) {
    toggle.addEventListener("click", () => {
      const open = mobile.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      body.style.overflow = open ? "hidden" : "";
      const icon = toggle.querySelector("img");
      if (icon) {
        const depth = toggle.dataset.iconDepth || "";
        icon.src = open
          ? `${depth}assets/icons/x.svg`
          : `${depth}assets/icons/menu.svg`;
        icon.alt = open ? "닫기" : "메뉴";
      }
    });
  }

  document.querySelectorAll(".mobile-group > button").forEach((btn) => {
    btn.addEventListener("click", () => {
      btn.parentElement.classList.toggle("is-open");
    });
  });

  // Desktop: click toggle for touch devices
  document.querySelectorAll(".nav-item > .nav-link[aria-haspopup='true']").forEach((link) => {
    link.addEventListener("click", (e) => {
      if (window.matchMedia("(hover: none)").matches) {
        e.preventDefault();
        const item = link.parentElement;
        const open = item.classList.toggle("is-open");
        document.querySelectorAll(".nav-item").forEach((other) => {
          if (other !== item) other.classList.remove("is-open");
        });
        link.setAttribute("aria-expanded", open ? "true" : "false");
      }
    });
  });

  document.addEventListener("click", (e) => {
    if (!e.target.closest(".nav-item")) {
      document.querySelectorAll(".nav-item.is-open").forEach((el) => el.classList.remove("is-open"));
    }
  });

  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.14, rootMargin: "0px 0px -40px 0px" }
  );
  document.querySelectorAll(".reveal").forEach((el) => io.observe(el));
})();

// ── 회원(Clerk) 로그인·회원가입 버튼 ─────────────────────────────────────────
// 회원 서버(auth-admin)의 주소. 배포 뒤 이 한 줄만 채우면 모든 페이지 상단에 버튼이 나타난다.
//   예: const AUTH_BASE_DEFAULT = "https://회원서버-주소";
// 개발 중에는 주소창에 ?authBase=http://localhost:3100 을 한 번 붙이면 이 브라우저에 기억된다(?authBase= 로 지운다).
(() => {
  const AUTH_BASE_DEFAULT = "";
  let base = AUTH_BASE_DEFAULT;
  try {
    const q = new URLSearchParams(location.search).get("authBase");
    if (q !== null) { q ? localStorage.setItem("methodos-auth-base", q) : localStorage.removeItem("methodos-auth-base"); }
    base = localStorage.getItem("methodos-auth-base") || base;
  } catch (_) {}
  base = String(base || "").replace(/\/+$/, "");
  if (!/^https?:\/\//.test(base)) return;

  const LABELS = {
    ko: ["로그인", "회원가입", "내 계정", "관리자", "로그아웃"],
    en: ["Log in", "Sign up", "My account", "Admin", "Log out"],
    zh: ["登录", "注册", "我的账户", "管理", "退出"],
  };
  const keys = ["auth.login", "auth.signup", "auth.account", "auth.admin", "auth.logout"];
  let loc = "ko";
  try { loc = localStorage.getItem("methodos-lab-locale") || "ko"; } catch (_) {}
  const L = LABELS[loc] || LABELS.ko;

  const mk = (i, href, cls) => {
    const a = document.createElement("a");
    a.href = href;
    a.className = cls;
    a.dataset.i18n = keys[i];
    a.textContent = L[i];
    return a;
  };

  const desk = document.createElement("div");
  desk.className = "auth-links";
  const mob = document.createElement("div");
  mob.className = "auth-links auth-links--mobile";

  function render(me) {
    for (const box of [desk, mob]) {
      box.replaceChildren();
      if (me && me.signedIn) {
        box.append(mk(2, base + "/account", "auth-link"));
        if (me.isAdmin) box.append(mk(3, base + "/admin", "auth-link auth-link--admin"));
      } else {
        box.append(mk(0, base + "/login", "auth-link"), mk(1, base + "/signup", "auth-link auth-link--solid"));
      }
    }
  }
  render(null);

  const toggle = document.querySelector(".nav-toggle");
  const cta = document.querySelector(".nav-inner .nav-cta");
  if (cta && cta.parentElement) cta.parentElement.insertBefore(desk, cta);
  else if (toggle && toggle.parentElement) toggle.parentElement.insertBefore(desk, toggle);
  const mobileBox = document.querySelector(".mobile-panel .mobile-cta") || document.querySelector(".mobile-panel");
  if (mobileBox) mobileBox.prepend(mob);

  // 회원 서버와 같은 주소(같은 도메인)에서 열렸을 때만 로그인 상태를 알 수 있다(쿠키가 같은 출처라서).
  if (new URL(base).origin === location.origin) {
    fetch(base + "/api/me", { cache: "no-store", credentials: "same-origin" })
      .then((r) => r.json())
      .then(render)
      .catch(() => {});
  }
})();

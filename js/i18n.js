(() => {
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

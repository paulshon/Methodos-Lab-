import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { LOCALES, copy } from "./copy.js";
import ProcedureShowcase from "./ProcedureShowcase.jsx";
import "./App.css";

const LOCALE_KEY = "methodos-guide-locale";

function readInitialLocale() {
  try {
    const saved = localStorage.getItem(LOCALE_KEY);
    if (saved && copy[saved]) return saved;
  } catch {
    /* ignore */
  }
  return "ko";
}

export default function App() {
  const [locale, setLocale] = useState(readInitialLocale);
  const [hotspots, setHotspots] = useState(null);
  const t = copy[locale] || copy.ko;

  useEffect(() => {
    let cancelled = false;
    fetch("./shots/hotspots.json")
      .then((r) => (r.ok ? r.json() : null))
      .then((data) => {
        if (!cancelled && data) setHotspots(data);
      })
      .catch(() => {});
    return () => {
      cancelled = true;
    };
  }, []);

  useEffect(() => {
    document.documentElement.lang = locale === "zh" ? "zh-CN" : locale;
    document.title = `${t.brand} — ${t.heroTitle}`;
    try {
      localStorage.setItem(LOCALE_KEY, locale);
    } catch {
      /* ignore */
    }
  }, [locale, t.brand, t.heroTitle]);

  const switchLocale = (id) => {
    if (!copy[id] || id === locale) return;
    setLocale(id);
  };

  return (
    <div className="page" data-locale={locale}>
      <header className="topbar">
        <div className="topbar__brand">
          <span className="topbar__mark" />
          {t.brand}
        </div>
        <nav className="topbar__lang" aria-label="Language">
          {LOCALES.map((l) => (
            <button
              key={l.id}
              type="button"
              className={`topbar__lang-btn${locale === l.id ? " is-on" : ""}`}
              aria-pressed={locale === l.id}
              onClick={() => switchLocale(l.id)}
            >
              {l.label}
            </button>
          ))}
        </nav>
      </header>

      <div key={locale} className="page__locale">
        <section className="hero">
          <motion.div
            className="hero__copy"
            initial={{ opacity: 0, y: 24 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7, ease: [0.22, 1, 0.36, 1] }}
          >
            <p className="hero__kicker">{t.kicker}</p>
            <h1 className="hero__brand">{t.brand}</h1>
            <p className="hero__title">{t.heroTitle}</p>
            <div className="hero__cta">
              <a className="btn btn--primary" href="#analyze">
                {t.ctaAnalyze}
              </a>
              <a className="btn btn--ghost" href="#learn">
                {t.ctaLearn}
              </a>
            </div>
          </motion.div>

          <motion.div
            className="hero__visual"
            initial={{ opacity: 0, scale: 0.96 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.12, duration: 0.75, ease: [0.22, 1, 0.36, 1] }}
          >
            <div className="hero__panel">
              {t.pillars.map((p, i) => (
                <motion.div
                  key={p.title}
                  className="hero__pillar"
                  initial={{ opacity: 0, x: 16 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: 0.3 + i * 0.1 }}
                >
                  <span className="hero__pillar-n">0{i + 1}</span>
                  <div>
                    <strong>{p.title}</strong>
                    <span>{p.text}</span>
                  </div>
                </motion.div>
              ))}
            </div>
          </motion.div>
        </section>

        <section className="intro" id="intro">
          <h2 className="intro__title">{t.introTitle}</h2>
          <div className="intro__body">
            {t.introBody.map((para) => (
              <p key={para.slice(0, 24)}>{para}</p>
            ))}
          </div>
        </section>

        <ProcedureShowcase
          id="analyze"
          accent="#2f8f88"
          eyebrow={t.analyzeSection.eyebrow}
          title={t.analyzeSection.title}
          sub={t.analyzeSection.sub}
          steps={t.analyzeSteps}
          menuLabel={t.analyzeSection.menuLabel}
          playLabel={t.analyzeSection.play}
          pauseLabel={t.analyzeSection.pause}
          replayLabel={t.analyzeSection.replay}
          shotNote={t.shotNote}
          clickHint={t.clickHint}
          hotspots={hotspots}
          locale={locale}
        />

        <ProcedureShowcase
          id="learn"
          accent="#1f5c72"
          eyebrow={t.learnSection.eyebrow}
          title={t.learnSection.title}
          sub={t.learnSection.sub}
          steps={t.learnSteps}
          menuLabel={t.learnSection.menuLabel}
          playLabel={t.learnSection.play}
          pauseLabel={t.learnSection.pause}
          replayLabel={t.learnSection.replay}
          shotNote={t.shotNote}
          clickHint={t.clickHint}
          hotspots={hotspots}
          locale={locale}
        />

        <footer className="foot">
          <p>{t.footer}</p>
        </footer>
      </div>
    </div>
  );
}

import { useEffect, useMemo, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";

const STEP_MS = 4200;

/** Locale-aware relative shot URLs: ./shots/{ko|en|zh}/file.png */
function shotUrl(shot, locale = "ko") {
  if (!shot) return "";
  const loc = locale === "en" || locale === "zh" ? locale : "ko";
  const file = String(shot).replace(/^.*\//, "");
  if (!file) return "";
  return `./shots/${loc}/${file}`;
}

function bubblePos(bubble, x, y) {
  // 핀(번호)과 겹치지 않도록 충분히 떨어뜨린다
  if (bubble === "left") {
    return {
      right: `${Math.min(100 - x + 8, 68)}%`,
      top: `${Math.min(Math.max(y, 14), 72)}%`,
      transform: "translateY(-50%)",
    };
  }
  if (bubble === "top") {
    return {
      left: `${x}%`,
      bottom: `${Math.min(100 - y + 10, 72)}%`,
      transform: "translateX(-50%)",
    };
  }
  if (bubble === "bottom") {
    return {
      left: `${Math.min(Math.max(x, 18), 72)}%`,
      top: `${Math.min(y + 12, 70)}%`,
      transform: "translateX(-50%)",
    };
  }
  return {
    left: `${Math.min(x + 8, 54)}%`,
    top: `${Math.min(Math.max(y, 14), 72)}%`,
    transform: "translateY(-50%)",
  };
}

function DropletRipples() {
  return (
    <span className="droplet" aria-hidden="true">
      <span className="droplet__ring droplet__ring--1" />
      <span className="droplet__ring droplet__ring--2" />
      <span className="droplet__ring droplet__ring--3" />
      <motion.span
        className="droplet__drop"
        animate={{ y: [-18, 0], opacity: [0, 1, 0], scale: [0.6, 1, 0.4] }}
        transition={{ duration: 0.9, repeat: Infinity, ease: "easeIn", repeatDelay: 0.35 }}
      />
      <span className="droplet__splash" />
    </span>
  );
}

function ClickHotspot({ step, accent, clickHint, menuLabel }) {
  const x = Number(step.x) || 50;
  const y = Number(step.y) || 50;
  const w = Math.max(Number(step.w) || 6, 4);
  const h = Math.max(Number(step.h) || 4, 3);
  const bubble = step.bubble || "right";

  return (
    <div className="hotspot" aria-live="polite">
      {/* 클릭 대상 하이라이트 */}
      <div
        className="hotspot__focus"
        style={{
          left: `${x}%`,
          top: `${y}%`,
          width: `${Math.max(w + 2.8, 8)}%`,
          height: `${Math.max(h + 2.4, 5.5)}%`,
        }}
      />

      {/* 자막 카드 — 하단 바는 삭제(중복). 번호는 핀에만 */}
      <motion.aside
        className={`hotspot__bubble hotspot__bubble--${bubble}`}
        style={bubblePos(bubble, x, y)}
        initial={{ opacity: 0, y: 12, scale: 0.96 }}
        animate={{ opacity: 1, y: 0, scale: 1 }}
        exit={{ opacity: 0 }}
        transition={{ delay: 0.1, duration: 0.35 }}
      >
        <p className="hotspot__click-hint">{clickHint}</p>
        <p className="hotspot__action">{step.action}</p>
        <p className="hotspot__menu">
          <span>{menuLabel}</span>
          {step.menu}
        </p>
        <p className="hotspot__detail">{step.detail}</p>
      </motion.aside>

      {/* 번호 핀 — 말풍선보다 앞에 (z-index) */}
      <motion.div
        className="hotspot__pin"
        style={{ left: `${x}%`, top: `${y}%` }}
        initial={{ scale: 0.5, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        transition={{ type: "spring", stiffness: 360, damping: 18 }}
      >
        <DropletRipples />
        <div className="hotspot__badge" title={`단계 ${step.n}`}>
          <span className="hotspot__badge-num">{step.n}</span>
        </div>
        <motion.div
          className="hotspot__cursor"
          animate={{ x: [10, 2, 2], y: [10, 2, 4], scale: [1, 1, 0.88, 1] }}
          transition={{ duration: 1.25, repeat: Infinity, ease: "easeInOut", times: [0, 0.45, 0.55, 1] }}
        >
          <svg width="32" height="32" viewBox="0 0 28 28" fill="none">
            <path
              d="M6 4.5L10.2 22.2l3.1-5.4 6.8 5.1L22.5 6.8 6 4.5z"
              fill="#111"
              stroke="#fff"
              strokeWidth="2"
              strokeLinejoin="round"
            />
          </svg>
        </motion.div>
      </motion.div>
    </div>
  );
}

export default function ProcedureShowcase({
  id,
  accent,
  eyebrow,
  title,
  sub,
  steps,
  menuLabel,
  playLabel,
  pauseLabel,
  replayLabel,
  shotNote,
  clickHint,
  hotspots,
  locale = "ko",
}) {
  const [active, setActive] = useState(0);
  const [playing, setPlaying] = useState(true);

  const merged = useMemo(
    () =>
      steps.map((s) => {
        const key = String(s.shot || "")
          .replace(/^\.\//, "")
          .replace(/^\/shots\//, "shots/")
          .replace(/^shots\//, "")
          .replace(/\.png$/, "");
        const hs = hotspots?.[key] || hotspots?.[String(s.shot || "").replace(/^.*\//, "").replace(/\.png$/, "")];
        if (!hs) return s;
        return {
          ...s,
          x: hs.x ?? s.x,
          y: hs.y ?? s.y,
          w: hs.w ?? s.w,
          h: hs.h ?? s.h,
          bubble: hs.bubble || s.bubble || "right",
        };
      }),
    [steps, hotspots],
  );

  useEffect(() => {
    if (!playing) return undefined;
    const timer = setTimeout(() => {
      setActive((i) => (i + 1) % merged.length);
    }, STEP_MS);
    return () => clearTimeout(timer);
  }, [playing, active, merged.length]);

  useEffect(() => {
    setActive(0);
  }, [id, steps]);

  const step = merged[active] || merged[0];

  return (
    <section id={id} className="proc">
      <div className="proc__head">
        <p className="proc__eyebrow" style={{ color: accent }}>
          {eyebrow}
        </p>
        <h2 className="proc__title">{title}</h2>
        <p className="proc__sub">{sub}</p>
        {shotNote ? <p className="proc__shot-note">{shotNote}</p> : null}
        <div className="proc__controls">
          <button type="button" className="proc__btn" onClick={() => setPlaying((p) => !p)}>
            {playing ? pauseLabel : playLabel}
          </button>
          <button
            type="button"
            className="proc__btn proc__btn--ghost"
            onClick={() => {
              setActive(0);
              setPlaying(true);
            }}
          >
            {replayLabel}
          </button>
        </div>
      </div>

      <div className="proc__stage">
        <div className="proc__rail" aria-hidden="true">
          <motion.div
            className="proc__rail-fill"
            style={{ background: accent }}
            animate={{ width: `${((active + 1) / merged.length) * 100}%` }}
            transition={{ duration: 0.45, ease: [0.22, 1, 0.36, 1] }}
          />
        </div>

        <div className="proc__numbers">
          {merged.map((s, i) => (
            <button
              key={s.n}
              type="button"
              className={`proc__num${i === active ? " is-active" : ""}${i < active ? " is-done" : ""}`}
              style={i === active ? { borderColor: accent, color: accent } : undefined}
              onClick={() => {
                setActive(i);
                setPlaying(false);
              }}
              aria-current={i === active ? "step" : undefined}
            >
              {s.n}
            </button>
          ))}
        </div>

        <div className="proc__theater">
          <AnimatePresence mode="wait">
            <motion.div
              key={`${locale}-${step.n}-${step.shot}`}
              className="proc__screen"
              initial={{ opacity: 0.35 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.3 }}
            >
              <img className="proc__shot" src={shotUrl(step.shot, locale)} alt={`${step.n} ${step.menu}`} draggable={false} />
              <ClickHotspot step={step} accent={accent} clickHint={clickHint} menuLabel={menuLabel} />
            </motion.div>
          </AnimatePresence>
        </div>

        <ol className="proc__ticks">
          {merged.map((s, i) => (
            <li key={s.n}>
              <button
                type="button"
                className={`proc__tick${i === active ? " is-active" : ""}`}
                style={i === active ? { borderColor: accent } : undefined}
                onClick={() => {
                  setActive(i);
                  setPlaying(false);
                }}
              >
                <strong style={i === active ? { color: accent } : undefined}>{s.n}</strong>
                <span>{s.action}</span>
              </button>
            </li>
          ))}
        </ol>
      </div>
    </section>
  );
}

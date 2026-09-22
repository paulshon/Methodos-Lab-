/** Procedure player — mirrors methodos-basic Framer Motion showcase UX */
(function () {
  const STEP_MS = 4200;

  function el(tag, cls, html) {
    const n = document.createElement(tag);
    if (cls) n.className = cls;
    if (html != null) n.innerHTML = html;
    return n;
  }

  function mountSection(container, section) {
    const steps = section.steps || [];
    let idx = 0;
    let playing = true;
    let timer = null;

    const proc = el("section", "proc");
    proc.id = section.id || "";
    const head = el("div", "proc__head");
    head.append(el("p", "proc__eyebrow", section.eyebrow || ""));
    head.append(el("h2", "proc__title", section.title || ""));
    head.append(el("p", "proc__sub", section.sub || ""));
    head.append(el("p", "proc__shot-note", section.shotNote || "번호 핀과 액션 자막을 따라가세요."));
    const controls = el("div", "proc__controls");
    const btnPlay = el("button", "proc__btn", section.play || "절차 재생");
    const btnReplay = el("button", "proc__btn proc__btn--ghost", section.replay || "처음부터");
    controls.append(btnPlay, btnReplay);
    head.append(controls);
    const rail = el("div", "proc__rail");
    const fill = el("div", "proc__rail-fill");
    rail.append(fill);
    const nums = el("div", "proc__numbers");
    head.append(rail, nums);

    const main = el("div", "proc__main");
    const theater = el("div", "proc__theater");
    const screen = el("div", "proc__screen");
    theater.append(screen);
    const ticks = el("ul", "proc__ticks");
    main.append(theater, ticks);
    proc.append(head, main);
    container.append(proc);

    steps.forEach((s, i) => {
      const b = el("button", "proc__num", s.n);
      b.type = "button";
      b.addEventListener("click", () => {
        idx = i;
        render();
        if (playing) schedule();
      });
      nums.append(b);

      const t = el("li", "");
      const btn = el("button", "proc__tick");
      btn.type = "button";
      btn.innerHTML = `<strong>${s.n}</strong><span><strong>${s.title}</strong><br/>${s.action}</span>`;
      btn.addEventListener("click", () => {
        idx = i;
        render();
        if (playing) schedule();
      });
      t.append(btn);
      ticks.append(t);
    });

    function clearTimer() {
      if (timer) {
        clearTimeout(timer);
        timer = null;
      }
    }

    function schedule() {
      clearTimer();
      if (!playing || !steps.length) return;
      timer = setTimeout(() => {
        idx = (idx + 1) % steps.length;
        render();
        schedule();
      }, STEP_MS);
    }

    function render() {
      const step = steps[idx];
      if (!step) return;
      fill.style.width = ((idx + 1) / steps.length) * 100 + "%";
      [...nums.children].forEach((b, i) => {
        b.classList.toggle("is-active", i === idx);
        b.classList.toggle("is-done", i < idx);
      });
      [...ticks.children].forEach((li, i) => {
        li.firstChild.classList.toggle("is-active", i === idx);
      });
      btnPlay.textContent = playing ? section.pause || "일시정지" : section.play || "절차 재생";

      screen.innerHTML = "";
      if (step.shot) {
        const img = el("img", "proc__shot");
        img.src = step.shot;
        img.alt = step.title;
        screen.append(img);
      } else {
        const mock = el("div", "proc__mock");
        const railM = el("div", "proc__mock-rail");
        railM.append(el("strong", "", section.railTitle || section.title || "메뉴"));
        (section.railItems || []).forEach((name, i) => {
          railM.append(el("span", i === idx % Math.max(section.railItems.length, 1) ? "is-on" : "", name));
        });
        const mainM = el("div", "proc__mock-main");
        mainM.append(el("h3", "", step.title));
        mainM.append(el("p", "", step.detail));
        const chips = el("div", "proc__mock-chips");
        (step.chips || [step.menu]).forEach((c) => chips.append(el("i", "", c)));
        mainM.append(chips);
        mock.append(railM, mainM);
        screen.append(mock);
      }

      const hotspot = el("div", "hotspot");
      const x = Number(step.x) || 55;
      const y = Number(step.y) || 45;
      const focus = el("div", "hotspot__focus");
      focus.style.left = x + "%";
      focus.style.top = y + "%";
      const pin = el("div", "hotspot__pin");
      pin.style.left = x + "%";
      pin.style.top = y + "%";
      pin.innerHTML =
        `<span class="droplet" aria-hidden="true"><span class="droplet__ring"></span><span class="droplet__ring droplet__ring--2"></span><span class="droplet__ring droplet__ring--3"></span></span>` +
        `<div class="hotspot__badge">${step.n}</div>` +
        `<div class="hotspot__cursor"><svg width="28" height="28" viewBox="0 0 28 28" fill="none"><path d="M6 4.5L10.2 22.2l3.1-5.4 6.8 5.1L22.5 6.8 6 4.5z" fill="#111" stroke="#fff" stroke-width="2" stroke-linejoin="round"/></svg></div>`;
      const bubble = el("aside", "hotspot__bubble");
      const bx = Math.min(x + 10, 58);
      const by = Math.min(Math.max(y - 6, 10), 62);
      bubble.style.left = bx + "%";
      bubble.style.top = by + "%";
      bubble.innerHTML =
        `<p class="hotspot__click-hint">${section.clickHint || "여기를 클릭"}</p>` +
        `<p class="hotspot__action">${step.action}</p>` +
        `<p class="hotspot__menu"><span>${section.menuLabel || "메뉴"}</span>${step.menu}</p>` +
        `<p class="hotspot__detail">${step.detail}</p>`;
      hotspot.append(focus, pin, bubble);
      screen.append(hotspot);
    }

    btnPlay.addEventListener("click", () => {
      playing = !playing;
      render();
      if (playing) schedule();
      else clearTimer();
    });
    btnReplay.addEventListener("click", () => {
      idx = 0;
      playing = true;
      render();
      schedule();
    });

    render();
    schedule();
  }

  window.MethodosProcedure = {
    mount(sel, data) {
      const root = typeof sel === "string" ? document.querySelector(sel) : sel;
      if (!root) return;
      root.innerHTML = "";
      (data.sections || []).forEach((s) => mountSection(root, s));
    },
  };
})();

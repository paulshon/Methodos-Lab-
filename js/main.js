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

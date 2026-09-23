# -*- coding: utf-8 -*-
"""Bridge site locale <-> Framer procedure guide locale."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent

BRIDGE = """<!-- methodos-locale-bridge -->
<script>
(function () {
  try {
    var lab = localStorage.getItem("methodos-lab-locale");
    if (lab === "ko" || lab === "en" || lab === "zh") {
      localStorage.setItem("methodos-guide-locale", lab);
    }
    var _set = Storage.prototype.setItem;
    Storage.prototype.setItem = function (k, v) {
      _set.call(this, k, v);
      if (k === "methodos-guide-locale" && (v === "ko" || v === "en" || v === "zh")) {
        _set.call(this, "methodos-lab-locale", v);
      }
    };
  } catch (e) {}
})();
</script>
"""


def main() -> None:
    n = 0
    for p in ROOT.rglob("index.html"):
        s = p.as_posix()
        if not any(x in s for x in ("-procedure", "/Q/", "/G/", "/basic/guide", "/basic/source/guide")):
            continue
        t = p.read_text(encoding="utf-8", errors="ignore")
        if 'id="root"' not in t and "id='root'" not in t:
            continue
        if "methodos-locale-bridge" in t:
            continue
        if "<head>" in t:
            t2 = t.replace("<head>", "<head>\n" + BRIDGE, 1)
        else:
            t2 = BRIDGE + t
        p.write_text(t2, encoding="utf-8")
        print("bridged", p.relative_to(ROOT).as_posix())
        n += 1
    print("total", n)


if __name__ == "__main__":
    main()

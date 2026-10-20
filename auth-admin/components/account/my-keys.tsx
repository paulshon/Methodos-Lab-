"use client";

import { useEffect, useState } from "react";
import { termLabel } from "@/lib/product";

type MyKey = {
  key: string;
  issuedTo: string;
  expires: string;
  termMonths: number | null;
  status: "active" | "revoked";
  maxDevices: number;
  devices: { fp: string; hostname: string; lastSeen: string }[];
  createdAt: string;
};

export function MyKeys() {
  const [keys, setKeys] = useState<MyKey[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [copied, setCopied] = useState("");

  useEffect(() => {
    fetch("/api/my-keys", { cache: "no-store" })
      .then(async (r) => {
        const j = await r.json();
        if (!r.ok) throw new Error(j.message || "불러오지 못했습니다.");
        setKeys(j.keys);
      })
      .catch((e) => setError((e as Error).message));
  }, []);

  const copy = (k: string) => navigator.clipboard?.writeText(k).then(() => { setCopied(k); setTimeout(() => setCopied(""), 1500); });

  return (
    <section className="mt-6 rounded-2xl border border-line bg-white p-5" aria-live="polite">
      <h2 className="font-bold text-ink">내 인증키</h2>
      {error && <p role="alert" className="mt-3 text-sm text-red-700">{error}</p>}
      {!error && keys === null && <p className="mt-3 text-sm text-ink-3">불러오는 중…</p>}
      {keys && keys.length === 0 && (
        <p data-testid="no-keys" className="mt-3 rounded-xl bg-wash px-4 py-4 text-sm leading-relaxed text-ink-2">
          아직 발급된 인증키가 없습니다. 가입이 접수되었으며, 관리자가 확인하면 이 곳에 인증키가 나타납니다.
        </p>
      )}
      <ul className="mt-3 space-y-3">
        {keys?.map((k) => (
          <li key={k.key} className="rounded-xl border border-line p-4">
            <div className="flex flex-wrap items-center gap-3">
              <code data-testid="my-key" className="select-all rounded-lg bg-wash px-3 py-2 font-mono text-base tracking-wider text-ink">{k.key}</code>
              <button onClick={() => copy(k.key)} className="rounded-full bg-brand px-3 py-1 text-xs font-semibold text-white hover:bg-brand-dark">
                {copied === k.key ? "복사됨" : "키 복사"}
              </button>
              <span className={`rounded-full px-2.5 py-0.5 text-[11px] font-semibold ${k.status === "active" ? "bg-brand-wash text-brand" : "bg-red-50 text-red-700"}`}>
                {k.status === "active" ? "사용 가능" : "해지됨"}
              </span>
            </div>
            <p className="mt-2 text-xs text-ink-2">
              {termLabel(k.termMonths) && <>기간 {termLabel(k.termMonths)} · </>}
              만료: {k.expires} · 사용 중인 PC {k.devices.length}/{k.maxDevices}대
              {k.devices.length > 0 && <> ({k.devices.map((d) => d.hostname || "이름 없음").join(", ")})</>}
            </p>
          </li>
        ))}
      </ul>
    </section>
  );
}

"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import { TERMS, termLabel } from "@/lib/product";

type Device = { fp: string; hostname: string; activatedAt: string; lastSeen: string };
type KeyRow = {
  key: string;
  issuedTo: string;
  edition: string;
  expires: string;
  termMonths: number | null;
  status: "active" | "revoked";
  maxDevices: number;
  note: string;
  createdAt: string;
  memberId: string | null;
  memberEmail: string | null;
  devices: Device[];
};
type MemberRow = {
  id: string;
  email: string;
  emailVerified: boolean;
  name: string;
  createdAt: string;
  lastSignInAt: string | null;
  keys: { key: string; status: "active" | "revoked"; expires: string; termMonths: number | null; devices: number; maxDevices: number }[];
};
type Tab = "members" | "keys";

/**
 * 인증키 관리 화면.
 * mode="session": Clerk 로그인 세션으로 인증 (운영). 같은 사이트 화면임을 알리는 x-admin-ui 헤더를 붙인다.
 * mode="token":   입력한 관리자 토큰으로 인증 (개발 미리보기 전용 — 운영 빌드에서는 이 모드로 열리지 않는다).
 */
export function AdminPanel({ mode, who }: { mode: "session" | "token"; who?: string }) {
  const [token, setToken] = useState("");
  const [rows, setRows] = useState<KeyRow[]>([]);
  const [members, setMembers] = useState<MemberRow[]>([]);
  const [tab, setTab] = useState<Tab>("members");
  const [mFilter, setMFilter] = useState<"all" | "none" | "has">("none");
  const [mQuery, setMQuery] = useState("");
  const [issuing, setIssuing] = useState<string | null>(null); // 발급 폼이 열린 회원 id
  const [issue, setIssue] = useState({ months: 1, maxDevices: 1, note: "" });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [notice, setNotice] = useState<string | null>(null);
  const [query, setQuery] = useState("");
  const [created, setCreated] = useState<KeyRow | null>(null);
  const [form, setForm] = useState({ issuedTo: "", months: 1, maxDevices: 1, note: "" });
  const [busy, setBusy] = useState(false);

  const headers = useMemo(() => {
    const h: Record<string, string> = { "content-type": "application/json" };
    if (mode === "session") h["x-admin-ui"] = "1";
    else h["x-admin-token"] = token;
    return h;
  }, [mode, token]);

  const call = useCallback(
    async (method: "GET" | "POST", path: string, body?: unknown) => {
      const res = await fetch(path, { method, headers, body: body ? JSON.stringify(body) : undefined });
      const json = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(json.message || json.error || `오류 ${res.status}`);
      return json;
    },
    [headers],
  );

  const load = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const json = await call("GET", "/admin/keys");
      setRows(json.keys as KeyRow[]);
      try {
        const m = await call("GET", "/admin/members");
        setMembers(m.members as MemberRow[]);
      } catch (e) {
        // 회원 목록(Clerk)만 실패해도 인증키 화면은 쓸 수 있어야 한다.
        setMembers([]);
        setError(`회원 목록을 읽지 못했습니다: ${(e as Error).message}`);
      }
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setLoading(false);
    }
  }, [call]);

  useEffect(() => {
    if (mode === "session" || token) void load();
  }, [mode, token, load]);

  async function act(fn: () => Promise<unknown>, ok: string) {
    setBusy(true);
    setError(null);
    setNotice(null);
    try {
      await fn();
      setNotice(ok);
      await load();
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setBusy(false);
    }
  }

  async function issueToMember(m: MemberRow) {
    setBusy(true);
    setError(null);
    setNotice(null);
    setCreated(null);
    try {
      const row = (await call("POST", "/admin/keys", {
        memberId: m.id,
        months: issue.months,
        maxDevices: issue.maxDevices,
        note: issue.note,
      })) as KeyRow;
      setCreated(row);
      setIssuing(null);
      setIssue({ months: 1, maxDevices: 1, note: "" });
      setNotice(`${m.email} 님에게 ${termLabel(row.termMonths)} 인증키를 발급했습니다. 회원이 「내 계정」에서 바로 볼 수 있습니다.`);
      await load();
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setBusy(false);
    }
  }

  async function create() {
    setBusy(true);
    setError(null);
    setNotice(null);
    setCreated(null);
    try {
      const row = (await call("POST", "/admin/keys", {
        issuedTo: form.issuedTo,
        months: form.months,
        maxDevices: form.maxDevices,
        note: form.note,
      })) as KeyRow;
      setCreated(row);
      setForm({ ...form, issuedTo: "", note: "" });
      await load();
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setBusy(false);
    }
  }

  const copy = (text: string) => navigator.clipboard?.writeText(text).then(() => setNotice("복사했습니다."));

  const weekAgo = Date.now() - 7 * 86400_000;
  const shownMembers = members.filter((m) => {
    const q = mQuery.trim().toLowerCase();
    if (q && !m.email.toLowerCase().includes(q) && !m.name.toLowerCase().includes(q)) return false;
    const hasKey = m.keys.length > 0;
    return mFilter === "all" || (mFilter === "none" ? !hasKey : hasKey);
  });
  const waiting = members.filter((m) => m.keys.length === 0).length;

  const shown = rows.filter((r) => {
    const q = query.trim().toLowerCase();
    return !q || r.key.toLowerCase().includes(q) || r.issuedTo.toLowerCase().includes(q) || r.note.toLowerCase().includes(q);
  });

  const inputCls =
    "w-full rounded-lg border border-line bg-white px-3 py-2 text-sm text-ink focus:border-brand focus:outline-none";
  const btn = "rounded-full px-3 py-1 text-xs font-semibold transition disabled:opacity-50";

  return (
    <div className="mx-auto max-w-6xl px-4 py-10 lg:px-6">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="text-2xl font-extrabold text-ink">회원 · 인증키 관리</h1>
          <p className="mt-1 text-sm text-ink-2">
            {mode === "session" ? (
              <>
                관리자 <strong className="text-ink">{who}</strong> 로 로그인됨 · 발급·연장·해지가 바로 서버에 반영됩니다.
              </>
            ) : (
              "개발 미리보기 — 관리자 토큰으로 인증합니다."
            )}
          </p>
        </div>
        <button onClick={load} disabled={loading} className={`${btn} border border-brand text-brand hover:bg-brand-wash`}>
          {loading ? "불러오는 중…" : "새로고침"}
        </button>
      </div>

      {mode === "token" && (
        <input
          type="password"
          value={token}
          onChange={(e) => setToken(e.target.value)}
          placeholder="관리자 토큰"
          aria-label="관리자 토큰"
          className={`${inputCls} mt-4 max-w-md`}
        />
      )}

      {error && <p role="alert" className="mt-4 rounded-lg border border-red-200 bg-red-50 px-4 py-2 text-sm text-red-700">{error}</p>}
      {notice && <p role="status" className="mt-4 rounded-lg border border-brand/30 bg-brand-wash/60 px-4 py-2 text-sm text-ink">{notice}</p>}


      <div className="mt-6 flex gap-2 border-b border-line" role="tablist" aria-label="관리 구역">
        {([
          ["members", `회원 (${members.length})${waiting ? ` · 대기 ${waiting}` : ""}`],
          ["keys", `인증키 (${rows.length})`],
        ] as [Tab, string][]).map(([id, label]) => (
          <button
            key={id}
            role="tab"
            aria-selected={tab === id}
            onClick={() => setTab(id)}
            className={`-mb-px border-b-2 px-4 py-2 text-sm font-semibold ${tab === id ? "border-brand text-brand" : "border-transparent text-ink-3 hover:text-ink"}`}
          >
            {label}
          </button>
        ))}
      </div>

      {tab === "members" && (
        <section className="mt-4" aria-label="회원 목록">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <div className="flex gap-2" role="group" aria-label="발급 여부">
              {([["none", "인증키 대기"], ["has", "발급됨"], ["all", "전체"]] as const).map(([v, l]) => (
                <button
                  key={v}
                  aria-pressed={mFilter === v}
                  onClick={() => setMFilter(v)}
                  className={`rounded-full border px-3 py-1 text-xs font-semibold ${mFilter === v ? "border-brand bg-brand text-white" : "border-line text-ink-2 hover:border-brand"}`}
                >
                  {l}
                </button>
              ))}
            </div>
            <input className={`${inputCls} max-w-xs`} value={mQuery} onChange={(e) => setMQuery(e.target.value)} placeholder="이메일·이름 검색" aria-label="회원 검색" />
          </div>
          <p className="mt-2 text-xs text-ink-3">회원가입(Clerk)한 사람이 여기에 나타납니다. 가입을 확인하고 기간을 골라 인증키를 발급하면, 그 회원의 「내 계정」에 키가 보입니다.</p>

          <div className="mt-3 overflow-x-auto rounded-2xl border border-line bg-white">
            <table className="w-full min-w-[760px] text-left text-sm">
              <thead className="border-b border-line bg-wash text-xs text-ink-2">
                <tr>
                  <th className="px-4 py-3">회원</th>
                  <th className="px-4 py-3">가입일</th>
                  <th className="px-4 py-3">인증키</th>
                  <th className="px-4 py-3">발급</th>
                </tr>
              </thead>
              <tbody>
                {shownMembers.length === 0 && (
                  <tr><td colSpan={4} className="px-4 py-8 text-center text-ink-3">{members.length ? "조건에 맞는 회원이 없습니다." : "아직 가입한 회원이 없습니다."}</td></tr>
                )}
                {shownMembers.map((m) => (
                  <tr key={m.id} data-testid="member-row" className="border-b border-line/60 align-top last:border-0">
                    <td className="px-4 py-3">
                      <div className="font-semibold text-ink">{m.email || "(이메일 없음)"}</div>
                      <div className="mt-0.5 flex flex-wrap items-center gap-1.5 text-[11px] text-ink-3">
                        {m.name && <span>{m.name}</span>}
                        <span className={`rounded-full px-2 py-0.5 font-semibold ${m.emailVerified ? "bg-brand-wash text-brand" : "bg-amber-50 text-amber-700"}`}>
                          {m.emailVerified ? "이메일 인증됨" : "이메일 미인증"}
                        </span>
                        {Date.parse(m.createdAt) > weekAgo && <span className="rounded-full bg-ink px-2 py-0.5 font-semibold text-white">NEW</span>}
                      </div>
                    </td>
                    <td className="px-4 py-3 text-xs text-ink-2">{m.createdAt.slice(0, 10)}</td>
                    <td className="px-4 py-3 text-xs">
                      {m.keys.length === 0 ? (
                        <span className="rounded-full bg-amber-50 px-2.5 py-0.5 text-[11px] font-semibold text-amber-700">대기</span>
                      ) : (
                        m.keys.map((k) => (
                          <div key={k.key} className="mb-1">
                            <button onClick={() => copy(k.key)} title="클릭해서 복사" className="font-mono text-[11px] text-ink hover:text-brand">{k.key}</button>
                            <span className={`ml-2 rounded-full px-2 py-0.5 text-[10px] font-semibold ${k.status === "active" ? "bg-brand-wash text-brand" : "bg-red-50 text-red-700"}`}>{k.status === "active" ? "사용 가능" : "해지됨"}</span>
                            <span className="ml-2 text-ink-3">{termLabel(k.termMonths)} · PC {k.devices}/{k.maxDevices}</span>
                          </div>
                        ))
                      )}
                    </td>
                    <td className="px-4 py-3">
                      {issuing === m.id ? (
                        <div className="w-72 space-y-2 rounded-xl border border-brand/30 bg-brand-wash/40 p-3">
                          <div className="flex flex-wrap gap-1" role="group" aria-label="기간">
                            {TERMS.map((t) => (
                              <button
                                key={t.months}
                                type="button"
                                aria-pressed={issue.months === t.months}
                                onClick={() => setIssue({ ...issue, months: t.months })}
                                className={`rounded-full border px-2.5 py-0.5 text-xs font-semibold ${issue.months === t.months ? "border-brand bg-brand text-white" : "border-line bg-white text-ink-2 hover:border-brand"}`}
                              >
                                {t.label}
                              </button>
                            ))}
                          </div>
                          <label className="block text-[11px] font-medium text-ink-2">
                            허용 PC 수
                            <input type="number" min={1} max={100} className={`${inputCls} mt-1`} value={issue.maxDevices} onChange={(e) => setIssue({ ...issue, maxDevices: Math.max(1, Number(e.target.value) || 1) })} />
                          </label>
                          <input className={inputCls} value={issue.note} onChange={(e) => setIssue({ ...issue, note: e.target.value })} placeholder="메모 (선택)" aria-label="메모" />
                          <div className="flex gap-2">
                            <button data-testid="issue-confirm" disabled={busy || !m.emailVerified || (mode === "token" && !token)} onClick={() => issueToMember(m)} className="rounded-full bg-brand px-4 py-1.5 text-xs font-semibold text-white hover:bg-brand-dark disabled:opacity-50">
                              {termLabel(issue.months)} 인증키 발급
                            </button>
                            <button onClick={() => setIssuing(null)} className="rounded-full border border-line px-3 py-1.5 text-xs text-ink-2">취소</button>
                          </div>
                          {!m.emailVerified && <p className="text-[11px] text-amber-700">이메일 인증이 끝나야 발급할 수 있습니다.</p>}
                        </div>
                      ) : (
                        <button
                          data-testid="issue-open"
                          onClick={() => { setIssuing(m.id); setIssue({ months: 1, maxDevices: 1, note: "" }); }}
                          className={`${btn} ${m.keys.length ? "border border-brand/40 text-brand hover:bg-brand-wash" : "bg-brand text-white hover:bg-brand-dark"}`}
                        >
                          {m.keys.length ? "추가 발급" : "인증키 발급"}
                        </button>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          {created && (
            <div className="mt-4 rounded-xl border border-brand/30 bg-brand-wash/60 p-4">
              <p className="text-xs font-semibold text-brand">방금 발급한 인증키</p>
              <div className="mt-2 flex flex-wrap items-center gap-3">
                <code data-testid="created-key" className="select-all rounded-lg bg-white px-3 py-2 font-mono text-base tracking-wider text-ink">{created.key}</code>
                <button onClick={() => copy(created.key)} className={`${btn} bg-brand text-white hover:bg-brand-dark`}>키 복사</button>
              </div>
            </div>
          )}
        </section>
      )}

      {tab === "keys" && (
        <>
      <section className="mt-6 rounded-2xl border border-line bg-white p-5">
        <h2 className="font-semibold text-ink">새 인증키 직접 발급 <span className="text-xs font-normal text-ink-3">(회원 가입 없이 — 오프라인 고객 등)</span></h2>
        <div className="mt-4 grid gap-4 md:grid-cols-4">
          <label className="text-xs font-medium text-ink-2 md:col-span-2">
            받는 사람 / 고객사
            <input className={`${inputCls} mt-1`} value={form.issuedTo} onChange={(e) => setForm({ ...form, issuedTo: e.target.value })} placeholder="예: 고객사A" />
          </label>
          <label className="text-xs font-medium text-ink-2">
            허용 PC 수
            <input type="number" min={1} max={100} className={`${inputCls} mt-1`} value={form.maxDevices} onChange={(e) => setForm({ ...form, maxDevices: Math.max(1, Number(e.target.value) || 1) })} />
          </label>
          <div className="md:col-span-4" role="group" aria-label="기간">
            <p className="text-xs font-medium text-ink-2">
              기간 <span className="text-ink-3">(구매자가 처음 활성화한 날부터 셉니다)</span>
            </p>
            <div className="mt-2 flex flex-wrap gap-2">
              {TERMS.map((t) => (
                <button
                  key={t.months}
                  type="button"
                  aria-pressed={form.months === t.months}
                  onClick={() => setForm({ ...form, months: t.months })}
                  className={`rounded-full border px-4 py-1.5 text-sm font-semibold transition ${
                    form.months === t.months
                      ? "border-brand bg-brand text-white shadow-sm"
                      : "border-line bg-white text-ink-2 hover:border-brand hover:text-brand"
                  }`}
                >
                  {t.label}
                </button>
              ))}
            </div>
          </div>
          <label className="text-xs font-medium text-ink-2 md:col-span-4">
            메모
            <input className={`${inputCls} mt-1`} value={form.note} onChange={(e) => setForm({ ...form, note: e.target.value })} placeholder="주문번호 등 (선택)" />
          </label>
        </div>
        <button
          onClick={create}
          disabled={busy || (mode === "token" && !token)}
          className="mt-4 rounded-full bg-brand px-6 py-2.5 text-sm font-semibold text-white hover:bg-brand-dark disabled:opacity-50"
        >
          {termLabel(form.months)} 인증키 발급
        </button>

        {created && (
          <div className="mt-5 rounded-xl border border-brand/30 bg-brand-wash/60 p-4">
            <p className="text-xs font-semibold text-brand">발급되었습니다 — 구매자에게 전달하세요</p>
            <div className="mt-2 flex flex-wrap items-center gap-3">
              <code className="select-all rounded-lg bg-white px-3 py-2 font-mono text-base tracking-wider text-ink">{created.key}</code>
              <button onClick={() => copy(created.key)} className={`${btn} bg-brand text-white hover:bg-brand-dark`}>키 복사</button>
            </div>
            <p className="mt-2 text-xs text-ink-2">
              {created.issuedTo || "(이름 없음)"} · {termLabel(created.termMonths) || created.expires} · PC {created.maxDevices}대
            </p>
          </div>
        )}
      </section>

      <section className="mt-6">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <h2 className="font-semibold text-ink">발급 내역 <span className="text-sm font-normal text-ink-3">({shown.length}/{rows.length})</span></h2>
          <input className={`${inputCls} max-w-xs`} value={query} onChange={(e) => setQuery(e.target.value)} placeholder="키·이름·메모 검색" aria-label="검색" />
        </div>

        <div className="mt-3 overflow-x-auto rounded-2xl border border-line bg-white">
          <table className="w-full min-w-[820px] text-left text-sm">
            <thead className="border-b border-line bg-wash text-xs text-ink-2">
              <tr>
                <th className="px-4 py-3">인증키</th>
                <th className="px-4 py-3">대상 · 회원</th>
                <th className="px-4 py-3">기간 · 만료</th>
                <th className="px-4 py-3">상태</th>
                <th className="px-4 py-3">사용 PC</th>
                <th className="px-4 py-3">관리</th>
              </tr>
            </thead>
            <tbody>
              {shown.length === 0 && (
                <tr><td colSpan={6} className="px-4 py-8 text-center text-ink-3">{rows.length ? "검색 결과가 없습니다." : "발급된 키가 없습니다."}</td></tr>
              )}
              {shown.map((r) => (
                <tr key={r.key} className="border-b border-line/60 align-top last:border-0">
                  <td className="px-4 py-3">
                    <button onClick={() => copy(r.key)} title="클릭해서 복사" className="font-mono text-xs text-ink hover:text-brand">{r.key}</button>
                    {r.note && <div className="mt-1 text-[11px] text-ink-3">{r.note}</div>}
                  </td>
                  <td className="px-4 py-3 text-ink-2">{r.issuedTo || "—"}{r.memberEmail && <div className="mt-0.5 text-[11px] text-brand">회원 {r.memberEmail}</div>}</td>
                  <td className="px-4 py-3 text-ink-2">
                    {r.termMonths ? <span className="mr-1 rounded-full bg-wash px-2 py-0.5 text-[11px] text-ink-2">{termLabel(r.termMonths)}</span> : null}
                    <span className="text-xs">{r.expires}</span>
                  </td>
                  <td className="px-4 py-3">
                    <span className={`rounded-full px-2.5 py-0.5 text-[11px] font-semibold ${r.status === "active" ? "bg-brand-wash text-brand" : "bg-red-50 text-red-700"}`}>
                      {r.status === "active" ? "사용 가능" : "해지됨"}
                    </span>
                  </td>
                  <td className="px-4 py-3 text-xs text-ink-2">
                    {r.devices.length}/{r.maxDevices}
                    {r.devices.map((d) => (
                      <div key={d.fp} className="mt-1 flex items-center gap-2">
                        <span className="text-ink">{d.hostname || "(이름 없음)"}</span>
                        <span className="font-mono text-[10px] text-ink-3">{d.fp.slice(0, 8)}</span>
                        <button
                          disabled={busy}
                          onClick={() => confirm(`${d.hostname || d.fp} 의 등록을 해제할까요? 다른 PC에서 다시 쓸 수 있게 됩니다.`) && act(() => call("POST", "/admin/keys/release", { key: r.key, fp: d.fp }), "PC 등록을 해제했습니다.")}
                          className="text-[11px] text-red-600 hover:underline disabled:opacity-50"
                        >
                          해제
                        </button>
                      </div>
                    ))}
                  </td>
                  <td className="px-4 py-3">
                    <div className="flex flex-wrap gap-1.5">
                      {[1, 3, 12].map((m) => (
                        <button key={m} disabled={busy} onClick={() => act(() => call("POST", "/admin/keys/extend", { key: r.key, months: m }), `${termLabel(m)} 연장했습니다.`)} className={`${btn} border border-brand/40 text-brand hover:bg-brand-wash`}>
                          +{termLabel(m)}
                        </button>
                      ))}
                      {r.status === "active" ? (
                        <button disabled={busy} onClick={() => confirm(`${r.key} 를 해지할까요? 사용 중인 PC는 다음 확인 때 분석이 막힙니다.`) && act(() => call("POST", "/admin/keys/revoke", { key: r.key }), "해지했습니다.")} className={`${btn} border border-red-300 text-red-600 hover:bg-red-50`}>
                          해지
                        </button>
                      ) : (
                        <span className="self-center text-[11px] text-ink-3">연장하면 복구됩니다</span>
                      )}
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
        </>
      )}
    </div>
  );
}

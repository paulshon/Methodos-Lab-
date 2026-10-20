// 종단 검증 — node scripts/verify-site.mjs
//  1) 타입 검사  2) 운영 빌드  3) 시험 서버(Clerk 없이, 회원 목록은 시험용 JSON)를 띄워
//  회원 → 인증키 발급 → 앱 활성화 → 좌석 제한 → 해지 까지의 API 흐름과 GitHub 배포처를 확인한다.
// 실제 Clerk 가입·로그인은 이 스크립트가 아니라 README 의 「Clerk 로 실제 시연」 절차로 확인한다.
import { spawn, spawnSync } from "node:child_process";
import crypto from "node:crypto";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const site = path.join(path.dirname(fileURLToPath(import.meta.url)), "..");
const PORT = 3191;
const base = `http://localhost:${PORT}`;
const TOKEN = "verify-" + crypto.randomBytes(12).toString("hex");

let pass = 0;
let fail = 0;
const check = (name, cond, extra = "") => {
  cond ? pass++ : fail++;
  console.log(cond ? "  ✓" : "  ✗", name, extra);
};

function run(cmd, args) {
  const r = spawnSync(cmd, args, { cwd: site, stdio: "inherit", shell: true });
  if (r.status !== 0) process.exit(r.status ?? 1);
}
const wait = (ms) => new Promise((r) => setTimeout(r, ms));

console.log("→ npm run typecheck");
run("npm", ["run", "typecheck"]);
if (!process.argv.includes("--no-build")) {
  console.log("→ npm run build");
  run("npm", ["run", "build"]);
}

// 시험용 서명 키쌍·저장소·회원 파일 (모두 임시 폴더)
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "lab-verify-"));
const { privateKey, publicKey } = crypto.generateKeyPairSync("ed25519");
const privPem = privateKey.export({ type: "pkcs8", format: "pem" });
const members = [
  { id: "user_verified", email: "member@example.com", emailVerified: true, name: "홍 길동", createdAt: "2026-10-01T00:00:00.000Z", lastSignInAt: null },
  { id: "user_unverified", email: "pending@example.com", emailVerified: false, name: "", createdAt: "2026-10-02T00:00:00.000Z", lastSignInAt: null },
  { id: "user_other", email: "other@example.com", emailVerified: true, name: "", createdAt: "2026-10-03T00:00:00.000Z", lastSignInAt: null },
];
fs.writeFileSync(path.join(tmp, "members.json"), JSON.stringify(members));

const child = spawn("npx", ["next", "dev", "--port", String(PORT), "--hostname", "localhost"], {
  cwd: site,
  shell: true,
  stdio: "ignore",
  env: {
    ...process.env,
    NEXT_PUBLIC_CLERK_KEYLESS: "0",
    NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY: "",
    CLERK_SECRET_KEY: "",
    LICENSE_STORE: "file",
    LICENSE_DEV_DB: path.join(tmp, "licenses.json"),
    LICENSE_ADMIN_TOKEN: TOKEN,
    LICENSE_PRIVATE_KEY: privPem.replace(/\n/g, "\\n"),
    MEMBERS_DEV_FILE: path.join(tmp, "members.json"),
    GITHUB_RELEASE_REPO: "",
    GITHUB_RELEASE_TAG: "",
  },
});

const admin = { "x-admin-token": TOKEN, "content-type": "application/json" };
const post = (p, body, headers = admin) => fetch(base + p, { method: "POST", headers, body: JSON.stringify(body) });
const fp = () => crypto.randomBytes(32).toString("hex");

try {
  for (let i = 0; i < 60; i++) {
    try {
      if ((await fetch(base + "/api/license-health")).status < 500) break;
    } catch {}
    await wait(1500);
  }

  console.log("\n페이지·배포처");
  for (const p of ["/", "/login", "/signup", "/account", "/offline", "/admin-preview"]) {
    const r = await fetch(base + p, { redirect: "manual" });
    check(`GET ${p}`, r.status === 200, String(r.status));
  }
  for (const id of ["win-portable", "win-setup"]) {
    const r = await fetch(`${base}/api/download/${id}`, { redirect: "manual" });
    const loc = r.headers.get("location") || "";
    check(
      `/api/download/${id} → GitHub paulshon/Methodos-Lab-`,
      r.status === 302 && loc.startsWith("https://github.com/paulshon/Methodos-Lab-/releases/download/") && !loc.includes("methodosbasic2"),
      loc,
    );
  }
  const me = await (await fetch(base + "/api/me")).json();
  check("/api/me (Clerk 없음)", me.configured === false && me.signedIn === false);

  console.log("\n관리자 보호");
  check("토큰 없이 /admin/members → 401", (await fetch(base + "/admin/members")).status === 401);
  check("엉뚱한 토큰 → 401", (await fetch(base + "/admin/members", { headers: { "x-admin-token": "nope" } })).status === 401);
  check("토큰 없이 /admin/keys → 401", (await fetch(base + "/admin/keys")).status === 401);
  check("Clerk 없이 /api/my-keys → 503(크래시 아님)", (await fetch(base + "/api/my-keys")).status === 503);

  console.log("\n회원 → 인증키 발급");
  let list = await (await fetch(base + "/admin/members", { headers: admin })).json();
  check("회원 3명이 보인다", list.members.length === 3 && list.members.every((m) => m.keys.length === 0));

  const r1 = await post("/admin/keys", { memberId: "user_verified", months: 3, maxDevices: 1, memberEmail: "evil@example.com" });
  const k1 = await r1.json();
  check("인증된 회원에게 3개월 키 발급", r1.status === 200 && k1.termMonths === 3 && /^MTDS-/.test(k1.key), k1.key);
  check("회원 이메일은 서버가 Clerk 쪽 값으로 기록(보낸 값 무시)", k1.memberId === "user_verified" && k1.memberEmail === "member@example.com");

  const r2 = await post("/admin/keys", { memberId: "user_unverified", months: 1 });
  check("이메일 미인증 회원 → 409", r2.status === 409 && (await r2.json()).error === "email_unverified");
  const r3 = await post("/admin/keys", { memberId: "user_ghost", months: 1 });
  check("없는 회원 → 404", r3.status === 404);

  list = await (await fetch(base + "/admin/members", { headers: admin })).json();
  const mine = list.members.find((m) => m.id === "user_verified");
  const other = list.members.find((m) => m.id === "user_other");
  check("회원 목록에 방금 발급한 키가 연결됨", mine.keys.length === 1 && mine.keys[0].key === k1.key);
  check("다른 회원에게는 섞이지 않음", other.keys.length === 0);

  console.log("\n앱 활성화 (데스크톱 앱이 부르는 API)");
  const f1 = fp();
  const a1 = await post("/api/activate", { key: k1.key, fp: f1, hostname: "PC-A" }, { "content-type": "application/json" });
  const lic = (await a1.json()).license;
  const sigOk = lic && crypto.verify(null, Buffer.from(lic.p), publicKey, Buffer.from(lic.s, "base64url"));
  const payload = lic ? JSON.parse(Buffer.from(lic.p, "base64url").toString()) : {};
  check("활성화 200 + 서명 유효", a1.status === 200 && sigOk === true);
  check("라이선스 내용: 회원 키·기간·이 PC 지문", payload.key === k1.key && payload.termMonths === 3 && payload.fp === f1 && !!payload.expires, payload.expires);
  const a2 = await post("/api/activate", { key: k1.key, fp: fp(), hostname: "PC-B" }, { "content-type": "application/json" });
  check("두 번째 PC → 409 seat_limit", a2.status === 409 && (await a2.json()).error === "seat_limit");
  const a3 = await post("/api/activate", { key: "AAAA-BBBB-CCCC-DDDD-EEEE", fp: f1 }, { "content-type": "application/json" });
  check("등록 안 된 키 → 404", a3.status === 404);

  console.log("\n해지");
  const rv = await post("/admin/keys/revoke", { key: k1.key });
  check("해지 200", rv.status === 200);
  const a4 = await post("/api/renew", { key: k1.key, fp: f1 }, { "content-type": "application/json" });
  check("해지된 키는 갱신 거부(403)", a4.status === 403 && (await a4.json()).error === "revoked");
} catch (e) {
  console.error(e);
  fail++;
} finally {
  if (child.pid) spawnSync("taskkill", ["/PID", String(child.pid), "/T", "/F"], { shell: true, stdio: "ignore" });
  fs.rmSync(tmp, { recursive: true, force: true });
}

console.log(`\n${pass} passed, ${fail} failed`);
if (fail) {
  console.error("VERIFY FAILED");
  process.exit(1);
}
console.log("VERIFY OK");

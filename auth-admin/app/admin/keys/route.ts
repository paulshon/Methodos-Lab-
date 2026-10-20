import { handle, readJson, requireAdmin } from "@/lib/license/http";
import { ApiError } from "@/lib/license/core";
import { adminCreate, adminList } from "@/lib/license/service";
import { getMember } from "@/lib/members";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function GET(req: Request) {
  return handle(async () => {
    await requireAdmin(req);
    return { keys: await adminList() };
  });
}

/** memberId 를 주면 그 회원(Clerk 사용자)에게 발급한다. 회원 이메일은 클라이언트가 보낸 값이 아니라 Clerk 에서 다시 읽는다. */
export async function POST(req: Request) {
  return handle(async () => {
    await requireAdmin(req);
    const body = await readJson(req);
    let member: { id: string; email: string } | undefined;
    if (body.memberId) {
      const m = await getMember(String(body.memberId));
      if (!m) throw new ApiError(404, "unknown_member", "해당 회원을 찾을 수 없습니다.");
      if (!m.emailVerified) throw new ApiError(409, "email_unverified", `${m.email} 은(는) 이메일 인증이 끝나지 않은 회원입니다.`);
      member = { id: m.id, email: m.email };
      if (!body.issuedTo) body.issuedTo = m.name ? `${m.name} <${m.email}>` : m.email;
    }
    return adminCreate(body, undefined, member);
  });
}

import { handle, requireAdmin } from "@/lib/license/http";
import { adminList } from "@/lib/license/service";
import { listMembers } from "@/lib/members";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

/** 가입한 회원 전부 + 각자에게 발급된 인증키 요약. 관리자만. */
export async function GET(req: Request) {
  return handle(async () => {
    await requireAdmin(req);
    const [members, keys] = await Promise.all([listMembers(), adminList()]);
    const byMember = new Map<string, typeof keys>();
    for (const k of keys) {
      if (!k.memberId) continue;
      byMember.set(k.memberId, [...(byMember.get(k.memberId) ?? []), k]);
    }
    return {
      members: members.map((m) => ({
        ...m,
        keys: (byMember.get(m.id) ?? []).map((k) => ({
          key: k.key,
          status: k.status,
          expires: k.expires,
          termMonths: k.termMonths,
          devices: k.devices.length,
          maxDevices: k.maxDevices,
        })),
      })),
    };
  });
}

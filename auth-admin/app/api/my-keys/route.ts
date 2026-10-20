import { auth } from "@clerk/nextjs/server";
import { clerkConfigured } from "@/lib/clerk";
import { ApiError } from "@/lib/license/core";
import { handle } from "@/lib/license/http";
import { keysOfMember } from "@/lib/license/service";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

/**
 * 메스도스랩 홈페이지(다른 도메인)에서 회원이 자기 키를 볼 수 있게 한다.
 * 홈페이지가 Clerk 세션 토큰을 `Authorization: Bearer` 로 보내면 auth() 가 같은 Clerk 앱의 사용자로 인식한다.
 * 허용 출처: ALLOWED_ORIGINS(쉼표) + NEXT_PUBLIC_HOMEPAGE_URL. 목록에 없는 출처에는 CORS 헤더를 주지 않는다.
 */
function allowedOrigin(req: Request): string | null {
  const origin = req.headers.get("origin");
  if (!origin) return null;
  const list = [process.env.ALLOWED_ORIGINS, process.env.NEXT_PUBLIC_HOMEPAGE_URL]
    .join(",")
    .split(/[,\s]+/)
    .map((s) => s.trim().replace(/\/$/, ""))
    .filter(Boolean);
  return list.includes(origin) ? origin : null;
}

function withCors(res: Response, origin: string | null): Response {
  if (origin) {
    res.headers.set("access-control-allow-origin", origin);
    res.headers.set("vary", "Origin");
  }
  return res;
}

export async function OPTIONS(req: Request) {
  const origin = allowedOrigin(req);
  const res = new Response(null, { status: 204 });
  if (origin) {
    res.headers.set("access-control-allow-origin", origin);
    res.headers.set("access-control-allow-methods", "GET, OPTIONS");
    res.headers.set("access-control-allow-headers", "authorization, content-type");
    res.headers.set("access-control-max-age", "600");
    res.headers.set("vary", "Origin");
  }
  return res;
}

/** 로그인한 회원 본인에게 발급된 인증키만. */
export async function GET(req: Request) {
  const res = await handle(async () => {
    if (!clerkConfigured()) throw new ApiError(503, "clerk_not_configured", "회원 기능(Clerk)이 설정되지 않았습니다.");
    const { userId } = await auth();
    if (!userId) throw new ApiError(401, "unauthorized", "로그인이 필요합니다.");
    return { keys: await keysOfMember(userId) };
  });
  return withCors(res, allowedOrigin(req));
}

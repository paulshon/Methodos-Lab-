import { auth } from "@clerk/nextjs/server";
import { clerkConfigured } from "@/lib/clerk";
import { ApiError } from "@/lib/license/core";
import { handle } from "@/lib/license/http";
import { keysOfMember } from "@/lib/license/service";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

/** 로그인한 회원 본인에게 발급된 인증키만. */
export async function GET() {
  return handle(async () => {
    if (!clerkConfigured()) throw new ApiError(503, "clerk_not_configured", "회원 기능(Clerk)이 설정되지 않았습니다.");
    const { userId } = await auth();
    if (!userId) throw new ApiError(401, "unauthorized", "로그인이 필요합니다.");
    return { keys: await keysOfMember(userId) };
  });
}

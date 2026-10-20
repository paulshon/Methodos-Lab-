import { NextResponse } from "next/server";
import { auth, currentUser } from "@clerk/nextjs/server";
import { clerkConfigured } from "@/lib/clerk";
import { checkClerkAdmin } from "@/lib/admin/clerk-admin";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

/** 홈페이지 상단의 로그인 표시용. 개인 정보는 이메일과 관리자 여부뿐이다. */
export async function GET() {
  const headers = { "cache-control": "no-store" };
  if (!clerkConfigured()) return NextResponse.json({ configured: false, signedIn: false }, { headers });
  const { userId } = await auth();
  if (!userId) return NextResponse.json({ configured: true, signedIn: false }, { headers });
  const user = await currentUser();
  const check = await checkClerkAdmin();
  return NextResponse.json(
    {
      configured: true,
      signedIn: true,
      email: user?.primaryEmailAddress?.emailAddress ?? "",
      isAdmin: check.state === "ok",
    },
    { headers },
  );
}

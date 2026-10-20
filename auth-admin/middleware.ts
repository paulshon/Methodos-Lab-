import { NextResponse } from "next/server";
import type { NextFetchEvent, NextRequest } from "next/server";
import { clerkMiddleware, createRouteMatcher } from "@clerk/nextjs/server";
import { clerkConfigured } from "@/lib/clerk";

const isPublic = createRouteMatcher([
  "/",
  "/login(.*)",
  "/signup(.*)",
  "/api/download(.*)",
  "/api/me", // 비로그인이면 signedIn:false 로 답한다
  // /api/my-keys 는 라우트가 직접 로그인 여부를 확인해 401 JSON 으로 답한다(리다이렉트 대신).
  "/api/my-keys",
  // 인증키 서버 — 앱(데스크톱)이 부른다. 보호는 서명·관리자 토큰으로 하므로 Clerk 로그인은 요구하지 않는다.
  "/api/activate",
  "/api/renew",
  "/api/deactivate",
  "/api/offline-activate",
  "/api/license-health",
  "/admin/keys(.*)",
  "/admin/members(.*)", // 라우트가 관리자 토큰·Clerk 세션을 직접 확인한다
  "/offline(.*)",
  "/admin-preview(.*)", // 운영에서는 페이지가 404 이고, 개발 미리보기는 토큰으로 인증한다
]);

const hasClerk = clerkConfigured();

const clerkHandler = clerkMiddleware(async (auth, req) => {
  if (isPublic(req)) return;
  const { userId } = await auth();
  if (!userId) {
    const url = req.nextUrl.clone();
    const back = req.nextUrl.pathname + req.nextUrl.search;
    url.pathname = "/login";
    url.search = "";
    url.searchParams.set("redirect_url", back);
    return NextResponse.redirect(url);
  }
});

function passthrough(_req: NextRequest, _event: NextFetchEvent) {
  return NextResponse.next();
}

export default hasClerk ? clerkHandler : passthrough;

export const config = {
  matcher: ["/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|webmanifest)).*)", "/(api|trpc)(.*)"],
};

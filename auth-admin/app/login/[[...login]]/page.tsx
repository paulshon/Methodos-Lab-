import Link from "next/link";
import { SignIn } from "@clerk/nextjs";
import { clerkConfigured } from "@/lib/clerk";

export const metadata = { title: "관리자 로그인 — Methodos Lab", robots: { index: false, follow: false } };

export default function LoginPage() {
  if (!clerkConfigured()) {
    return (
      <div className="mx-auto max-w-md px-4 py-16 text-center">
        <h1 className="text-xl font-semibold text-ink">관리자 로그인</h1>
        <p className="mt-3 text-sm text-ink-2">
          Clerk가 설정되지 않았습니다. <code className="text-xs">NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY</code>·
          <code className="text-xs">CLERK_SECRET_KEY</code> 를 Vercel 환경변수에 추가하세요.
        </p>
        <Link href="/" className="mt-6 inline-block rounded-full bg-brand px-5 py-2.5 text-sm font-semibold text-white hover:bg-brand-dark">
          다시 시도
        </Link>
      </div>
    );
  }

  return (
    <div className="flex flex-col items-center px-4 py-12">
      <p className="mb-4 text-sm text-ink-2">관리자 전용입니다. 회원가입·회원 로그인은 메스도스랩 홈페이지에서 합니다.</p>
      <SignIn routing="path" path="/login" forceRedirectUrl="/admin" />
    </div>
  );
}

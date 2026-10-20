import Link from "next/link";
import { SignUp } from "@clerk/nextjs";
import { clerkConfigured } from "@/lib/clerk";

export default function SignUpPage() {
  if (!clerkConfigured()) {
    return (
      <div className="mx-auto max-w-md px-4 py-16 text-center">
        <h1 className="text-xl font-semibold text-ink">Sign up</h1>
        <p className="mt-3 text-sm text-ink-2">Clerk 환경 변수가 없어 회원가입이 비활성화되어 있습니다.</p>
        <Link
          href="/"
          className="mt-6 inline-block rounded-full bg-brand px-5 py-2.5 text-sm font-semibold text-white hover:bg-brand-dark"
        >
          홈으로
        </Link>
      </div>
    );
  }

  return (
    <div className="flex justify-center px-4 py-12">
      <SignUp routing="path" path="/signup" signInUrl="/login" />
    </div>
  );
}

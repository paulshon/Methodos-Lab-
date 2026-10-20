import Link from "next/link";
import { SignIn } from "@clerk/nextjs";
import { clerkConfigured } from "@/lib/clerk";

export default function LoginPage() {
  if (!clerkConfigured()) {
    return (
      <div className="mx-auto max-w-md px-4 py-16 text-center">
        <h1 className="text-xl font-semibold text-ink">Sign in</h1>
        <p className="mt-3 text-sm text-ink-2">
          Clerk가 설정되지 않았습니다. <code className="text-xs">NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY</code>를 Vercel에
          추가하면 로그인이 활성화됩니다.
        </p>
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
      <SignIn routing="path" path="/login" signUpUrl="/signup" />
    </div>
  );
}

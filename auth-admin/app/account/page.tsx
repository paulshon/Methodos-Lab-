import { redirect } from "next/navigation";
import { auth } from "@clerk/nextjs/server";
import { MyKeys } from "@/components/account/my-keys";
import { clerkConfigured } from "@/lib/clerk";
import { WIN_ARTIFACT, WIN_SETUP_ARTIFACT } from "@/lib/product";

export const dynamic = "force-dynamic";
export const metadata = { title: "내 계정 — Methodos Lab", robots: { index: false, follow: false } };

export default async function AccountPage() {
  if (!clerkConfigured()) {
    return (
      <div className="mx-auto max-w-lg px-4 py-16 text-center text-sm text-ink-2">
        Clerk 가 설정되지 않아 회원 기능이 꺼져 있습니다.
      </div>
    );
  }
  const { userId } = await auth();
  if (!userId) redirect("/login?redirect_url=/account");

  return (
    <div className="mx-auto max-w-3xl px-4 py-10 lg:px-6">
      <h1 className="text-2xl font-extrabold text-ink">내 계정</h1>
      <MyKeys />
      <section className="mt-8 rounded-2xl border border-line bg-white p-5">
        <h2 className="font-bold text-ink">프로그램 내려받기</h2>
        <p className="mt-1 text-sm text-ink-2">설치한 뒤 처음 실행하면 인증키 창이 뜹니다. 위의 인증키를 붙여 넣으세요.</p>
        <div className="mt-3 flex flex-wrap gap-2">
          {[WIN_ARTIFACT, WIN_SETUP_ARTIFACT].map((a) => (
            <a key={a.id} href={`/api/download/${a.id}`} className="rounded-full bg-brand px-5 py-2 text-sm font-semibold text-white hover:bg-brand-dark">
              {a.label}
            </a>
          ))}
        </div>
        <p className="mt-3 text-xs text-ink-3">인터넷이 없는 PC 는 <a className="underline" href="/offline">오프라인 활성화</a>를 쓰세요.</p>
      </section>
    </div>
  );
}

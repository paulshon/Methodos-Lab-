import Link from "next/link";
import { BrandMark } from "@/components/brand-mark";

const HOME = (process.env.NEXT_PUBLIC_HOMEPAGE_URL || "").trim();

export default function Home() {
  const card = "rounded-2xl border border-line bg-white p-6 shadow-sm";
  return (
    <main className="mx-auto max-w-3xl px-4 py-14 lg:px-6">
      <BrandMark size="lg" />
      <h1 className="mt-8 text-3xl font-extrabold tracking-tight text-ink">회원가입하고 인증키를 받으세요</h1>
      <p className="mt-3 leading-relaxed text-ink-2">
        Methodos Basic 은 인증키로 PC 를 활성화해 사용합니다. 이 곳에서 회원으로 가입하면 관리자가 가입을 확인한 뒤 인증키를
        발급하고, 발급된 키는 <strong className="text-ink">내 계정</strong>에서 바로 확인할 수 있습니다.
      </p>
      <ol className="mt-8 grid gap-4 sm:grid-cols-3">
        {[
          ["1", "회원가입", "이메일 인증까지 마치면 가입이 완료됩니다."],
          ["2", "관리자 확인", "관리자가 가입한 회원을 확인하고 기간(1개월~3년)을 정해 인증키를 발급합니다."],
          ["3", "내 계정에서 확인", "발급된 인증키를 복사해 프로그램의 인증키 창에 입력하세요."],
        ].map(([n, t, d]) => (
          <li key={n} className={card}>
            <span className="text-xs font-bold text-brand">STEP {n}</span>
            <h2 className="mt-1 font-bold text-ink">{t}</h2>
            <p className="mt-2 text-sm leading-relaxed text-ink-2">{d}</p>
          </li>
        ))}
      </ol>
      <div className="mt-8 flex flex-wrap gap-3">
        <Link href="/signup" className="rounded-full bg-brand px-6 py-2.5 text-sm font-semibold text-white hover:bg-brand-dark">회원가입</Link>
        <Link href="/login" className="rounded-full border border-brand px-6 py-2.5 text-sm font-semibold text-brand hover:bg-brand-wash">로그인</Link>
        <Link href="/account" className="rounded-full border border-line px-6 py-2.5 text-sm font-semibold text-ink-2 hover:border-brand hover:text-brand">내 계정</Link>
        {HOME && <a href={HOME} className="rounded-full border border-line px-6 py-2.5 text-sm font-semibold text-ink-2 hover:border-brand hover:text-brand">메스도스랩 홈페이지</a>}
      </div>
    </main>
  );
}

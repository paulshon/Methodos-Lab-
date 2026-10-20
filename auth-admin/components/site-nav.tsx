"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useState } from "react";
import { SignOutButton } from "@clerk/nextjs";
import { clerkConfigured } from "@/lib/clerk";
import { BrandMark } from "./brand-mark";

type Me = { configured: boolean; signedIn: boolean; email?: string; isAdmin?: boolean };

const HOME = (process.env.NEXT_PUBLIC_HOMEPAGE_URL || "").trim().replace(/\/$/, "");

export function SiteNav() {
  const [me, setMe] = useState<Me | null>(null);
  const pathname = usePathname(); // 로그인·로그아웃으로 주소가 바뀌면 다시 읽는다

  useEffect(() => {
    let alive = true;
    fetch("/api/me", { cache: "no-store" })
      .then((r) => r.json())
      .then((j: Me) => alive && setMe(j))
      .catch(() => alive && setMe({ configured: false, signedIn: false }));
    return () => {
      alive = false;
    };
  }, [pathname]);

  const pill = "rounded-full px-4 py-1.5 text-[13px] font-semibold transition-colors";
  return (
    <header className="sticky top-0 z-50 border-b border-line/80 bg-white/95 backdrop-blur-md">
      <div className="mx-auto flex max-w-6xl flex-wrap items-center gap-3 px-4 py-3 lg:px-6">
        <Link href="/" className="shrink-0">
          <BrandMark size="sm" />
        </Link>
        <nav className="ml-auto flex flex-wrap items-center gap-2 text-[13px]" aria-label="계정 메뉴">
          {HOME && (
            <a href={HOME} className="px-2 text-ink-2 hover:text-brand">
              홈페이지
            </a>
          )}
          {me?.signedIn ? (
            <>
              <span className="hidden max-w-[220px] truncate text-ink-3 sm:inline" title={me.email}>
                {me.email}
              </span>
              <Link href="/account" className={`${pill} border border-brand text-brand hover:bg-brand-wash`}>
                내 계정
              </Link>
              {me.isAdmin && (
                <Link href="/admin" className={`${pill} bg-ink text-white hover:bg-ink-2`}>
                  관리자
                </Link>
              )}
              {clerkConfigured() && (
                <SignOutButton redirectUrl="/">
                  <button type="button" className="px-2 text-ink-2 hover:text-brand">
                    로그아웃
                  </button>
                </SignOutButton>
              )}
            </>
          ) : (
            <>
              <Link href="/login" className={`${pill} border border-line text-ink-2 hover:border-brand hover:text-brand`}>
                로그인
              </Link>
              <Link href="/signup" className={`${pill} bg-brand text-white hover:bg-brand-dark`}>
                회원가입
              </Link>
            </>
          )}
        </nav>
      </div>
    </header>
  );
}

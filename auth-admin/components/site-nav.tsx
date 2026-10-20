"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useState } from "react";
import { SignOutButton } from "@clerk/nextjs";
import { clerkConfigured } from "@/lib/clerk";
import { BrandMark } from "./brand-mark";

type Me = { configured: boolean; signedIn: boolean; email?: string; isAdmin?: boolean };

const HOME = (process.env.NEXT_PUBLIC_HOMEPAGE_URL || "").trim().replace(/\/$/, "");

/** 관리자 전용 서버의 상단: 관리자 로그인 / 로그아웃만 있다. */
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
        <Link href="/admin" className="flex shrink-0 items-center gap-2">
          <BrandMark size="sm" />
          <span className="rounded-full bg-ink px-2 py-0.5 text-[11px] font-bold text-white">관리자</span>
        </Link>
        <nav className="ml-auto flex flex-wrap items-center gap-2 text-[13px]" aria-label="관리자 메뉴">
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
              {clerkConfigured() && (
                <SignOutButton redirectUrl="/login">
                  <button type="button" className={`${pill} border border-line text-ink-2 hover:border-brand hover:text-brand`}>
                    로그아웃
                  </button>
                </SignOutButton>
              )}
            </>
          ) : (
            <Link href="/login" className={`${pill} bg-brand text-white hover:bg-brand-dark`}>
              관리자 로그인
            </Link>
          )}
        </nav>
      </div>
    </header>
  );
}

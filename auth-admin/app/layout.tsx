import type { Metadata, Viewport } from "next";
import { AppProviders } from "@/components/providers";
import { SiteFooter } from "@/components/site-footer";
import { SiteNav } from "@/components/site-nav";
import "./globals.css";

export const metadata: Metadata = {
  title: "Methodos Lab — 관리자",
  description: "Methodos Lab 회원 확인과 Methodos Basic 인증키 발급 관리자.",
};

export const viewport: Viewport = {
  themeColor: "#0B665C",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ko">
      <body className="font-sans">
        <AppProviders>
          <SiteNav />
          {children}
          <SiteFooter />
        </AppProviders>
      </body>
    </html>
  );
}

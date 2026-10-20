import { BrandMark } from "./brand-mark";

export function SiteFooter() {
  return (
    <footer className="mt-16 border-t border-line bg-white">
      <div className="mx-auto flex max-w-6xl flex-col gap-3 px-4 py-8 md:flex-row md:items-center md:justify-between lg:px-6">
        <BrandMark size="sm" />
        <p className="text-xs text-ink-3">© {new Date().getFullYear()} Methodos Lab · 인증키 및 회원 서버</p>
      </div>
    </footer>
  );
}

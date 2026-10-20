import { cn } from "@/lib/cn";

type Props = { size?: "sm" | "md" | "lg"; className?: string };

const SIZES = { sm: 30, md: 38, lg: 52 } as const;

/** 메스도스랩-홈페이지 상단과 같은 로고 + 「Methodos Lab」. */
export function BrandMark({ size = "md", className }: Props) {
  const px = SIZES[size];
  return (
    <span className={cn("inline-flex items-center gap-2.5", className)}>
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img src="/methodos-lab-logo.svg" alt="Methodos Lab" width={px} height={px} />
      <span className={cn("font-extrabold tracking-tight text-ink", size === "lg" ? "text-2xl" : "text-[17px]")}>
        Methodos <em className="not-italic text-brand">Lab</em>
      </span>
    </span>
  );
}

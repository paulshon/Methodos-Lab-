/**
 * Clerk 사용 여부.
 * NEXT_PUBLIC_CLERK_KEYLESS=1 은 개발 전용이다: 키 없이 Clerk 의 임시 개발 인스턴스를 받아 쓴다(시연·시험용).
 * 운영 빌드에서는 무시한다.
 */
export function clerkKeyless(): boolean {
  return (
    process.env.NEXT_PUBLIC_CLERK_KEYLESS === "1" &&
    process.env.NODE_ENV !== "production" &&
    !(process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY || "").trim()
  );
}

export function clerkConfigured(): boolean {
  return !!(process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY || "").trim() || clerkKeyless();
}

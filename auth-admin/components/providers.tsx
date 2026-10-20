import { ClerkProvider } from "@clerk/nextjs";
import { clerkConfigured, clerkKeyless } from "@/lib/clerk";

const CLERK_GREEN = {
  variables: {
    colorPrimary: "#178175",
    colorPrimaryForeground: "#ffffff",
  },
  elements: {
    formButtonPrimary:
      "bg-[#178175] hover:bg-[#0c4f4a] focus:ring-[#178175] text-white",
    socialButtonsBlockButton: "border-[#178175] text-[#178175]",
  },
} as const;

export function AppProviders({ children }: { children: React.ReactNode }) {
  const pk = (process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY || "").trim();
  if (!clerkConfigured()) return children;

  return (
    <ClerkProvider
      {...(clerkKeyless() ? {} : { publishableKey: pk })}
      signInUrl="/login"
      signUpUrl="/signup"
      signInFallbackRedirectUrl="/"
      signUpFallbackRedirectUrl="/"
      appearance={CLERK_GREEN}
    >
      {children}
    </ClerkProvider>
  );
}

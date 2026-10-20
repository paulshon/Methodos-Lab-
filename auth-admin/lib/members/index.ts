/**
 * 회원 목록 — Clerk 가 정본이다.
 * 운영: Clerk 백엔드 API(CLERK_SECRET_KEY). 가입한 사람이 곧 회원이다.
 * 개발: Clerk 키가 없을 때만 MEMBERS_DEV_FILE(JSON 배열)을 읽는다. 운영 빌드에서는 이 길이 막혀 있다.
 */
import fs from "node:fs";
import { clerkClient } from "@clerk/nextjs/server";
import { clerkConfigured } from "@/lib/clerk";
import { ApiError } from "@/lib/license/core";

export type Member = {
  id: string;
  email: string;
  emailVerified: boolean;
  name: string;
  createdAt: string; // ISO
  lastSignInAt: string | null;
};

function devFile(): string | null {
  const f = (process.env.MEMBERS_DEV_FILE || "").trim();
  return f && process.env.NODE_ENV !== "production" && !(process.env.CLERK_SECRET_KEY || "").trim() ? f : null;
}

type ClerkUser = Awaited<ReturnType<Awaited<ReturnType<typeof clerkClient>>["users"]["getUser"]>>;

export function toMember(u: ClerkUser): Member {
  const primary = u.emailAddresses.find((e) => e.id === u.primaryEmailAddressId) ?? u.emailAddresses[0];
  const phone = u.phoneNumbers[0]?.phoneNumber ?? "";
  return {
    id: u.id,
    email: primary?.emailAddress ?? phone ?? "",
    emailVerified: primary?.verification?.status === "verified",
    name: [u.lastName, u.firstName].filter(Boolean).join(" ") || u.username || "",
    createdAt: new Date(u.createdAt).toISOString(),
    lastSignInAt: u.lastSignInAt ? new Date(u.lastSignInAt).toISOString() : null,
  };
}

function readDev(file: string): Member[] {
  try {
    return JSON.parse(fs.readFileSync(file, "utf-8")) as Member[];
  } catch {
    return [];
  }
}

export async function listMembers(): Promise<Member[]> {
  const dev = devFile();
  if (dev) return readDev(dev).sort((a, b) => b.createdAt.localeCompare(a.createdAt));
  if (!clerkConfigured() && !(process.env.CLERK_SECRET_KEY || "").trim()) {
    throw new ApiError(503, "clerk_not_configured", "Clerk 가 설정되지 않아 회원 목록을 읽을 수 없습니다.");
  }
  const client = await clerkClient();
  const out: Member[] = [];
  for (let offset = 0; offset < 5000; offset += 100) {
    const page = await client.users.getUserList({ limit: 100, offset, orderBy: "-created_at" });
    out.push(...page.data.map(toMember));
    if (page.data.length < 100) break;
  }
  return out;
}

export async function getMember(id: string): Promise<Member | null> {
  const dev = devFile();
  if (dev) return readDev(dev).find((m) => m.id === id) ?? null;
  try {
    const client = await clerkClient();
    return toMember(await client.users.getUser(id));
  } catch {
    return null;
  }
}

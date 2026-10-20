import { createClient, type SupabaseClient } from "@supabase/supabase-js";

const url = (process.env.NEXT_PUBLIC_SUPABASE_URL || "").trim();
const anon = (process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || "").trim();
const service = (process.env.SUPABASE_SERVICE_ROLE_KEY || "").trim();

export function supabaseConfigured(): boolean {
  return !!(url && anon);
}

export function supabaseAnon(): SupabaseClient | null {
  if (!url || !anon) return null;
  return createClient(url, anon);
}

export function supabaseAdmin(): SupabaseClient | null {
  if (!url || !service) return null;
  return createClient(url, service, { auth: { persistSession: false, autoRefreshToken: false } });
}

/** Supabase Storage public URL: NEXT_PUBLIC_SUPABASE_URL + /storage/v1/object/public/{bucket}/{path} */
export function storagePublicUrl(bucket: string, objectPath: string): string | null {
  if (!url) return null;
  const b = bucket.replace(/^\/+|\/+$/g, "");
  const p = objectPath.replace(/^\/+/, "");
  return `${url.replace(/\/$/, "")}/storage/v1/object/public/${b}/${p}`;
}

import { createReadStream, existsSync } from "node:fs";
import { stat } from "node:fs/promises";
import path from "node:path";
import { Readable } from "node:stream";
import { NextResponse } from "next/server";
import type { ArtifactId } from "@/lib/product";
import { ARTIFACTS } from "@/lib/product";
import { isValidArtifactId, resolveDownloadUrl } from "@/lib/download-url";
import { supabaseAdmin } from "@/lib/supabase";

type Params = { params: Promise<{ artifact: string }> };

async function logDownload(artifact: ArtifactId) {
  const admin = supabaseAdmin();
  if (!admin) return;
  try {
    await admin.from("download_events").insert({ artifact_id: artifact });
  } catch {
    /* table optional */
  }
}

async function localDevFile(artifact: ArtifactId): Promise<string | null> {
  const base = (process.env.LOCAL_RELEASES_DIR || "").trim();
  if (!base) return null;
  const row = ARTIFACTS.find((a) => a.id === artifact);
  if (!row) return null;
  const full = path.join(base, row.fileName);
  return existsSync(full) ? full : null;
}

export async function GET(_req: Request, { params }: Params) {
  const { artifact: raw } = await params;
  if (!isValidArtifactId(raw)) {
    return NextResponse.json({ error: "unknown artifact" }, { status: 404 });
  }

  const remote = resolveDownloadUrl(raw);
  if (remote) {
    await logDownload(raw);
    return NextResponse.redirect(remote, 302);
  }

  const local = await localDevFile(raw);
  if (local) {
    const st = await stat(local);
    const stream = createReadStream(local);
    await logDownload(raw);
    return new NextResponse(Readable.toWeb(stream) as ReadableStream, {
      headers: {
        "Content-Type": "application/octet-stream",
        "Content-Length": String(st.size),
        "Content-Disposition": `attachment; filename="${path.basename(local)}"`,
      },
    });
  }

  return NextResponse.json(
    {
      error: "download_not_configured",
      message: "Set NEXT_PUBLIC_DOWNLOAD_*_URL or Supabase Storage bucket paths. See /docs",
      artifact: raw,
    },
    { status: 503 },
  );
}

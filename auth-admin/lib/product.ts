import { resolveDownloadUrl } from "@/lib/download-url";

export const PRODUCT = {
  slug: "methodos-basic-lt",
  name: "Methodos Basic",
  edition: "AuthV1",
  version: "22.20.1-LT.V4-R20-Learn-AuthV1",
} as const;

export type ArtifactId = "win-portable" | "win-setup" | "mac-x64-dmg" | "mac-arm64-dmg";

export type ReleaseArtifact = {
  id: ArtifactId;
  label: string;
  platform: "Windows" | "macOS";
  description: string;
  fileName: string;
  envKey: string;
};

export const WIN_ARTIFACT: ReleaseArtifact = {
  id: "win-portable",
  label: "Windows 포터블",
  platform: "Windows",
  description: "설치 없이 exe 하나로 실행합니다. USB·오프라인 환경에 적합합니다.",
  fileName: "MethodosBasic-LT-4-all-v4-R20-Learn-AuthV1.exe",
  envKey: "NEXT_PUBLIC_DOWNLOAD_WIN_PORTABLE_URL",
};

export const WIN_SETUP_ARTIFACT: ReleaseArtifact = {
  id: "win-setup",
  label: "Windows 설치형",
  platform: "Windows",
  description: "설치 마법사로 설치하고 바탕화면·시작 메뉴에서 실행합니다.",
  fileName: "MethodosBasic-LT-4-all-v4-R20-Learn-AuthV1-Setup.exe",
  envKey: "NEXT_PUBLIC_DOWNLOAD_WIN_SETUP_URL",
};

export const MAC_DMG_ARTIFACTS: ReleaseArtifact[] = [
  {
    id: "mac-x64-dmg",
    label: "macOS Intel (x64)",
    platform: "macOS",
    description: "Intel Mac용 dmg 설치 파일입니다.",
    fileName: "MethodosBasic-LT_V1-Le1-6M-mac-x64.dmg",
    envKey: "NEXT_PUBLIC_DOWNLOAD_MAC_X64_DMG_URL",
  },
  {
    id: "mac-arm64-dmg",
    label: "macOS Apple Silicon (arm64)",
    platform: "macOS",
    description: "Apple Silicon Mac용 dmg 설치 파일입니다.",
    fileName: "MethodosBasic-LT_V1-Le1-6M-mac-arm64.dmg",
    envKey: "NEXT_PUBLIC_DOWNLOAD_MAC_ARM64_DMG_URL",
  },
];

export const ARTIFACTS: ReleaseArtifact[] = [WIN_ARTIFACT, WIN_SETUP_ARTIFACT, ...MAC_DMG_ARTIFACTS];

// 1~11개월 + 1년(=12개월) + 2년 + 3년
export const TERMS: { months: number; label: string }[] = [
  ...Array.from({ length: 11 }, (_, i) => ({ months: i + 1, label: `${i + 1}개월` })),
  { months: 12, label: "1년" },
  { months: 24, label: "2년" },
  { months: 36, label: "3년" },
];

export const termLabel = (m: number | null) => (m == null ? "" : m % 12 === 0 ? `${m / 12}년` : `${m}개월`);

export function artifactPublicUrl(id: ArtifactId): string | null {
  return resolveDownloadUrl(id);
}

import { redirect } from "next/navigation";

/** 이 서버는 관리자 전용이다. 회원가입·로그인은 메스도스랩 홈페이지에서 한다. */
export default function Home() {
  redirect("/admin");
}

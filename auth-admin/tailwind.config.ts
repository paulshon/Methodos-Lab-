import type { Config } from "tailwindcss";

// 색은 메스도스랩-홈페이지(css/styles.css)와 같은 청록·잉크 계열이다.
const config: Config = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}", "./lib/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        brand: { DEFAULT: "#178175", dark: "#0c4f4a", wash: "#e6f2f0" },
        ink: { DEFAULT: "#0c1b24", 2: "#243844", 3: "#5d717d" },
        line: { DEFAULT: "#dbe4e9" },
        wash: { DEFAULT: "#f5f8fa" },
      },
      fontFamily: {
        sans: ["NanumSquareNeo", "Malgun Gothic", "Apple SD Gothic Neo", "sans-serif"],
      },
    },
  },
  plugins: [],
};

export default config;

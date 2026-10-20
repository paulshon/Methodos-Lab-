# Methodos Lab Homepage

Methodos Lab 공식 홈페이지 
<<<<<<< HEAD
=======

## Stack note
- Fonts: NanumSquareNeo 
- Icons: Lucide (free icon) 

## Languages
- KO / EN / ZH switcher on every page

## Open locally
```
python -m http.server 8765
```
Then open `http://127.0.0.1:8765/`.

## Members & license keys (Clerk)
- `auth-admin/` is the member server (Next.js + Clerk + Supabase): sign-up / log-in, "My account", the admin page that issues Methodos Basic license keys to registered members, and the license API used by the desktop app. See `auth-admin/README.md`.
- Every page shows Log in / Sign up buttons once `AUTH_BASE_DEFAULT` in `js/main.js` points at the deployed member server (for local testing open `http://localhost:8765/?authBase=http://localhost:3000`).
- Desktop installers are published as GitHub Releases of this repository (`paulshon/Methodos-Lab-`).
>>>>>>> 76b3b69 (Add Clerk member server (auth-admin), login/signup buttons, Desktop download buttons)

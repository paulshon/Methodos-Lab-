-- Optional: download analytics (Supabase SQL editor)
create table if not exists public.download_events (
  id bigint generated always as identity primary key,
  artifact_id text not null,
  created_at timestamptz not null default now()
);

alter table public.download_events enable row level security;

create policy "service insert only"
  on public.download_events
  for insert
  to service_role
  with check (true);

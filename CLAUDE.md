# CLAUDE.md

## Who I am

Alex Ruiz, AI Operations Lead at Imara AI — a boutique AI consultancy in
Monterrey, Mexico. I sit between our founder's strategy work and client
delivery. I build and run the automation and agent systems behind our
engagements.

## How everything gets written

Plain and direct. No filler.

Never use these words or phrases: leverage, seamless, delve, robust,
unlock, elevate, game-changer, unleash, harness the power of, "in today's
fast-paced world."

Short sentences over long ones.

## What this project is

A personal multi-agent system.

This root session is my **Project Manager** — the one I talk to day to day.
It has its own tools and delegates anything outside its own lane to a
specialized subagent.

## House rule: delegation

When I ask about something that belongs to a subagent's job, actually
invoke that subagent and wait for its answer. Don't answer from memory.
Don't guess.

Say when you're doing it — "checking with Ops..." — instead of doing it
silently.

## What I hold directly: Google Calendar

Google Calendar is the Project Manager's own tool. No delegation hop — read
it and answer.

It's the exception on purpose. ClickUp and Drive structure carry a rulebook
— ids that can't be guessed, actions that are manual-only, folder
conventions, confidentiality — and that rulebook lives in a subagent. The
calendar doesn't. It's a lookup I'll ask for constantly, and routing it
through an agent just to read back what's on Thursday adds a hop and buys
nothing.

Scheduling questions, what's on my day, when a meeting is, finding a slot,
who's invited — answer those here.

The line: the calendar is when and who. What was *said* in a meeting is the
meetings subagent's, even when the two are about the same event. Looking up
Thursday's call is calendar. Recapping it afterward is meetings.

## Subagents currently active

- **meetings** — Plaud recordings, calls and transcripts. Recaps, decisions,
  action items, and agenda prep for an upcoming meeting built from what's
  still open. Owns meeting content only; not the calendar, not file
  storage, not tasks.

- **ops** — ClickUp and Drive structure. Tasks, workspace shape, folder
  layout, where a file lives, and current engagement status — IMARA Phase,
  Wave, Health. Owns structure and status only; not deliverables, not
  meeting content, not the calendar.

- **reports** — Status reports and client-facing deliverable documents, as
  real `.docx`/`.pptx` output. Owns what a document says and how it reads;
  not ClickUp or Drive structure. When a report needs live ClickUp status
  it says so and waits rather than guessing — that comes from ops.

More get added here as they're built.

## Routing: what goes where

- Anything about a meeting, a recording, or what was said or decided in a
  past conversation goes to the meetings subagent.

- Anything about ClickUp tasks, Drive folder structure, or current
  engagement status goes to the ops subagent.

- Anything asking for a status report or a client-facing deliverable goes to
  the reports subagent. If reports needs current status to write it, check
  with ops first and pass what you get to reports, rather than making
  reports guess.

Google Calendar is the exception above — I answer that one myself.

## House rule: memory persistence

This project runs in a cloud environment. An idle session's VM can be
reclaimed. Anything not committed to git can be lost.

So: whenever a subagent's memory file under `.claude/agent-memory/` has
changed since the last commit, commit it before I end a session. Don't wait
for the next scheduled phase commit.

If you notice uncommitted changes there, ask me: "want me to commit agent
memory before we wrap up?"

## House rule: every phase ends with a commit

Every change to any agent's file — including changes an agent makes to its
own file later — must be something I can diff and revert. Not something I
have to reconstruct from memory.

## Tooling: where the MCP connections live

Google Drive, Google Calendar, ClickUp and Plaud are **account-level
connectors** on the claude.ai account, already authorized. They are not
CLI-registered MCP servers, so they do not appear in `.mcp.json` and there
is nothing to re-authorize per session. They load automatically whenever
this environment spins up a session.

Of the four, only Google Calendar is called directly by this session. Drive
and ClickUp are reached through ops, Plaud through meetings.

`.mcp.json` is here and committed, but empty. It is the place for a
genuinely project-scoped server — one with a public HTTP endpoint that this
project needs and the account does not already provide:

    claude mcp add --scope project --transport http <name> <url>

Never put a token or secret in `.mcp.json`. It is committed to git.

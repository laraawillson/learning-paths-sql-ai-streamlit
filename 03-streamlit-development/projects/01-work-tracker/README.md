# Work Tracker — Phase 1 Plan (MVP)

This is the detailed build plan for [Path 3's](../../README.md) Phase 1: the simplest possible version of the tracker, built first, used immediately. See the path README for the full multi-phase picture (SQLite persistence, Jira ticket drafting, etc. come later) — this doc is scoped to Phase 1 only.

## Goal

A local Streamlit app with a 4-column board (**Ideas / Up Next / In Flight / Done**) that you are actually putting real tasks into by the end of this phase — including tasks for the rest of this learning curriculum. Nothing here persists to disk yet; that's Phase 2, on purpose (see "What's explicitly out of scope" below).

## Definition of Done for Phase 1

- [ ] The app runs locally with `streamlit run app.py`
- [ ] You can add a task with just a title in one action (no required fields beyond title)
- [ ] You can see all tasks grouped into the four status columns
- [ ] You can move a task to a different status
- [ ] You can edit or delete a task
- [ ] You've added at least 5 real tasks (not test data) and used it for at least a day

If any of these feel like they need a database to work, that's a sign you've drifted into Phase 2 — pull back to session state.

## Task Data Model

Keep this minimal — every extra required field is friction against low-friction capture.

| Field | Type | Required? | Notes |
|---|---|---|---|
| `id` | int or uuid | yes | Needed to identify a task for edit/move/delete |
| `title` | str | yes | The only thing required to capture an idea |
| `description` | str | no | Optional detail, empty by default |
| `status` | str | yes | One of `"Ideas"`, `"Up Next"`, `"In Flight"`, `"Done"` — default `"Ideas"` for anything quick-captured |
| `created_at` | datetime | yes | For ordering and for spotting stale items later |

Deliberately **not** in Phase 1: tags, priority, due dates, Jira ticket key. Those show up in later phases once you know you actually want them.

## App Structure

One file is enough for Phase 1 — resist splitting into modules before there's a reason to:

```
03-streamlit-development/projects/01-work-tracker/
├── README.md      (this file)
└── app.py         (the whole app)
```

## Session State Design

- `st.session_state.tasks`: a list of task dicts (or a list of small dataclass instances) matching the model above
- Initialize it once, guarded so a rerun doesn't wipe it: `if "tasks" not in st.session_state: st.session_state.tasks = [...]`
- All mutations (add/move/edit/delete) operate on this list in place, then Streamlit's rerun naturally redraws the board

## UI Layout Plan

1. **Quick-add bar at the top** — a single text input plus an "Add" button (or an `st.form` that clears on submit) that creates a new task straight into "Ideas" with just a title. This is the low-friction capture path; it should never ask for more than a title.
2. **Four columns below** (`st.columns(4)`), one per status, each showing that status's tasks as simple cards (title + a way to expand for description/edit/delete/move).
3. **Per-task controls** — keep these lightweight: a selectbox or small set of buttons to change status, an expander or small "edit" toggle for description, a delete action. Avoid a dense edit form appearing by default.
4. **Empty-column state** — a column with no tasks should say something neutral ("Nothing here yet"), not look broken.

## Suggested Build Order

Work through these as separate small commits, not one big push:

1. Static skeleton: four columns with hardcoded sample tasks, no interactivity yet
2. Quick-add: wire up the top bar to append a new task into session state and rerun
3. Move: add the status-change control on each task card
4. Edit/delete: add the ability to change a title/description or remove a task
5. Polish pass: empty-state messaging, ordering tasks by `created_at`, basic styling

## What's Explicitly Out of Scope for Phase 1

Don't build these yet — they belong to later phases in [the path README](../../README.md), and pulling them in early is exactly the kind of scope creep this project exists to avoid:
- Database persistence (Phase 2)
- Multi-page app / separate reports view (Phase 2)
- Tags, priority, due dates (add only once Phase 1 usage tells you they're needed)
- Jira ticket drafting / LLM integration (Phase 3)
- Auth, deployment, sharing with others (Phase 4+)

## 🤖 Working Through This With AI

Default to tutor mode (see [`CLAUDE.md`](../../../CLAUDE.md)) — write each step yourself first. Example prompts per build step:

- "Explain how `st.session_state` survives a rerun but not a full restart, then let me write the initialization guard myself."
- "Here's my quick-add form using `st.form` [paste]. Don't fix it — ask me what happens if I submit with an empty title."
- "I want to move a task between columns by clicking a button. Ask me what data I need to know which task and which button was clicked, before showing me a pattern."
- "Review my four-column layout code without rewriting it — what would you flag about how I'm looping over tasks per status?"

## After Phase 1

Once the Definition of Done above is checked off and you've used it for a few real days, go back to [the path README](../../README.md) and move into Phase 2 (SQLite persistence) — informed by whatever was actually annoying about the session-state version.

# Streamlit Development Learning Path — Flagship Project

Build a personal **work productivity tracker**: a Streamlit app to track work you've done, work in flight, what's up next, and ideas — designed to actually work with an ADHD brain instead of against it, with a built-in flow to turn a tracked task into a Jira ticket using an LLM and a template.

## Why this is the flagship, not just "one of the paths"

Everything else in this repo (SQL, the Tableau assistant, AI-assisted product development) is skill-building. This is the project that solves a real, present problem: keeping track of what's done, in flight, up next, and just an idea — without the tracking system itself becoming another source of overwhelm.

**Build the MVP first — before, or alongside, the SQL fundamentals — and then actually use it to track the rest of this curriculum.** Don't wait until this path comes up in sequence. The tool only pays off once it's holding your real tasks, including "practice recursive CTEs" and "parse a real Tableau workbook." Harden it later (persistence, Jira integration, refined design) once you've felt where it's annoying to use day-to-day.

## 🧠 ADHD-Aware Design Principles

These apply from the very first version, not just at the "polish" stage:

- **Low-friction capture** — adding an idea or task should take seconds. If it takes more than one screen/click to jot something down, ideas will get lost before they're written.
- **One clear next action** — the UI should always make it obvious what the *single* next thing to do is, not just a wall of everything at once.
- **Visual status without overload** — a glance at the board should tell you where things stand; avoid dense tables or too many fields per task by default.
- **Non-punitive handling of stale items** — a task sitting in "Up Next" for three weeks is information, not a failure to be guilted over. Surface staleness gently (e.g., a subtle age indicator), never with red warnings or streak-breaking language.
- **A dedicated inbox for half-formed ideas** — "Ideas" should be a true brain-dump zone: no pressure to flesh them out before they're allowed in.

## Learning Progression

### 📍 Phase 1: MVP — Build This First
- Streamlit basics, layout, and components
- Forms and widgets for quick task capture
- Session state for an in-memory Kanban board (Ideas / Up Next / In Flight / Done)
- Get it running locally and **start using it today** — even before touching SQL
- **Full build plan:** [`projects/01-work-tracker/README.md`](./projects/01-work-tracker/README.md) — data model, layout, step-by-step build order, and Definition of Done

### 📍 Ongoing: Dogfood It
- Use it daily to track SQL, Tableau, and AI-assisted-product-development work as you go through those paths
- Keep a running note (even just a task in the "Ideas" column) of friction points and feature ideas — this becomes real input for the harden phase, not speculation

### 📍 Phase 2: Harden — Persistence & Design (once real usage has surfaced pain points)
- Move from session state to SQLite (reuses **Advanced SQL** skills)
- Multi-page app: Tracker board, Ideas backlog, Weekly summary/report
- Filtering and sorting by tag, priority, project/initiative, due date
- Caching (`@st.cache_data`/`@st.cache_resource`) for DB reads
- Deliberately apply the ADHD-aware design principles above, informed by what actually annoyed you in Phase 1

### 📍 Phase 3: AI-Powered Ticket Drafting
- Designing a reusable Jira ticket template (Summary, Description, Acceptance Criteria, Priority, Labels, Story Points)
- Calling the Claude API to fill the template from a task's tracked details
- Reviewing/editing the AI-drafted ticket before it's finalized
- **First real input:** the PRD you write in [AI-Assisted Product Development](../04-ai-assisted-product-development/README.md)'s capstone ("Work Tracker v2") — turn that PRD into the first tickets this feature ever drafts

### 📍 Phase 4: Integration & Polish (optional stretch)
- Push the drafted ticket directly into Jira via the Jira REST API, and store the returned ticket key/link back on the task
- Weekly status report generator: summarize the Done column into a stand-up/1:1-ready recap
- Styling/theming, error handling, and (if ever shared beyond yourself) basic auth

## 📚 Topics Covered

### MVP
1. **Getting Started**
   - Installation and setup
   - Your first app: a 4-column Kanban board
   - Understanding the rerun execution model

2. **Core Components**
   - Text elements (title, header, subheader, write)
   - Input widgets (button, text_input, text_area, selectbox, date_input)
   - `st.form` for adding/editing a task without partial reruns
   - Columns/containers for the board layout

3. **Task Data Model**
   - Fields: title, description, status (Idea/Up Next/In Flight/Done), tags, priority, created/updated dates, linked Jira ticket key
   - Moving a task between statuses
   - Keep the required fields minimal at first — low friction beats completeness

### Harden Phase
4. **State Management**
   - Session state basics
   - Handling form state and edits
   - Callback functions for status changes

5. **Persistence**
   - SQLite schema for tasks (and a status-change history/audit table)
   - SQLAlchemy or raw `sqlite3` for reads/writes
   - Query caching

6. **Multi-page Apps**
   - Pages directory structure: Board, Backlog/Ideas, Reports
   - Shared state/config across pages

### AI-Powered Ticket Drafting
7. **LLM Integration**
   - Calling the Claude API from a Streamlit callback
   - Prompt template: task details in, structured Jira-ticket fields out
   - Displaying and editing the draft before accepting it
   - Handling API errors/timeouts gracefully in the UI

8. **Jira Integration (optional stretch)**
   - Jira REST API auth (API token)
   - Creating an issue from the accepted draft
   - Storing the returned issue key and syncing status back

9. **Reporting**
   - Summarizing completed tasks into a weekly recap (optionally LLM-assisted)
   - Simple charts: tasks completed per week, time-in-status

## 🎓 Projects

### Project 1: Work Tracker MVP ⭐ *(build this first)*
**Level:** Beginner
**Skills:** Forms, widgets, session state
Four-column board (Ideas / Up Next / In Flight / Done); add, edit, and move tasks in memory. Start using it immediately — don't polish it before putting real tasks in it. Full plan: [`projects/01-work-tracker/README.md`](./projects/01-work-tracker/README.md).

### Project 2: Persistent Tracker with SQLite
**Level:** Intermediate
**Skills:** Database integration, multi-page apps, caching
Move storage to SQLite, add a status-change history table, and split the app into Board / Backlog / Reports pages with filtering — shaped by what actually bugged you in Project 1.

### Project 3: AI Jira Ticket Drafting
**Level:** Intermediate-Advanced
**Skills:** LLM API integration, prompt templates, form review/edit flow
Add a "Draft Jira Ticket" button per task that calls Claude with a fixed template and returns an editable draft. First real test case: the "Work Tracker v2" PRD from Path 4.

### Project 4: Jira API Auto-Creation *(stretch)*
**Level:** Advanced
**Skills:** REST API integration, external service auth
Push the accepted draft into Jira via its REST API and store the resulting ticket key/link on the task.

### Project 5: Weekly Status Report Generator *(stretch)*
**Level:** Advanced
**Skills:** LLM summarization, reporting
Auto-summarize the week's completed and in-flight work into a stand-up- or 1:1-ready recap.

## 💻 Tech Stack

### Core
- **Streamlit** — web framework
- **SQLite** — task storage (via `sqlite3` or SQLAlchemy)
- **Pandas** — for reports/summary views

### Integrations
- **`anthropic` Python SDK** — LLM calls for ticket drafting and weekly summaries
- **Jira REST API** (`requests`, or the `jira` package) — optional ticket creation

## 💡 Learning Tips

1. **Build the board first, today** - Get the simplest possible Kanban UI running before adding anything else
2. **Use it before you improve it** - Real friction points are worth more than imagined ones
3. **Keep the task schema minimal at first** - Add fields only once you feel the need for them
4. **Treat the Jira template as a contract** - Keep the fields the LLM must fill fixed and explicit so drafts stay consistent
5. **Test locally first** - Always test before relying on it day-to-day

## 🤖 Working through this with AI

Default to tutor mode (see [`CLAUDE.md`](../CLAUDE.md)) — try building each piece yourself first. Example prompts:
- "Walk me through how `st.session_state` persists across reruns, then let me try building the move-task-between-columns logic myself."
- "Here's my SQLite schema for tasks and status history [paste]. Don't rewrite it — ask me questions about what I'm missing."
- "Help me design the Jira ticket prompt template by asking me what fields I actually need, instead of just giving me one."

## 📖 Resources

### Documentation
- [Streamlit Official Docs](https://docs.streamlit.io/)
- [Streamlit Multipage Apps](https://docs.streamlit.io/develop/concepts/multipage-apps)
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)

### LLM/Anthropic
- [Anthropic API Documentation](https://docs.claude.com/)
- [Claude Python SDK](https://github.com/anthropics/anthropic-sdk-python)

### Jira
- [Jira REST API Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
- [`jira` Python package](https://jira.readthedocs.io/)

### Database
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

## 🚀 Next Steps

1. Build Project 1 today, before anything else in this repo
2. Reuse **Advanced SQL** query patterns for the reporting page once you harden it
3. Reuse **AI Development** LLM-integration patterns from the Tableau Assistant for the ticket-drafting flow
4. Write the "Work Tracker v2" PRD in **AI-Assisted Product Development**, then build it here

---

**Ready to start?** Build the 4-column board with hardcoded sample tasks first, then wire up `st.form` to add real ones — and start tracking everything else in this repo with it today.

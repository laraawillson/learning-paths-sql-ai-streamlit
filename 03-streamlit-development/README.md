# Streamlit Development Learning Path

Build a personal **work productivity tracker**: a Streamlit app to track work you've done, work in flight, what's up next, and ideas — with a built-in flow to turn a tracked task into a Jira ticket using an LLM and a template.

## Learning Progression

### 📍 Level 1: Fundamentals (Week 1)
- Streamlit basics, layout, and components
- Forms and widgets for creating/editing tasks
- Session state for an in-memory Kanban board (Ideas / Up Next / In Flight / Done)
- Running the app locally

### 📍 Level 2: Intermediate (Week 2-3)
- Persisting tasks in SQLite (reuses **Advanced SQL** skills) instead of session state
- Multi-page app: Tracker board, Ideas backlog, Weekly summary/report
- Filtering and sorting by tag, priority, project/initiative, due date
- Caching (`@st.cache_data`/`@st.cache_resource`) for DB reads

### 📍 Level 3: Advanced (Week 4-5)
- LLM-powered "Draft Jira Ticket" action on any task
- Designing a reusable Jira ticket template (Summary, Description, Acceptance Criteria, Priority, Labels, Story Points)
- Calling the Claude API to fill the template from a task's tracked details
- Reviewing/editing the AI-drafted ticket before it's finalized

### 📍 Level 4: Integration & Polish (Week 6+)
- Optional: push the drafted ticket directly into Jira via the Jira REST API, and store the returned ticket key/link back on the task
- Weekly status report generator: summarize the Done column into a stand-up/1:1-ready recap
- Styling/theming, error handling, and (if ever shared beyond yourself) basic auth

## 📚 Topics Covered

### Fundamentals
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

### Intermediate
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

### Advanced
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

### Project 1: Work Tracker (Kanban MVP)
**Level:** Beginner
**Skills:** Forms, widgets, session state
Four-column board (Ideas / Up Next / In Flight / Done); add, edit, and move tasks in memory.

### Project 2: Persistent Tracker with SQLite
**Level:** Intermediate
**Skills:** Database integration, multi-page apps, caching
Move storage to SQLite, add a status-change history table, and split the app into Board / Backlog / Reports pages with filtering.

### Project 3: AI Jira Ticket Drafting
**Level:** Intermediate-Advanced
**Skills:** LLM API integration, prompt templates, form review/edit flow
Add a "Draft Jira Ticket" button per task that calls Claude with a fixed template and returns an editable draft (Summary, Description, Acceptance Criteria, Priority, Labels, Story Points).

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

1. **Build the board first** - Get the Kanban UI working in memory before adding a database
2. **Model the task schema early** - Decide task fields before wiring up persistence, since the LLM template depends on them
3. **Treat the Jira template as a contract** - Keep the fields the LLM must fill fixed and explicit so drafts stay consistent
4. **Cache wisely** - Understand what should be cached when reading from SQLite
5. **Test locally first** - Always test before relying on it day-to-day

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

After completing this path:
1. Reuse **Advanced SQL** query patterns for the reporting page
2. Reuse **AI Development** LLM-integration patterns from the Tableau Assistant for the ticket-drafting flow
3. Treat the finished tracker as the flagship **Integrated Project**

---

**Ready to start?** Build the 4-column board with hardcoded sample tasks first, then wire up `st.form` to add real ones.

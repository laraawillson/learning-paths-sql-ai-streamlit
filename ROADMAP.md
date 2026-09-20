# Learning Roadmap

A rough sequence for working through this repo — loose weeks to show how the pieces relate in time, not a schedule to fall behind on. No hour quotas, no "complete N by week X." Move at whatever pace works; the [Work Tracker](./03-streamlit-development/README.md) is where your actual day-to-day pacing and status live, not this document.

## 🗺️ Overview

```
Week 1-2:   Work Tracker MVP (build first) + AI-collaboration basics
    ↓
Week 3-4:   SQL Fundamentals (HR-flavored data)
    ↓
Week 5-6:   SQL Intermediate + AI Dev: Tableau file parsing
    ↓
Week 7-8:   AI Dev: workbook linter (real workbook) + Tracker: SQLite persistence
    ↓
Week 9-10:  SQL Advanced (org hierarchy) + AI Dev: LLM calculation explainer
    ↓
Week 11-12: AI Dev: package as CLI tool + AI-collaboration workflow practice
    ↓
Week 13-14: PRD/requirements writing (Work Tracker v2)
    ↓
Week 15-16: Tracker: AI Jira ticket drafting, built from that PRD
    ↓
Week 17+:   Optional stretch (Jira API, weekly reports, polish)
```

## 📅 Detailed Timeline

### Week 1-2: Work Tracker MVP + AI-Collaboration Basics
Build the simplest possible 4-column Kanban board (Ideas / Up Next / In Flight / Done) in Streamlit, using session state — no database yet. Start using it today to track the rest of this roadmap. Alongside it, read through [`CLAUDE.md`](./CLAUDE.md) and [Path 4's](./04-ai-assisted-product-development/README.md) prompting fundamentals so you're working in tutor mode from day one.

**Roughly aim for:**
- A working Kanban board you're actually putting real tasks into
- Comfort with `st.form`, session state, and the Streamlit rerun model
- A first attempt at structured, tutor-mode prompting

**Resources:** Streamlit Getting Started, [Path 3](./03-streamlit-development/README.md) Phase 1, [Path 4](./04-ai-assisted-product-development/README.md) Level 1

---

### Week 3-4: SQL Fundamentals (HR-Flavored Data)
SQL review, JOINs, aggregates — practiced against the HR dataset. Project 1 (E-Commerce Dashboard) is already done and stays as a reference for the workflow.

**Roughly aim for:**
- Comfortable writing JOINs and GROUP BY/HAVING queries from scratch
- Basic EXPLAIN literacy

**Resources:** PostgreSQL documentation, Mode Analytics SQL Tutorial, [Path 1](./01-advanced-sql/README.md)

---

### Week 5-6: SQL Intermediate + AI Dev: Tableau File Parsing
Window functions and CTEs on the HR dataset. Start the Tableau Workbook Assistant: parsing `.twb`/`.twbx` structure into Python objects.

**Roughly aim for:**
- A few window-function and CTE queries against the HR dataset
- A real `.twbx` workbook (see [`02-ai-development/workbooks/`](./02-ai-development/workbooks/README.md)) parsed into Python objects, validated against Tableau Desktop

**Resources:** Window Functions tutorials, Tableau Document API docs, Real Python's XML guide, [Path 1](./01-advanced-sql/README.md), [Path 2](./02-ai-development/README.md) Project 1

---

### Week 7-8: AI Dev: Workbook Linter + Tracker: SQLite Persistence
Build the rule-based linter against a real workbook. Separately, move the tracker from session state to SQLite now that you've felt where the in-memory version was annoying.

**Roughly aim for:**
- A lint report flagging unused fields, hardcoded values, and naming issues on a real workbook
- The tracker persisting tasks in SQLite across restarts

**Resources:** [Path 2](./02-ai-development/README.md) Project 2, [Path 3](./03-streamlit-development/README.md) Phase 2

---

### Week 9-10: SQL Advanced (Org Hierarchy) + AI Dev: LLM Calculation Explainer
Recursive CTEs for the org-hierarchy project. Start calling the Claude API from Python to explain calculated-field formulas in plain English with structured output.

**Roughly aim for:**
- The org-hierarchy recursive CTE (span of control, org depth)
- A working Claude API call that returns validated structured (JSON) output for at least one real calculated field

**Resources:** PostgreSQL recursive query docs, Anthropic API documentation, [Path 1](./01-advanced-sql/README.md) Project 2, [Path 2](./02-ai-development/README.md) Project 3

---

### Week 11-12: AI Dev: CLI Packaging + AI-Collaboration Workflow Practice
Package the parser/linter/LLM-reviewer into a single CLI tool. In parallel, deliberately practice the draft-then-review workflow (Path 4, Level 2) on real code from this or earlier weeks.

**Roughly aim for:**
- A `tableau-review my_workbook.twbx` CLI that runs end-to-end
- At least one real code-review practice session comparing your own review to AI's

**Resources:** `typer`/`argparse` docs, `pytest` docs, [Path 2](./02-ai-development/README.md) Project 4, [Path 4](./04-ai-assisted-product-development/README.md) Level 2

---

### Week 13-14: PRD & Requirements Writing (Work Tracker v2)
By now you've used the tracker for months. Write a real PRD for its next version based on that experience — problem statement, scope, user stories, acceptance criteria.

**Roughly aim for:**
- A written PRD for a genuine tracker enhancement
- User stories with checkable acceptance criteria, not prose

**Resources:** [Path 4](./04-ai-assisted-product-development/README.md) Level 3 and capstone

---

### Week 15-16: Tracker: AI Jira Ticket Drafting
Build the "Draft Jira Ticket" feature — a fixed template filled by Claude from task details. Use the PRD from Week 13-14 as its first real test input.

**Roughly aim for:**
- A working ticket-drafting flow, tested against the PRD you just wrote
- An editable draft review step before anything is treated as final

**Resources:** Anthropic API documentation, Jira REST API documentation, [Path 3](./03-streamlit-development/README.md) Phase 3

---

### Week 17+ (Optional Stretch)
Pick whichever of these are still interesting:
- Push drafted tickets into Jira directly via its REST API
- Weekly status-report generator from the Done column
- Refine the tracker's ADHD-aware design further, based on continued real usage
- Publish the Tableau Assistant or tracker as a public project

## 🎯 Learning Milestones

### Milestone 1: Tracker Live
- [ ] Kanban MVP built and in daily use
- [ ] Tutor-mode prompting feels natural

### Milestone 2: SQL + Tableau Parsing Competency
- [ ] Comfortable with JOINs, window functions, and CTEs
- [ ] A real workbook parsed and linted successfully

### Milestone 3: LLM Integration Working
- [ ] Structured JSON output from the Claude API, validated before use
- [ ] Tracker persists to SQLite

### Milestone 4: Planning → Building Loop Closed
- [ ] A real PRD written and broken into acceptance criteria
- [ ] That PRD turned into actual drafted tickets by the tracker

## 🗂️ Repository Organization

```
01-advanced-sql/
└── projects/                        ← e-commerce (done), org hierarchy, workforce trends

02-ai-development/
└── workbooks/                       ← local only, gitignored — real .twb/.twbx files

03-streamlit-development/            ⭐ flagship — build first, harden later

04-ai-assisted-product-development/  ← meta-skill: prompting, PRDs, code review
```


## 💡 Flexible Ordering

The sequence above is a suggestion, not a requirement. The one fixed point is: **build the tracker MVP before anything else**, since it's what you'll use to hold everything that follows. After that, SQL, AI Development, and AI-Assisted Product Development can happen in whatever order keeps you interested — they aren't strictly sequential, and Path 4's draft-then-review practice works on whatever you're building at the time.

---

**Questions?** Check the README in each directory or [`CLAUDE.md`](./CLAUDE.md) for how AI should work with you here.

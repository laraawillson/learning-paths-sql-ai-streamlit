# Learning Paths: SQL, AI Development, Streamlit & AI-Assisted Product Development

> **The vision:** build a small suite of AI-assisted tools that solve real problems in my life — most importantly, a workflow system that helps keep me organized — while leveling up SQL, Python, Streamlit, and Tableau using realistic (HR-*flavored*, not HR-*specific*) practice data. Throughout, learn to direct AI well as both a coding partner and a planning partner.

**Build the [Work Tracker MVP](./03-streamlit-development/README.md) first, before anything else here, regardless of what order you tackle the rest in.** It's the flagship project, and it only pays off once it's tracking your real work — including the rest of this curriculum.

## 🤖 Working with AI on this repo

This repo has a `CLAUDE.md` that tells any Claude session working here to default to **tutor mode**: explain, ask guiding questions, have you attempt things first, review rather than rewrite. Builder mode (AI just writes the code) is opt-in only — ask for it explicitly when you want it. See [`CLAUDE.md`](./CLAUDE.md) for the full contract.

## 📚 Repository Structure

```
├── CLAUDE.md
├── 01-advanced-sql/
│   ├── README.md
│   └── projects/
├── 02-ai-development/
│   ├── README.md
│   └── workbooks/          (local only, gitignored — real Tableau files)
├── 03-streamlit-development/
│   └── README.md            ⭐ flagship — build this first
├── 04-ai-assisted-product-development/
│   └── README.md            (meta-skill supporting the other three)
└── ROADMAP.md
```

## 🎯 Learning Paths Overview

### ⭐ Path 3: Streamlit Development — *build first*
**Skills:** Interactive apps, database integration, LLM integration — a personal work tracker with AI-drafted Jira tickets, designed around ADHD-aware workflow principles

### Path 1: Advanced SQL
**Skills:** Database design, query optimization, window functions, CTEs, recursive queries — practiced against an HR-flavored dataset (org hierarchy, workforce trends, attrition)

### Path 2: AI Development
**Skills:** Python for tooling, parsing the Tableau `.twb`/`.twbx` file format, LLM (Claude API) integration — building a Tableau Workbook Review & Assistant app, tested against real work workbooks

### Path 4: AI-Assisted Product Development
**Skills:** Prompting, AI-assisted code review/pair-programming, PRDs, user stories, acceptance criteria — the meta-skill that supports the other three, not a separate technical domain

## 🚀 Quick Start

1. **Build the Work Tracker MVP (Path 3, Project 1) first.** Get a bare-bones Kanban board running today and start using it to track everything else.
2. **Then pick any order for Paths 1, 2, and 4** — they're not strictly sequential. Use the tracker to hold whatever you're working through.
3. **Practice draft-then-review (Path 4) continuously**, on real code from whichever path you're in — not as a separate exercise done later.
4. **Harden the tracker (Path 3, later phases)** once real usage has told you what's actually annoying about it.

## 📖 Detailed Sections

- [Advanced SQL Learning Path](./01-advanced-sql/README.md)
- [AI Development Learning Path](./02-ai-development/README.md)
- [Streamlit Development Learning Path (flagship)](./03-streamlit-development/README.md)
- [AI-Assisted Product Development](./04-ai-assisted-product-development/README.md)
- [Learning Roadmap](./ROADMAP.md)
- [Working with AI on this repo](./CLAUDE.md)

## 🛠️ Technologies & Tools

**SQL:** SQLite, PostgreSQL  
**AI:** Python, `anthropic` SDK (Claude API), `tableaudocumentapi`, `lxml`  
**Streamlit:** Streamlit, Pandas, SQLAlchemy, Jira REST API  

## 📝 How to Use This Repository

1. Build the Work Tracker MVP first
2. Read the README in each learning path
3. Work through exercises in tutor mode — attempt first, then review with AI
4. Track your actual progress in the tracker, not just in these docs
5. Harden and extend projects as real usage surfaces what's missing

## 🤝 Contributing

This is a personal learning repo, but feel free to:
- Add better examples
- Fix errors or unclear explanations
- Share your learning progress

## 📚 Additional Resources

- [SQL Official Documentation](https://www.postgresql.org/docs/)
- [Anthropic API Documentation](https://docs.claude.com/)
- [Tableau Document API (Python)](https://github.com/tableau/document-api-python)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Jira REST API Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)

---

**Start learning:** Build the [Work Tracker MVP](./03-streamlit-development/README.md) today. 🎓

Questions? Check the README in each directory.

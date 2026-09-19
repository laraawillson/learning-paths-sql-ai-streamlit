# Integrated Projects: SQL + AI + Streamlit

Apply all three skills together to build complete, real tools you'll actually use for work.

## Project-Based Learning

These projects combine Advanced SQL for data, Python/LLM integration for intelligence, and Streamlit for interfaces — built around HR analytics, Tableau workbook review, and personal work tracking rather than generic datasets.

## 🚀 Project Ideas

### Project 1: Work Tracker + AI Jira Ticket Generator ⭐ *(flagship)*
**Difficulty:** Intermediate-Advanced
**Duration:** 4-6 weeks

**Components:**
- SQL: SQLite schema for tasks and status-change history; queries for the reporting page
- AI: Claude API call that turns a tracked task into a structured Jira ticket draft (Summary, Description, Acceptance Criteria, Priority, Labels, Story Points); optional weekly-summary generation
- Streamlit: Kanban board (Ideas / Up Next / In Flight / Done), multi-page app, ticket-draft review UI

**Skills Developed:**
- Designing a task data model and persisting it
- Prompt templates for structured LLM output
- Multi-page Streamlit apps with shared state
- (Stretch) Jira REST API integration to create tickets directly

This is the natural integration point for all three learning paths — see [`03-streamlit-development/README.md`](../03-streamlit-development/README.md) for the full project breakdown.

---

### Project 2: Tableau Workbook Assistant, Streamlit Front End
**Difficulty:** Intermediate-Advanced
**Duration:** 2-3 weeks

**Components:**
- SQL: optional — log review history/metrics per workbook if you want trends over time
- AI: the parser/linter/LLM-review pipeline built in [`02-ai-development/`](../02-ai-development/README.md)
- Streamlit: upload a `.twbx`, display the inventory and lint results, show the LLM's field explanations/suggestions

**Skills Developed:**
- Wrapping an existing Python tool in a web UI
- File upload handling (`st.file_uploader` for zip-based `.twbx` files)
- Presenting LLM output (explanations, suggested rewrites) in a readable, actionable layout

---

### Project 3: HR Analytics Dashboard
**Difficulty:** Intermediate
**Duration:** 2-3 weeks

**Components:**
- SQL: the org-hierarchy and workforce-trend queries from [`01-advanced-sql/`](../01-advanced-sql/README.md) (Projects 2 & 3)
- AI: optional — LLM-generated plain-English narrative summary of the current headcount/attrition numbers
- Streamlit: interactive org chart, headcount trend charts, attrition/turnover views, filters by department

**Skills Developed:**
- Turning recursive-CTE org data into a visual hierarchy
- Time-series charts from SQL window-function output
- Building a dashboard aimed at a real audience (yourself, or an HR stakeholder)

---

## 📋 Project Template

Each project should follow this structure:

```
project-name/
├── README.md           # Project overview
├── requirements.txt    # Python dependencies
├── data/
│   ├── raw/           # Original data
│   └── processed/     # Cleaned data
├── sql/
│   ├── schema.sql     # Database schema
│   └── queries.sql    # Key queries
├── ai/
│   ├── prompts.py      # LLM prompt templates
│   └── client.py       # LLM API wrapper
├── app.py             # Streamlit application
└── config.py            # Configuration
```

## 🎯 Implementation Steps (for any project)

### Phase 1: Data & SQL (Week 1)
- [ ] Identify data sources
- [ ] Design database schema
- [ ] Write SQL queries for:
  - Data extraction
  - Aggregation
  - Feature engineering
- [ ] Validate data quality

### Phase 2: AI/LLM Integration (Week 2-3)
- [ ] Define the task the AI component performs (explain, draft, summarize, classify)
- [ ] Design the prompt/template and desired output shape
- [ ] Wire up the API call and handle errors/timeouts
- [ ] Validate output quality on real examples
- [ ] Decide what, if anything, gets persisted back to SQL

### Phase 3: Streamlit Interface (Week 3-4)
- [ ] Design app layout
- [ ] Implement data loading
- [ ] Build visualizations
- [ ] Integrate the AI component into the UI
- [ ] Add user interactions
- [ ] Test thoroughly

### Phase 4: Integration & Optimization (Week 4+)
- [ ] Connect all components
- [ ] Optimize performance
- [ ] Add caching where appropriate
- [ ] Handle edge cases
- [ ] Documentation
- [ ] Deployment

## 📚 Learning Resources for Integration

### End-to-End Examples
- [Real Python Tutorials](https://realpython.com/)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)

### Architecture Patterns
- [Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)

### Deployment Guides
- [Streamlit Cloud Deployment](https://docs.streamlit.io/streamlit-cloud/)
- [Docker for Python Apps](https://docs.docker.com/)
- [Database Best Practices](https://www.postgresql.org/docs/current/tutorial.html)

## 🏆 Best Practices

### SQL Best Practices
- ✅ Use indexes for large tables
- ✅ Write efficient queries (use EXPLAIN)
- ✅ Cache query results when appropriate
- ✅ Validate data quality
- ❌ Avoid N+1 queries in loops

### AI/LLM Best Practices
- ✅ Ask for structured (JSON) output when the result will be used programmatically
- ✅ Validate LLM output before displaying or acting on it
- ✅ Keep prompt templates version-controlled alongside the code
- ✅ Handle API errors/timeouts gracefully in the UI
- ❌ Don't trust free-text output for anything downstream logic depends on
- ❌ Don't hardcode API keys — use environment variables/secrets

### Streamlit Best Practices
- ✅ Use session state for interactivity
- ✅ Cache expensive operations
- ✅ Keep the app responsive
- ✅ Validate user inputs
- ✅ Provide clear error messages
- ❌ Don't perform heavy computation on every rerun
- ❌ Don't store credentials in code

## 🚀 Deployment Checklist

Before relying on any of these day-to-day:

- [ ] Code is clean and documented
- [ ] Environment variables configured (API keys for Claude/Jira)
- [ ] Database file backed up or otherwise not a single point of failure
- [ ] Error handling implemented
- [ ] Logging enabled
- [ ] Performance tested
- [ ] Security reviewed (no secrets in the repo)
- [ ] README with setup instructions

## 💡 Tips for Success

1. **Start small** - Begin with the MVP of whichever project you pick first
2. **Iterate quickly** - Build MVP, then enhance
3. **Version control** - Use git for all projects
4. **Document as you go** - Make future you happy
5. **Use it for real** - The best signal these tools work is using them for actual work

---

**Ready to integrate?** Start with Project 1 (Work Tracker + AI Jira Ticket Generator) — it's the one you'll use immediately.

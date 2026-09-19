# Learning Roadmap

A comprehensive roadmap showing the recommended learning sequence and time commitment.

## 🗺️ Overview

```
Week 1-2: SQL Fundamentals
    ↓
Week 3-4: SQL Intermediate + AI Fundamentals
    ↓
Week 5-6: AI Intermediate + Streamlit Fundamentals
    ↓
Week 7-8: AI Advanced + Streamlit Intermediate
    ↓
Week 9-10: SQL Advanced + Streamlit Advanced
    ↓
Week 11-16: Integrated Projects
```

## 📅 Detailed Timeline

### Month 1: Foundations (Weeks 1-4)

#### Week 1-2: Advanced SQL Fundamentals
**Time Commitment:** 8-10 hours  
**Topics:**
- SQL review and core concepts
- Advanced JOIN operations
- Subqueries and nested queries
- Aggregate functions and GROUP BY

**Deliverables:**
- [ ] Complete 5 SQL exercises
- [ ] Build 1 simple query project
- [ ] Understand EXPLAIN basics

**Resources:**
- LeetCode 5 easy SQL problems
- PostgreSQL documentation
- Mode Analytics SQL Tutorial (first 3 sections)

---

#### Week 3-4: SQL Intermediate + AI Foundations
**Time Commitment:** 10-12 hours  
**Topics:**
- Window functions (ROW_NUMBER, RANK, LAG, LEAD)
- CTEs (Common Table Expressions)
- Query optimization basics
- Start: Python fundamentals for ML

**Deliverables:**
- [ ] Master 5 window function patterns
- [ ] Write 3 CTE-based queries
- [ ] Setup Python ML environment
- [ ] Review NumPy and Pandas basics

**Resources:**
- Window Functions tutorials
- CTE deep dives
- Fast.ai Practical Deep Learning (setup)
- Python for Data Science course

---

### Month 2: Intermediate Skills (Weeks 5-8)

#### Week 5-6: AI Intermediate (Python for Tooling + Tableau File Parsing)
**Time Commitment:** 12-14 hours  
**Topics:**
- Python classes/dataclasses for modeling structured data
- Parsing the `.twb`/`.twbx` file format (zip + XML)
- Extracting data sources and calculated fields
- Start: Streamlit fundamentals

**Deliverables:**
- [ ] Parse a real `.twbx` workbook into Python objects
- [ ] Export a calculated-field inventory to CSV
- [ ] Setup first Streamlit app
- [ ] Validate parsing against Tableau Desktop on the same workbook

**Resources:**
- Tableau Document API (Python) docs
- Real Python: Working with XML
- Streamlit Getting Started

**Mini-Project:** Tableau File Parser (see [02-ai-development](./02-ai-development/README.md), Project 1)

---

#### Week 7-8: Streamlit Intermediate + SQL Optimization
**Time Commitment:** 10-12 hours  
**Topics:**
- Streamlit widgets and state management
- Caching and performance
- Database integration (SQLite) for task persistence
- Query optimization and EXPLAIN ANALYZE
- Multi-page apps

**Deliverables:**
- [ ] Build the 4-column Kanban board (Ideas/Up Next/In Flight/Done) as a 2+ page Streamlit app
- [ ] Persist tasks in SQLite and implement caching correctly
- [ ] Optimize 3 slow SQL queries
- [ ] Implement a workbook linter for the Tableau Assistant (unused fields, hardcoded values, naming)

**Resources:**
- Streamlit documentation
- State management guides
- PostgreSQL/SQLite EXPLAIN
- Custom Streamlit components

**Mini-Project:** Persistent Work Tracker (see [03-streamlit-development](./03-streamlit-development/README.md), Project 2)

---

### Month 3: Advanced Techniques (Weeks 9-12)

#### Week 9-10: Advanced SQL (HR Dataset) + LLM Integration Basics
**Time Commitment:** 12-14 hours  
**Topics:**
- Recursive CTEs against the HR dataset (org hierarchy)
- Advanced indexing
- Query execution plans
- Calling the Claude API from Python (`anthropic` SDK)
- Prompt design for structured (JSON) output

**Deliverables:**
- [ ] Write the org hierarchy recursive CTE (span of control, org depth)
- [ ] Analyze 5 query execution plans
- [ ] Get a calculated-field formula explained in plain English via the Claude API
- [ ] Return and validate a structured JSON response from a prompt

**Resources:**
- PostgreSQL advanced documentation
- Anthropic API documentation
- Prompt Engineering Guide

**Mini-Project:** LLM-Powered Calculation Explainer (see [02-ai-development](./02-ai-development/README.md), Project 3)

---

#### Week 11-12: Advanced Streamlit + AI Jira Ticket Drafting
**Time Commitment:** 12-14 hours  
**Topics:**
- Custom styling and theming
- Multi-page apps with a shared SQLite database
- Designing a Jira ticket template (Summary, Description, Acceptance Criteria, Priority, Labels)
- Calling Claude to fill the template from task data
- Draft review/edit UI before accepting a ticket

**Deliverables:**
- [ ] Build a styled multi-page tracker app with database persistence
- [ ] Add the "Draft Jira Ticket" action with a fixed prompt template
- [ ] Display and allow edits to the AI-drafted ticket
- [ ] (Stretch) Push an accepted draft into Jira via its REST API

**Resources:**
- Advanced Streamlit patterns
- Anthropic API documentation
- Jira REST API documentation
- SQLAlchemy tutorials

**Mini-Project:** AI Jira Ticket Drafting (see [03-streamlit-development](./03-streamlit-development/README.md), Project 3)

---

### Months 4-5: Integration & Specialization (Weeks 13-20)

#### Week 13-16: First Integrated Project (Flagship)
**Project:** Work Tracker + AI Jira Ticket Generator  
**Time Commitment:** 20-25 hours  
**Skills Integration:**
- SQL: Task and status-history schema, reporting queries
- AI: Claude API for ticket drafting and weekly-summary generation
- Streamlit: Multi-page Kanban board with draft review UI

---

#### Week 17-18: Second Integrated Project
**Project:** Tableau Workbook Assistant, Streamlit Front End  
**Time Commitment:** 12-15 hours  
**Skills Integration:**
- AI: Reuse the parser/linter/LLM-review pipeline from Path 2
- Streamlit: File upload UI, inventory and lint-result display

---

#### Week 19-20: Third Integrated Project
**Project:** HR Analytics Dashboard  
**Time Commitment:** 12-15 hours  
**Skills Integration:**
- SQL: Org-hierarchy and workforce-trend queries from Path 1
- AI: Optional LLM-generated narrative summary of the numbers
- Streamlit: Org chart, headcount/attrition visualizations

---

## 🎯 Learning Milestones

### Milestone 1: SQL Competency ✓
**After Week 4**
- [ ] Write complex JOINs confidently
- [ ] Understand and use window functions
- [ ] Create and use CTEs
- [ ] Read basic query plans

### Milestone 2: AI Fundamentals ✓
**After Week 8**
- [ ] Parse a Tableau `.twbx` workbook into Python objects
- [ ] Implement rule-based workbook lint checks
- [ ] Call the Claude API and get structured JSON output
- [ ] Build first Streamlit app

### Milestone 3: Full Stack Skills ✓
**After Week 12**
- [ ] Advanced SQL optimization (HR dataset)
- [ ] LLM-powered calculation explanations and Jira ticket drafts
- [ ] Advanced Streamlit apps
- [ ] Database integration

### Milestone 4: Production Ready ✓
**After Week 16**
- [ ] Build complete SQL↔AI↔Streamlit pipelines
- [ ] Deploy applications
- [ ] Optimize performance
- [ ] Monitor and maintain systems

---

## 🗂️ Repository Organization

As you progress, build within the provided structure:

```
01-advanced-sql/
├── fundamentals/      ← Weeks 1-2
├── intermediate/      ← Weeks 3-4, 11-12
├── advanced/          ← Weeks 9-10
└── projects/          ← Weeks 13+

02-ai-development/
├── fundamentals/      ← Weeks 3-4
├── intermediate/      ← Weeks 5-8
├── advanced/          ← Weeks 9-10, 11-12
└── projects/          ← Weeks 13+

03-streamlit-development/
├── fundamentals/      ← Weeks 5-6
├── intermediate/      ← Weeks 7-8
├── advanced/          ← Weeks 11-12
└── projects/          ← Weeks 13+

04-integrated-projects/
└── full-stack-examples/
    ├── work-tracker-jira/        ← Weeks 13-16
    ├── tableau-assistant-ui/     ← Weeks 17-18
    ├── hr-analytics-dashboard/   ← Weeks 19-20
    └── your-projects/            ← Weeks 21+
```

---

## 📊 Time Breakdown

| Phase | Duration | Hours | Focus |
|-------|----------|-------|-------|
| SQL Foundations | 2 weeks | 18-20 | Queries, optimization (HR dataset) |
| AI Foundations | 4 weeks | 36-40 | Python, Tableau file parsing |
| Streamlit Basics | 4 weeks | 28-32 | Web apps, visualization |
| Advanced Topics | 4 weeks | 40-44 | LLM integration, optimization |
| Integration | 8 weeks | 80-100 | Full-stack projects |
| **TOTAL** | **20 weeks** | **200-240 hours** | |

---

## 🎓 Certification Paths (Optional)

After completing the core roadmap:

### Official Certifications
- **Google Cloud Professional Data Engineer**
- **Databricks Lakehouse Fundamentals**
- **Atlassian Certified Jira Administrator** (if going deeper on the Jira integration)

### Portfolio Building
- Publish the Tableau Assistant and Work Tracker as public GitHub projects
- Write up the HR analytics build for a portfolio/blog post
- Share the tools with your team for real feedback

---

## 💡 Flexible Learning Paths

### Path A: SQL-First (Data Engineering Focus)
1. SQL Fundamentals + Intermediate (4 weeks)
2. SQL Advanced (2 weeks)
3. AI Fundamentals + Intermediate (6 weeks)
4. Streamlit (3 weeks)
5. Integration (8 weeks)

**Best for:** Data engineers, database specialists

### Path B: AI-First (Tooling/LLM Focus)
1. AI Fundamentals (2 weeks)
2. AI Intermediate + SQL Basics (6 weeks)
3. AI Advanced (4 weeks)
4. Streamlit (3 weeks)
5. SQL Advanced + Integration (8 weeks)

**Best for:** Building the Tableau Assistant first, before the tracker app

### Path C: Streamlit-First (App Development Focus)
1. Streamlit Fundamentals (2 weeks)
2. SQL Fundamentals + Streamlit Intermediate (4 weeks)
3. AI Fundamentals + Streamlit Advanced (4 weeks)
4. AI Intermediate + Advanced (6 weeks)
5. Integration (8 weeks)

**Best for:** Full-stack developers, product engineers

---

## 🚀 Getting Started

1. **Choose your path:** Standard, SQL-first, AI-first, or Streamlit-first
2. **Set a schedule:** Commit 10-15 hours per week
3. **Start with Week 1:** Advanced SQL Fundamentals
4. **Build projects:** Don't just watch tutorials
5. **Track progress:** Check off deliverables each week
6. **Join community:** Find study groups, share progress

---

## 📞 Support & Resources

- **Questions?** Check the relevant README in each directory
- **Stuck?** Review the resources listed for that week
- **Want feedback?** Create pull requests with your projects
- **Contribute:** Improve these materials with PRs!

---

**Remember:** Consistency beats perfection. 10 hours per week for 20 weeks beats 40 hours once a month. Let's get started! 🚀

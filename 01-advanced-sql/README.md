# Advanced SQL Learning Path

Master complex SQL queries, database optimization, and advanced techniques for data analysis and engineering — practiced against an **HR-flavored dataset** to keep things realistic instead of generic. HR isn't a specialization goal here; it's just a relatable domain to hang the SQL on. Swap in whatever domain feels real to you if HR ever stops being interesting.

> **Dataset strategy:** Project 1 (E-Commerce Analytics Dashboard) is already complete and stays as-is — it's where JOINs, aggregates, and window function fundamentals were first practiced. Every project and exercise started from here forward uses an **HR dataset** instead of generic e-commerce/retail data, mainly because org charts and headcount trends make for more interesting recursive/window-function practice than another product catalog would.

## Learning Progression

### 📍 Level 1: Fundamentals (Week 1-2)
- SQL Basics Review
- Data Types and Constraints
- JOIN Operations Deep Dive
- Subqueries and Nested Queries
- Aggregate Functions and GROUP BY

### 📍 Level 2: Intermediate (Week 2-4)
- Window Functions (ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD)
- Common Table Expressions (CTEs)
- Query Optimization Basics
- Indexes and Performance
- Set Operations (UNION, INTERSECT, EXCEPT)

### 📍 Level 3: Advanced (Week 4-6)
- Recursive CTEs
- Advanced Window Functions
- Query Execution Plans
- Partitioning Strategies
- Advanced Indexing Techniques
- Query Tuning and EXPLAIN

## 📚 Topics Covered

### Fundamentals
1. **SQL Basics Review**
   - SELECT, WHERE, ORDER BY
   - LIMIT and OFFSET
   - DISTINCT

2. **JOINs**
   - INNER JOIN
   - LEFT/RIGHT/FULL OUTER JOINs
   - CROSS JOIN
   - Self Joins (e.g., employee-to-manager)

3. **Aggregate Functions**
   - COUNT, SUM, AVG, MIN, MAX
   - GROUP BY with HAVING
   - Filtering aggregates

### Intermediate
4. **Window Functions**
   - Ranking functions (e.g., tenure rank within department)
   - Aggregating functions over windows (e.g., rolling headcount)
   - Row numbering

5. **CTEs**
   - Simple CTEs
   - Multiple CTEs
   - Recursive CTEs (intro — reporting chains)

6. **Performance**
   - Index basics
   - Query optimization strategies
   - Execution plans

### Advanced
7. **Recursive Queries**
   - Hierarchical data (org charts, reporting lines)
   - Graph traversal
   - Path finding

8. **Complex Optimization**
   - EXPLAIN ANALYZE
   - Index strategies
   - Query rewriting
   - Statistics and planner

## 🗂️ HR Dataset Plan

A single HR SQLite database (built the same way `01-ecommerce-dashboard` was — schema + Python generator + validation script) will back Projects 2 and 3. Planned tables:

| Table | Purpose |
|---|---|
| `employees` | Core employee record — name, hire date, department, job title, status (active/terminated), `manager_id` (self-referencing FK for org hierarchy) |
| `departments` | Department names, cost center, division |
| `job_titles` | Title, job level/grade |
| `compensation_history` | Salary/comp changes over time per employee (effective date, amount, reason) |
| `performance_reviews` | Review cycle, rating, employee/manager |
| `time_off_requests` | PTO type, dates, status |
| `terminations` | Termination date, reason (voluntary/involuntary), employee |
| `job_requisitions` / `candidates` | Open reqs, posted date, filled date, stage — for time-to-fill analysis |

This mirrors the e-commerce project's structure (`schema.sql`, `generate_data.py`, `validate_data.sql`) so the workflow is familiar.

## 🎓 Projects

### Project 1: E-Commerce Analytics Dashboard ✅ *(complete)*
**Level:** Intermediate
**Skills:** JOINs, Aggregates, Window Functions
Sales performance, customer behavior, and product trend queries — already built out in [`projects/01-ecommerce-dashboard/`](./projects/01-ecommerce-dashboard/). Left untouched.

### Project 2: Org Hierarchy & Span-of-Control Analysis
**Level:** Advanced
**Skills:** Recursive CTEs, Self Joins, Window Functions
Use `employees.manager_id` to build full reporting chains with a recursive CTE. Answer questions like: how many direct and indirect reports does each manager have, what's the org depth from any employee to the CEO, which managers have the widest span of control, and which departments have the most/fewest management layers.

### Project 3: Workforce Trends & Attrition Analysis
**Level:** Advanced
**Skills:** Window Functions, Date Functions, CTEs, Query Optimization
Analyze headcount and turnover over time: month-over-month headcount trend, hires vs. terminations, voluntary vs. involuntary attrition rate by department/quarter, average tenure at termination, moving averages of headcount, and time-to-fill for open requisitions.

## 💡 Learning Tips

1. **Practice regularly** - SQL skills improve with consistent practice
2. **Use the HR dataset** - Working against realistic data makes the queries feel less like toy exercises
3. **Understand EXPLAIN** - Learn to read and optimize query plans
4. **Think in sets** - SQL is set-based, not procedural
5. **Test performance** - Always measure query performance on realistic data

## 🤖 Working through this with AI

Default to tutor mode (see [`CLAUDE.md`](../CLAUDE.md)) — try the query yourself first. Example prompts:
- "Explain recursive CTEs conceptually, then give me 2 practice problems on the org-hierarchy schema before showing me any solution."
- "Here's my attempt at the attrition window-function query [paste]. Review it without rewriting it — tell me what's wrong and ask me a question that points me at the fix."
- "Quiz me on the difference between RANK, DENSE_RANK, and ROW_NUMBER with 3 short scenarios before I write the span-of-control query."

## 📖 Resources

### Documentation
- [PostgreSQL Official Docs](https://www.postgresql.org/docs/)
- [SQL Window Functions](https://www.postgresql.org/docs/current/functions-window.html)
- [CTE Documentation](https://www.postgresql.org/docs/current/queries-with.html)

### Interactive Learning
- [LeetCode Database Problems](https://leetcode.com/problemset/database/)
- [HackerRank SQL Challenges](https://www.hackerrank.com/domains/sql)
- [Mode Analytics SQL Tutorial](https://mode.com/sql-tutorial/)

### Books
- "SQL Performance Explained" by Markus Winand
- "Advanced SQL" by Joe Celko

## 🚀 Next Steps

If you haven't already, build the [Work Tracker MVP](../03-streamlit-development/README.md) first — it's the flagship project, and using it from day one to track this SQL work is the point. From here:
1. Move to **AI Development** to apply Python skills to the Tableau Workbook Assistant
2. Use **AI-Assisted Product Development** to practice the draft-then-review workflow on these queries
3. Harden the **Streamlit** tracker later, informed by real usage

---

**Ready to start?** Begin Project 2 by designing `schema.sql` for the HR dataset.

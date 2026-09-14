# E-Commerce Analytics Dashboard - Project 1

## 📊 Project Overview

Build a comprehensive SQL analytics solution for an e-commerce platform. You'll create complex queries to analyze sales performance, customer behavior, and product trends.

**Duration:** 2-3 weeks  
**Difficulty:** Intermediate  
**Skills:** JOINs, Aggregates, Window Functions, Subqueries

## Project Progress and File Guide

### Completed Work

- Designed the SQLite schema for customers, products, orders, order items, and reviews.
- Added primary keys, foreign keys, `CHECK` constraints, and `UNIQUE` constraints.
- Built a Python data generator that creates customers, products, orders, order items, and reviews.
- Generated dates within 2026 for registrations, products, orders, and reviews.
- Ensured orders use existing customers and products.
- Calculated order totals from quantities, prices, and discounts on order items.
- Ensured review ratings and customer/product pairs satisfy the schema rules.
- Validated row counts, foreign-key relationships, dates, totals, ratings, and duplicate review pairs.

### Current Files

| File | Purpose |
|---|---|
| `schema.sql` | Creates the five database tables and defines their keys and constraints. |
| `generate_data.py` | Recreates the SQLite database and generates realistic sample data in dependency order. |
| `validate_data.sql` | Contains SQL checks for review counts, rating ranges, and duplicate customer/product reviews. |
| `ecommerce.db` | SQLite database file available for local exploration. |
| `README.md` | Documents the project goals, schema, progress, and planned analysis work. |

### Next Development Stage

The data-generation stage is complete. The next stage is to write analytical SQL queries for the business questions below, beginning with joins and aggregate functions, then progressing to CTEs and window functions.

## 🎯 Learning Objectives

By completing this project, you'll master:
- ✅ Complex JOIN operations across multiple tables
- ✅ Aggregate functions with GROUP BY and HAVING
- ✅ Window functions for ranking and trends
- ✅ Subqueries and CTEs for complex logic
- ✅ Real-world business analytics queries

## 📁 Project Structure

```
01-advanced-sql/projects/01-ecommerce-dashboard/
├── README.md                 (this file)
├── schema.sql               # Database schema
├── sample_data.sql          # Sample data to load
├── queries/
│   ├── 01_basic_joins.sql
│   ├── 02_aggregates.sql
│   ├── 03_window_functions.sql
│   ├── 04_advanced_queries.sql
│   └── 05_solutions.sql
├── exercises/
│   ├── exercise_1.md
│   ├── exercise_2.md
│   ├── exercise_3.md
│   ├── exercise_4.md
│   └── exercise_5.md
└── notes.md                 # Your learnings
```

## 📋 Database Schema

The e-commerce database has 5 main tables:

### 1. **customers**
```
- customer_id (PK)
- first_name
- last_name
- email
- country
- registration_date
- customer_segment (Premium, Standard, Basic)
```

### 2. **products**
```
- product_id (PK)
- product_name
- category
- price
- cost
- stock_quantity
- created_date
```

### 3. **orders**
```
- order_id (PK)
- customer_id (FK)
- order_date
- total_amount
- status (Completed, Pending, Cancelled)
- shipping_country
```

### 4. **order_items**
```
- order_item_id (PK)
- order_id (FK)
- product_id (FK)
- quantity
- unit_price
- discount_percent
```

### 5. **reviews**
```
- review_id (PK)
- product_id (FK)
- customer_id (FK)
- rating (1-5)
- review_text
- review_date
```

## 🔍 Key Business Questions to Answer

### Sales Analysis
1. What is the total revenue by product category?
2. What is the top-selling product in each category?
3. What is the month-over-month sales growth?
4. Which customers spent the most in the last 90 days?

### Customer Analysis
5. How many orders has each customer placed?
6. What is the average order value by customer segment?
7. How long after registration do customers make their first purchase?
8. What is the customer retention rate (repeat customers)?

### Product Analysis
9. Which products have the highest profit margin?
10. What is the average rating by product category?
11. Which products are frequently bought together?
12. What is the inventory turnover rate?

### Trend Analysis
13. What is the sales trend over time?
14. Which products are trending up/down?
15. How do seasonal patterns affect sales?

## 📚 Learning Path

### Phase 1: Setup & Understanding (Day 1-2)
- [X] Review the database schema
- [X] Load sample data
- [X] Run simple SELECT queries to explore tables
- [X] Understand data relationships

### Phase 2: Basic Queries (Day 3-5)
- [ ] Master JOIN operations (INNER, LEFT, RIGHT, FULL)
- [ ] Practice aggregate functions (SUM, COUNT, AVG, MAX, MIN)
- [ ] Learn GROUP BY and HAVING clauses
- [ ] Complete Exercise 1-2

### Phase 3: Intermediate Queries (Day 6-10)
- [ ] Subqueries in SELECT, WHERE, FROM
- [ ] CTEs (Common Table Expressions)
- [ ] Multiple aggregations
- [ ] Complete Exercise 3

### Phase 4: Advanced Queries (Day 11-15)
- [ ] Window functions (ROW_NUMBER, RANK, DENSE_RANK)
- [ ] Aggregating window functions (SUM OVER, AVG OVER)
- [ ] LAG and LEAD functions
- [ ] Complete Exercise 4-5

### Phase 5: Analysis & Optimization (Day 16-21)
- [ ] Answer all 15 business questions
- [ ] Optimize slow queries
- [ ] Create views for commonly used queries
- [ ] Document your findings

## 💡 Tips for Success

1. **Start simple** - Begin with basic SELECT queries before complex JOINs
2. **Use aliases** - Make queries readable with short table aliases
3. **Test incrementally** - Build queries piece by piece
4. **Use EXPLAIN** - Understand query execution plans
5. **Comment your code** - Document what each query does
6. **Verify results** - Check if answers make business sense

## 🚀 Getting Started

1. **Setup PostgreSQL** or SQLite locally
2. **Create the schema** - Run `schema.sql`
3. **Load sample data** - Run `sample_data.sql`
4. **Review the data** - Explore with basic queries
5. **Start with exercises** - Work through each exercise
6. **Write your own queries** - Answer the business questions

## 📖 Next Steps

After completing this project:
- Move to **Project 2: Hierarchical Data Analysis** for recursive CTEs
- Start **AI Development** to work with this data
- Build a **Streamlit dashboard** to visualize these insights

---

**Ready to begin?** Start with the schema and sample data, then work through the exercises in order!

**Estimated Time Commitment:**
- Schema & Setup: 30 min
- Exercises: 10-12 hours
- Business Questions: 4-6 hours
- Optimization: 2-3 hours
- **Total: 16-22 hours over 2-3 weeks**


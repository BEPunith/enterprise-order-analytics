# Enterprise Order Analytics Platform

## Project Overview
End-to-end batch data engineering pipeline
built on real-world e-commerce data for NovaCart,
a e-commerce company.

## Architecture
CSV Files → MySQL → PySpark → Transfomation → Analytics

## Tech Stack
- MySQL — source database
- Python — ETL scripts
- Apache PySpark — large scale processing
- Apache Airflow — pipeline orchestration
- Docker — containerization
- Git/GitHub — version control
- Databricks — Delta Lake + SQL analytics

## Business Questions Answered
- Which products generate the most revenue?
- Which states have the highest order volume?
- Which sellers delay orders most?
- Which customers are repeat buyers?
- Which payment methods are most popular?
- How long does delivery actually take?
- Which categories get the worst reviews?

## Schema & Data Quality
## Day 2 — Schema & Data Quality

- Mapped the 9-table Olist schema: customers → orders → order_items → products/sellers,
  plus payments, reviews, geolocation, and category translation.
- Documented primary keys and foreign keys (including composite keys on order_items and order_payments).
- Verified row counts across all 9 tables — matches source CSVs.
- Added `data_verification_and_quality_checks.sql` — NULL checks, duplicate checks,
  and referential integrity checks between tables.
- Data confirmed clean and ready for SQL analysis.
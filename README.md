# 🐦 Ducks Unlimited University Chapters ETL Pipeline

## 📌 Overview

This project is an end-to-end **data engineering pipeline** that extracts university chapter data from the Ducks Unlimited ArcGIS API, transforms it using Python and dbt, and loads it into Google BigQuery for analytics.

The pipeline demonstrates:

- ETL development in Python
- Data warehousing in BigQuery
- Data modeling using dbt
- Data quality testing
- Reproducible data pipeline design

---

## 🏗 Architecture

```text
ArcGIS API
    ↓
Python ETL (Extract + Transform)
    ↓
BigQuery (Raw Table)
    ↓
dbt (Staging + Marts + Tests)
    ↓
Analytics-ready tables
```

🧰 Tech Stack
Python 3.10
pandas / requests
Google BigQuery
dbt (data build tool)
SQL
GitHub

📊 Data Source
Ducks Unlimited University Chapters API (ArcGIS REST API)

Fields used:

chapter_id
chapter_name
city
state
latitude
longitude

🚀 How to Run the Project

1. Clone repository

git clone <repo-url>
cd ducks-etl-pipeline

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate # Windows

3. Install dependencies
   pip install -r requirements.txt

4. Set Google credentials
   set GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account.json"

5. Run ETL pipeline
   python -m etl.main

6. Run dbt models
   cd dbt_project
   dbt run

7. Run dbt tests
   dbt test

🧱 dbt Data Models
Staging Layer
stg_chapters
Cleans raw BigQuery data
Removes duplicates
Standardises schema
Mart Layer
dim_chapters
Business-ready dataset
Filtered and structured for analytics

🧪 Data Quality Tests

Implemented dbt tests:

not_null on chapter_id, city, state
unique constraint on chapter_id

🔄 Pipeline Flow
1.Extract data from ArcGIS API
2.Transform and clean data using Python
3.Load raw data into BigQuery
4.Transform using dbt (staging + marts)
5.Validate using dbt tests

⚠️ Assumptions
API data is stable and accessible
Duplicate chapter IDs handled in staging layer
BigQuery dataset is pre-created
Service account has required permissions

📈 Future Improvements
Incremental loading in dbt
CI/CD using GitHub Actions
Data orchestration with Airflow / Cloud Composer
Data quality dashboards
Partitioning in BigQuery for performance

👨‍💻 Author

Data Engineering Assessment Project

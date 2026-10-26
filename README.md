# Weather Data Pipeline

A lightweight Python-based ETL (Extract, Transform, Load) data pipeline that ingests raw weather API JSON payloads, cleans and normalizes schema attributes using Pandas, and loads structured telemetry into a PostgreSQL database.

---

## Architecture Overview

data/raw/ (*.json)  --->  src/transform.py  --->  data/processed/weather_cleaned.csv  --->  src/load.py  --->  PostgreSQL

---

## Key Features

* Data Extraction: Parses raw JSON weather telemetry files dynamically from source directories.
* Data Transformation: 
  * Cleans missing and null attributes (city, temperature).
  * Converts Unix epoch timestamps into standard Pandas datetime objects.
  * Handles record deduplication across unique city and timestamp pairs.
* Database Loading: Writes structured data directly into a relational PostgreSQL database table using SQLAlchemy and Pandas.

---

## Repository Structure

weather-data-pipeline/
├── data/
│   ├── raw/                  # Ingested raw JSON weather files
│   └── processed/            # Cleaned CSV output (weather_cleaned.csv)
├── src/
│   ├── transform.py          # Data cleaning and normalization script
│   └── load.py               # PostgreSQL database loading script
├── .gitignore
└── README.md

---

## How to Run

1. Transform Raw Data:
   python src/transform.py

2. Load Data into PostgreSQL:
   python src/load.py
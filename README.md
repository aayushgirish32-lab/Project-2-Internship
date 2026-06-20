# Week 1 — Data Cleaning & Preprocessing

## Project Title

Hospitality Booking Analytics Project

---

## Objective

The objective of Week 1 was to prepare raw hospitality booking data for further analysis by performing data cleaning, preprocessing, and feature engineering.

This phase ensures that the dataset becomes reliable, consistent, and ready for exploratory analysis and dashboard creation.

---

## Dataset

Dataset Used:
hotel_bookings.csv

Source:
Hospitality Booking Dataset

---

## Tools Used

* Python
* Pandas
* VS Code
* Git & GitHub

---

## Folder Structure

```text
Hospitality_project/
│
├── data/
│   ├── raw/
│   │   └── hotel_bookings.csv
│   │
│   └── cleaned/
│       └── clean_hotel.csv
│
├── notebooks/
├── clean_data.py
├── README.md
```

---

## Week 1 Tasks Completed

### 1. Dataset Loading

Loaded raw CSV dataset using Pandas.

### 2. Duplicate Removal

Removed duplicate records to improve data quality.

### 3. Missing Value Handling

Handled missing values for:

* agent
* company
* country
* children

Applied:

* Numerical → replaced with 0
* Categorical → replaced with "Unknown"

### 4. Feature Engineering

Created new column:

```text
total_stay
```

Formula:

```text
stays_in_weekend_nights + stays_in_week_nights
```

### 5. Basic Data Analysis

Calculated:

* Cancellation Rate
* Average ADR
* Missing Values Summary

### 6. Export Clean Dataset

Generated cleaned dataset:

```text
data/cleaned/clean_hotel.csv
```

---

## Sample Results

Cancellation Rate:
≈ 27.5%

Average ADR:
≈ 106.34

---

## Key Learning Outcomes

* Data cleaning techniques
* Missing value treatment
* Feature engineering
* CSV handling using Pandas
* Project structure organization
* Git version control workflow

---

## Challenges Faced

* Python environment setup
* File path issues
* Data export validation
* Git branch management

---

## Conclusion

Week 1 successfully transformed raw hospitality booking data into a structured and cleaned dataset ready for exploratory analysis and business intelligence reporting in subsequent project phases.

Status:
Completed ✅

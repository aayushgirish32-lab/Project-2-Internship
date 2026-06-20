# Hospitality Booking Analytics Project

---

# Project Overview

The Hospitality Booking Analytics Project focuses on transforming raw hotel booking data into meaningful business insights through data cleaning, preprocessing, exploratory analysis, and visualization.

The project aims to support business decision-making by understanding customer behavior, booking trends, pricing performance, and cancellation patterns.

---

# Project Objectives

* Clean and preprocess raw hospitality data
* Handle missing values and duplicates
* Create derived business features
* Perform exploratory data analysis (EDA)
* Generate business insights using visualizations
* Prepare data for dashboard and predictive analytics

---

# Tools & Technologies

* Python
* Pandas
* Matplotlib
* Seaborn
* Jupyter Notebook
* VS Code
* Git & GitHub

---

# Project Folder Structure

```text
Hospitality_project/

├── data/
│   ├── raw/
│   │   └── hotel_bookings.csv
│   │
│   └── cleaned/
│       └── clean_hotel.csv
│
├── notebooks/
│   └── eda_analysis.ipynb
│
├── screenshots/
│   └── week2/
│
├── clean_data.py
├── README.md
└── requirements.txt
```

---

# WEEK 1 — Data Cleaning & Preprocessing

## Objective

Prepare raw booking data for analysis by improving data quality and creating structured datasets.

---

## Tasks Completed

### Dataset Loading

Loaded:

```text
hotel_bookings.csv
```

using Pandas.

---

### Duplicate Removal

Removed duplicate rows to improve reliability.

---

### Missing Value Treatment

Handled missing values for:

* agent
* company
* country
* children

Methods used:

* Numerical → replaced with 0
* Categorical → replaced with "Unknown"

---

### Feature Engineering

Created:

```text
total_stay
```

Formula:

```text
stays_in_weekend_nights + stays_in_week_nights
```

---

### Basic Analysis

Generated:

* Missing value summary
* Cancellation rate
* Average ADR

---

## Week 1 Output

Generated cleaned dataset:

```text
data/cleaned/clean_hotel.csv
```

---

## Results

Cancellation Rate:

≈ 27.5%

Average ADR:

≈ 106.34

---

# WEEK 2 — Exploratory Data Analysis (EDA)

## Objective

Analyze booking patterns and convert cleaned data into actionable business insights.

---

## Tasks Completed

### Data Exploration

Performed:

* Dataset inspection
* Statistical summary
* Variable analysis

---

### Visualization Development

Created business visualizations.

---

### Chart 1 — Booking Cancellation Distribution

Purpose:

Understand cancellation behavior.

Business Insight:

Identified cancellation trends among bookings.

---

### Chart 2 — Average Daily Rate Distribution

Purpose:

Understand pricing behavior.

Business Insight:

Observed booking price concentration.

---

### Chart 3 — Lead Time vs Cancellation

Purpose:

Analyze booking timing impact.

Business Insight:

Long lead times showed greater cancellation tendency.

---

### Chart 4 — Correlation Heatmap

Purpose:

Study relationships between variables.

Business Insight:

Helped identify dependency among booking metrics.

---

## Visual Outputs

Saved inside:

```text
screenshots/week2/
```

Examples:

```text
cancellation_distribution.png
adr_distribution.png
leadtime_vs_cancel.png
correlation_heatmap.png
```

---

# Key Learnings

* Data preprocessing
* Missing value handling
* Feature engineering
* Exploratory Data Analysis
* Data visualization
* Business storytelling
* Analytical thinking

---

# Challenges Faced

* Python environment setup
* Jupyter Notebook configuration
* Dataset path handling
* Visualization rendering
* Git branch management

---

# Conclusion

Week 1 and Week 2 successfully converted raw hospitality booking data into a clean and analysis-ready dataset while generating business insights through visual exploration.

This phase establishes the foundation for predictive analytics and dashboard development.

Project Status:

✅ Week 1 Completed
✅ Week 2 Completed

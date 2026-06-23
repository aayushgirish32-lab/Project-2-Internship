# Hospitality Booking Analytics Project

---

# Project Overview

The Hospitality Booking Analytics Project focuses on transforming raw hotel booking data into business insights through cleaning, exploratory analysis, and predictive analytics.

The project aims to analyze customer booking behavior, pricing trends, booking cancellations, and generate business intelligence for decision-making.

---

# Project Objectives

* Clean and preprocess hospitality data
* Handle missing values and inconsistencies
* Create business features
* Perform Exploratory Data Analysis (EDA)
* Generate business insights
* Develop a predictive cancellation model

---

# Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
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
│   ├── eda_analysis.ipynb
│   └── model.ipynb
│
├── screenshots/
│
├── model.pkl
├── clean_data.py
├── README.md
└── requirements.txt
```

---

# WEEK 1 — Data Cleaning & Preprocessing

## Objective

Prepare raw hospitality data for analysis.

---

## Tasks Completed

### Dataset Loading

Loaded:

hotel_bookings.csv

---

### Data Cleaning

Completed:

* Duplicate removal
* Missing value treatment
* Data validation

Handled:

* agent
* company
* country
* children

---

### Feature Engineering

Created:

total_stay

Formula:

stays_in_weekend_nights + stays_in_week_nights

---

### Week 1 Output

Generated:

data/cleaned/clean_hotel.csv

---

## Results

Cancellation Rate:

≈ 27.5%

Average ADR:

≈ 106.34

---

# WEEK 2 — Exploratory Data Analysis (EDA)

## Objective

Explore booking patterns and generate business insights.

---

## Analysis Performed

### Booking Cancellation Distribution

Purpose:

Understand customer cancellation behavior.

---

### Average Daily Rate Distribution

Purpose:

Study hotel pricing patterns.

---

### Lead Time vs Cancellation

Purpose:

Identify whether earlier bookings increase cancellation.

---

### Correlation Heatmap

Purpose:

Understand relationships between booking variables.

---

## Insights

* Significant booking cancellation patterns identified
* Pricing variation observed
* Lead time influenced cancellations
* Feature relationships supported prediction modeling

---

## Outputs

Generated:

* Cancellation Distribution
* ADR Distribution
* Lead Time Analysis
* Correlation Heatmap

Saved inside:

screenshots/week2/

---

# WEEK 3 — Predictive Analytics (Cancellation Prediction)

## Objective

Build a machine learning model to predict booking cancellation probability.

---

## Tasks Completed

### Dataset Preparation

Selected features:

* lead_time
* adr
* total_stay
* adults
* children

Target Variable:

is_canceled

---

### Data Splitting

Performed:

* Training Dataset
* Testing Dataset

Split Ratio:

80 : 20

---

### Model Development

Algorithm Used:

Logistic Regression

Implemented:

* Model Training
* Prediction
* Evaluation

---

### Model Evaluation

Metrics Generated:

* Accuracy
* Precision
* Recall
* Classification Report

---

### Feature Importance

Created visualization showing contribution of variables.

Business Understanding:

* Lead Time strongly influenced cancellation probability
* Pricing patterns contributed to customer behavior

---

### Model Export

Generated:

model.pkl

---

## Week 3 Deliverables

Created:

```text
notebooks/model.ipynb
model.pkl
screenshots/week3/
```

---

# Key Learning Outcomes

* Data Cleaning
* Feature Engineering
* EDA
* Business Storytelling
* Machine Learning
* Logistic Regression
* Model Evaluation
* Predictive Analytics

---

# Challenges Faced

* Jupyter setup
* File path handling
* Dataset loading
* Git branch management
* Model execution

---

# Conclusion

Weeks 1–3 successfully transformed hospitality booking data into a structured analytics workflow.

The project progressed from:

Raw Data
↓
Cleaning
↓
EDA
↓
Predictive Modeling

This prepared the project for dashboarding and final business reporting.

Project Status:

✅ Week 1 Completed
✅ Week 2 Completed
✅ Week 3 Completed

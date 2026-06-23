# Hotel Booking Analytics Project

---

# Project Overview

The Hotel Booking Analytics Project focuses on transforming raw hotel booking data into business insights through cleaning, exploratory analysis, and predictive analytics.

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
Project Status:

✅ Week 1 Completed

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

Project Status:

✅ Week 2 Completed

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

✅ Week 3 Completed

# Week 4 — Dashboard Development & Business Reporting

# Objective

The objective of Week 4 was to transform analytical findings and predictive outputs into an interactive business dashboard and generate actionable insights for decision-making.

This phase focused on converting technical analysis into a business-friendly reporting experience.

---

# Tools & Technologies

* Power BI
* Python
* Pandas
* Jupyter Notebook
* Scikit-Learn
* Git & GitHub

---

# Dashboard Objective

The dashboard was designed to provide a visual summary of:

* Booking performance
* Cancellation trends
* Pricing behavior
* Customer segments
* Business KPIs

The dashboard enables stakeholders to monitor booking activities and identify business opportunities.

---

# Data Source

Input Dataset:

```text
clean_hotel.csv
```

Source:

Generated during Week 1 cleaning and used throughout analytical stages.

---

# Dashboard Components

## KPI Section

Created KPI cards for:

### Total Bookings

Displays total booking volume.

### Cancellation Rate

Shows percentage of cancelled bookings.

### Average Daily Rate (ADR)

Displays average booking price.

### Average Stay

Shows average customer stay duration.

---

## Dashboard Visualizations

### Monthly Booking Trend

Purpose:
Identify seasonal demand and booking fluctuations.

---

### Cancellation Distribution

Purpose:
Analyze cancellation behavior.

---

### Market Segment Analysis

Purpose:
Understand contribution of customer segments.

---

### Average ADR by Customer Type

Purpose:
Compare pricing trends among customer groups.

---

## Interactive Filters

Implemented slicers for:

* Hotel Type
* Country
* Customer Type
* Booking Month
* Market Segment

---

# Business Insights Generated

* Booking demand varied across periods.
* Cancellation trends influenced business performance.
* Customer segments showed different booking behaviors.
* Pricing variation revealed revenue opportunities.
* Dashboard improved monitoring and decision support.

---

# Dashboard Deliverables

Generated:

```text
dashboard/
hospitality_dashboard.pbix
```

Screenshots saved:

```text
screenshots/week4/
```

---

# Business Recommendations

* Reduce cancellation through targeted retention strategies.
* Optimize pricing during high-demand periods.
* Improve customer engagement for selected segments.
* Monitor booking behavior continuously.

---

# Challenges Faced

* Power BI dashboard alignment
* Data relationship setup
* Visualization formatting
* Dashboard optimization

---

# Learning Outcomes

* Dashboard Design
* KPI Development
* Business Reporting
* Interactive Filtering
* Data Storytelling
* Business Intelligence

---

# Conclusion

Week 4 successfully transformed analytical outputs into a professional dashboard and reporting solution.

The dashboard converted raw hospitality booking information into actionable business insights for decision-making.

Project Status:

✅ Dashboard Completed
✅ Business Reporting Completed
✅ Week 4 Completed

# Week 4 — Dashboard Development, Reporting & Final Documentation

## Project Title

Hotel Booking Analytics Project

---

# Objective

The objective of Week 4 was to transform analytical outputs into business reporting by developing an interactive Power BI dashboard and preparing final project documentation.

This phase focused on presenting insights in a clear and decision-oriented format.

---

# Tools & Technologies Used

* Power BI
* Python
* Pandas
* Jupyter Notebook
* Scikit-Learn
* Git & GitHub
* Microsoft Word

---

# Dashboard Development

## Purpose

The dashboard was created to provide a business-friendly view of hospitality booking performance and support decision-making.

The dashboard combines KPIs, trends, filters, and visual analytics.

---

# Dashboard Components

## KPI Cards

Created the following KPIs:

### Total Bookings

Displays overall booking volume.

### Cancellation Rate

Shows percentage of cancelled reservations.

### Average Daily Rate (ADR)

Displays average booking revenue.

### Average Stay Duration

Shows average customer stay length.

---

## Dashboard Visualizations

### Monthly Booking Trend

Purpose:
Track seasonal booking demand.

---

### Cancellation Distribution

Purpose:
Understand customer cancellation behavior.

---

### Market Segment Analysis

Purpose:
Analyze contribution of booking segments.

---

### ADR by Customer Type

Purpose:
Compare pricing performance.

---

# Interactive Features

Added filters for:

* Hotel Type
* Country
* Booking Month
* Customer Type
* Market Segment

Implemented:

* Cross filtering
* Dynamic visuals
* Interactive exploration

---

# Business Insights

Insights identified from dashboard:

1. Booking demand changed across periods.

2. Higher lead time influenced cancellation probability.

3. Customer segments showed different booking behavior.

4. Pricing trends revealed business opportunities.

5. Dashboard improved monitoring efficiency.

---

# Report Preparation

Final project documentation was created to summarize the complete analytics workflow.

Included sections:

* Introduction
* Dataset Description
* Week-wise Progress
* Dashboard Explanation
* Business Insights
* Challenges
* Conclusion

---

# Report Deliverables

Generated Reports:

```text id="r0d8s7"
reports/



├── Hotel_Booking_Analytics_Final_Report.docx


```

---

# Dashboard Deliverables

Generated Files:

```text id="tzhk3o"
dashboard/

└── hospitality_dashboard.pbix
```

Screenshots:

```text id="w5zk4k"
screenshots/

└── week4/
    └── dashboard_final.png
```

---

# Challenges Faced

* Dashboard formatting
* Report generation
* Git merge handling
* Screenshot integration
* Repository organization

---

# Learning Outcomes

* Dashboard Design
* KPI Development
* Business Reporting
* Data Storytelling
* Documentation
* Git Workflow

---

# Conclusion

Week 4 successfully converted technical analytics outputs into a professional reporting and dashboard solution.

The project delivered a complete end-to-end hospitality analytics workflow including analysis, prediction, visualization, reporting, and version control.

Status:

✅ Dashboard Completed
✅ Reports Completed
✅ Documentation Completed
✅ GitHub Updated
✅ Week 4 Completed
✅ project completed

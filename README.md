# EL_task_2
# Titanic Dataset - Exploratory Data Analysis

## Overview
This repository contains a comprehensive exploratory data analysis of the famous Titanic dataset. The analysis examines passenger demographics, survival patterns, and relationships between various features to understand the factors that influenced survival during the Titanic disaster.

## Dataset
- **Source**: Titanic-Dataset.csv

## Analysis Performed

### 1. Data Overview & Quality Assessment
- Dataset shape and structure analysis
- Column information and data types
- Descriptive statistics for all features
- Missing value identification and quantification
- Median calculations for numerical features

### 2. Univariate Analysis
**Distribution Analysis** for numerical features:
- Age distribution
- Fare distribution  
- SibSp (siblings/spouses) distribution
- Parch (parents/children) distribution

**Outlier Detection** using box plots for all numerical variables to identify extreme values and potential data quality issues.

### 3. Correlation Analysis
- Correlation matrix heatmap showing relationships between survival and numerical features
- Identified key correlations between:
  - Survival and passenger features
  - Inter-feature relationships

### 4. Bivariate Analysis
**Pairplot Analysis**: Comprehensive pairwise relationships between all numerical features, colored by survival status to reveal patterns.

### 5. Survival Pattern Analysis
**Categorical Analysis**:
- Survival rate by gender
- Survival rate by passenger class
- Combined analysis of class and gender effects

**Continuous Variable Analysis**:
- Age distribution by survival status (violin plots)
- Fare distribution by survival status (box plots)

## 6. Multi-dimensional Analysis
- Cross-tabulation of survival rates by passenger class and gender
- Stacked bar chart visualization of survival patterns across class-gender combinations





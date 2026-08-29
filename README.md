# prodigy_task2_DS
Exploratory Data Analysis of the Titanic dataset using Python, Pandas, and Matplotlib as part of my Data Science Internship at Prodigy InfoTech.
# Task 2 - Exploratory Data Analysis on Titanic Dataset

## 📌 Overview

This project is part of my **Data Science Internship at Prodigy InfoTech**.

The objective of this task is to perform **Data cleaning and Exploratory Data Analysis (EDA)** on the Titanic dataset. The analysis focuses on cleaning the data, understanding passenger characteristics, exploring relationships between variables, and identifying patterns related to passenger survival.

## 🎯 Objectives

- Understand the structure of the Titanic dataset
- Identify and handle missing values
- Check for duplicate records
- Perform exploratory data analysis
- Analyze passenger survival patterns
- Explore relationships between survival and gender
- Explore relationships between survival and passenger class
- Analyze the age distribution of passengers
- Create visualizations to present the findings

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Jupyter Notebook / VS Code

## 📂 Dataset

The Titanic dataset contains information about passengers, including:

| Column | Description |
|---|---|
| PassengerId | Unique identification number of the passenger |
| Survived | Survival status (0 = No, 1 = Yes) |
| Pclass | Passenger class (1st, 2nd, or 3rd) |
| Name | Passenger name |
| Sex | Passenger gender |
| Age | Passenger age |
| SibSp | Number of siblings/spouses aboard |
| Parch | Number of parents/children aboard |
| Ticket | Ticket number |
| Fare | Passenger fare |
| Cabin | Cabin number |
| Embarked | Port of embarkation |

## 🧹 Data Cleaning

The following data cleaning steps were performed:

1. Loaded the dataset using Pandas.
2. Inspected the dataset structure and column names.
3. Checked for missing values.
4. Checked for duplicate records.
5. Filled missing `Age` values using the median age.
6. Filled missing `Embarked` values using the most frequently occurring value.
7. Removed the `Cabin` column because it contained a large number of missing values.
8. Verified the dataset again after cleaning.

The original dataset was not modified. All cleaning operations were performed on the DataFrame in Python.

## 📊 Exploratory Data Analysis

The following analyses and visualizations were performed:

### 1. Titanic Survival Distribution

This visualization compares the number of passengers who survived with those who did not survive.

**Observation:**  
Out of 891 passengers, 342 survived and 549 did not survive. Therefore, the number of passengers who did not survive was higher than the number who survived.

### 2. Survival by Gender

This visualization compares the number of male and female passengers who survived.

**Observation:**  
233 female passengers survived compared with 109 male passengers, showing that the number of female survivors was considerably higher.

### 3. Survival Rate by Gender

This visualization compares the survival percentage of male and female passengers.

**Observation:**  
Approximately 74% of female passengers survived, compared with approximately 19% of male passengers. This shows a significant difference in survival rates between the two genders.

### 4. Survival Rate by Passenger Class**

This visualization compares survival rates across 1st, 2nd, and 3rd class passengers.

**Observation:**  
First-class passengers had the highest survival rate at approximately 63%, followed by second-class passengers at approximately 47%. Third-class passengers had the lowest survival rate at approximately 24%.

### 5. Age Distribution

This histogram shows the distribution of passenger ages.

### Observation:
A large proportion of passengers were approximately between 20 and 40 years old, while fewer passengers were very young or elderly.

### 🔍 Key Findings

- More passengers did not survive than survived.
- Female passengers had a significantly higher survival rate than male passengers.
- First-class passengers had the highest survival rate.
- Third-class passengers had the lowest survival rate.
- Most passengers were between approximately 20 and 40 years old.
- Gender and passenger class showed noticeable relationships with survival.

## Conclusion

This task helped me gain practical experience in data cleaning, exploratory data analysis, data visualization, and interpreting real-world datasets.





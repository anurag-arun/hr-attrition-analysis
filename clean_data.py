import pandas as pd
import numpy as np

# 1. Load Raw Data
raw_path = 'data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv'
df = pd.read_csv(raw_path)
print(f"Original Data Shape: {df.shape}")

# 2. Drop Redundant / Zero-Variance Columns
# 'EmployeeCount', 'StandardHours', 'Over18' have only 1 unique value across all rows
# 'EmployeeNumber' is kept as Primary Key; drop 'EmployeeId' if present
cols_to_drop = ['EmployeeCount', 'StandardHours', 'Over18']
df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])

# 3. Standardize Binary Columns
df['Attrition_Numeric'] = df['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)
df['OverTime_Numeric'] = df['OverTime'].apply(lambda x: 1 if x == 'Yes' else 0)

# 4. Feature Engineering: Analytical Buckets (Crucial for Dashboards & SQL)

# A. Tenure Cohorts
def categorize_tenure(years):
    if years <= 1:
        return '0-1 Years'
    elif years <= 3:
        return '2-3 Years'
    elif years <= 7:
        return '4-7 Years'
    else:
        return '8+ Years'

df['TenureBand'] = df['YearsAtCompany'].apply(categorize_tenure)

# B. Age Groups
def categorize_age(age):
    if age < 25:
        return '<25'
    elif age <= 34:
        return '25-34'
    elif age <= 44:
        return '35-44'
    elif age <= 54:
        return '45-54'
    else:
        return '55+'

df['AgeBand'] = df['Age'].apply(categorize_age)

# C. Monthly Income Quartile Buckets
df['IncomeBand'] = pd.qcut(
    df['MonthlyIncome'], 
    q=4, 
    labels=['Low (Q1)', 'Lower-Mid (Q2)', 'Upper-Mid (Q3)', 'High (Q4)']
)

# D. Map Survey Scaled Ratings to Readable Text Labels
rating_map = {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'}
df['JobSatisfaction_Label'] = df['JobSatisfaction'].map(rating_map)
df['EnvSatisfaction_Label'] = df['EnvironmentSatisfaction'].map(rating_map)
df['WorkLifeBalance_Label'] = df['WorkLifeBalance'].map({1: 'Bad', 2: 'Good', 3: 'Better', 4: 'Best'})

# 5. Export Cleaned Dataset
output_path = 'data/processed/hr_cleaned.csv'
df.to_csv(output_path, index=False)

print(f"Data Cleaned Successfully!")
print(f"Processed Data Shape: {df.shape}")
print(f"Saved to: {output_path}")

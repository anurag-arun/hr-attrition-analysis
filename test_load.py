import pandas as pd

file_path = "data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"

try:
    df = pd.read_csv(file_path)
    print("SUCCESS: Dataset loaded successfully!")
    print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print("\nAttrition breakdown:")
    print(df['Attrition'].value_counts())
except Exception as e:
    print(f"Error loading file: {e}")

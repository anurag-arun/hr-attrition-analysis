import sqlite3
import pandas as pd

# 1. Load cleaned data
df = pd.read_csv('data/processed/hr_cleaned.csv')

# 2. Connect to SQLite database (creates hr_analytics.db if not exists)
conn = sqlite3.connect('hr_analytics.db')

# 3. Write data to table
df.to_sql('hr_data', conn, if_exists='replace', index=False)

print('SUCCESS: Cleaned data loaded into SQLite database: hr_analytics.db (Table: hr_data)')

# Quick test query
cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM hr_data;')
print(f'Total records verified in hr_data: {cursor.fetchone()[0]}')

conn.close()

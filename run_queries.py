import sqlite3
import pandas as pd

conn = sqlite3.connect('hr_analytics.db')

queries = {
    '1. Top-Level KPIs': '''
        SELECT 
            COUNT(*) AS TotalEmployees,
            SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalAttritions,
            ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS AttritionRatePct,
            ROUND(AVG(MonthlyIncome), 2) AS AvgMonthlyIncome
        FROM hr_data;
    ''',
    '2. Attrition by Overtime': '''
        SELECT 
            OverTime,
            COUNT(*) AS TotalStaff,
            SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Leavers,
            ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS AttritionRatePct
        FROM hr_data
        GROUP BY OverTime;
    ''',
    '3. Attrition by Tenure Band': '''
        SELECT 
            TenureBand,
            COUNT(*) AS TotalStaff,
            SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Leavers,
            ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS AttritionRatePct
        FROM hr_data
        GROUP BY TenureBand
        ORDER BY AttritionRatePct DESC;
    '''
}

for title, q in queries.items():
    print('\n' + '=' * 50)
    print(title)
    print('=' * 50)
    res = pd.read_sql_query(q, conn)
    print(res.to_string(index=False))

conn.close()

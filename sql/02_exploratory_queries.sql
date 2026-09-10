-- ====================================================================
-- HR ATTRITION ANALYSIS: CORE BUSINESS ANALYTICS QUERIES
-- ====================================================================

-- 1. Top-Level Workforce KPIs
SELECT 
    COUNT(*) AS TotalEmployees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalAttritions,
    ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS AttritionRatePct,
    ROUND(AVG(MonthlyIncome), 2) AS AvgMonthlyIncome,
    ROUND(AVG(YearsAtCompany), 1) AS AvgTenureYears
FROM hr_data;


-- 2. Attrition by Department & Job Role
SELECT 
    Department,
    JobRole,
    COUNT(*) AS TotalStaff,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Leavers,
    ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS AttritionRatePct
FROM hr_data
GROUP BY Department, JobRole
ORDER BY AttritionRatePct DESC;


-- 3. Overtime vs Attrition Breakdown
SELECT 
    OverTime,
    COUNT(*) AS TotalStaff,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Leavers,
    ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS AttritionRatePct
FROM hr_data
GROUP BY OverTime;


-- 4. Turnover by Tenure Cohorts (Flight Risk by Loyalty)
SELECT 
    TenureBand,
    COUNT(*) AS TotalStaff,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Leavers,
    ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS AttritionRatePct
FROM hr_data
GROUP BY TenureBand
ORDER BY AttritionRatePct DESC;


-- 5. Cross-Tab: Income Quartiles vs Attrition
SELECT 
    IncomeBand,
    ROUND(AVG(MonthlyIncome), 2) AS AvgIncomeInBand,
    COUNT(*) AS Headcount,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Leavers,
    ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS AttritionRatePct
FROM hr_data
GROUP BY IncomeBand
ORDER BY IncomeBand ASC;


-- 6. Financial Replacement Cost Impact (Assuming 50% of annual salary per exit)
SELECT 
    Department,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalLeavers,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN (MonthlyIncome * 12) * 0.5 ELSE 0 END), 2) AS EstimatedReplacementCostUSD
FROM hr_data
GROUP BY Department
ORDER BY EstimatedReplacementCostUSD DESC;

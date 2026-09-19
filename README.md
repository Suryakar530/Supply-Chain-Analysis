# Supply-Chain-Analysis
📦 Supply Chain Analytics — PostgreSQL, Python & Power BI
📌 Project Overview

This project analyzes supply chain operations to identify patterns and business opportunities across sales, revenue, inventory, logistics, shipping, manufacturing costs, and product quality.

The project combines PostgreSQL, Python, Pandas, Matplotlib, and Power BI to transform raw supply-chain data into meaningful business insights and an interactive dashboard.

🎯 Project Objectives

The main objectives of this project are to:

Analyze overall sales and revenue performance
Identify high-performing product categories
Find top products by revenue and units sold
Analyze costs and estimated profitability
Evaluate inventory levels and stock risks
Compare shipping carriers and transportation modes
Analyze shipping time and shipping costs
Identify products and suppliers with higher defect rates
Evaluate inspection results and quality risks
Generate actionable business recommendations
🗂️ Dataset

The dataset contains supply-chain information covering:

SKU / Product
Product Type
Supplier
Location
Price
Number of Products Sold
Revenue Generated
Stock Levels
Availability
Manufacturing Costs
Shipping Costs
Shipping Times
Shipping Carriers
Transportation Modes
Routes
Defect Rates
Inspection Results
🛠️ Tools & Technologies
Tool	Purpose
PostgreSQL	SQL analysis and business queries
Python	Data analysis and calculations
Pandas	Data manipulation and aggregation
NumPy	Numerical operations
Matplotlib	Data visualization
Power BI	Interactive dashboard
GitHub	Project documentation and version control
🗄️ PostgreSQL Analysis

The PostgreSQL analysis is organized into 8 major sections.

1. Overall Data Validation

Performed:

Record count
Unique SKU count
Product-type count
Supplier count
Location count
Shipping-carrier count
Transportation-mode count
Column/data-type validation

The SQL validation checks the overall structure and dimensions of the supply_chain table.

2. Overall Business KPIs

Calculated:

Total records
Total units sold
Total revenue
Average product price
Average revenue
Average shipping cost
Average manufacturing cost
Average defect rate
3. Sales & Revenue Analysis

Analyzed:

Revenue by product type
Units sold by product type
Top 10 products by revenue
Top 10 products by units sold

4. Revenue & Cost Analysis

Analyzed:

Total revenue
Shipping costs
Manufacturing costs
Other costs
Total cost
Estimated profit
Estimated profit margin
Cost percentage
Profitability by product type

5. Inventory & Availability Analysis

Analyzed:

Average stock
Minimum and maximum stock
Total stock
Average availability
Inventory by product type
Potential stock risks

Inventory was classified into statuses such as Out of Stock, High Stock Risk, Medium Stock Risk, and Healthy Stock.

6. Shipping & Logistics Analysis

Analyzed:

Shipping carrier performance
Transportation-mode performance
Shipping cost by product type
Route performance

7. Quality & Defect Analysis

Analyzed:

Overall defect rate
Inspection results
Defect rate by product type
Highest-defect products
Quality-risk classification

The SQL classifies products into High, Medium, and Low Quality Risk based on defect rates.

8. Business Insights & Executive Summary

The final SQL section combines major supply-chain KPIs including revenue, costs, estimated profit, profit margin, inventory, availability, shipping time, and defect rate.

📈 Visualizations

The Python analysis includes visualizations such as:

Distribution of Product Prices
Units Sold by Product Type
Revenue by Product Type
Average Defect Rate by Inspection Result
Average Stock Level by Product Type
Shipping Time vs Shipping Cost
Average Shipping Cost by Carrier
Top 10 SKUs by Revenue
Average Shipping Time by Transportation Mode
📊 Power BI Dashboard

The project also includes an interactive Power BI dashboard for presenting the major supply-chain KPIs and analysis visually.

The dashboard can be used to explore:

Sales performance
Revenue
Product performance
Inventory
Shipping & logistics
Quality and defects
Business insights
💡 Business Recommendations

Based on the analysis, the project recommends:

Focus on high-revenue product categories to support sales growth.
Monitor critically low inventory levels to reduce stock-out risk.
Review suppliers with high defect rates and introduce corrective quality-control measures.
Evaluate transportation modes and shipping carriers based on both cost and delivery performance.
Optimize inventory levels while maintaining sufficient stock for high-demand products.
Monitor supplier, inventory, logistics, sales, and quality KPIs regularly to improve overall supply-chain efficiency.

These recommendations are also reflected in the project's Python executive-summary section.

🔄 Project Workflow
Raw Supply Chain Data
        ↓
Data Loading & Validation
        ↓
PostgreSQL
        ↓
SQL Data Analysis
        ↓
Python / Pandas Analysis
        ↓
Matplotlib Visualizations
        ↓
Power BI Dashboard
        ↓
Business Insights
        ↓
Recommendations
🎓 Skills Demonstrated
PostgreSQL
SQL
Pandas
NumPy
Matplotlib
Exploratory Data Analysis
Sales & Revenue Analysis
Inventory Analysis
Supply Chain Analytics
Logistics Analysis
Quality Analysis
Business Intelligence
Power BI
Data Visualization
Business Problem Solving
GitHub


🏁 Conclusion

This project demonstrates an end-to-end Supply Chain Analytics workflow, starting from raw data validation and SQL analysis and progressing to Python visualization and Power BI reporting.

The analysis provides insights into sales, revenue, inventory, logistics, shipping costs, transportation performance, and product quality, helping identify areas where operational efficiency and business performance can be improve

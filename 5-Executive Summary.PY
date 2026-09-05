#LOAD DATA

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("supply_chain_data.csv")

print("Dataset loaded successfully.")
print("Shape:", df.shape)

# 9.1 Create an Executive Summary


print("\n" + "=" * 60)
print("BUSINESS INSIGHTS & CONCLUSION")
print("=" * 60)

total_revenue = df["Revenue generated"].sum()
total_cost = df["Costs"].sum()
total_profit = total_revenue - total_cost
avg_defect = df["Defect rates"].mean()
avg_shipping = df["Shipping times"].mean()
avg_stock = df["Stock levels"].mean()

print("\nKEY BUSINESS METRICS")
print("-" * 40)

print("Total Revenue:", round(total_revenue, 2))
print("Total Cost:", round(total_cost, 2))
print("Estimated Profit:", round(total_profit, 2))
print("Average Defect Rate:", round(avg_defect, 2))
print("Average Shipping Time:", round(avg_shipping, 2))
print("Average Stock Level:", round(avg_stock, 2))


# 9.2 Identify the Best Product Category
best_product = (
    df.groupby("Product type")["Revenue generated"]
    .sum()
    .idxmax()
)

print("\nBest Revenue-Generating Product Type:")
print(best_product)



# 9.3 Identify the Best Supplier

best_supplier = (
    df.groupby("Supplier name")["Defect rates"]
    .mean()
    .idxmin()
)

print("\nSupplier with Lowest Average Defect Rate:")
print(best_supplier)



# 9.4 Identify the Highest-Risk Supplier
highest_risk_supplier = (
    df.groupby("Supplier name")["Defect rates"]
    .mean()
    .idxmax()
)

print("\nSupplier with Highest Average Defect Rate:")
print(highest_risk_supplier)


# 9.5 Identify Inventory Risk
critical_products = (
    df[df["Inventory Risk"] == "Critical"]
    .shape[0]
)

print("\nCritical Inventory Products:",
      critical_products)


# 9.6 Final Business Recommendations
print("\n" + "=" * 60)
print("BUSINESS RECOMMENDATIONS")
print("=" * 60)

print("""
1. Focus on high-revenue product categories to maximize sales growth.

2. Monitor products with critically low inventory levels
   to reduce stock-out risk.

3. Review suppliers with high defect rates and consider
   corrective quality-control measures.

4. Evaluate shipping modes and carriers with high shipping
   times or high transportation costs.

5. Reduce unnecessary inventory while maintaining sufficient
   stock for high-demand products.

6. Use supplier, inventory, logistics and quality KPIs
   regularly to improve supply-chain efficiency.
""")
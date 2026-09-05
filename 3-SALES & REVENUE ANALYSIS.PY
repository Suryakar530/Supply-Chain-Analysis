#LOAD DATA
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("supply_chain_data.csv")

# Calculate estimated profit
df["Estimated Profit"] = (
    df["Revenue generated"] - df["Costs"]
)

print("Dataset loaded successfully.")


# 3.1 — TOTAL SALES AND REVENUE

print("\n" + "=" * 60)
print("SALES & REVENUE OVERVIEW")
print("=" * 60)

total_units = df["Number of products sold"].sum()
total_revenue = df["Revenue generated"].sum()
total_cost = df["Costs"].sum()
total_profit = df["Estimated Profit"].sum()

print("Total Units Sold:", total_units)
print("Total Revenue:", round(total_revenue, 2))
print("Total Cost:", round(total_cost, 2))
print("Estimated Profit:", round(total_profit, 2))

#3.2 — Revenue by Product Type

revenue_by_product = (
    df.groupby("Product type")
    .agg(
        Units_Sold=("Number of products sold", "sum"),
        Revenue=("Revenue generated", "sum"),
        Profit=("Estimated Profit", "sum")
    )
    .sort_values("Revenue", ascending=False)
)

print("\nRevenue by Product Type:")
print(revenue_by_product)

# 3.3 — Top 10 products by sales

top_sales = (
    df[
        ["SKU", "Product type", "Number of products sold"]
    ]
    .sort_values(
        "Number of products sold",
        ascending=False
    )
    .head(10)
)

print("\n" + "=" * 60)
print("TOP 10 PRODUCTS BY UNITS SOLD")
print("=" * 60)

print(top_sales)

# 3.4 — Top 10 products by revenue

top_revenue = (
    df[
        ["SKU", "Product type", "Revenue generated"]
    ]
    .sort_values(
        "Revenue generated",
        ascending=False
    )
    .head(10)
)

print("\n" + "=" * 60)
print("TOP 10 PRODUCTS BY REVENUE")
print("=" * 60)

print(top_revenue)

# 4.6 — Top 10 products by profit

top_profit = (
    df[
        ["SKU", "Product type", "Revenue generated",
         "Costs", "Estimated Profit"]
    ]
    .sort_values(
        "Estimated Profit",
        ascending=False
    )
    .head(10)
)

print("\n" + "=" * 60)
print("TOP 10 PRODUCTS BY ESTIMATED PROFIT")
print("=" * 60)

print(top_profit)

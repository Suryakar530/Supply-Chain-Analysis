#  2.1 — Load the cleaned dataset

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("supply_chain_data.csv")

print("Dataset loaded successfully.")
print("Shape:", df.shape)

#  2.2 — Key business metrics

print("\n" + "=" * 60)
print("KEY BUSINESS METRICS")
print("=" * 60)

print("Total Units Sold:", df["Number of products sold"].sum())
print("Average Units Sold:", df["Number of products sold"].mean())

print("Total Revenue:", df["Revenue generated"].sum())
print("Average Revenue:", df["Revenue generated"].mean())

print("Total Costs:", df["Costs"].sum())
print("Average Costs:", df["Costs"].mean())

print("Average Stock Level:", df["Stock levels"].mean())
print("Average Shipping Time:", df["Shipping times"].mean())
print("Average Defect Rate:", df["Defect rates"].mean())

#2.3 — Calculate estimated profit

print("\n" + "=" * 60)
print("TOP 10 PRODUCTS BY REVENUE")
print("=" * 60)

top_products = df[
    ["SKU", "Product type", "Revenue generated"]
].sort_values(
    by="Revenue generated",
    ascending=False
).head(10)

print(top_products)

#2.4 — Top 10 products by revenue

print("\n" + "=" * 60)
print("TOP 10 PRODUCTS BY REVENUE")
print("=" * 60)

top_products = df[
    ["SKU", "Product type", "Revenue generated"]
].sort_values(
    by="Revenue generated",
    ascending=False
).head(10)

print(top_products)

#2.5 — Final output

print("\n" + "=" * 60)
print("DESCRIPTIVE ANALYSIS COMPLETED")
print("=" * 60)
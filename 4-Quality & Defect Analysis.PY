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





# 8.1 Overall Quality

print("\n" + "=" * 60)
print("QUALITY & DEFECT ANALYSIS")
print("=" * 60)

print("Average Defect Rate:",
      round(df["Defect rates"].mean(), 2))

print("Maximum Defect Rate:",
      round(df["Defect rates"].max(), 2))

print("Minimum Defect Rate:",
      round(df["Defect rates"].min(), 2))


# 8.2 Defects by Product Type
defect_by_product = (
    df.groupby("Product type")
    .agg(
        Average_Defect_Rate=("Defect rates", "mean"),
        Product_Count=("SKU", "count")
    )
    .sort_values("Average_Defect_Rate", ascending=False)
)

print("\nDefect Rate by Product Type:")
print(defect_by_product)


# 8.3 Defects by Supplier


defect_by_supplier = (
    df.groupby("Supplier name")
    .agg(
        Average_Defect_Rate=("Defect rates", "mean"),
        Products=("SKU", "count")
    )
    .sort_values("Average_Defect_Rate", ascending=False)
)

print("\nDefect Rate by Supplier:")
print(defect_by_supplier)


# 8.4 Top 10 Highest-Defect Products


top_defects = (
    df[
        ["SKU", "Product type", "Supplier name",
         "Defect rates", "Inspection results"]
    ]
    .sort_values("Defect rates", ascending=False)
    .head(10)
)

print("\nTop 10 Products with Highest Defect Rates:")
print(top_defects)


# 8.5 Inspection Result Analysis


inspection_analysis = (
    df.groupby("Inspection results")
    .agg(
        Products=("SKU", "count"),
        Average_Defect_Rate=("Defect rates", "mean")
    )
    .sort_values("Average_Defect_Rate", ascending=False)
)

print("\nInspection Result Analysis:")
print(inspection_analysis)


# 8.6 Quality Risk Classification


def quality_risk(defect_rate):

    if defect_rate >= 4:
        return "High Risk"

    elif defect_rate >= 2:
        return "Medium Risk"

    else:
        return "Low Risk"


df["Quality Risk"] = df["Defect rates"].apply(quality_risk)

print("\nQuality Risk Distribution:")
print(df["Quality Risk"].value_counts())


# 8.7 Final Section 8


print("\n" + "=" * 60)
print("QUALITY & DEFECT ANALYSIS COMPLETED")
print("=" * 60)
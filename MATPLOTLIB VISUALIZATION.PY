# Step A — Common setup


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("supply_chain_data.csv")

# Create calculated columns
df["Estimated Profit"] = (
    df["Revenue generated"] - df["Costs"]
)

df["Profit Margin %"] = (
    df["Estimated Profit"] /
    df["Revenue generated"]
) * 100

# Inventory Risk
def inventory_risk(row):
    if row["Stock levels"] < 20:
        return "Critical"
    elif row["Stock levels"] < 40:
        return "High"
    elif row["Stock levels"] < 60:
        return "Medium"
    else:
        return "Low"

df["Inventory Risk"] = df.apply(inventory_risk, axis=1)

print("Dataset loaded successfully.")
# 1 Which product type generates the highest revenue?
# Chart

# Bar Chart
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("supply_chain_data.csv")

revenue_by_product = (
    df.groupby("Product type")["Revenue generated"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

plt.bar(
    revenue_by_product.index,
    revenue_by_product.values
)

plt.title("Revenue by Product Type")
plt.xlabel("Product Type")
plt.ylabel("Total Revenue")

plt.xticks(rotation=45)

for i, value in enumerate(revenue_by_product.values):
    plt.text(
        i,
        value,
        f"{value:,.0f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("heighest_revenue.png")
plt.show()
# Business question answered:

# Which product category contributes the most revenue?

# 2 Which product type has the highest number of units sold?
# Chart

# Bar Chart

units_by_product = (
    df.groupby("Product type")["Number of products sold"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

plt.bar(
    units_by_product.index,
    units_by_product.values
)

plt.title("Units Sold by Product Type")
plt.xlabel("Product Type")
plt.ylabel("Number of Products Sold")

plt.xticks(rotation=45)

for i, value in enumerate(units_by_product.values):
    plt.text(
        i,
        value,
        f"{value:,.0f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("heighest_no_of_unitssold.png")

plt.show()

# 3 Which are the top 10 products by revenue?
# Chart

# Horizontal Bar Chart

top_revenue = (
    df.groupby("SKU")["Revenue generated"]
    .sum()
    .sort_values(ascending=True)
    .tail(10)
)

plt.figure(figsize=(10, 6))

plt.barh(
    top_revenue.index,
    top_revenue.values
)

plt.title("Top 10 SKUs by Revenue")
plt.xlabel("Revenue")
plt.ylabel("SKU")

for i, value in enumerate(top_revenue.values):
    plt.text(
        value,
        i,
        f" {value:,.0f}",
        va="center"
    )

plt.tight_layout()
plt.savefig("top_10_products_by_revenue.png")

plt.show()

# 4 Which product type has the lowest average stock?
# Chart

# Bar Chart

average_stock = (
    df.groupby("Product type")["Stock levels"]
    .mean()
    .sort_values()
)

plt.figure(figsize=(10, 6))

plt.bar(
    average_stock.index,
    average_stock.values
)

plt.title("Average Stock Level by Product Type")
plt.xlabel("Product Type")
plt.ylabel("Average Stock Level")

plt.xticks(rotation=45)

for i, value in enumerate(average_stock.values):
    plt.text(
        i,
        value,
        f"{value:.1f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("lowest_avg_stock.png")

plt.show()
# Business question:

# Which product categories may require closer inventory monitoring?

# Business question:



# 5 Which transportation mode has the longest shipping time?
# Chart

# Bar Chart

shipping_by_mode = (
    df.groupby("Transportation modes")["Shipping times"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 6))

plt.bar(
    shipping_by_mode.index,
    shipping_by_mode.values
)

plt.title("Average Shipping Time by Transportation Mode")
plt.xlabel("Transportation Mode")
plt.ylabel("Average Shipping Time")

plt.xticks(rotation=45)

for i, value in enumerate(shipping_by_mode.values):
    plt.text(
        i,
        value,
        f"{value:.1f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("transportmode_wirh_longest_shippingtime.png")

plt.show()
# Business question:

# Which transportation mode is slower and may require optimization?

# 6 Which shipping carrier has the highest shipping cost?
# Chart

# Bar Chart

shipping_cost = (
    df.groupby("Shipping carriers")["Shipping costs"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 6))

plt.bar(
    shipping_cost.index,
    shipping_cost.values
)

plt.title("Average Shipping Cost by Carrier")
plt.xlabel("Shipping Carrier")
plt.ylabel("Average Shipping Cost")

plt.xticks(rotation=45)

for i, value in enumerate(shipping_cost.values):
    plt.text(
        i,
        value,
        f"{value:.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("shippingcarrier_with_heighest_shippingcost.png")

plt.show()
# Business question:

# Which carriers are associated with higher shipping costs?

# 7 Does inspection result relate to defect rates?
# Chart

# Bar Chart

inspection_defects = (
    df.groupby("Inspection results")["Defect rates"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 6))

plt.bar(
    inspection_defects.index,
    inspection_defects.values
)

plt.title("Average Defect Rate by Inspection Result")
plt.xlabel("Inspection Result")
plt.ylabel("Average Defect Rate")

for i, value in enumerate(inspection_defects.values):
    plt.text(
        i,
        value,
        f"{value:.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("inspection_result_to_defect_rates.png")

plt.show()
# Business question:

# How does average defect rate differ across inspection results?

# 8 Is there a relationship between price and units sold?
# Chart

# Scatter Plot

plt.figure(figsize=(9, 6))

plt.scatter(
    df["Price"],
    df["Number of products sold"]
)

plt.title("Price vs Number of Products Sold")
plt.xlabel("Price")
plt.ylabel("Number of Products Sold")

plt.tight_layout()
plt.savefig("relationship_between_price_and_unitssold.png")
plt.show()
# Business question:

# Do higher-priced products tend to sell more or fewer units?

# 9 Is shipping time related to shipping cost?
# Chart

# Scatter Plot

plt.figure(figsize=(9, 6))

plt.scatter(
    df["Shipping times"],
    df["Shipping costs"]
)

plt.title("Shipping Time vs Shipping Cost")
plt.xlabel("Shipping Time")
plt.ylabel("Shipping Cost")

plt.tight_layout()
plt.savefig("shipping_time_with_shippimng_cost.png")

plt.show()
# Business question:

# Does longer shipping time appear to be associated with higher shipping costs?

# 10 What is the distribution of product prices?
# Chart

# Histogram

plt.figure(figsize=(9, 6))

plt.hist(
    df["Price"],
    bins=10
)

plt.title("Distribution of Product Prices")
plt.xlabel("Price")
plt.ylabel("Number of Products")

plt.tight_layout()
plt.savefig("distribution_of_product_prices.png")
plt.show()
# # Business question:

# What price range contains most products?


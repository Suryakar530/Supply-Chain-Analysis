# ============================================================
# SUPPLY CHAIN ANALYSIS
# STEP 1: DATA LOADING AND VALIDATION
# ============================================================

import pandas as pd
import numpy as np


# ------------------------------------------------------------
# 1. LOAD DATA
# ------------------------------------------------------------

file_path = "supply_chain_data.csv"

df = pd.read_csv(file_path)


# ------------------------------------------------------------
# 2. BASIC DATA INSPECTION
# ------------------------------------------------------------

print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())


# ------------------------------------------------------------
# 3. DATA TYPES
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)

print(df.dtypes)


# ------------------------------------------------------------
# 4. MISSING VALUES
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

missing_values = df.isnull().sum()

print(missing_values)


# ------------------------------------------------------------
# 5. DUPLICATE RECORDS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("DUPLICATE RECORDS")
print("=" * 60)

print("Number of duplicate rows:", df.duplicated().sum())


# ------------------------------------------------------------
# 6. UNIQUE VALUES
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("UNIQUE VALUES")
print("=" * 60)

print(df.nunique())


# ------------------------------------------------------------
# 7. NUMERICAL SUMMARY
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("NUMERICAL SUMMARY")
print("=" * 60)

print(df.describe())


# ------------------------------------------------------------
# 8. CATEGORICAL SUMMARY
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("CATEGORICAL SUMMARY")
print("=" * 60)

print(df.describe(include="object"))


# ------------------------------------------------------------
# 9. CHECK NEGATIVE VALUES
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("NEGATIVE VALUE CHECK")
print("=" * 60)

numeric_columns = df.select_dtypes(include=np.number).columns

for column in numeric_columns:
    negative_count = (df[column] < 0).sum()

    if negative_count > 0:
        print(f"{column}: {negative_count} negative values")
    else:
        print(f"{column}: No negative values")


# ------------------------------------------------------------
# 10. FINAL VALIDATION
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("VALIDATION COMPLETE")
print("=" * 60)

print(f"Total Rows: {df.shape[0]}")
print(f"Total Columns: {df.shape[1]}")
print(f"Total Missing Values: {df.isnull().sum().sum()}")
print(f"Total Duplicate Rows: {df.duplicated().sum()}")

print("\nDataset successfully loaded and validated.")

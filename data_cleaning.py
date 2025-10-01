# Data Cleaning with Pandas

# Topics: Handling missing values, duplicates, formatting, replacing invalid data

import pandas as pd
import numpy as np


# 1. Create Sample DataFrame with issues

data = {
    "Name": ["Aravind", "Rahul", None, "Priya", "Aravind"],
    "Age": [24, np.nan, 23, 22, 24],
    "Grade": ["A", "B", "C", None, "A"],
    "City": ["Coventry", "London", "Manchester", "London", "Coventry"]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
print("\n")


# 2. Handling Missing Values

# Check for missing values
print("Missing values per column:\n", df.isna().sum())

# Fill missing numeric values with mean
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Fill missing categorical values with 'Unknown'
df["Name"].fillna("Unknown", inplace=True)
df["Grade"].fillna("Unknown", inplace=True)

print("DataFrame after filling missing values:\n", df)
print("\n")


# 3. Removing Duplicates

df_no_duplicates = df.drop_duplicates()
print("DataFrame after removing duplicates:\n", df_no_duplicates)
print("\n")


# 4. Formatting Data

# Convert names to uppercase
df_no_duplicates["Name"] = df_no_duplicates["Name"].str.upper()
print("DataFrame with uppercase names:\n", df_no_duplicates)


# 5. Replacing Invalid Data

# Suppose 'Unknown' in Grade is invalid, replace with 'F'
df_no_duplicates["Grade"].replace("Unknown", "F", inplace=True)
print("DataFrame after replacing invalid grades:\n", df_no_duplicates)
print("\n")


# 6. Mini Exercises

# 1. Add a new column 'Pass' (Grade A/B/C = True, else False)
df_no_duplicates["Pass"] = df_no_duplicates["Grade"].isin(["A", "B", "C"])
print("Added Pass column:\n", df_no_duplicates)

# 2. Reset index after cleaning
df_no_duplicates.reset_index(drop=True, inplace=True)
print("DataFrame after index reset:\n", df_no_duplicates)

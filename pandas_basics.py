#  Pandas Series & DataFrames

# Topics: Pandas Series, DataFrames, CSV loading, data exploration

import pandas as pd


# 1. Pandas Series

print("### Pandas Series ###")
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print("Series:\n", series)

# Custom index
series_index = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print("Series with custom index:\n", series_index)

# Accessing elements
print("First element:", series[0])
print("Element with index 'c':", series_index['c'])
print("\n")


# 2. Pandas DataFrame

print("### Pandas DataFrame ###")
# Create DataFrame from dictionary
data_dict = {
    "Name": ["Aravind", "Rahul", "Priya"],
    "Age": [24, 22, 23],
    "Grade": ["A", "B", "A"]
}
df = pd.DataFrame(data_dict)
print("DataFrame:\n", df)

# Access columns
print("Names column:\n", df["Name"])

# Access rows by index
print("First row:\n", df.iloc[0])


# 3. Load CSV

print("### Load CSV ###")
# Example: Create sample CSV first
df.to_csv("students.csv", index=False)

# Read CSV
df_csv = pd.read_csv("students.csv")
print("CSV loaded DataFrame:\n", df_csv)


# 4. Explore Data

print("First 2 rows:\n", df_csv.head(2))
print("Last row:\n", df_csv.tail(1))
print("Info:\n")
print(df_csv.info())
print("Summary statistics:\n", df_csv.describe(include='all'))


# 5. Indexing and Selection

# Select multiple columns
print("Name and Age columns:\n", df_csv[["Name", "Age"]])

# Select rows using conditions
print("Students with grade A:\n", df_csv[df_csv["Grade"] == "A"])


# 6. Mini Exercises

# 1. Add a new column 'City'
df_csv["City"] = ["Coventry", "London", "Manchester"]
print("Added City column:\n", df_csv)

# 2. Calculate average age
average_age = df_csv["Age"].mean()
print("Average age:", average_age)

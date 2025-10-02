# Data Transformation with Pandas

# Topics: map, apply, groupby, aggregation

import pandas as pd


# 1. Create Sample DataFrame

data = {
    "Name": ["Aravind", "Rahul", "Priya", "Sita", "John"],
    "Age": [24, 22, 23, 21, 25],
    "Grade": ["A", "B", "A", "C", "B"],
    "Math": [95, 85, 90, 70, 80],
    "Science": [90, 80, 85, 65, 75]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
print("\n")


# 2. Using map() to transform column

# Map Grade to numeric score
grade_mapping = {"A": 4, "B": 3, "C": 2, "D": 1}
df["Grade_Score"] = df["Grade"].map(grade_mapping)
print("After mapping Grade to numeric:\n", df)
print("\n")


# 3. Using apply() for row-wise operation

# Calculate total marks
df["Total_Marks"] = df[["Math", "Science"]].apply(lambda row: row["Math"] + row["Science"], axis=1)
print("After calculating Total Marks:\n", df)
print("\n")


# 4. GroupBy and Aggregation

# Group by Grade and calculate average total marks
grade_avg = df.groupby("Grade")["Total_Marks"].mean()
print("Average Total Marks by Grade:\n", grade_avg)
print("\n")

# Count of students in each grade
grade_count = df.groupby("Grade")["Name"].count()
print("Number of students in each grade:\n", grade_count)
print("\n")


# 5. Mini Exercises

# 1. Add column Pass/Fail based on Total Marks >= 150
df["Pass"] = df["Total_Marks"].apply(lambda x: "Pass" if x >= 150 else "Fail")
print("After adding Pass/Fail column:\n", df)
print("\n")

# 2. Sort students by Total Marks descending
df_sorted = df.sort_values(by="Total_Marks", ascending=False)
print("Students sorted by Total Marks:\n", df_sorted)

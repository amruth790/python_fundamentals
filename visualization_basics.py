# Visualization Basics

# Topics: Matplotlib, Seaborn, plotting, customizing plots

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Create Sample DataFrame

data = {
    "Student": ["Aravind", "Rahul", "Priya", "Sita", "John"],
    "Math": [95, 85, 90, 70, 80],
    "Science": [90, 80, 85, 65, 75],
    "English": [88, 82, 85, 70, 78]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)


# 2. Matplotlib: Line Plot

plt.figure(figsize=(8,5))
plt.plot(df["Student"], df["Math"], marker='o', label="Math")
plt.plot(df["Student"], df["Science"], marker='s', label="Science")
plt.title("Student Scores Line Plot")
plt.xlabel("Student")
plt.ylabel("Score")
plt.legend()
plt.show()


# 3. Matplotlib: Bar Chart

plt.figure(figsize=(8,5))
plt.bar(df["Student"], df["English"], color='skyblue')
plt.title("English Scores Bar Chart")
plt.xlabel("Student")
plt.ylabel("Score")
plt.show()


# 4. Matplotlib: Histogram

plt.figure(figsize=(8,5))
plt.hist(df["Math"], bins=5, color='orange', edgecolor='black')
plt.title("Math Scores Histogram")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()


# 5. Seaborn: Scatter Plot

plt.figure(figsize=(8,5))
sns.scatterplot(x="Math", y="Science", data=df, hue="Student", s=100)
plt.title("Math vs Science Scores")
plt.show()


# 6. Seaborn: Box Plot

plt.figure(figsize=(8,5))
sns.boxplot(data=df[["Math","Science","English"]])
plt.title("Score Distribution Box Plot")
plt.show()


# 7. Seaborn: Heatmap

plt.figure(figsize=(6,4))
sns.heatmap(df[["Math","Science","English"]], annot=True, cmap="YlGnBu", cbar=True)
plt.title("Scores Heatmap")
plt.show()


# 8. Mini Exercises

# 1. Add a new column Total_Score
df["Total_Score"] = df[["Math","Science","English"]].sum(axis=1)
print("DataFrame with Total Score:\n", df)

# 2. Plot Total Score Bar Chart
plt.figure(figsize=(8,5))
sns.barplot(x="Student", y="Total_Score", data=df, palette="viridis")
plt.title("Total Score of Students")
plt.show()

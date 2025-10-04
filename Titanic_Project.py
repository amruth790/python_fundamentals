# Mini Project - Titanic Dataset

# Topics: Data Cleaning, Transformation, Visualization, Saving outputs

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create folder for plots
if not os.path.exists("plots"):
    os.makedirs("plots")


# 1. Load Dataset

# Download Titanic dataset CSV into the repo folder as 'titanic.csv'
df = pd.read_csv("titanic.csv")
print("First 5 rows:\n", df.head())


# 2. Explore Data

print("\nDataFrame Info:\n")
print(df.info())
print("\nSummary statistics:\n", df.describe(include='all'))


# 3. Data Cleaning

# Fill missing Age with median
df["age"] = df["age"].fillna(df["age"].median())

# Fill Embarked missing values with most frequent
df.columns = df.columns.str.strip().str.lower()
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])


# Drop Cabin column (too many missing)
df.drop("Cabin", axis=1, inplace=True)

# Verify missing values
print("\nMissing values after cleaning:\n", df.isna().sum())


# 4. Data Transformation

# Convert Sex to numeric
df["Sex_num"] = df["Sex"].map({"male":0, "female":1})

# Create FamilySize feature
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# Create AgeGroup
df["AgeGroup"] = pd.cut(df["Age"], bins=[0,12,18,35,60,100], labels=["Child","Teen","Adult","MidAge","Senior"])


# 5. Visualization

# Survival count plot
plt.figure(figsize=(6,4))
sns.countplot(x="Survived", data=df)
plt.title("Survival Count")
plt.savefig("plots/survival_count.png")
plt.close()

# Age distribution by survival
plt.figure(figsize=(8,5))
sns.histplot(data=df, x="age", hue="Survived", bins=20, kde=False)
plt.title("Age Distribution by Survival")
plt.savefig("plots/age_distribution_survived.png")
plt.close()

# Survival rate by Sex
plt.figure(figsize=(6,4))
sns.barplot(x="Sex", y="Survived", data=df)
plt.title("Survival Rate by Sex")
plt.savefig("plots/survival_by_sex.png")
plt.close()

# Family size vs survival
plt.figure(figsize=(8,5))
sns.barplot(x="FamilySize", y="Survived", data=df)
plt.title("Survival Rate by Family Size")
plt.savefig("plots/survival_by_family.png")
plt.close()

# Age group vs survival
plt.figure(figsize=(8,5))
sns.barplot(x="AgeGroup", y="Survived", data=df)
plt.title("Survival Rate by Age Group")
plt.savefig("plots/survival_by_agegroup.png")
plt.close()

print("All plots saved in 'plots/' folder.")

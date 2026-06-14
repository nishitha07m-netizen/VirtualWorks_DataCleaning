import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Customers.csv")

print("DATASET SHAPE:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing Profession values
df["Profession"] = df["Profession"].fillna("Unknown")

# Check duplicates
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

# Remove duplicates
df = df.drop_duplicates()

# Standardize text
df["Gender"] = df["Gender"].str.strip().str.title()
df["Profession"] = df["Profession"].str.strip().str.title()

# Structural validation
df = df[df["Age"] > 0]
df = df[df["Annual Income ($)"] > 0]
df = df[(df["Spending Score (1-100)"] >= 1) &
        (df["Spending Score (1-100)"] <= 100)]
df = df[df["Work Experience"] >= 0]
df = df[df["Family Size"] > 0]

# Save cleaned dataset
df.to_csv("Cleaned_Customers.csv", index=False)

print("\nCleaned dataset saved successfully!")

# Age Distribution
plt.figure(figsize=(6,4))
plt.hist(df["Age"], bins=15)
plt.title("Age Distribution")
plt.savefig("Age_Distribution.png")
plt.close()

# Income Distribution
plt.figure(figsize=(6,4))
plt.hist(df["Annual Income ($)"], bins=15)
plt.title("Income Distribution")
plt.savefig("Income_Distribution.png")
plt.close()

# Spending Score Distribution
plt.figure(figsize=(6,4))
plt.hist(df["Spending Score (1-100)"], bins=15)
plt.title("Spending Score Distribution")
plt.savefig("SpendingScore_Distribution.png")
plt.close()

print("Charts saved successfully!")
print("Project Completed!")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/synthetic_credit_data.csv")

# Basic Information
print("\nDataset Info:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# Create graphs folder if it doesn't exist
import os
os.makedirs("reports", exist_ok=True)

# 1. Class Distribution
plt.figure(figsize=(6,4))
sns.countplot(x="repayment_status", data=df)
plt.title("Repayment Status Distribution")
plt.savefig("reports/class_distribution.png")
#plt.show()

# 2. Histograms
df.hist(figsize=(12,10))
plt.tight_layout()
plt.savefig("reports/histograms.png")
#plt.show()

# 3. Correlation Heatmap
numeric_df = df.select_dtypes(include=["int64", "float64"])

plt.figure(figsize=(12,8))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.savefig("reports/correlation_heatmap.png")
plt.close()

# Gender Distribution

plt.figure(figsize=(6,4))
sns.countplot(x="gender", data=df)
plt.title("Gender Distribution")
plt.savefig("reports/gender_distribution.png")
plt.close()


# Income Distribution

plt.figure(figsize=(8,4))
sns.histplot(df["income_level"], bins=30)
plt.title("Income Level Distribution")
plt.savefig("reports/income_distribution.png")
plt.close()

print("\nEDA Completed Successfully!")
print("Graphs saved inside reports folder.")
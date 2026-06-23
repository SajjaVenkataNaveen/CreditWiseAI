import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/synthetic_credit_data.csv")

df["gender"] = df["gender"].map({
    "Male": 0,
    "Female": 1
})

X = df.drop("repayment_status", axis=1)

# Load model
model = joblib.load("models/random_forest.pkl")

# Feature importance
importance = model.feature_importances_

feature_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
})

feature_df = feature_df.sort_values(
    by="Importance",
    ascending=False
)

print(feature_df)

# Plot
plt.figure(figsize=(10,6))
plt.barh(
    feature_df["Feature"],
    feature_df["Importance"]
)

plt.xlabel("Importance")
plt.title("Feature Importance")
plt.tight_layout()

plt.savefig(
    "reports/feature_importance.png"
)

plt.show()
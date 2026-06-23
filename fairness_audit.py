import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("data/synthetic_credit_data.csv")

# Encode gender
df["gender"] = df["gender"].map({
    "Male": 0,
    "Female": 1
})

# Features and target
X = df.drop("repayment_status", axis=1)
y = df["repayment_status"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Load trained model
model = joblib.load("models/random_forest.pkl")

# Predictions
y_pred = model.predict(X_test)

# Create results dataframe
results = pd.DataFrame({
    "gender": X_test["gender"],
    "actual": y_test,
    "predicted": y_pred
})

# Separate groups
male = results[results["gender"] == 0]
female = results[results["gender"] == 1]

# Accuracy by group
male_acc = accuracy_score(
    male["actual"],
    male["predicted"]
)

female_acc = accuracy_score(
    female["actual"],
    female["predicted"]
)

print("\n===== FAIRNESS AUDIT =====")
print(f"Male Accuracy   : {male_acc:.4f}")
print(f"Female Accuracy : {female_acc:.4f}")
print(f"Difference      : {abs(male_acc-female_acc):.4f}")
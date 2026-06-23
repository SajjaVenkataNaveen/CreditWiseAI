import pandas as pd
import joblib

# Load model
model = joblib.load("models/random_forest.pkl")

# Load dataset
df = pd.read_csv("data/synthetic_credit_data.csv")

# Encode gender
df["gender"] = df["gender"].map({
    "Male": 0,
    "Female": 1
})

# Pick a sample user
sample_user = df.drop(
    "repayment_status",
    axis=1
).sample(1, random_state=None)

# Predict probability
probability = model.predict_proba(sample_user)[0][1]

# Convert to credit score
credit_score = int(
    300 + probability * 550
)

# Risk category
if credit_score >= 750:
    category = "Excellent"
elif credit_score >= 650:
    category = "Good"
elif credit_score >= 550:
    category = "Fair"
else:
    category = "Poor"

print("\n===== CREDIT REPORT =====")
print(f"Repayment Probability : {probability:.4f}")
print(f"Credit Score          : {credit_score}")
print(f"Category              : {category}")
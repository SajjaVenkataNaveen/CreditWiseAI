import pandas as pd
import numpy as np

np.random.seed(42)

n_users = 10000

# =========================
# BASIC USER DATA
# =========================

data = pd.DataFrame({

    "gender":
        np.random.choice(
            ["Male", "Female"],
            n_users
        ),

    "age":
        np.random.randint(
            18,
            60,
            n_users
        ),

    "education_years":
        np.random.randint(
            5,
            18,
            n_users
        ),

    "income_level":
        np.random.randint(
            5000,
            100000,
            n_users
        ),

    "financial_literacy":
        np.random.randint(
            0,
            101,
            n_users
        ),

    "risk_preference":
        np.random.randint(
            0,
            101,
            n_users
        ),

    "numerical_reasoning":
        np.random.randint(
            0,
            101,
            n_users
        ),

    "social_capital":
        np.random.randint(
            0,
            101,
            n_users
        ),

    "consistency_score":
        np.random.randint(
            0,
            101,
            n_users
        ),

    "response_time":
        np.random.uniform(
            30,
            300,
            n_users
        ),

    "answer_changes":
        np.random.randint(
            0,
            10,
            n_users
        ),

    "session_duration":
        np.random.uniform(
            5,
            30,
            n_users
        ),

    "mobile_usage_score":
        np.random.randint(
            0,
            101,
            n_users
        ),

    "skipped_questions":
        np.random.randint(
            0,
            6,
            n_users
        )
})

# =========================
# NEW FINANCIAL FEATURES
# =========================

data["expenses"] = (
    data["income_level"]
    *
    np.random.uniform(
        0.30,
        0.95,
        n_users
    )
).astype(int)

data["savings"] = (
    data["income_level"]
    -
    data["expenses"]
)

data["savings_rate"] = (
    data["savings"]
    /
    data["income_level"]
) * 100

# =========================
# REPAYMENT SCORE
# =========================

repayment_score = (

    0.20 * data["financial_literacy"]

    + 0.15 * data["numerical_reasoning"]

    + 0.10 * data["social_capital"]

    + 0.10 * data["consistency_score"]

    + 0.10 * data["mobile_usage_score"]

    + 0.10 * data["savings_rate"]

    + 0.10 * (
        data["income_level"] / 1000
    )

    - 0.10 * data["risk_preference"]

    - 0.05 * data["skipped_questions"]

)

threshold = np.median(
    repayment_score
)

data["repayment_status"] = (
    repayment_score > threshold
).astype(int)

# =========================
# SAVE DATASET
# =========================

data.to_csv(
    "data/synthetic_credit_data.csv",
    index=False
)

print("\n===== DATASET CREATED =====")

print(data.head())

print(
    "\nDataset Shape:",
    data.shape
)

print(
    "\nColumns:\n",
    data.columns.tolist()
)
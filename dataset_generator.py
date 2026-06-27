import pandas as pd
import numpy as np

np.random.seed(42)

n_users = 10000

# ==========================================
# USER INFORMATION
# ==========================================

data = pd.DataFrame({

    "gender": np.random.choice(
        ["Male", "Female"],
        n_users
    ),

    "age": np.random.randint(
        18,
        60,
        n_users
    ),

    "education_years": np.random.randint(
        5,
        18,
        n_users
    ),

    "income_level": np.random.randint(
        5000,
        100000,
        n_users
    ),

    "financial_literacy": np.random.randint(
        20,
        101,
        n_users
    ),

    "numerical_reasoning": np.random.randint(
        20,
        101,
        n_users
    ),

    "risk_preference": np.random.randint(
        0,
        101,
        n_users
    ),

    "social_capital": np.random.randint(
        20,
        101,
        n_users
    ),

    "consistency_score": np.random.randint(
        20,
        101,
        n_users
    ),

    "response_time": np.random.uniform(
        40,
        240,
        n_users
    ),

    "answer_changes": np.random.randint(
        0,
        8,
        n_users
    ),

    "session_duration": np.random.uniform(
        8,
        25,
        n_users
    ),

    "mobile_usage_score": np.random.randint(
        20,
        101,
        n_users
    ),

    "skipped_questions": np.random.randint(
        0,
        5,
        n_users
    )

})

# ==========================================
# FINANCIAL INFORMATION
# ==========================================

expense_ratio = np.random.uniform(
    0.30,
    1.10,
    n_users
)

data["expenses"] = (
    data["income_level"] *
    expense_ratio
).astype(int)

# ==========================================
# PSYCHOMETRIC SCORE
# ==========================================

data["psychometric_score"] = (

    0.30 * data["financial_literacy"] +

    0.25 * data["numerical_reasoning"] +

    0.20 * data["consistency_score"] +

    0.15 * data["social_capital"] +

    0.10 * (100 - data["risk_preference"])

).clip(0, 100).round(2)

# ==========================================
# NORMALIZED COMPONENTS
# ==========================================

psychometric_component = (
    data["psychometric_score"] / 100
)

behavior_component = (
        0.30 * (
        (100 - data["skipped_questions"] * 20) / 100
    )

    +

    0.25 * (
        (100 - data["answer_changes"] * 12.5) / 100
    )

    +

    0.25 * (
        data["mobile_usage_score"] / 100
    )

    +

    0.20 * (
        1 -
        (
            np.abs(
                data["response_time"] - 120
            ) / 120
        )
    )

).clip(0, 1)

financial_component = (

    0.55 * (
        data["income_level"] / 100000
    )

    +

    0.45 * (
        1 -
        (
            data["expenses"] /
            data["income_level"]
        ).clip(0, 2)
    )

).clip(0, 1)

# ==========================================
# CREDIT SCORE
# ==========================================

psychometric_component = (
    data["psychometric_score"] / 100
)

financial_component = (

    0.50 * (data["income_level"] / 100000)

    +

    0.50 * (
        1 -
        (
            data["expenses"] /
            data["income_level"]
        ).clip(0,1)
    )

).clip(0,1)

behavior_component = (

    0.35 * (
        (100 - data["skipped_questions"]*20)/100
    )

    +

    0.25 * (
        (100 - data["answer_changes"]*12.5)/100
    )

    +

    0.20 * (
        data["mobile_usage_score"]/100
    )

    +

    0.20 * (
        1 -
        np.abs(
            data["response_time"]-120
        )/120
    )

).clip(0,1)

credit_score = (

    300

    +

    psychometric_component * 275

    +

    financial_component * 165

    +

    behavior_component * 110

)

# ==========================================
# BONUSES
# ==========================================

credit_score += np.where(
    data["psychometric_score"] >= 90,
    55,
    0
)

credit_score += np.where(
    data["psychometric_score"] >= 80,
    25,
    0
)

credit_score += np.where(
    data["income_level"] >= 70000,
    20,
    0
)

credit_score += np.where(
    data["expenses"] <
    data["income_level"]*0.40,
    35,
    0
)

credit_score += np.where(
    (
        data["psychometric_score"] >= 85
    )
    &
    (
        data["expenses"] <
        data["income_level"]*0.50
    ),
    35,
    0
)

# ==========================================
# PENALTIES
# ==========================================

credit_score -= np.where(
    data["psychometric_score"] < 40,
    80,
    0
)

credit_score -= np.where(
    data["expenses"] >
    data["income_level"],
    80,
    0
)

credit_score -= np.where(
    data["risk_preference"] > 80,
    35,
    0
)

# Small natural randomness

credit_score += np.random.normal(
    0,
    8,
    n_users
)

credit_score = np.clip(
    credit_score,
    300,
    850
)

data["credit_score"] = (
    credit_score.round()
).astype(int)

# ==========================================
# REPAYMENT STATUS
# ==========================================

data["repayment_status"] = np.where(

    data["credit_score"] >= 650,

    1,

    0

)

# ==========================================
# SAVE DATASET
# ==========================================

data.to_csv(
    "data/synthetic_credit_data.csv",
    index=False
)

# ==========================================
# OUTPUT
# ==========================================

print("\n========== DATASET CREATED ==========\n")

print(data.head())

print("\nDataset Shape :")
print(data.shape)

print("\nCredit Score Statistics :")
print(data["credit_score"].describe())

print("\nPsychometric Score Statistics :")
print(data["psychometric_score"].describe())

print("\nRepayment Status Distribution :")
print(data["repayment_status"].value_counts())

print("\nColumns :")
print(data.columns.tolist())

print("\nDataset saved successfully to:")
print("data/synthetic_credit_data.csv")
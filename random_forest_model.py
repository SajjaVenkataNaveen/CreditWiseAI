import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv(
    "data/synthetic_credit_data.csv"
)

df["gender"] = df["gender"].map({
    "Male":0,
    "Female":1
})

# ==========================================
# FEATURES
# ==========================================

X = df.drop(
    ["credit_score","repayment_status"],
    axis=1
)

# Target

y = df["credit_score"]

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42,

    shuffle=True

)

# ==========================================
# MODEL
# ==========================================

model = RandomForestRegressor(

    n_estimators=150,

    max_depth=15,

    min_samples_split=4,

    min_samples_leaf=2,

    max_features="sqrt",

    random_state=42,

    n_jobs=-1

)

# ==========================================
# TRAIN
# ==========================================

model.fit(

    X_train,

    y_train

)

# ==========================================
# PREDICTION
# ==========================================

predictions = model.predict(

    X_test

)

# ==========================================
# METRICS
# ==========================================

mae = mean_absolute_error(

    y_test,

    predictions

)


rmse = np.sqrt(

    mean_squared_error(

        y_test,

        predictions

    )

)

r2 = r2_score(

    y_test,

    predictions

)

print("\n========== RANDOM FOREST REGRESSOR ==========\n")

print(f"MAE  : {mae:.2f}")

print(f"RMSE : {rmse:.2f}")

print(f"R²   : {r2:.4f}")

# ==========================================
# FEATURE IMPORTANCE
# ==========================================

importance = pd.DataFrame({

    "Feature":X.columns,

    "Importance":model.feature_importances_

})

importance = importance.sort_values(

    by="Importance",

    ascending=False

)

print("\n========== FEATURE IMPORTANCE ==========\n")

print(importance)

print("\nTop 5 Features")

print(
    importance.tail(5)
)
# ==========================================
# SAVE FEATURE IMPORTANCE GRAPH
# ==========================================

plt.figure(figsize=(10,7))

importance = importance.sort_values(
    "Importance",
    ascending=True
)

plt.barh(
    importance["Feature"],
    importance["Importance"]
)

plt.xlabel("Feature Importance")
plt.title("CreditWise AI Feature Importance")

for i, value in enumerate(importance["Importance"]):
    plt.text(
        value + 0.002,
        i,
        f"{value:.3f}",
        va="center",
        fontsize=8
    )

plt.tight_layout()

plt.savefig(
    "reports/feature_importance.png",
    dpi=300
)

plt.close()

# ==========================================
# SAVE MODEL
# ==========================================

joblib.dump(

    model,

    "models/random_forest.pkl"

)

print("\nModel Saved Successfully!")
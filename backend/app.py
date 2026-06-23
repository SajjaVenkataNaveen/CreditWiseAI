from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "message": "CreditWise AI API is live"
    })

model = joblib.load("../models/random_forest.pkl")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    gender = 1 if data["gender"] == "Female" else 0

    income = int(data["income_level"])

    expenses = int(data["expenses"])

    savings = income - expenses

    savings_rate = (
        savings / income
    ) * 100 if income > 0 else 0

    input_data = pd.DataFrame([{

        "gender": gender,

        "age":
            int(data["age"]),

        "education_years":
            int(data["education_years"]),

        "income_level":
            income,

        "financial_literacy":
            float(data["financial_literacy"]),

        "risk_preference":
            float(data["risk_preference"]),

        "numerical_reasoning":
            float(data["numerical_reasoning"]),

        "social_capital":
            float(data["social_capital"]),

        "consistency_score":
            float(data["consistency_score"]),

        "response_time":
            float(data["response_time"]),

        "answer_changes":
            int(data["answer_changes"]),

        "session_duration":
            float(data["session_duration"]),

        "mobile_usage_score":
            float(data["mobile_usage_score"]),

        "skipped_questions":
            int(data["skipped_questions"]),

        "expenses":
    int(data["expenses"]),

"savings":
    float(data["savings"]),

"savings_rate":
    float(data["savings_rate"]),

    }])

    input_data = input_data[[
        "gender",
        "age",
        "education_years",
        "income_level",
        "financial_literacy",
        "risk_preference",
        "numerical_reasoning",
        "social_capital",
        "consistency_score",
        "response_time",
        "answer_changes",
        "session_duration",
        "mobile_usage_score",
        "skipped_questions",
        "expenses",
        "savings",
        "savings_rate"
    ]]

    probability = model.predict_proba(
        input_data
    )[0][1]

    credit_score = int(
        300 + probability * 550
    )

    if credit_score >= 750:
        category = "Excellent"
    elif credit_score >= 650:
        category = "Good"
    elif credit_score >= 550:
        category = "Fair"
    else:
        category = "Poor"

    return jsonify({
        "credit_score": credit_score,
        "probability": round(probability, 4),
        "category": category
    })

if __name__ == "__main__":
    app.run(debug=True)
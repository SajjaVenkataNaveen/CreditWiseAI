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

    psychometric_score = (

        0.30 * float(data["financial_literacy"])

        + 0.25 * float(data["numerical_reasoning"])

        + 0.20 * float(data["consistency_score"])

        + 0.15 * float(data["social_capital"])

        + 0.10 * (
            100 - float(data["risk_preference"])
        )

    )

    input_data = pd.DataFrame([{

    "gender": gender,

    "age": int(data["age"]),

    "education_years": int(data["education_years"]),

    "income_level": income,

    "financial_literacy": float(data["financial_literacy"]),

    "numerical_reasoning": float(data["numerical_reasoning"]),

    "risk_preference": float(data["risk_preference"]),

    "social_capital": float(data["social_capital"]),

    "consistency_score": float(data["consistency_score"]),

    "response_time": float(data["response_time"]),

    "answer_changes": int(data["answer_changes"]),

    "session_duration": float(data["session_duration"]),

    "mobile_usage_score": float(data["mobile_usage_score"]),

    "skipped_questions": int(data["skipped_questions"]),

    "expenses": expenses,

    "psychometric_score": psychometric_score

}])

    input_data = input_data[[

    "gender",

    "age",

    "education_years",

    "income_level",

    "financial_literacy",

    "numerical_reasoning",

    "risk_preference",

    "social_capital",

    "consistency_score",

    "response_time",

    "answer_changes",

    "session_duration",

    "mobile_usage_score",

    "skipped_questions",

    "expenses",

    "psychometric_score"

]]

    credit_score = int(
    model.predict(input_data)[0]
)

    if credit_score >= 750:
        category = "Excellent"
    elif credit_score >= 650:
        category = "Good"
    elif credit_score >= 550:
        category = "Fair"
    else:
        category = "Poor"

    repayment_probability = round((credit_score - 300) / 550, 4)

    repayment_probability = round((credit_score - 300) / 550, 2)

    return jsonify({
        "credit_score": credit_score,
        "category": category,
        "repayment_probability": repayment_probability
    })
if __name__ == "__main__":
    app.run(debug=True)
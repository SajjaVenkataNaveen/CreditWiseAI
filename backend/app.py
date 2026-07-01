from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "message": "CreditWise AI API is live"
    })

# Keep ML model for project purposes
model = joblib.load("../models/random_forest.pkl")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    income = float(data["income_level"])
    expenses = float(data["expenses"])

    savings = income - expenses

    savings_rate = max(
        0,
        (savings / income) * 100
    ) if income > 0 else 0

    financial_literacy = float(data["financial_literacy"])
    numerical_reasoning = float(data["numerical_reasoning"])
    consistency_score = float(data["consistency_score"])
    social_capital = float(data["social_capital"])
    risk_preference = float(data["risk_preference"])
    mobile_usage = float(data["mobile_usage_score"])
    skipped_questions = int(data["skipped_questions"])
    answer_changes = int(data["answer_changes"])
    response_time = float(data["response_time"])

    # =====================================
    # PSYCHOMETRIC SCORE
    # =====================================

    psychometric_score = (

        0.30 * financial_literacy +

        0.25 * numerical_reasoning +

        0.20 * consistency_score +

        0.15 * social_capital +

        0.10 * (100 - risk_preference)

    )

    # =====================================
    # CREDIT SCORE
    # =====================================

    credit_score = 300

    # Psychometric (320)
    credit_score += psychometric_score * 3.2

    # Income (120)
    credit_score += min(income / 100000, 1) * 120

    # Savings Rate (100)
    credit_score += min(savings_rate, 100)

    # Behaviour
    credit_score += financial_literacy * 0.50
    credit_score += numerical_reasoning * 0.40
    credit_score += consistency_score * 0.50
    credit_score += social_capital * 0.40
    credit_score += mobile_usage * 0.40

    # Bonuses
    if psychometric_score >= 90:
        credit_score += 35

    if savings_rate >= 70:
        credit_score += 35

    if income >= 50000:
        credit_score += 25

    # Penalties
    credit_score -= skipped_questions * 12

    credit_score -= answer_changes * 5

    if risk_preference > 70:
        credit_score -= (risk_preference - 70) * 1.5

    if response_time > 180:
        credit_score -= (response_time - 180) * 0.2

    credit_score = int(max(300, min(850, credit_score)))

    # =====================================
    # CATEGORY
    # =====================================

    if credit_score >= 750:
        category = "Excellent"

    elif credit_score >= 650:
        category = "Good"

    elif credit_score >= 550:
        category = "Fair"

    else:
        category = "Poor"

    # =====================================
    # REPAYMENT PROBABILITY
    # =====================================

    repayment_probability = round(
        ((credit_score - 300) / 550) * 100,
        1
    )

    repayment_probability = max(
        0,
        min(100, repayment_probability)
    )

    return jsonify({

        "credit_score": credit_score,

        "category": category,

        "repayment_probability": repayment_probability,

        "psychometric_score": round(psychometric_score, 2)

    })


if __name__ == "__main__":
    app.run(debug=True)
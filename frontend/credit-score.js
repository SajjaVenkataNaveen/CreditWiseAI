const psychometricScore =
    Number(
        localStorage.getItem(
            "psychometricScore"
        )
    ) || 0;

const financialData =
    JSON.parse(
        localStorage.getItem(
            "financialData"
        )
    ) || {};

const sectionScores =
    JSON.parse(
        localStorage.getItem(
            "sectionScores"
        )
    ) || {};

const income =
    Number(financialData.income_level) || 0;

const expenses =
    Number(financialData.expenses) || 0;

const savings =
    income - expenses;

const savingsRate =
    income > 0
    ? ((savings / income) * 100).toFixed(1)
    : 0;

/* =========================
   SUMMARY
========================= */

document.getElementById(
    "psychoScore"
).innerText =
    psychometricScore + "/100";

document.getElementById(
    "incomeValue"
).innerText =
    "₹" + income.toLocaleString();

document.getElementById(
    "expenseValue"
).innerText =
    "₹" + expenses.toLocaleString();

document.getElementById(
    "savingValue"
).innerText =
    "₹" + savings.toLocaleString();

/* =========================
   RANDOM FOREST API CALL
========================= */

fetch(
    "http://127.0.0.1:5000/predict",
    {
        method: "POST",

        headers: {
            "Content-Type":
            "application/json"
        },

        body: JSON.stringify({

    gender: financialData.gender,

    age: Number(financialData.age),

    education_years:
        Number(financialData.education_years),

    income_level:
        Number(financialData.income_level),

    expenses:
        Number(financialData.expenses),

    savings:
        savings,

    savings_rate:
        Number(savingsRate),

    financial_literacy:
        sectionScores.financial_literacy,

    risk_preference:
        sectionScores.risk_preference,

    numerical_reasoning:
        sectionScores.numerical_reasoning,

    social_capital:
        sectionScores.social_capital,

    consistency_score:
        sectionScores.consistency_score,

    response_time: 60,

    answer_changes: 2,

    session_duration: 15,

    mobile_usage_score: 70,

    skipped_questions: 1
})
    }
)

.then(response => response.json())

.then(result => {

    const creditScore =
        result.credit_score;

    const label =
        result.category;
    
    let reasons = [];

        if (savings > 20000)
        {
            reasons.push(
                "Strong savings behavior."
            );
        }

        if (
            sectionScores.financial_literacy >= 70
        )
        {
            reasons.push(
                "High financial literacy score."
            );
        }

        if (
            sectionScores.consistency_score >= 70
        )
        {
            reasons.push(
                "Consistent decision making."
            );
        }

        if (
            sectionScores.risk_preference <= 40
        )
        {
            reasons.push(
                "Low financial risk preference."
            );
        }

        if (
            Number(financialData.income_level)
            >= 50000
        )
        {
            reasons.push(
                "Stable income profile."
            );
        }

        document.getElementById(
            "aiReason"
        ).innerHTML =
            `
            <ul>
            ${reasons.map(reason =>
            `<li>${reason}</li>`).join("")}
            </ul>
            `

    document.getElementById(
        "creditScore"
    ).innerText =
        creditScore;

    document.getElementById(
        "scoreLabel"
    ).innerText =
        label;

    document.getElementById(
        "probabilityValue"
    ).innerText =
        (result.probability * 100).toFixed(1) + "%";
    document.getElementById(
    "aiInsight"
).innerHTML = `
    Based on psychometric assessment,
    financial profile and behavioral
    indicators, the Random Forest model
    predicts a credit score of
    <strong>${creditScore}</strong>.

    <br><br>

    Repayment Probability:
    <strong>${(result.probability * 100).toFixed(1)}%</strong>

    <br><br>

    Credit Category:
    <strong>${label}</strong>

    <br><br>

    Savings Rate:
    <strong>${savingsRate}%</strong>
`;

    const recommendationList =
        document.getElementById(
            "recommendationList"
        );

    recommendationList.innerHTML = "";

    let recommendations = [];

    if (label === "Excellent") {

        recommendations = [
            "Maintain current financial discipline",
            "Explore long-term investments",
            "Build larger emergency reserves"
        ];

    } else if (label === "Good") {

        recommendations = [
            "Increase savings rate",
            "Track monthly spending",
            "Improve financial planning"
        ];

    } else if (label === "Fair") {

        recommendations = [
            "Reduce unnecessary expenses",
            "Increase income sources",
            "Maintain consistent savings"
        ];

    } else {

        recommendations = [
            "Create a strict budget",
            "Avoid risky spending",
            "Focus on improving savings habits"
        ];
    }

    recommendations.forEach(item => {

        const li =
            document.createElement("li");

        li.innerText = item;

        recommendationList.appendChild(li);

    });

    const circle =
        document.getElementById(
            "progressCircle"
        );

    const circumference =
        2 * Math.PI * 100;

    const progress =
    Math.min((creditScore - 300) / 600, 1);

    const offset =
        circumference -
        (progress * circumference);

    setTimeout(() => {

        circle.style.strokeDashoffset =
            offset;

    }, 300);

})

.catch(error => {

    console.error(error);

    document.getElementById(
        "scoreLabel"
    ).innerText =
        "Backend Connection Error";

});

document
.getElementById("downloadReportBtn")
.addEventListener("click", () => {

    const { jsPDF } = window.jspdf;

    const doc = new jsPDF();

    const score =
        document.getElementById(
            "creditScore"
        ).innerText;

    const category =
        document.getElementById(
            "scoreLabel"
        ).innerText;

    const repayment =
        document.getElementById(
            "probabilityValue"
        ).innerText;

    doc.setFontSize(24);
    doc.setTextColor(20,40,90);
    doc.text(
        "CreditWise AI Report",
        20,
        20
    );
    doc.line(20,25,190,25);

    doc.setFontSize(14);

    doc.text(
        `Credit Score: ${score}`,
        20,
        50
    );

    doc.text(
        `Category: ${category}`,
        20,
        60
    );

    doc.text(
        `Psychometric Score: ${psychometricScore}/100`,
        20,
        70
    );

    doc.text(
        `Income: Rs. ${income}`,
        20,
        80
    );

    doc.text(
        `Expenses: Rs. ${expenses}`,
        20,
        90
    );

    doc.text(
        `Savings: Rs. ${savings}`,
        20,
        100
    );

    doc.text(
        `Repayment Probability: ${repayment}`,
        20,
        110
    );

    doc.text(
        "AI Insights",
        20,
        130
    );

    doc.setFontSize(12);

    doc.text(
        [
            "• Financial behavior analysed using Random Forest.",
            "• Credit score combines psychometric and financial factors.",
            "• Higher savings and literacy improve score.",
            "• Consistency and numerical reasoning strengthen repayment prediction."
        ],
        20,
        145
    );

    doc.save("CreditWise_Report.pdf");

});
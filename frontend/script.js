const questions = [

{
    section: "Financial Literacy",
    question: "If you save ₹1000 every month for 12 months, how much will you save?",
    options: ["₹10,000", "₹11,000", "₹12,000", "₹13,000"],
    scores: [1,2,4,1]
},

{
    section: "Financial Literacy",
    question: "What is the main purpose of a budget?",
    options: ["Increase spending", "Track and manage money", "Avoid saving", "Take more loans"],
    scores: [1,4,1,1]
},

{
    section: "Financial Literacy",
    question: "An emergency fund should cover approximately:",
    options: ["1 week", "1 month", "3–6 months", "10 years"],
    scores: [1,2,4,1]
},

{
    section: "Financial Literacy",
    question: "Which habit improves financial stability?",
    options: ["Spending all income", "Taking frequent loans", "Ignoring expenses", "Maintaining savings"],
    scores: [1,1,1,4]
},

{
    section: "Financial Literacy",
    question: "What is compound interest?",
    options: [
        "Interest on principal only",
        "Interest on interest and principal",
        "Bank fee",
        "Loan penalty"
    ],
    scores: [1,4,1,1]
},

{
    section: "Risk Preference",
    question: "You receive ₹10,000 unexpectedly. What do you do?",
    options: [
        "Save all",
        "Save most and spend some",
        "Spend all",
        "Take more risks"
    ],
    scores: [3,4,1,1]
},

{
    section: "Risk Preference",
    question: "Preferred investment option?",
    options: [
        "Fixed Deposit",
        "Mutual Fund",
        "Crypto Only",
        "Gambling"
    ],
    scores: [4,3,1,0]
},

{
    section: "Risk Preference",
    question: "Before taking a loan you:",
    options: [
        "Compare lenders",
        "Take first offer",
        "Ask friends only",
        "Ignore interest rate"
    ],
    scores: [4,1,1,0]
},

{
    section: "Risk Preference",
    question: "Investment drops 10%. You:",
    options: [
        "Panic sell",
        "Review and wait",
        "Borrow more",
        "Ignore completely"
    ],
    scores: [1,4,1,2]
},

{
    section: "Risk Preference",
    question: "Long-term investing means:",
    options: [
        "1 week",
        "1 month",
        "1 year",
        "5+ years"
    ],
    scores: [0,1,2,4]
},

{
    section: "Numerical Reasoning",
    question: "20% of ₹5000 equals:",
    options: ["₹500", "₹1000", "₹1500", "₹2000"],
    scores: [1,4,1,1]
},

{
    section: "Numerical Reasoning",
    question: "₹100 increases by 10%. New value?",
    options: ["₹105", "₹110", "₹115", "₹120"],
    scores: [1,4,1,1]
},

{
    section: "Numerical Reasoning",
    question: "Income ₹50,000 and expenses ₹35,000. Savings?",
    options: ["₹10,000", "₹15,000", "₹20,000", "₹25,000"],
    scores: [1,4,1,1]
},

{
    section: "Numerical Reasoning",
    question: "Which is largest?",
    options: ["0.5", "0.75", "0.8", "0.95"],
    scores: [1,2,3,4]
},

{
    section: "Numerical Reasoning",
    question: "EMI mainly affects your:",
    options: [
        "Savings capacity",
        "Hair style",
        "Mobile signal",
        "Education"
    ],
    scores: [4,0,0,1]
},

{
    section: "Social Capital",
    question: "People trust you financially?",
    options: ["Never", "Rarely", "Often", "Always"],
    scores: [1,2,3,4]
},

{
    section: "Social Capital",
    question: "Do you repay borrowed money on time?",
    options: ["Never", "Sometimes", "Usually", "Always"],
    scores: [1,2,3,4]
},

{
    section: "Social Capital",
    question: "Community participation?",
    options: ["None", "Rare", "Regular", "Active"],
    scores: [1,2,3,4]
},

{
    section: "Social Capital",
    question: "Can someone recommend you financially?",
    options: ["No", "Maybe", "Likely", "Definitely"],
    scores: [1,2,3,4]
},

{
    section: "Social Capital",
    question: "Family support in emergencies?",
    options: ["None", "Limited", "Moderate", "Strong"],
    scores: [1,2,3,4]
},

{
    section: "Consistency",
    question: "How often do you change important decisions?",
    options: ["Very often", "Often", "Sometimes", "Rarely"],
    scores: [1,2,3,4]
},

{
    section: "Consistency",
    question: "Do you finish tasks you start?",
    options: ["Never", "Rarely", "Usually", "Always"],
    scores: [1,2,3,4]
},

{
    section: "Consistency",
    question: "How often do you miss deadlines?",
    options: ["Always", "Often", "Sometimes", "Rarely"],
    scores: [1,2,3,4]
},

{
    section: "Consistency",
    question: "How consistent are your spending habits?",
    options: ["Poor", "Average", "Good", "Excellent"],
    scores: [1,2,3,4]
},

{
    section: "Consistency",
    question: "Do you review expenses regularly?",
    options: ["Never", "Sometimes", "Monthly", "Weekly"],
    scores: [1,2,3,4]
}

];

let currentQuestion = 0;
let answers = new Array(questions.length).fill(null);

/* =========================
   ASSESSMENT PAGE
========================= */

if (document.getElementById("nextBtn")) {

    let currentQuestion = 0;
    let answers = new Array(questions.length).fill(null);

    const sectionTitle =
        document.getElementById("sectionTitle");

    const progressBar =
        document.getElementById("progressBar");

    const progressText =
        document.getElementById("progressText");

    const questionCard =
        document.querySelector(".question-card");

    const nextBtn =
        document.getElementById("nextBtn");

    const prevBtn =
        document.getElementById("prevBtn");

    function loadQuestion() {

        const q = questions[currentQuestion];

        sectionTitle.innerText = q.section;

        progressText.innerText =
            `Question ${currentQuestion + 1} of ${questions.length}`;

        progressBar.style.width =
            `${((currentQuestion + 1) / questions.length) * 100}%`;

        let html = `<p>${q.question}</p>`;

        q.options.forEach((option, index) => {

            const checked =
                answers[currentQuestion] === q.scores[index]
                    ? "checked"
                    : "";

            html += `
                <label>
                    <input
                        type="radio"
                        name="answer"
                        value="${q.scores[index]}"
                        ${checked}
                    >
                    ${option}
                </label>
            `;
        });

        questionCard.innerHTML = html;

        prevBtn.disabled = currentQuestion === 0;

        nextBtn.innerText =
            currentQuestion === questions.length - 1
            ? "Finish"
            : "Next";
    }

    nextBtn.addEventListener("click", () => {

        const selected =
            document.querySelector(
                'input[name="answer"]:checked'
            );

        if (!selected) {
            alert("Please select an answer.");
            return;
        }

        answers[currentQuestion] =
            Number(selected.value);

        if (currentQuestion < questions.length - 1) {

            currentQuestion++;
            loadQuestion();

        } else {

            const totalScore =
    answers.reduce(
        (sum, score) => sum + score,
        0
    );

/* SECTION SCORES */

const financialLiteracyRaw =
    answers.slice(0, 5)
    .reduce((a, b) => a + b, 0);

const riskPreferenceRaw =
    answers.slice(5, 10)
    .reduce((a, b) => a + b, 0);

const numericalReasoningRaw =
    answers.slice(10, 15)
    .reduce((a, b) => a + b, 0);

const socialCapitalRaw =
    answers.slice(15, 20)
    .reduce((a, b) => a + b, 0);

const consistencyRaw =
    answers.slice(20, 25)
    .reduce((a, b) => a + b, 0);

/* CONVERT TO 0-100 */

const sectionScores = {

    financial_literacy:
        Math.round(
            (financialLiteracyRaw / 20) * 100
        ),

    risk_preference:
        Math.round(
            (riskPreferenceRaw / 20) * 100
        ),

    numerical_reasoning:
        Math.round(
            (numericalReasoningRaw / 20) * 100
        ),

    social_capital:
        Math.round(
            (socialCapitalRaw / 20) * 100
        ),

    consistency_score:
        Math.round(
            (consistencyRaw / 20) * 100
        )
};

localStorage.setItem(
    "sectionScores",
    JSON.stringify(sectionScores)
);

localStorage.setItem(
    "psychometricScore",
    totalScore
);

window.location.href =
    "details.html";
        }
    });

    prevBtn.addEventListener("click", () => {

        if (currentQuestion > 0) {

            const selected =
                document.querySelector(
                    'input[name="answer"]:checked'
                );

            if (selected) {
                answers[currentQuestion] =
                    Number(selected.value);
            }

            currentQuestion--;
            loadQuestion();
        }
    });

    loadQuestion();
}


/* =========================
   DETAILS PAGE
========================= */

if (
    document.getElementById("income") &&
    document.getElementById("expenses")
) {

    const incomeInput =
        document.getElementById("income");

    const expenseInput =
        document.getElementById("expenses");

    function updateSnapshot() {

        const income =
            Number(incomeInput.value) || 0;

        const expense =
            Number(expenseInput.value) || 0;

        const savings =
            income - expense;

        const rate =
            income > 0
            ? ((savings / income) * 100).toFixed(1)
            : 0;

        const incomeView =
            document.getElementById("incomeView");

        const expenseView =
            document.getElementById("expenseView");

        const savingView =
            document.getElementById("savingView");

        const rateView =
            document.getElementById("rateView");

        if (incomeView)
            incomeView.innerText =
                "₹" + income.toLocaleString();

        if (expenseView)
            expenseView.innerText =
                "₹" + expense.toLocaleString();

        if (savingView)
            savingView.innerText =
                "₹" + savings.toLocaleString();

        if (rateView)
            rateView.innerText =
                rate + "%";
    }

    incomeInput.addEventListener(
        "input",
        updateSnapshot
    );

    expenseInput.addEventListener(
        "input",
        updateSnapshot
    );

    updateSnapshot();
}
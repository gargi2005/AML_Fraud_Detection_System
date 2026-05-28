import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AML Fraud Detection",
    page_icon="🛡️",
    layout="centered"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #0f172a, #1e293b);
    color: white;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #38bdf8;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 30px;
    font-size: 18px;
}

.box {
    background-color: #1e293b;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 0px 20px rgba(0,0,0,0.3);
}

.stButton>button {
    width: 100%;
    background-color: #38bdf8;
    color: black;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    height: 50px;
    border: none;
}

.stButton>button:hover {
    background-color: #0ea5e9;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ---------------- #

model = joblib.load("models/fraud_model.pkl")
model_columns = joblib.load("models/model_columns.pkl")

# ---------------- TITLE ---------------- #

st.markdown(
    '<div class="title">🛡️ AML Fraud Detection System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Detect Suspicious Financial Transactions</div>',
    unsafe_allow_html=True
)

# ---------------- INPUTS ---------------- #

with st.container():

    st.markdown('<div class="box">', unsafe_allow_html=True)

    transaction_amount = st.number_input(
        "💸 Transaction Amount",
        min_value=0.0,
        value=1000.0
    )

    avg_amount = st.number_input(
        "📊 Average Transaction Amount",
        min_value=0.0,
        value=5000.0
    )

    balance = st.number_input(
        "🏦 Account Balance",
        min_value=0.0,
        value=20000.0
    )

    if st.button("🔍 Check Transaction"):

        # Input Data
        input_data = {
            'TransactionAmount': transaction_amount,
            'TransactionType': 1,
            'ModeOfTransactionCode': 1,
            'transaction_hour': 12,
            'day_of_week': 2,
            'Balance': balance,
            'MinimumBalance': 5000,
            'avg_account_txn_amount': avg_amount,
            'max_account_txn_amount': avg_amount * 2,
            'account_tenure_days': 365,
            'Gender': 1,
            'RiskCategoryId': 2,
            'transaction_month': 5,
            'transaction_year': 2025,
            'account_open_month': 1,
            'account_open_year': 2020
        }

        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])

        # Dummy Encoding
        input_df = pd.get_dummies(input_df)

        # Match Training Columns
        input_df = input_df.reindex(
            columns=model_columns,
            fill_value=0
        )

        # ---------------- FRAUD LOGIC ---------------- #

        if transaction_amount > (avg_amount * 20):

            result = "Fraud"

        else:

            prediction = model.predict(input_df)[0]

            if prediction == 1:
                result = "Fraud"
            else:
                result = "Safe"

        # ---------------- RESULT ---------------- #

        st.markdown("## Result")

        if result == "Fraud":
            st.error("🚨 Fraud Transaction Detected")

        else:
            st.success("✅ Safe Transaction")

    st.markdown('</div>', unsafe_allow_html=True)
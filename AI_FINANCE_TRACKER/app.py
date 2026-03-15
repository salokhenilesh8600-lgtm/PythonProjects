import streamlit as st
from streamlit_option_menu import option_menu

from database import add_transaction
from expense_manager import get_dataframe
from ai_modules.budget_predictor import predict_spending
from ai_modules.fraud_detector import detect_fraud
from ai_modules.finance_chatbot import chat

st.set_page_config(page_title="AI Finance Tracker", layout="wide")

st.title("💰 AI Personal Finance Tracker")

# Top Navigation Menu
selected = option_menu(
    menu_title=None,
    options=[
        "Add Expense",
        "Dashboard",
        "AI Prediction",
        "Fraud Detection",
        "AI Chat"
    ],
    icons=[
        "plus-circle",
        "bar-chart",
        "graph-up",
        "shield-exclamation",
        "chat-dots"
    ],
    orientation="horizontal"
)

# -----------------------------
# Add Expense
# -----------------------------
if selected == "Add Expense":

    st.subheader("Add Transaction")

    t = st.selectbox("Type", ["income", "expense"])
    amount = st.number_input("Amount")
    cat = st.text_input("Category")
    desc = st.text_input("Description")
    date = st.text_input("Date")

    if st.button("Add Transaction"):
        add_transaction(t, amount, cat, desc, date)
        st.success("Transaction Added")

# -----------------------------
# Dashboard
# -----------------------------
elif selected == "Dashboard":

    st.subheader("Finance Dashboard")

    df = get_dataframe()

    st.dataframe(df)

    st.bar_chart(df.groupby("category")["amount"].sum())

# -----------------------------
# AI Prediction
# -----------------------------
elif selected == "AI Prediction":

    st.subheader("AI Spending Prediction")

    df = get_dataframe()

    pred = predict_spending(df)

    st.success(f"Predicted Next Month Spending: ₹{pred}")

# -----------------------------
# Fraud Detection
# -----------------------------
elif selected == "Fraud Detection":

    st.subheader("Fraud Detection")

    df = get_dataframe()

    fraud = detect_fraud(df)

    st.write("Suspicious Transactions")

    st.dataframe(fraud)

# -----------------------------
# AI Chat
# -----------------------------
elif selected == "AI Chat":

    st.subheader("Finance AI Assistant")

    df = get_dataframe()

    q = st.text_input("Ask a question")

    if st.button("Ask AI"):
        answer = chat(df, q)
        st.write(answer)
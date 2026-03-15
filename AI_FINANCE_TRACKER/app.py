import streamlit as st
import pandas as pd
from database import add_transaction, get_transactions
from expense_manager import get_dataframe
from ai_modules.budget_predictor import predict_spending
from ai_modules.fraud_detector import detect_fraud
from ai_modules.finance_chatbot import chat

st.title("AI Personal Finance Tracker")

menu = ["Add Expense","Dashboard","AI Prediction","Fraud Detection","AI Chat"]

choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Expense":

    t = st.selectbox("Type",["income","expense"])
    amount = st.number_input("Amount")
    cat = st.text_input("Category")
    desc = st.text_input("Description")
    date = st.text_input("Date")

    if st.button("Add"):
        add_transaction(t,amount,cat,desc,date)
        st.success("Transaction Added")


elif choice == "Dashboard":

    df = get_dataframe()

    st.dataframe(df)

    st.bar_chart(df.groupby("category")["amount"].sum())


elif choice == "AI Prediction":

    df = get_dataframe()

    pred = predict_spending(df)

    st.write("Predicted Next Month Spending:", pred)


elif choice == "Fraud Detection":

    df = get_dataframe()

    fraud = detect_fraud(df)

    st.write("Suspicious Transactions")

    st.dataframe(fraud)


elif choice == "AI Chat":

    df = get_dataframe()

    q = st.text_input("Ask AI")

    if st.button("Ask"):
        ans = chat(df,q)
        st.write(ans)
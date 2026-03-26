import streamlit as st
from utils.fetch_stock import get_stock_data
from models.anomaly_model import detect_anomalies

st.title("🚨 Stock Anomaly Detection")

ticker = st.text_input("Enter Stock Ticker", "AAPL")

if st.button("Detect Anomalies"):
    df = get_stock_data(ticker)

    df = detect_anomalies(df)

    st.subheader("📊 Data with Anomalies")
    st.dataframe(df.tail())

    anomalies = df[df["anomaly"] == -1]

    st.subheader("🚨 Detected Anomalies")

    if not anomalies.empty:
        st.dataframe(anomalies)
    else:
        st.success("No anomalies detected 🎉")
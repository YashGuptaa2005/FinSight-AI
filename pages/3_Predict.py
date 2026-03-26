import streamlit as st
from utils.fetch_stock import get_stock_data
from models.prediction_model import train_model

st.title("📈 Stock Prediction")

ticker = st.text_input("Enter Stock Ticker", "AAPL")

if st.button("Predict"):

    df = get_stock_data(ticker)

    # -------- FIX COLUMNS --------
    df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

    close_col = "Close"

    latest = float(df[close_col].iloc[-1])
    high = float(df[close_col].max())
    low = float(df[close_col].min())

    # -------- METRICS --------
    col1, col2, col3 = st.columns(3)
    col1.metric("📊 Current Price", f"{latest:.2f}")
    col2.metric("🔼 High", f"{high:.2f}")
    col3.metric("🔽 Low", f"{low:.2f}")

    # -------- MODEL --------
    model = train_model(df)
    prediction = model.predict([[latest]])

    st.markdown("---")
    st.subheader("🤖 AI Prediction")

    if prediction[0] == 1:
        st.success("📈 Stock likely to go UP")
    else:
        st.error("📉 Stock likely to go DOWN")
import streamlit as st
from utils.fetch_stock import get_stock_data
from models.prediction_model import train_model

st.title("📈 Stock Prediction")

ticker = st.text_input("Enter Stock Ticker", "AAPL")

if st.button("Predict"):
    # Fetch data
    df = get_stock_data(ticker)

    # Train model
    model = train_model(df)

    # Get correct Close column
    close_col = [col for col in df.columns if "Close" in col][0]

    # Get latest value
    latest_close = float(df.iloc[-1][close_col])

    # ✅ IMPORTANT: pass as simple list (no DataFrame)
    prediction = model.predict([[latest_close]])

    # Output
    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.success("Stock likely to go UP 📈")
    else:
        st.error("Stock likely to go DOWN 📉")
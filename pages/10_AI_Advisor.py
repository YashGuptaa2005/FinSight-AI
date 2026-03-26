import streamlit as st
from utils.fetch_stock import get_stock_data
from models.prediction_model import train_model
from models.sentiment_model import analyze_sentiment, load_model
from utils.fetch_news import load_news_data

st.title("🤖 AI Financial Advisor")

ticker = st.text_input("Enter Stock Ticker", "AAPL")

if st.button("Get Recommendation"):

    # -------- STOCK PREDICTION --------
    df = get_stock_data(ticker)

    model_pred = train_model(df)

    close_col = [col for col in df.columns if "Close" in col][0]
    latest_close = float(df.iloc[-1][close_col])

    pred = model_pred.predict([[latest_close]])

    # -------- NEWS SENTIMENT --------
    news_df = load_news_data()

    model_sent = load_model()

    sample_text = news_df["Title"].iloc[0]

    result = analyze_sentiment(sample_text, model_sent)

    sentiment = result[0]['label']

    # -------- FINAL DECISION --------
    st.subheader("🧠 AI Decision")

    if pred[0] == 1 and sentiment == "positive":
        st.success("📈 BUY — Strong positive signals")
    elif pred[0] == 0 and sentiment == "negative":
        st.error("📉 SELL — Strong negative signals")
    else:
        st.warning("⚖️ HOLD — Mixed signals")
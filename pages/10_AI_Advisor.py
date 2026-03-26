import streamlit as st
from utils.fetch_stock import get_stock_data
from models.prediction_model import train_model
from models.sentiment_model import analyze_sentiment, load_model
from utils.fetch_news import load_news_data

st.title("🤖 AI Financial Advisor")

ticker = st.text_input("Enter Ticker", "AAPL")

if st.button("Get Advice"):

    df = get_stock_data(ticker)
    df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

    latest = float(df["Close"].iloc[-1])

    model = train_model(df)
    pred = model.predict([[latest]])

    news = load_news_data()
    model_sent = load_model()

    result = analyze_sentiment(news["Title"].iloc[0], model_sent)
    sentiment = result[0]['label']

    if pred[0] == 1 and sentiment == "positive":
        st.success("📈 BUY")
    elif pred[0] == 0 and sentiment == "negative":
        st.error("📉 SELL")
    else:
        st.warning("⚖️ HOLD")
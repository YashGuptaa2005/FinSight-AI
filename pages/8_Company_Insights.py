import streamlit as st
from utils.fetch_stock import get_stock_data
from utils.fetch_news import load_news_data
from models.sentiment_model import analyze_sentiment, load_model

st.title("🏢 Company Insights Dashboard")

ticker = st.text_input("Enter Company Ticker", "AAPL")

if st.button("Analyze Company"):

    # Fetch stock data
    stock_df = get_stock_data(ticker)

    # ✅ FIX: Flatten multi-level columns (yfinance issue)
    stock_df.columns = [col[0] if isinstance(col, tuple) else col for col in stock_df.columns]

    st.subheader("📈 Stock Data")
    st.line_chart(stock_df.set_index("Date")["Close"])

    # Load news data
    news_df = load_news_data()

    st.subheader("📰 Sample News")
    st.dataframe(news_df.head())

    # Load model
    model = load_model()

    # Take first news headline
    sample_text = news_df["Title"].iloc[0]

    # Analyze sentiment
    result = analyze_sentiment(sample_text, model)

    label = result[0]['label']
    score = result[0]['score']

    st.subheader("🧠 AI Insight")

    if label == "positive":
        st.success(f"Positive Outlook 📈 (Confidence: {score:.2f})")
    elif label == "negative":
        st.error(f"Negative Outlook 📉 (Confidence: {score:.2f})")
    else:
        st.warning(f"Neutral Outlook 😐 (Confidence: {score:.2f})")
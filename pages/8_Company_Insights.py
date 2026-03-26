import streamlit as st
from utils.fetch_stock import get_stock_data
from utils.fetch_news import load_news_data
from models.sentiment_model import analyze_sentiment, load_model

st.title("🏢 Company Insights Dashboard")

ticker = st.text_input("Enter Company Ticker", "AAPL")

if st.button("Analyze"):

    stock_df = get_stock_data(ticker)

    # Fix columns
    stock_df.columns = [col[0] if isinstance(col, tuple) else col for col in stock_df.columns]

    news_df = load_news_data()
    model = load_model()

    tab1, tab2, tab3 = st.tabs(["📈 Stock", "📰 News", "🧠 AI Insight"])

    # -------- STOCK TAB --------
    with tab1:
        close = stock_df["Close"]

        col1, col2, col3 = st.columns(3)
        col1.metric("Current", f"{close.iloc[-1]:.2f}")
        col2.metric("High", f"{close.max():.2f}")
        col3.metric("Low", f"{close.min():.2f}")

        st.line_chart(stock_df.set_index("Date")["Close"])

    # -------- NEWS TAB --------
    with tab2:
        st.dataframe(news_df.head())

    # -------- AI TAB --------
    with tab3:
        sample = news_df["Title"].iloc[0]
        result = analyze_sentiment(sample, model)

        label = result[0]['label']
        score = result[0]['score']

        st.metric("Sentiment", label.upper())
        st.metric("Confidence", f"{score:.2f}")

        if label == "positive":
            st.success("📈 Positive Outlook")
        elif label == "negative":
            st.error("📉 Negative Outlook")
        else:
            st.warning("😐 Neutral Outlook")
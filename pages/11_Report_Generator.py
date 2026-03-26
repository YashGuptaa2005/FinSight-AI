import streamlit as st
from utils.fetch_stock import get_stock_data
from utils.fetch_news import load_news_data
from models.sentiment_model import analyze_sentiment, load_model
from models.prediction_model import train_model

st.title("📄 AI Report Generator")

ticker = st.text_input("Enter Stock Ticker", "AAPL")

if st.button("Generate Report"):

    # -------- STOCK DATA --------
    df = get_stock_data(ticker)

    close_col = [col for col in df.columns if "Close" in col][0]
    latest_close = float(df.iloc[-1][close_col])

    # -------- PREDICTION --------
    model_pred = train_model(df)
    pred = model_pred.predict([[latest_close]])

    # -------- SENTIMENT --------
    news_df = load_news_data()
    model_sent = load_model()

    sample_text = news_df["Title"].iloc[0]
    result = analyze_sentiment(sample_text, model_sent)

    sentiment = result[0]['label']
    score = result[0]['score']

    # -------- BUILD REPORT --------
    report = f"""
    📊 AI Financial Report

    Stock: {ticker}
    Latest Price: {latest_close:.2f}

    Prediction: {"UP 📈" if pred[0] == 1 else "DOWN 📉"}

    News Sentiment: {sentiment} (Confidence: {score:.2f})

    Final Suggestion:
    """

    if pred[0] == 1 and sentiment == "positive":
        report += "BUY 📈"
    elif pred[0] == 0 and sentiment == "negative":
        report += "SELL 📉"
    else:
        report += "HOLD ⚖️"

    # Show report
    st.subheader("📄 Generated Report")
    st.text(report)

    # Download option
    st.download_button(
        label="⬇️ Download Report",
        data=report,
        file_name=f"{ticker}_report.txt",
        mime="text/plain"
    )
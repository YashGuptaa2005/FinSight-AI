import streamlit as st
from utils.fetch_stock import get_stock_data
from utils.fetch_news import load_news_data
from models.sentiment_model import analyze_sentiment, load_model
from models.prediction_model import train_model

st.title("📄 AI Report Generator")

ticker = st.text_input("Enter Stock Ticker", "AAPL")

if st.button("Generate Report"):

    df = get_stock_data(ticker)
    df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

    close = df["Close"]
    latest = float(close.iloc[-1])

    model_pred = train_model(df)
    pred = model_pred.predict([[latest]])

    news = load_news_data()
    model_sent = load_model()

    result = analyze_sentiment(news["Title"].iloc[0], model_sent)

    sentiment = result[0]['label']
    score = result[0]['score']

    # -------- METRICS --------
    col1, col2, col3 = st.columns(3)

    col1.metric("Price", f"{latest:.2f}")
    col2.metric("Prediction", "UP" if pred[0] == 1 else "DOWN")
    col3.metric("Sentiment", sentiment.upper())

    st.markdown("---")

    # -------- FINAL DECISION --------
    st.subheader("🤖 Final Recommendation")

    if pred[0] == 1 and sentiment == "positive":
        decision = "BUY 📈"
        st.success(decision)
    elif pred[0] == 0 and sentiment == "negative":
        decision = "SELL 📉"
        st.error(decision)
    else:
        decision = "HOLD ⚖️"
        st.warning(decision)

    st.markdown("---")

    # -------- REPORT TEXT --------
    report = f"""
Stock: {ticker}
Price: {latest:.2f}
Prediction: {"UP" if pred[0] == 1 else "DOWN"}
Sentiment: {sentiment} ({score:.2f})
Decision: {decision}
"""

    st.text_area("📄 Report", report, height=200)

    st.download_button(
        "⬇️ Download Report",
        data=report,
        file_name=f"{ticker}_report.txt"
    )
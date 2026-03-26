import streamlit as st
from utils.fetch_news import load_news_data
from models.sentiment_model import analyze_sentiment, load_model

st.title("📰 Financial News Sentiment Analysis")

# Load data
df = load_news_data()

# Load model once
model = load_model()

# Preview
st.subheader("📊 News Data Preview")
st.dataframe(df.head())

# Input
user_input = st.text_area("Enter custom news headline:")

if st.button("Analyze Sentiment"):

    if user_input:
        text = user_input
    else:
        text = df["Title"].iloc[0]

    result = analyze_sentiment(text, model)

    st.subheader("🔍 Sentiment Result")

    label = result[0]['label']
    score = result[0]['score']

    if label == "positive":
        st.success(f"Positive 📈 (Confidence: {score:.2f})")
    elif label == "negative":
        st.error(f"Negative 📉 (Confidence: {score:.2f})")
    else:
        st.warning(f"Neutral 😐 (Confidence: {score:.2f})")
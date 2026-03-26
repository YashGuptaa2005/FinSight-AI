import streamlit as st
from models.sentiment_model import analyze_sentiment, load_model

st.title("📰 News Sentiment Analysis")

text = st.text_area("Enter News Headline")

if st.button("Analyze Sentiment"):

    model = load_model()
    result = analyze_sentiment(text, model)

    label = result[0]['label']
    score = result[0]['score']

    st.markdown("---")
    st.subheader("🔍 Sentiment Result")

    col1, col2 = st.columns(2)
    col1.metric("Sentiment", label.upper())
    col2.metric("Confidence", f"{score:.2f}")

    if label == "positive":
        st.success("📈 Positive News")
    elif label == "negative":
        st.error("📉 Negative News")
    else:
        st.warning("😐 Neutral News")
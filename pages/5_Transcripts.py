import streamlit as st
import os
from models.sentiment_model import analyze_sentiment, load_model

st.title("🧠 CEO Transcript Analysis")

# Load model once
model = load_model()

# Folder path
TRANSCRIPT_PATH = "data/transcripts"

# List companies
companies = os.listdir(TRANSCRIPT_PATH)

selected_company = st.selectbox("Select Company", companies)

# Get files for selected company
company_path = os.path.join(TRANSCRIPT_PATH, selected_company)
files = os.listdir(company_path)

selected_file = st.selectbox("Select Transcript File", files)

# Read file
file_path = os.path.join(company_path, selected_file)

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Show preview
st.subheader("📄 Transcript Preview")
st.write(text[:1000])

if st.button("Analyze Transcript"):

    # Limit text size (important for model)
    chunk = text[:512]

    result = analyze_sentiment(chunk, model)

    st.subheader("🔍 Sentiment Result")

    label = result[0]['label']
    score = result[0]['score']

    if label == "positive":
        st.success(f"Positive 📈 (Confidence: {score:.2f})")
    elif label == "negative":
        st.error(f"Negative 📉 (Confidence: {score:.2f})")
    else:
        st.warning(f"Neutral 😐 (Confidence: {score:.2f})")
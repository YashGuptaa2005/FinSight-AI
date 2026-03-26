import streamlit as st
import os
from models.sentiment_model import analyze_sentiment, load_model

st.title("🧠 CEO Transcript Analysis")

model = load_model()

TRANSCRIPT_PATH = "data/transcripts"

companies = os.listdir(TRANSCRIPT_PATH)
selected_company = st.selectbox("Select Company", companies)

company_path = os.path.join(TRANSCRIPT_PATH, selected_company)
files = os.listdir(company_path)

selected_file = st.selectbox("Select File", files)

file_path = os.path.join(company_path, selected_file)

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

tab1, tab2 = st.tabs(["📄 Preview", "🤖 Analysis"])

with tab1:
    st.write(text[:1000])

with tab2:
    if st.button("Analyze Transcript"):

        result = analyze_sentiment(text[:512], model)

        label = result[0]['label']
        score = result[0]['score']

        st.metric("Sentiment", label.upper())
        st.metric("Confidence", f"{score:.2f}")
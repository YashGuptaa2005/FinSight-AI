import streamlit as st

st.title("🏠 Home Dashboard")

st.markdown("### Welcome to FinSight AI 🚀")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    📈 Stock Prediction  
    📰 News Sentiment  
    🧠 Transcript Analysis  
    """)

with col2:
    st.success("""
    🚨 Anomaly Detection  
    💼 Portfolio Insights  
    🤖 AI Advisor  
    """)

st.markdown("---")

st.subheader("✨ About Project")

st.write("""
FinSight AI is a financial intelligence platform that combines machine learning 
and natural language processing to provide insights on stocks, news, and company performance.
""")
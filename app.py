import streamlit as st

st.set_page_config(
    page_title="FinSight AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------- CSS --------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.main {
    background-color: #0e1117;
    color: white;
}
h1, h2, h3 {
    color: #ffffff;
}
.stButton>button {
    border-radius: 12px;
    background-color: #4CAF50;
    color: white;
    font-size: 16px;
    padding: 10px 20px;
}
.stTextInput>div>div>input {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# -------- SIDEBAR --------
st.sidebar.title("🚀 FinSight AI")
st.sidebar.markdown("### AI Financial Dashboard")
st.sidebar.markdown("---")
st.sidebar.info("Select a page")

# -------- MAIN --------
st.title("📊 FinSight AI Dashboard")
st.markdown("### Next-Gen Financial Intelligence System")
st.markdown("---")

st.success("👈 Select a feature from sidebar to begin")
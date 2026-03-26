import streamlit as st
from utils.fetch_stock import get_stock_data

st.title("🏢 Company Overview")

ticker = st.text_input("Enter Company Ticker", "AAPL")

if st.button("Analyze"):

    df = get_stock_data(ticker)

    # Fix columns
    df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

    close = df["Close"]

    # -------- METRICS --------
    col1, col2, col3 = st.columns(3)

    col1.metric("📊 Current Price", f"{close.iloc[-1]:.2f}")
    col2.metric("🔼 High", f"{close.max():.2f}")
    col3.metric("🔽 Low", f"{close.min():.2f}")

    st.markdown("---")

    # -------- TABS --------
    tab1, tab2 = st.tabs(["📈 Stock Chart", "📊 Raw Data"])

    with tab1:
        st.line_chart(df.set_index("Date")["Close"])

    with tab2:
        st.dataframe(df.tail())
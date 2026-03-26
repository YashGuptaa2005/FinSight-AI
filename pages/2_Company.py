import streamlit as st
import pandas as pd
from utils.fetch_stock import get_stock_data

st.title("🏢 Company Analysis")

# Input
ticker = st.text_input("Enter Stock Ticker", "AAPL")

# Button
if st.button("Fetch Data"):
    df = get_stock_data(ticker)

    st.subheader(f"{ticker} Stock Data")

    st.write(df.tail())

    st.line_chart(df.set_index("Date")["Close"])
import streamlit as st
from utils.fetch_stock import get_stock_data
import pandas as pd

st.title("💼 Portfolio Insights")

tickers = st.text_input("Enter Tickers", "AAPL,TSLA,MSFT")

if st.button("Analyze"):

    ticker_list = [t.strip().upper() for t in tickers.split(",")]

    data = []

    for t in ticker_list:
        df = get_stock_data(t)

        df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

        price = float(df["Close"].iloc[-1])

        data.append({"Ticker": t, "Price": price})

    df = pd.DataFrame(data)

    st.dataframe(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Average", f"{df['Price'].mean():.2f}")
    col2.metric("Highest", f"{df['Price'].max():.2f}")
    col3.metric("Lowest", f"{df['Price'].min():.2f}")
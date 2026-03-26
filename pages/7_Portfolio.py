import streamlit as st
from utils.fetch_stock import get_stock_data
import pandas as pd

st.title("💼 Portfolio Insights")

# User input (multiple stocks)
tickers = st.text_input("Enter Stock Tickers (comma separated)", "AAPL,TSLA,MSFT")

if st.button("Analyze Portfolio"):

    ticker_list = [t.strip().upper() for t in tickers.split(",")]

    all_data = []

    for ticker in ticker_list:
        df = get_stock_data(ticker)

        latest_price = float(df.iloc[-1][df.columns[1]])

        all_data.append({
            "Ticker": ticker,
            "Latest Price": latest_price
        })

    portfolio_df = pd.DataFrame(all_data)

    st.subheader("📊 Portfolio Data")
    st.dataframe(portfolio_df)

    st.subheader("📈 Summary")

    avg_price = portfolio_df["Latest Price"].mean()
    max_price = portfolio_df["Latest Price"].max()
    min_price = portfolio_df["Latest Price"].min()

    st.write(f"Average Price: {avg_price:.2f}")
    st.write(f"Highest Price: {max_price:.2f}")
    st.write(f"Lowest Price: {min_price:.2f}")
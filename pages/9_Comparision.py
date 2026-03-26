import streamlit as st
from utils.fetch_stock import get_stock_data

st.title("⚖️ Company Comparison")

tickers = st.text_input("Enter Tickers (comma separated)", "AAPL,TSLA")

if st.button("Compare"):

    ticker_list = [t.strip().upper() for t in tickers.split(",")]

    st.subheader("📈 Stock Comparison")

    combined_df = None

    for ticker in ticker_list:
        df = get_stock_data(ticker)

        # Fix multi-level columns
        df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

        df = df[["Date", "Close"]]
        df = df.rename(columns={"Close": ticker})

        if combined_df is None:
            combined_df = df
        else:
            combined_df = combined_df.merge(df, on="Date")

    combined_df = combined_df.set_index("Date")

    st.line_chart(combined_df)
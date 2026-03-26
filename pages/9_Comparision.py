import streamlit as st
from utils.fetch_stock import get_stock_data

st.title("⚖️ Company Comparison")

tickers = st.text_input("Enter Tickers", "AAPL,TSLA")

if st.button("Compare"):

    ticker_list = [t.strip().upper() for t in tickers.split(",")]

    combined = None

    for t in ticker_list:
        df = get_stock_data(t)

        df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

        df = df[["Date", "Close"]]
        df = df.rename(columns={"Close": t})

        if combined is None:
            combined = df
        else:
            combined = combined.merge(df, on="Date")

    st.line_chart(combined.set_index("Date"))
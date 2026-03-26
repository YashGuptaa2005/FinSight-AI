import yfinance as yf
import pandas as pd

def get_stock_data(ticker="AAPL", start="2020-01-01", end="2024-01-01"):
    data = yf.download(ticker, start=start, end=end)
    data.reset_index(inplace=True)
    return data

if __name__ == "__main__":
    df = get_stock_data("AAPL")
    print(df.head())
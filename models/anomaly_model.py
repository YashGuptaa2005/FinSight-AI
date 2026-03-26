import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_anomalies(df):
    """
    Detect anomalies in stock data
    """

    model = IsolationForest(contamination=0.05)

    df["anomaly"] = model.fit_predict(df[["Close"]])

    return df


# Test
if __name__ == "__main__":
    from utils.fetch_stock import get_stock_data

    df = get_stock_data("AAPL")

    df = detect_anomalies(df)

    print(df[["Date", "Close", "anomaly"]].head())
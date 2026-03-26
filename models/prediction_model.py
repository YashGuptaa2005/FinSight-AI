import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score


def train_model(df):
    """
    Train prediction model
    """

    # Find correct Close column (like 'Close AAPL')
    close_col = [col for col in df.columns if "Close" in col][0]

    # Rename to standard name
    df = df.rename(columns={close_col: "Close"})

    # Dummy target
    df["target"] = np.random.randint(0, 2, size=len(df))

    # ✅ IMPORTANT: use values (remove column names issue)
    X = df[["Close"]].values
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = XGBClassifier()

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)

    print(f"Accuracy: {acc}")

    return model
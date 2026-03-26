import pandas as pd
import re

def clean_text(text):
    """
    Clean text data
    """
    text = str(text)
    text = text.lower()  # lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # remove special chars
    text = re.sub(r'\s+', ' ', text).strip()  # remove extra spaces
    return text


def preprocess_news(df):
    """
    Apply cleaning on news dataset
    """
    if "Title" in df.columns:
        df["clean_text"] = df["Title"].apply(clean_text)
    elif "text" in df.columns:
        df["clean_text"] = df["text"].apply(clean_text)
    
    return df


# Test
if __name__ == "__main__":
    from fetch_news import load_news_data

    df = load_news_data()
    df = preprocess_news(df)

    print(df[["clean_text"]].head())
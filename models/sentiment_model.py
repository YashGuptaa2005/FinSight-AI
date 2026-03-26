from transformers import pipeline

# Load FinBERT model once
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="ProsusAI/finbert"
)

def load_model():
    """
    Return the loaded sentiment model
    """
    return sentiment_pipeline


def analyze_sentiment(text, model):
    """
    Analyze sentiment using FinBERT
    """
    result = model(text[:512])  # limit text length
    return result


# Test (optional)
if __name__ == "__main__":
    model = load_model()

    sample_text = "The company reported strong growth and profits."

    result = analyze_sentiment(sample_text, model)

    print(result)
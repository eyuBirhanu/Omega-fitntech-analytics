"""
Module: sentiment_analysis.py
Description: Applies NLP to classify sentiment of banking reviews.
"""

import pandas as pd  # For data handling
from transformers import pipeline  # Hugging Face library for AI models
import torch  # PyTorch is the engine behind the AI

def load_data(filepath):
    """Loads CSV data into a DataFrame."""
    try:
        df = pd.read_csv(filepath)
        print("Data loaded successfully.")
        return df
    except FileNotFoundError:
        print("File not found. Please run scraper.py first.")
        return None

def analyze_sentiment(df):
    """
    Applies the DistilBERT model to the review text.
    """
    print("Loading Sentiment Model (this may take a moment)...")
    
    # Initialize the specific model requested in the assignment
    sentiment_pipeline = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

    # Define a helper function to process a single text
    def get_sentiment(text):
        # Truncate text to 512 chars because BERT has a limit
        # The model returns a list like [{'label': 'POSITIVE', 'score': 0.99}]
        try:
            result = sentiment_pipeline(str(text)[:512])[0]
            return result['label'], result['score']
        except Exception:
            return "NEUTRAL", 0.0

    print("Applying sentiment analysis to reviews...")
    
    # Apply the function to the 'review_text' column
    # zip(*...) unzips the result into two separate columns
    results = df['review_text'].apply(get_sentiment)
    
    # Create new columns in the DataFrame
    df['sentiment_label'] = [res[0] for res in results]
    df['sentiment_score'] = [res[1] for res in results]

    return df

def main():
    # 1. Load Data
    df = load_data('bank_reviews.csv')
    
    if df is not None:
        # 2. Analyze
        df_analyzed = analyze_sentiment(df)
        
        # 3. Save Results
        output_file = 'bank_reviews_with_sentiment.csv'
        df_analyzed.to_csv(output_file, index=False)
        print(f"Analysis Complete. Saved to {output_file}")

if __name__ == "__main__":
    main()
"""
Module: sentiment_analysis.py
Description: Applies NLP to classify sentiment and extract themes.
"""

import pandas as pd
from transformers import pipeline
from collections import Counter
import re

# 1. Load Data
def load_data(filepath):
    try:
        df = pd.read_csv(filepath)
        print("Data loaded successfully.")
        return df
    except FileNotFoundError:
        print("File not found. Please run scraper.py first.")
        return None

# 2. Sentiment Analysis (Using DistilBERT)
def analyze_sentiment(df):
    print("Loading Sentiment Model...")
    sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    def get_sentiment(text):
        try:
            # Truncate to 512 tokens to prevent crash
            result = sentiment_pipeline(str(text)[:512])[0] 
            return result['label'], result['score']
        except Exception:
            return "NEUTRAL", 0.0

    print("Scoring reviews...")
    results = df['review_text'].apply(get_sentiment)
    df['sentiment_label'] = [res[0] for res in results]
    df['sentiment_score'] = [res[1] for res in results]
    return df

# 3. Thematic Analysis (New Feature)
def extract_themes(text):
    """
    Simple Rule-Based Clustering.
    We look for specific keywords and assign a 'Theme'.
    """
    text = str(text).lower()
    
    # Define keywords for each theme
    themes = {
        'Login/Access': ['login', 'password', 'access', 'otp', 'cant open', 'sign in', 'error'],
        'Performance': ['slow', 'lag', 'stuck', 'loading', 'wait', 'network', 'connect'],
        'Stability': ['crash', 'close', 'bug', 'fix', 'update', 'force stop'],
        'UI/UX': ['interface', 'design', 'look', 'easy', 'confusing', 'hard', 'user friendly'],
        'Transactions': ['transfer', 'money', 'send', 'payment', 'balance', 'transaction']
    }
    
    found_themes = []
    for theme, keywords in themes.items():
        if any(word in text for word in keywords):
            found_themes.append(theme)
            
    if not found_themes:
        return "General"
    return ", ".join(found_themes)

def main():
    df = load_data('bank_reviews.csv')
    if df is not None:
        # Run Sentiment
        df = analyze_sentiment(df)
        
        # Run Thematic Analysis
        print("Extracting themes...")
        df['theme'] = df['review_text'].apply(extract_themes)
        
        # Save
        output_file = 'bank_reviews_analyzed.csv'
        df.to_csv(output_file, index=False)
        print(f"Complete! Data saved to {output_file}")

if __name__ == "__main__":
    main()

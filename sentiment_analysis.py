import pandas as pd 
from transformers import pipeline 
import torch

def load_data(filepath):
    try:
        df = pd.read_csv(filepath)
        print("Data loaded successfully.")
        return df
    except FileNotFoundError:
        print("File not found. Please run scraper.py first.")
        return None

def analyze_sentiment(df):
  
    print("Loading Sentiment Model (this may take a moment)...")
    
    sentiment_pipeline = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

    def get_sentiment(text):
        try:
            result = sentiment_pipeline(str(text)[:512])[0]
            return result['label'], result['score']
        except Exception:
            return "NEUTRAL", 0.0

    print("Applying sentiment analysis to reviews...")
    
    results = df['review_text'].apply(get_sentiment)
    
    df['sentiment_label'] = [res[0] for res in results]
    df['sentiment_score'] = [res[1] for res in results]

    return df

def main():
    df = load_data('bank_reviews.csv')
    
    if df is not None:
        df_analyzed = analyze_sentiment(df)
        
        output_file = 'bank_reviews_with_sentiment.csv'
        df_analyzed.to_csv(output_file, index=False)
        print(f"Analysis Complete. Saved to {output_file}")

if __name__ == "__main__":
    main()

"""
Module: topic_modeling.py
Description: Extracts keywords and assigns themes to reviews using TF-IDF.
"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(df, bank_name):
    """
    Finds top keywords for a specific bank to identify themes.
    """
    # Filter reviews for this bank
    subset = df[df['bank'] == bank_name]['review_text'].astype(str)
    
    if len(subset) < 10:
        return []

    # Initialize TF-IDF (Ignore common English words like 'the', 'and')
    vectorizer = TfidfVectorizer(stop_words='english', max_features=10, ngram_range=(1, 2))
    
    try:
        matrix = vectorizer.fit_transform(subset)
        feature_names = vectorizer.get_feature_names_out()
        return feature_names
    except ValueError:
        return []

def assign_theme_rule_based(text):
    """
    Assigns a theme based on simple keywords found in the text.
    This is a 'Rule-Based' approach, which is robust for simple tasks.
    """
    text = str(text).lower()
    
    if any(x in text for x in ['crash', 'close', 'stuck', 'slow', 'loading', 'bug', 'error']):
        return "Stability & Performance"
    elif any(x in text for x in ['login', 'password', 'otp', 'sms', 'code', 'access']):
        return "Authentication/Login"
    elif any(x in text for x in ['ui', 'interface', 'design', 'look', 'user friendly', 'menu']):
        return "User Interface (UI)"
    elif any(x in text for x in ['transfer', 'send', 'money', 'transaction', 'payment']):
        return "Transactions"
    elif any(x in text for x in ['service', 'support', 'staff', 'branch', 'call']):
        return "Customer Service"
    else:
        return "General/Other"

def main():
    print("Loading sentiment data...")
    try:
        df = pd.read_csv('bank_reviews_with_sentiment.csv')
    except FileNotFoundError:
        print("Error: Run sentiment_analysis.py first!")
        return

    print("Extracting keywords per bank (for Report Insights)...")
    banks = df['bank'].unique()
    for bank in banks:
        keywords = extract_keywords(df, bank)
        print(f"Top Keywords for {bank}: {list(keywords)}")

    print("Assigning Themes to reviews...")
    df['theme'] = df['review_text'].apply(assign_theme_rule_based)

    # Save the final processed dataset
    output_file = 'bank_reviews_final.csv'
    df.to_csv(output_file, index=False)
    print(f"Thematic Analysis Complete. Saved to {output_file}")

if __name__ == "__main__":
    main()
"""
Module: visualization.py
Description: Generates charts for the final report.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    try:
        df = pd.read_csv('bank_reviews_analyzed.csv')
    except FileNotFoundError:
        print("Error: CSV not found. Run sentiment_analysis.py first.")
        return

    # Set the visual style
    sns.set_theme(style="whitegrid")

    # --- PLOT 1: Sentiment Count ---
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='bank', hue='sentiment_label', palette='viridis')
    plt.title('Sentiment Distribution by Bank')
    plt.xlabel('Bank Name')
    plt.ylabel('Number of Reviews')
    plt.tight_layout()
    plt.savefig('sentiment_chart.png') # Saves the image
    print("Generated: sentiment_chart.png")

    # --- PLOT 2: Average Rating ---
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x='bank', y='rating', estimator='mean', errorbar=None, palette='coolwarm')
    plt.title('Average Star Rating')
    plt.ylabel('Stars (1-5)')
    plt.ylim(0, 5)
    plt.tight_layout()
    plt.savefig('rating_chart.png') # Saves the image
    print("Generated: rating_chart.png")

    # --- PLOT 3: Common Issues (Themes) ---
    # Look only at Negative reviews to find pain points
    neg_reviews = df[df['sentiment_label'] == 'NEGATIVE']
    
    if not neg_reviews.empty:
        plt.figure(figsize=(10, 6))
        # Count the top 10 themes in negative reviews
        top_issues = neg_reviews['theme'].value_counts().head(10)
        sns.barplot(x=top_issues.values, y=top_issues.index, palette='magma')
        plt.title('Top Complaints (Themes in Negative Reviews)')
        plt.xlabel('Count')
        plt.tight_layout()
        plt.savefig('themes_chart.png') # Saves the image
        print("Generated: themes_chart.png")
    else:
        print("No negative reviews found to plot themes.")

if __name__ == "__main__":
    main()
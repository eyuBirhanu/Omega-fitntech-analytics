"""
Module: scraper.py
Description: Scrapes user reviews from Google Play Store for CBE, BOA, and Dashen Bank.
Author: Data Analyst (You)
Date: 2025-11-30
"""

import pandas as pd  # Library for DataFrames (tables)
from google_play_scraper import reviews, Sort  # Library to fetch Play Store data
from datetime import datetime  # To handle date formats

# 1. Configuration: Define the target apps and their IDs
# These IDs are found in the Google Play URL after 'id='
APPS = {
    'CBE': 'com.combanketh.mobilebanking',
    'BOA': 'com.bankofabyssinia.mobilebanking',
    'Dashen': 'com.dashenbank.mobile'
}

def scrape_reviews(bank_name, app_id, count=500):
    """
    Scrapes reviews for a single app.
    Args:
        bank_name (str): Name of the bank.
        app_id (str): Google Play App ID.
        count (int): Number of reviews to fetch.
    Returns:
        list: A list of dictionaries containing review data.
    """
    print(f"Starting scrape for {bank_name}...")
    
    try:
        # Fetch reviews using the library
        result, _ = reviews(
            app_id,
            lang='en',           # Language: English
            country='et',        # Country: Ethiopia
            sort=Sort.NEWEST,    # Sort by: Newest first
            count=count          # Quantity: Target 500 to ensure we meet the 400 minimum
        )
        
        # Add the bank name to each review so we can distinguish them later
        for r in result:
            r['bank_name'] = bank_name
            r['source'] = 'Google Play'
            
        print(f"Successfully fetched {len(result)} reviews for {bank_name}.")
        return result

    except Exception as e:
        print(f"Error scraping {bank_name}: {e}")
        return []

def main():
    """
    Main execution function.
    """
    all_data = []  # List to hold all reviews from all banks

    # Loop through our dictionary of apps
    for bank, app_id in APPS.items():
        bank_data = scrape_reviews(bank, app_id)
        all_data.extend(bank_data)  # Combine lists

    # Convert list to Pandas DataFrame
    df = pd.DataFrame(all_data)

    # Data Cleaning / Preprocessing
    # 1. Select only required columns
    required_columns = ['content', 'score', 'at', 'bank_name', 'source']
    df = df[required_columns]

    # 2. Rename columns to match assignment specs
    df.rename(columns={
        'content': 'review_text',
        'score': 'rating',
        'at': 'review_date',
        'bank_name': 'bank'
    }, inplace=True)

    # 3. Normalize Date (remove time, keep YYYY-MM-DD)
    df['review_date'] = pd.to_datetime(df['review_date']).dt.date

    # 4. Handle duplicates
    initial_count = len(df)
    df.drop_duplicates(inplace=True)
    print(f"Removed {initial_count - len(df)} duplicate rows.")

    # Save to CSV
    output_file = 'bank_reviews.csv'
    df.to_csv(output_file, index=False)
    print(f"Process Complete. Data saved to {output_file}")

# This ensures the script only runs if executed directly
if __name__ == "__main__":
    main()
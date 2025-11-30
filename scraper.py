import pandas as pd  # Library for DataFrames (tables)
from google_play_scraper import reviews, Sort  # Library to fetch Play Store data
from datetime import datetime  # To handle date formats

APPS = {
    'CBE': 'com.combanketh.mobilebanking',
    'BOA': 'com.bankofabyssinia.mobilebanking',
    'Dashen': 'com.dashenbank.mobile'
}

def scrape_reviews(bank_name, app_id, count=500):
    print(f"Starting scrape for {bank_name}...")
    
    try:
        result, _ = reviews(
            app_id,
            lang='en',         
            country='et',      
            sort=Sort.NEWEST,  
            count=count          
        )
        
        for r in result:
            r['bank_name'] = bank_name
            r['source'] = 'Google Play'
            
        print(f"Successfully fetched {len(result)} reviews for {bank_name}.")
        return result

    except Exception as e:
        print(f"Error scraping {bank_name}: {e}")
        return []

def main():

    all_data = []  # List to hold all reviews from all banks

    for bank, app_id in APPS.items():
        bank_data = scrape_reviews(bank, app_id)
        all_data.extend(bank_data)  # Combine lists

    df = pd.DataFrame(all_data)

    required_columns = ['content', 'score', 'at', 'bank_name', 'source']
    df = df[required_columns]

    df.rename(columns={
        'content': 'review_text',
        'score': 'rating',
        'at': 'review_date',
        'bank_name': 'bank'
    }, inplace=True)

    df['review_date'] = pd.to_datetime(df['review_date']).dt.date

    initial_count = len(df)
    df.drop_duplicates(inplace=True)
    print(f"Removed {initial_count - len(df)} duplicate rows.")

    output_file = 'bank_reviews.csv'
    df.to_csv(output_file, index=False)
    print(f"Process Complete. Data saved to {output_file}")

if __name__ == "__main__":
    main()

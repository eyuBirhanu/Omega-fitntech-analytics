# Customer Experience Analytics for Fintech Apps

## Project Overview
This project analyzes customer satisfaction for three major Ethiopian banks (CBE, BOA, Dashen) by scraping and processing user reviews from the Google Play Store. The goal is to identify key drivers of satisfaction and pain points using Natural Language Processing (NLP).

## Features
- **Data Collection**: Scrapes 1,200+ reviews using `google-play-scraper`.
- **Preprocessing**: Cleans data, normalizes dates, and removes duplicates.
- **Sentiment Analysis**: Uses `distilbert-base-uncased-finetuned-sst-2-english` to score reviews.

## Installation
1. Clone the repository:
   ```bash
   git clone <your-repo-link>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Scrape Data:
   ```bash
   python scraper.py
   ```
   Output: `bank_reviews.csv`
2. Run Sentiment Analysis:
   ```bash
   python sentiment_analysis.py
   ```
   Output: `bank_reviews_with_sentiment.csv`

## Methodology
* **Scraping**: Targeted the "Newest" 500 reviews per bank to ensure relevance.
* **NLP**: Utilized a pre-trained Hugging Face transformer model for high-accuracy sentiment detection.

## Author
Eyu Birhanu - Omega Consultancy Data Analyst

---

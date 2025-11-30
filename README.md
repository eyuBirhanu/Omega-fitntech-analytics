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
Install dependencies:
code
Bash
pip install -r requirements.txt
Usage
Scrape Data:
code
Bash
python scraper.py
Output: bank_reviews.csv
Run Sentiment Analysis:
code
Bash
python sentiment_analysis.py
Output: bank_reviews_with_sentiment.csv
Methodology
Scraping: Targeted the "Newest" 500 reviews per bank to ensure relevance.
NLP: Utilized a pre-trained Hugging Face transformer model for high-accuracy sentiment detection.
Author
[Your Name] - Omega Consultancy Data Analyst
code
Code
---

### **Phase 6: Commit and Push to GitHub**

Now that your files are ready (`scraper.py`, `sentiment_analysis.py`, `requirements.txt`, `README.md`, `.gitignore`), let's save them to Git.

1.  **Add files:**
    ```bash
    git add .
    ```
2.  **Commit:**
    ```bash
    git commit -m "feat: implement scraping and basic sentiment analysis pipeline"
    ```
3.  **Push to GitHub:**
    *   Go to GitHub.com -> Create New Repository -> Name it `fintech-reviews-analytics`.
    *   Copy the URL (e.g., `https://github.com/YourUser/fintech-reviews-analytics.git`).
    *   Run these commands in your terminal:
    ```bash
    git branch -M main
    git remote add origin https://github.com/YourUser/fintech-reviews-analytics.git
    git push -u origin main
    ```

---

### **Phase 7: The Interim Report (Quick Guide)**

You need a PDF report (max 4 pages). Open Word/Docs and write these sections:

1.  **Title Page**: "Interim Report: Customer Experience Analytics for Fintech Apps".
2.  **Introduction**:
    *   "Objective: To scrape and analyze Google Play reviews for CBE, BOA, and Dashen to improve customer retention."
    *   "Current Progress: Successfully established the data extraction pipeline and initial sentiment model."
3.  **Data Collection Methodology**:
    *   Tool used: `google-play-scraper`.
    *   Target: 500 reviews per bank (Total ~1500).
    *   Data fields: Review text, Rating, Date, Bank Name.
4.  **Preliminary Findings (Look at your CSV to fill this)**:
    *   "CBE has the highest volume of reviews."
    *   "Initial scan shows frequent mention of 'connection' issues."
5.  **Next Steps**:
    *   "Refine sentiment analysis themes."
    *   "Deploy PostgreSQL database."
    *   "Generate final visualizations."

**Save as PDF** and you are ready to submit!
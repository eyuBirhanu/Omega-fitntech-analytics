# Fintech Customer Experience Analytics 🇪🇹

A data engineering pipeline to scrape, analyze, and visualize customer sentiment for Ethiopian banking apps (CBE, BOA, Dashen) using NLP and PostgreSQL.

## 📌 Project Overview

**Omega Consultancy Challenge:** Analyze user reviews from the Google Play Store to identify key drivers of customer satisfaction and pain points.

**Key Features:**
*   **ETL Pipeline:** Scrapes data → Cleans text → Loads to SQL.
*   **NLP:** Uses Hugging Face Transformers (`DistilBERT`) for sentiment analysis.
*   **Database:** Stores structured data in PostgreSQL.
*   **Visualization:** Generates automated reports on customer sentiment.

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| `scraper.py` | Extracts reviews from Google Play Store. |
| `sentiment_analysis.py` | Applies BERT model and keyword clustering. |
| `db_loader.py` | Connects to PostgreSQL and inserts processed data. |
| `visualization.py` | Generates charts for reporting. |
| `requirements.txt` | List of Python dependencies. |

## 🚀 Setup & Usage

### 1. Prerequisites
*   Python 3.9+
*   PostgreSQL installed and running.

### 2. Installation

```bash
git clone https://github.com/eyuBirhanu/fintech-reviews-analytics.git
cd fintech-reviews-analytics
pip install -r requirements.txt
```

### 3. Database Setup
Create a database named `bank_reviews` in PostgreSQL. Update the `DB_PASS` in `db_loader.py` with your password.

### 4. Running the Pipeline

**Step 1: Scrape Data**
```bash
python scraper.py
```

**Step 2: Analyze Sentiment & Themes**
```bash
python sentiment_analysis.py
```

**Step 3: Load to Database**
```bash
python db_loader.py
```

**Step 4: Generate Reports**
```bash
python visualization.py
```

## 📊 Insights
*   **Top Complaint:** Transaction failures and App Stability.
*   **Sentiment:** ~65% Positive, ~35% Negative.

## 👤 Author
**Eyu Birhanu** - *Data Analyst*
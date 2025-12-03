"""
Module: db_loader.py
Description: Connects to PostgreSQL and inserts the review data.
"""

import pandas as pd
import psycopg2 

# --- CONFIGURATION ---
DB_NAME = "bank_reviews"
DB_USER = "postgres"
DB_PASS = "1234"  
DB_HOST = "localhost"
DB_PORT = "5432"

def create_tables(conn):
    """Creates the tables in the database if they don't exist."""
    cur = conn.cursor()
    
    # 1. Create Banks Table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS banks (
            bank_id SERIAL PRIMARY KEY,
            bank_name VARCHAR(100) UNIQUE
        );
    """)
    
    # 2. Create Reviews Table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            review_id SERIAL PRIMARY KEY,
            bank_id INTEGER REFERENCES banks(bank_id),
            review_text TEXT,
            rating INTEGER,
            review_date DATE,
            sentiment_label VARCHAR(50),
            sentiment_score FLOAT,
            theme VARCHAR(255),
            source VARCHAR(50)
        );
    """)
    conn.commit()
    print("Tables created (or already exist).")

def insert_data(conn, df):
    """Inserts data from DataFrame into SQL."""
    cur = conn.cursor()
    
    # Get unique banks and insert them
    unique_banks = df['bank'].unique()
    bank_map = {} 
    
    for bank in unique_banks:
        # Insert Bank Name safely
        cur.execute("INSERT INTO banks (bank_name) VALUES (%s) ON CONFLICT (bank_name) DO NOTHING;", (bank,))
        conn.commit()
        
        # Get the ID back
        cur.execute("SELECT bank_id FROM banks WHERE bank_name = %s;", (bank,))
        bank_id = cur.fetchone()[0]
        bank_map[bank] = bank_id
        
    print("Banks processed:", bank_map)

    # Insert Reviews
    print("Inserting reviews (this might take a few seconds)...")
    for index, row in df.iterrows():
        # Handle missing themes just in case
        theme_val = row['theme'] if 'theme' in df.columns and pd.notna(row['theme']) else 'General'
        
        cur.execute("""
            INSERT INTO reviews 
            (bank_id, review_text, rating, review_date, sentiment_label, sentiment_score, theme, source)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            bank_map[row['bank']],
            row['review_text'],
            row['rating'],
            row['review_date'],
            row['sentiment_label'],
            row['sentiment_score'],
            str(theme_val),
            'Google Play'
        ))
    
    conn.commit()
    print("Success! All reviews inserted into PostgreSQL.")

def main():
    # 1. Read the CSV file from Task 2
    # Ensure this matches the filename you saved in the previous step
    try:
        df = pd.read_csv('bank_reviews_analyzed.csv')
    except FileNotFoundError:
        print("Error: 'bank_reviews_analyzed.csv' not found.") 
        print("Please run 'sentiment_analysis.py' first!")
        return

    # 2. Connect to Database
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
        )
        print("Connected to PostgreSQL successfully.")
        
        # 3. Run Functions
        create_tables(conn)
        insert_data(conn, df)
        
        conn.close()
        
    except Exception as e:
        print(f"Database Error: {e}")
        print("Did you start the PostgreSQL server? Is the password correct?")

if __name__ == "__main__":
    main()
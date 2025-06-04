# Run this while in the root director of the project to insert stock data into the database
import pandas as pd
import json
import mysql.connector

db_password = json.load(open('secrets.json'))['database_password']

# Read in the stock data downloadable from Alpha Vantage for their tickers
df = pd.read_csv('database/setup/listing_status.csv', usecols=['symbol', 'name', 'exchange', 'assetType', 'ipoDate'])

df.dropna(inplace=True)

df['ipoDate'] = pd.to_datetime(df['ipoDate'], errors='coerce').dt.strftime('%Y-%m-%d')

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password=db_password,
    database='DRIFTBASE'
)

cursor = conn.cursor()

insert_query = """
INSERT IGNORE INTO STOCK (stock_name, ticker, exchange, asset_type, ipo_date)
VALUES (%s, %s, %s, %s, %s);
"""

records = df[['name', 'symbol', 'exchange', 'assetType', 'ipoDate']].values.tolist()

cursor.executemany(insert_query, records)
conn.commit()
conn.close()
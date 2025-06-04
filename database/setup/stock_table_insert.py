# Run this while in the root director of the project to insert stock data into the database
import pandas as pd
import json
import mysql.connector

db_password = json.load(open('secrets.json'))['database_password']

# Read in the stock data downloadable from Alpha Vantage for their tickers
df = pd.read_csv('database/setup/listing_status.csv', usecols=['symbol', 'name', 'exchange', 'assetType', 'ipoDate'])

print(df.head())
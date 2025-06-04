# Run this while in the root director of the project to insert stock data into the database
import pandas as pd
import json
import mysql.connector
import requests
from io import StringIO

# Load in the database password from secrets.json
db_password = json.load(open('secrets.json'))['database_password']

# Fetch stock data from Alpha Vantage
url = "https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=demo"
r = requests.get(url)

# Read the CSV data from the response into a DataFrame
df = pd.read_csv(StringIO(r.text), usecols=['symbol', 'name', 'exchange', 'assetType', 'ipoDate'])

df.dropna(inplace=True) # drop rows with any NaN values
df['ipoDate'] = pd.to_datetime(df['ipoDate'], errors='coerce').dt.strftime('%Y-%m-%d') # Convert ipoDate to string format YYYY-MM-DD

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password=db_password,
    database='DRIFTBASE'
)

cursor = conn.cursor()

# Create the insert query for the STOCK table
insert_query = """
INSERT IGNORE INTO STOCK (stock_name, ticker, exchange, asset_type, ipo_date)
VALUES (%s, %s, %s, %s, %s);
"""

# Conver the DataFrame to a list of tuples for insertion
records = df[['name', 'symbol', 'exchange', 'assetType', 'ipoDate']].values.tolist()

# Execute the insert query with the records, commit the changes, and close the connection
cursor.executemany(insert_query, records)
conn.commit()
conn.close()

print(f"Inserted {len(records)} records into the STOCK table.")
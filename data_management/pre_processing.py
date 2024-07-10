import pymongo
import pandas as pd
import os
import yfinance as yf

# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or select a database
database = client["day_stock_data"]

# Create or select a collectio
collection = database["minute_prices"]

stocks = ['AAPL', 'AMZN', 'GOOG', 'META', 'MRNA', 'MSFT', 'NFLX', 'NVDA', 'PLTR', 'SOFI', 'TSLA']

# The code below downloads minute-by-minute stock data for the specified stocks and inserts the data into the MongoDB collection.
tickerData = yf.download(stocks, start='2024-07-02', end='2024-07-03', interval='1m')
for index, data in tickerData.iterrows():
    timestamp = index
    for ticker in stocks:
        ticker_data = {
            "ticker": ticker,
            "open": data['Open'][ticker],
            "close": data['Close'][ticker],
            "high": data['High'][ticker],
            "low": data['Low'][ticker],
            "volume": data['Volume'][ticker],
            "adj_close": data['Adj Close'][ticker]
        }
        collection.update_one(
            {'timestamp': timestamp},
            {'$push': {'prices': ticker_data}},
            upsert=True
        )

print("Data insertion complete.")

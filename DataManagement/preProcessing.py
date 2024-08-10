import pymongo
import pandas as pd
import os
import yfinance as yf


def addIntraDay(dbName, collectionName, stocks, timeStart, timeEnd, interval):
    '''
    Add intraday stock data to a MongoDB collection.
    :param dbName: The name of the database.
    :param collectionName: The name of the collection.
    :param stocks: A list of stock tickers.
    :param timeStart: The start date for the data.
    :param timeEnd: The end date for the data.
    :param interval: The interval for the data.
    '''
    # Create or select a database
    database = client[dbName]

    # Create or select a collection
    collection = database[collectionName]

    # Download stock data
    tickerData = yf.download(stocks, start=timeStart, end=timeEnd, interval=interval)

    # Insert the data into the MongoDB collection
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


def addPrePost(dbName, collectionName, stocks, timeStart, timeEnd, interval):
    '''
    Add prepost stock data to a MongoDB collection.
    :param dbName: The name of the database.
    :param collectionName: The name of the collection.
    :param stocks: A list of stock tickers.
    :param timeStart: The start date for the data.
    :param timeEnd: The end date for the data.
    :param interval: The interval for the data.
    '''
    # Create or select a database
    database = client[dbName]

    # Create or select a collection
    collection = database[collectionName]

    # Download stock data
    tickerData = yf.download(stocks, start=timeStart, end=timeEnd, interval=interval, prepost=True)

    # Insert the data into the MongoDB collection
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
    
    def showData(dbName, collectionName):
        '''
        Show the data in a MongoDB collection.
        :param dbName: The name of the database.
        :param collectionName: The name of the collection.
        '''
        # Create or select a database
        database = client[dbName]

        # Create or select a collection
        collection = database[collectionName]

        # Find and print all documents in the collection
        documents = collection.find()
        for document in documents:
            print(document)


if __name__ == "__main__":
    # Connect to the MongoDB server
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Stock Data
    stocks = ['AAPL', 'AMZN', 'GOOG', 'META', 'MRNA', 'MSFT', 'NFLX', 'NVDA', 'PLTR', 'SOFI', 'TSLA']

    # stock intraday to a MongoDB collection
    addIntraDay("day_stock_data", "intraday", stocks, "2024-07-02", "2024-07-03", "1m")
    print("Intraday Data inserted.")
    
    # stock prepost data to a mongodb collection
    addPrePost("day_stock_data", "prepost", stocks, "2024-07-02", "2024-07-03", "1m")
    print("PrePost Data inserted.")

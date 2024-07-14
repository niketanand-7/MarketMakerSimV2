import pymongo

# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the database
database = client["day_stock_data"]

# Select the collection
collection = database["minute_prices"]

# Find and print all documents in the collection
documents = collection.find()
print(documents[0])
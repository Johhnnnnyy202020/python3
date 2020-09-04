from pymongo import MongoClient
# pprint library is used to make the output look more pretty

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb+srv://Netflix:Netflix@cluster0.7n1lg.mongodb.net/sample_mflix?retryWrites=true&w=majority')
db = client.sample_mflix


print(db.list_collection_names())
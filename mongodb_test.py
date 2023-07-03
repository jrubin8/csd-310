from pymongo import MongoClient
#importing necessary modules
 
url = "mongodb+srv://admin:admin@cluster0.guokdam.mongodb.net/"
#connecting to MongoDB
client = MongoClient(url)

db = client.pytech
#connecting to the database
print("\n -- Pytech Collection List --")
#since it was stated that the format must match
print("\n", db.list_collection_names())

input("\n \n \nPress the enter key to end the program.")
#a message signalling the end of the program




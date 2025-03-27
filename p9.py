import os
os.system('cls')
import pymongo

user = {
    "name" : "Alice",
    "email" : "alice@gmail.com",
    "age" : 22
}

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['day15Test']
usersListsCollection = db['usersLists']

# user_id=usersListsCollection.insert_one(user)
query_data = usersListsCollection.find_one({})
print(query_data)

for data in query_data:
    print(data)
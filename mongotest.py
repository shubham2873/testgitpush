import pymongo
client = pymongo.MongoClient("mongodb+srv://shubham_2873:Jaiswal123@cluster0.oa0ueu9.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Shubham",
    "email": "shubhamjaiswal3417@gmail.com",
    "surname": "Jaiswal"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
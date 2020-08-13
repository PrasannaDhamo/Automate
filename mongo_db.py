from pymongo import MongoClient

un = input("Username: ")
pwd = input("Password: ")
em = input("Email: ")

client = MongoClient("mongodb://prasanna1411:mathan100@prasanna-mongodb-shard-00-00.wfmy0.gcp.mongodb.net:27017,prasanna-mongodb-shard-00-01.wfmy0.gcp.mongodb.net:27017,prasanna-mongodb-shard-00-02.wfmy0.gcp.mongodb.net:27017/user-db?ssl=true&replicaSet=atlas-1g0i65-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.get_database('user-db')
cl = db.get_collection('user-details')
    
doc = {
    "username" : un,
    "password" : pwd,
    "email" : em
    }

cl.insert_one(doc)




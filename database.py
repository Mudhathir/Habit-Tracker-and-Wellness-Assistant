from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.habit_tracker
    return db

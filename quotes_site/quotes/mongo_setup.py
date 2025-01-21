from pymongo import MongoClient

def get_mongo_client():
    return MongoClient("mongodb://localhost:27017/")

def get_database():
    client = get_mongo_client()
    return client['quotes_db']
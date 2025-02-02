from pymongo import MongoClient

def get_database():
    # Provide the MongoDB connection string
    client = MongoClient("mongodb://localhost:27017/")
    return client["mubashireen"]

db = get_database()

def insert_project_request(request_data):
    requests_collection = db["project_requests"]
    requests_collection.insert_one(request_data)

def read_project_requests():
    requests_collection = db["project_requests"]
    return list(requests_collection.find({}, {"_id": 0}))
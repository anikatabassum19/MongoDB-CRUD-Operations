import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['Dht11Readings']
    collection = db['Readings']
    print("Database Created")

    first_reading = collection.find_one({'temperature':'30'},{'humidity':0,'_id':0})
    
    print(first_reading)
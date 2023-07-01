import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['Dht11Readings']
    collection = db['Readings']
    print("Database Created")

    collection.insert_one(
        {'temperature':'30','humidity':'40'}
    )

    print("Data Inserted")


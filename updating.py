import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['Dht11Readings']
    collection = db['Readings']
    print("Database Created")

    before_update = {'temperature':'30'}
    after_update = {'$set':{'temperature':'10'}}

    collection.update_one(before_update,after_update)
    #update many to change multiple temperature value'

    data = {'temperature':'10'}
    collection.delete_one(data)
    
    
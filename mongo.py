import pymongo

def insertDataMongo(mongo_uri, data):
  client = pymongo.MongoClient(mongo_uri)
  db = client.temperaturesForecast
  municipio = data["Nombre del municipio"]
  collection = db[municipio]
  collection.insert_one(data)

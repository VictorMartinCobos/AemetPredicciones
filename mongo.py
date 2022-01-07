import pymongo

def insertDataMongo(mongo_uri, data):
  client = pymongo.MongoClient(mongo_uri)
  db = client.meteo
  collection = db.temperatures
  query = {"municipio": data["municipio"], "ts": data["ts"]}
  collection.replace_one(query, data, upsert = True)

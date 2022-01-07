#MAIN MODULE
import requests, os, mongo, aemet
from dotenv import load_dotenv

load_dotenv()
api_aemet = os.environ.get("api_aemet")
mongo_uri = os.environ.get("mongo_uri")

def getTemperatures(nombreMunicipio, api_key_aemet, mongo_string):
  jsonMunicipios = aemet.getJsonMunicipios(api_key_aemet)
  idMunicipio = aemet.getIdMunicipio(nombreMunicipio,jsonMunicipios)
  temperaturesForecast = aemet.getTemperatureForecast(nombreMunicipio, idMunicipio, api_key_aemet)
  mongo.insertDataMongo(mongo_string, temperaturesForecast)
  return(temperaturesForecast)


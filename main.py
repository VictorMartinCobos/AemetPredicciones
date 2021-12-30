#MAIN MODULE
import requests, os, mongo, aemet
from dotenv import load_dotenv

load_dotenv()
api_aemet = os.environ.get("api_aemet")
mongo_uri = os.environ.get("mongo_uri")

def getTemperatures(nombreMunicipio, api_key_aemet, mongo_string):
  jsonMunicipios = getJsonMunicipios(api_key_aemet)
  idMunicipio = getIdMunicipio(nombreMunicipio,jsonMunicipios)
  temperaturesForecast = getTemperatureForecast(nombreMunicipio, idMunicipio, api_key_aemet)
  insertDataMongo(mongo_string, temperaturesForecast)
  return(temperaturesForecast)
  
  

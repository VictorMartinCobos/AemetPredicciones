#Functions to obtain hourly temperature forecasts from AEMET
import requests
from datetime import datetime, timedelta

#Get a json with data from every municipality (included its id)
def getJsonMunicipios(api_key):
  url = "https://opendata.aemet.es/opendata/api/maestro/municipios"
  req = requests.get(url, headers = {"api_key": api_key})
  return(req.json())

#Function to get the id of a municipality in a dictionary
def getIdMunicipio(nombreMunicipio, json):
  for i in range(len(json)):
    if json[i]["capital"] == nombreMunicipio:
      return(json[i]["id"])
    
#Function to get temperature forecast from a specific municipality given its id
def getTemperatureForecast(nombreMunicipio, idMunicipio, api_key):
  ini_url = "https://opendata.aemet.es/opendata/api/"
  path = "prediccion/especifica/municipio/horaria/"
  url = ini_url + path + idMunicipio[2:]
  req = requests.get(url, headers = {"api_key": api_key})
  json = req.json()
  
  url2 = json["datos"]
  req2 = requests.get(url2, headers = {"api_key": api_key})
  json2 = req2.json()
  
  temperatures = {"Nombre del municipio": nombreMunicipio,\
  "Fecha de consulta": datetime.utcnow().strftime("%d-%m-%YT%H:%M:%S")}
  ini_dt = datetime.strptime(json2[0]["elaborado"], "%Y-%m-%dT%H:%M:%S")
  for i in range(len(json2[0]["prediccion"]["dia"])):
    for j in range(len(json2[0]["prediccion"]["dia"][i]["temperatura"])):
      h = int(json2[0]["prediccion"]["dia"][i]["temperatura"][j]["periodo"])
      dt = ini_dt.replace(hour = h, minute = 0, second = 0) + timedelta(days = i)
      str_dt = dt.strftime("%d-%m-%YT%H:%M:%S")
      temperature = int(json2[0]["prediccion"]["dia"][i]["temperatura"][j]["value"])
      temperatures[str_dt] = temperature
  
  return(temperatures)


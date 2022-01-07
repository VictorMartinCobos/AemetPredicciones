#Functions to obtain hourly temperature forecasts from AEMET
import requests, datetime

#Get a json with data from every municipality (included its id)
def getJsonMunicipios(api_key):
  url = "https://opendata.aemet.es/opendata/api/maestro/municipios"
  resp = requests.get(url, headers = {"api_key": api_key})
  return(resp.json())

#Function to get the id of a municipality in a dictionary
def getIdMunicipio(nombre, municipios):
  for municipio in municipios:
    if municipio["capital"] == nombre:
      return(municipio["id"][2:])

#Function to get temperature forecast from a specific municipality given its id
def getTemperatureForecast(nombreMunicipio, idMunicipio, api_key):
  ini_url = "https://opendata.aemet.es/opendata/api/"
  path = "prediccion/especifica/municipio/horaria/"
  url = ini_url + path + idMunicipio
  headers = {"api_key": api_key}
  
  resp = requests.get(url, headers)
  if resp.status_code != 200:
    raise Exception("Status code:", resp.status_code, "Body:", resp.text)
  
  resp_json = resp.json()
  if resp_json["estado"] != 200:
    raise Exception(resp_json)
  
  url2 = resp_json["datos"]
  
  resp2 = requests.get(url2, headers)
  if resp2.status_code != 200:
    raise Exception("Status code:", resp2.status_code, "Body:", resp2.text)
  
  resp_json2 = resp2.json()

  d = datetime.date.today() + datetime.timedelta(days = 1)
  d_datetime = datetime.datetime(d.year, d.month, d.day)
  d_isoformat = d_datetime.isoformat()

  days_list = resp_json2[0]["prediccion"]["dia"]
  
  for day in days_list:
    if day["fecha"] == d_isoformat:
      data = day
  
  temperatures = data["temperatura"]
  
  if len(temperatures) != 24:
    raise Exception("Wrong API response. Didn't return 24 values.")

  temperatures_list = [t["value"] for t in temperatures]

  doc = {
    "municipio": nombreMunicipio,
    "ts": d_datetime,
    "temperatures": temperatures_list
  }
  
  return(doc)


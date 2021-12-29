import requests
import tabulate
#

api_key = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ2aWN0b3JtYXJ0aW5jb2Jvc0BnbWFpbC5jb20iLCJqdGkiOiJiYTVhZDk4Ni05MmMzLTQ2OGUtOGNmZS02ZDJjNGU4ZTdiOTkiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTY0MDc5Nzc3MiwidXNlcklkIjoiYmE1YWQ5ODYtOTJjMy00NjhlLThjZmUtNmQyYzRlOGU3Yjk5Iiwicm9sZSI6IiJ9.YM5e6Q1omNryoxOvyg2AIAWTTw5eXrhvLM6sRo1O5UU"
headers = {"api_key": api_key}

url = "https://opendata.aemet.es/opendata/api/maestro/municipios"
req_municipios = requests.get(url, headers = headers)
json_municipios = req_municipios.json()

def idMunicipio(nombreMunicipio):
  for i in range(len(json_municipios)):
    if json_municipios[i]["capital"] == nombreMunicipio:
      return(json_municipios[i]["id"])
  else:
    print("No se encontraron resultados")
    
idConsultada = idMunicipio(municipioConsultado)

url2 = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/horaria/" + idConsultada[2:]

req = requests.get(url2, headers = headers)
json2 = req.json()



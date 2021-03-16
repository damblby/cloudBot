import json
import requests

def index(query):
    resp = requests.post("https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/postal_unit", 
    headers = {"Content-Type":"application/json", "Accept": "application/json", 
    "Authorization": "Token 0036fbc613dd234976ca70a6fe1e05341c9eaef3"},
    json = {"query":query})
    return resp.json()["suggestions"][0]["unrestricted_value"]
   

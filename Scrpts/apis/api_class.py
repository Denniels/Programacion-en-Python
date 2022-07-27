import requests, json
import pandas as pd

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?sol=1000&api_key=I1n7ru8DjxuiUdc5saiGiFJfKFo2ZrbNAHwiUzdc" 

def request(url):
    payload = ""
    headers = headers = {"api_key" : "I1n7ru8DjxuiUdc5saiGiFJfKFo2ZrbNAHwiUzdc"}
    response = requests.request("GET",url, data = payload, headers = headers)
    return json.loads(response.text)

results = request(url)

z=[]

for i in range(25):
    x = results["latest_photos"][i]["img_src"]
    z.append(x)

print(z)
import requests, json

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?sol=10"

headers = {"x-api-key": "I1n7ru8DjxuiUdc5saiGiFJfKFo2ZrbNAHwiUzdc"}

response = requests.get(url, headers=headers)

result = json.loads(response.text)

results = request(url)
z=[]
for i in range(25):
    x= results["latest_photos"][i]["img_src"]
    z.append(x)
    
#print(result)
#print(result[0:300])
#print(len(result))
#print(type(result))
#print(type(result.keys()))
#print(result.items())
#print(response.status_code)
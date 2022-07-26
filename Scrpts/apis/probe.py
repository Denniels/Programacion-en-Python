
import requests, json

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos'

'''{"title":"Cambio de post",
                "body": "Este es un cambio en el post 20", 
                "userId":"d.mardones.s@gmail.com",
                }'''

playloads = {'Authorization' :'I1n7ru8DjxuiUdc5saiGiFJfKFo2ZrbNAHwiUzdc'}
headers = {'Content-type':'Application/json'}

response = requests.request('GET',  url, data = playloads, headers = headers)
result = json.loads(response.text)

#print(response.text)
#print(headers)
print(type(result))
print(result)
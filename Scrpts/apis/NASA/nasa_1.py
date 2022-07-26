import requests, json

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos"

headers = {"x-api-key": "I1n7ru8DjxuiUdc5saiGiFJfKFo2ZrbNAHwiUzdc"}

response = requests.get(url, headers=headers)
#result = json.loads(response.text)
result = json.loads(response.text)

for key in result:

    print(key, ":", result[key])
    print(key,'\n')
    print(type(result),'\n')
    print(result.values(),'\n')
    print(type(result.values()),'\n')
    dic = result.values()
    print(result.keys(),'\n')
    print(dic,'\n')
    print(type(dic),'\n')

#print(result)
#print(type(result))
#print(result[0:300])
#print(len(result))
#print(type(result))
#print(type(result.keys()))
#print(result.items())
#print(response.status_code)
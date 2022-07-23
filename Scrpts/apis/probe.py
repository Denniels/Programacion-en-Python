
import requests, json

url = 'https://reqres.in/api/users'

playloads = ''
headers = {'Content-type':'Application/json'}

response = requests.request('GET',  url, headers = headers, data = playloads)
result = json.loads(response.text)

#print(response.text)
#print(headers)
print(type(result))
print(result)
print(result.values())
print(result.items())

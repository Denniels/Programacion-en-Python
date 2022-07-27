from urllib import response
import requests, json
import pandas as pd

url = 'https://httpbin.org/get'#'https://reqres.in/api/users'

payload = {}
headers ={}

response = requests.request('GET', url, headers=headers, data = payload)
result = json.loads(response.text)

for name in enumerate(result):
    print(name[0:2])
    #print(type(name))


#print (response)
#print (response.text)
#print (type(response))
#print (result)
print (type(result))
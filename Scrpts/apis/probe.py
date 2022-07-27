
import requests, json

url = 'https://reqres.in/api/users'

'''{"title":"Cambio de post",
                "body": "Este es un cambio en el post 20"
                }'''

playloads = '''{"title":"primer post",
                "body": "Este es el primer post"
                }'''
headers = {'Content-type':'Application/json'}

response = requests.request('GET',  url, data = playloads, headers = headers)
result = json.loads(response.text)

#print(response.text)
#print(headers)
print(type(result))
print(result)
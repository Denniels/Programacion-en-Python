from urllib import response
import requests, json
from string import Template

html_template = Template('''<!DOCTYPE html>
                            <html>
                            <head>
                            <title>Curiosity photos</title>
                            </head>
                            <body>

                            <h1>25 Curiosity photos</h1>   

                            $body

                            </body>
                            </html>''')

url = 'https://reqres.in/api/users'

payload = {}
headers ={}

response = requests.request('GET', url, headers=headers, data = payload)
result = json.loads(response.text)

user_data = result['data']
del user_data[5]

created_user = {'id': 6, 'email': 'ignacio.garcia@reqres.in', 'first_name': 'Ignacio', 'last_name': 'Garcia'}

print(f'{user_data}\n')

user_data.append(created_user)
print(user_data)

print(type(user_data))
print(len(user_data))

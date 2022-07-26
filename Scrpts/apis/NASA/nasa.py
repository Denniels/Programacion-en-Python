import requests, json

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos'

playloads = ''
headers = {'x-api-key": "I1n7ru8DjxuiUdc5saiGiFJfKFo2ZrbNAHwiUzdc'}

response = requests.request('GET',  url, headers = headers, data = playloads)
result = json.loads(response.text)
print(result)

'''# import requests module
import requests

# Making a get request
r = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos')
# print request object
'''


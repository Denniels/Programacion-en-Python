import requests, json

url = 'https://api.nasa.gov/planetary/apod?api_key=FktVqNaxJQ0lxJGNlfK4GIgGvyGsIXlccvu1hsAU'

playloads = ''
headers = {'Content-type':'Application/json'}

response = requests.request('GET',  url, headers = headers, data = playloads)
result = json.loads(response.text)

print(type(result))
print(result)
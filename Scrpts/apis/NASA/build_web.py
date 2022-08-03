from string import Template
import requests
import json

html_template = Template('''<!DOCTYPE html>
                            <html>
                            <head>
                            <title>Curiosity photos</title>
                            </head>
                            <body>

                            <h1>25 Curiosity photos</h1>   

                            $body

                            </body>
                            </html>
                        ''')

def request(url):
    payload = ""
    headers = headers = {"api_key" : "gWUcmw9gZkOevaD6ZXAzCyORwAhLHV7Nq9A4lUdg"}
    response = requests.request("GET",url, data = payload, headers = headers)
    return json.loads(response.text)

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key=gWUcmw9gZkOevaD6ZXAzCyORwAhLHV7Nq9A4lUdg" #sol=25&

results = request(url)
print(results)
z=[]

for i in range(25):
    x= results["latest_photos"][i]["img_src"]
    z.append(x)

def build_web_page(html_template):
    img_template = Template('<img src="$url">')
    texto_img = ''
    for url in z:
        texto_img += img_template.substitute(url = url) +'\n'

    html = html_template.substitute(body = texto_img)

    with open('output.html', 'w') as f:
        f.write(html)
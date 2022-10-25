import requests, json, os, webbrowser, time
from string import Template

html_template = Template('''<!DOCTYPE html>
                            <html>
                            <head>
                            <title>Curiosity Photos</title>
                            </head>
                            <body>

                            <h1>25 Curiosity photos</h1>   

                            $body

                            </body>
                            </html>''')

def request(url):
    payload = ""
    headers = headers = {"api_key" : "RcHSlmsABnzu9xCcjQhQnadBUVP71DrVUXqGUHAf"}
    response = requests.request("GET",url, data = payload, headers = headers)
    return json.loads(response.text)

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key=RcHSlmsABnzu9xCcjQhQnadBUVP71DrVUXqGUHAf'

results= request(url)

z=[]
for i in range(25):
    x= results["latest_photos"][i]["img_src"]
    z.append(x)

def build_web_page(html_template):
    img_template = Template('<img src="$url"width=50%>')
    texto_img = ''
    for url in z:
        texto_img += img_template.substitute(url = url) +'\n'

    html = html_template.substitute(body = texto_img)

    with open('output.html', 'w') as f:
        f.write(html)
    webbrowser.open(f'output.html')
    time.sleep(5)
    os.remove(f'output.html')

build_web_page(html_template)
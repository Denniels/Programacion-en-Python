from string import Template
import requests, json

def request(url):
    payload = ""
    headers = headers = {"api_key" : "I1n7ru8DjxuiUdc5saiGiFJfKFo2ZrbNAHwiUzdc"}
    response = requests.request("GET",url, data = payload, headers = headers)
    return json.loads(response.text)

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?sol=25&api_key=I1n7ru8DjxuiUdc5saiGiFJfKFo2ZrbNAHwiUzdc"

results = request(url)

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
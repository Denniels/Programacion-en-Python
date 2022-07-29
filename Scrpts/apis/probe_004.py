import requests, json
from string import Template

html_template = Template('''<!DOCTYPE html>
                            <html>
                            <head>
                            <title>Fotos de aves</title>
                            </head>
                            <body>

                            <h1>Fotos de aves</h1>   

                            $body

                            </body>
                            </html>''')

url = 'https://aves.ninjas.cl/api/birds'

playloads = {}
headers = {'Content-type':'Application/json'}

response = requests.request('GET',  url, data = playloads)
result = json.loads(response.text)

print(type(result))
print(len(result))
#print(result[5]['images']['full'])
#print(result)

z=[]
for i in range(5):
    x= result[i]['images']['full']
    z.append(x)
'''
h=[]
for j in range(5):
    w= result[j]['name']['spanish']
    h.append(w)

g=[]
for k in range(5):
    u= result[k]['name']['english']
    g.append(u)'''


#SSSprint(f'{z}"\n"{h}"\n"{g}')

def build_web_page(html_template):
    img_template = Template('<img src="$url">')
    texto_img = ''
    for url in z:
        texto_img += img_template.substitute(url = url) +'\n'

    html = html_template.substitute(body = texto_img)

    with open('output.html', 'w') as f:
        f.write(html)

build_web_page(html_template)

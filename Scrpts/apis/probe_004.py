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

z=[]
for i in range(15):
    x= result[i]['images']['full']
    z.append(x)

h=[]
for j in range(15):
    w= result[j]['name']['spanish']
    h.append(w)

g=[]
for k in range(15):
    u= result[k]['name']['english']
    g.append(u)


#print(f'{z}"\n"{h}"\n"{g}')

def build_web_page(html_template):
    img_template = Template('<img src="$url">')
    h_template = Template('<p>$url</p>')
    g_template = Template('<p>$url</p>')
    texto_img = ''
    texto_h = ''
    texto_g = ''

    for url in z:
        texto_img += img_template.substitute(url = url) +'\n'
    for url in h:
        texto_h += h_template.substitute(url = url) +'\n'
    for url in g:
        texto_g += g_template.substitute(url = url) +'\n'

    html = html_template.substitute(body = texto_img)
    html1 = html_template.substitute(body = texto_h)
    html2 = html_template.substitute(body = texto_g)

    with open('output.html', 'w') as f:
        f.write(html)
        f.write(html1)
        f.write(html2)

build_web_page(html_template)

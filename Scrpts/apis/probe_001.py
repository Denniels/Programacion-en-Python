import requests, json

def req(metodo,url,data = {}):
    '''
    Parametros:
    1.- metodo: Resibe un str, con distintos valores de la funcion request,
    que serian: 'GET' 'PUT' 'POST' 'DELETE'
    2.- url: Recive un str, con la direccion http para conectarse a la api
    3.- data: Para colocar nueva data em los parametros payload del request.

    Retornara un diccionario con la data del requerimiento request
    '''
    return json.load(requests.request(metodo, url = url, data = data).text)


def del_req():
    url = url + f'/{id}'
    print(url)
    return requests.request('DELETE',)

def build_web_page():
    pass
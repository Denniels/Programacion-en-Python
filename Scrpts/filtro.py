import sys

valor_consulta = int(sys.argv[1])
arg2 = ''

if len(sys.argv) <= 2:
    arg2 = 'mayor'
elif sys.argv[2] == 'menor':
    arg2 = str('menor')
elif sys.argv[2] == 'mayor':
    arg2 = 'mayor'
else:
    print('Lo sentimos, no es una operación válida')

precios = {'Notebook': 700000,
           'Teclado': 25000,
           'Mouse': 12000,
           'Monitor': 250000,
           'Escritorio': 135000,
           'Tarjeta de Video': 1500000}

def filtrar_mayor(diccionario, valor_consulta):
    filtro = {k:v for k,v in diccionario.items() if v > valor_consulta}
    return filtro.keys()

def filtrar_menor(diccionario, valor_consulta):
    filtro1 = {j:l for j,l in diccionario.items() if l < valor_consulta}
    return filtro1.keys()

if arg2 == 'mayor':
    print('los productos mayores al umbral son: ',filtrar_mayor(precios, valor_consulta))

elif arg2 == 'menor':
    print('los productos menores al umbral son: ',filtrar_menor(precios, valor_consulta))
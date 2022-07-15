'''
Se solicita devolver un informe resumido que exponga los meses que superan un cierto
umbral. El programa mayor_a.py debe retornar un diccionario con el mes y el valor
asociado siempre y cuando superen el umbral especificado.
Ejemplo:
python mayor_a.py 40000
{'Mayo': 81000, 'Agosto': 41200, 'Noviembre': 91000}
'''

from sys import argv

consulta = int(argv[1])

resultado = {}

ventas = {"Enero": 15000,
          "Febrero": 22000,
          "Marzo": 12000,
          "Abril": 17000,
          "Mayo": 81000,
          "Junio": 13000,
          "Julio": 21000,
          "Agosto": 41200,
          "Septiembre": 25000,
          "Octubre": 21500,
          "Noviembre": 91000,
          "Diciembre": 21000,}


for mes in ventas.keys():
    if ventas.get(mes) > consulta:
        resultado[mes]=ventas.get(mes)

print(resultado)



'''for i in ventas:
    if ventas.get(i) > consulta:
        print(i, ventas.get(i))'''

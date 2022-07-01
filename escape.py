'''
La velocidad de escape de un planeta se define como la mínima velocidad necesaria para
salir de un planeta venciendo la gravedad.
La velocidad de escape se calcula mediante la siguiente fórmula:

        V = la raiz cuadrada de (2 * (g * r))
 
Donde:
V: corresponde a la Velocidad de Escape en [m/s].
g: corresponde a la constante gravitacional en [m/s2].
r: Corresponde al radio del planeta en [m].

Se solicita crear un script escape.py que permita calcular la velocidad de escape
ingresando como datos de entradas el radio r y la constante g. Los datos de entrada
deben ingresarse de manera interactiva utilizando la función input().
(5 Puntos)
'''
# importamos libreria para usar la funcion sqrt() o raiz cuadrada
from math import sqrt
# Definición de variables de entrada y consultas a usuario
gravitacional = float(input("Ingrese la constante gravitacional en m/s2: "))
radio = int(input("Ingrese el radio de la tierra en Km: "))
radio_metros = radio * 1000

# Proceso
velosidad_escape = sqrt(2*(gravitacional * radio_metros))

# Variable con funcion round para calibrar la salida esperada
velosidad = round(velosidad_escape, 2)

# Salida
print(f"La velocidad de escape es {velosidad} [m/s]")